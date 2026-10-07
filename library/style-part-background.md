---
name: Background (a part guide)
summary: What lies behind everything - the page's ground and what shows between its sections, from one flat colour to a detailed ground with signs and small things to find. Each option can be picked on its own and used with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: the mockups made with the skill so far, and the guides named in each option
---

# Background

A part guide. It covers what lies behind everything on a page: the ground under the sections, and what a visitor sees in the gaps between them and down the sides on a wide screen. A site picks one option in its own guide, and in the blueprint as `project.style.parts`: `{"background": "<option-id>"}`. The picked option wins over the feel guide for the background only; the feel guide still decides everything else. The general guide's accessibility minimums (contrast, text size, tap size) still hold whatever is picked.

The background is the largest area on the page and the one a visitor looks at least. That is why it sets the feel so strongly: the general guide gives the page's colour to the lead feel guide for this reason. A picked background takes the lead's colour unless the site's own guide says otherwise: a detailed ground under a warm lead is a detailed ground in warm's bold colour, not in night blue.

**Words never sit on a busy ground.** Every option from grain upwards keeps reading text on something calm laid over the ground: a sheet, a panel, a band of one colour. The ground is what shows round them. `check` and `audit` measure text over a texture or a picture from a photograph of the page, and the worst of what lies under the words decides.

## Choosing

| Option | What it feels like | Suits best | Fights |
|---|---|---|---|
| Plain | Clean, quiet, nothing between the reader and the words | Professional; artistic, when the signature carries the page | Warm, where it reads as a template |
| Coloured bands | Bold and flat, a poster in blocks | Warm; a shop with a dark lead | Professional, unless the colour is pale |
| Grain | Made, not printed; paper or plaster | Warm; artistic; a single maker | Little: it is the safest step up from plain |
| Material ground | The page is made of something from the subject | Warm; a dark, painterly lead | Professional |
| Painted ground | The picture's world, behind the panels | A game-style site | Anything meant to feel calm or official |
| Detailed ground | A full, lived-in room with something in every corner | A dark, painterly lead; artistic with a dense brief | Professional; a spare brief; long forms |
| One long scene | A journey: the world changes as you scroll | A game-style site; a story told down one page | Long reading; many pages that share one layout |

How to choose: start from the brief's line on how full the page should feel. Spare points to plain or grain, balanced to grain, bands or a material, dense to a detailed ground or a long scene. Then ask what the site is made of: if the brief already names a material (see the materials part guide), the ground is usually that material, plain or detailed. Only the last three need art made for the site; budget for it.

## Options

### Plain
- Id: plain
- Status: draft
- Looks like: one flat colour behind everything, usually a near-white with a little warmth. Sections are separated by space, and at most a hairline.
- Made with: the general guide's `--color-ground` token on the body, and nothing else. Sections are told apart by a larger gap than anything inside them; a second, slightly darker tint may mark one band (an "about" or a form) where space alone does not group it.

```css
:root { --ground: #f7f4ee; --ground-band: #f3f5ef; --ink: #1c1f23; --line: #d8d2c6; }
body { background: var(--ground); color: var(--ink); }
.band { background: var(--ground-band); }          /* one band at most, where space alone does not group it */
section + section { margin-top: var(--space-8); }  /* or a 1px rule in --line */
```

- Careful: the easiest option for contrast, since each pair is measured once and holds everywhere. The risk is the template look: a pale ground with one accent is tell 7 in the general guide, and the first volunteer page, plain all over, was called "very plain ... like I made it with a cheap make-your-own-website tool". Plain works only when the signature piece and the repeated item are designed; it gives them the stage.
- Goes with: `frames: none` or `hairline`; `materials: fine-paper`; `light: flat-and-even`.
- Used on: 4 mockups: a tutoring site, a browser game's pages for deciding, a poetry site in its default look, and the first version of a volunteer page.

### Coloured bands
- Id: coloured-bands
- Status: draft
- Looks like: each section sits on a whole band of one strong colour, edge to edge: deep red, then forest green, then night. On dark bands a fine grain in the band's own hue; nothing changes colour at a glance.
- Made with: one colour token per band, set on full-width sections, with the same grain tile laid over every band so they read as one material. Keep each band's text colour as a token too, and measure it against that band. A shaped edge between bands (a valance, a torn edge, a wave) comes from the frames part guide.

