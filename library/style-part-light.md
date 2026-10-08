---
name: Light (a part guide)
summary: Where the light on a page comes from and what it does, in layers that switch on their own - direction, shadows, glow, sky and focus - from no light at all to one lamp in a dark room or a sky that follows the clock. It owns every shadow, glow and pool of light on the page, so paper, frames and panels all cast the same shadow from the same side. Each layer works on a light page and a dark one, and can be picked with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: research online (six kinds of source, listed under Sources), the light of 13 mockups made with the skill, the problems four of them met with this part's first version, and the feel guides named in each option
---

# Light

A part guide. It covers the light on a page: where it comes from, what raised things cast, what gives off light, the colour of the light, and where it leads the eye. It is made of five layers, each one decision that switches on its own: **direction**, **shadows**, **glow**, **sky** and **focus**. A site picks a starting point whole, or a starting point with one layer changed, in its own guide and in the blueprint as `project.style.parts`: `{"light": "one-light"}`, or `{"light": {"start": "field-journal", "sky": "none"}}`. The pick wins over the feel guide for the light only. The general guide's accessibility minimums (contrast, text size, tap size) still hold whatever is picked.

**This part owns every shadow, glow and pool of light on the page** (the owners table in the general guide). A material or a frame decides the *shape* of a thing (a torn edge, a strip of tape, a riveted plate); this part decides the shadow it casts and the light that falls on it. So when two other parts each bring a shadow recipe, neither is used: both take this part's. That settles the clash met on the field-notebook mockup, where torn paper (a `filter: drop-shadow()`) and paper-and-tape (a `box-shadow`) gave opposite recipes for the same sheet (see "Paper on paper" below).

**This part does not own the page's colour or what lies on the ground.** How dark the page is comes from the colour part's tone; what is drawn behind the sections comes from the background part. Light tints and shades what is already there, with the shared colour names (see "Parts, layers and the shared colour names" in the general guide) and two blend modes: `multiply` to darken and colour, `screen` to brighten (R8). So daylight over a felt board is a felt board in daylight, not a sky painted over it: the field notebook met "the material ground and daylight both claim the whole ground", and the answer is that only the background claims the ground. A painted sky is a background scene; this part gives it its light.

**Words never sit in the light's effects.** Every layer below draws on the ground and on the things on it, and never over the sheet that holds the words: the sheet keeps its own colour at every hour and under every lamp, so its text is measured once. Words straight on the ground (`--on-ground`) are measured at the worst state of the light: the darkest hour of a sky, the far corner of a vignette.

## How it is built

