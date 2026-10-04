---
name: three.js
summary: Library for drawing 3D in a web page. Use for a 3D piece at the top of an ordinary site, or a viewer where a product or model is turned by hand. Setup with no build step, what a mockup opened from a folder can and cannot load, and what 3D pages usually forget.
detect: ["three.module", "from 'three'", "from \"three\"", "three/addons", "import('three')"]
version: 0.186.1
checked: 2026-10-03
source: https://threejs.org/docs/ and https://threejs.org/manual/
---

# three.js

A library that draws 3D scenes into a `<canvas>` using the graphics card. It is large, changes monthly (the version number goes up by one each release, and things are renamed or removed between releases), and does nothing for you about sizing, pausing, accessibility or fallbacks. Pin the version and re-run the tests when moving to a newer one.

This entry covers setup and what every 3D page needs, with two uses in mind: **a 3D piece on an ordinary page** and **a viewer where one object is turned by dragging**. `three-scenes.md` adds what a full scene or game needs: crowds, more than one view, a camera that follows, picking, labels and keys.

Everything inside the canvas is invisible to the page: there are no elements in it to pin a note to, nothing for a screen reader to find, and nothing the skill's contrast check can see. See "Describing a scene" in `references/context-format.md` for how a blueprint records what is in one.

## Use it properly

In the `<head>`, an import map that pins the version. Add-ons will not load without it:

```html
<script type="importmap">{"imports":{
  "three":"https://cdn.jsdelivr.net/npm/three@0.186.1/build/three.module.js",
  "three/addons/":"https://cdn.jsdelivr.net/npm/three@0.186.1/examples/jsm/"}}</script>
```

In the page, a box with a fixed shape that already holds a fallback picture:

```html
<div class="stage" id="stage"><img src="soap.png" alt="A bar of rosemary soap"></div>
```

And this starter, which was tested as a whole (`tests/three/starter-pattern.html`). It draws sharply, follows the size of its box, runs only while on screen, stays still for people who ask for less motion, gives the canvas a name, and leaves the fallback picture in place if 3D cannot start:

```js
import * as THREE from 'three';

function start(stage, label) {
  const still = matchMedia('(prefers-reduced-motion: reduce)');
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });   // throws if 3D cannot start
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  const canvas = renderer.domElement;
  canvas.setAttribute('role', 'img');
  canvas.setAttribute('aria-label', label);
  canvas.style.width = '100%';
  canvas.style.height = '100%';

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 100);
  camera.position.z = 4;
  const thing = new THREE.Mesh(new THREE.BoxGeometry(), new THREE.MeshStandardMaterial({ color: '#b8481f' }));
  scene.add(thing, new THREE.HemisphereLight('#ffffff', '#806040', 3));

  const draw = () => renderer.render(scene, camera);
  const tick = () => { thing.rotation.y += 0.01; draw(); };

  new ResizeObserver(() => {
    renderer.setSize(stage.clientWidth, stage.clientHeight, false);
    camera.aspect = stage.clientWidth / stage.clientHeight;
    camera.updateProjectionMatrix();
    draw();
  }).observe(stage);

  let onScreen = false;
  const setLoop = () => renderer.setAnimationLoop(onScreen && !still.matches ? tick : null);
  new IntersectionObserver(([entry]) => { onScreen = entry.isIntersecting; setLoop(); }).observe(canvas);
  still.addEventListener('change', setLoop);

  stage.replaceChildren(canvas);   // the fallback picture gives way only once 3D has started
}

try { start(document.getElementById('stage'), 'A bar of rosemary soap, turning slowly'); } catch (error) { /* the picture stays */ }
```

Rules that save time, each explained in the notes below:

- In a mockup that will be opened from a folder, make shapes and textures in code, or embed them in the page. Model and picture files beside the page will not load.
- Keep your own 3D code inline in the page, or in an ordinary script that calls `import('three')`. A module file of your own beside the page will not load from a folder.
- Nothing shows without a light, except with `MeshBasicMaterial`.
- One renderer per page if possible, and never more than a handful.
- If the object can be dragged, switch off wheel zoom and give up-and-down swipes back to the page.

## Notes

### An import map and one module script are enough to start
- Status: approved
- Test: `tests/three/setup-loads.html` (passed 2026-10-03, version 0.186.1)
- What happens: with the import map above and an inline `<script type="module">`, three.js loads from the CDN and draws, including when the page is opened straight from a folder. No build step.
- What to do: start every three.js mockup this way, with the version pinned in both lines of the import map.
- In someone else's mockup: a blank canvas and "Failed to resolve module specifier" in the console means the import map is missing or comes after the script that needs it.

