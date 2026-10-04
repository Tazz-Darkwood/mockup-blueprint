---
name: three.js full scenes
summary: For a whole 3D scene or game, not one object on a page: crowds of moving things, more than one view, a camera that follows something or rides inside it, picking one thing out of many, name labels, keyboard control. Read after three.md, which covers setup and what every 3D page needs.
detect: ["InstancedMesh", "CSS2DRenderer", "setScissor", "setViewport", "TubeGeometry", "Raycaster", "mergeGeometries", "BackSide"]
version: 0.186.1
checked: 2026-10-03
source: https://threejs.org/docs/ and https://threejs.org/manual/
---

# three.js full scenes

Everything in `three.md` still applies: the import map, sizing, pausing off-screen, reduced motion, the fallback, a name for screen readers, and what will not load from a folder. This file adds what a scene with many things in it needs.

The yardstick used here is **draw calls**: how many times a frame the graphics card is asked to draw something. It can be read from `renderer.info.render.calls` and counted exactly, even in a test browser that cannot measure speed. Fewer is better, and a scene that draws each small thing separately is the usual reason a 3D game is slow.

## Use it properly

- **Keep the world separate from the picture.** Hold the state of the game (where each ant is, what it is doing) in plain data, advanced by time. The 3D code only reads that data and draws it. Then the same rules can run on a server, be saved, or be drawn a second way.
- **One renderer, one scene, as many cameras as there are views.**
- **A crowd is one `InstancedMesh`**, not one mesh each. Scenery that never moves is merged into one.
- **Move things by the time that has passed**, never by a fixed step each frame.
- **Names and numbers are HTML laid over the scene**, not drawn in it.
- **A cutaway is a hollow shape drawn from the inside.** The same shape then serves a camera that goes in.
- **Decide the most there can ever be** of each kind of thing before building its crowd.

These notes were worked out on a full game mockup, an ant colony seen from above and from inside, whose drawing code was kept in one file and its rules in another. That mockup is not part of the skill.

## Notes

### Five hundred separate objects are five hundred draw calls; one InstancedMesh is one
- Status: approved
- Test: `tests/three-scenes/many-objects-one-draw.html` (passed 2026-10-03, version 0.186.1)
- What happens: 500 small meshes sharing one shape and material took 500 draw calls. The same 500 as one `InstancedMesh` took 1, and drew exactly the same picture.
- What to do: anything there are many of, ants, eggs, seeds, is one `InstancedMesh` per kind. Each one is placed with `setMatrixAt(index, matrix)`.
- In someone else's mockup: a loop that calls `new THREE.Mesh` hundreds of times is the first thing to change when a scene is slow.

### Moving or recolouring one of a crowd shows only after a flag is set
- Status: approved
- Test: `tests/three-scenes/instance-move-needs-flag.html` (passed 2026-10-03, version 0.186.1)
- What happens: after `setMatrixAt`, the picture did not change until `instanceMatrix.needsUpdate = true` was set. After `setColorAt`, it did not change until `instanceColor.needsUpdate = true`. Each one of a crowd can have its own colour this way.
- What to do: set the flag once per frame after moving everything, not once per ant. Call `setColorAt` for every one at the start so the colour store exists.
- In someone else's mockup: a crowd frozen at its starting positions while the numbers on screen say it is moving.

### A crowd that moves away from where it started can vanish
- Status: approved
- Test: `tests/three-scenes/crowd-vanishes-when-moved.html` (passed 2026-10-03, version 0.186.1)
- What happens: three.js skips drawing anything it thinks is out of view, and for an `InstancedMesh` it works that out once, from where the crowd first was. A crowd that walked away, with the camera following, was not drawn at all until `computeBoundingSphere()` was called on it.
- What to do: after the crowd has spread or moved, call `crowd.computeBoundingSphere()` now and then, or set `crowd.frustumCulled = false` if the crowd is always meant to be seen.
- In someone else's mockup: every ant disappears at once when the camera turns or travels, and comes back when it returns.

### A click on a crowd says which one was hit
- Status: approved
- Test: `tests/three-scenes/pick-one-of-many.html` (passed 2026-10-03, version 0.186.1)
- What happens: `raycaster.intersectObject(crowd)` on an `InstancedMesh` returns the hit with an `instanceId`: the number of the one that was clicked. A click on empty space returned nothing.
- What to do: keep the game's own list in the same order as the instances, so `instanceId` is the index of the ant. Work out the pointer position from the canvas, as in `three.md`.
- Careful: small things are hard to hit. Pick with a larger invisible shape than the one drawn, or choose the nearest one within a few pixels.