Every option sets a few custom properties on the page root, and the rest of the page reads them. The light that blends (a lamp's pool, a sky, a vignette) is drawn on two layers fixed over the window, `body::before` (multiply: it darkens and colours) and `body::after` (screen: it brightens), over the ground and the bands and under everything a reader needs; each option adds its gradients to one or both through its own `--light-…` values, so any set of picks stacks on the same two layers, and words on sheets never sit in the light. One lesson from building the swatch book: **a blend mode on a `::before` inside an element that has a `z-index` blends only inside that element**, so it paints as plain colour; the layers are on `body`, which has none. All of this is under "Base" below; a thing whose outline is not its own box (torn paper, a cut tag) takes `filter: var(--drop-low)` in the part that draws its shape (see "Paper on paper").

What the layers hand to the rest of the page:

| Property | Set by | What it is |
|---|---|---|
| `--lx`, `--ly` | direction | which way shadows fall, as two numbers (`0`, `1` is straight down). Every shadow's offset is a multiple of them, so all share one light (R5) |
| `--hx`, `--hy` | direction | the lit edge: where a raised thing on a dark page catches the light |
| `--light-at` | direction | where the light is, as a position for gradients (the sun, the lamp, the sky's bright side) |
| `--shadow-low`, `--shadow-mid`, `--shadow-high` | shadows | three heights, as `box-shadow` values: a button or a sheet lying on another; a sheet or card on the page; a menu, popover or dialog |
| `--drop-low` | shadows | the low shadow as a `filter`, for shapes that are not their own box |
| `--edge-lit` | shadows | a one-pixel lit edge, seen only on a dark page |
| `--shade` | sky (default `rgb(var(--shadow-rgb))`) | the colour of shadows: the page's own hue from the colour part, turned cooler by a warm sky |
| `--shadow-strength` | this part | how dark shadows are. The colour part gives it a starting value per tone; a site that wants its shadows lighter or darker changes that one number in its own guide, never per element |
| `--lamp-lch`, `--lamp` | glow, turned by sky | the colour of light that things give off, as three oklch numbers and as a colour. Warm tungsten gold by default; never the accent unless a site says so |
| `--light-rim`, `--drop-rim`, `--light-bloom` | glow | glows added to the shadows of sheets, controls and the main button (this part adds them to the hooks itself; `--drop-rim` is for the part that draws a cut or torn shape: `filter: var(--drop-low) var(--drop-rim)`) |

Every shadow colour is written as the shade at a strength: `color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * k) * 100%), transparent)`, where `k` is the option's own number. The `min(1, ...)` keeps it valid if a site turns the strength up.

**The colour of the light itself** (a lamp's gold, a sky's blue, a sunset's peach, the moon) belongs to no colour name: it is light, not paint. This part writes it as three numbers, lightness, chroma and hue, and turns them into a colour with `oklch(var(--lamp-lch))`, so a site can shift a sunset or a lamp without writing a colour, and these colours are only ever blended over the ground or used as glow, never for words, lines or controls.

**A lamp is warm light, not the accent.** The first version lit the lamp in the accent colour; with a green accent that made a teal lamp, and a lantern on a light page read as a grey-blue smudge with a teal dot. Light from a flame or a bulb is warm whatever the page is: a candle is about 1,800 K and a household bulb 2,700 to 3,000 K (R22). So the glow layer carries its own colour, `--lamp`, warm tungsten gold by default. The sky turns it for things that only catch light: under a day sky a rim is sunlit gold, at dusk amber, under a night sky moonlit blue. A lamp is its own source, so `glow: lamp` keeps it warm under any sky: a lantern at night is warm light in a blue night. A site that wants its light in its own colour (a magic glow in the accent, a neon sign) says so in its guide and sets `--lamp: var(--accent)` on the page; the main button still takes the lamp's colour only when the colour part's accent is already warm (amber, as in the sorcery and lantern-fair colour starts). In the code: "Base" sets `--lamp-lch` to tungsten gold unless a sky has set `--light-sky-lamp` (day sunlight `0.86 0.11 85`, dusk amber `0.8 0.14 55`, night moonlight `0.8 0.08 235`), and `glow: lamp` sets `--lamp-lch` back to tungsten itself, so a lamp is always its own warm light.

## Choosing

Start from a starting point (below), then change a layer if the brief asks for it.

| Starting point | What it feels like | Suits best | Fights |
|---|---|---|---|
| Flat and even | No light at all: a page, not a picture | Professional or artistic, with a toned ground or a strong signature | A scene that is meant to be lit |
| Professional | Even, soft light from above; only things that float have a shadow | Professional; civic | Warm (too clean), anything hand-made |
| Warm | A kitchen table by a window: paper lying on paper | Warm; a single maker | A dark lead |
| Daylight | Bright open air, a high sun, hard little shadows | A game-style or playful site; outdoors | Anything hushed or official |
| Moonlight | Night, cool and quiet; everything visible but blue | Artistic; a second look | Warm, professional |
| Sky by the clock | The page keeps time: day, dusk, night as the hours pass | A place people come back to | Anything that must look the same in every picture |
| Almanac plate | Printed charts under the visitor's own sky | A society, an observatory, a garden | Shops (the product must look the same at every hour) |
| One light | A room with one lamp in it; the rest falls away | Artistic; a dark, painterly lead | Warm (it wants the whole page bright), professional |
| Spotlight on the main thing | The light picks out the one thing that matters | Sales (the product); one light | A page with no single main thing |
| Glow on edges | Bright rims on small things, like a game screen | A game-style site, small marks only | Professional; anything meant to look hand-made |
| Sorcery | A low lamp in a dark room; the corners are lost | The dark, painterly guide | Anything bright |
| Gilded dark | Panels over a bright painted world, rimmed in light | The game-interface guide | Calm or official sites |
| Lantern fair | One paper lantern over a market at night | A night market; a shop with a dark lead | Daytime services |
| Field journal | Taped-in pages in morning sun | A walking club, a naturalist, a garden | A dark lead |
| Repair cafe | Cut card and pegboard: flat light, hard shadows | A bright community page, busy and hand-made | Professional; a calm brief |

How to choose:

- **The colour part decides how bright the page is; this part decides where the light is.** A dark tone with one lamp is one light; a light tone with one lamp is a light page with a warm pool on it, quieter (the swatch book shows both). If the brief wants the page to be a dark room, pick a dark or lamplit tone first.
- **One light per look.** Two sources on one page (a bright sun and a lamp) fight over which is brightest; on one mockup the painted sun had to be dimmed so the light the figure held stayed the brightest thing. The exception is the clock: by day the sun, at night a lamp, never both at full strength.
- **One direction per page.** Every shadow, every lit edge, the ball of light in a picture and the lamp in a drawing come from the same side (R5). Decide it before drawing: a glow laid over a picture depends on where its light is.
- **A site with two looks** may pick a light for each, and a site may use two lights on different pages when each page is a different place: the 3D game kept its pages for deciding in flat daylight and its game screen underground, lit by lamps.

## Base

What every pick of this part needs: the values the options build on, the shadows the shared hooks cast, the two layers of light, and what the visitor's settings switch off. `style css` lifts it whatever is picked.

- **The two layers are fixed over the window,** so a lamp, a sky or a vignette stays where the window is as the page scrolls, as a room's light would. Each is drawn only when an option fills it (the `content: ""` is in the option), so a page with no blended light pays nothing for it.
- **They sit over the ground and the bands, and under everything a reader needs** (`z-index: 1` on `<body>`'s own layers; see "Who draws where" in the general guide). They light the colour part's ground, the background part's texture, drawings and coloured bands, and a band's fill; sheets and panels stand at `z-index: 2`, and so does every child of a band that is not a drawing (every drawing carries `aria-hidden="true"`), so headings, words, forms and sheets keep their own colour under any lamp or sky. For that to hold, `.page` and `.band` must never be stacking layers of their own (no `isolation`, `z-index`, `filter`, `opacity` below 1 or `transform` on them): a blend layer cannot reach into one, and one would carry every sheet in it under the light. The background part writes the same stacking rule, so either part alone keeps it. A lamp now shows over coloured bands, as on a night market's.
- **Shadows on the hooks:** a sheet or card on the page takes the mid shadow, a sheet on a sheet the low one, a panel (a menu, a dialog) the high one, a button the low one. A part that draws a cut or torn outline on a hook's `::before` sets `box-shadow: none` on it and `filter: var(--drop-low) var(--drop-rim)` instead, never both.

```css assemble
/* light, base: the values every option builds on. --shadow-rgb and --shadow-strength come from the colour part. */
& { --light-dx: calc(var(--lx, 0) * 1px); --light-dy: calc(var(--ly, 1) * 1px);
  --shade: rgb(var(--shadow-rgb, 60 45 30));
  --lamp-lch: var(--light-sky-lamp, 0.84 0.13 78); --lamp: oklch(var(--lamp-lch));   /* tungsten gold unless a sky turns it */
  --light-rim: 0 0 transparent; --light-bloom: 0 0 transparent; --drop-rim: opacity(1); }
/* the shadows every raised hook casts: one light for the whole page */
.sheet { box-shadow: var(--shadow-mid), var(--edge-lit, 0 0 transparent), var(--light-rim); }
.sheet .sheet, .sheet .panel { box-shadow: var(--shadow-low), var(--edge-lit, 0 0 transparent), var(--light-rim); }   /* paper on paper */
.panel { box-shadow: var(--shadow-high), var(--edge-lit, 0 0 transparent), var(--light-rim); }
.btn { box-shadow: var(--shadow-low), var(--light-rim); }
.btn-main { box-shadow: var(--shadow-low), var(--light-rim), var(--light-bloom); }
/* the two layers of light, between the ground and the sheets; an option fills them */
body::before, body::after { position: fixed; inset: 0; z-index: 1; pointer-events: none; }   /* over the ground and the bands, under the words (2) */
:is(.sheet, .panel) { position: relative; z-index: 2; }                           /* never in the light */
:where(.band > :not([aria-hidden="true"])) { position: relative; z-index: 2; }   /* words straight on a band too; drawings (aria-hidden) stay lit */
body::before { mix-blend-mode: multiply; background-blend-mode: multiply;
  background: var(--light-vignette, none), var(--light-lamp-shade, none), var(--light-sky-mul, none); }
body::after { mix-blend-mode: screen; background-blend-mode: screen;
  background: var(--light-lamp-pool, none), var(--light-sky-scr, none); }
/* what the visitor's settings switch off */
@media (prefers-contrast: more) {   /* atmosphere down, glows off: the words and edges carry everything (R10) */
  body::before, body::after { opacity: 0.35; }
  & { --light-rim: 0 0 transparent; --light-bloom: 0 0 transparent; --drop-rim: opacity(1); }
}
@media (forced-colors: active) {   /* the browser removes every shadow and gradient (R9); the frames part gives sheets an edge */
  body::before, body::after { display: none; }
}
```

## Layers

### Direction
- Layer: direction
- Owns: where the light comes from. It sets the side every shadow falls to, the edge that catches the light, and the point the glow and the sky gather round. It draws nothing itself.
- Default: overhead

#### None
- Id: none
- Status: draft
- Looks like: no source at all. Shadows, if any, sit evenly round each thing, like a cloudy day; nothing has a bright side.
- Made with: both numbers at zero, so every offset is zero and only the blur shows. Washes gather in the middle.

```css assemble
& { --lx: 0; --ly: 0; --hx: 0; --hy: 0; --light-at: 50% 30%; }
```

- Careful: with `shadows: crisp` a shadow with no offset is hidden behind its own sheet: crisp needs a direction. With `shadows: soft` it is an even haze round each sheet, which reads as a glow more than a shadow on a light page.
- Light and dark: the same on both; nothing has a lit edge.
- Personality: serious, calm
- Goes with: `light: shadows none` (the flat-and-even page); `light: glow none`.
- Used on: 1 mockup: a quiet gallery of pots, drawn flat like cut paper with no shading at all.

#### Overhead
- Id: overhead
- Status: draft
- Looks like: light from straight above. Every shadow falls just below its sheet, a little more for things that float higher. The look of most design systems.
- Made with: no sideways offset. Fluent and Material place their shadows straight down, the offset growing with height (R3, R4).

```css assemble
& { --lx: 0; --ly: 1; --hx: 0; --hy: 1; --light-at: 50% 2%; }
```

- Careful: the safest choice, and the most anonymous. On a page meant to feel made by hand, a slight angle (top left or top right) reads as a real room.
- Light and dark: on a dark page the lit edge is a one-pixel line along the top of each raised sheet.
- Personality: any
- Goes with: `light: shadows soft`; `light: sky by-the-clock` (the sun is high most of the day).
- Used on: most mockups so far, without saying so: a soap shop, a poetry site, a volunteer page, an observatory and a 3D game all drop their shadows straight down.

#### Top left
- Id: top-left
- Status: draft
- Looks like: light from above and to the left, so shadows fall down and a little right. The long habit of screens, and of right-handed drawing.
- Made with: the shadow's sideways offset half its drop, so the drop is twice the sideways shift: "the vertical offset is always 2x the horizontal one" (R5).

```css assemble
& { --lx: 0.5; --ly: 1; --hx: 1; --hy: 1; --light-at: 8% 6%; }
```

- Careful: the lit edge runs along the top and the left of each sheet, so a sheet with a border on those sides doubles it; frames that draw a top highlight should take `--hx` and `--hy` too.
- Light and dark: as overhead, with the lit edge on two sides.
- Personality: calm, friendly, playful
- Goes with: `light: shadows paper-lift` or `crisp`; `light: glow lamp` (the lamp in the upper left of the picture).
- Used on: 2 mockups: a repair café (every card's hard shadow falls down and right) and a joke site in an inked style (`5px 6px 0` under its slabs).

#### Top right
- Id: top-right
- Status: draft
- Looks like: light from above and to the right: a window on the other side, or a sun or lantern placed top right in the picture.
- Made with: the mirror of top left.

```css assemble
& { --lx: -0.5; --ly: 1; --hx: -1; --hy: 1; --light-at: 92% 6%; }
```

- Careful: pick it when the picture already has its light on the right; do not pick it only for variety. On the night market and the field notebook, the lantern and the sun were drawn top right first, and the shadows followed.
- Light and dark: as top left, mirrored.
- Personality: calm, friendly, dramatic
- Goes with: `light: sky day` (a sun top right), `light: glow lamp` (a lantern top right).
- Used on: 2 mockups: a field notebook (a faint warm wash from the top right, every shadow falling down and left), a night market (one paper lantern top right).

#### Low side
- Id: low-side
- Status: draft
- Looks like: a low light from one side, late in the day or from a lamp on a table. Shadows are long and fall sideways; things are lit on one flank. In painting, a single low source is what makes a scene feel still or dramatic (R18).
- Made with: a sideways offset larger than the drop.

```css assemble
& { --lx: 2; --ly: 0.7; --hx: 2; --hy: 0; --light-at: 2% 45%; }
```

- Careful: long sideways shadows on every card get heavy on a busy page: keep it for pages with few raised things, or with `shadows: soft`. Long cast shadows drawn as a flat stripe (the flat-design fashion of the 2010s) are not this: a shadow here is still soft or crisp, only longer.
- Light and dark: on a dark page the lit edge is on the light's side only, two pixels: a rim of light.
- Personality: dramatic
- Goes with: `light: glow lamp` (a lamp low in the picture); `light: sky dusk`; `light: focus vignette`.
- Used on: no mockup yet as a whole page. The painted wizard pictures behind the sorcery guide are lit this way (an orb on a table lighting a face from below and to one side).

### Shadows
- Layer: shadows
- Owns: what raised things cast: three heights (low, mid, high) as `box-shadow` values, the low one again as a `filter`, the shade's strength, and the lit edge a raised thing gets on a dark page. Every sheet, card, button, menu and paper on the page takes one of these; no other part writes a shadow.
- Default: soft

**Paper on paper.** Every sheet lying on another sheet takes the **low** shadow, whatever it lies on: its height is counted from what is under it, so a stack of notes never adds up to a floating dialog. A thing whose outline is its own box (a card, a plain sheet) takes it as `box-shadow: var(--shadow-low)`. A thing whose outline is not its box (torn paper clipped on its `::before`, paper with tape sticking past its edge, a die-cut label, an SVG shape) takes the same shadow as `filter: var(--drop-low)` on the element, because `box-shadow` follows the box and is cut off by a clip, and a drop shadow follows the drawn shape, tape included (R5). Never both on one element. The frames part's rule still holds: the clip goes on the `::before`, never on the element, so its shadow and focus ring are not clipped. So torn paper taped to a page is: the paper's shape from frames, the tape from materials, `filter: var(--drop-low)` from here.

#### None
- Id: none
- Status: draft
- Looks like: nothing is raised. Sheets are told apart from the ground by their colour, a line or space alone.
- Made with: every shadow transparent, so lists of shadows that add a glow still work.

```css assemble
& { --shadow-low: 0 0 transparent; --shadow-mid: 0 0 transparent; --shadow-high: 0 0 transparent;
  --drop-low: opacity(1); --edge-lit: 0 0 transparent; }
```

- Careful: with no shadow, a white sheet on a pale ground, and paper on paper, can vanish: in the swatch book the torn card on a white card has nothing to separate it. Give sheets a colour a clear step from the ground (the colour part's toned or mid tone), or a line from the frames part. Menus and dialogs still need to stand off the page: give them a border and the scrim behind them.
- Light and dark: on a dark page sheets are told apart only by `--surface` against `--ground`; a hairline in `--line` helps more than on a light one.
- Personality: serious, calm
- Goes with: `light: direction none`; `frames: hairline`; a toned ground.
- Used on: 2 mockups: a quiet gallery of pots ("no shadow at all: pots are drawn flat, like cut paper, so nothing is raised") and a tutoring site (inset rules and underlines only).

#### Soft
- Id: soft
- Status: draft
- Looks like: layered, soft shadows that grow larger, softer and fainter the higher a thing floats. Close to the page they are small and dark; far from it, wide and faint. The usual good web shadow.
- Made with: two or three shadows stacked, each twice the offset of the last, blur about twice the offset, in the page's own hue rather than black (R5, R6). Each design system that documents shadows builds them from a sharp "key" shadow near the edge and a soft "ambient" one further out (R3, R4).

```css assemble
& {
  --shadow-low: var(--light-dx) var(--light-dy) 2px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.55) * 100%), transparent),
    calc(var(--light-dx) * 2) calc(var(--light-dy) * 3) 6px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.4) * 100%), transparent);
  --shadow-mid: var(--light-dx) calc(var(--light-dy) * 2) 3px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.5) * 100%), transparent),
    calc(var(--light-dx) * 4) calc(var(--light-dy) * 6) 12px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.4) * 100%), transparent),
    calc(var(--light-dx) * 10) calc(var(--light-dy) * 16) 32px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.35) * 100%), transparent);
  --shadow-high: calc(var(--light-dx) * 2) calc(var(--light-dy) * 4) 6px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.45) * 100%), transparent),
    calc(var(--light-dx) * 8) calc(var(--light-dy) * 14) 28px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.4) * 100%), transparent),
    calc(var(--light-dx) * 20) calc(var(--light-dy) * 34) 64px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.35) * 100%), transparent);
  --drop-low: drop-shadow(var(--light-dx) var(--light-dy) 1px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.55) * 100%), transparent))
    drop-shadow(calc(var(--light-dx) * 2) calc(var(--light-dy) * 3) 3px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.4) * 100%), transparent));
  --edge-lit: inset calc(var(--hx) * 1px) calc(var(--hy) * 1px) 0 light-dark(transparent, color-mix(in oklab, var(--ink) 14%, transparent)); }
```

- Careful: this is half of the second template tell in the general guide: "every repeated item is the same white box with rounded corners and a soft shadow". Soft is right for things that really float (a menu, a dialog, one panel holding a form); for repeated items on a warm or artistic site, pick paper lift or crisp, or no shadow and a frame. A `drop-shadow()` blur is about half its `box-shadow` blur for the same look, which is why the filter's numbers are smaller. Paper on paper: a faint, soft lift.
- Light and dark: on a light page the shade is the page's own brown-grey at about a fifth. On a dark page shadows barely show (R1, R2): each raised thing is drawn in `--surface-raised`, lighter the higher it is, and gets a one-pixel lit edge on the light's side (Fluent and Windows give every surface a one-pixel stroke for the same reason, R3, R4). The shadows are kept, darker, as Atlassian keeps them (R2).
- Personality: serious, calm, friendly
- Goes with: `light: direction overhead`; `frames: card` (for the things that float); any sky.
- Used on: 1 mockup: a 3D game (`0 8px 24px` under its panels); and the general guide's starting tokens (`--shadow`), so every mockup that kept them.

#### Paper lift
- Id: paper-lift
- Status: draft
- Looks like: a tight, dark contact line where the paper touches what it lies on, and a soft lift below it that starts inside the paper's edge. Paper on a table, notes on a board, a taped-in page: thin things that do not float.
- Made with: two shadows. The contact shadow is offset by one pixel with one pixel of blur; the lift has a negative spread, so it shows only below the sheet and not round its sides. The same two as a filter for torn and taped paper.

```css assemble
& {
  --shadow-low: calc(var(--light-dx) * 0.5) var(--light-dy) 1px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.1) * 100%), transparent),
    calc(var(--light-dx) * 2) calc(var(--light-dy) * 4) 7px -2px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.7) * 100%), transparent);
  --shadow-mid: calc(var(--light-dx) * 0.5) var(--light-dy) 1px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.1) * 100%), transparent),
    calc(var(--light-dx) * 5) calc(var(--light-dy) * 10) 18px -6px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.9) * 100%), transparent);
  --shadow-high: calc(var(--light-dx) * 0.5) var(--light-dy) 1px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.1) * 100%), transparent),
    calc(var(--light-dx) * 9) calc(var(--light-dy) * 18) 30px -10px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1) * 100%), transparent);
  --drop-low: drop-shadow(calc(var(--light-dx) * 0.5) var(--light-dy) 0.5px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.1) * 100%), transparent))
    drop-shadow(calc(var(--light-dx) * 2) calc(var(--light-dy) * 4) 3px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 0.6) * 100%), transparent));
  --edge-lit: inset calc(var(--hx) * 1px) calc(var(--hy) * 1px) 0 light-dark(transparent, color-mix(in oklab, var(--ink) 12%, transparent)); }
```

- Careful: a `drop-shadow()` cannot take a spread, so the filter's lift is a little wider than the box's; side by side on one page the difference does not show. Paper on paper is this option's own case: a crisp contact line under every note. The materials part's fine paper, paper and tape, and cut paper on felt, and the frames part's torn paper each wrote their own numbers before this part owned shadows; with this option picked, they all use these.
- Light and dark: on a dark page the contact line is near black and the lift a darker pool; the paper's own lighter `--surface-raised` and the lit edge do most of the work. Paper on a dark page reads best when the paper is pale (the colour part's lamplit tone).
- Personality: calm, friendly, playful
- Goes with: `light: direction top-left` or `top-right`; `materials: paper-and-tape`, `fine-paper` or `cut-paper-on-felt`; `frames: torn-paper`.
- Used on: 5 mockups: a field notebook (taped sheets, `drop-shadow(-2px 3px 0)` and a soft one, falling down and left), a soap shop, a poetry site and an observatory (each `0 1px 2px` and a lift with a negative spread), and a volunteer page (notes on felt, two drop shadows).

#### Crisp
- Id: crisp
- Status: draft
- Looks like: a hard, flat offset with no blur, like a block print, a cut-out card or a comic panel. Sunlight on a clear day: a small, sharp shadow.
- Made with: one shadow, no blur, offset along the direction, in the shade at a strength the eye reads as a shadow, not a second border.

```css assemble
& {
  --shadow-low: calc(var(--light-dx) * 2) calc(var(--light-dy) * 3) 0 color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.6) * 100%), transparent);
  --shadow-mid: calc(var(--light-dx) * 4) calc(var(--light-dy) * 6) 0 color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.6) * 100%), transparent);
  --shadow-high: calc(var(--light-dx) * 7) calc(var(--light-dy) * 10) 0 color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.6) * 100%), transparent);
  --drop-low: drop-shadow(calc(var(--light-dx) * 2) calc(var(--light-dy) * 3) 0 color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.6) * 100%), transparent));
  --edge-lit: 0 0 transparent; }
```

- Careful: it needs a direction (`none` hides it behind the sheet). A shadow in solid ink (`5px 6px 0` in the pen colour) is the frames part's inked panel, a drawn line rather than light; this is the shade, partly see-through, so the ground shows through it. A button that is pressed moves into its shadow (`translate` by the low offset, and the shadow goes); that movement stops under reduced motion. Paper on paper: a hard sliver under each card, like cut card laid on cut card.
- Light and dark: on a light page a soft brown-grey slab; on a dark page a near-black one, which reads as a cut-out against the dark ground and needs no lit edge.
- Personality: playful, friendly
- Goes with: `light: direction top-left`; `frames: inked-panel`; `light: sky day`.
- Used on: 4 mockups: a repair café (`1px 2px 0` and `2px 3px 0` on cards and pegged notices), a joke site in an inked style, a volunteer page's buttons (`0 4px 0`), and a game-style joke site's buttons (`0 3px 0`).

#### Deep
- Id: deep
- Status: draft
- Looks like: heavy, dark shadows: panels standing well off a dark painted world, tags hanging in front of a stall, a heavy frame on a wall.
- Made with: a close, dark shadow and a large, very soft one, both stronger than soft. On a dark page the shade is near black at more than half.

```css assemble
& {
  --shadow-low: var(--light-dx) calc(var(--light-dy) * 2) 2px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.2) * 100%), transparent),
    calc(var(--light-dx) * 3) calc(var(--light-dy) * 6) 10px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.1) * 100%), transparent);
  --shadow-mid: calc(var(--light-dx) * 2) calc(var(--light-dy) * 4) 4px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.2) * 100%), transparent),
    calc(var(--light-dx) * 8) calc(var(--light-dy) * 16) 30px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.5) * 100%), transparent);
  --shadow-high: calc(var(--light-dx) * 3) calc(var(--light-dy) * 6) 6px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.2) * 100%), transparent),
    calc(var(--light-dx) * 14) calc(var(--light-dy) * 28) 52px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.7) * 100%), transparent);
  --drop-low: drop-shadow(var(--light-dx) calc(var(--light-dy) * 2) 1px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.2) * 100%), transparent))
    drop-shadow(calc(var(--light-dx) * 3) calc(var(--light-dy) * 6) 5px color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.1) * 100%), transparent));
  --edge-lit: inset calc(var(--hx) * 1px) calc(var(--hy) * 1px) 0 light-dark(transparent, color-mix(in oklab, var(--ink) 18%, transparent)); }
```

- Careful: on a light page it is heavy, and on a pale ground it quickly looks like the 2000s. It is meant for dark pages and for panels over a picture, where Fluent also makes its shadows stronger (R3). Large blurs cost the browser more the larger they are and the more of them there are (R12, R13): keep the biggest on a few panels, not on every item in a list. Paper on paper: a dark contact and a short soft pool, as tags look under a stall's lamp.
- Light and dark: on a dark page the panel's lighter surface and its lit edge show it is raised; the shadow sinks the ground round it.
- Personality: dramatic, playful
- Goes with: `light: glow edges` or `lamp`; `materials: metal-and-dark-glass` or `wood-and-canvas`; a dark tone.
- Used on: 4 mockups: two game-style joke sites (panels and slots, `0 6px 14px` at 0.5 black), a small shop with a dark lead and a night market (`drop-shadow(0 6px 8px)` at 0.6 under hanging tags).

### Glow
- Layer: glow
- Owns: light given off by things: a lamp in the picture, a rim of light round frames and controls, a haze round the brightest thing. Not the focus ring, which is the colour part's `--focus` and always a solid outline.
- Default: none

**A glow shows on a dark page and hardly at all on a light one.** Nothing on a screen is brighter than white, so on a pale page light can only show by its warmth and by the shade round it. Each option says what it becomes on a light page: a lamp is the ground turning warm and pale towards it and darker away from it; a rim and a bloom are warm halos, drawn stronger than on a dark page. Designers make light on a pale page with a lighter edge on one side and a darker one on the other, and those pairs are too faint to carry meaning (R17), so on a light page a glow is decoration only.

#### None
- Id: none
- Status: draft
- Looks like: nothing gives off light; the page is lit from outside.
- Made with: nothing.

```css assemble
/* light / glow: none. Nothing gives off light: the rim and bloom keep Base's transparent values. */
```

- Careful: the right choice for most pages. Two briefs named "glowing panels" as what a hand-made page must not look like.
- Light and dark: the same on both.
- Personality: any
- Goes with: every shadows option.
- Used on: most mockups: every one not named under the other options.

#### Lamp
- Id: lamp
- Status: draft
- Looks like: one source of light inside the picture, a lamp, a lantern or a glowing ball, with a pool of light round it and the rest of the page falling into shade the further it is. The light is warm (`--lamp`), and the main button is the brightest thing after it; with an amber accent the two share a colour.
- Made with: three things at the point the direction sets: a small source (a warm-white core in a disc of `--lamp`, with a halo), a `screen` layer with a radial gradient in the lamp's colour (brightening near it), and a `multiply` layer with a warm tint near the lamp and the shade far from it (darkening away). On a light page the warm tint does the work, since screen can only make a pale page a little paler. Light reads by the dark round it (R18), so the shade does as much as the glow.

- Needs markup: none for the pool and the shade; to show the lamp itself where the picture holds it, `<i class="light-lamp" aria-hidden="true"></i>`, positioned by the page.

```css assemble
& { --lamp-lch: 0.84 0.13 78;   /* a lamp is always its own warm light, under any sky */
  --light-lamp-shade: radial-gradient(circle at var(--light-at), light-dark(color-mix(in oklab, var(--lamp) 55%, transparent), transparent) 0,
    light-dark(color-mix(in oklab, var(--lamp) 18%, transparent), transparent) 18%, transparent 30%, color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.3) * 100%), transparent) 85%);
  --light-lamp-glow: light-dark(color-mix(in oklab, var(--lamp) 30%, var(--surface-raised)), var(--lamp));
  --light-lamp-pool: radial-gradient(circle at var(--light-at), var(--light-lamp-glow) 0, color-mix(in oklab, var(--light-lamp-glow) 45%, transparent) 12%,
    color-mix(in oklab, var(--light-lamp-glow) 14%, transparent) 30%, transparent 55%); }
body::before, body::after { content: ""; }
/* the lamp itself, where the picture holds it: <i class="light-lamp" aria-hidden="true"></i>, placed by the page (optional: the pool works without it) */
.light-lamp { display: block; width: 1rem; aspect-ratio: 1; border-radius: 50%; pointer-events: none;
  background: radial-gradient(circle, oklch(var(--light-lamp-core, 0.99 0.03 90)) 0 30%, var(--lamp) 75%);
  box-shadow: 0 0 10px 3px color-mix(in oklab, var(--lamp) 70%, transparent), 0 0 30px 12px color-mix(in oklab, var(--lamp) 35%, transparent); }
```

- Careful: the light is small. A page that glows all over has no light at all; nothing very bright covers more than a small part of it (the sorcery guide measured under 15% in every picture it was made from). Nothing glows behind words meant to be read: they sit on a sheet dimmer than the light (one mockup kept its paper at about two-thirds of the light's brightness). Text in the shaded parts still passes 4.5 to 1: darkness is not a way to make words quieter. If the lamp breathes (two mockups, over seven seconds), animate the `opacity` of the light layer, never its gradient or a blur (R7, R12), keep the change small, stop it under reduced motion, and never flash. Put the lamp layer above the sky layer, so a lamp at night is lit over the night.
- Light and dark: on a dark page a gold pool, the corners near black: the one-light room. On a light page a warm, pale pool round a small glowing source, and a soft shade gathering away from it: a lamp lit in a room by day, gentler than at night. If the brief wants a lamp people notice, the colour part's dark or lamplit tone is the first decision.
- Personality: dramatic, calm
- Goes with: `light: direction top-left`, `top-right` or `low-side` (where the lamp is); `light: shadows soft` or `deep`; `light: focus vignette`; a dark or lamplit tone.
- Used on: 6 mockups: a dark, painterly joke site (a gold orb), two versions of a small shop with a dark lead, the first two versions of a game-style joke site, and a night market (one paper lantern, its amber used only for the lantern and the two main buttons).

#### Edges
- Id: edges
- Status: draft
- Looks like: thin bright rims round frames and controls, a slot glowing in its rarity colour, a verdict word with a soft halo. Neon-like, and very much a game screen.
- Made with: a one-pixel ring in the light's colour (`--lamp`) and a blur in the same colour, added to each frame's and control's own shadow; for a shape that is not its box, the same as two `drop-shadow()`s.

```css assemble
& { --light-rim: 0 0 0 1px var(--lamp),
    0 0 12px 2px light-dark(color-mix(in oklab, var(--lamp) 70%, transparent), color-mix(in oklab, var(--lamp) 55%, transparent));
  --drop-rim: drop-shadow(0 0 0.5px var(--lamp))
    drop-shadow(0 0 6px light-dark(color-mix(in oklab, var(--lamp) 70%, transparent), color-mix(in oklab, var(--lamp) 60%, transparent))); }
```

- Careful: a glow does not count towards contrast or towards a focus indicator: WCAG measures the thing's own edge and colour, and a shadow outside it is not counted (R16). So the rim is decoration, the button's edge is still `--accent-edge`, and the focus ring is still a solid outline in `--focus`, drawn outside the rim. A halo round small text blurs its letters: keep it for large words and rims. A glow that moves (a pulse, a shimmer) is slow, stops under reduced motion, and changes brightness less than three times a second.
- Light and dark: on a dark page a real glow, gold on brown (or ice on steel under a night sky). On a light page the halo is stronger, so the rim reads as warm light round the edge rather than an outline; it is still gentler than on a dark page. Rarity colours (a blue rim for one kind, purple for another) are content: the site sets `--lamp` per item.
- Personality: playful, dramatic
- Goes with: `light: shadows deep`; `frames: riveted-metal`; `materials: metal-and-dark-glass`; a dark tone.
- Used on: 1 mockup: the latest version of a game-style joke site (rarity rims on reward slots, a halo on the verdict row).

#### Bloom
- Id: bloom
- Status: draft
- Looks like: a soft haze round the brightest thing only, the main button or the sun, as a camera sees a bright light. Everything else is lit normally.
- Made with: one wide, soft halo in the light's colour, even all round as light spreads, on the main button alone.

```css assemble
& { --light-bloom: 0 0 30px 4px light-dark(color-mix(in oklab, var(--lamp) 75%, transparent), color-mix(in oklab, var(--lamp) 50%, transparent)); }
```

- Careful: one thing per screen, or it is a glowing page. Like every glow, it does not count towards the button's contrast or its focus ring.
- Light and dark: on a dark page a halo of gold light round the button. On a light page a warm glow round it, stronger so it shows on the pale ground; it reads as light, softly.
- Personality: playful, dramatic, friendly
- Goes with: `light: sky by-the-clock` or `night` (the lit things at night bloom); `light: focus spotlight`.
- Used on: 2 mockups: an observatory (the sun's halo by day, the hut window and track lamps at night) and a joke site (a halo round the message announcing the second look).

### Sky
- Layer: sky
- Owns: the colour of the light over the page: clear day, a low warm dusk, moonlight, or all of them by the clock. It tints the ground and the things on it, and turns shadows the opposite temperature. It never paints the ground (that is the background) and never touches the sheet with the words.
- Default: none

Painters light a scene in two temperatures: a warm light and cool shadows, filled in by the blue sky, or the other way round (R24). Daylight is warmer and softer at sunrise and sunset, when the sun is low and shadows are long (R19); just after sunset the light goes blue (R20). At night the eye loses red first, so night looks blue and reds go dark (R21); films have long shown night with a blue cast for that reason. The options here follow those four states.

Each sky is two layers over the ground: `multiply` with the sky's colour from the top (it colours a light page; on a dark one it barely shows), and `screen` with the sun or moon at the light's point and a faint wash of the sky (it lights a dark page). Light and dark pages need different strengths, chosen with `light-dark()`.

#### None
- Id: none
- Status: draft
- Looks like: white light. The page keeps its own colours.
- Made with: nothing; shadows take the page's own hue.

```css assemble
/* light / sky: none. White light: shadows keep the page's own hue (Base's --shade). */
```

- Careful: none.
- Light and dark: the same on both.
- Personality: any
- Goes with: everything.
- Used on: most mockups.

#### Day
- Id: day
- Status: draft
- Looks like: a clear sky and a warm sun: the top of the page takes a little sky blue, the side the light comes from a warm pale glow, and shadows turn slightly blue.
- Made with: the sky's blue multiplied from the top, the sun screened at the light's point, and the shade mixed with a cool blue.

```css assemble
& { --light-cool: 0.42 0.1 250; --shade: color-mix(in oklab, rgb(var(--shadow-rgb, 60 45 30)) 70%, oklch(var(--light-cool)));
  --light-sky-lamp: 0.86 0.11 85;   /* rims catch sunlight */
  --light-sky-top: 0.8 0.08 235; --light-sun: 0.97 0.07 92; --light-sun-dk: 0.82 0.12 82;
  --light-sky-mul: linear-gradient(light-dark(oklch(var(--light-sky-top) / 0.5), oklch(var(--light-sky-top) / 0.6)), transparent 60%);
  --light-sky-scr: radial-gradient(circle at var(--light-at), light-dark(oklch(var(--light-sun) / 0.85), oklch(var(--light-sun-dk) / 0.4)), transparent 55%),
    linear-gradient(light-dark(transparent, oklch(var(--light-sky-top) / 0.16)), transparent 60%); }
body::before, body::after { content: ""; }
```

- Careful: this is the colour of daylight on whatever the page is made of. The old daylight option painted a blue sky behind the page; that is now the background part's painted ground or one long scene, lit by this. With a material ground (paper, felt), the material stays and the light falls on it: the field notebook kept its paper, put the real sky in one taped-in sketch, and carried daylight as a warm wash from the top right and every shadow falling down and left. Words on a painted sky still go on a panel: white on a mid-blue sky is about 2.5 to 1.
- Light and dark: on a light page a cool top, a warm sunny corner and bluish shadows: the clearest of the four. On a dark page a faint warm haze from the light's side, like sun through a dark room's window; the page stays dark.
- Personality: friendly, playful
- Goes with: `light: direction top-right` or `top-left`; `light: shadows crisp` (a high sun) or `paper-lift`; `background: scene painted-ground`.
- Used on: 3 mockups: a game-style joke site (a summer day on a road to a castle), the 3D game's pages above ground, and a field notebook (the sun-wash only).

#### Dusk
- Id: dusk
- Status: draft
- Looks like: a low, warm light from one side and violet overhead: peach near the light, lilac above, shadows turning violet. Golden hour: warm, soft, long shadows (R19).
- Made with: a violet-to-peach gradient multiplied over the ground, an orange sun screened at the light's point, and a violet shade.

```css assemble
& { --light-cool: 0.35 0.12 300; --shade: color-mix(in oklab, rgb(var(--shadow-rgb, 60 45 30)) 65%, oklch(var(--light-cool)));
  --light-sky-lamp: 0.8 0.14 55;   /* amber */
  --light-dusk-high: 0.68 0.11 305; --light-dusk-low: 0.84 0.12 55; --light-dusk-sun: 0.8 0.16 48;
  --light-sky-mul: linear-gradient(light-dark(oklch(var(--light-dusk-high) / 0.55), oklch(var(--light-dusk-high) / 0.7)), light-dark(oklch(var(--light-dusk-low) / 0.6), oklch(var(--light-dusk-low) / 0.7)));
  --light-sky-scr: radial-gradient(circle at var(--light-at), light-dark(oklch(var(--light-dusk-sun) / 0.6), oklch(var(--light-dusk-sun) / 0.35)), transparent 50%),
    linear-gradient(light-dark(transparent, oklch(var(--light-dusk-high) / 0.14)), light-dark(transparent, oklch(var(--light-dusk-low) / 0.2))); }
body::before, body::after { content: ""; }
```

- Careful: the strongest tint of the four on a light page: the ground goes pink and peach, and so do the cards on it. Words on the ground must be measured under it; words on sheets are untouched. The accent's colour on the ground shifts too: a green accent laid straight on the ground looks brown at dusk. Pair it with `direction: low-side` for long shadows.
- Light and dark: on a light page a sunset over paper. On a dark page a warm orange glow from the light's side and a faint violet over the rest.
- Personality: calm, dramatic
- Goes with: `light: direction low-side`; `light: glow lamp` (lamps coming on); `light: shadows soft`.
- Used on: none as a whole look; it is the clock's sunrise and sunset on 2 mockups (an observatory, a 3D game).

#### Night
- Id: night
- Status: draft
- Looks like: moonlight. The scene goes blue and dim, a pale cool pool where the moon is, shadows deep blue; the sheets with the words stay as they are, like a chart read by torchlight.
- Made with: a deep blue multiplied over everything, a cool moon screened at the light's point, a faint blue screened over a dark page, and a navy shade.

```css assemble
& { --light-cool: 0.2 0.08 265; --shade: color-mix(in oklab, rgb(var(--shadow-rgb, 60 45 30)) 55%, oklch(var(--light-cool)));
  --light-sky-lamp: 0.8 0.08 235;   /* moonlight */
  --light-night-high: 0.42 0.1 262; --light-night-low: 0.6 0.08 250; --light-moon: 0.92 0.04 230;
  --light-sky-mul: linear-gradient(light-dark(oklch(var(--light-night-high) / 0.6), oklch(var(--light-night-high) / 0.8)), light-dark(oklch(var(--light-night-low) / 0.45), oklch(var(--light-night-low) / 0.7)));
  --light-sky-scr: radial-gradient(circle at var(--light-at), light-dark(oklch(var(--light-moon) / 0.5), oklch(var(--light-moon) / 0.22)), transparent 35%),
    linear-gradient(light-dark(transparent, oklch(var(--light-night-low) / 0.16)), transparent); }
body::before, body::after { content: ""; }
```

- Careful: on a light page the ground goes a mid blue-grey, so dark words straight on the ground lose contrast: measure them, or keep words on sheets. Colours on the ground go dull and close in brightness at night (reds first, R21): a meaning carried by colour needs a word beside it. The sheets staying bright at night is a choice the observatory made and accepted ("at night the sheets are the brightest thing on the page"); if the brief wants the page itself dark at night, that is the colour part's tone changing with the clock, not this layer (see by the clock).
- Light and dark: on a light page moonlit paper, blue-grey. On a dark page near-black blue with a cool pool where the moon is; cards on the ground almost disappear, as things do at night.
- Personality: calm, dramatic
- Goes with: `light: focus vignette`; `light: glow lamp` (a lantern at night, drawn over the night); `light: glow bloom`.
- Used on: 3 mockups: the second look of a game-style joke site (a moonlit lake), the night hours of a 3D game, and a night market (a dark car park under one lantern).

#### By the clock
- Id: by-the-clock
- Status: draft
- Looks like: the light follows a clock: day, a warm glow at sunrise and sunset, then night with the moon. The page looks different at different times, which makes it feel like a place that goes on when nobody is looking.
- Made with: a script works out from the hour how far the sun is up, and sets two numbers on the page root: `--light-day` (0 at night, 1 by day) and `--light-dusk` (1 at sunrise and sunset). The CSS mixes the day and night colours by `--light-day` and lays the dusk glow over them by `--light-dusk`. The script is not lifted by `style css` (it lifts only CSS and SVG): copy it into the page's own script. A small copy of the sky at its own hour (the swatch book's chips) needs its colours set on its own layers, since a custom property that uses `var()` is worked out where it is written and children only inherit the result; the swatch book shows how.

- Needs markup: none: the script comes in `parts.js` and sets the hour on the page root. To set the clock by hand add `<input id="clock" type="time">` (or open the page with `?t=21:40`); a place's own sunset is `data-lat` and `data-lon` on `<body>`; a copy at a fixed hour is any element with `data-t="21:40"`.

```css assemble
/* the script below sets --light-day (0 at night, 1 by day) and --light-dusk (1 at sunrise and sunset) on the page root */
& { --light-day: 1; --light-dusk: 0; --light-cool-day: 0.42 0.1 250; --light-cool-night: 0.2 0.08 265;
  --shade: color-mix(in oklab, rgb(var(--shadow-rgb, 60 45 30)) 62%, color-mix(in oklab, oklch(var(--light-cool-day)) calc(var(--light-day) * 100%), oklch(var(--light-cool-night))));
  --light-sky-top: 0.8 0.08 235; --light-sun: 0.97 0.07 92; --light-sun-dk: 0.82 0.12 82;
  --light-night-high: 0.42 0.1 262; --light-night-low: 0.6 0.08 250; --light-dusk-low: 0.84 0.12 55; --light-moon: 0.92 0.04 230;
  --light-sky-mul: linear-gradient(transparent 25%, light-dark(oklch(var(--light-dusk-low) / calc(var(--light-dusk) * 0.65)), oklch(var(--light-dusk-low) / calc(var(--light-dusk) * 0.7)))),
    linear-gradient(color-mix(in oklab, light-dark(oklch(var(--light-sky-top) / 0.5), oklch(var(--light-sky-top) / 0.6)) calc(var(--light-day) * 100%), light-dark(oklch(var(--light-night-high) / 0.6), oklch(var(--light-night-high) / 0.8))),
      color-mix(in oklab, transparent calc(var(--light-day) * 100%), light-dark(oklch(var(--light-night-low) / 0.45), oklch(var(--light-night-low) / 0.7))));
  --light-sky-scr: radial-gradient(circle at var(--light-at), color-mix(in oklab, light-dark(oklch(var(--light-sun) / 0.85), oklch(var(--light-sun-dk) / 0.4)) calc(var(--light-day) * 100%),
      light-dark(oklch(var(--light-moon) / 0.5), oklch(var(--light-moon) / 0.22))), transparent 50%),
    linear-gradient(transparent 25%, light-dark(transparent, oklch(var(--light-dusk-low) / calc(var(--light-dusk) * 0.22)))),
    linear-gradient(color-mix(in oklab, light-dark(transparent, oklch(var(--light-sky-top) / 0.16)) calc(var(--light-day) * 100%), light-dark(transparent, oklch(var(--light-night-low) / 0.16))), transparent 70%); }
body::before, body::after { content: ""; }
```

```js assemble
// Rough sunrise and sunset from the date and a place: good to about half an hour, enough for the colour of the light.
// The place comes from data-lat and data-lon on <body>; with no longitude, noon is read from the time zone.
function sunTimes(date, lat, lon) {
  const n = Math.round((date - new Date(date.getFullYear(), 0, 0)) / 864e5);
  const decl = 23.44 * Math.sin(2 * Math.PI * (284 + n) / 365) * Math.PI / 180;
  const half = Math.acos(Math.max(-1, Math.min(1, -Math.tan(lat * Math.PI / 180) * Math.tan(decl)))) * 12 / Math.PI;
  const jan = new Date(date.getFullYear(), 0, 1).getTimezoneOffset(), jul = new Date(date.getFullYear(), 6, 1).getTimezoneOffset();
  const solarNoon = lon == null ? 12.3 + (date.getTimezoneOffset() < Math.max(jan, jul) ? 1 : 0) : 12 - date.getTimezoneOffset() / 60 - lon / 15;
  return { rise: solarNoon - half, set: solarNoon + half };
}
// The light at an hour: day 0..1, dusk 0..1 (peaks as the sun crosses the horizon, and stays a while after: the blue hour)
function lightAt(hour, rise, set) {
  const clamp = (v) => Math.max(0, Math.min(1, v));
  let h;                                                   // 1 at noon, 0 at sunrise and sunset, -1 deep in the night
  if (hour >= rise && hour <= set) h = Math.cos(((hour - (rise + set) / 2) / ((set - rise) / 2)) * Math.PI / 2);
  else {
    const away = Math.min((rise - hour + 24) % 24, (hour - set + 24) % 24), nightHalf = (24 - (set - rise)) / 2;
    h = -Math.sin(Math.min(1, away / nightHalf) * Math.PI / 2);
  }
  return { day: clamp((h + 0.12) / 0.34), dusk: clamp(1 - Math.abs(h - 0.02) / 0.24) };
}
// The clock can be set, for pictures and for checks: ?t=21:40 in the address, a time field (#clock), or data-t="21:40"
const hourOf = (text) => { const m = /^(\d{1,2}):(\d{2})$/.exec(text || ''); return m ? +m[1] + m[2] / 60 : null; };
function paintSky() {
  const now = new Date(), asked = hourOf(document.getElementById('clock')?.value) ?? hourOf(new URLSearchParams(location.search).get('t'));
  const lat = +(document.body.dataset.lat || 45), lon = document.body.dataset.lon == null ? null : +document.body.dataset.lon;
  const { rise, set } = sunTimes(now, lat, lon);
  for (const el of [document.documentElement, ...document.querySelectorAll('[data-t]')]) {   // the page, and any copy at its own hour
    const { day, dusk } = lightAt(hourOf(el.dataset.t) ?? asked ?? now.getHours() + now.getMinutes() / 60, rise, set);
    el.style.setProperty('--light-day', day.toFixed(3));
    el.style.setProperty('--light-dusk', dusk.toFixed(3));
  }
}
document.getElementById('clock')?.addEventListener('input', paintSky);
paintSky();
setInterval(paintSky, 60000);   // once a minute, with no transition: a change too small to see is not motion
```

- Careful:
  - **Sunrise and sunset move with the date and the place.** The first version had them fixed at six and six; the code above works them out (roughly) from the date and a latitude, and from a longitude when the page knows it. Say in the blueprint whose clock it is: the visitor's, the place's (a society in one town wants its own sunset, and sets `data-lat`, `data-lon` and the place's time zone), or a game's (on the 3D game, one day every 24 real minutes).
  - **Set the clock for pictures and checks.** A page that follows the clock must also be settable, or nobody can photograph its night at noon. Build `?t=21:40` in the address: `try "page.html?t=21:40" --shot night.png` opens the page at that hour, and it is the link to send someone. A small time field on the page is worth adding for visitors who want to look at another hour (`fill #clock=21:40` sets it as a step), and `data-t` sets a copy at a fixed hour. List noon, dusk and night in `project.check_states` so `check` sees the worst hour.
  - **Reduced motion.** The sky is repainted once a minute with no transition, and each repaint changes it by under a hundredth: that is not motion, so it continues under reduced motion. What stops under reduced motion is anything that moves within a minute: twinkling stars, drifting clouds, a sun that slides (R11). Never animate the change between two repaints.
  - **Contrast changes with the hour**, so it must pass at the worst one. Keep words on sheets, which the sky never touches; then only words straight on the ground, and anything pressable laid on it, are measured at each hour.
  - **A page that turns dark at night** is the colour part's tone changing, not this layer: the clock script sets the tone class (`tone-light` by day, `tone-dark` from the end of dusk) as well as `--light-day`, and every name follows. Say so in the site guide; both tones are then checked.
- Light and dark: the light page goes from a cool clear day through a peach dusk to moonlit blue paper; the dark page stays dark and takes a warm haze by day, an orange glow at dusk and a cool blue at night.
- Personality: calm, playful
- Goes with: `light: direction overhead`; `light: shadows soft` or `paper-lift`; `light: glow bloom` (lamps that bloom at night); `background: scene one-long-scene` (an observatory's sky, hill and track).
- Used on: 2 mockups: an observatory (the visitor's own sky, with a time field and `?t=`), a 3D game (the game's own clock).

### Focus
- Layer: focus
- Owns: where the light leads the eye: a pool on the main thing, or the corners falling into shade. Not keyboard focus: the focus ring is the colour part's `--focus`, and it is drawn whatever is picked here.
- Default: none

#### None
- Id: none
- Status: draft
- Looks like: the light is even across the page.
- Made with: nothing.

```css assemble
/* light / focus: none. The light is even across the page. */
```

- Careful: most pages. The main thing is found by its size, place and colour, not by light.
- Light and dark: the same on both.
- Personality: any
- Goes with: everything.
- Used on: most mockups.

#### Spotlight
- Id: spotlight
- Status: draft
- Looks like: a pool of light on the one thing that matters, the main action or the product, with the rest a step darker. It answers the visitor: it grows when they reach for the main button with the pointer or the keyboard.
- Made with: two layers round the main thing, on the `::before` and `::after` of its wrapper, which the page marks `.light-main` (the wrapper has no `z-index` of its own, so the layers blend with the ground under it): a pool of light screened behind it, and a circle of shade multiplied round it, fixed in size so the shade past it stays even and shows no edge. `:has()` brightens the pool when the main button is pointed at or focused (R15).

- Needs markup: `class="light-main"` on the wrapper of the one main thing (the main button and what it is about), a direct child of its `.band`, with no `z-index` of its own.

```css assemble
/* the main thing's wrapper carries .light-main, as a child of its band; it is not a stacking context, so the two layers blend with the band under it */
.light-main { position: relative; z-index: auto; }
.band:has(> .light-main) { overflow: clip; }   /* or the shade spreads over the whole page; this band takes no shaped edge from frames, which the clip would cut */
.light-main::before, .light-main::after { content: ""; position: absolute; z-index: 1; pointer-events: none; }
.light-main > * { position: relative; z-index: 2; }   /* the main thing above its own pool */
.light-main::before { inset: -30% -25%; mix-blend-mode: screen; opacity: 0.75;
  transition: opacity var(--dur-medium, 0.5s) var(--ease-out, ease), scale var(--dur-medium, 0.5s) var(--ease-out, ease);
  background: radial-gradient(closest-side, light-dark(color-mix(in oklab, var(--lamp) 25%, var(--surface-raised)), color-mix(in oklab, var(--lamp) 45%, var(--surface-raised))), transparent); }
.light-main::after { inset: -100vmax; mix-blend-mode: multiply;   /* one fixed circle; past it the shade stays even, so no edge */
  background: radial-gradient(circle 26rem at 50% 50%, transparent 30%, color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 1.4) * 100%), transparent)); }
.light-main:has(.btn:hover, .btn:focus-visible)::before { opacity: 1; scale: 1.12; }
@media (prefers-reduced-motion: reduce) { .light-main::before { transition: none; } }
@media (prefers-contrast: more) { .light-main::after { opacity: 0.35; } }
```

- Careful: it reacts to keyboard focus as well as the pointer, and it is never the only sign of focus: the ring is still drawn. The darker parts round it still pass the contrast minimum for anything on the ground, and things under the shade stay usable (R15). It animates `opacity` and `scale` only, never the gradient or a blur, which is cheap (R7). One per screen: two spotlights is no spotlight. The wrapper must clip it (`overflow: clip` on the section), or the shade spreads over the whole page; the clip also cuts the frames part's shaped edge at the top of that section, so put the spotlight in the first section or give its section a straight edge. Keep `.light-main` a direct child of its band: a wrapper round it with a `z-index` (every child of a band has one) would keep its blend inside.
- Light and dark: on a light page a paler pool and a soft brown shade round it, like a lamp over a desk. On a dark page a warm glow behind the main thing and the rest near black: a stage.
- Personality: dramatic, playful
- Goes with: `light: glow lamp` or `bloom`; a product shown alone (the sales guide).
- Used on: 2 mockups, in part: a dark, painterly joke site (its light grows when the main button is pointed at) and a 3D game (a small light travels with the player's own piece, at night and underground).

#### Vignette
- Id: vignette
- Status: draft
- Looks like: the corners fall into shade, so the eye stays in the middle. An old photograph, a painting lit by one candle.
- Made with: one radial gradient multiplied over the ground, transparent in the middle and darkest past the edges, so the dark is pushed outside the box and reads as light falling off, not a frame (R14). An inset `box-shadow` leaves "an awkwardly visible square" (R14), so it is a gradient.

```css assemble
& { --light-vignette: radial-gradient(ellipse 80% 75% at 50% 45%, transparent 50%, color-mix(in oklab, var(--shade) calc(min(1, var(--shadow-strength) * 2) * 100%), transparent) 110%); }
body::before { content: ""; }
```

- Careful: on a long page, put it on each band or on the first screen, not on the whole page: a vignette 5,000 pixels tall only darkens the sides. Words on the ground near the edges are measured at the dark end. Not under a form.
- Light and dark: on a light page the corners take a soft brown shade, like old paper. On a dark page the corners go near black; subtle, but it deepens the room.
- Personality: dramatic, calm
- Goes with: `light: sky night`; `light: glow lamp`; `light: direction low-side`.
- Used on: 2 mockups: a night market (the band darkening away from the lantern, with grain), and a joke site in an inked style (a darkened edge on its parchment).

## What the visitor's settings switch off

Every option keeps these; the code is in "Base", and the swatch book has them too. With more contrast asked for, the two layers of light are turned down to about a third and the rims and blooms are off, so the words and edges carry everything (R10). With forced colours on, the browser removes every shadow and every gradient (R9), and the layers are hidden: a raised sheet with no border then becomes invisible, so the frames part gives it an edge there (`border: 1px solid CanvasText`; the swatch book draws it). Under reduced motion nothing in this part moves except the clock's once-a-minute repaint.

## Starting points

### Flat and even
- Id: flat-and-even
- Picks: direction: none; shadows: none; glow: none; sky: none; focus: none
- Personality: serious, calm
- Looks like: no light at all: a page, not a picture. Sheets are told from the ground by colour and line. **About pale grounds:** the first version warned against pairing this with a pale ground (the template's "pale ground, white boxes, one accent"), while other guides recommended exactly that pair. Both were partly right: flat light on a pale ground is the template look only when nothing else on the page was designed. On a toned ground (the colour part's toned tone, such as the quiet gallery's bisque), or under a designed signature piece (the professional guide's), it is calm, not plain. With a pale ground, the page needs the signature and a designed repeated item; with neither, pick another light or a toned ground.
- Used on: a quiet gallery of pots (flat drawings, no shadows, a toned ground) and a tutoring site (no raised things at all).

### Professional
- Id: professional
- Picks: direction: overhead; shadows: soft
- Personality: serious, calm
- Looks like: even, soft light from above. Only things that float (menus, a dialog, one panel holding a form) have a shadow you notice; the rest lie flat. Even and exact.
- Used on: the professional guide (one institutional look, no decoration) and the general guide's starting tokens, whose one `--shadow` is this option from straight above.

### Warm
- Id: warm
- Picks: direction: top-left; shadows: paper-lift
- Personality: friendly, calm
- Looks like: a kitchen table by a window. Every paper thing has a thin dark contact line and a soft lift falling down and to the right, so cut paper, notes and tags look laid by hand.
- Used on: the warm guide (cut paper, notes, bunting); a soap shop and a volunteer page used the same two shadows, from straight above.

### Daylight
- Id: daylight
- Picks: direction: top-right; shadows: crisp; sky: day
- Personality: playful, friendly
- Looks like: bright open air: a cool sky at the top, a warm sun in the corner, hard little shadows from a high sun. Behind a painted ground it is a summer's day; over paper, a sunny morning.
- Used on: a game-style joke site (a summer day on a road to a castle) and the 3D game's pages above ground.

### Moonlight
- Id: moonlight
- Picks: direction: top-left; shadows: soft; sky: night; focus: vignette
- Personality: calm, dramatic
- Looks like: night, cool and quiet: the scene goes blue and dim, a pale moon in the corner, the edges lost; the sheets stay readable like a chart under a torch.
- Used on: the second look of a game-style joke site (a moonlit lake) and the night hours of a 3D game.

### Sky by the clock
- Id: sky-by-the-clock
- Picks: direction: overhead; shadows: soft; sky: by-the-clock
- Personality: calm, playful
- Looks like: the page keeps time with the visitor's day: clear and cool by day, peach at sunrise and sunset, blue at night.
- Used on: a 3D game in the browser (its own clock).

### Almanac plate
- Id: almanac-plate
- Picks: direction: overhead; shadows: paper-lift; sky: by-the-clock; glow: bloom
- Personality: calm, serious
- Looks like: printed charts laid under the visitor's own sky: paper sheets with a fine contact shadow, the sky's light changing round them, and one thing that blooms (the sun by day, a lamp at night).
- Used on: an observatory mockup (sheets of fine paper that stay light at every hour, a time field and `?t=` to set the clock).

### One light
- Id: one-light
- Picks: direction: top-left; shadows: soft; glow: lamp
- Personality: dramatic
- Looks like: a room with one lamp in it. Near the lamp things are lit in its colour, further away they fall into shade; the main button takes the lamp's colour. With the colour part's dark or lamplit tone, a dark room; with a light tone, a lit corner on a pale page.
- Used on: a dark, painterly joke site; two versions of a small shop with a dark lead; the first two versions of a game-style joke site.

### Spotlight on the main thing
- Id: spotlight-on-the-main-thing
- Picks: shadows: soft; focus: spotlight
- Personality: dramatic, playful
- Looks like: a pool of light on the one thing that matters, a step of shade round it, and the pool growing when the visitor reaches for the main button.
- Used on: a dark, painterly joke site (in part) and a 3D game (in part).

### Glow on edges
- Id: glow-on-edges
- Picks: shadows: deep; glow: edges
- Personality: playful, dramatic
- Looks like: panels with heavy shadows and bright rims on frames and controls, like a game screen. On a light page the rims are thin coloured rings.
- Used on: the latest version of a game-style joke site.

### Sorcery
- Id: sorcery
- Picks: direction: low-side; shadows: deep; glow: lamp; focus: vignette
- Personality: dramatic
- Looks like: a low lamp at one side of a dark room, its light falling across the page; long, heavy shadows; the corners lost in dark. Pick it with the colour part's sorcery start (a lamplit night-blue room).
- Used on: the sorcery guide (one light inside the picture in 5 of its 6 pictures, lit from low and to one side); a dark, painterly joke site.

### Gilded dark
- Id: gilded-dark
- Picks: direction: overhead; shadows: deep; glow: edges; sky: day
- Personality: dramatic, playful
- Looks like: heavy panels rimmed in gold, standing over a bright painted world in daylight.
- Used on: the game-interface guide; a game-style joke site in both its looks.

### Lantern fair
- Id: lantern-fair
- Picks: direction: top-right; shadows: paper-lift; glow: lamp; sky: night
- Personality: dramatic, friendly
- Looks like: one paper lantern hanging top right over a market at night: a warm pool round it, paper tags with fine shadows falling down and left, the rest blue night.
- Used on: a night-market mockup (one lantern, its amber kept for the lantern and the two main buttons); two versions of a small shop with a dark lead.

### Field journal
- Id: field-journal
- Picks: direction: top-right; shadows: paper-lift; sky: day
- Personality: calm, friendly
- Looks like: taped-in pages in morning sun: a faint warm wash from the top right, a little sky at the top, and every page's contact shadow falling down and to the left.
- Used on: a field-notebook mockup (`--sun-wash` from the top right, `drop-shadow(-2px 3px 0)` and a soft one on each taped sheet).

### Repair cafe
- Id: repair-cafe
- Picks: direction: top-left; shadows: crisp
- Personality: playful, friendly
- Looks like: cut card and pegboard under flat bright light: every card, notice and button has a hard little shadow down and to the right, no blur.
- Used on: a repair-café mockup (`1px 2px 0` and `2px 3px 0` on cards, notices and buttons).

## Swatch book

`tests/parts/light.html` shows every option of every layer, then every starting point, each on a light page and on a dark one side by side; open it in a browser to choose by eye. Every swatch has the same things in it, so the light is the only thing that changes: a raised sheet with a heading and a button, a stack of three cards (the top one torn and taped, to show paper on paper), a ball whose bright side shows where the light comes from, and the light's own layers. The direction swatches mark where the light is with a small sun. The by-the-clock swatches show four hours on small chips (dawn, noon, dusk and night, worked out for today) and `?t=21:40` or the field at the top sets the clock for the large ones (`try "library/tests/parts/light.html?t=21:40" --shot night.png`). It writes the layer classes short (`di-top-left` for `light-direction-top-left`, and `sh-`, `gl-`, `sk-`, `fo-` for the others). It is built by `tests/parts/source/light.py` from `light-template.html` beside it; run `python3 light.py ../light.html` there to rebuild it.

## Not covered yet

- **Shadows that swing with the clock.** The sun moves from east to west, so morning shadows could fall one way and evening ones the other. Easy to add (the clock script sets `--lx` too), but no site has wanted it, and direction would then have two owners.
- **Photographs.** Every lit page so far was drawn in code. A real photograph has its own light; on a page with one, the direction should be the photograph's, and the sky layer should not tint it.
- **A light that moves as the visitor scrolls** (the sun setting as they read down). Not tried.
- **The brightest moment of a light that moves.** `check` and `audit` measure one moment; a lamp that breathes, or text near a glow, is measured at whatever moment the picture was taken.
- **A light source that is the page's own interface** (a screen glowing in a dark room, light through a window frame). Named as ideas in briefs, not drawn.
- **A real page.** The swatches are small. The first site made from these layers should be one of the existing mockups rebuilt from its starting point (the field notebook or the night market) and put beside the original.

## Sources

Read on 2026-10-07. Six kinds of source: design-system documents (R1 to R4), craft writing by people who make interfaces (R5, R6, R14, R15, R17), the web platform's own references (R8 to R11, R16), speed (R7, R12, R13), light in painting and in nature (R18 to R24), and accessibility on light and dark pages (R1, R9, R10, R16, R17). The mockups made with the skill are the seventh: their CSS and their site guides are quoted in each option's "Used on". Pages that would not open: Material's dark-theme page (m2.material.io and the archive; its numbers, "1dp 5% ... 24dp 16% white overlay", are from a search result, not the page), a painter's warm-and-cool article (R24, behind a paywall; the rule is the one painters' guides repeat everywhere), and two painting lessons that showed only their outlines.

- R1 Material Design 2, dark theme (elevation shown by a lighter overlay, 5% at 1dp to 16% at 24dp; read from a search result): m2.material.io/design/color/dark-theme
- R2 Atlassian Design System, elevation (paired surface and shadow tokens; in dark mode surfaces "distantly lit from the front", lighter the higher): atlassian.design/foundations/elevation
- R3 Microsoft Fluent 2, elevation (every shadow a sharp key and a soft ambient; stronger in dark mode): fluent2.microsoft.design/elevation
- R4 Microsoft, layering and elevation in Windows (an elevation per surface, a one-pixel stroke on every one, "use shadows to show depth, not as decoration"): learn.microsoft.com/en-us/windows/apps/design/signature-experiences/layering
- R5 Josh Comeau, designing beautiful shadows in CSS ("Every shadow on the page should share the same ratio"; "The vertical offset is always 2x the horizontal one"; offset and blur grow and opacity falls with height; "By matching the hue and lowering the saturation/lightness, we can create an authentic shadow"): joshwcomeau.com/css/designing-shadows/
- R6 Tobias Ahlin, smoother and sharper shadows with layered box-shadows (offsets doubling, blur equal to offset): tobiasahlin.com/blog/layered-smooth-box-shadows/
- R7 Tobias Ahlin, how to animate box-shadow (animate the opacity of a pseudo-element, not the shadow): tobiasahlin.com/blog/how-to-animate-box-shadow/
- R8 MDN, mix-blend-mode (multiply darkens, screen lightens; `isolation: isolate` keeps blending inside a group): developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode
- R9 MDN, forced-colors (`box-shadow` and `text-shadow` forced to none, and background images that are not a url): developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors
- R10 MDN, prefers-contrast: developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-contrast
- R11 web.dev, prefers-reduced-motion (reduce means removing decorative motion; animate only inside no-preference): web.dev/articles/prefers-reduced-motion
- R12 Chrome for Developers, animating a blur (cost grows with radius and area; cross-fade pre-blurred copies with opacity): developer.chrome.com/blog/animated-blur/
- R13 WebKit bug 240865, slow pages with large blur filters: bugs.webkit.org/show_bug.cgi?id=240865
- R14 Una Kravets, vignettes in CSS (`radial-gradient(transparent 50%, black)`; an inset box-shadow leaves "an awkwardly visible square"): una.im/vignettes/
- R15 Frontend Masters, a CSS spotlight effect (a radial gradient on a layer that ignores the pointer; keep what is under it readable and usable): frontendmasters.com/blog/css-spotlight-effect/
- R16 WCAG 2.2, focus appearance (a shadow or glow outside the component does not count towards the indicator): w3.org/WAI/WCAG22/Understanding/focus-appearance.html
- R17 Accessible neumorphism (light and dark shadow pairs on a pale page are too faint to carry meaning): medium.com/@xurxe/accessible-neumorphism-soft-ui-992286900bfa
- R18 Wikipedia, chiaroscuro ("strong contrasts between light and dark"; single candle-lit scenes by Georges de La Tour and Joseph Wright of Derby): en.wikipedia.org/wiki/Chiaroscuro
- R19 Wikipedia, golden hour ("Daylight is redder and softer than when the sun is higher in the sky"; longer shadows; "shadows are less dark"): en.wikipedia.org/wiki/Golden_hour_(photography)
- R20 Wikipedia, blue hour (just after sunset and before sunrise, the remaining light "takes on a mostly blue shade"): en.wikipedia.org/wiki/Blue_hour
- R21 Wikipedia, Purkinje effect ("reds will appear darker relative to other colors as light levels decrease"): en.wikipedia.org/wiki/Purkinje_effect
- R22 Wikipedia, colour temperature (candle about 1,800 K, tungsten 2,700 to 3,000 K, midday sun 5,500 to 6,000 K, blue sky 10,000 K and over): en.wikipedia.org/wiki/Color_temperature
- R23 Clip Studio tips, how to apply light in illustration (key light, rim light, warm light and cool shadow; read from a search result): tips.clip-studio.com/en-us/articles/6429
- R24 James Gurney, the warm and cool approach (warm light, cool shadows filled by the sky; paywalled, rule from its summary): jamesgurney.substack.com/p/the-warm-and-cool-approach