### Add-ons do not load without the import map
- Status: approved
- Test: `tests/three/addon-needs-import-map.html`, `tests/three/addons-load-with-import-map.html` (passed 2026-10-03, version 0.186.1)
- What happens: three.js itself can be imported by its full address. Its add-ons (OrbitControls, GLTFLoader, RoundedBoxGeometry, RoomEnvironment and the rest) cannot, because each one imports `'three'` by that short name. Without an import map the browser reports `Failed to resolve module specifier "three"`.
- What to do: always use the import map, and import add-ons as `three/addons/...`. Both lines must carry the same version.
- In someone else's mockup: the core loads and the controls or loader do not. Add the import map.

### Opened from a folder, your own module files, models and pictures do not load
- Status: approved
- Test: `tests/three/local-files-from-a-folder.html` (passed 2026-10-03, version 0.186.1)
- What happens: on a page opened by double-clicking it, all three of these fail: a module file of your own beside the page (`import './scene.js'`), a model file loaded with GLTFLoader, and a picture loaded with TextureLoader. The browser refuses them for security. These still work: an ordinary `<script src>` file, which can reach three.js with `import('three')`; a model or picture written into the page as a `data:` address; and anything on a CDN.
- What to do: in a mockup, build shapes in code and paint textures onto a canvas (`CanvasTexture`), or embed small files as `data:` addresses. Put shared 3D code in an ordinary script that calls `import('three')`. Say in the blueprint that the real site, served from a host, can use ordinary files.
- In someone else's mockup: "it works on my machine" usually means they ran a local server. If it must open from a folder, the files have to be embedded or hosted.

### A model on a CDN loads, and is black until the scene has light
- Status: approved
- Test: `tests/three/model-from-cdn.html` (passed 2026-10-03, version 0.186.1)
- What happens: GLTFLoader loads a `.glb` file from a CDN, including on a page opened from a folder, and the model arrives as `gltf.scene`. With no light in the scene it draws solid black. Setting `scene.environment` from the `RoomEnvironment` add-on lights it believably with no extra files.
- What to do: for a product viewer, use `scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment()).texture`. Measure the model with `Box3` and place the camera from that, because models come in any size.
- In someone else's mockup: a black silhouette of the right shape is a model with no light.

### three.js is a large download, and the minified file saves little
- Status: approved
- Test: `tests/three/download-size.html` (passed 2026-10-03, version 0.186.1)
- What happens: `three.module.js` pulls in a second file, `three.core.js`. Together they are about 390 KB over the wire, compressed, before anything is drawn. `three.module.min.js` still pulls in the full-size core, so it comes to about 350 KB: a saving of a tenth, not a half.
- What to do: load three.js only on pages that have a 3D piece, and let the page's text and fallback picture show first. Do not expect the minified file to fix the size. A real build that bundles only what it uses is the way to shrink it.
- In someone else's mockup: three.js loaded on every page of a site for one 3D piece on the home page is wasted download on the rest.

### The canvas starts at 300 by 150 and setSize pins its size in pixels
- Status: approved
- Test: `tests/three/canvas-size.html` (passed 2026-10-03, version 0.186.1)
- What happens: a new renderer's canvas is 300 by 150. `setSize(400, 300)` sets both the drawing size and a fixed CSS size of 400px by 300px. `setSize(400, 300, false)` sets the drawing size and leaves CSS alone. three.js sets `display: block` on canvases it makes itself.
- What to do: size the canvas with CSS (`width: 100%; height: 100%` inside a box that has a shape) and call `setSize(width, height, false)`.
- In someone else's mockup: a small picture in the corner of a large box is a renderer that was never given a size.

### The picture does not follow its box unless code resizes it
- Status: approved
- Test: `tests/three/no-resize-by-itself.html` (passed 2026-10-03, version 0.186.1)
- What happens: after `setSize`, shrinking the box leaves the canvas at its old pixel size, sticking out. Nothing in three.js watches for size changes.
- What to do: a `ResizeObserver` on the box that calls `setSize(width, height, false)`, updates `camera.aspect`, calls `camera.updateProjectionMatrix()` and draws again. The starter does this. Watching the box is better than listening for the window resizing, because the box can change when the window does not.
- In someone else's mockup: a 3D piece that overflows on a phone or looks squashed after rotating the screen. This is also a likely cause of sideways scrolling in the phone check.

