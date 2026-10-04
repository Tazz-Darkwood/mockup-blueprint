---
name: PixiJS
summary: Library that draws fast 2D pictures in a canvas with the graphics card: sprites, layers, tints, bending meshes. Read when a mockup or build uses PixiJS, for a game view or anything with many moving pictures inside an ordinary page. Setup that works from a folder, how to colour and bake layered art, and what a canvas takes away (touch scrolling, screen readers, reduced motion).
detect: ["\\bpixijs\\b", "pixi\\.js", "pixi\\.min", "\\bPIXI\\.", "from ['\"]pixi"]
version: 8.22.0
checked: 2026-10-03
source: https://pixijs.com/8.x/guides and the tests named in each note
---

# PixiJS

PixiJS draws into one `<canvas>`. It is a renderer, not a game engine: it puts pictures on the screen quickly and tells you what was clicked, and leaves rules, menus and data to the rest of the page. That makes it a good fit beside ordinary HTML: the tank or the battle is a canvas, and the buttons, lists and forms around it are normal elements.

Everything inside the canvas is invisible to the page. Text drawn there cannot be selected, searched, or read by a screen reader, nothing in it can carry a blueprint anchor, and the skill's checks cannot see into it. So keep in HTML whatever a person must read or press, and treat the canvas as the picture. In the blueprint a PixiJS canvas is one element described by a `scene` (see `references/context-format.md`), exactly as for three.js; much of `three-scenes.md` on stopping when out of sight and on fallbacks applies here too.

## Use it properly

In the `<head>`, pinned to a version, as an ordinary script. This works when the mockup is opened from a folder:

```html
<script src="https://cdn.jsdelivr.net/npm/pixi.js@8.22.0/dist/pixi.min.js"></script>
```

Then, in a script at the end of the page:

```html
<div id="tank" data-bp="tank">
  <p class="fallback">Three axolotls in a planted tank.</p>   <!-- shown until the canvas is in, and if it never is -->
</div>
<script>
(async () => {
  const holder = document.getElementById('tank');
  const app = new PIXI.Application();
  await app.init({ width: 600, height: 400, background: '#102030',       // options go to init(), not to the constructor
                   resolution: window.devicePixelRatio || 1, autoDensity: true });
  app.canvas.style.touchAction = 'pan-y';                                 // let a finger scroll the page past the canvas
  app.canvas.setAttribute('role', 'img');
  app.canvas.setAttribute('aria-label', 'Three axolotls in a planted tank');
  holder.replaceChildren(app.canvas);

  const still = window.matchMedia('(prefers-reduced-motion: reduce)');
  const inView = new IntersectionObserver(([entry]) => {                  // stop drawing when nobody can see it
    if (entry.isIntersecting && !still.matches) app.ticker.start(); else app.ticker.stop();
  });
  inView.observe(app.canvas);
  // ... make sprites, add them to app.stage, move them in app.ticker.add(() => { ... })
  app.render();                                                           // one frame, for when the ticker is stopped
})();
</script>
```

Rules that save time, each explained in the notes below:

- Pictures used in a mockup opened from a folder must be written into the page as data addresses, or drawn in code. Picture files beside the page cannot be used.
- Draw art for tinting in white and light greys. A tint can only darken.
- Give PixiJS colours as hex or `rgb()`. Convert anything worked out in OKLab or OKLCH first.
- One `Application` for the page. The browser allows about sixteen.
- Anything a person must be able to press with a keyboard or hear from a screen reader is either an HTML element, or a sprite marked `accessible`.

## Notes

### One script tag and an awaited init() are enough to draw
- Status: approved
- Test: `tests/pixi/setup-loads.html` (passed 2026-10-03, version 8.22.0)
- What happens: with the one script tag, `new PIXI.Application()` followed by `await app.init({...})` made a canvas and drew a sprite on the background colour, on a page opened from a folder. It drew with WebGL.
- What to do: use the starter above. `init()` returns a promise, so the code that follows it lives in an `async` function.