```css
:root { --band-a: #6a1a26; --band-b: #1f3a2c; --band-c: #1a0b12; --on-band: #f0e2c2;
  --grain: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.55 0'/%3E%3C/filter%3E%3Crect width='240' height='240' filter='url(%23n)'/%3E%3C/svg%3E"); }
.band { padding-block: var(--space-8) var(--space-7); background-image: var(--grain); color: var(--on-band); }
.band-a { background-color: var(--band-a); }
.band-b { background-color: var(--band-b); }
```

- Careful: a grain dark enough to show on a dark band will take soft text on a light sheet below 4.5:1; one shop needed a second, lighter grain (`0.22` in place of `0.55`) for its parchment. Bold colour widens the general guide's three colours but never lifts the contrast minimums: measure every band against its text. The warm guide's "bold and flat" was read on one shop as "one solid hue, no gradient", with grain allowed.
- Goes with: `frames: wavy-edge` or `torn-paper` between bands; `materials: wood-and-canvas` or `cut-paper-on-felt`; `density: balanced`.
- Used on: 3 mockups: a small shop (three deep bands with grain), a volunteer page (a yellow poster block over a blue board), and a tutoring site (one pale tinted band, the quiet end of this option).

### Grain
- Id: grain
- Status: draft
- Looks like: a pale or dark ground with a fine speckle, like paper or plaster. Close up it is made; from across the room it is still one colour.
- Made with: a small SVG tile drawn by `feTurbulence`, coloured by `feColorMatrix` so it only darkens (or only lightens, on a dark ground), at low strength. `stitchTiles='stitch'` makes the tile repeat without seams. Write it as a data URI, or a small file beside the stylesheet.

```css
:root { --ground: #f8f0e0; --ink: #2b2118;
  --grain: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='260' height='260'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.7' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.45 0 0 0 0 0.36 0 0 0 0 0.22 0 0 0 0.5 -0.13'/%3E%3C/filter%3E%3Crect width='260' height='260' filter='url(%23n)' opacity='0.55'/%3E%3C/svg%3E"); }
body { background: var(--ground) var(--grain); color: var(--ink); }
/* on a dark ground, a white speckle at about a tenth: values '0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .1 0' */
```

- Careful: text straight on grain is fine at this strength; the check measures it from a picture, and on the mockups here it passed. Turn the strength up only with the check run again. The grain is decoration: it is a background image, so nothing needs hiding from screen readers. It costs the browser a little to draw; a tile of 220 to 260 pixels was enough everywhere.
- Goes with: `materials: paper-and-tape` or `fine-paper`; `frames: torn-paper`; any light.
- Used on: 4 mockups: a soap maker's shop (warm paper), a poetry site (in three of its alternative looks), a small shop (on every band) and a dark, painterly joke site (over its wall). The most used option after plain.

### Material ground
- Id: material-ground
- Status: draft
- Looks like: the ground is the material the site is made of, laid behind everything: the felt of a noticeboard, a wall of dressed stone, the canvas of a stall. Sheets, notes and panels are pinned or set on it.
- Made with: the material's own technique from the materials part guide (`cut-paper-on-felt`, `stone-and-chalk`, `wood-and-canvas`), applied to the body or to the one wrapper that holds the sections, so it shows in every gap. A fine repeating mark makes the surface: a dot weave for felt, courses of near-shade rectangles for stone. Grain over it is optional.

```css
:root { --felt: #1e3f8f; --on-felt: #fffaf0; }
.board { background-color: var(--felt); color: var(--on-felt);
  background-image: radial-gradient(rgb(255 255 255 / 0.07) 1px, transparent 1.3px); background-size: 6px 6px; }
/* stone: a 420 x 208 SVG tile of blocks in three or four near shades, mortar lines in ink, a crack or two,
   repeated on the body with a fine white grain over it. Drawn once by a script; see materials: stone-and-chalk */
```