### The picture is drawn at one pixel per CSS pixel until told otherwise
- Status: approved
- Test: `tests/three/pixel-ratio.html` (passed 2026-10-03, version 0.186.1)
- What happens: the renderer's pixel ratio starts at 1 whatever the screen. After `setPixelRatio(2)`, a 300 by 200 picture is drawn at 600 by 400 and shown at 300 by 200.
- What to do: `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`. Without it the picture is blurry on phones and modern laptops. The cap of 2 is common advice to spare phones with very dense screens; it has not been measured here.
- In someone else's mockup: soft, blurry 3D beside crisp text.

### A standard material is black until the scene has a light
- Status: approved
- Test: `tests/three/black-without-light.html` (passed 2026-10-03, version 0.186.1)
- What happens: a white `MeshStandardMaterial` with no light draws pure black. `MeshBasicMaterial` ignores light and draws its colour. Adding `AmbientLight(white, 1)` brought the standard material to a mid grey (152 of 255), not white.
- What to do: every scene needs a light or an environment. For something soft and even, a `HemisphereLight` with an intensity around 3, or `RoomEnvironment` as above.
- In someone else's mockup: a black shape on a black background is nearly always this.

### A point light of intensity 1 is far dimmer than a directional light of 1
- Status: approved
- Test: `tests/three/point-light-is-dim.html` (passed 2026-10-03, version 0.186.1)
- What happens: lighting a white surface from 3 units away, `DirectionalLight` at intensity 1 gave a brightness of 151 of 255 and `PointLight` at intensity 1 gave 52. The point light needed intensity 9 to match. Point lights fade with the square of the distance.
- What to do: expect to give point and spot lights intensities in the tens. Code copied from older tutorials, written before lights worked this way, comes out very dark.
- In someone else's mockup: a dim, murky scene built from an old example. Raise the point light intensities or move them closer.

### Colours match CSS, but a picture used as a texture must be marked as colour
- Status: approved
- Test: `tests/three/colours-match-css.html` (passed 2026-10-03, version 0.186.1)
- What happens: a material given the colour `#1d6a43` draws exactly that colour. The same colour painted onto a canvas and used as a texture drew much lighter (95, 173, 140 against 29, 106, 67) until the texture was given `colorSpace = THREE.SRGBColorSpace`.
- What to do: pass the site's colour tokens straight to materials. For any texture that holds colour, made with `CanvasTexture` or `TextureLoader`, set `texture.colorSpace = THREE.SRGBColorSpace`. Models loaded with GLTFLoader do this themselves.
- In someone else's mockup: textures that look washed out or chalky.

### The background is solid black unless the renderer is made with alpha
- Status: approved
- Test: `tests/three/background.html` (passed 2026-10-03, version 0.186.1)
- What happens: an empty scene draws opaque black. A renderer made with `{ alpha: true }` draws a see-through background, so the page shows behind the object. Setting `scene.background` to a colour fills it with exactly that colour.
- What to do: for a 3D piece that sits on a page, make the renderer with `alpha: true` and let the page's own background show. It must be chosen when the renderer is made.
- In someone else's mockup: a black rectangle around a 3D object on a light page.

### Edges are jagged unless antialias is asked for when the renderer is made
- Status: approved
- Test: `tests/three/antialias.html` (passed 2026-10-03, version 0.186.1)
- What happens: with the default settings the edge of a tilted box has no in-between pixels at all: hard steps. With `{ antialias: true }` the edges are smoothed.
- What to do: `new THREE.WebGLRenderer({ antialias: true })`. It cannot be switched on afterwards.

### Nothing casts a shadow until four separate things are switched on
- Status: approved
- Test: `tests/three/shadows-off.html` (passed 2026-10-03, version 0.186.1)
- What happens: a shadow appeared only when all four were on: `renderer.shadowMap.enabled`, `light.castShadow`, `castShadow` on the object, and `receiveShadow` on the surface it falls on. Any three of them gave no shadow and no warning. While writing the test, a flat plane facing the light cast no shadow either; a solid block did.
- What to do: switch on all four. For a product on a page, a soft CSS shadow under the canvas is cheaper and often looks better.

### The animation loop keeps drawing when the canvas is scrolled out of sight
- Status: approved
- Test: `tests/three/loop-runs-offscreen.html` (passed 2026-10-03, version 0.186.1)
- What happens: with `setAnimationLoop` running and the canvas far below the visible part of the page, 37 frames were drawn in 0.6 seconds. With an `IntersectionObserver` switching the loop, none were drawn out of sight, and drawing resumed on scrolling to it.
- What to do: run the loop only while the canvas is on screen, as the starter does. On a long page a 3D piece at the top would otherwise use the battery for the whole visit.
- In someone else's mockup: a fan that spins up on a page whose 3D piece is long gone from view.