### Options given to new Application() are silently ignored
- Status: approved
- Test: `tests/pixi/old-constructor-options.html` (passed 2026-10-03, version 8.22.0)
- What happens: `new PIXI.Application({ width: 120, height: 60 })`, the way versions before 8 were set up, raised no error and made no renderer. After `init()` with no options the canvas was 800 by 600. With the same options given to `init()` it was 120 by 60.
- What to do: every option goes to `init()`. Most examples on the web, and much of what a language model remembers, are written for version 7 and put them in the constructor.
- In someone else's mockup: a canvas that is 800 by 600 whatever the code asks for, or `app.view` and `app.renderer` used before `init()` has finished.

### PixiJS also loads as a module through an import map
- Status: approved
- Test: `tests/pixi/module-from-cdn.html` (passed 2026-10-03, version 8.22.0)
- What happens: with an import map naming `pixi.js` as `.../dist/pixi.min.mjs` on the CDN, `import { Application } from 'pixi.js'` worked on a page opened from a folder.
- What to do: either way works. The plain script tag is simpler for a mockup. Whichever is used, the page's own code must stay inside the page: a module file of your own beside the page will not load from a folder (see "Opened from a folder" in `three.md`, which holds here too).

### Opened from a folder, a picture file beside the page cannot become a texture
- Status: approved
- Test: `tests/pixi/local-pictures-from-a-folder.html` (passed 2026-10-03, version 8.22.0)
- What happens: on a page opened from a folder, `PIXI.Assets.load('local.png')` failed. An `<img>` pointing at the same file loaded, but giving it to PixiJS as a texture failed with a security error from the browser ("the image element contains cross-origin data"). The same picture written into the page as a data address (`data:image/png;base64,...`) loaded and drew.
- What to do: in a mockup, put each picture into the page as a data address (a small script that sets `const ART = { body: "data:image/png;base64,..." }` works from a folder), or draw simple shapes with `PIXI.Graphics`. The real site, served from a host, loads picture files normally.
- For the blueprint: say where each picture comes from in the real site and who makes it, in the scene's `assets`. The mockup's embedded pictures are stand-ins.

### A tint multiplies: it can colour and darken a layer, never lighten it
- Status: approved
- Test: `tests/pixi/tint-multiplies.html` (passed 2026-10-03, version 8.22.0)
- What happens: a picture half white and half mid-grey (128) was tinted orange, `0xff8000`. The white half became exactly the tint, [255, 128, 0]. The grey half became [128, 64, 0]: each channel is the picture's value times the tint's.
- What to do: draw art that is to be coloured by tinting in white and light greys, with the shading as darker greys. White takes the tint's colour exactly and everything else comes out darker. A colour lighter than the art cannot be reached by tinting; for that the art has to be lighter, or the colour mapped another way (a filter, or recolouring the pixels when the picture is baked).

### A tint takes hex, names, rgb() and hsl(), but not oklch() or oklab()
- Status: approved
- Test: `tests/pixi/tint-colour-words.html` (passed 2026-10-03, version 8.22.0)
- What happens: `#ff8000`, `rgb(255 128 0)`, `orange` and `hsl(30 100% 50%)` were accepted. `oklch(0.75 0.18 60)` and `oklab(0.75 0.09 0.15)` raised "Unable to convert color".
- What to do: when colours are worked out in OKLab or OKLCH (for mixing that looks right to the eye), convert the result to sRGB hex before giving it to PixiJS, with a colour library, and bring colours a screen cannot show back into range there too.

### Several tinted layers can be baked into one texture
- Status: approved
- Test: `tests/pixi/bake-layers.html` (passed 2026-10-03, version 8.22.0)
- What happens: five half-clear layers, each tinted differently, drew pixel [199, 81, 161]. `app.renderer.generateTexture(container)` turned them into one texture, 80 by 64, and a single sprite using it drew [200, 81, 161] at the same spot: the same picture to within rounding.
- What to do: for a creature built from layers (body, markings, eyes) whose colours do not change every frame, build the layers once, bake them, and show one sprite. A tank of fifty creatures is then fifty sprites, not three hundred. Call `texture.destroy(true)` when the creature goes.

### MeshRope bends a flat picture along a line of points
- Status: approved
- Test: `tests/pixi/rope-bends.html` (passed 2026-10-03, version 8.22.0)
- What happens: a picture laid along five points in a straight line covered the line and nothing 50 pixels above it. After the middle point was moved up by 50 and the scene drawn again, the picture covered that higher spot: it had bent with the line.
- What to do: `new PIXI.MeshRope({ texture, points })`, then move the points each frame (a sine wave along the spine) for a swimming body or a swaying gill, with no rigging tool. The rope follows the points by itself when drawn.