- Careful: keep the surface's pattern faint (the felt's dots are 7% white) so pale words straight on it still pass; anything long goes on a sheet. One material per page: the materials guide records that stone walls with a felt board read as stickers from different sets. A material ground with signs and things drawn on it has become a detailed ground; pick that instead.
- Goes with: the matching materials option, always; `frames: torn-paper` for notes on felt; `light: flat-and-even` or `one-light`.
- Used on: 2 mockups: a volunteer page (a felt noticeboard under the events) and a dark, painterly joke site (a wall of dressed stone, which became its detailed ground).

### Painted ground
- Id: painted-ground
- Status: draft
- Looks like: the painted world from the picture at the top, carried on behind the panels as a repeating tile: rock in broad strokes, with a few lit edges and shadow speckle. The panels float on it in heavy frames.
- Made with: a large SVG tile, about 1200 by 1400 and drawn by a script, of a few hundred rounded strokes in three or four shades of the ground colour, then hatching and stipple in the shadow colour, then shorter strokes in the light's colour at 12 to 30% for lit edges. Draw the strokes again one tile-width to each side so the tile wraps without a seam. Set it under a plain colour token so the page is the right colour before it loads.

```css
:root { --ground: #3e1812; --ground-art: url("art/world.svg"); }
html { background: var(--ground); }
body { background: var(--ground) var(--ground-art) center top / 1200px auto repeat; }
.panel { background: var(--panel); color: var(--text); }   /* words always on a panel, never on the strokes */
```

- Careful: no words on the strokes; the panels are opaque. The tile must be big (1200 pixels or more) or the repeat shows in a column of the same rocks. On the mockup it was made for, the guide it followed asked for "the same world, not a texture", and the repeating tile was recorded as still a texture: it is the fallback when one long scene is too much work. A second look (night, say) needs its own tile in its own colours, swapped with a custom property.
- Goes with: `frames: riveted-metal`; `materials: metal-and-dark-glass`; `light: daylight` or `moonlight`; `density: busy`.
- Used on: 2 mockups: two game-style joke sites (the earlier one also scattered hand-drawn signs over the strokes, which made it a detailed ground).

### Detailed ground
- Id: detailed-ground
- Status: draft
- Looks like: a dark ground in a colour of its own (night blue, oxblood), with grain, a slow mottling and fine hatching. Over it, hand-drawn signs here and there: circles with stars and triangles in them, a moon and an orbit, a written line in made-up letters, a branching mark. A few are large and set by hand: one runs off the edge of the page, one is half under a sheet. In the gaps and corners there are small things to find, drawn for the site: a ring of keys, a row of bottles, an inkpot, a bird on a bracket. The words sit on calm sheets laid over it. Nothing is left as an empty patch, and from across the room it is still one dark colour.
- Made with: five layers, each doing one job. They were worked out on three mockups and the owner chose this ground over a quieter one of the same shop.
  1. **The colour.** A dark token with a hue, never black: `--ground`. Everything else is laid over it, so recolouring the page is one line.
  2. **A large repeating tile, drawn by a script**, 640 by 720 or larger (the shop used 1400 by 2200, so the repeat is never seen): a slow mottling (`feTurbulence` with a stretched, low frequency such as `0.006 0.02`, coloured black at about 0.55), fine hatching (a 7-pixel pattern turned 38 degrees, at 0.3 to 0.35), a few hundred dark specks, and about one small sign for every 200 by 200 pixels. Each sign has its own size (14 to 58), turn and one of three muted colours from the page (a parchment, a cold blue, a rust) at 0.14 to 0.3, with no two closer than about 170 pixels. All signs are roughened by one displacement filter, so no line is machine-straight. Leave the tile transparent where it is not drawn, so the colour comes from the token.
  3. **A fine grain** over everything (white at about 0.1 on a dark ground), so even the calm parts are made.
  4. **Signs set by hand.** Ten to thirty larger signs (90 to 240 pixels), written as inline SVG that `use` a handful of shared symbols, each placed in the stylesheet with its own width, position and turn. Chalk colour at half strength on the ground; dark ink at about 0.6 in the corner of a sheet, clear of the words. Some run off the page edge, some sit half under a sheet, some cross the band between sections. On the first mockup there were twenty-eight of nine kinds.
  5. **Small things to find.** Three to six little drawings in the gaps, about 4 to 13rem wide, in the page's colours and roughened by the same filter: an object from the subject, never a stock icon. They appear only where there is a gap to hold them, from about 48rem, and a heading beside one is narrowed to make room.