### three.js never checks whether the visitor asked for less motion
- Status: approved
- Test: `tests/three/ignores-reduced-motion.html` (passed 2026-10-03, version 0.186.1)
- What happens: with an animation loop and `autoRotate` running, neither three.js nor OrbitControls asked the browser about `prefers-reduced-motion`. The object kept turning.
- What to do: check `matchMedia('(prefers-reduced-motion: reduce)')` yourself. Draw one still picture and do not start the loop when it matches. The starter does this and reacts if the setting changes. Dragging can stay: that motion is the visitor's own.
- In someone else's mockup: any scene that moves by itself and has no mention of `prefers-reduced-motion` in its code. The audit flags this.

### Dragging with OrbitControls moves the camera and fires a change event
- Status: approved
- Test: `tests/three/orbit-drag.html` (passed 2026-10-03, version 0.186.1)
- What happens: with `new OrbitControls(camera, renderer.domElement)`, a real drag of 50 pixels across a 200-pixel-tall canvas swung the camera a quarter of the way round. Each movement fired a `change` event.
- What to do: for a viewer that only moves when dragged, draw on `change` and run no loop at all: `controls.addEventListener('change', draw)`. If damping or auto-rotation is switched on, `controls.update()` must be called every frame, so a loop is needed after all.

### With OrbitControls, the mouse wheel over the canvas zooms and the page stops scrolling
- Status: approved
- Test: `tests/three/orbit-wheel-traps-scroll.html` (passed 2026-10-03, version 0.186.1)
- What happens: turning the wheel with the pointer over the canvas zoomed the camera and did not scroll the page at all. With `controls.enableZoom = false` the same wheel turn scrolled the page.
- What to do: on an ordinary scrolling page, set `controls.enableZoom = false`. Otherwise someone scrolling down the page gets stuck the moment the pointer crosses the 3D piece. Offer zoom with buttons if it is needed.
- In someone else's mockup: a page that "stops scrolling" halfway down.

### With OrbitControls, a finger that starts on the canvas cannot scroll the page
- Status: approved
- Test: `tests/three/orbit-touch-blocks-scroll.html` (passed 2026-10-03, version 0.186.1)
- What happens: OrbitControls sets `touch-action: none` on the canvas. A finger swiped up 250 pixels over it scrolled the page by nothing. After setting `touch-action: pan-y` on the canvas, the same swipe scrolled the page.
- What to do: after creating the controls, set `renderer.domElement.style.touchAction = 'pan-y'`, so up-and-down swipes scroll the page and side-to-side drags turn the object. On a phone a 3D piece can fill the screen's width, and without this the page cannot be scrolled past it.
- In someone else's mockup: a phone visitor trapped on a 3D viewer. This matters more than the wheel, because on a phone there is nowhere else to put the finger.
- Not tested: whether a side-to-side drag still turns the object smoothly on a real phone once `pan-y` is set. The test only proves the page scrolls again.

### Finding what was clicked must use the canvas's own position, not the window's
- Status: approved
- Test: `tests/three/click-needs-canvas-position.html` (passed 2026-10-03, version 0.186.1)
- What happens: with the canvas placed part-way across and down a page, a real click on an object was found when the pointer position was worked out from the canvas's `getBoundingClientRect()`, and missed when worked out from the window's width and height, which is how many examples do it.
- What to do: `const r = canvas.getBoundingClientRect(); x = ((event.clientX - r.left) / r.width) * 2 - 1; y = -((event.clientY - r.top) / r.height) * 2 + 1;`
- In someone else's mockup: clicks that land on the wrong object, or work only when the page is scrolled to the top. The example they copied assumed a full-window canvas.

### A screen reader finds nothing in a 3D canvas unless it is given a name
- Status: approved
- Test: `tests/three/invisible-to-screen-readers.html` (passed 2026-10-03, version 0.186.1)
- What happens: a canvas with a scene drawn in it gave a screen reader nothing at all. With `role="img"` and an `aria-label`, it was announced as an image with that label.
- What to do: give every 3D canvas `role="img"` and a label that says what is shown. Anything that can be done inside the scene (choose a colour, open a part) also needs an ordinary button or link outside it, because nothing inside the canvas can be reached by keyboard.
- In someone else's mockup: the audit reports a canvas with no name as `a11y/canvas-alt`.