### Scenery that never moves can be merged into one draw
- Status: approved
- Test: `tests/three-scenes/scenery-merged.html` (passed 2026-10-03, version 0.186.1)
- What happens: 40 separate blocks took 40 draw calls. Joined with `mergeGeometries` from the `BufferGeometryUtils` add-on they took 1 and drew the same picture.
- What to do: build walls, tunnels and ground as separate shapes, then merge the ones that share a material and never move.

### One renderer can draw two views of the same scene
- Status: approved
- Test: `tests/three-scenes/two-views-one-renderer.html` (passed 2026-10-03, version 0.186.1)
- What happens: with `setScissorTest(true)`, then `setViewport` and `setScissor` to a part of the canvas before each `render`, the left half showed the scene through one camera and the right half through another. With the scissor test off, the second render wiped the first.
- What to do: for a main view with a smaller overview in a corner, use one canvas and render twice, once per camera. Do not make a second renderer: each costs a graphics context, and a page can keep only about sixteen.
- Careful: viewport and scissor are measured from the bottom left, in CSS pixels. Give each camera the shape of its own part, not of the whole canvas.

### A camera attached to an object follows it only if the object is in the scene
- Status: approved
- Test: `tests/three-scenes/camera-rides-object.html` (passed 2026-10-03, version 0.186.1)
- What happens: a camera added as a child of a carrier moved with it and saw what it should when the carrier was in the scene. With the carrier not added to the scene, the picture stayed as it was although the carrier had moved.
- What to do: to ride along with something, `thing.add(camera)` and make sure the thing is in the scene. For a chase view, give the camera a small offset behind and above.

### lookAt points an object's front at the target, and a camera's view
- Status: approved
- Test: `tests/three-scenes/lookat-direction.html` (passed 2026-10-03, version 0.186.1)
- What happens: after `lookAt(target)`, an ordinary object has its +z side facing the target. A camera has its −z side facing it, which is the way a camera looks. The target is a position in the world, including for a child of something that has moved.
- What to do: build models with their front towards +z. Then `ant.lookAt(nextPoint)` turns them the way they are walking.
- In someone else's mockup: creatures that walk backwards or sideways were modelled facing another way.

### From inside a shape nothing is drawn unless the material is told to show its inside
- Status: approved
- Test: `tests/three-scenes/inside-needs-backside.html` (passed 2026-10-03, version 0.186.1)
- What happens: with the camera inside a tube, the default material drew nothing: the walls were invisible. With `side: THREE.BackSide` or `THREE.DoubleSide` they were drawn.
- What to do: a tunnel or room seen from inside uses `BackSide`. If the same shape is also seen from outside, use `DoubleSide`.
- In someone else's mockup: a first-person view that shows only blackness or the sky.

### Anything nearer than the camera's near distance is cut away
- Status: approved
- Test: `tests/three-scenes/near-plane-clips-closeups.html` (passed 2026-10-03, version 0.186.1)
- What happens: a new `PerspectiveCamera()` has a near distance of 0.1 and a far distance of 2000. A wall 0.05 away was not drawn at all with near at 0.1, and was drawn with near at 0.01.
- What to do: choose the size of the world first. For a camera at an ant's height in a narrow tunnel, set `near` to a small fraction of the tunnel's width. Keep `far` no larger than needed: a huge range between the two makes distant surfaces flicker.
- In someone else's mockup: walls that open into holes as the camera brushes past them.

### A tunnel can be shown growing by drawing only part of it
- Status: approved
- Test: `tests/three-scenes/reveal-with-draw-range.html` (passed 2026-10-03, version 0.186.1)
- What happens: a tube built along a path at full length, then given `geometry.setDrawRange(0, half)`, drew only the first half of its length and half as many triangles.
- What to do: for something that grows along a path, such as a tunnel being dug, build the whole shape once and raise the draw range as it grows. This is far cheaper than building a new shape each time.

### CSS2DRenderer keeps ordinary HTML labels pinned to things in the scene
- Status: approved
- Test: `tests/three-scenes/name-labels.html` (passed 2026-10-03, version 0.186.1)
- What happens: a `CSS2DObject` holding an ordinary HTML element, added as a child of a mesh, stayed over that mesh as it moved. The label was real text: a screen reader was given it. The layer the labels live in covers the canvas, and until it was set to `pointer-events: none` no click reached the canvas at all.
- What to do: use it for names and small tags. Render it after the main render each frame, give it the same size as the canvas, lay it over the canvas with `position: absolute`, and set `pointer-events: none` on the layer. A label that must be clickable sets `pointer-events: auto` on itself.
- Careful: each label is a page element moved every frame. A handful is fine; do not label hundreds at once. Not measured.