```css
:root { --ground: #17142e; --chalk: #a9b4e6; --ink: #1d0f08;
  --grain: url("data:image/svg+xml,...");          /* white speckle at 0.1, 220px tile */
  --detail: url("art/ground.svg"); }               /* mottling, hatching, specks and small signs; transparent */
body { background-color: var(--ground); background-image: var(--grain), var(--detail); background-size: 220px, 640px auto; }
.wall { overflow-x: clip; }                         /* signs run off the edge here; clip, not hidden, so sticky still works */
.sign { position: absolute; z-index: -1; max-width: none; pointer-events: none; fill: none; stroke: currentColor;
  stroke-width: 2; stroke-linecap: round; filter: url(#pen); }
.sign * { vector-effect: non-scaling-stroke; }       /* the same line weight at any size */
.sign.chalk { color: var(--chalk); opacity: 0.5; }
.sign.inkmark { z-index: 1; color: var(--ink); opacity: 0.6; }
.s1 { width: 190px; left: -112px; top: -124px; rotate: 14deg; }   /* each one placed by hand */
.find { display: none; position: absolute; pointer-events: none; }
@media (min-width: 48rem) { .find { display: block; } .find-keys { width: 6rem; right: 9%; bottom: var(--space-4); } }
```

```html
<svg width="0" height="0" style="position: absolute" aria-hidden="true" focusable="false"><defs>
  <filter id="pen"><feTurbulence type="fractalNoise" baseFrequency="0.09" numOctaves="2" seed="4" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="3" xChannelSelector="R" yChannelSelector="G"/></filter>
  <symbol id="sg-ring" viewBox="0 0 100 100"><circle cx="50" cy="52" r="45"/><path d="M50 10L88 76H12Z"/><circle cx="50" cy="54" r="12"/></symbol>
</defs></svg>
<svg class="sign chalk s1" viewBox="0 0 100 100" aria-hidden="true" focusable="false"><use href="#sg-ring"/></svg>
```

- Careful:
  - Reading text never sits on the ground. It goes on sheets (`materials: parchment-and-ink` on the mockups) or on a plain dark slab; these are the calm patches. The form, its fields and the footer stay plain and dark, each with at most one sign in a corner.
  - A sign is never over words or a control. Hand-placed signs sit behind (`z-index: -1` or 0), ink marks in a sheet's margin only, and all have `pointer-events: none`.
  - Every sign and drawing is `aria-hidden="true"` and `focusable="false"`; none carries meaning.
  - Signs that run off the edge are clipped by `overflow-x: clip` on one full-width wrapper. `overflow: hidden` there breaks every sticky thing inside it (see `css-layout.md`).
  - On a phone there is almost no ground to draw on (about 12 pixels each side). Hide the things to find and most large signs below 48rem; keep a few as slivers at the edges and let the ink marks in the sheets' margins do the work. Widen the gaps and let more appear from 48rem and 62rem.
  - Measure: on the first mockup, after the owner asked for more parchment, the whole-page picture was 58% dark and 40% parchment (it had been 94% dark). A detailed ground with no calm patches is too dark to read.
  - Speed: the filters are drawn by the browser. Bake the mottling, hatching and small signs into one SVG file; keep live filters for the few hand-placed signs. Not yet tried on a slow phone.
  - Under a warm lead, the ground keeps its fullness but takes warm's colour and warm's things: cut paper, bunting, members' drawings, in place of chalk signs on night blue.
