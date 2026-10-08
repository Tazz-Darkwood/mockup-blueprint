---
name: Background (a part guide)
summary: What lies behind everything - what shows between a page's sections, in layers that switch on their own (texture, pattern, drawings, things to find, scene), from nothing at all to a detailed ground with signs and small things to find. Each layer works on a light page and a dark one, and can be picked with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: the mockups made with the skill so far, and the guides named in each option
---

# Background

A part guide. It covers what lies behind everything on a page: what a visitor sees in the gaps between sections and down the sides on a wide screen. It is made of layers, each one decision that switches on its own: texture, pattern, drawings, things to find and scene. A site picks a starting point whole, or a starting point with one layer changed, in its own guide and in the blueprint as `project.style.parts`: `{"background": "grain"}`, or `{"background": {"start": "detailed-ground", "drawings": "a-few"}}`. The pick wins over the feel guide for the background only; the feel guide still decides everything else. The general guide's accessibility minimums (contrast, text size, tap size) still hold whatever is picked.

**The background does not own the page's colour.** That is `--ground`, from the colour part (and, when guides are stacked, from the lead guide). Every layer here draws over `--ground` with the shared colour names only (`--ink`, `--mark`, `--accent`, `--surface`, `--texture-rgb`, `--texture-strength`, `--band-1` to `--band-3` and the rest; see "Parts, layers and the shared colour names" in the general guide), so the same layer works on a bright page and a dark one, and a detailed ground under a warm lead is a detailed ground in warm's colour, not in night blue. The tiles are masks: black shapes whose only job is their alpha, coloured in CSS by a shared name. A layer that looks right on one page and wrong on the other has a raw colour in it somewhere.

The background is the largest area on the page and the one a visitor looks at least. That is why it sets the feel so strongly.

**Words never sit on a busy ground.** Every layer above "none" keeps reading text on something calm laid over the ground: a sheet, a panel, a band of one colour, all `--surface` with `--ink`. The ground is what shows round them. `check` and `audit` measure text over a texture or a picture from a photograph of the page, and the worst of what lies under the words decides.

How the layers are built. Each layer is drawn behind the sections, inside `.page` (the wrapper of the sections), in this order from the back, each at its own `z-index` so the order holds however the page is written. Neither `.page` nor `.band` is a stacking layer of its own (no `isolation`, no `z-index`, no clipping of a band), so the light part's fixed layers (`z-index: 1`) lie over the bands and their drawings and under everything a reader needs, which stands at `z-index: 2` (see "Who draws where" in the general guide):

| From the back | Layer | Drawn on | Needs markup |
|---|---|---|---|
| -4 | scene: painted ground | `<div class="background-scene">` as the first thing in `.page` | yes, four empty `<i>` |
| -3 | pattern: stone courses | `main::before` (faces) and `main::after` (joints) | no |
| (on the band) | pattern: coloured bands | each `.band`'s own fill, its texture on `.band::after` | no |
| -2 | texture | `.page::before` | no |
| -1 | drawings: the small signs' tile | `.page::after` | no |
| 0 | drawings: hand-set signs, things to find, one long scene | inline SVG the site writes (`.background-sign`, `.background-find`, `.background-paint`), `aria-hidden` | yes |
| 0 | a band's texture | `.band::after`, over the band's drawings | no |
| (1) | the light part's lamp, sky and vignette | `body::before`, `body::after` | no |
| 2 | everything in a band a reader needs: headings, words, forms, sheets, panels | every child of a band not marked `aria-hidden="true"` | no |

So texture, pattern and the drawings' tile need nothing but the page's hooks; signs, finds and the scenes are art made for the site, placed by hand. `--ground` itself is painted by the colour part on the page's root element; nothing here paints it.

## Choosing

Start from a starting point (below), then change a layer if the brief asks for it.

| Starting point | What it feels like | Suits best | Fights |
|---|---|---|---|
| Plain | Clean, quiet, nothing between the reader and the words | Professional; artistic, when the signature carries the page | Warm, where it reads as a template |
| Coloured bands | Bold and flat, a poster in blocks | Warm; a shop with a dark lead | Professional, unless the colour is pale |
| Grain | Made, not printed; paper or plaster | Warm; artistic; a single maker | Little: it is the safest step up from plain |
| Material ground | The page is made of something from the subject | Warm; a dark, painterly lead | Professional |
| Painted ground | The picture's world, behind the panels | A game-style site | Anything meant to feel calm or official |
| Detailed ground | A full, lived-in room with something in every corner | A dark, painterly lead; artistic with a dense brief; a bright, busy community page | Professional; a spare brief; long forms |
| One long scene | A journey: the world changes as you scroll | A game-style site; a story told down one page | Long reading; many pages that share one layout |

How to choose: start from the brief's line on how full the page should feel. Spare points to plain or grain, balanced to grain, bands or a material, dense to a detailed ground or a long scene. Then ask what the site is made of: if the brief already names a material (see the materials part guide), the texture or pattern is usually that material. Then change single layers: a detailed ground that is too much for a long form keeps its texture and drops to `drawings: a-few`; a grain ground for a playful site can take `finds: on`. Only drawings, things to find and the two scenes need art made for the site; budget for it.

Light or dark is not a choice made here. Every layer is drawn from the shared names, so it follows the page the colour part sets; the "Light and dark" line on each option says what changes.

## Base

Whatever is picked: the page is positioned but never a stacking layer, so the texture and the tile at negative `z-index` lie over the colour part's ground and under every band, and the light part's layers can lie over the bands; its sides clip whatever runs off the edge (`overflow-x: clip`, never `overflow: hidden`, which breaks every sticky thing inside it); and `.page::before` is the texture layer, invisible until a texture option sets its mask and strength. The grain tile is here because grain, mottling and the grain on coloured bands all use it. The one roughening filter, for signs, finds and painted scenes, is drawn once at the top of `<body>`.

A band is positioned but never a stacking layer and never clips: the frames part draws the edge between sections on `.band::before`, poking above the band. What a band holds is stacked by number instead: its drawings (every one `aria-hidden="true"`) at 0, its texture over them, the light part's layers at 1, and every other child of the band (headings, words, a form, sheets, panels) at 2, so words keep their colour under any lamp or sky. The light part writes the same rule, so either part alone keeps it.

The background also owns the fill other parts ask for behind a section: `--background-alternate`, the fill of every other band when density alternates them, and `--background-patch` with `--background-patch-ink`, the calm patch density puts behind words straight on a band when the page is full. They are `--surface` and `--ink` here; an option that lays its own ground behind the bands changes them.

```css assemble
/* the grain tile (alpha only), drawn by tests/parts/source/background.py, which redraws it here */
& { --background-alternate: var(--surface); --background-patch: var(--surface); --background-patch-ink: var(--ink); }   /* what density lays behind a section or a heading */
& { --background-grain: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E %3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2.4 0 0 0 -0.95'/%3E%3C/filter%3E %3Crect width='240' height='240' filter='url(%23n)'/%3E%3C/svg%3E"); }
.page { position: relative; overflow-x: clip; }   /* positioned, never a stacking layer: the light part's layers lie over the bands */
.band { position: relative; }                      /* never a stacking layer, never clipped: frames' edge pokes above it */
:where(.band > :not([aria-hidden="true"])) { position: relative; z-index: 2; }   /* words, forms, sheets above the light (1); drawings below it */
.background-sign, .background-find, .background-scene { display: none; }   /* drawn only when their layer is picked */
.page::before { content: ""; position: absolute; inset: 0; z-index: -2; pointer-events: none;   /* the texture layer */
  background: rgb(var(--texture-rgb)); opacity: calc(var(--texture-strength) * var(--background-texture-amount, 0));
  mask: var(--background-texture-mask, linear-gradient(transparent, transparent)); }
```

```html assemble
<filter id="background-pen" x="-8%" y="-8%" width="116%" height="116%"><feTurbulence type="fractalNoise" baseFrequency="0.09" numOctaves="2" seed="4" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3" xChannelSelector="R" yChannelSelector="G"/></filter>
```

## Layers

### Texture
- Layer: texture
- Owns: the fine surface of the ground, seen close up: speckle, weave, mottling, hatching. From across the room the ground is still one colour.
- Default: none

#### None
- Id: none
- Status: draft
- Looks like: one flat colour behind everything. Sections are separated by space, and at most a hairline.
- Made with: `--ground`, from the colour part, and nothing else. Sections are told apart by a larger gap than anything inside them (density); one band (an "about" or a form) may take `--surface` where space alone does not group it.

```css assemble
/* texture: none. The ground is the colour part's --ground alone; the Base's texture layer stays invisible. */
```