### Something see-through in front can hide something see-through behind it
- Status: approved
- Test: `tests/three-scenes/see-through-order.html` (passed 2026-10-03, version 0.186.1)
- What happens: a see-through mark behind a sheet of see-through glass was drawn correctly when three.js chose the order by distance. When the glass was forced to draw first it hid the mark completely. With `depthWrite: false` on the glass, the mark showed whatever the order.
- What to do: give a glass front, water, or any large see-through surface `transparent: true` and `depthWrite: false`.
- In someone else's mockup: things behind glass that flicker in and out as the camera moves.

### A canvas hears no keys until it can take focus and has it
- Status: approved
- Test: `tests/three-scenes/keys-need-focus.html` (passed 2026-10-03, version 0.186.1)
- What happens: a key listener on the canvas heard nothing, even after the canvas was clicked. After giving the canvas `tabindex="0"` and clicking it, it heard the key. A listener on the window heard keys with nothing focused.
- What to do: for a game played with keys, give the canvas `tabindex="0"`, a visible focus outline and a label saying which keys do what. Listen on the canvas, not the window, so typing in a form elsewhere on the page does not steer the game. Everything keys can do must also be possible with buttons on the page.

### The loop is handed the time; a fixed step per frame ties speed to the screen
- Status: approved
- Test: `tests/three-scenes/loop-time.html` (passed 2026-10-03, version 0.186.1)
- What happens: the function given to `setAnimationLoop` is called with the time in milliseconds. In one second it ran 61 times here. Something moved by a fixed amount each frame travelled in proportion to the number of frames, so it would go twice as fast on a screen that refreshes twice as often. Something moved by speed times the seconds passed travelled the same distance regardless.
- What to do: `const dt = Math.min((time - last) / 1000, 0.1)` and move everything by `speed * dt`. The cap matters: when a tab has been in the background the gap can be minutes, and without it everything leaps.
- In someone else's mockup: a game that runs at double speed on a gaming monitor.
- Not tested: the leap after a tab comes back from the background. The cap is in the test, but the test browser cannot put a tab in the background.

### A moving part on every member of a crowd needs a second crowd
- Status: approved
- Test: `tests/three-scenes/parts-of-a-crowd.html` (passed 2026-10-03, version 0.186.1)
- What happens: an `InstancedMesh` has one position for each member, so nothing inside a member can move by itself. Two bodies in one crowd, with an arm each in a second crowd placed at body times turn times reach, showed the arm swinging round its own body, for two draw calls in all.
- What to do: put the parts that move (legs, wings, wheels) in their own crowd, with as many members as there are bodies times parts. Each frame, work out the body's matrix once, then each part's as `body × where it joins × how far it has turned`. On Meridian each ant is one body and six legs.
- In someone else's mockup: creatures that slide along like chess pieces have their limbs baked into the body shape.

### Each member's colour is multiplied by the crowd's own colour
- Status: approved
- Test: `tests/three-scenes/instance-colour-multiplies.html` (passed 2026-10-03, version 0.186.1)
- What happens: a member given blue with `setColorAt` drew black in a crowd whose material was red, half-strength blue in a grey crowd, and blue only in a white crowd.
- What to do: give a crowd that uses per-member colours a white material, and put every colour on the members.
- In someone else's mockup: per-member colours that come out dark or wrong, in a crowd whose material already has a colour.

### A crowd can be drawn at less than its full number
- Status: approved
- Test: `tests/three-scenes/crowd-count.html` (passed 2026-10-03, version 0.186.1)
- What happens: a crowd made for 5 drew 5, then 2 after `count = 2`, none after `count = 0`, and 5 again when set back.
- What to do: make each crowd once, for the most there can ever be, and set `count` each frame to how many there are now. It cannot be raised above the number it was made for, so decide that limit first; it is a question for the blueprint.

### Merging shapes gives nothing back unless they are the same kind
- Status: approved
- Test: `tests/three-scenes/merge-needs-same-kind.html` (passed 2026-10-03, version 0.186.1)
- What happens: `mergeGeometries` returned `null`, with only a line in the console, when one shape shared its corners between faces and the other did not, and again when one had texture positions and the other had none. Two shapes of the same kind merged.
- What to do: call `.toNonIndexed()` on every shape before merging, and make sure each has the same set of attributes. Check the result is not `null` before using it.
- In someone else's mockup: "Cannot read properties of null" on the line after a merge.