- Goes with: `materials: parchment-and-ink` or `stone-and-chalk`; `frames: inked-panel` or `carved-plate`, with a band between sections that carries signs too; `light: one-light`; `lettering: bladed-letters`; `density: busy`.
- Used on: 3 mockups: a dark, painterly joke site (a stone wall with chalk signs and things in the gaps; the owner asked for more signs "drawn in random places" and then approved it), a small shop with a dark lead (oxblood with grain, hatching and scattered signs; chosen by the owner over the same shop with a quieter ground), and a game-style joke site (painted strokes with signs and sign-circles). The owner asked for this option by name.

### One long scene
- Id: one-long-scene
- Status: draft
- Looks like: there is no separate ground. The picture at the top goes on down the page, band by band: a road to a castle, then a meadow and a stream, then a trader's stall, then a camp, then a cave. Each band ends in a wavy edge in the next band's ground colour, so the world joins up as the visitor scrolls. Panels sit on each band.
- Made with: every section is a band with `position: relative; isolation: isolate; overflow: clip`. Inside it, first, an inline SVG painting stretched to the band with `preserveAspectRatio="xMidYMin slice"` (the top band uses `xMidYMax` so its ground stays at the foot), then a short SVG of a wavy edge pinned to the band's foot in the next band's colour, then the content. A shared displacement filter roughens the painted shapes. Wider than a phone, put the panel to one side and the painting's subject (a figure, a stall) in the other half, where it shows.

```css
.band { position: relative; isolation: isolate; overflow: clip; padding: var(--space-8) var(--gutter); }
.band > .paint { position: absolute; inset: 0; width: 100%; height: 100%; z-index: -1; max-width: none; }
.band > .edge  { position: absolute; bottom: -1px; left: 0; width: 100%; height: 56px; z-index: -1; max-width: none; }
.panel { max-width: 44rem; background: var(--panel); color: var(--text); }   /* opaque, or 0.9 at least */
```

```html
<section class="band">
  <svg class="paint" viewBox="0 0 1600 1100" preserveAspectRatio="xMidYMin slice" aria-hidden="true" focusable="false">...</svg>
  <svg class="edge" viewBox="0 0 1600 80" preserveAspectRatio="none" aria-hidden="true" focusable="false">
    <path d="M0 80V52Q50 66 120 50Q250 18 400 52Q560 90 720 54Q880 16 1020 48Q1180 86 1330 52Q1470 20 1600 46V80Z" fill="var(--next-ground)"/></svg>
  <div class="panel">...</div>
</section>
```

- Careful: daylight scenes are bright, and pale words on a sky fail; every word goes on a dark panel (see `light: daylight`). With `slice`, the sides of the painting are cut on a phone: keep the important things near the middle of each band, or move them to a strip in the flow on a phone. The painting is decoration and is hidden from screen readers; if a figure in it matters, say so in words. Any movement in the world stops under reduced motion. It is a lot of drawing: one band per section, each different, and a second look needs all of them again.
- Goes with: `frames: riveted-metal`; `light: daylight` or `sky-by-the-clock`; `density: busy`.
- Used on: 1 mockup: a game-style joke site, in both of its looks (day and night). It answered the earlier site's open question of how a long page continues one painting downwards.

## Swatch book

`tests/parts/background.html` shows every option live; open it in a browser to choose by eye. Its painted and detailed tiles are drawn by `tests/parts/source/background.py` from `background-template.html` beside it; run `python3 background.py ../background.html` there to redraw them.

## Not covered yet

- **A soft gradient** as the whole ground. No mockup used one: the shop that weighed it chose flat bands with grain, and the only gradients on the mockups were light (a lantern's glow, a sky). If a site wants one, it belongs with the light part guide's sky, or here as a new option once a mockup has tried it.
- **A plain repeating pattern** (stripes, checks, a printed motif). Hatching and dot weaves were used only inside the detailed ground and the material ground.
- **A photograph as the ground.** No mockup had real photographs.
- **Light pages with a detailed ground.** Every detailed ground so far was dark. How signs and things to find look on a bright warm page is untried.
- **Dark mode.** Only sites with a designed second look were made; nobody has asked for a ground to darken by itself.
- **Speed on slow phones** for the detailed ground and the long scene.
- **Long pages for the painted ground**: whether a tile that changes every few screens could stand in for one long scene.