- Careful: the easiest option for contrast, since each pair is measured once and holds everywhere. The risk is the template look: a pale ground with one accent is tell 7 in the general guide, and the first volunteer page, plain all over, was called "very plain ... like I made it with a cheap make-your-own-website tool". With every other layer also off, it works only when the signature piece and the repeated item are designed; it gives them the stage.
- Light and dark: nothing changes but `--ground` itself. On a dark page the difference between `--ground` and `--surface` is what tells a sheet from the page, so a hairline in `--line` round sheets helps more than on a light one.
- Personality: any
- Goes with: `frames: none` or `frames: hairline`; `materials: fine-paper`; `light: flat-and-even`.
- Used on: 4 mockups as the whole background (a tutoring site, a browser game's pages for deciding, a poetry site in its default look, the first version of a volunteer page), and under the bands, painted grounds and scenes of the others.

#### Grain
- Id: grain
- Status: draft
- Looks like: a fine speckle over the ground, like paper or plaster. Close up it is made; from across the room it is still one colour.
- Made with: a small SVG tile drawn by `feTurbulence`, whose `feColorMatrix` turns the noise into alpha only (`... 2.4 0 0 0 -0.95` on the last row, so only the specks are opaque). The tile is a mask over a layer of `rgb(var(--texture-rgb))`, at a strength set from `--texture-strength`: the texture colour is dark on a light page and light on a dark one, so the grain darkens one and lightens the other by itself. `stitchTiles='stitch'` makes the tile repeat without seams. A tile of 220 to 260 pixels was enough everywhere.

```css assemble
/* the Base's texture layer (.page::before) takes the grain tile; coloured bands read the same two values */
& { --background-texture-mask: var(--background-grain) 0 0 / 240px 240px; --background-texture-amount: 2.2; }
```

- Careful: words go on sheets, but text straight on grain at this strength passed the check on the mockups here; turn the strength up only with the check run again. A grain strong enough to show on a dark band once took soft text on a light sheet below 4.5:1, which is why the strength is one shared number per page and not set by eye per section. It is decoration, a background, so nothing needs hiding from screen readers. It costs the browser a little to draw.
- Light and dark: the same tile. On a light page it is dark specks at about a fifth; on a dark page light specks, a little stronger because `--texture-strength` is higher there (grain set for a light page looks muddy on a dark one). On a band it takes the band's ink instead (see coloured bands).
- Personality: calm, friendly, playful
- Goes with: `materials: paper-and-tape` or `materials: fine-paper`; `frames: torn-paper`; any light.
- Used on: 4 mockups as the ground (a soap maker's shop on warm paper, a poetry site in three of its alternative looks, a small shop on every band, a dark, painterly joke site over its wall). The most used layer after none.

#### Felt weave
- Id: felt-weave
- Status: draft
- Looks like: a faint, even dot weave, the felt of a noticeboard. Notes and sheets are pinned on it.
- Made with: a dot mask, one small `radial-gradient` repeated every 6 pixels, over a layer of `rgb(var(--texture-rgb))` at `--texture-strength`. The felt's own colour is `--ground`: a board-blue felt is the colour part setting a blue ground, not this layer.

```css assemble
/* a dot mask (only its alpha counts) on the Base's texture layer */
& { --background-texture-mask: radial-gradient(circle, black 1px, transparent 1.4px) 0 0 / 6px 6px; --background-texture-amount: 1.4; }
```

- Careful: keep the dots faint (on the volunteer page they were 7%) so pale words straight on the felt still pass; anything long goes on a note or a sheet. One material per page: the materials guide records that stone walls with a felt board read as stickers from different sets. This is the felt only; the pinned notes are `materials: cut-paper-on-felt`.
- Light and dark: dark dots on a light felt, light dots on a dark one. A strongly coloured felt (the volunteer page's blue) behaves like a dark page: the colour part sets `--texture-rgb` and `--ink` light on it.
- Personality: friendly, playful
- Goes with: `materials: cut-paper-on-felt`, always; `frames: torn-paper` for notes on it; `light: flat-and-even`.
- Used on: 1 mockup: a volunteer page (a felt noticeboard under the events).

#### Mottled and hatched
- Id: mottled-and-hatched
- Status: draft
- Looks like: an old, worked surface: slow, soft patches of shade, fine diagonal hatching, and grain over all of it. From across the room it is still one colour, with weather in it.
- Made with: two layers, each one job. Behind, a large mottling tile (`feTurbulence` with a stretched, low frequency such as `0.006 0.02`, its alpha only) over `rgb(var(--texture-rgb))`. In front, fine hatching (a repeating line every 7 pixels, turned) and the grain tile, over the same colour. Both take `--texture-strength`, so the surface shows on a dark page as well as a light one. Draw the mottling into a file or a data URI once; it is the heaviest part to render.

In the assembly code the two layers are one, the texture layer of the Base: the mottling at full strength, and the hatching and a softer grain tile at two thirds of it (a mask counts only alpha, so the hatching's two-thirds black is a `color-mix` and the soft grain is the grain tile with its alpha scaled), which is the swatch book's 2.4 and 1.6.

```css assemble
/* the mottling and the soft grain tiles (alpha only), drawn by tests/parts/source/background.py, which redraws them here */
& { --background-mottle: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='640' height='720'%3E %3Cfilter id='m' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.006 0.02' numOctaves='4' seed='6' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1.8 0 0 0 -0.55'/%3E%3C/filter%3E %3Crect width='640' height='720' filter='url(%23m)'/%3E%3C/svg%3E"); }
& { --background-grain-soft: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E %3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2.4 0 0 0 -0.95'/%3E%3CfeComponentTransfer%3E%3CfeFuncA type='linear' slope='0.67'/%3E%3C/feComponentTransfer%3E%3C/filter%3E %3Crect width='240' height='240' filter='url(%23n)'/%3E%3C/svg%3E"); }
& { --background-texture-amount: 2.4;
  --background-texture-mask: var(--background-mottle) 0 0 / 640px 720px,
    repeating-linear-gradient(128deg, color-mix(in srgb, black 67%, transparent) 0 1px, transparent 1px 7px),
    var(--background-grain-soft) 0 0 / 240px 240px; }
```

- Careful: this is the texture of the detailed ground; on its own it is already a lot. Reading text never sits on it. Measure the whole page: on the first detailed ground, after the owner asked for more calm sheets, the whole-page picture was 58% dark ground and 40% sheet (it had been 94% ground). Bake the mottling into one file; keep live filters for a few things.
- Light and dark: on a light page the patches are soft brown-grey stains and the hatching shows as pencil; it reads as old paper. On a dark page the patches are pale smoke over the dark ground and the hatching and grain are light scratches: a worn wall at night. The dark copy is the stronger of the two; if it is too much, lower `--texture-strength` for the dark page in the colour part, not here.
- Personality: dramatic, playful
- Goes with: `materials: parchment-and-ink` or `materials: stone-and-chalk`; `light: one-light`; `background: drawings lots`.
- Used on: 3 mockups, all under a detailed ground (a dark, painterly joke site, a small shop with a dark lead, a game-style joke site).

### Pattern
- Layer: pattern
- Owns: large shapes repeated across the ground or from section to section: bands of colour, courses of stone. Not the edge between sections, which is the frames part.
- Default: none

#### None
- Id: none
- Status: draft
- Looks like: no large shapes; the ground is one field, with whatever texture is picked.
- Made with: nothing.

```css assemble
/* pattern: none. No large shapes behind the sections. */
```

- Careful: none.
- Light and dark: nothing changes.
- Personality: any
- Goes with: `background: texture grain`; any frames.
- Used on: most mockups.

#### Coloured bands
- Id: coloured-bands
- Status: draft
- Looks like: each section sits on a whole band of a strong colour, edge to edge: deep red, then forest green, then night. The page reads as a poster in blocks. With grain on top, every band is one material, and pale words can sit straight on a band.
- Made with: the colour part's band colours, `--band-1`, `--band-2` and `--band-3`, set on full-width sections in turn, with `--on-band` for the words straight on them. Buttons and long text still go on a `--surface` sheet. For a pale, tinted band (the quiet end of this option) the colour part sets the band colours pale and `--on-band` dark. A shaped edge between bands (a wave, a torn edge) comes from the frames part guide.

**Texture on a band takes the band's ink.** Grain, weave or mottling laid over a band is coloured `--on-band`, not `rgb(var(--texture-rgb))`: `--texture-rgb` is made for the ground, so on a light page it is dark, and so are deep bands, and the grain vanishes. `--on-band` is pale on deep bands and dark on pale ones, so the texture always shows, on a light page and a dark one, and with `bands: none` it is the words on the ground, the same as before. The strength is still `--texture-strength`; no new name is needed.

The band takes whatever texture is picked (none, grain, felt or mottling), from the two values the texture option sets, so `pattern: coloured-bands; texture: none` is flat bands. The padding is density's section gap, read and not set. The sheet on a band gets back the ink, since the band's words are `--on-band`; its fill is the materials part's.

```css assemble
.band { position: relative; color: var(--on-band); padding-block: var(--gap-groups, 2rem); }   /* not isolated: the light part's lamp lies over the bands */
.band:nth-of-type(3n+1) { background-color: var(--band-1); }
.band:nth-of-type(3n+2) { background-color: var(--band-2); }
.band:nth-of-type(3n)   { background-color: var(--band-3); }
.band::after { content: ""; position: absolute; inset: 0; z-index: 0; pointer-events: none;   /* texture takes the band's ink: over the band's drawings, under its words (2) */
  background: var(--on-band); opacity: calc(var(--texture-strength) * var(--background-texture-amount, 0));
  mask: var(--background-texture-mask, linear-gradient(transparent, transparent)); }
.band .sheet, .band .panel { color: var(--ink); }   /* buttons and long text sit on these */
```

- Careful: bold colour widens the general guide's three colours but never lifts the contrast minimums: `--on-band` is measured against every band, with the grain on it (`audit` does this from a picture). A grain strong enough to show on a dark band can pull pale words down; one shop needed a lighter grain for its parchment than for its bands. The warm guide's "bold and flat" was read on one shop as "one solid hue, no gradient", with grain allowed.
- Light and dark: the bands are deep on both; on a dark page the colour part sets them a little deeper still, so they do not glow against the dark ground round them. `--on-band` stays pale on both, and so the grain on the bands is pale specks on both: fainter on the light page's bands, which are a little lighter, and stronger on the dark page's, where `--texture-strength` is higher. On pale bands it turns to dark specks by itself.
- Personality: friendly, playful
- Goes with: `frames: wavy-edge` or `frames: torn-paper` between bands; `materials: wood-and-canvas`; `density: balanced`; `background: texture grain`.
- Used on: 3 mockups: a small shop (three deep bands with grain), a volunteer page (a yellow poster block over a blue board), and a tutoring site (one pale tinted band, the quiet end of this option).

#### Stone courses
- Id: stone-courses
- Status: draft
- Looks like: a wall of dressed stone behind everything: courses of blocks in near shades of the ground, mortar lines between them, a crack or two.
- Made with: two mask tiles drawn once by a script, about 420 by 208: the block faces (rectangles at three or four alphas) over `rgb(var(--texture-rgb))` at `--texture-strength`, so each block is a near shade of the ground; and the joints (lines and a crack) over `rgb(var(--shadow-rgb))`. Draw every block that crosses the tile's edge again one tile across, so the wall repeats without a seam. Grain over it is the texture layer.

The wall is drawn on `main`'s two pseudo-elements, behind the texture; a page with no `<main>` puts the two rules on its own wrapper of the sections.

```css assemble
/* the block faces and the joints (alpha only), drawn by tests/parts/source/background.py, which redraws them here */
& { --background-stone-faces: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='420' height='208'%3E%3Crect x='0' y='0' width='109' height='52' opacity='0.35'/%3E%3Crect x='109' y='0' width='114' height='52' opacity='0.15'/%3E%3Crect x='223' y='0' width='94' height='52' opacity='0.15'/%3E%3Cg transform='translate(-420 0)'%3E%3Crect x='317' y='0' width='112' height='52' opacity='0.15'/%3E%3C/g%3E%3Crect x='317' y='0' width='112' height='52' opacity='0.15'/%3E%3Crect x='-82' y='52' width='103' height='52' opacity='0.15'/%3E%3Cg transform='translate(420 0)'%3E%3Crect x='-82' y='52' width='103' height='52' opacity='0.15'/%3E%3C/g%3E%3Crect x='21' y='52' width='116' height='52' opacity='0.15'/%3E%3Crect x='137' y='52' width='104' height='52' opacity='0.80'/%3E%3Crect x='241' y='52' width='94' height='52' opacity='0.15'/%3E%3Cg transform='translate(-420 0)'%3E%3Crect x='335' y='52' width='147' height='52' opacity='0.15'/%3E%3C/g%3E%3Crect x='335' y='52' width='147' height='52' opacity='0.15'/%3E%3Crect x='0' y='104' width='125' height='52' opacity='0.80'/%3E%3Crect x='125' y='104' width='93' height='52' opacity='0.35'/%3E%3Crect x='218' y='104' width='93' height='52' opacity='0.35'/%3E%3Crect x='310' y='104' width='107' height='52' opacity='0.35'/%3E%3Cg transform='translate(-420 0)'%3E%3Crect x='418' y='104' width='122' height='52' opacity='0.55'/%3E%3C/g%3E%3Crect x='418' y='104' width='122' height='52' opacity='0.55'/%3E%3Crect x='-50' y='156' width='131' height='52' opacity='0.15'/%3E%3Cg transform='translate(420 0)'%3E%3Crect x='-50' y='156' width='131' height='52' opacity='0.15'/%3E%3C/g%3E%3Crect x='80' y='156' width='125' height='52' opacity='0.35'/%3E%3Crect x='205' y='156' width='112' height='52' opacity='0.15'/%3E%3Cg transform='translate(-420 0)'%3E%3Crect x='318' y='156' width='124' height='52' opacity='0.35'/%3E%3C/g%3E%3Crect x='318' y='156' width='124' height='52' opacity='0.35'/%3E%3C/svg%3E"); }
& { --background-stone-joints: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='420' height='208'%3E%3Cg fill='none' stroke='black' stroke-width='3'%3E%3Cpath d='M0 0H420'/%3E%3Cpath d='M109 0V52'/%3E%3Cpath d='M223 0V52'/%3E%3Cpath d='M317 0V52'/%3E%3Cpath d='M0 52H420'/%3E%3Cpath d='M21 52V104'/%3E%3Cpath d='M137 52V104'/%3E%3Cpath d='M241 52V104'/%3E%3Cpath d='M335 52V104'/%3E%3Cpath d='M0 104H420'/%3E%3Cpath d='M125 104V156'/%3E%3Cpath d='M218 104V156'/%3E%3Cpath d='M310 104V156'/%3E%3Cpath d='M418 104V156'/%3E%3Cpath d='M0 156H420'/%3E%3Cpath d='M80 156V208'/%3E%3Cpath d='M205 156V208'/%3E%3Cpath d='M318 156V208'/%3E%3Cpath d='M200 60l14 18l-6 14l12 18' stroke-width='1.5'/%3E%3C/g%3E%3C/svg%3E"); }
main::before, main::after { content: ""; position: absolute; inset: 0; z-index: -3; pointer-events: none; }
main::before { background: rgb(var(--texture-rgb)); opacity: var(--texture-strength); mask: var(--background-stone-faces) 0 0 / 420px 208px; }
main::after  { background: rgb(var(--shadow-rgb)); opacity: calc(var(--shadow-strength) * 2); mask: var(--background-stone-joints) 0 0 / 420px 208px; }
```

- Careful: keep the faces faint, so pale words straight on the wall still pass; anything long goes on a sheet. One material per page. Stone with signs drawn on it has become the detailed ground's wall; that is this pattern with `drawings: lots`.
- Light and dark: on a light page a pale limestone wall with grey joints; on a dark page the faces lighten a little and the joints go near black, so it reads as a wall at night.
- Personality: dramatic, serious
- Goes with: `materials: stone-and-chalk`, always; `light: one-light`; `frames: carved-plate`.
- Used on: 1 mockup: a dark, painterly joke site (a wall of dressed stone, which became its detailed ground).

### Drawings
- Layer: drawings
- Owns: signs drawn by hand on the ground: circles with stars and triangles in them, a moon and an orbit, a written line in made-up letters, a branching mark. Never anything with meaning.
- Default: none

#### None
- Id: none
- Status: draft
- Looks like: nothing drawn on the ground.
- Made with: nothing.

```css assemble
/* drawings: none. Nothing drawn on the ground. */
```

- Careful: none.
- Light and dark: nothing changes.
- Personality: any
- Goes with: any.
- Used on: most mockups.

#### A few
- Id: a-few
- Status: draft
- Looks like: three to six large signs (90 to 240 pixels), each set by hand: one runs off the edge of the page, one sits half under a sheet, one crosses the band between sections. The rest of the ground is quiet.
- Made with: inline SVG that `use` a handful of shared symbols, each placed in the stylesheet with its own width, position and turn. The lines are `currentColor` with `color: var(--mark)` at about half strength, roughened by one displacement filter so no line is machine-straight. The symbols and the filter are drawn once, at the top of the page.

Each sign is placed by the site, in the gap it is meant for, with its own `style` (or a class of the site's own): `<svg class="background-sign" style="width: 150px; left: -6%; top: 52%; rotate: 14deg" viewBox="0 0 100 100" aria-hidden="true" focusable="false"><use href="#background-sg-ring"/></svg>`, inside `.page` or a `.band`. The five signs of the swatch book come with it, as symbols; a site draws its own in the same way.

- Needs markup: three to six `<svg class="background-sign" style="width: 150px; left: -6%; top: 52%; rotate: 14deg" viewBox="0 0 100 100" aria-hidden="true" focusable="false"><use href="#background-sg-ring"/></svg>` (or `-diamond`, `-rose`, `-tree`, `-moon`, or the site's own symbol), each placed first inside the `.band` (or `.page`) whose gap it sits in; the symbols and the pen filter come in `parts.js`.

```css assemble
.background-sign { display: block; position: absolute; z-index: 0; max-width: none; height: auto; pointer-events: none; fill: none;
  stroke: currentColor; stroke-width: 2; stroke-linecap: round; filter: url(#background-pen); color: var(--mark); opacity: 0.6; }
.background-sign * { vector-effect: non-scaling-stroke; }       /* the same line weight at any size */
```

```html assemble
<symbol id="background-sg-ring" viewBox="0 0 100 100"><circle cx="50" cy="52" r="45"/><path d="M50 10L88 76H12Z"/><circle cx="50" cy="54" r="12"/><path d="M50 34V26M34 62L27 66M66 62L73 66"/></symbol>
<symbol id="background-sg-diamond" viewBox="0 0 100 100"><circle cx="50" cy="50" r="46"/><path d="M50 4L96 50L50 96L4 50Z"/><circle cx="50" cy="50" r="30"/><circle cx="50" cy="50" r="3"/></symbol>
<symbol id="background-sg-rose" viewBox="0 0 100 100"><path d="M50 12V88M12 50H88M24 24L76 76M76 24L24 76"/><circle cx="50" cy="50" r="13"/><circle cx="50" cy="7" r="5"/><circle cx="93" cy="50" r="5"/><circle cx="50" cy="93" r="5"/><circle cx="7" cy="50" r="5"/></symbol>
<symbol id="background-sg-tree" viewBox="0 0 100 100"><path d="M30 86V70M30 60V46M30 36V20"/><circle cx="30" cy="91" r="5"/><circle cx="30" cy="65" r="5"/><circle cx="30" cy="41" r="5"/><circle cx="30" cy="15" r="5"/><path d="M34 62C50 58 62 54 62 42"/><circle cx="62" cy="37" r="5"/><path d="M62 32C62 22 44 18 35 15M66 34C78 30 86 26 86 16"/><circle cx="86" cy="11" r="5"/></symbol>
<symbol id="background-sg-moon" viewBox="0 0 100 100"><path d="M58 14A36 36 0 1 0 58 86A28 28 0 1 1 58 14Z"/><ellipse cx="50" cy="50" rx="48" ry="14"/><circle cx="84" cy="22" r="3"/></symbol>
```

- Careful:
  - A sign is never over words or a control: signs sit behind them (`z-index: 0`, where the words of a band stand at 2), and all have `pointer-events: none`. A sign placed straight in `.page` goes before the bands, so they cover it where they have a fill.
  - Every sign is `aria-hidden="true"` and `focusable="false"`; none carries meaning. `--mark` is for decoration only.
  - Signs that run off the edge are clipped by `overflow-x: clip` on one full-width wrapper. `overflow: hidden` there breaks every sticky thing inside it (see `css-layout.md`).
  - On a phone there is almost no ground to draw on (about 12 pixels each side): keep a sign or two as slivers at the edges.
- Light and dark: the signs are `--mark`: a brown pencil on a light page, a pale chalk on a dark one. On a light page they can go a little stronger (0.6 to 0.7), since a light mark on a dark ground shows more at the same strength.
- Personality: friendly, playful, dramatic
- Goes with: `background: texture grain`; `frames: inked-panel`; `density: balanced`.
- Used on: the quieter parts of the 3 detailed grounds (their forms and footers kept one sign each), and the earlier game-style joke site, whose scattered signs over painted strokes were the first try at it.

#### Lots
- Id: lots
- Status: draft
- Looks like: something in every corner. Small signs scattered all over the ground in one repeating tile, specks between them, and over that ten to thirty larger signs set by hand, some running off the page, some half under a sheet, one in ink in a sheet's margin.
- Made with: the hand-set signs of "a few", more of them, plus a large mask tile drawn by a script, 640 by 720 or larger (the shop used 1400 by 2200, so the repeat is never seen): about one small sign for every 200 by 200 pixels, each its own size (14 to 58), turn and strength, no two closer than about 150 pixels, all roughened by one displacement filter, with a few hundred specks. The tile is a mask over `--mark`.

The tile needs no markup: it is `.page::after`, over the texture. The hand-set signs are those of "a few"; a sign in a sheet's corner takes `background-sign background-in-margin` (the sheet needs `position: relative`), and one kept as a sliver at a phone's edge `background-sign background-sliver`.

- Needs markup: ten to thirty hand-set signs as in "a few" (`<svg class="background-sign" ... aria-hidden="true" focusable="false"><use href="#background-sg-..."/></svg>`); one inside a sheet's corner takes `class="background-sign background-in-margin"`, one kept at a phone's edge `background-sign background-sliver`. The tile of small signs needs nothing.

```css assemble
/* the small signs' tile (alpha only), drawn by tests/parts/source/background.py, which redraws it here */
& { --background-signs: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='640' height='720'%3E %3Cfilter id='r'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.05' numOctaves='2' seed='12'/%3E%3CfeDisplacementMap in='SourceGraphic' scale='3'/%3E%3C/filter%3E %3Cg opacity='0.5'%3E%3Ccircle cx='633' cy='569' r='1.1'/%3E%3Ccircle cx='124' cy='436' r='0.9'/%3E%3Ccircle cx='517' cy='521' r='0.9'/%3E%3Ccircle cx='624' cy='58' r='0.7'/%3E%3Ccircle cx='301' cy='243' r='1.1'/%3E%3Ccircle cx='631' cy='439' r='0.6'/%3E%3Ccircle cx='582' cy='248' r='1.2'/%3E%3Ccircle cx='534' cy='86' r='1.0'/%3E%3Ccircle cx='455' cy='144' r='1.5'/%3E%3Ccircle cx='278' cy='458' r='0.7'/%3E%3Ccircle cx='606' cy='520' r='1.1'/%3E%3Ccircle cx='476' cy='61' r='0.8'/%3E%3Ccircle cx='636' cy='20' r='1.2'/%3E%3Ccircle cx='298' cy='472' r='1.2'/%3E%3Ccircle cx='381' cy='342' r='1.5'/%3E%3Ccircle cx='100' cy='395' r='0.6'/%3E%3Ccircle cx='512' cy='523' r='0.7'/%3E%3Ccircle cx='480' cy='100' r='1.6'/%3E%3Ccircle cx='125' cy='629' r='0.6'/%3E%3Ccircle cx='136' cy='361' r='1.4'/%3E%3Ccircle cx='209' cy='392' r='1.4'/%3E%3Ccircle cx='39' cy='533' r='1.5'/%3E%3Ccircle cx='424' cy='587' r='1.1'/%3E%3Ccircle cx='529' cy='632' r='0.7'/%3E%3Ccircle cx='97' cy='368' r='1.5'/%3E%3Ccircle cx='497' cy='438' r='1.4'/%3E%3Ccircle cx='96' cy='102' r='1.2'/%3E%3Ccircle cx='77' cy='44' r='1.3'/%3E%3Ccircle cx='340' cy='347' r='1.4'/%3E%3Ccircle cx='565' cy='41' r='0.8'/%3E%3Ccircle cx='27' cy='70' r='1.1'/%3E%3Ccircle cx='18' cy='644' r='0.7'/%3E%3Ccircle cx='208' cy='701' r='1.2'/%3E%3Ccircle cx='128' cy='200' r='1.1'/%3E%3Ccircle cx='517' cy='366' r='0.8'/%3E%3Ccircle cx='335' cy='631' r='1.5'/%3E%3Ccircle cx='591' cy='643' r='0.8'/%3E%3Ccircle cx='286' cy='300' r='1.0'/%3E%3Ccircle cx='202' cy='483' r='1.0'/%3E%3Ccircle cx='136' cy='218' r='0.7'/%3E%3Ccircle cx='497' cy='676' r='1.2'/%3E%3Ccircle cx='234' cy='182' r='0.7'/%3E%3Ccircle cx='299' cy='538' r='0.7'/%3E%3Ccircle cx='566' cy='117' r='1.3'/%3E%3Ccircle cx='143' cy='509' r='1.6'/%3E%3Ccircle cx='258' cy='303' r='1.0'/%3E%3Ccircle cx='59' cy='263' r='0.9'/%3E%3Ccircle cx='294' cy='506' r='1.0'/%3E%3Ccircle cx='331' cy='213' r='1.6'/%3E%3Ccircle cx='72' cy='661' r='0.8'/%3E%3Ccircle cx='561' cy='61' r='0.9'/%3E%3Ccircle cx='580' cy='131' r='1.4'/%3E%3Ccircle cx='525' cy='612' r='1.3'/%3E%3Ccircle cx='605' cy='292' r='1.1'/%3E%3Ccircle cx='329' cy='356' r='0.9'/%3E%3Ccircle cx='179' cy='576' r='0.8'/%3E%3Ccircle cx='573' cy='194' r='0.6'/%3E%3Ccircle cx='57' cy='188' r='1.2'/%3E%3Ccircle cx='142' cy='190' r='0.7'/%3E%3Ccircle cx='7' cy='716' r='1.0'/%3E%3Ccircle cx='586' cy='448' r='0.6'/%3E%3Ccircle cx='454' cy='675' r='1.6'/%3E%3Ccircle cx='168' cy='130' r='1.5'/%3E%3Ccircle cx='402' cy='382' r='0.8'/%3E%3Ccircle cx='285' cy='484' r='0.9'/%3E%3Ccircle cx='514' cy='716' r='0.6'/%3E%3Ccircle cx='12' cy='364' r='1.6'/%3E%3Ccircle cx='329' cy='177' r='1.0'/%3E%3Ccircle cx='421' cy='468' r='1.3'/%3E%3Ccircle cx='349' cy='640' r='1.6'/%3E%3Ccircle cx='197' cy='155' r='0.8'/%3E%3Ccircle cx='127' cy='635' r='1.3'/%3E%3Ccircle cx='89' cy='712' r='1.6'/%3E%3Ccircle cx='536' cy='10' r='1.2'/%3E%3Ccircle cx='563' cy='310' r='0.7'/%3E%3Ccircle cx='426' cy='274' r='1.1'/%3E%3Ccircle cx='621' cy='431' r='1.3'/%3E%3Ccircle cx='29' cy='133' r='0.9'/%3E%3Ccircle cx='2' cy='262' r='0.9'/%3E%3Ccircle cx='630' cy='233' r='0.6'/%3E%3Ccircle cx='565' cy='157' r='0.8'/%3E%3Ccircle cx='215' cy='60' r='0.9'/%3E%3Ccircle cx='420' cy='179' r='1.4'/%3E%3Ccircle cx='58' cy='588' r='0.7'/%3E%3Ccircle cx='376' cy='284' r='0.9'/%3E%3Ccircle cx='403' cy='61' r='1.6'/%3E%3Ccircle cx='546' cy='112' r='1.5'/%3E%3Ccircle cx='502' cy='430' r='1.4'/%3E%3Ccircle cx='461' cy='356' r='0.9'/%3E%3Ccircle cx='396' cy='104' r='1.4'/%3E%3Ccircle cx='458' cy='369' r='1.0'/%3E%3Ccircle cx='449' cy='364' r='1.5'/%3E%3Ccircle cx='482' cy='409' r='1.4'/%3E%3Ccircle cx='10' cy='494' r='1.4'/%3E%3Ccircle cx='455' cy='688' r='1.2'/%3E%3Ccircle cx='54' cy='30' r='1.2'/%3E%3Ccircle cx='614' cy='271' r='1.1'/%3E%3Ccircle cx='32' cy='14' r='1.1'/%3E%3Ccircle cx='157' cy='190' r='1.1'/%3E%3Ccircle cx='45' cy='671' r='1.5'/%3E%3Ccircle cx='59' cy='379' r='1.3'/%3E%3Ccircle cx='303' cy='583' r='1.4'/%3E%3Ccircle cx='150' cy='545' r='0.8'/%3E%3Ccircle cx='416' cy='331' r='1.4'/%3E%3Ccircle cx='49' cy='656' r='0.9'/%3E%3Ccircle cx='30' cy='456' r='0.8'/%3E%3Ccircle cx='384' cy='239' r='1.3'/%3E%3Ccircle cx='443' cy='447' r='0.7'/%3E%3Ccircle cx='309' cy='350' r='1.6'/%3E%3Ccircle cx='64' cy='157' r='1.1'/%3E%3Ccircle cx='454' cy='206' r='1.1'/%3E%3Ccircle cx='491' cy='715' r='1.1'/%3E%3Ccircle cx='199' cy='62' r='1.1'/%3E%3Ccircle cx='185' cy='55' r='1.1'/%3E%3Ccircle cx='637' cy='716' r='1.0'/%3E%3Ccircle cx='587' cy='670' r='0.7'/%3E%3Ccircle cx='58' cy='538' r='0.9'/%3E%3Ccircle cx='230' cy='434' r='1.2'/%3E%3Ccircle cx='179' cy='81' r='1.0'/%3E%3Ccircle cx='319' cy='631' r='1.0'/%3E%3C/g%3E %3Cg filter='url(%23r)' fill='none' stroke='black' stroke-linecap='round'%3E%3Cg transform='translate(318 379) rotate(168)' stroke-width='1.7' opacity='0.97'%3E%3Ccircle r='34'/%3E%3Ccircle r='27'/%3E%3Cpath d='M27 0L34 0'/%3E%3Cpath d='M23 13L30 17'/%3E%3Cpath d='M13 23L17 30'/%3E%3Cpath d='M0 27L0 34'/%3E%3Cpath d='M-13 23L-17 30'/%3E%3Cpath d='M-23 13L-30 17'/%3E%3Cpath d='M-27 0L-34 0'/%3E%3Cpath d='M-23 -13L-30 -17'/%3E%3Cpath d='M-13 -23L-17 -30'/%3E%3Cpath d='M-0 -27L-0 -34'/%3E%3Cpath d='M13 -23L17 -30'/%3E%3Cpath d='M23 -13L30 -17'/%3E%3Cpath d='M0 -21L17 14L-17 14Z'/%3E%3C/g%3E%3Cg transform='translate(248 209) rotate(281)' stroke-width='1.2' opacity='0.59'%3E%3Cpath d='M0 -19V19M0 -7L10 -19M0 0L-9 8'/%3E%3C/g%3E%3Cg transform='translate(377 104) rotate(59)' stroke-width='1.4' opacity='0.70'%3E%3Cpath d='M8 -27a27 27 0 1 0 0 55a20 20 0 1 1 0 -55'/%3E%3Cellipse rx='44' ry='14'/%3E%3C/g%3E%3Cg transform='translate(545 313) rotate(28)' stroke-width='2.0' opacity='0.80'%3E%3Cpath d='M-62 -8v16l8 -8l-8 -8'/%3E%3Cpath d='M-47 -8v16l8 -8l-8 -8'/%3E%3Cpath d='M-32 -8v16l8 -8l-8 -8'/%3E%3Cpath d='M-17 -8l9 16M-8 -8l-9 16'/%3E%3Cpath d='M-2 -8l9 16M7 -8l-9 16'/%3E%3Cpath d='M13 -8v16M13 -4l7 -4'/%3E%3Cpath d='M28 -8v16M28 -4l7 -4'/%3E%3Cpath d='M43 -8v16l8 -8l-8 -8'/%3E%3Cpath d='M58 -8l9 16M67 -8l-9 16'/%3E%3C/g%3E%3Cg transform='translate(427 652) rotate(137)' stroke-width='1.6' opacity='0.65'%3E%3Ccircle r='32'/%3E%3Cpath d='M0 -32L14 29L-25 -20L31 7L-31 7L25 -20L-14 29Z'/%3E%3C/g%3E%3Cg transform='translate(103 151) rotate(4)' stroke-width='1.6' opacity='0.92'%3E%3Ccircle r='31'/%3E%3Ccircle r='24'/%3E%3Cpath d='M24 0L31 0'/%3E%3Cpath d='M21 12L27 16'/%3E%3Cpath d='M12 21L16 27'/%3E%3Cpath d='M0 24L0 31'/%3E%3Cpath d='M-12 21L-16 27'/%3E%3Cpath d='M-21 12L-27 16'/%3E%3Cpath d='M-24 0L-31 0'/%3E%3Cpath d='M-21 -12L-27 -16'/%3E%3Cpath d='M-12 -21L-16 -27'/%3E%3Cpath d='M-0 -24L-0 -31'/%3E%3Cpath d='M12 -21L16 -27'/%3E%3Cpath d='M21 -12L27 -16'/%3E%3Cpath d='M0 -19L16 12L-16 12Z'/%3E%3C/g%3E%3Cg transform='translate(136 381) rotate(115)' stroke-width='1.5' opacity='0.61'%3E%3Cpath d='M0 -30V30M0 -12L16 -30M0 0L-15 13'/%3E%3C/g%3E%3Cg transform='translate(555 468) rotate(143)' stroke-width='1.4' opacity='0.73'%3E%3Cpath d='M9 -29a29 29 0 1 0 0 57a21 21 0 1 1 0 -57'/%3E%3Cellipse rx='46' ry='14'/%3E%3C/g%3E%3Cg transform='translate(159 651) rotate(40)' stroke-width='1.3' opacity='0.82'%3E%3Cpath d='M-41 -8v16M-41 -4l7 -4'/%3E%3Cpath d='M-26 -8v16M-26 -4l7 -4'/%3E%3Cpath d='M-11 8l5 -16l5 16'/%3E%3Cpath d='M4 -8v16M4 -4l7 -4'/%3E%3Cpath d='M19 -8v16l8 -8l-8 -8'/%3E%3Cpath d='M34 -8v16M34 -4l7 -4'/%3E%3C/g%3E%3Cg transform='translate(268 542) rotate(177)' stroke-width='1.2' opacity='0.88'%3E%3Ccircle r='19'/%3E%3Cpath d='M0 -19L8 17L-15 -12L19 4L-19 4L15 -12L-8 17Z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E"); }
.page::after { content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background: var(--mark); opacity: 0.45; mask: var(--background-signs) 0 0 / 640px 720px; }
.background-sign { display: block; position: absolute; z-index: 0; max-width: none; height: auto; pointer-events: none; fill: none;
  stroke: currentColor; stroke-width: 2; stroke-linecap: round; filter: url(#background-pen); color: var(--mark); opacity: 0.6; }
.background-sign * { vector-effect: non-scaling-stroke; }
.background-sign.background-in-margin { z-index: 1; width: 56px; right: -14px; bottom: -16px; rotate: 12deg; opacity: 0.7; }   /* a sheet's corner, clear of the words */
@media (max-width: 47.99rem) { .background-sign:not(.background-sliver, .background-in-margin) { display: none; } }
```

```html assemble
<symbol id="background-sg-ring" viewBox="0 0 100 100"><circle cx="50" cy="52" r="45"/><path d="M50 10L88 76H12Z"/><circle cx="50" cy="54" r="12"/><path d="M50 34V26M34 62L27 66M66 62L73 66"/></symbol>
<symbol id="background-sg-diamond" viewBox="0 0 100 100"><circle cx="50" cy="50" r="46"/><path d="M50 4L96 50L50 96L4 50Z"/><circle cx="50" cy="50" r="30"/><circle cx="50" cy="50" r="3"/></symbol>
<symbol id="background-sg-rose" viewBox="0 0 100 100"><path d="M50 12V88M12 50H88M24 24L76 76M76 24L24 76"/><circle cx="50" cy="50" r="13"/><circle cx="50" cy="7" r="5"/><circle cx="93" cy="50" r="5"/><circle cx="50" cy="93" r="5"/><circle cx="7" cy="50" r="5"/></symbol>
<symbol id="background-sg-tree" viewBox="0 0 100 100"><path d="M30 86V70M30 60V46M30 36V20"/><circle cx="30" cy="91" r="5"/><circle cx="30" cy="65" r="5"/><circle cx="30" cy="41" r="5"/><circle cx="30" cy="15" r="5"/><path d="M34 62C50 58 62 54 62 42"/><circle cx="62" cy="37" r="5"/><path d="M62 32C62 22 44 18 35 15M66 34C78 30 86 26 86 16"/><circle cx="86" cy="11" r="5"/></symbol>
<symbol id="background-sg-moon" viewBox="0 0 100 100"><path d="M58 14A36 36 0 1 0 58 86A28 28 0 1 1 58 14Z"/><ellipse cx="50" cy="50" rx="48" ry="14"/><circle cx="84" cy="22" r="3"/></symbol>
```

- Careful:
  - Everything under "a few" holds, and more so. The form, its fields and the footer stay calm, each with at most one sign in a corner.
  - On a phone, hide most large signs below 48rem; let the small tile and the margin marks do the work. Widen the gaps and let more appear from 48rem and 62rem.
  - On the first mockup there were twenty-eight hand-set signs of nine kinds; the owner asked for more signs "drawn in random places" and then approved it.
  - Speed: bake the tile into one file; keep live filters for the hand-set signs. Not yet tried on a slow phone.
  - Under a warm lead, keep the fullness but draw warm's things (cut paper, bunting, members' drawings) in place of chalk signs.
- Light and dark: on a light page the tile and signs are a brown pencil over a pale ground and read as a sketchbook or a workshop wall; on a dark page they are chalk on a dark wall. The strength is the same; check on the light page that the tile does not turn the ground grey.
- Personality: playful, dramatic
- Goes with: `background: texture mottled-and-hatched`; `materials: parchment-and-ink`; `frames: inked-panel`; `lettering: bladed-letters`; `density: busy`.
- Used on: 3 mockups, all detailed grounds: a dark, painterly joke site (chalk signs on a stone wall), a small shop with a dark lead (signs on oxblood with grain and hatching), a game-style joke site (signs and sign-circles over painted strokes).

### Things to find
- Layer: finds
- Owns: small drawings hidden in the gaps for a visitor to notice: objects from the subject, drawn for the site.
- Default: off

#### Off
- Id: off
- Status: draft
- Looks like: nothing hidden.
- Made with: nothing.

```css assemble
/* finds: off. Nothing hidden in the gaps. */
```

- Careful: none.
- Light and dark: nothing changes.
- Personality: any
- Goes with: any.
- Used on: most mockups.

#### On
- Id: on
- Status: draft
- Looks like: three to six little drawings in the gaps beside the sheets, about 4 to 13rem wide: a ring of keys, a row of bottles, an inkpot with a quill, a bird on a bracket. An object from the subject, never a stock icon.
- Made with: inline SVG, lines in `currentColor` with `color: var(--mark)`, fills mixed from the shared names, roughened by the same filter as the signs. They appear only where there is a gap to hold them, from about 48rem, and a heading beside one is narrowed to make room.

Each find is the site's own drawing, placed by the site: `<svg class="background-find" style="width: 6rem; right: 9%; bottom: 1rem" viewBox="..." aria-hidden="true" focusable="false"><g filter="url(#background-pen)">...</g></svg>`, its shapes filled with the three classes below.

- Needs markup: three to six of the site's own drawings, `<svg class="background-find" style="width: 6rem; right: 9%; bottom: 1rem" viewBox="..." aria-hidden="true" focusable="false"><g filter="url(#background-pen)">...</g></svg>`, each inside the `.band` whose gap holds it, its shapes classed `background-solid`, `background-fill-a`, `-b` or `-c`.

```css assemble
.background-find { display: none; position: absolute; z-index: 0; max-width: none; height: auto; pointer-events: none; color: var(--mark);
  fill: none; stroke: currentColor; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }
.background-find .background-solid { fill: currentColor; }
.background-find .background-fill-a { fill: color-mix(in oklab, var(--mark) 45%, var(--ground)); }
.background-find .background-fill-b { fill: color-mix(in oklab, var(--accent) 45%, var(--ground)); }
.background-find .background-fill-c { fill: color-mix(in oklab, var(--surface-raised) 70%, var(--mark)); }
@media (min-width: 48rem) { .background-find { display: block; } }   /* only where there is a gap to hold them */
```

- Careful: every drawing is `aria-hidden="true"` and `focusable="false"`; if a find is a game (click the keys), it is a real button with a name, and then it is not this layer. Never place one over words or a control. On a phone there is no gap: hide them below 48rem.
- Light and dark: fills are mixed into `--ground`, so they sit back on either page: soft browns and greens on a light page, dull bronze on a dark one. Lines are the mark, as for drawings.
- Personality: friendly, playful, dramatic
- Goes with: `background: drawings lots`; `density: busy` or `density: full-but-quiet`.
- Used on: the detailed grounds; the first (a dark, painterly joke site) had keys, bottles, an inkpot and a bird in its gaps.

### Scene
- Layer: scene
- Owns: a painted picture world behind the panels, carried on from the picture at the top.
- Default: none

#### None
- Id: none
- Status: draft
- Looks like: no picture behind the sections.
- Made with: nothing.

```css assemble
/* scene: none. No picture behind the sections. */
```

- Careful: none.
- Light and dark: nothing changes.
- Personality: any
- Goes with: any.
- Used on: most mockups.

#### Painted ground
- Id: painted-ground
- Status: draft
- Looks like: the painted world from the picture at the top, carried on behind the panels, like the backdrop of a painted game or a gouache landscape. A sky with two far ridges fading into it at the top; below, a cliff of rock ledges that repeats down the page: lit tops, upright faces with darker facets turned from the light, a cast shadow under each lip, earth slopes between, a few bushes. The panels float on it in heavy frames.
- Made with: big shapes in three or four values first, detail second, as a landscape painter blocks in (see Sources below). The light comes from one side (here the upper left), and every layer is a mask coloured by its own mix of the shared names:
  - the earth is the layer's own colour, `--mark` mixed into `--ground`;
  - the rock faces are a darker mix with `--shadow-rgb`, with upright strokes of varied width that follow the fall of the stone;
  - the shade (facets turned away, the shadow under each lip) is a mix of `--mark` and `--shadow-rgb` laid with `mix-blend-mode: multiply`, and the lit tops and rims a mix of `--mark` and `--surface-raised` laid with `screen`: multiply only darkens and screen only lightens, so shade and light read the right way round on a light page and a dark one;
  - the bushes are `--accent` mixed into a dark `--mark` (at night into a grey from `--ink-soft`), kept dull so they never look pressable;
  - the far ridges are one mask at two strengths over a sky mixed from `--accent`, `--surface-raised` and `--ground`: the farther is paler and closer to the air's colour (atmospheric perspective), and the cliff fades in out of that haze.
  A script draws the masks, one tile of 960 by 600 with four ledges, each ledge line periodic across the tile and drawn again one tile away where it crosses the top or bottom, so it repeats without a seam. One `feTurbulence` and `feDisplacementMap` filter, the same in every mask, roughens all edges like a loaded brush and keeps the masks lined up. The swatch book's masks are about 30 KB together.

The painting is one element the site puts first in `.page`, `<div class="background-scene" aria-hidden="true"><i class="background-face"></i><i class="background-shade"></i><i class="background-lit"></i><i class="background-leaf"></i></div>`: the sky and earth are its fill, the far ridges its `::before`, and the four values its four `<i>`. Words always sit on a sheet or panel, never on the painting.

- Needs markup: `<div class="background-scene" aria-hidden="true"><i class="background-face"></i><i class="background-shade"></i><i class="background-lit"></i><i class="background-leaf"></i></div>` as the first thing inside `.page`.

```css assemble
/* the five masks (alpha only), drawn by tests/parts/source/background.py, which redraws them here */
& { --background-face: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='960' height='600'%3E%3Cfilter id='b' filterUnits='userSpaceOnUse' x='-20' y='-20' width='1000' height='640'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.045' numOctaves='3' seed='3'/%3E%3CfeDisplacementMap in='SourceGraphic' scale='9'/%3E%3C/filter%3E%3Cg filter='url(%23b)' stroke='black' stroke-linecap='round' stroke-linejoin='round'%3E%3Cg id='g0'%3E%3Cpath d='M0 37L48 38L96 31L144 24L192 31L240 37L288 46L336 69L384 83L432 74L480 90L528 73L576 70L624 64L672 87L720 83L768 87L816 79L864 58L912 53L960 37L960 115L912 145L864 153L816 146L768 175L720 152L672 178L624 125L576 137L528 151L480 163L432 154L384 159L336 162L288 111L240 126L192 96L144 97L96 125L48 102L0 115Z' opacity='.9'/%3E%3Cg fill='none'%3E%3Cpath d='M27 48L27 78' stroke-width='8' opacity='.5'/%3E%3Cpath d='M60 45L65 77' stroke-width='6' opacity='.3'/%3E%3Cpath d='M99 41L105 95' stroke-width='3' opacity='.4'/%3E%3Cpath d='M230 54L226 98' stroke-width='8' opacity='.4'/%3E%3Cpath d='M218 44L215 69' stroke-width='8' opacity='.3'/%3E%3Cpath d='M252 51L264 116' stroke-width='4' opacity='.3'/%3E%3Cpath d='M318 69L316 103' stroke-width='9' opacity='.5'/%3E%3Cpath d='M408 93L410 120' stroke-width='8' opacity='.4'/%3E%3Cpath d='M435 93L429 133' stroke-width='6' opacity='.3'/%3E%3Cpath d='M510 97L509 145' stroke-width='11' opacity='.5'/%3E%3Cpath d='M531 80L531 106' stroke-width='5' opacity='.4'/%3E%3Cpath d='M600 83L596 143' stroke-width='8' opacity='.5'/%3E%3Cpath d='M731 100L734 132' stroke-width='6' opacity='.4'/%3E%3Cpath d='M904 73L909 98' stroke-width='8' opacity='.6'/%3E%3Cpath d='M919 64L918 113' stroke-width='7' opacity='.5'/%3E%3C/g%3E%3C/g%3E%3Cuse href='%23g0' y='600'/%3E%3Cpath d='M0 213L48 233L96 246L144 256L192 258L240 249L288 237L336 223L384 228L432 224L480 222L528 221L576 223L624 218L672 204L720 194L768 186L816 190L864 203L912 204L960 213L960 308L912 279L864 271L816 271L768 254L720 282L672 265L624 285L576 308L528 285L480 286L432 307L384 311L336 289L288 317L240 315L192 323L144 317L96 313L48 309L0 308Z' opacity='.9'/%3E%3Cg fill='none'%3E%3Cpath d='M31 238L36 265' stroke-width='5' opacity='.4'/%3E%3Cpath d='M73 247L71 282' stroke-width='10' opacity='.3'/%3E%3Cpath d='M97 263L102 331' stroke-width='5' opacity='.5'/%3E%3Cpath d='M105 263L110 296' stroke-width='6' opacity='.4'/%3E%3Cpath d='M177 274L185 342' stroke-width='10' opacity='.6'/%3E%3Cpath d='M160 268L159 301' stroke-width='6' opacity='.3'/%3E%3Cpath d='M230 269L232 331' stroke-width='11' opacity='.5'/%3E%3Cpath d='M271 253L274 291' stroke-width='4' opacity='.3'/%3E%3Cpath d='M356 236L355 267' stroke-width='6' opacity='.5'/%3E%3Cpath d='M383 237L380 276' stroke-width='9' opacity='.3'/%3E%3Cpath d='M422 241L424 268' stroke-width='3' opacity='.5'/%3E%3Cpath d='M462 231L465 260' stroke-width='10' opacity='.3'/%3E%3Cpath d='M442 235L440 299' stroke-width='9' opacity='.3'/%3E%3Cpath d='M517 230L519 282' stroke-width='10' opacity='.5'/%3E%3Cpath d='M525 229L528 274' stroke-width='3' opacity='.4'/%3E%3Cpath d='M567 241L564 267' stroke-width='9' opacity='.4'/%3E%3Cpath d='M606 226L607 295' stroke-width='7' opacity='.4'/%3E%3Cpath d='M669 213L665 268' stroke-width='7' opacity='.4'/%3E%3Cpath d='M756 203L751 240' stroke-width='8' opacity='.4'/%3E%3Cpath d='M763 194L766 231' stroke-width='9' opacity='.4'/%3E%3Cpath d='M847 214L846 277' stroke-width='6' opacity='.3'/%3E%3Cpath d='M884 222L883 258' stroke-width='9' opacity='.4'/%3E%3C/g%3E%3Cpath d='M0 370L48 377L96 377L144 386L192 381L240 372L288 386L336 383L384 383L432 381L480 386L528 372L576 367L624 377L672 363L720 333L768 327L816 339L864 329L912 356L960 370L960 451L912 447L864 420L816 430L768 408L720 424L672 437L624 450L576 437L528 457L480 456L432 464L384 448L336 445L288 464L240 445L192 449L144 476L96 460L48 454L0 451Z' opacity='.9'/%3E%3Cg fill='none'%3E%3Cpath d='M16 380L19 428' stroke-width='6' opacity='.3'/%3E%3Cpath d='M82 389L84 436' stroke-width='9' opacity='.6'/%3E%3Cpath d='M110 399L116 440' stroke-width='6' opacity='.4'/%3E%3Cpath d='M211 390L208 452' stroke-width='8' opacity='.3'/%3E%3Cpath d='M283 397L280 428' stroke-width='8' opacity='.3'/%3E%3Cpath d='M350 395L349 423' stroke-width='8' opacity='.4'/%3E%3Cpath d='M450 398L457 449' stroke-width='3' opacity='.3'/%3E%3Cpath d='M452 390L455 416' stroke-width='11' opacity='.6'/%3E%3Cpath d='M552 379L550 411' stroke-width='3' opacity='.3'/%3E%3Cpath d='M532 389L541 454' stroke-width='9' opacity='.3'/%3E%3Cpath d='M702 364L707 422' stroke-width='7' opacity='.4'/%3E%3Cpath d='M760 338L758 399' stroke-width='3' opacity='.5'/%3E%3Cpath d='M789 352L786 400' stroke-width='10' opacity='.3'/%3E%3Cpath d='M826 355L828 387' stroke-width='11' opacity='.5'/%3E%3Cpath d='M872 346L871 397' stroke-width='9' opacity='.4'/%3E%3Cpath d='M926 374L921 441' stroke-width='9' opacity='.4'/%3E%3Cpath d='M927 372L926 414' stroke-width='8' opacity='.6'/%3E%3C/g%3E%3Cg id='g3'%3E%3Cpath d='M0 489L48 500L96 497L144 518L192 514L240 536L288 522L336 542L384 523L432 533L480 536L528 554L576 542L624 562L672 560L720 543L768 536L816 530L864 519L912 506L960 489L960 582L912 592L864 610L816 613L768 623L720 615L672 646L624 632L576 607L528 616L480 600L432 617L384 604L336 619L288 605L240 601L192 597L144 611L96 573L48 578L0 582Z' opacity='.9'/%3E%3Cg fill='none'%3E%3Cpath d='M21 507L26 533' stroke-width='5' opacity='.5'/%3E%3Cpath d='M10 508L15 578' stroke-width='4' opacity='.5'/%3E%3Cpath d='M141 534L145 585' stroke-width='8' opacity='.3'/%3E%3Cpath d='M155 534L165 584' stroke-width='8' opacity='.6'/%3E%3Cpath d='M293 542L300 609' stroke-width='7' opacity='.4'/%3E%3Cpath d='M315 549L324 613' stroke-width='7' opacity='.6'/%3E%3Cpath d='M359 553L360 590' stroke-width='10' opacity='.4'/%3E%3Cpath d='M395 542L402 595' stroke-width='5' opacity='.3'/%3E%3Cpath d='M436 549L432 614' stroke-width='9' opacity='.4'/%3E%3Cpath d='M483 548L488 580' stroke-width='4' opacity='.4'/%3E%3Cpath d='M520 563L516 620' stroke-width='9' opacity='.4'/%3E%3Cpath d='M651 570L658 632' stroke-width='7' opacity='.5'/%3E%3Cpath d='M678 567L684 598' stroke-width='5' opacity='.4'/%3E%3Cpath d='M709 561L711 589' stroke-width='9' opacity='.4'/%3E%3Cpath d='M830 542L839 597' stroke-width='6' opacity='.6'/%3E%3Cpath d='M911 514L921 569' stroke-width='9' opacity='.5'/%3E%3Cpath d='M943 516L949 552' stroke-width='8' opacity='.4'/%3E%3Cpath d='M957 501L953 541' stroke-width='9' opacity='.3'/%3E%3C/g%3E%3C/g%3E%3Cuse href='%23g3' y='-600'/%3E%3C/g%3E%3C/svg%3E"); }
& { --background-shade: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='960' height='600'%3E%3Cfilter id='b' filterUnits='userSpaceOnUse' x='-20' y='-20' width='1000' height='640'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.045' numOctaves='3' seed='3'/%3E%3CfeDisplacementMap in='SourceGraphic' scale='9'/%3E%3C/filter%3E%3Cg filter='url(%23b)' stroke='black' stroke-linecap='round' stroke-linejoin='round'%3E%3Cg id='g0'%3E%3Cpath d='M48 38L96 31L96 125L54 102Z' opacity='.6'/%3E%3Cpath d='M96 31L144 24L144 97L102 125Z' opacity='.6'/%3E%3Cpath d='M384 83L432 74L432 154L390 159Z' opacity='.6'/%3E%3Cpath d='M480 90L528 73L528 151L486 163Z' opacity='.6'/%3E%3Cpath d='M576 70L624 64L624 125L582 137Z' opacity='.6'/%3E%3Cpath d='M672 87L720 83L720 152L678 178Z' opacity='.6'/%3E%3Cpath d='M768 87L816 79L816 146L774 175Z' opacity='.7'/%3E%3Cpath d='M816 79L864 58L864 153L822 146Z' opacity='.8'/%3E%3Cpath d='M864 58L912 53L912 145L870 153Z' opacity='.7'/%3E%3Cpath d='M912 53L960 37L960 115L918 145Z' opacity='.7'/%3E%3Cg fill='none'%3E%3Cpath d='M73 50L70 116' stroke-width='4' opacity='.3'/%3E%3Cpath d='M128 45L131 96' stroke-width='7' opacity='.5'/%3E%3Cpath d='M191 47L192 83' stroke-width='11' opacity='.5'/%3E%3Cpath d='M241 49L252 113' stroke-width='8' opacity='.4'/%3E%3Cpath d='M374 86L378 114' stroke-width='9' opacity='.5'/%3E%3Cpath d='M420 86L415 143' stroke-width='11' opacity='.5'/%3E%3Cpath d='M548 89L544 129' stroke-width='5' opacity='.5'/%3E%3Cpath d='M636 88L629 141' stroke-width='10' opacity='.6'/%3E%3Cpath d='M624 74L625 117' stroke-width='4' opacity='.3'/%3E%3Cpath d='M708 97L717 164' stroke-width='9' opacity='.4'/%3E%3Cpath d='M703 100L711 167' stroke-width='6' opacity='.5'/%3E%3Cpath d='M800 96L806 165' stroke-width='5' opacity='.5'/%3E%3Cpath d='M817 91L823 143' stroke-width='9' opacity='.3'/%3E%3Cpath d='M842 75L846 120' stroke-width='10' opacity='.3'/%3E%3Cpath d='M889 62L895 105' stroke-width='7' opacity='.5'/%3E%3Cpath d='M0 44L48 45L96 38L144 31L192 38L240 44L288 53L336 76L384 90L432 81L480 97L528 80L576 77L624 71L672 94L720 90L768 94L816 86L864 65L912 60L960 44' stroke-width='9' opacity='.5'/%3E%3Cpath d='M0 118L48 105L96 128L144 100L192 99L240 129L288 114L336 165L384 162L432 157L480 166L528 154L576 140L624 128L672 181L720 155L768 178L816 149L864 156L912 148L960 118' stroke-width='14' opacity='.3'/%3E%3Cpath d='M161 114L217 128' stroke-width='4' opacity='.3'/%3E%3Cpath d='M259 152L325 172' stroke-width='6' opacity='.2'/%3E%3Cpath d='M347 201L446 232' stroke-width='6' opacity='.2'/%3E%3Cpath d='M610 156L690 178' stroke-width='8' opacity='.2'/%3E%3Cpath d='M707 187L762 195' stroke-width='8' opacity='.3'/%3E%3Cpath d='M828 168L897 180' stroke-width='6' opacity='.2'/%3E%3Cpath d='M898 158L990 179' stroke-width='11' opacity='.3'/%3E%3C/g%3E%3C/g%3E%3Cuse href='%23g0' y='600'/%3E%3Cpath d='M192 258L240 249L240 315L198 323Z' opacity='.6'/%3E%3Cpath d='M240 249L288 237L288 317L246 315Z' opacity='.7'/%3E%3Cpath d='M288 237L336 223L336 289L294 317Z' opacity='.6'/%3E%3Cpath d='M576 223L624 218L624 285L582 308Z' opacity='.7'/%3E%3Cpath d='M624 218L672 204L672 265L630 285Z' opacity='.7'/%3E%3Cpath d='M672 204L720 194L720 282L678 265Z' opacity='.7'/%3E%3Cpath d='M720 194L768 186L768 254L726 282Z' opacity='.7'/%3E%3Cg fill='none'%3E%3Cpath d='M38 246L37 284' stroke-width='4' opacity='.4'/%3E%3Cpath d='M78 255L80 315' stroke-width='3' opacity='.3'/%3E%3Cpath d='M296 242L300 270' stroke-width='6' opacity='.5'/%3E%3Cpath d='M394 235L386 296' stroke-width='4' opacity='.3'/%3E%3Cpath d='M662 220L655 270' stroke-width='8' opacity='.4'/%3E%3Cpath d='M698 206L701 240' stroke-width='5' opacity='.4'/%3E%3Cpath d='M712 211L718 271' stroke-width='8' opacity='.5'/%3E%3Cpath d='M809 203L823 272' stroke-width='4' opacity='.5'/%3E%3Cpath d='M878 219L871 274' stroke-width='5' opacity='.4'/%3E%3Cpath d='M958 222L963 262' stroke-width='9' opacity='.5'/%3E%3Cpath d='M0 220L48 240L96 253L144 263L192 265L240 256L288 244L336 230L384 235L432 231L480 229L528 228L576 230L624 225L672 211L720 201L768 193L816 197L864 210L912 211L960 220' stroke-width='9' opacity='.5'/%3E%3Cpath d='M0 311L48 312L96 316L144 320L192 326L240 318L288 320L336 292L384 314L432 310L480 289L528 288L576 311L624 288L672 268L720 285L768 257L816 274L864 274L912 282L960 311' stroke-width='14' opacity='.3'/%3E%3Cpath d='M48 330L93 345' stroke-width='7' opacity='.3'/%3E%3Cpath d='M444 340L498 364' stroke-width='8' opacity='.2'/%3E%3Cpath d='M535 323L634 360' stroke-width='8' opacity='.3'/%3E%3Cpath d='M613 304L704 332' stroke-width='5' opacity='.3'/%3E%3Cpath d='M725 309L829 339' stroke-width='8' opacity='.3'/%3E%3Cpath d='M901 299L952 317' stroke-width='5' opacity='.2'/%3E%3C/g%3E%3Cpath d='M144 386L192 381L192 449L150 476Z' opacity='.7'/%3E%3Cpath d='M192 381L240 372L240 445L198 449Z' opacity='.7'/%3E%3Cpath d='M480 386L528 372L528 457L486 456Z' opacity='.6'/%3E%3Cpath d='M528 372L576 367L576 437L534 457Z' opacity='.6'/%3E%3Cpath d='M624 377L672 363L672 437L630 450Z' opacity='.7'/%3E%3Cpath d='M672 363L720 333L720 424L678 437Z' opacity='.7'/%3E%3Cpath d='M720 333L768 327L768 408L726 424Z' opacity='.7'/%3E%3Cpath d='M816 339L864 329L864 420L822 430Z' opacity='.7'/%3E%3Cg fill='none'%3E%3Cpath d='M71 393L74 433' stroke-width='9' opacity='.3'/%3E%3Cpath d='M137 392L139 432' stroke-width='4' opacity='.4'/%3E%3Cpath d='M169 400L169 456' stroke-width='9' opacity='.3'/%3E%3Cpath d='M243 387L254 439' stroke-width='4' opacity='.3'/%3E%3Cpath d='M315 400L315 460' stroke-width='5' opacity='.5'/%3E%3Cpath d='M405 402L408 467' stroke-width='8' opacity='.3'/%3E%3Cpath d='M519 386L523 415' stroke-width='6' opacity='.5'/%3E%3Cpath d='M599 378L602 423' stroke-width='9' opacity='.4'/%3E%3Cpath d='M662 376L669 418' stroke-width='7' opacity='.5'/%3E%3Cpath d='M665 383L663 444' stroke-width='7' opacity='.3'/%3E%3Cpath d='M702 354L709 408' stroke-width='4' opacity='.5'/%3E%3Cpath d='M843 351L841 377' stroke-width='7' opacity='.4'/%3E%3Cpath d='M870 339L864 392' stroke-width='7' opacity='.3'/%3E%3Cpath d='M0 377L48 384L96 384L144 393L192 388L240 379L288 393L336 390L384 390L432 388L480 393L528 379L576 374L624 384L672 370L720 340L768 334L816 346L864 336L912 363L960 377' stroke-width='9' opacity='.5'/%3E%3Cpath d='M0 454L48 457L96 463L144 479L192 452L240 448L288 467L336 448L384 451L432 467L480 459L528 460L576 440L624 453L672 440L720 427L768 411L816 433L864 423L912 450L960 454' stroke-width='14' opacity='.3'/%3E%3Cpath d='M130 513L174 532' stroke-width='8' opacity='.2'/%3E%3Cpath d='M415 492L481 516' stroke-width='8' opacity='.2'/%3E%3Cpath d='M736 440L812 470' stroke-width='8' opacity='.2'/%3E%3Cpath d='M817 457L862 469' stroke-width='8' opacity='.3'/%3E%3C/g%3E%3Cg id='g3'%3E%3Cpath d='M240 536L288 522L288 605L246 601Z' opacity='.7'/%3E%3Cpath d='M336 542L384 523L384 604L342 619Z' opacity='.7'/%3E%3Cpath d='M528 554L576 542L576 607L534 616Z' opacity='.6'/%3E%3Cpath d='M672 560L720 543L720 615L678 646Z' opacity='.6'/%3E%3Cpath d='M720 543L768 536L768 623L726 615Z' opacity='.6'/%3E%3Cpath d='M768 536L816 530L816 613L774 623Z' opacity='.7'/%3E%3Cpath d='M816 530L864 519L864 610L822 613Z' opacity='.7'/%3E%3Cpath d='M864 519L912 506L912 592L870 610Z' opacity='.7'/%3E%3Cpath d='M912 506L960 489L960 582L918 592Z' opacity='.6'/%3E%3Cg fill='none'%3E%3Cpath d='M86 510L84 540' stroke-width='6' opacity='.4'/%3E%3Cpath d='M131 526L127 562' stroke-width='9' opacity='.5'/%3E%3Cpath d='M223 540L216 604' stroke-width='6' opacity='.5'/%3E%3Cpath d='M276 541L280 578' stroke-width='8' opacity='.6'/%3E%3Cpath d='M529 563L532 604' stroke-width='10' opacity='.5'/%3E%3Cpath d='M621 571L620 640' stroke-width='7' opacity='.4'/%3E%3Cpath d='M672 580L679 626' stroke-width='6' opacity='.4'/%3E%3Cpath d='M731 558L729 586' stroke-width='6' opacity='.5'/%3E%3Cpath d='M740 548L741 600' stroke-width='7' opacity='.5'/%3E%3Cpath d='M812 543L819 591' stroke-width='5' opacity='.5'/%3E%3Cpath d='M875 531L881 566' stroke-width='6' opacity='.3'/%3E%3Cpath d='M0 496L48 507L96 504L144 525L192 521L240 543L288 529L336 549L384 530L432 540L480 543L528 561L576 549L624 569L672 567L720 550L768 543L816 537L864 526L912 513L960 496' stroke-width='9' opacity='.5'/%3E%3Cpath d='M0 585L48 581L96 576L144 614L192 600L240 604L288 608L336 622L384 607L432 620L480 603L528 619L576 610L624 635L672 649L720 618L768 626L816 616L864 613L912 595L960 585' stroke-width='14' opacity='.3'/%3E%3Cpath d='M56 617L161 645' stroke-width='10' opacity='.2'/%3E%3Cpath d='M222 620L309 638' stroke-width='11' opacity='.2'/%3E%3Cpath d='M331 657L390 666' stroke-width='9' opacity='.3'/%3E%3Cpath d='M418 645L483 665' stroke-width='9' opacity='.2'/%3E%3Cpath d='M716 630L818 662' stroke-width='8' opacity='.2'/%3E%3Cpath d='M797 645L889 683' stroke-width='10' opacity='.2'/%3E%3Cpath d='M901 632L1001 662' stroke-width='8' opacity='.2'/%3E%3C/g%3E%3C/g%3E%3Cuse href='%23g3' y='-600'/%3E%3C/g%3E%3C/svg%3E"); }
& { --background-lit: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='960' height='600'%3E%3Cfilter id='b' filterUnits='userSpaceOnUse' x='-20' y='-20' width='1000' height='640'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.045' numOctaves='3' seed='3'/%3E%3CfeDisplacementMap in='SourceGraphic' scale='9'/%3E%3C/filter%3E%3Cg filter='url(%23b)' stroke='black' stroke-linecap='round' stroke-linejoin='round'%3E%3Cg id='g0'%3E%3Cpath d='M0 18L48 22L96 13L144 13L192 15L240 17L288 35L336 48L384 62L432 60L480 77L528 59L576 56L624 42L672 73L720 74L768 77L816 60L864 36L912 38L960 18L960 37L912 53L864 58L816 79L768 87L720 83L672 87L624 64L576 70L528 73L480 90L432 74L384 83L336 69L288 46L240 37L192 31L144 24L96 31L48 38L0 37Z' opacity='.8'/%3E%3Ccircle cx='698' cy='66' r='4' opacity='.8'/%3E%3Ccircle cx='697' cy='57' r='4' opacity='.8'/%3E%3Ccircle cx='708' cy='57' r='5' opacity='.8'/%3E%3Ccircle cx='311' cy='31' r='5' opacity='.8'/%3E%3Ccircle cx='305' cy='28' r='6' opacity='.8'/%3E%3Ccircle cx='307' cy='31' r='5' opacity='.8'/%3E%3Cg fill='none'%3E%3Cpath d='M0 38L48 39' stroke-width='3' opacity='.9'/%3E%3Cpath d='M144 25L192 32' stroke-width='4' opacity='.9'/%3E%3Cpath d='M192 32L240 38' stroke-width='2' opacity='.8'/%3E%3Cpath d='M240 38L288 47' stroke-width='3' opacity='.9'/%3E%3Cpath d='M288 47L336 70' stroke-width='3' opacity='.8'/%3E%3Cpath d='M336 70L384 84' stroke-width='3' opacity='.9'/%3E%3Cpath d='M432 75L480 91' stroke-width='3' opacity='.9'/%3E%3Cpath d='M528 74L576 71' stroke-width='3' opacity='.9'/%3E%3Cpath d='M624 65L672 88' stroke-width='4' opacity='.9'/%3E%3Cpath d='M720 84L768 88' stroke-width='2' opacity='.9'/%3E%3Cpath d='M-7 31L19 26' stroke-width='6' opacity='.7'/%3E%3Cpath d='M147 17L168 16' stroke-width='6' opacity='.5'/%3E%3Cpath d='M281 37L307 36' stroke-width='6' opacity='.4'/%3E%3Cpath d='M427 67L451 64' stroke-width='4' opacity='.8'/%3E%3Cpath d='M574 63L598 65' stroke-width='5' opacity='.6'/%3E%3Cpath d='M723 74L741 73' stroke-width='4' opacity='.7'/%3E%3Cpath d='M863 53L889 55' stroke-width='3' opacity='.7'/%3E%3Cpath d='M52 118L112 134' stroke-width='6' opacity='.3'/%3E%3Cpath d='M447 182L547 226' stroke-width='11' opacity='.3'/%3E%3Cpath d='M538 184L591 197' stroke-width='8' opacity='.3'/%3E%3C/g%3E%3C/g%3E%3Cuse href='%23g0' y='600'/%3E%3Cpath d='M0 192L48 215L96 226L144 242L192 236L240 230L288 219L336 202L384 213L432 208L480 212L528 206L576 204L624 202L672 195L720 177L768 167L816 178L864 187L912 191L960 192L960 213L912 204L864 203L816 190L768 186L720 194L672 204L624 218L576 223L528 221L480 222L432 224L384 228L336 223L288 237L240 249L192 258L144 256L96 246L48 233L0 213Z' opacity='.8'/%3E%3Ccircle cx='607' cy='182' r='6' opacity='.8'/%3E%3Ccircle cx='621' cy='193' r='4' opacity='.8'/%3E%3Ccircle cx='614' cy='191' r='5' opacity='.8'/%3E%3Ccircle cx='595' cy='191' r='3' opacity='.8'/%3E%3Ccircle cx='610' cy='187' r='5' opacity='.8'/%3E%3Ccircle cx='320' cy='195' r='4' opacity='.8'/%3E%3Ccircle cx='306' cy='182' r='6' opacity='.8'/%3E%3Ccircle cx='314' cy='189' r='4' opacity='.8'/%3E%3Cg fill='none'%3E%3Cpath d='M0 214L48 234' stroke-width='3' opacity='.8'/%3E%3Cpath d='M48 234L96 247' stroke-width='2' opacity='.8'/%3E%3Cpath d='M96 247L144 257' stroke-width='2' opacity='.7'/%3E%3Cpath d='M144 257L192 259' stroke-width='4' opacity='.9'/%3E%3Cpath d='M336 224L384 229' stroke-width='3' opacity='1.0'/%3E%3Cpath d='M384 229L432 225' stroke-width='3' opacity='1.0'/%3E%3Cpath d='M432 225L480 223' stroke-width='2' opacity='.7'/%3E%3Cpath d='M480 223L528 222' stroke-width='3' opacity='.8'/%3E%3Cpath d='M528 222L576 224' stroke-width='4' opacity='.9'/%3E%3Cpath d='M768 187L816 191' stroke-width='2' opacity='.8'/%3E%3Cpath d='M816 191L864 204' stroke-width='3' opacity='.9'/%3E%3Cpath d='M864 204L912 205' stroke-width='2' opacity='.9'/%3E%3Cpath d='M912 205L960 214' stroke-width='3' opacity='.8'/%3E%3Cpath d='M-7 204L31 198' stroke-width='6' opacity='.8'/%3E%3Cpath d='M151 248L193 242' stroke-width='5' opacity='.6'/%3E%3Cpath d='M294 229L313 226' stroke-width='4' opacity='.6'/%3E%3Cpath d='M435 216L464 214' stroke-width='7' opacity='.7'/%3E%3Cpath d='M570 214L593 213' stroke-width='3' opacity='.4'/%3E%3Cpath d='M718 185L751 184' stroke-width='6' opacity='.4'/%3E%3Cpath d='M869 195L908 195' stroke-width='7' opacity='.5'/%3E%3Cpath d='M159 351L227 362' stroke-width='9' opacity='.3'/%3E%3Cpath d='M231 340L288 355' stroke-width='10' opacity='.3'/%3E%3Cpath d='M347 311L406 336' stroke-width='12' opacity='.2'/%3E%3Cpath d='M802 305L864 332' stroke-width='12' opacity='.2'/%3E%3C/g%3E%3Cpath d='M0 351L48 365L96 365L144 370L192 361L240 360L288 369L336 370L384 367L432 362L480 377L528 363L576 352L624 361L672 349L720 313L768 316L816 317L864 314L912 338L960 351L960 370L912 356L864 329L816 339L768 327L720 333L672 363L624 377L576 367L528 372L480 386L432 381L384 383L336 383L288 386L240 372L192 381L144 386L96 377L48 377L0 370Z' opacity='.8'/%3E%3Ccircle cx='602' cy='341' r='5' opacity='.8'/%3E%3Ccircle cx='615' cy='349' r='6' opacity='.8'/%3E%3Ccircle cx='619' cy='341' r='3' opacity='.8'/%3E%3Ccircle cx='43' cy='347' r='5' opacity='.8'/%3E%3Ccircle cx='39' cy='352' r='4' opacity='.8'/%3E%3Ccircle cx='23' cy='352' r='5' opacity='.8'/%3E%3Ccircle cx='28' cy='348' r='3' opacity='.8'/%3E%3Cg fill='none'%3E%3Cpath d='M0 371L48 378' stroke-width='3' opacity='1.0'/%3E%3Cpath d='M48 378L96 378' stroke-width='4' opacity='.8'/%3E%3Cpath d='M96 378L144 387' stroke-width='4' opacity='.9'/%3E%3Cpath d='M240 373L288 387' stroke-width='2' opacity='.9'/%3E%3Cpath d='M288 387L336 384' stroke-width='4' opacity='1.0'/%3E%3Cpath d='M336 384L384 384' stroke-width='4' opacity='.9'/%3E%3Cpath d='M384 384L432 382' stroke-width='3' opacity='1.0'/%3E%3Cpath d='M432 382L480 387' stroke-width='3' opacity='.9'/%3E%3Cpath d='M576 368L624 378' stroke-width='3' opacity='1.0'/%3E%3Cpath d='M768 328L816 340' stroke-width='4' opacity='.8'/%3E%3Cpath d='M864 330L912 357' stroke-width='4' opacity='.8'/%3E%3Cpath d='M912 357L960 371' stroke-width='4' opacity='.8'/%3E%3Cpath d='M-2 362L32 369' stroke-width='4' opacity='.5'/%3E%3Cpath d='M152 377L189 371' stroke-width='5' opacity='.5'/%3E%3Cpath d='M278 375L298 377' stroke-width='5' opacity='.7'/%3E%3Cpath d='M441 369L470 373' stroke-width='5' opacity='.7'/%3E%3Cpath d='M582 361L627 355' stroke-width='3' opacity='.8'/%3E%3Cpath d='M727 323L759 326' stroke-width='4' opacity='.4'/%3E%3Cpath d='M855 322L884 327' stroke-width='3' opacity='.5'/%3E%3Cpath d='M60 489L109 502' stroke-width='5' opacity='.3'/%3E%3Cpath d='M222 469L276 493' stroke-width='5' opacity='.2'/%3E%3Cpath d='M353 478L446 512' stroke-width='6' opacity='.2'/%3E%3Cpath d='M535 487L615 506' stroke-width='9' opacity='.3'/%3E%3Cpath d='M637 469L707 491' stroke-width='9' opacity='.2'/%3E%3Cpath d='M912 470L1007 488' stroke-width='9' opacity='.2'/%3E%3C/g%3E%3Cg id='g3'%3E%3Cpath d='M0 476L48 490L96 478L144 507L192 494L240 523L288 503L336 521L384 502L432 520L480 520L528 533L576 525L624 542L672 551L720 526L768 527L816 512L864 509L912 490L960 476L960 489L912 506L864 519L816 530L768 536L720 543L672 560L624 562L576 542L528 554L480 536L432 533L384 523L336 542L288 522L240 536L192 514L144 518L96 497L48 500L0 489Z' opacity='.8'/%3E%3Ccircle cx='650' cy='539' r='6' opacity='.8'/%3E%3Ccircle cx='641' cy='532' r='5' opacity='.8'/%3E%3Ccircle cx='653' cy='535' r='6' opacity='.8'/%3E%3Ccircle cx='661' cy='537' r='6' opacity='.8'/%3E%3Ccircle cx='636' cy='536' r='5' opacity='.8'/%3E%3Ccircle cx='462' cy='504' r='4' opacity='.8'/%3E%3Ccircle cx='465' cy='508' r='5' opacity='.8'/%3E%3Ccircle cx='463' cy='505' r='5' opacity='.8'/%3E%3Cg fill='none'%3E%3Cpath d='M0 490L48 501' stroke-width='3' opacity='1.0'/%3E%3Cpath d='M48 501L96 498' stroke-width='3' opacity='.8'/%3E%3Cpath d='M96 498L144 519' stroke-width='4' opacity='.8'/%3E%3Cpath d='M144 519L192 515' stroke-width='2' opacity='.9'/%3E%3Cpath d='M192 515L240 537' stroke-width='4' opacity='.8'/%3E%3Cpath d='M288 523L336 543' stroke-width='4' opacity='.7'/%3E%3Cpath d='M384 524L432 534' stroke-width='3' opacity='.9'/%3E%3Cpath d='M432 534L480 537' stroke-width='3' opacity='.9'/%3E%3Cpath d='M480 537L528 555' stroke-width='3' opacity='.8'/%3E%3Cpath d='M576 543L624 563' stroke-width='3' opacity='.9'/%3E%3Cpath d='M624 563L672 561' stroke-width='4' opacity='.7'/%3E%3Cpath d='M-5 484L27 484' stroke-width='4' opacity='.7'/%3E%3Cpath d='M151 506L170 507' stroke-width='6' opacity='.5'/%3E%3Cpath d='M295 512L320 517' stroke-width='3' opacity='.5'/%3E%3Cpath d='M426 527L469 520' stroke-width='7' opacity='.6'/%3E%3Cpath d='M573 536L612 529' stroke-width='4' opacity='.7'/%3E%3Cpath d='M728 535L773 542' stroke-width='6' opacity='.5'/%3E%3Cpath d='M870 511L909 504' stroke-width='7' opacity='.6'/%3E%3Cpath d='M125 638L199 670' stroke-width='9' opacity='.3'/%3E%3Cpath d='M509 640L618 656' stroke-width='7' opacity='.3'/%3E%3Cpath d='M627 671L707 702' stroke-width='5' opacity='.2'/%3E%3C/g%3E%3C/g%3E%3Cuse href='%23g3' y='-600'/%3E%3C/g%3E%3C/svg%3E"); }
& { --background-leaf: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='960' height='600'%3E%3Cfilter id='b' filterUnits='userSpaceOnUse' x='-20' y='-20' width='1000' height='640'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.045' numOctaves='3' seed='3'/%3E%3CfeDisplacementMap in='SourceGraphic' scale='9'/%3E%3C/filter%3E%3Cg filter='url(%23b)' stroke='black' stroke-linecap='round' stroke-linejoin='round'%3E%3Cg id='g0'%3E%3Ccircle cx='729' cy='73' r='11'/%3E%3Ccircle cx='700' cy='68' r='8'/%3E%3Ccircle cx='723' cy='67' r='10'/%3E%3Ccircle cx='697' cy='70' r='6'/%3E%3Ccircle cx='729' cy='62' r='8'/%3E%3Ccircle cx='700' cy='59' r='9'/%3E%3Ccircle cx='711' cy='60' r='10'/%3E%3Ccircle cx='706' cy='72' r='10'/%3E%3Ccircle cx='744' cy='72' r='9'/%3E%3Ccircle cx='314' cy='34' r='9'/%3E%3Ccircle cx='308' cy='32' r='12'/%3E%3Ccircle cx='337' cy='47' r='11'/%3E%3Ccircle cx='323' cy='43' r='11'/%3E%3Ccircle cx='310' cy='34' r='10'/%3E%3Ccircle cx='337' cy='30' r='7'/%3E%3Ccircle cx='348' cy='39' r='9'/%3E%3Cg fill='none'%3E%3C/g%3E%3C/g%3E%3Cuse href='%23g0' y='600'/%3E%3Ccircle cx='612' cy='201' r='9'/%3E%3Ccircle cx='611' cy='186' r='11'/%3E%3Ccircle cx='635' cy='188' r='7'/%3E%3Ccircle cx='623' cy='196' r='8'/%3E%3Ccircle cx='617' cy='194' r='10'/%3E%3Ccircle cx='597' cy='193' r='7'/%3E%3Ccircle cx='651' cy='193' r='9'/%3E%3Ccircle cx='613' cy='190' r='10'/%3E%3Ccircle cx='647' cy='192' r='7'/%3E%3Ccircle cx='322' cy='197' r='7'/%3E%3Ccircle cx='309' cy='186' r='11'/%3E%3Ccircle cx='340' cy='188' r='9'/%3E%3Ccircle cx='316' cy='192' r='7'/%3E%3Ccircle cx='308' cy='201' r='9'/%3E%3Ccircle cx='344' cy='201' r='9'/%3E%3Cg fill='none'%3E%3C/g%3E%3Ccircle cx='604' cy='343' r='9'/%3E%3Ccircle cx='631' cy='346' r='12'/%3E%3Ccircle cx='619' cy='353' r='11'/%3E%3Ccircle cx='609' cy='356' r='12'/%3E%3Ccircle cx='648' cy='346' r='9'/%3E%3Ccircle cx='614' cy='359' r='12'/%3E%3Ccircle cx='596' cy='358' r='7'/%3E%3Ccircle cx='621' cy='343' r='7'/%3E%3Ccircle cx='609' cy='356' r='11'/%3E%3Ccircle cx='46' cy='350' r='10'/%3E%3Ccircle cx='51' cy='361' r='6'/%3E%3Ccircle cx='42' cy='354' r='8'/%3E%3Ccircle cx='26' cy='355' r='10'/%3E%3Ccircle cx='30' cy='350' r='7'/%3E%3Ccircle cx='60' cy='358' r='6'/%3E%3Ccircle cx='58' cy='350' r='6'/%3E%3Cg fill='none'%3E%3C/g%3E%3Cg id='g3'%3E%3Ccircle cx='654' cy='543' r='13'/%3E%3Ccircle cx='644' cy='535' r='11'/%3E%3Ccircle cx='657' cy='539' r='13'/%3E%3Ccircle cx='665' cy='541' r='12'/%3E%3Ccircle cx='639' cy='539' r='11'/%3E%3Ccircle cx='648' cy='546' r='9'/%3E%3Ccircle cx='703' cy='536' r='13'/%3E%3Ccircle cx='674' cy='547' r='11'/%3E%3Ccircle cx='677' cy='547' r='10'/%3E%3Ccircle cx='464' cy='507' r='9'/%3E%3Ccircle cx='468' cy='511' r='11'/%3E%3Ccircle cx='484' cy='512' r='11'/%3E%3Ccircle cx='466' cy='508' r='11'/%3E%3Ccircle cx='505' cy='507' r='10'/%3E%3Ccircle cx='481' cy='511' r='9'/%3E%3Cg fill='none'%3E%3C/g%3E%3C/g%3E%3Cuse href='%23g3' y='-600'/%3E%3C/g%3E%3C/svg%3E"); }
& { --background-ridge: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1200' height='120'%3E%3Cfilter id='b' x='-5%25' y='-20%25' width='110%25' height='140%25'%3E %3CfeTurbulence type='fractalNoise' baseFrequency='0.04' numOctaves='3' seed='3'/%3E%3CfeDisplacementMap in='SourceGraphic' scale='7'/%3E%3C/filter%3E %3Cg filter='url(%23b)'%3E%3Cpath d='M0 120L0 10L30 14L60 22L90 28L120 29L150 29L180 34L210 42L240 46L270 41L300 30L330 22L360 22L390 29L420 37L450 42L480 45L510 53L540 68L570 83L600 90L630 86L660 78L690 72L720 71L750 71L780 66L810 58L840 54L870 59L900 70L930 78L960 78L990 71L1020 63L1050 58L1080 55L1110 47L1140 32L1170 17L1200 10L1200 120Z' opacity='0.45'/%3E%3Cpath d='M0 120L0 65L30 73L60 81L90 85L120 89L150 95L180 103L210 111L240 111L270 105L300 97L330 94L360 94L390 96L420 94L450 91L480 91L510 96L540 103L570 107L600 103L630 95L660 87L690 83L720 79L750 73L780 65L810 57L840 57L870 63L900 71L930 74L960 74L990 72L1020 74L1050 77L1080 77L1110 72L1140 65L1170 61L1200 65L1200 120Z' opacity='0.8'/%3E%3C/g%3E%3C/svg%3E"); }
/* light-dark(day, night): the night colours follow the colour-scheme the colour part's tone sets */
.background-scene { display: block; position: absolute; inset: 0; z-index: -4; pointer-events: none; --background-sky-h: 5.5rem;
  --background-earth: light-dark(color-mix(in oklab, var(--mark) 40%, var(--ground)), color-mix(in oklab, var(--ink-soft) 22%, color-mix(in oklab, var(--mark) 20%, var(--ground))));
  background: linear-gradient(light-dark(color-mix(in oklab, var(--accent) 14%, var(--ground)), color-mix(in oklab, var(--ink-soft) 16%, var(--ground))),
    light-dark(color-mix(in oklab, var(--surface-raised) 55%, var(--ground)), color-mix(in oklab, var(--ink-soft) 38%, var(--ground)))) 0 0 / 100% var(--background-sky-h) no-repeat, var(--background-earth); }
.background-scene::before { content: ""; position: absolute; inset: 0 0 auto; height: calc(var(--background-sky-h) + 1.5rem);   /* far ridges, two strengths */
  background: light-dark(color-mix(in oklab, var(--mark) 45%, var(--ground)), color-mix(in oklab, var(--mark) 12%, var(--ground)));
  mask: var(--background-ridge) -200px 100% / 1200px 100% repeat-x; }
.background-scene > i { position: absolute; inset: var(--background-sky-h) 0 0; mask-size: 960px 600px, 100% 100%; mask-position: -120px -36px, 0 0;
  mask-repeat: repeat, no-repeat; mask-composite: intersect; --background-fade: linear-gradient(transparent, black 3.5rem); }   /* the cliff comes out of the haze */
.background-face  { background: color-mix(in oklab, var(--mark) 62%, rgb(var(--shadow-rgb))); opacity: 0.55; mask-image: var(--background-face), var(--background-fade); }
.background-shade { background: light-dark(color-mix(in oklab, var(--mark) 45%, rgb(var(--shadow-rgb))), color-mix(in oklab, var(--mark) 22%, rgb(var(--shadow-rgb)))); mix-blend-mode: multiply; opacity: 0.85; mask-image: var(--background-shade), var(--background-fade); }
.background-lit   { background: light-dark(color-mix(in oklab, var(--mark) 40%, var(--surface-raised)), color-mix(in oklab, var(--ink) 72%, var(--surface-raised))); mix-blend-mode: screen; opacity: 0.9; mask-image: var(--background-lit), var(--background-fade); }
.background-leaf  { background: light-dark(color-mix(in oklab, var(--accent) 35%, color-mix(in oklab, var(--mark) 50%, rgb(var(--shadow-rgb)))), color-mix(in oklab, var(--accent) 22%, color-mix(in oklab, var(--ink-soft) 48%, var(--ground)))); opacity: 0.9; mask-image: var(--background-leaf), var(--background-fade); }
```

- Careful:
  - No words on the painting; the panels are opaque.
  - What makes it read as painted and not as smears: a few big shapes in a few values; strokes with a direction that follows the form (upright down a face, along a ledge, slanting down a slope) and of different widths; one light side, kept the same in every layer; detail (rims, bushes) in small amounts. The first version, a few hundred near-flat strokes at random strengths, read as "flat horizontal smears".
  - The sky sits only at the top of the page; further down, the cliff repeats. Keep the tile large (900 pixels or more) or the same ledge shows in a column.
  - On the mockup it was made for, the guide it followed asked for "the same world, not a texture", and the repeating tile was recorded as still a texture: it is the fallback when one long scene is too much work. A second look (night, say) needs no new tile: the shared names change and the painting follows.
- Light and dark: on a light page it is sandstone in sun under a pale sky: near-white lit tops, warm brown shade, olive bushes. On a dark page it is the same cliff by moonlight, and here the same mixes are not enough: night needs a different light, not a dimmer day. So the sky, ridges, earth, lit tops, shade and bushes each pick their night colour with `light-dark()`, which follows the `color-scheme` the colour part's tone sets, still from shared names only. Moonlight is cool and pale (the lit tops are mostly `--ink` through `screen`), so there is a clear gap between lit tops and shaded faces; the earth is a cool grey from `--ink-soft`; the sky is lighter than the ridges, so they read as a silhouette; and the bushes are a dark grey-green, never the gold of a dark page's mark or accent. `light-dark()`, `mask-composite` and `mix-blend-mode` need a browser from 2024 or later.
- Personality: playful, dramatic
- Goes with: `frames: riveted-metal`; `materials: metal-and-dark-glass`; `light: daylight` or `light: moonlight`; `density: busy`.
- Used on: 2 mockups: two game-style joke sites (the earlier one also scattered hand-drawn signs over the strokes, which made it a detailed ground).
- Sources: value grouping and value compression with distance, https://willkempartschool.com/how-to-create-depth-in-landscape-painting-understanding-value-compression/; painting light and form shadow, https://proko.com/course-lesson/understanding-light-and-shadow-for-painting; `feTurbulence` and `feDisplacementMap` for rough edges, https://tympanus.net/codrops/?p=37751 and https://henry.codes/writing/how-to-distort-text-with-svg/.

#### One long scene
- Id: one-long-scene
- Status: draft
- Looks like: there is no separate ground. The picture at the top goes on down the page, band by band: a road to a castle, then a meadow and a stream, then a trader's stall, then a camp, then a cave. Each band ends in a wavy edge in the next band's ground, so the world joins up as the visitor scrolls. Panels sit on each band.
- Made with: every section is a band (positioned, but neither isolated nor clipped: the page's `overflow-x: clip` holds the sides, and the edge between bands must poke out). Inside it, first, an inline SVG painting stretched to the band with `preserveAspectRatio="xMidYMin slice"` (the top band uses `xMidYMax` so its ground stays at the foot), then the content. The band's own fill is the colour at the top of its painting (set on each band by the page), and the wavy join between two bands is the frames part's (`section-edge: wavy`), cut in that fill and laid over the foot of the band above; this part no longer draws an edge of its own. Each shape in the painting has a class whose fill is a shared name or a mix of two; a shared displacement filter roughens them. Wider than a phone, put the panel to one side and the painting's subject (a figure, a stall) in the other half, where it shows.

- Needs markup: in each `.band`, first, `<svg class="background-paint" viewBox="0 0 1600 1100" preserveAspectRatio="xMidYMin slice" aria-hidden="true" focusable="false">` with the band's painting, its shapes given the classes below; and on the band `style="background-color: ...; --background-next-ground: ..."` (the colour at the top of its own painting, written as a mix of shared names, and the ground of the band after it). Pick `frames: section-edge wavy` for the joins.

Each band's painting is the site's own inline SVG, its shapes given the classes below; the band's own `background-color` is the colour at the top of its painting, which the frames part's wavy edge is cut in, and `--background-next-ground` the ground of the band after it (the sky, the meadow), so its meadow leads into the next.

```css assemble
.band { position: relative; padding-block: var(--gap-groups, 2rem) var(--gap-sections, 4rem); }   /* no clip: frames' edge pokes above each band; each band's fill is set on it (Needs markup) */
.band > .background-paint { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 0; max-width: none; pointer-events: none; }
.band { --background-next-ground: color-mix(in oklab, var(--accent) 22%, var(--ground)); }   /* each band sets its own */
.background-paint .background-sky    { fill: color-mix(in oklab, var(--accent) 10%, var(--ground)); }
.background-paint .background-far    { fill: color-mix(in oklab, var(--mark) 25%, var(--ground)); }
.background-paint .background-castle { fill: color-mix(in oklab, var(--mark) 35%, var(--ground)); }
.background-paint .background-near   { fill: color-mix(in oklab, var(--mark) 50%, var(--ground)); }
.background-paint .background-road   { fill: color-mix(in oklab, var(--mark) 20%, var(--surface)); }
.background-paint .background-meadow { fill: var(--background-next-ground); }
.background-paint .background-water  { fill: color-mix(in oklab, var(--accent) 55%, var(--surface-raised)); stroke: color-mix(in oklab, var(--accent) 20%, var(--surface-raised)); stroke-width: 4; }
.background-paint .background-tuft   { fill: none; stroke: color-mix(in oklab, var(--accent) 60%, var(--ink)); stroke-width: 4; stroke-linecap: round; }
```

```html
<section class="band" style="background-color: color-mix(in oklab, var(--accent) 10%, var(--ground)); --background-next-ground: ...">
  <svg class="background-paint" viewBox="0 0 1600 1100" preserveAspectRatio="xMidYMin slice" aria-hidden="true" focusable="false">
    <g filter="url(#background-pen)"><rect class="background-sky" width="1600" height="700"/>...</g></svg>
  <div class="panel">...</div>
</section>
```

- Careful: water and anything else that must be seen in a band needs more than a tint: a stream at 30% of the accent over a meadow at 22% vanished on the light page; at 55%, with a pale bank, it shows on both. Daylight scenes are bright, and pale words on a sky fail; every word goes on a panel (see `light: daylight`). With `slice`, the sides of the painting are cut on a phone: keep the important things near the middle of each band, or move them to a strip in the flow on a phone. The painting is decoration and is hidden from screen readers; if a figure in it matters, say so in words. Any movement in the world stops under reduced motion. It is a lot of drawing: one band per section, each different. Fills written as presentation attributes (`fill="var(--x)"`) are not reliable; use classes.
- Light and dark: the same painting. On a light page it is a pale, sunny country in sand and sage; on a dark page the same hills at dusk, low in contrast, the castle a silhouette. The mockup's own day and night were two sets of paintings; drawn from the shared names, one set serves both.
- Personality: playful, dramatic
- Goes with: `frames: riveted-metal`; `light: daylight` or `light: sky-by-the-clock`; `density: busy`.
- Used on: 1 mockup: a game-style joke site, in both of its looks (day and night). It answered the earlier site's open question of how a long page continues one painting downwards.

## Starting points

### Plain
- Id: plain
- Picks: texture: none; pattern: none; drawings: none; finds: off; scene: none
- Personality: serious, calm
- Looks like: one flat colour behind everything; sections separated by space. Gives the stage to a designed signature piece.
- Used on: 4 mockups: a tutoring site, a browser game's pages for deciding, a poetry site in its default look, and the first version of a volunteer page.

### Coloured bands
- Id: coloured-bands
- Picks: pattern: coloured-bands; texture: grain
- Personality: friendly, playful
- Looks like: each section on a whole band of one colour, edge to edge, with the same grain on every band so they read as one material.
- Used on: 3 mockups: a small shop (three deep bands with grain), a volunteer page (a poster block over a board), and a tutoring site (one pale tinted band).

### Grain
- Id: grain
- Picks: texture: grain
- Personality: calm, friendly
- Looks like: a pale or dark ground with a fine speckle, like paper or plaster. The safest step up from plain.
- Used on: 4 mockups: a soap maker's shop, a poetry site (three of its alternative looks), a small shop, and a dark, painterly joke site. The most used option after plain.

### Material ground
- Id: material-ground
- Picks: texture: felt-weave
- Personality: friendly, playful
- Looks like: the ground is the material the site is made of, laid behind everything: the felt of a noticeboard, with notes pinned on it. For a stone wall, change the layers: `{"start": "material-ground", "texture": "grain", "pattern": "stone-courses"}`.
- Used on: 2 mockups: a volunteer page (a felt noticeboard under the events) and a dark, painterly joke site (a wall of dressed stone, which became its detailed ground).

### Painted ground
- Id: painted-ground
- Picks: scene: painted-ground
- Personality: playful, dramatic
- Looks like: the painted world from the picture at the top, carried on behind the panels as a repeating tile. Add `drawings: lots` and it becomes a detailed ground.
- Used on: 2 mockups: two game-style joke sites.

### Detailed ground
- Id: detailed-ground
- Picks: texture: mottled-and-hatched; drawings: lots; finds: on
- Personality: dramatic, playful
- Looks like: a full, lived-in room. The ground in its own colour, with mottling, hatching and grain; signs here and there, small and large, one off the edge, one half under a sheet; small things to find in the gaps. The words sit on calm sheets laid over it. Nothing is left as an empty patch, and from across the room it is still one colour. Worked out on three mockups; the owner chose it over a quieter ground for the same shop, and asked for it by name.
- Used on: 3 mockups: a dark, painterly joke site, a small shop with a dark lead, and a game-style joke site.

### One long scene
- Id: one-long-scene
- Picks: scene: one-long-scene
- Personality: playful, dramatic
- Looks like: there is no separate ground; the picture at the top goes on down the page band by band, each joined to the next by a wavy edge.
- Used on: 1 mockup: a game-style joke site, in both of its looks.

## Swatch book

`tests/parts/background.html` shows every option of every layer, then every starting point, each on a light page and on a dark one side by side; open it in a browser to choose by eye. It is built by `tests/parts/source/background.py` from `background-template.html` beside it, which draws the mask tiles; run `python3 background.py ../background.html` there to rebuild it.

## Not covered yet

- **A soft gradient** as the whole ground. No mockup used one: the shop that weighed it chose flat bands with grain, and the only gradients on the mockups were light (a lantern's glow, a sky). If a site wants one, it belongs with the light part guide's sky, or here as a new pattern once a mockup has tried it.
- **A plain repeating pattern** (stripes, checks, a printed motif). Hatching was used only inside the mottled texture, and dot weaves only as felt.
- **A photograph as the ground.** No mockup had real photographs.
- **Light pages with a detailed ground.** Every detailed ground on the first mockups was dark, and its first write-up was for dark pages only. A light-page detailed ground was then used once, on a bright repair-café mockup, where the old wording ("the rest stays dark or muted") did not fit. Every layer is now drawn from the shared names and shown on a light page in the swatch book; it has not yet been approved on a second light site.
- **Speed on slow phones** for the detailed ground and the long scene.
- **Long pages for the painted ground**: whether a tile that changes every few screens could stand in for one long scene.
- **Other painted worlds.** The painted ground is drawn as a rock cliff only; foliage, a forest floor or a cave would each need their own masks, drawn the same way (big shapes in a few values, one light side). Not yet tried on a site.
- **Texture on bands at full strength on a dark page.** Grain coloured `--on-band` shows well on both pages; on the dark page it is fairly strong, since `--texture-strength` is set there for a dark ground. If a site finds it too busy behind pale words, the colour part lowers the strength, and `audit` re-measures the words.