### A picture saved from the canvas loses the background unless preserveDrawingBuffer is on
- Status: approved
- Test: `tests/pixi/saving-a-picture.html` (passed 2026-10-03, version 8.22.0, three runs alike)
- What happens: with `preserveDrawingBuffer` left off, `canvas.toDataURL()` gave the sprite correctly but the background as black, [0, 0, 0], where the background colour was #102030, both straight after drawing and five frames later. With `preserveDrawingBuffer: true` in `init()`, the saved picture had the sprite and the right background. In an earlier trial on a differently built page the background came back right without the setting, so what is saved without it is not dependable.
- What to do: turn `preserveDrawingBuffer` on only where pictures are taken from the canvas by script: a "save a picture of my pet" button, or a development build that compares pictures. It costs speed, so leave it off otherwise. The skill's own screenshots (`try --shot`, `check`) are taken by the browser and showed the canvas correctly without it.

### resolution makes the canvas bigger on the page unless autoDensity is on
- Status: approved
- Test: `tests/pixi/pixel-ratio.html` (passed 2026-10-03, version 8.22.0)
- What happens: asked for 100 wide at `resolution: 2`, the canvas had 200 pixels and took 200 pixels of the page. With `autoDensity: true` it had 200 pixels and took 100. Left alone, `resolution` was 1.
- What to do: for sharp drawing on phones and high-density screens pass both `resolution: window.devicePixelRatio || 1` and `autoDensity: true`. Without the first, the picture is blurry on a phone; with the first and not the second, it is twice the size.

### resizeTo follows the window, not the box it was given
- Status: approved
- Test: `tests/pixi/resize-to-element.html` (passed 2026-10-03, version 8.22.0)
- What happens: with `resizeTo` set to a box 400 wide, the canvas was 400 wide. The box was narrowed to 250 and the canvas stayed 400. After a window `resize` event it became 250.
- What to do: `resizeTo` is enough when the box only changes size with the window. When a layout can change the box without the window changing (a side panel opening, a phone turning is fine), watch the box with a `ResizeObserver` and call `app.resize()`.

### The ticker keeps running when the canvas is scrolled out of sight
- Status: approved
- Test: `tests/pixi/loop-runs-offscreen.html` (passed 2026-10-03, version 8.22.0)
- What happens: with the canvas scrolled 2,500 pixels out of view, the ticker ran 30 times in 30 frames. After `app.ticker.stop()` it ran 0 times, and `app.ticker.start()` set it going again.
- What to do: stop the ticker when the canvas is out of sight, with an `IntersectionObserver` as in the starter. A phone's battery pays for every frame nobody sees.

### PixiJS takes no notice of the reduced-motion setting
- Status: approved
- Test: `tests/pixi/ignores-reduced-motion.html` (passed 2026-10-03, version 8.22.0)
- What happens: with the browser reporting that the visitor asked for less motion, the ticker ran 20 times in 20 frames as usual.
- What to do: check `matchMedia('(prefers-reduced-motion: reduce)')` yourself. For those visitors draw one still frame, or keep only movement that carries meaning, and say in the blueprint which. The skill's `check` photographs the canvas twice under that setting and reports `a11y/reduced-motion` if it is still moving.

### A sprite hears no clicks until its eventMode is set
- Status: approved
- Test: `tests/pixi/events-need-event-mode.html` (passed 2026-10-03, version 8.22.0)
- What happens: a new sprite has `eventMode` "passive". Two sprites were given a `pointerdown` listener and clicked; only the one with `eventMode = 'static'` heard it.
- What to do: set `eventMode = 'static'` on everything that can be clicked or tapped (`'dynamic'` for things that must react while moving under a still pointer). A listener on a sprite left as it was does nothing and reports nothing.