### Drawing only the inside of a tunnel makes it a cutaway from the front
- Status: approved
- Test: `tests/three-scenes/cutaway-backside.html` (passed 2026-10-03, version 0.186.1)
- What happens: with a ball inside a tube and the camera in front, the tube hid the ball with the default material and with `DoubleSide`. With `side: THREE.BackSide` the near half of the tube was not drawn, and the ball showed against the far wall.
- What to do: for anything seen in cross-section, an ant farm, a pipe, a room with its front wall off, use `BackSide` on the hollow shape. The same material then serves a camera inside it, so one shape gives both the cutaway and the inside view.

### Where two hollow shapes join, the wall between them blocks the view until it is cut away
- Status: approved
- Test: `tests/three-scenes/opening-between-shells.html` (passed 2026-10-03, version 0.186.1)
- What happens: from inside a chamber, looking towards a tunnel that leaves it, the chamber's own wall was all that showed. After removing the triangles of the chamber that lay within the tunnel's width of its middle line, the tunnel showed through the opening.
- What to do: build each hollow place as a shape with its faces listed separately (`toNonIndexed()`), drop every triangle whose centre falls inside the mouth of a joining tunnel, and stop each tunnel just inside the shape it joins. Use a finely divided shape, or the opening has a saw-toothed edge when seen close up.
- In someone else's mockup: a walk-through that ends at a blank wall where a doorway should be.

### Something too deep inside a tunnel is swallowed by its far wall
- Status: approved
- Test: `tests/three-scenes/swallowed-by-the-wall.html` (passed 2026-10-03, version 0.186.1)
- What happens: in a tunnel of radius 1 seen from the front, a small ball at height 0.8 showed at depth 0.4 and vanished at depth 0.8, though the same depth was fine at the middle of the tunnel. A round tunnel is shallower towards its edges: at a distance h from the middle it is only the square root of (r² − h²) deep.
- What to do: work out the widest and deepest point of whatever moves through a tunnel, with its limbs at full stretch, and keep that inside the circle. On Meridian the ants' feet were sticking through the tunnel sides until the ants were made smaller and walked nearer the middle.
- In someone else's mockup: limbs that flicker in and out of a wall as a creature walks.

### A camera keeps its own idea of up, and lookAt uses it
- Status: approved
- Test: `tests/three-scenes/camera-up.html` (passed 2026-10-03, version 0.186.1)
- What happens: a camera looking along x had the top of its picture pointing up the y axis. Setting `camera.up` to the z axis changed nothing until `lookAt` was called again; then the top of the picture pointed along z.
- What to do: when the thing being followed walks on a wall or a ceiling, set `camera.up` to that surface's own "up" and then call `lookAt`. When up changes, ease it over a moment, or the picture flips.

### Easing after a target must use the time passed, or the screen's speed changes it
- Status: approved
- Test: `tests/three-scenes/ease-any-frame-rate.html` (passed 2026-10-03, version 0.186.1)
- What happens: moving a fixed share of the remaining distance each frame got 95% of the way in a second at 60 frames a second and 99.8% at 120. `THREE.MathUtils.damp(from, to, 3, dt)` got exactly the same distance at 30, 60 and 120.
- What to do: ease a following camera with `MathUtils.damp`, or `1 - Math.exp(-rate * dt)` as the share to move. Ease where it is and what it looks at separately. When the subject stops, let the camera stop too and keep watching it; a camera that keeps circling a creature at work is tiring to watch.

### A texture stretched past its edge smears unless it is told to repeat
- Status: approved
- Test: `tests/three-scenes/texture-repeat.html` (passed 2026-10-03, version 0.186.1)
- What happens: a strip that asked for a black-and-white picture four times along its length showed it once and then smeared its last row the rest of the way. With `wrapT = THREE.RepeatWrapping` it showed four times.
- What to do: for anything laid along a length, a trail, a road, a fence, set the wrapping to repeat in that direction and scale the texture positions by the length, so the pattern keeps its size however long the strip is.

### How many things a phone can draw has not been measured
- Status: draft
- Source: none. The test browser draws 3D in software.
- What would confirm it: running a finished scene on a real phone with a few hundred instanced ants and reading the frame time.
- Until then: count draw calls with `renderer.info.render.calls` and keep them in the tens, not the hundreds.

## What the skill cannot check

- Whether a scene is smooth. Only draw calls can be counted here.
- Whether a game is fun, fair or understandable. That needs people playing it.
- Anything that happens over time on a server.

## Questions it raises

- How many moving things will there be at most, and does that grow without limit?
- How many views are there, and can they be seen at once?
- Can the game be played without a mouse, and without a keyboard?
- Does the world live in the browser, or on a server that the browser only draws?