### When 3D cannot start, making the renderer throws an error
- Status: approved
- Test: `tests/three/webgl-unavailable.html` (passed 2026-10-03, version 0.186.1)
- What happens: on a device where the browser will not give a 3D context, `new THREE.WebGLRenderer()` throws "Error creating WebGL context", and any script after it stops. The `WebGL.isWebGL2Available()` add-on returns false in the same situation.
- What to do: put a picture in the box first, and replace it with the canvas only after the renderer has been made, inside `try`. The starter does this. The page then works for everyone and is better for those who can run 3D.
- In someone else's mockup: an empty box, and a page whose other scripts died with it.

### Taking an object out of the scene does not free its memory
- Status: approved
- Test: `tests/three/dispose.html` (passed 2026-10-03, version 0.186.1)
- What happens: after `scene.remove(mesh)`, the renderer still held the mesh's geometry and texture in graphics memory. They were released only after calling `dispose()` on the geometry, the material and the texture.
- What to do: when swapping one object for another, for example a different product in a viewer, dispose of the old one's geometry, materials and textures. `renderer.info.memory` shows what is still held.
- In someone else's mockup: a viewer that slows down or crashes after many swaps.

### A page can only keep about sixteen 3D canvases alive
- Status: approved
- Test: `tests/three/too-many-renderers.html` (passed 2026-10-03, version 0.186.1)
- What happens: after making 20 renderers on one page, the first four stopped working and 16 stayed alive. The browser drops the oldest.
- What to do: never give each product tile its own renderer. Use pictures for the tiles and one 3D viewer for the chosen product, or draw several objects with one renderer.
- In someone else's mockup: the first few 3D tiles in a grid go blank once enough have loaded.
- Careful: sixteen is what this browser allowed. Phones are reported to allow fewer; not measured.

### Speed has not been measured
- Status: draft
- Source: none. The test browser draws 3D in software, not on a graphics card, so it can show that something is correct but not that it is fast.
- What would confirm it: trying a finished mockup on a real phone and noting whether it turns smoothly and whether the phone warms up.
- Until then: keep a 3D piece on a page to one object, a few lights, no shadows, and a pixel ratio capped at 2.

### Compressed models need extra decoder files
- Status: draft
- Source: the three.js manual says models compressed with Draco or Meshopt need a decoder set on GLTFLoader. Not tested here.
- What would confirm it: a test that loads a compressed model with and without the decoder.

## What the audit tries

When a page has a canvas, `audit` and `check` open it several more times and report under "3D":

| Finding | How it is found |
|---|---|
| `3d/no-fallback` | The page is opened with 3D switched off. Nothing is shown where the 3D piece goes |
| `3d/error-without-3d` | The same page, and a script stopped with an error |
| `a11y/reduced-motion` | The page is opened as a device that asks for less motion. The canvas is photographed twice and has changed |
| `3d/wheel-traps-scroll` | The mouse wheel is turned over the canvas and the page does not scroll |
| `mobile/canvas-traps-scroll` | At phone width, a wide canvas takes every touch for itself |
| `a11y/canvas-alt` | A canvas has no role and label |

`check` also asks for a `scene` description on the element that holds a 3D canvas.

## Applied so far

- **Greenfire Herbs, 2026-10-03.** Two pieces, both built in code with no model files so the mockup opens from a folder: three stacked bars turning slowly at the top of the home page, with the drawn herbs kept around them, and a turn-the-bar view on the product page that loads three.js only when asked for. The shared code is `greenfire/soap3d.js`, an ordinary script that calls `import('three')`. The audit found nothing to report on the home page. The product view starts on a button press, so it was tried by hand: wheel, finger, reduced motion and 3D switched off all behaved as the notes say.

## What the skill cannot check

- A 3D piece that only starts after something is pressed. The audit looks at the page as it loads, so try those by hand, as was done for the Greenfire product view.

- The contrast check cannot see into a canvas. Text laid over a 3D piece has to be looked at by a person.
- Whether the picture looks right. The tests read individual pixels; they do not judge a scene.
- Anything on a real phone, including speed and how dragging feels.

## Questions it raises

- What shows if 3D cannot run on someone's device?
- Does the scene move by itself, and what do people who ask for less motion see?
- Can visitors turn or zoom the object, and by how much?
- Where do the models and textures come from, who makes them, and may they be used?
- Is the 3D piece on every page or only one?