### A finger that starts on the canvas cannot scroll the page
- Status: approved
- Test: `tests/pixi/touch-scroll-trapped.html` (passed 2026-10-03, version 8.22.0)
- What happens: PixiJS gave its canvas the style `touch-action: none`. On a touch screen, a finger dragged 200 pixels up the canvas scrolled the page by 0. With `app.canvas.style.touchAction = 'pan-y'` the same drag scrolled it by 185.
- What to do: unless the canvas itself is dragged or panned, set `touchAction = 'pan-y'` after `init()`. A canvas that fills a phone's screen with `touch-action: none` traps the visitor on that screen. The skill's `check` reports this as `mobile/canvas-traps-scroll`.
- For the blueprint: if dragging inside the canvas is part of the design, say how a phone user gets past it.

### The mouse wheel over a PixiJS canvas still scrolls the page
- Status: approved
- Test: `tests/pixi/wheel-scrolls-page.html` (passed 2026-10-03, version 8.22.0)
- What happens: the wheel turned 300 pixels with the pointer on the canvas scrolled the page by 300.
- What to do: nothing. Unlike three.js with its orbit controls, a PixiJS canvas does not take the wheel. If a design zooms with the wheel, that is the page's own code, and then the wheel no longer scrolls the page: see the wheel note in `three.md`.

### A sprite marked accessible becomes a real button for assistive technology, after the first Tab
- Status: approved
- Test: `tests/pixi/accessible-overlay.html` (passed 2026-10-03, version 8.22.0)
- What happens: a sprite with `accessible = true` and `accessibleTitle = 'Feed the axolotl'` was, at first, nothing to assistive technology: the page offered it nothing at all. After Tab was pressed once, PixiJS put an invisible layer of real elements over the canvas and the sprite was announced as `button "Feed the axolotl"`. Pressing Enter on it reached the sprite's click listeners. Text drawn in the canvas with `PIXI.Text` ("Hunger: 3 of 5") was never offered.
- What to do: mark every pressable sprite `accessible` with a title, and it becomes reachable by keyboard and screen reader. Do not rely on it for anything that must be read: numbers, names and messages go in HTML beside the canvas, or in the canvas's own `aria-label` when they describe the picture.
- Careful: a screen reader user who does not press Tab first (many browse with other keys) meets an empty canvas. Give the canvas `role="img"` and a label saying what it shows, as in the starter.

### Each Application takes a graphics context, and the browser allows about sixteen
- Status: approved
- Test: `tests/pixi/too-many-canvases.html` (passed 2026-10-03, version 8.22.0)
- What happens: with 18 Applications on one page, the first lost its graphics context and went blank. `app.destroy(true)` gave a context back.
- What to do: one Application for the tank, not one per creature card. For a list of many small pictures (a market, a collection), draw each creature once, save it as a picture (see the note on saving) or bake it and show it in one shared canvas, and use ordinary `<img>` elements in the list.

### Where the graphics card cannot be used, PixiJS falls back to a plain 2D canvas by itself
- Status: approved
- Test: `tests/pixi/webgl-unavailable.html` (passed 2026-10-03, version 8.22.0)
- What happens: with WebGL and WebGPU made unavailable, `init()` still finished, the renderer called itself "canvas", and a sprite tinted orange drew the right colour.
- What to do: keep a fallback in the holder anyway (the starter's paragraph), for when the script itself fails to load. Do not assume the fallback renderer does everything: filters and meshes were not tried on it here.

### Filters are costly on many sprites
- Status: draft
- Test: none. A fair test needs timing on a real phone, which this runner cannot do.
- Source: PixiJS's own performance guide says filters break batching and are expensive in bulk.
- What would confirm it: frame times for fifty sprites with and without a glow or blur filter on a mid-range phone.
- Until then: do not put a filter on every creature. Bake a glow into the texture, or draw it as a second, pre-blurred sprite behind, and keep real filters for the one creature in focus.

## What the skill cannot check

- Anything drawn inside the canvas: whether it looks right, whether text in it is readable, whether colours contrast.
- Speed. How many creatures a real phone can hold has to be measured on a real phone.
- That the art in a mockup is the art the real site will have.

## Questions it raises

- What is in the canvas, and what stays as ordinary HTML around it?
- Where does each picture come from, who makes it, and in what form (layers, greys for tinting)?
- What does someone see who cannot run the canvas, or who has asked for less motion?
- Can everything pressable in the canvas be reached with a keyboard?
- How many creatures must it show at once, and on what kind of phone?
