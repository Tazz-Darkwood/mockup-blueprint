---
name: Materials (a part guide)
summary: What the surfaces that hold words seem made of, in layers that switch on their own - the sheet (paper, card, kraft, parchment, canvas, glass, metal), its grain, how it is fixed on (tape, pins, clips, rivets, string from a rail), its wear, and how the ink sits on it. Every texture is a mask coloured by the shared colour names, so each layer works on a light page, a dark one and a lamplit one, and can be picked with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: research online (six kinds of source, listed under Sources), the materials of 12 mockups made with the skill, the problems five of them met with this part's first version, and the feel guides named in each starting point
---

# Materials

A part guide. It covers what the surfaces with words on them seem made of: the sheet, its fine texture, how it is laid on, how old it is, and how the ink sits on it. It is made of five layers, each one decision that switches on its own: **sheet**, **grain**, **fixing**, **wear** and **ink**. A site picks a starting point whole, or a starting point with one layer changed, in its own guide and in the blueprint as `project.style.parts`: `{"materials": "paper-and-tape"}`, or `{"materials": {"start": "fine-paper", "fixing": "clips"}}`. The pick wins over the feel guide for the material only. The general guide's accessibility minimums (contrast, text size, tap size) still hold whatever is picked.

**This part owns what surfaces seem made of: their texture and how they are laid on** (the owners table in the general guide). It does not own:

- **the sheet's colour.** That is `--surface`, from the colour part. A material only leans it towards a shared name: paper and cloth towards `--line`, kraft and card towards `--earth`, metal towards `--metal` (below). No material writes a colour of its own.
- **borders and edges.** That is frames. No sheet here has a border: fine paper under `frames: none` has none, and the torn edge of torn paper is frames' shape with this part's paper inside it. The first version's fine paper said it went with no frames and then gave every sheet a border; that cannot happen now.
- **shadows.** That is light. A sheet takes `box-shadow: var(--shadow-low)`; a sheet whose fixing sticks out past it (tape) takes `filter: var(--drop-low)` instead, so the tape casts with the paper. Never both. The first version's paper and tape, and torn paper, gave opposite shadows for the same sheet; both now take light's.
- **what lies behind the sections.** That is background. A felt board, a stone wall or a pegboard is the ground; the notices pinned to it are this part.

**Words never sit on texture at full strength.** Text on a material must reach 4.5 to 1 against the worst of what lies under it, not the average (WCAG's failure F83 is exactly "a background image that does not give the text enough contrast", R20). `check` and `audit` measure it from a picture of the page. Every texture here stays under 0.1 of the ink's strength behind words on a light page (research put grain that reads as paper at 0.03 to 0.12 and "dirt" above 0.15, R6), stains and wear stay at the edges and corners, and only headings and short labels take a rough ink: reading text is always printed.

**Material is a cue, not decoration.** Flat pages lose the signs of what can be touched (an eye-tracking study found weak cues cost 22% more time and 25% more looks, R1), and the "flat 2.0" answer is a little depth and texture, used to say what a thing is (R2). So a material goes on the things that are things (a notice, a tag, a ticket, a pane), one material per page, and the button on it stays a button.

## How it is built

Every sheet that shows its material has one empty element inside it, behind the words, that holds the whole material: `.materials-mat` (the swatch book calls it `.mat`). The paper is that element, so it can turn (pinned up crooked) while the words stay level and sharp, as the warm guide learned. Its `::before` is the sheet's body and wear (slow and large: the cloud in fine paper, stains, sheen, dirt), always darker, in the shadow colour; its `::after` is the grain (fine), in `--ink`, so it is dark on a pale sheet and light on a dark one. Fixings (tape, pins, a clip, the rail) are a second empty element, `.materials-fix` (`.fix` in the swatch book), laid over the sheet's top. Both are `aria-hidden`.

```html
<article class="sheet">
  <span class="materials-mat" aria-hidden="true"></span>
  <span class="materials-fix" aria-hidden="true"><!-- tape, pins, a clip or a rail: see Fixing --></span>
  <h3>…</h3><p>…</p><button class="btn">…</button>
</article>
```

The code that draws it is under Base, below; each option sets a few of its custom properties (all beginning `--materials-`).

Each option sets values that do not depend on colour on the page root, and the colours it makes from the shared names on `.sheet`, so a band whose colours differ gets its own. Three things the swatch book taught:

- **Every mask list starts with a transparent layer.** A mask whose every layer is `none` is no mask at all, and the whole `::before` would paint as a flat dark sheet over the paper. The first transparent gradient keeps "nothing picked" meaning nothing.
- **Tiles are masks, drawn once.** A tile written as an SVG data URI cannot read CSS custom properties, so every tile here is black shapes whose only job is their alpha, coloured in CSS by a shared name (as the background part found). Noise drawn by `feTurbulence` inside a data-URI tile is drawn once into an image and repeated; a live SVG filter on page content is redrawn on every repaint and is slow (R17). The tiles are made by `tests/parts/source/materials.py`; each option that uses one carries it in its assembly block as `--materials-tile-<name>`, copied from `tests/parts/materials.html`, where each is a custom property near the top of the style.
- **What each sheet leans to.** Paper, parchment and canvas lean towards `--materials-fibre`, which is `--line`: the colour part makes it in the neutral's own hue on every tone, so they lean the way the page's neutrals lean. The first version leaned towards `--mark`, which turned the light sheets pink and lamplit parchment salmon (the mark there is cool blue). Kraft, card, tape, string and the rail lean towards `--earth`, the colour part's brown on every tone (kraft by day, dark wood at night), falling back to `--line` where a page has none: with `--line` alone, kraft was oatmeal by day and a grey board at night. Metal leans towards `--metal`, `--metal-deep` and `--metal-lit` (gold by default). The sheets lean further on a light page than on a dark one, written with `light-dark()`. Soft text on kraft and metal is `--ink-soft` taken 45% of the way to `--ink` (`--materials-soft-on-brown`): the colour part's writer measured plain soft text on kraft at 3.84 to 1. The helpers are made on the page and on each band, and the darker soft text is set on the sheet, because a custom property cannot be made from itself on one element.

`--materials-sheet` is this part's answer to "what colour is the paper", and `--sheet-fill` the whole of what the sheet's background paints (the worn rim, then that colour), set on every `.sheet` in Base. Any other part that paints a sheet (frames' torn paper, on the sheet's `::before` through its `--sheet-mask`) paints `var(--sheet-fill)`, so the torn shape and the material agree. The texture span takes `mask: var(--sheet-mask, none)`, so its grain is cut to the same shape; the fixing span is never masked, so tape and pins overhang a torn edge. This part never draws on the sheet's own `::before` or `::after`: they are the frames part's.

## Choosing

Start from a starting point (below), then change a layer if the brief asks for it.

| Starting point | What it feels like | Suits best | Fights |
|---|---|---|---|
| Fine paper | Quiet, printed, careful: a good sheet on a desk | Professional; artistic | A loud or crowded brief |
| Paper and tape | Made at a kitchen table by one person | Warm; a single maker's shop | Professional |
| Cut paper on felt | A club's notice board: card pinned up a little crooked | Warm; a community page | Professional; a dark lead |
| Parchment and ink | Old, hand-written, worn at the edges | A dark, painterly lead; artistic | Professional; a bright warm page, where it looks tired |
| Stone and chalk | A slate someone has written on | A dark, painterly lead; a school, a pub board | Warm paper looks; professional |
| Wood and canvas | A market stall: canvas tags on string from an oak rail | Warm; a small shop with a dark lead | Professional |
| Metal and dark glass | A game's interface: smoked glass in riveted metal | A game-style site | Long reading; anything calm or official |
| Warm | Somebody's hand is visible: card, tape, a stamp | The warm guide | A dark lead |
| Sorcery | Stained parchment nailed up in a dark room | The dark, painterly guide | Anything bright and new |
| Gilded dark | Battered glass panes in riveted frames | The game-interface guide | Calm or official sites |
| Lantern fair | Brown paper tags on string at a night market | A night market; a shop with a dark lead | Daytime services |
| Almanac plate | A printed plate pressed into laid paper | A society, an observatory, a library | Anything hand-made |
| Catalogue of glazes | A museum label: plain matte card | A gallery, a maker of objects | A busy brief |
| Field journal | A notebook page clipped to a board, folded in a pocket | A walking club, a naturalist, a garden | A dark lead |
| Repair cafe | Manila repair tags, handled and stamped | A bright, busy community page | Professional; a calm brief |

How to choose:

- **Ask what the organisation would pin to a wall, and what it is made of** (the warm guide's two questions; they work for any site). A parcel is kraft; a ticket is card; a scroll is parchment; a dashboard pane is glass. Then the fixing is how that real thing is held up: tape in a notebook, pins on a board, string on a stall, rivets on a machine.
- **One material per page.** Two sheets from different worlds (stone slabs and a felt board) read as stickers from different sets; one shop under a warm lead dropped its stone to keep only parchment. The exception seen: a market stall is wood, canvas and paper tags because all three are one real object.
- **Detail goes where the eye should go.** A material on every box is a template with texture; on the repeated item (the tag, the notice, the ticket) and one signature sheet, it is the site's own. Plain sheets are a real choice for forms, long reading and anything that must look official.
- **The colour part decides how dark the page is; this part does not.** Fine paper on a dark page is a dark sheet; on the lamplit tone it is lit paper in a dark room. If the brief wants pale paper in a dark room, pick the lamplit tone first.

## Base

Code every pick needs, whatever the options. It paints the material's fill on every `.sheet` itself, so a page made only of the hooks shows the paper's colour; the texture and the turn need the empty `.materials-mat` element inside the sheet (above), and a fixing needs `.materials-fix`. A sheet with a `.materials-mat` gives its own fill to it, so the paper can turn while the words stay level; a sheet without one is a plain sheet in the material's colour, which is the right thing for a form. Only sheets with a `.materials-fix` turn and take the room their fixing needs, so a page can mix pinned notices and flat forms under one pick. In forced colours the material layers are switched off and the paper keeps a plain edge (see "What the visitor's settings switch off"); on a phone the paper turns half as far.

```css assemble
/* The material lives on one empty element inside each sheet, behind the words: <span class="materials-mat" aria-hidden="true"></span>.
   Its ::before is the body and wear (slow and large), in the shadow colour; its ::after the grain (fine), in --ink.
   Every mask list starts with a transparent layer, so an all-none pick paints nothing. */
.page, .band, & { --materials-fibre: var(--line); --materials-brown: var(--earth, var(--line));
  --materials-twine: color-mix(in oklab, var(--materials-brown) 60%, var(--ink-soft));            /* tape and string */
  --materials-soft-on-brown: color-mix(in oklab, var(--ink-soft) 55%, var(--ink)); }              /* soft text on kraft and metal */
.sheet { position: relative; isolation: isolate;
  --sheet-fill: var(--materials-wear-lit, none), var(--materials-sheet, var(--surface));   /* what the paper is: frames' shaped edge paints this too */
  background: var(--sheet-fill);
  -webkit-backdrop-filter: var(--materials-glass, none); backdrop-filter: var(--materials-glass, none); }
.panel { background-color: var(--surface-raised); }   /* a raised box (a menu, a message) is plain raised surface, whatever the sheets are made of */
.sheet:has(> .materials-mat) { --sheet-fill: transparent; background: none; -webkit-backdrop-filter: none; backdrop-filter: none; }   /* the span is the paper */
.materials-mat { position: absolute; inset: 0; z-index: -1; border-radius: inherit; pointer-events: none;
  background: var(--materials-wear-lit, none), var(--materials-sheet, var(--surface));
  -webkit-mask: var(--sheet-mask, none); mask: var(--sheet-mask, none);   /* cut with a shaped sheet (frames); the fixings never are */
  rotate: var(--materials-tilt, 0deg); transform-origin: var(--materials-tilt-at, 50% 50%);
  -webkit-backdrop-filter: var(--materials-glass, none); backdrop-filter: var(--materials-glass, none); }
.materials-mat::before, .materials-mat::after { content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none; }
.materials-mat::before { background: rgb(var(--shadow-rgb)); opacity: calc(min(var(--texture-strength, 0.1), 0.11) * 2.5);   /* the body is slow and large: it does not grow with a dark page's stronger texture */
  -webkit-mask-image: linear-gradient(transparent, transparent), var(--materials-body, none), var(--materials-wear, none), var(--materials-wear-2, none);
          mask-image: linear-gradient(transparent, transparent), var(--materials-body, none), var(--materials-wear, none), var(--materials-wear-2, none);
  -webkit-mask-size: auto, var(--materials-body-size, 100% 100%), var(--materials-wear-size, 100% 100%), var(--materials-wear-2-size, 100% 100%);
          mask-size: auto, var(--materials-body-size, 100% 100%), var(--materials-wear-size, 100% 100%), var(--materials-wear-2-size, 100% 100%);
  -webkit-mask-repeat: no-repeat, repeat, var(--materials-wear-repeat, no-repeat), no-repeat;
          mask-repeat: no-repeat, repeat, var(--materials-wear-repeat, no-repeat), no-repeat; }
.materials-mat::after { background: var(--materials-grain-ink, var(--ink));
  opacity: var(--materials-grain-op, calc(var(--texture-strength, 0.1) * var(--materials-grain-k, 1)));
  -webkit-mask-image: linear-gradient(transparent, transparent), var(--materials-grain, none), var(--materials-grain-2, none), var(--materials-grain-3, none);
          mask-image: linear-gradient(transparent, transparent), var(--materials-grain, none), var(--materials-grain-2, none), var(--materials-grain-3, none);
  -webkit-mask-size: auto, var(--materials-grain-size, auto), var(--materials-grain-2-size, auto), var(--materials-grain-3-size, auto);
          mask-size: auto, var(--materials-grain-size, auto), var(--materials-grain-2-size, auto), var(--materials-grain-3-size, auto); }
/* fixings: tape, pins, a clip, rivets or a rail, on a second empty element: <span class="materials-fix" aria-hidden="true">...</span> */
.materials-fix { position: absolute; inset: 0; z-index: 2; pointer-events: none; }
.sheet > :is(.materials-mat, .materials-fix) { grid-area: auto !important; }   /* both cover the whole sheet, even when a layout places every child of a grid sheet */
.materials-fix > * { position: absolute; display: block; }
@media (max-width: 30rem) { .materials-mat { rotate: calc(var(--materials-tilt, 0deg) / 2); } }   /* on a phone the paper turns half as far */
@media (forced-colors: active) {   /* masks, gradients and shadows go; the paper keeps a plain edge, so it is still a sheet */
  .materials-mat { border: 1px solid CanvasText; }
  .materials-mat::before, .materials-mat::after, .materials-fix { display: none; }
  .sheet :is(h1, h2, h3) { -webkit-mask: none; mask: none; }
}
```

## Layers

### Sheet
- Layer: sheet
- Owns: what the surface with words is made of: how far its colour leans from `--surface`, and its slow body (the cloud in paper, the stains in parchment, the sheen on metal, the blur behind glass).
- Default: plain

#### Plain
- Id: plain
- Status: draft
- Looks like: no material. One flat colour, the surface, and nothing else.
- Made with: `--surface` and no body.

```css assemble
/* sheet: plain. The fill is the surface itself, the Base's default; no body. */
```

- Careful: the right sheet for forms, tables, long reading and any page that must look official. It is also the base for a slate (with `grain: speckle` and `ink: chalk`) and for a pane that only its fixings make metal.
- Light and dark: the surface itself on both.
- Personality: any
- Goes with: `materials: grain none`; `frames: hairline` or `card`; `light: shadows soft`.
- Used on: most mockups' forms and footers, and a tutoring site throughout.

#### Fine paper
- Id: fine-paper
- Status: draft
- Looks like: a good sheet: bright, even, with the faintest cloud in it, as paper looks held to the light (paper-makers call it the formation).
- Made with: the surface leaned a third of the way to `--surface-raised`, so it is a touch brighter than plain, and a large, very soft cloud tile in the body.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form).

```css assemble
.sheet { --materials-sheet: color-mix(in oklab, var(--surface) 60%, var(--surface-raised)); }
& { --materials-body: var(--materials-tile-formation); --materials-body-size: 300px 300px; }
/* the tile (alpha only) is drawn by tests/parts/source/materials.py; copy it from tests/parts/materials.html if it is redrawn */
& { --materials-tile-formation: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E %3Cfilter id='n' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.03' numOctaves='3' seed='4' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.6 0 0 0 -0.31'/%3E%3C/filter%3E %3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E"); }
```

- Careful: the cloud is meant to be felt, not seen; the first try at twice this strength read as grey camouflage. **With `frames: none` and `light: shadows none` there is no sheet**: a fine-paper sheet on a ground of the same colour vanishes. Then the page itself is the paper, and the paper's texture is the background part's (`background: texture grain`), with this part's sheet left plain; the quiet gallery came to exactly this ("material moved into the grained ground"). With any shadow or a ground a step darker (the colour part's toned tone), the sheet shows by itself.
- Light and dark: on a light page a bright sheet; on a dark page a dark sheet a step lighter than the surface, the cloud a little darker in it. On the lamplit tone it is the lit paper itself.
- Personality: serious, calm
- Goes with: `materials: grain fibre` or `laid`; `light: shadows paper-lift`; `frames: none` or `hairline`.
- Used on: 3 mockups: a poetry site (sheets on grained paper), an observatory (sheets that stay light under a night sky) and a quiet gallery of pots (the paper moved into the ground).

#### Card
- Id: card
- Status: draft
- Looks like: thick, matte card with a little colour in it: a label, a luggage tag, a notice, a museum caption.
- Made with: the surface leaned 20% towards `--earth` on a light page and 14% on a dark one (in oklch, so the colour stays clean): a manila card. No body: card is even.

- Needs markup: none: the sheet takes the colour itself; add `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form) only for the turn a fixing gives.

```css assemble
.sheet { --materials-fibre: var(--materials-brown);
  --materials-sheet: light-dark(color-mix(in oklch, var(--surface) 80%, var(--materials-fibre)), color-mix(in oklch, var(--surface) 86%, var(--materials-fibre))); }
```

- Careful: card is the sheet for the repeated item that is a thing: a tag, a ticket, a label. Matte, never glossy: museum label guides ask for surfaces that cut glare and plain, non-condensed type (R12). It takes its hue from `--earth`: manila on a light page, a warm dark board at night. A museum label that should be neutral takes `sheet: fine-paper` instead.
- Light and dark: a pale warm card on a light page; a dark board, warmer than the surface, on a dark one.
- Personality: friendly, calm
- Goes with: `materials: fixing pins` or `string`; `light: shadows crisp` or `paper-lift`; `frames: torn-paper`.
- Used on: 3 mockups: a repair café (manila repair tags), a volunteer page (coloured notices) and a browser game's pages (specimen labels for its cards).

#### Kraft
- Id: kraft
- Status: draft
- Looks like: brown paper: a parcel, a paper bag, a price tag.
- Made with: the surface leaned 70% towards `--earth` on a light page and 45% on a dark one, with the faint paper cloud in the body; usually with fibre grain, since kraft is unbleached pulp with visible specks.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form).

```css assemble
.sheet { --ink-soft: var(--materials-soft-on-brown);   /* soft text darkened on brown: plain soft text measured 3.84 to 1 */
  --materials-fibre: var(--materials-brown);
  --materials-sheet: light-dark(color-mix(in oklch, var(--surface) 30%, var(--materials-fibre)), color-mix(in oklch, var(--surface) 55%, var(--materials-fibre))); }
& { --materials-body: var(--materials-tile-formation); --materials-body-size: 300px 300px; }
/* the tile (alpha only) is drawn by tests/parts/source/materials.py; copy it from tests/parts/materials.html if it is redrawn */
& { --materials-tile-formation: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E %3Cfilter id='n' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.03' numOctaves='3' seed='4' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.6 0 0 0 -0.31'/%3E%3C/filter%3E %3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E"); }
```

- Careful: kraft is the darkest sheet, and printers warn that ink on kraft lands darker, warmer and lower in contrast (R10). So soft text on kraft is darkened (`--soft-on-brown`); plain `--ink-soft` measured 3.84 to 1. Leaned towards `--line` instead of `--earth`, kraft was oatmeal by day and a grey board at night; `--earth` is the brown whatever the neutrals. Keep kraft for short things (tags, prices, a parcel label); long reading goes on paper.
- Light and dark: brown paper on a light page; a dark, warm cardboard at night; on lamplit a brown tag a step darker than the parchment.
- Personality: friendly, playful
- Goes with: `materials: grain fibre`; `materials: fixing string` or `tape`; `materials: ink stamped`.
- Used on: 2 mockups: a soap maker's shop (kraft price tags) and a field notebook (kraft tape, tags and footer).

#### Parchment
- Id: parchment
- Status: draft
- Looks like: old skin-paper, warm and uneven, with slow stains through it.
- Made with: the surface leaned 28% towards `--fibre` on a light page and 22% on a dark one, and a large, slow mottling tile in the body.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form).

```css assemble
.sheet { --materials-sheet: light-dark(color-mix(in oklch, var(--surface) 72%, var(--materials-fibre)), color-mix(in oklch, var(--surface) 78%, var(--materials-fibre))); }
& { --materials-body: var(--materials-tile-mottle); --materials-body-size: 420px 420px; }
/* the tile (alpha only) is drawn by tests/parts/source/materials.py; copy it from tests/parts/materials.html if it is redrawn */
& { --materials-tile-mottle: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='520' height='520'%3E %3Cfilter id='n' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.009' numOctaves='4' seed='7' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1.3 0 0 0 -0.48'/%3E%3C/filter%3E %3Crect width='520' height='520' filter='url(%23n)'/%3E%3C/svg%3E"); }
```

- Careful: the material where contrast is most often lost: the stains darken the sheet unevenly, so the ink is chosen against the darkest patch under any words. On one shop, ink that gave 7 to 1 on the plain sheet gave 5.4 to 1 on the worst stain. Keep it dim: the sorcery guide's parchment "never becomes a white page", and on a bright page a bright parchment looks brown and tired. Links on parchment are ink, underlined. Its first recipe wrote its own parchment colour (`#c9b083`); the colour part's lamplit tone now makes `--surface` that parchment, so this option only adds the stains.
- Light and dark: on a light page a beige sheet with grey-brown stains (it suits a light page least); on a dark page a dark, leathery sheet; on lamplit the dim parchment the sorcery guide asks for.
- Personality: dramatic, calm
- Goes with: `colour: tone lamplit`; `materials: wear soft-edges` or `stained`; `frames: torn-paper` or `inked-panel`; `light: glow lamp`.
- Used on: 4 mockups: a dark, painterly joke site (every word on torn parchment), two versions of a small shop of handmade goods (parchment notices and tags), and one look of a game-style joke site.

#### Canvas
- Id: canvas
- Status: draft
- Looks like: unbleached cloth: an awning, a banner, a stall's cover, a book's cloth binding.
- Made with: the surface leaned 28% towards `--fibre` on a light page and 18% on a dark one, with the weave grain.

- Needs markup: none: the sheet takes the colour itself; add `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form) only for the turn a fixing gives.

```css assemble
.sheet { --materials-sheet: light-dark(color-mix(in oklch, var(--surface) 72%, var(--materials-fibre)), color-mix(in oklch, var(--surface) 82%, var(--materials-fibre))); }
```

- Careful: without `grain: weave` it is only a tinted card; the weave is what makes it cloth. A striped canvas valance across the top of a section is a frame (`frames: wavy-edge` scallops), not a sheet: no words on stripes.
- Light and dark: a pale linen on a light page; a dark sacking on a dark one, where the weave shows most.
- Personality: friendly, playful
- Goes with: `materials: grain weave`; `materials: fixing string`; `frames: wavy-edge`.
- Used on: 2 mockups: a night market (canvas sheets and fact boxes, a striped valance) and a fair-stall shop.

#### Glass
- Id: glass
- Status: draft
- Looks like: smoked glass over the world behind: whatever lies under the pane shows through, blurred.
- Made with: the surface at 68% with `backdrop-filter: blur(10px) saturate(1.3)`, and a soft darkening towards the bottom in the body. A solid fallback when the browser has no backdrop blur, and a solid pane when the visitor asks for less transparency or more contrast.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form).

```css assemble
.sheet { --materials-sheet: color-mix(in oklab, var(--surface) 68%, transparent); --materials-glass: blur(10px) saturate(1.3); }
& { --materials-body: linear-gradient(160deg, transparent 40%, color-mix(in srgb, black 35%, transparent)); }
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) { .sheet { --materials-sheet: color-mix(in oklab, var(--surface) 96%, transparent); } }
@media (prefers-reduced-transparency: reduce), (prefers-contrast: more) { .sheet { --materials-sheet: var(--surface); --materials-glass: none; } }
```

- Careful: glass is only glass if something is behind it; on a flat ground it is a plain sheet. Windows' own acrylic material is kept to short-lived surfaces (menus, flyouts), never stacked, never butted edge to edge, and falls back to solid on battery saver, with transparency off and in high contrast (R13); Apple asks for the same respect for "reduce transparency" (R15). Here too: a pane or two, not every card. Blur costs the browser in proportion to the area it covers, and a blurred sticky header over scrolling content is the worst case (R18, R19); 8 to 16 pixels is enough (R9). **Any ancestor with a `filter`, an `opacity` below 1 or a mask stops the blur** (it becomes the "backdrop root"), so a glass sheet never takes `filter: var(--drop-low)`: it uses `box-shadow`. Measure text over the busiest thing that can pass behind it; `prefers-reduced-transparency` is not yet in every browser (R21), so the pane must pass without it.
- Light and dark: on a light page a frosted pale pane; on a dark page the smoked dark glass the game guide asks for. **Not on the lamplit tone**: a pale sheet made see-through over a dark room darkens, and soft text fell to 2.7 to 1 in the swatch book's lamplit test. On lamplit, panes are paper.
- Personality: dramatic, playful
- Goes with: `materials: fixing rivets`; `frames: riveted-metal`; `background: scene painted-ground`; `light: shadows deep`.
- Used on: 3 mockups: three versions of a game-style joke site (dark panes over a painted world).

#### Metal
- Id: metal
- Status: draft
- Looks like: a brushed plate: a soft sheen across it and fine streaks one way. A name plate, a machine's panel, a plaque.
- Made with: the surface leaned 45% towards `--metal` on a light page (brass) and 38% towards `--metal-deep` on a dark one (bronze), two broad soft bands of sheen in the body, the brushed grain, and soft text darkened as on kraft. Without the colour part's metal names it falls back to `--ink-soft`, a pewter.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form).

```css assemble
.sheet { --ink-soft: var(--materials-soft-on-brown);
  --materials-sheet: light-dark(color-mix(in oklab, var(--surface) 55%, var(--metal, var(--ink-soft))), color-mix(in oklab, var(--surface) 62%, var(--metal-deep, var(--ink-soft)))); }
& { --materials-body: linear-gradient(104deg, transparent 6%, color-mix(in srgb, black 30%, transparent) 30%, transparent 50%,
    transparent 64%, color-mix(in srgb, black 22%, transparent) 80%, transparent 94%); }
```

- Careful: which metal (gold, steel, bronze) is the colour part's metal layer; this is the brushed surface. Brushed brass on a light page can read as pale wood if the sheen is turned down: keep both sheen bands. The heavy riveted ring round a window is `frames: riveted-metal`. Metal holds a few words (a name, a heading, a number), not paragraphs. A sheen that moves stops under reduced motion.
- Light and dark: brushed brass on a light page; dark bronze on a dark one.
- Personality: serious, dramatic
- Goes with: `materials: grain brushed`; `materials: fixing rivets`; `frames: riveted-metal`.
- Used on: 3 mockups: three versions of a game-style joke site (bevelled name plates; drawn there as gradients in gold and steel).

### Grain
- Layer: grain
- Owns: the fine texture on the sheet, seen close up: specks, fibres, laid lines, threads, wood, streaks, flecks, a printed grid.
- Default: none

#### None
- Id: none
- Status: draft
- Looks like: smooth.
- Made with: nothing.

```css assemble
/* grain: none. The sheet is smooth; the Base's grain layer stays empty. */
```

- Careful: the right choice for glass, for plain sheets that hold forms, and for any page whose material is in its fixings alone.
- Light and dark: the same.
- Personality: any
- Goes with: `materials: sheet plain` or `glass`.
- Used on: most sheets on most mockups.

#### Fibre
- Id: fibre
- Status: draft
- Looks like: fine specks and a few short, curled fibres lying every way, as in any paper made from pulp.
- Made with: a 260-pixel tile: `feTurbulence` speckle turned into alpha, with about forty short curved strokes drawn over it (each drawn again a tile away where it crosses an edge, so the tile has no seam). Over `--ink` at 1.9 times `--texture-strength`.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form): the grain is its `::after`.

```css assemble
& { --materials-grain: var(--materials-tile-fibre); --materials-grain-size: 260px 260px; --materials-grain-k: 1.9; }
/* the tile (alpha only) is drawn by tests/parts/source/materials.py; copy it from tests/parts/materials.html if it is redrawn */
& { --materials-tile-fibre: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='260' height='260'%3E %3Cfilter id='n' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' seed='1' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2.2 0 0 0 -1.0'/%3E%3C/filter%3E %3Crect width='260' height='260' filter='url(%23n)'/%3E%3Cg fill='none' stroke='black' stroke-width='0.7' stroke-linecap='round'%3E%3Cpath d='M117.6 145.5Q122.8 143.0 127.9 140.2' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M49.4 209.0Q43.2 213.1 36.2 211.0' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M78.9 23.6Q77.2 15.2 84.1 10.2' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M78.9 23.6Q77.2 15.2 84.1 10.2' transform='translate(0 260)' opacity='0.5'/%3E%3Cpath d='M250.8 170.0Q244.7 171.0 244.9 164.8' transform='translate(-260 0)' opacity='0.7'/%3E%3Cpath d='M250.8 170.0Q244.7 171.0 244.9 164.8' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M16.4 9.3Q23.1 6.8 26.0 0.2' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M16.4 9.3Q23.1 6.8 26.0 0.2' transform='translate(0 260)' opacity='0.5'/%3E%3Cpath d='M16.4 9.3Q23.1 6.8 26.0 0.2' transform='translate(260 0)' opacity='0.5'/%3E%3Cpath d='M16.4 9.3Q23.1 6.8 26.0 0.2' transform='translate(260 260)' opacity='0.5'/%3E%3Cpath d='M114.5 219.0Q107.7 218.2 101.0 217.4' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M22.1 170.2Q14.5 170.1 11.6 177.2' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M22.1 170.2Q14.5 170.1 11.6 177.2' transform='translate(260 0)' opacity='0.35'/%3E%3Cpath d='M184.0 82.0Q188.9 86.1 185.2 91.4' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M104.1 220.1Q95.2 223.2 90.9 231.6' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M55.5 241.0Q59.8 244.7 65.5 244.4' transform='translate(0 -260)' opacity='0.5'/%3E%3Cpath d='M55.5 241.0Q59.8 244.7 65.5 244.4' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M19.0 163.7Q15.8 158.4 20.6 154.6' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M19.0 163.7Q15.8 158.4 20.6 154.6' transform='translate(260 0)' opacity='0.5'/%3E%3Cpath d='M3.9 106.6Q8.3 106.7 10.7 103.1' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M3.9 106.6Q8.3 106.7 10.7 103.1' transform='translate(260 0)' opacity='0.35'/%3E%3Cpath d='M15.6 207.2Q18.8 212.7 21.2 218.6' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M15.6 207.2Q18.8 212.7 21.2 218.6' transform='translate(260 0)' opacity='0.35'/%3E%3Cpath d='M256.2 200.1Q252.0 203.6 246.9 205.2' transform='translate(-260 0)' opacity='0.35'/%3E%3Cpath d='M256.2 200.1Q252.0 203.6 246.9 205.2' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M0.1 224.7Q7.4 228.6 13.1 222.7' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M0.1 224.7Q7.4 228.6 13.1 222.7' transform='translate(260 0)' opacity='0.35'/%3E%3Cpath d='M54.8 102.5Q55.8 94.6 63.1 91.7' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M55.4 67.2Q54.1 61.9 56.9 57.3' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M19.3 54.3Q16.3 52.8 15.3 49.6' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M19.3 54.3Q16.3 52.8 15.3 49.6' transform='translate(260 0)' opacity='0.7'/%3E%3Cpath d='M117.8 249.4Q111.0 246.4 105.0 250.7' transform='translate(0 -260)' opacity='0.35'/%3E%3Cpath d='M117.8 249.4Q111.0 246.4 105.0 250.7' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M163.1 80.8Q161.8 87.7 164.9 94.0' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M192.3 244.5Q191.5 254.0 198.0 260.9' transform='translate(0 -260)' opacity='0.7'/%3E%3Cpath d='M192.3 244.5Q191.5 254.0 198.0 260.9' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M20.4 12.3Q26.7 14.3 29.8 20.0' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M20.4 12.3Q26.7 14.3 29.8 20.0' transform='translate(0 260)' opacity='0.7'/%3E%3Cpath d='M183.2 66.8Q184.3 60.0 189.1 55.0' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M241.6 254.1Q244.6 259.3 249.8 262.4' transform='translate(-260 -260)' opacity='0.7'/%3E%3Cpath d='M241.6 254.1Q244.6 259.3 249.8 262.4' transform='translate(-260 0)' opacity='0.7'/%3E%3Cpath d='M241.6 254.1Q244.6 259.3 249.8 262.4' transform='translate(0 -260)' opacity='0.7'/%3E%3Cpath d='M241.6 254.1Q244.6 259.3 249.8 262.4' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M159.7 72.9Q161.0 66.6 167.1 68.7' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M107.0 64.8Q111.4 66.4 116.0 67.5' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M24.0 36.0Q18.5 35.3 14.5 39.0' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M24.0 36.0Q18.5 35.3 14.5 39.0' transform='translate(260 0)' opacity='0.7'/%3E%3Cpath d='M152.0 36.5Q154.1 41.2 158.0 37.8' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M81.1 8.7Q75.8 10.2 75.4 4.7' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M81.1 8.7Q75.8 10.2 75.4 4.7' transform='translate(0 260)' opacity='0.5'/%3E%3Cpath d='M82.9 259.8Q87.4 264.8 94.1 265.6' transform='translate(0 -260)' opacity='0.7'/%3E%3Cpath d='M82.9 259.8Q87.4 264.8 94.1 265.6' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M191.7 33.7Q195.6 28.5 201.5 31.4' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M234.2 226.5Q225.7 227.2 220.8 234.2' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M3.8 172.2Q4.5 177.4 -0.7 176.4' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M3.8 172.2Q4.5 177.4 -0.7 176.4' transform='translate(260 0)' opacity='0.35'/%3E%3Cpath d='M166.2 258.3Q170.8 252.4 177.0 248.2' transform='translate(0 -260)' opacity='0.7'/%3E%3Cpath d='M166.2 258.3Q170.8 252.4 177.0 248.2' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M180.5 119.0Q174.4 120.3 168.3 121.9' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M7.7 156.3Q3.2 154.9 -1.0 157.4' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M7.7 156.3Q3.2 154.9 -1.0 157.4' transform='translate(260 0)' opacity='0.5'/%3E%3Cpath d='M202.8 171.6Q194.6 173.7 186.1 173.1' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M176.3 52.7Q179.0 60.8 184.5 67.4' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M129.6 62.8Q125.1 64.2 122.1 67.9' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M228.9 99.9Q222.8 100.7 220.4 95.1' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M91.2 232.9Q93.3 238.4 97.7 234.6' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M29.3 122.6Q35.9 117.9 43.6 115.4' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M128.4 82.0Q132.7 74.2 137.9 66.9' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M215.5 72.3Q208.6 69.6 204.4 63.5' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M80.3 205.8Q84.2 205.8 87.9 206.7' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M200.0 69.3Q206.2 62.5 202.8 54.0' transform='translate(0 0)' opacity='0.35'/%3E%3C/g%3E%3C/svg%3E"); }
```

- Careful: the safest grain. At 2.4 times the strength it looked like dust on a dark page; 1.9 is felt on both. The noise numbers come from the usual grainy-texture recipes (`fractalNoise`, `stitchTiles='stitch'`, R5, R6).
- Light and dark: dark specks on a light sheet, light specks on a dark one; slightly stronger on a dark page, where `--texture-strength` is higher.
- Personality: calm, friendly
- Goes with: `materials: sheet fine-paper`, `card`, `kraft` or `parchment`; `light: shadows paper-lift`.
- Used on: 5 mockups, as grain on the page or the sheets: a soap maker's shop, a poetry site, a field notebook, a night market (its canvas) and a repair café (its pegboard).

#### Laid
- Id: laid
- Status: draft
- Looks like: fine lines close together, and a few far apart across them: hand-made and good writing paper held to the light.
- Made with: a line every 4 pixels at 60% and a "chain line" every 96 pixels at 70%, both gradients, at 0.6 times the strength.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form): the grain is its `::after`.

```css assemble
& { --materials-grain: repeating-linear-gradient(0deg, color-mix(in srgb, black 60%, transparent) 0 1px, transparent 1px 4px);
  --materials-grain-2: repeating-linear-gradient(90deg, transparent 0 94px, color-mix(in srgb, black 70%, transparent) 94px 95px, transparent 95px 96px);
  --materials-grain-k: 0.6; }
```

- Careful: at full strength the lines read as a screen's scan lines and the chain lines as the columns of a table; it must be barely there. Do not combine with ruled or graph lines.
- Light and dark: on a dark page the lines are light and show a little more.
- Personality: serious, calm
- Goes with: `materials: sheet fine-paper`; `materials: ink letterpress`; `lettering: sober-pair`.
- Used on: no mockup yet. From research: letterpress printers prefer heavy cotton papers, whose fibres take the impression (R10, R11).

#### Weave
- Id: weave
- Status: draft
- Looks like: threads crossing: linen, canvas, book cloth.
- Made with: two sets of threads as gradients, one every 3 pixels and a weaker one between, each way, and the fibre tile over them for slubs.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form): the grain is its `::after`.

```css assemble
& { --materials-grain: repeating-linear-gradient(0deg, color-mix(in srgb, black 70%, transparent) 0 1px, transparent 1px 3px, color-mix(in srgb, black 35%, transparent) 3px 4px, transparent 4px 6px);
  --materials-grain-2: repeating-linear-gradient(90deg, color-mix(in srgb, black 60%, transparent) 0 1px, transparent 1px 3px, black 3px 4px, transparent 4px 5px);
  --materials-grain-3: var(--materials-tile-fibre); --materials-grain-3-size: 260px 260px; --materials-grain-k: 0.9; }
/* the tile (alpha only) is drawn by tests/parts/source/materials.py; copy it from tests/parts/materials.html if it is redrawn */
& { --materials-tile-fibre: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='260' height='260'%3E %3Cfilter id='n' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' seed='1' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2.2 0 0 0 -1.0'/%3E%3C/filter%3E %3Crect width='260' height='260' filter='url(%23n)'/%3E%3Cg fill='none' stroke='black' stroke-width='0.7' stroke-linecap='round'%3E%3Cpath d='M117.6 145.5Q122.8 143.0 127.9 140.2' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M49.4 209.0Q43.2 213.1 36.2 211.0' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M78.9 23.6Q77.2 15.2 84.1 10.2' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M78.9 23.6Q77.2 15.2 84.1 10.2' transform='translate(0 260)' opacity='0.5'/%3E%3Cpath d='M250.8 170.0Q244.7 171.0 244.9 164.8' transform='translate(-260 0)' opacity='0.7'/%3E%3Cpath d='M250.8 170.0Q244.7 171.0 244.9 164.8' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M16.4 9.3Q23.1 6.8 26.0 0.2' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M16.4 9.3Q23.1 6.8 26.0 0.2' transform='translate(0 260)' opacity='0.5'/%3E%3Cpath d='M16.4 9.3Q23.1 6.8 26.0 0.2' transform='translate(260 0)' opacity='0.5'/%3E%3Cpath d='M16.4 9.3Q23.1 6.8 26.0 0.2' transform='translate(260 260)' opacity='0.5'/%3E%3Cpath d='M114.5 219.0Q107.7 218.2 101.0 217.4' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M22.1 170.2Q14.5 170.1 11.6 177.2' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M22.1 170.2Q14.5 170.1 11.6 177.2' transform='translate(260 0)' opacity='0.35'/%3E%3Cpath d='M184.0 82.0Q188.9 86.1 185.2 91.4' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M104.1 220.1Q95.2 223.2 90.9 231.6' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M55.5 241.0Q59.8 244.7 65.5 244.4' transform='translate(0 -260)' opacity='0.5'/%3E%3Cpath d='M55.5 241.0Q59.8 244.7 65.5 244.4' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M19.0 163.7Q15.8 158.4 20.6 154.6' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M19.0 163.7Q15.8 158.4 20.6 154.6' transform='translate(260 0)' opacity='0.5'/%3E%3Cpath d='M3.9 106.6Q8.3 106.7 10.7 103.1' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M3.9 106.6Q8.3 106.7 10.7 103.1' transform='translate(260 0)' opacity='0.35'/%3E%3Cpath d='M15.6 207.2Q18.8 212.7 21.2 218.6' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M15.6 207.2Q18.8 212.7 21.2 218.6' transform='translate(260 0)' opacity='0.35'/%3E%3Cpath d='M256.2 200.1Q252.0 203.6 246.9 205.2' transform='translate(-260 0)' opacity='0.35'/%3E%3Cpath d='M256.2 200.1Q252.0 203.6 246.9 205.2' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M0.1 224.7Q7.4 228.6 13.1 222.7' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M0.1 224.7Q7.4 228.6 13.1 222.7' transform='translate(260 0)' opacity='0.35'/%3E%3Cpath d='M54.8 102.5Q55.8 94.6 63.1 91.7' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M55.4 67.2Q54.1 61.9 56.9 57.3' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M19.3 54.3Q16.3 52.8 15.3 49.6' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M19.3 54.3Q16.3 52.8 15.3 49.6' transform='translate(260 0)' opacity='0.7'/%3E%3Cpath d='M117.8 249.4Q111.0 246.4 105.0 250.7' transform='translate(0 -260)' opacity='0.35'/%3E%3Cpath d='M117.8 249.4Q111.0 246.4 105.0 250.7' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M163.1 80.8Q161.8 87.7 164.9 94.0' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M192.3 244.5Q191.5 254.0 198.0 260.9' transform='translate(0 -260)' opacity='0.7'/%3E%3Cpath d='M192.3 244.5Q191.5 254.0 198.0 260.9' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M20.4 12.3Q26.7 14.3 29.8 20.0' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M20.4 12.3Q26.7 14.3 29.8 20.0' transform='translate(0 260)' opacity='0.7'/%3E%3Cpath d='M183.2 66.8Q184.3 60.0 189.1 55.0' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M241.6 254.1Q244.6 259.3 249.8 262.4' transform='translate(-260 -260)' opacity='0.7'/%3E%3Cpath d='M241.6 254.1Q244.6 259.3 249.8 262.4' transform='translate(-260 0)' opacity='0.7'/%3E%3Cpath d='M241.6 254.1Q244.6 259.3 249.8 262.4' transform='translate(0 -260)' opacity='0.7'/%3E%3Cpath d='M241.6 254.1Q244.6 259.3 249.8 262.4' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M159.7 72.9Q161.0 66.6 167.1 68.7' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M107.0 64.8Q111.4 66.4 116.0 67.5' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M24.0 36.0Q18.5 35.3 14.5 39.0' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M24.0 36.0Q18.5 35.3 14.5 39.0' transform='translate(260 0)' opacity='0.7'/%3E%3Cpath d='M152.0 36.5Q154.1 41.2 158.0 37.8' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M81.1 8.7Q75.8 10.2 75.4 4.7' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M81.1 8.7Q75.8 10.2 75.4 4.7' transform='translate(0 260)' opacity='0.5'/%3E%3Cpath d='M82.9 259.8Q87.4 264.8 94.1 265.6' transform='translate(0 -260)' opacity='0.7'/%3E%3Cpath d='M82.9 259.8Q87.4 264.8 94.1 265.6' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M191.7 33.7Q195.6 28.5 201.5 31.4' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M234.2 226.5Q225.7 227.2 220.8 234.2' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M3.8 172.2Q4.5 177.4 -0.7 176.4' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M3.8 172.2Q4.5 177.4 -0.7 176.4' transform='translate(260 0)' opacity='0.35'/%3E%3Cpath d='M166.2 258.3Q170.8 252.4 177.0 248.2' transform='translate(0 -260)' opacity='0.7'/%3E%3Cpath d='M166.2 258.3Q170.8 252.4 177.0 248.2' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M180.5 119.0Q174.4 120.3 168.3 121.9' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M7.7 156.3Q3.2 154.9 -1.0 157.4' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M7.7 156.3Q3.2 154.9 -1.0 157.4' transform='translate(260 0)' opacity='0.5'/%3E%3Cpath d='M202.8 171.6Q194.6 173.7 186.1 173.1' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M176.3 52.7Q179.0 60.8 184.5 67.4' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M129.6 62.8Q125.1 64.2 122.1 67.9' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M228.9 99.9Q222.8 100.7 220.4 95.1' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M91.2 232.9Q93.3 238.4 97.7 234.6' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M29.3 122.6Q35.9 117.9 43.6 115.4' transform='translate(0 0)' opacity='0.7'/%3E%3Cpath d='M128.4 82.0Q132.7 74.2 137.9 66.9' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M215.5 72.3Q208.6 69.6 204.4 63.5' transform='translate(0 0)' opacity='0.5'/%3E%3Cpath d='M80.3 205.8Q84.2 205.8 87.9 206.7' transform='translate(0 0)' opacity='0.35'/%3E%3Cpath d='M200.0 69.3Q206.2 62.5 202.8 54.0' transform='translate(0 0)' opacity='0.35'/%3E%3C/g%3E%3C/svg%3E"); }
```

- Careful: an even grid reads as window screen; the uneven pitch and the fibre are what make it cloth. Gradient patterns like this need no file at all (R8).
- Light and dark: a fine linen on a light sheet; a coarse sacking on a dark one.
- Personality: friendly, calm
- Goes with: `materials: sheet canvas`; `materials: fixing string`.
- Used on: 2 mockups: a night market and a fair-stall shop (canvas, drawn there with grain only).

#### Wood
- Id: wood
- Status: draft
- Looks like: long, gently wavy lines along the board, closer in places, parting round a knot.
- Made with: a 480 by 160 tile of about 25 lines, each a sum of two sine waves with a whole number of periods across the tile (so it repeats sideways without a seam), bending round one knot. Drawn by script, not by noise: turbulence stretched sideways looked like fur.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form): the grain is its `::after`.

```css assemble
& { --materials-grain: var(--materials-tile-wood); --materials-grain-size: 480px 160px; --materials-grain-k: 2.2; }
/* the tile (alpha only) is drawn by tests/parts/source/materials.py; copy it from tests/parts/materials.html if it is redrawn */
& { --materials-tile-wood: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='480' height='160'%3E%3Cg fill='none' stroke='black' stroke-linecap='round'%3E%3Cpath d='M0 12L16 13L32 13L48 12L64 12L80 12L96 12L112 12L128 12L144 12L160 12L176 12L192 12L208 11L224 10L240 10L256 9L272 9L288 10L304 10L320 10L336 10L352 10L368 10L384 10L400 10L416 10L432 10L448 11L464 12L480 12' stroke-width='1.6' opacity='0.55'/%3E%3Cpath d='M0 12L16 13L32 13L48 12L64 12L80 12L96 12L112 12L128 12L144 12L160 12L176 12L192 12L208 11L224 10L240 10L256 9L272 9L288 10L304 10L320 10L336 10L352 10L368 10L384 10L400 10L416 10L432 10L448 11L464 12L480 12' transform='translate(0 160)' stroke-width='1.6' opacity='0.55'/%3E%3Cpath d='M0 15L16 15L32 15L48 15L64 14L80 13L96 13L112 12L128 12L144 13L160 14L176 15L192 15L208 15L224 15L240 15L256 15L272 15L288 15L304 16L320 17L336 17L352 18L368 18L384 17L400 16L416 15L432 15L448 15L464 15L480 15' stroke-width='0.8' opacity='0.55'/%3E%3Cpath d='M0 20L16 20L32 21L48 20L64 20L80 19L96 18L112 18L128 17L144 18L160 18L176 19L192 20L208 20L224 20L240 20L256 20L272 19L288 20L304 20L320 21L336 22L352 22L368 23L384 22L400 22L416 21L432 20L448 20L464 20L480 20' stroke-width='0.8' opacity='0.55'/%3E%3Cpath d='M0 29L16 30L32 30L48 31L64 32L80 32L96 32L112 33L128 33L144 33L160 33L176 33L192 33L208 33L224 33L240 33L256 32L272 32L288 31L304 30L320 30L336 30L352 29L368 29L384 29L400 29L416 29L432 29L448 29L464 29L480 29' stroke-width='0.8' opacity='0.55'/%3E%3Cpath d='M0 37L16 36L32 36L48 37L64 37L80 38L96 39L112 39L128 39L144 38L160 38L176 37L192 36L208 36L224 37L240 37L256 38L272 38L288 37L304 37L320 36L336 35L352 35L368 35L384 36L400 36L416 37L432 38L448 38L464 37L480 37' stroke-width='1.1' opacity='0.55'/%3E%3Cpath d='M0 40L16 40L32 40L48 41L64 41L80 41L96 41L112 41L128 41L144 41L160 42L176 42L192 43L208 43L224 44L240 44L256 44L272 44L288 43L304 43L320 43L336 43L352 43L368 43L384 43L400 42L416 42L432 41L448 41L464 40L480 40' stroke-width='0.6' opacity='0.35'/%3E%3Cpath d='M0 45L16 45L32 45L48 45L64 46L80 47L96 48L112 49L128 49L144 49L160 48L176 47L192 47L208 46L224 47L240 47L256 47L272 47L288 47L304 46L320 45L336 44L352 43L368 43L384 43L400 44L416 45L432 45L448 46L464 45L480 45' stroke-width='1.1' opacity='0.55'/%3E%3Cpath d='M0 58L16 58L32 58L48 58L64 58L80 59L96 59L112 59L128 59L144 59L160 58L176 58L192 57L208 56L224 56L240 56L256 56L272 56L288 56L304 56L320 55L336 55L352 55L368 55L384 55L400 56L416 56L432 57L448 58L464 58L480 58' stroke-width='1.6' opacity='0.55'/%3E%3Cpath d='M0 61L16 61L32 61L48 62L64 62L80 63L96 63L112 64L128 65L144 65L160 65L176 65L192 65L208 65L224 65L240 65L256 65L272 65L288 64L304 64L320 63L336 63L352 62L368 61L384 61L400 61L416 61L432 61L448 61L464 61L480 61' stroke-width='0.6' opacity='0.35'/%3E%3Cpath d='M0 73L16 73L32 73L48 72L64 72L80 71L96 71L112 71L128 71L144 72L160 72L176 72L192 73L208 73L224 73L240 72L256 70L272 70L288 70L304 70L320 71L336 71L352 71L368 71L384 70L400 70L416 70L432 70L448 71L464 72L480 73' stroke-width='1.6' opacity='0.55'/%3E%3Cpath d='M0 81L16 81L32 81L48 81L64 81L80 80L96 80L112 80L128 80L144 79L160 79L176 78L192 80L208 82L224 83L240 83L256 80L272 78L288 78L304 78L320 78L336 78L352 78L368 78L384 79L400 80L416 80L432 81L448 81L464 81L480 81' stroke-width='1.1' opacity='0.8'/%3E%3Cpath d='M0 85L16 85L32 85L48 85L64 86L80 87L96 88L112 88L128 88L144 88L160 88L176 89L192 91L208 94L224 97L240 96L256 93L272 91L288 89L304 88L320 87L336 86L352 86L368 86L384 86L400 86L416 86L432 86L448 86L464 86L480 85' stroke-width='1.1' opacity='0.8'/%3E%3Cpath d='M0 93L16 92L32 91L48 90L64 90L80 90L96 90L112 91L128 92L144 93L160 93L176 92L192 90L208 87L224 85L240 86L256 90L272 93L288 95L304 96L320 96L336 96L352 95L368 94L384 93L400 93L416 93L432 93L448 93L464 93L480 93' stroke-width='0.8' opacity='0.8'/%3E%3Cpath d='M0 102L16 102L32 102L48 101L64 101L80 100L96 100L112 100L128 100L144 100L160 100L176 100L192 99L208 97L224 96L240 96L256 98L272 99L288 100L304 101L320 102L336 102L352 102L368 102L384 102L400 102L416 101L432 101L448 102L464 102L480 102' stroke-width='0.6' opacity='0.8'/%3E%3Cpath d='M0 108L16 107L32 106L48 106L64 105L80 106L96 106L112 107L128 107L144 108L160 107L176 106L192 105L208 104L224 104L240 105L256 106L272 107L288 108L304 109L320 108L336 108L352 107L368 107L384 106L400 107L416 107L432 108L448 108L464 108L480 108' stroke-width='0.6' opacity='0.55'/%3E%3Cpath d='M0 110L16 110L32 109L48 109L64 108L80 108L96 108L112 108L128 109L144 109L160 109L176 109L192 109L208 108L224 108L240 109L256 110L272 111L288 111L304 112L320 112L336 112L352 112L368 111L384 111L400 111L416 111L432 111L448 111L464 111L480 110' stroke-width='1.6' opacity='0.55'/%3E%3Cpath d='M0 114L16 114L32 114L48 114L64 114L80 114L96 113L112 113L128 113L144 112L160 112L176 112L192 113L208 113L224 113L240 113L256 114L272 114L288 114L304 114L320 114L336 115L352 115L368 115L384 116L400 116L416 116L432 115L448 115L464 115L480 114' stroke-width='1.6' opacity='0.8'/%3E%3Cpath d='M0 120L16 120L32 120L48 119L64 119L80 119L96 119L112 120L128 120L144 120L160 120L176 120L192 120L208 119L224 118L240 118L256 118L272 118L288 119L304 119L320 119L336 119L352 118L368 118L384 118L400 118L416 118L432 118L448 119L464 120L480 120' stroke-width='0.6' opacity='0.35'/%3E%3Cpath d='M0 124L16 123L32 124L48 124L64 124L80 124L96 123L112 123L128 123L144 122L160 122L176 122L192 122L208 122L224 122L240 122L256 122L272 122L288 122L304 122L320 122L336 123L352 123L368 123L384 124L400 124L416 124L432 124L448 124L464 124L480 124' stroke-width='0.8' opacity='0.8'/%3E%3Cpath d='M0 130L16 129L32 129L48 129L64 129L80 130L96 130L112 131L128 130L144 130L160 129L176 129L192 128L208 128L224 128L240 128L256 129L272 129L288 129L304 129L320 128L336 128L352 127L368 128L384 128L400 129L416 129L432 130L448 130L464 130L480 130' stroke-width='1.1' opacity='0.8'/%3E%3Cpath d='M0 133L16 133L32 133L48 134L64 134L80 135L96 136L112 136L128 135L144 135L160 134L176 133L192 133L208 133L224 133L240 133L256 133L272 133L288 132L304 132L320 131L336 130L352 130L368 131L384 131L400 132L416 133L432 133L448 133L464 133L480 133' stroke-width='0.8' opacity='0.8'/%3E%3Cpath d='M0 140L16 140L32 139L48 139L64 138L80 138L96 137L112 137L128 137L144 137L160 137L176 137L192 136L208 135L224 135L240 134L256 134L272 135L288 135L304 136L320 136L336 137L352 137L368 137L384 137L400 137L416 137L432 138L448 139L464 139L480 140' stroke-width='0.8' opacity='0.35'/%3E%3Cpath d='M0 149L16 149L32 149L48 149L64 149L80 150L96 150L112 149L128 149L144 148L160 148L176 147L192 147L208 147L224 147L240 147L256 147L272 147L288 147L304 147L320 146L336 146L352 147L368 147L384 148L400 148L416 149L432 149L448 149L464 149L480 149' transform='translate(0 -160)' stroke-width='0.8' opacity='0.35'/%3E%3Cpath d='M0 149L16 149L32 149L48 149L64 149L80 150L96 150L112 149L128 149L144 148L160 148L176 147L192 147L208 147L224 147L240 147L256 147L272 147L288 147L304 147L320 146L336 146L352 147L368 147L384 148L400 148L416 149L432 149L448 149L464 149L480 149' stroke-width='0.8' opacity='0.35'/%3E%3Cpath d='M0 154L16 154L32 154L48 154L64 154L80 154L96 153L112 153L128 152L144 151L160 151L176 150L192 150L208 150L224 150L240 150L256 150L272 150L288 150L304 150L320 150L336 151L352 151L368 152L384 153L400 153L416 154L432 154L448 154L464 154L480 154' transform='translate(0 -160)' stroke-width='1.1' opacity='0.55'/%3E%3Cpath d='M0 154L16 154L32 154L48 154L64 154L80 154L96 153L112 153L128 152L144 151L160 151L176 150L192 150L208 150L224 150L240 150L256 150L272 150L288 150L304 150L320 150L336 151L352 151L368 152L384 153L400 153L416 154L432 154L448 154L464 154L480 154' stroke-width='1.1' opacity='0.55'/%3E%3Cpath d='M0 154L16 153L32 154L48 154L64 154L80 155L96 155L112 155L128 154L144 153L160 153L176 153L192 154L208 154L224 155L240 156L256 157L272 156L288 156L304 156L320 155L336 155L352 155L368 156L384 157L400 157L416 157L432 156L448 156L464 155L480 154' transform='translate(0 -160)' stroke-width='0.8' opacity='0.55'/%3E%3Cpath d='M0 154L16 153L32 154L48 154L64 154L80 155L96 155L112 155L128 154L144 153L160 153L176 153L192 154L208 154L224 155L240 156L256 157L272 156L288 156L304 156L320 155L336 155L352 155L368 156L384 157L400 157L416 157L432 156L448 156L464 155L480 154' stroke-width='0.8' opacity='0.55'/%3E%3Cpath d='M0 167L16 167L32 167L48 168L64 168L80 168L96 167L112 167L128 167L144 166L160 165L176 165L192 165L208 165L224 165L240 165L256 165L272 165L288 164L304 164L320 164L336 165L352 165L368 165L384 166L400 167L416 167L432 167L448 167L464 167L480 167' transform='translate(0 -160)' stroke-width='1.1' opacity='0.35'/%3E%3Cpath d='M0 167L16 167L32 167L48 168L64 168L80 168L96 167L112 167L128 167L144 166L160 165L176 165L192 165L208 165L224 165L240 165L256 165L272 165L288 164L304 164L320 164L336 165L352 165L368 165L384 166L400 167L416 167L432 167L448 167L464 167L480 167' stroke-width='1.1' opacity='0.35'/%3E%3C/g%3E%3Cellipse cx='227' cy='88' rx='9' ry='4' fill='black' opacity='0.5'/%3E%3Cellipse cx='227' cy='88' rx='15' ry='7' fill='none' stroke='black' opacity='0.4'/%3E%3C/svg%3E"); }
```

- Careful: wood is for a plank, a sign, a rail: short words. On kraft (which leans to `--earth`) it reads as pine by day and dark oak at night. The tile repeats every 480 pixels; on a sheet wider than that the knot repeats, so a wide plank wants a second tile or the knot taken out.
- Light and dark: a pale board with brown lines; a dark board with pale lines.
- Personality: friendly, playful
- Goes with: `materials: sheet kraft` or `card`; `materials: fixing string` (the rail).
- Used on: 2 mockups: a night market and a fair-stall shop (an oak rail and a name plank, drawn there as faint stripes).

#### Brushed
- Id: brushed
- Status: draft
- Looks like: fine straight streaks one way: brushed steel or tin.
- Made with: noise stretched hard along one axis (`baseFrequency='0.002 0.75'`), turned into alpha.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form): the grain is its `::after`.

```css assemble
& { --materials-grain: var(--materials-tile-brushed); --materials-grain-size: 480px 240px; --materials-grain-k: 2.6; }
/* the tile (alpha only) is drawn by tests/parts/source/materials.py; copy it from tests/parts/materials.html if it is redrawn */
& { --materials-tile-brushed: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='480' height='240'%3E %3Cfilter id='n' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.002 0.75' numOctaves='2' seed='9' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2.6 0 0 0 -1.05'/%3E%3C/filter%3E %3Crect width='480' height='240' filter='url(%23n)'/%3E%3C/svg%3E"); }
```

- Careful: it reads as metal only with the metal sheet's sheen; on paper it looks like a scratched photocopy.
- Light and dark: pewter on a light page, gunmetal on a dark one.
- Personality: serious, dramatic
- Goes with: `materials: sheet metal`; `materials: fixing rivets`.
- Used on: no mockup yet. The game-style site drew its metal as smooth gradients.

#### Speckle
- Id: speckle
- Status: draft
- Looks like: sparse flecks over a slow, veined cloud: stone or slate (pale stone on a light page), or frost on glass.
- Made with: two tiles: noise with a steep threshold, so only the brightest points become flecks; and a large tile of thin veins (where `turbulence` noise crosses zero) over a faint cloud, so the surface is uneven like stone rather than even like paper.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form): the grain is its `::after`.

```css assemble
& { --materials-grain: var(--materials-tile-speckle); --materials-grain-size: 220px 220px;
  --materials-grain-2: var(--materials-tile-vein); --materials-grain-2-size: 560px 380px; --materials-grain-k: 3; }
/* the tile (alpha only) is drawn by tests/parts/source/materials.py; copy it from tests/parts/materials.html if it is redrawn */
& { --materials-tile-speckle: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E %3Cfilter id='n' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.42' numOctaves='2' seed='5' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9.0 0 0 0 -6.2'/%3E%3C/filter%3E %3Crect width='220' height='220' filter='url(%23n)'/%3E%3C/svg%3E"); }
& { --materials-tile-vein: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='560' height='380'%3E %3Cfilter id='v' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='turbulence' baseFrequency='0.006 0.011' numOctaves='4' seed='12' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -5 0 0 0 0.5'/%3E%3C/filter%3E %3Cfilter id='c' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.008' numOctaves='3' seed='3' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.8 0 0 0 -0.36'/%3E%3C/filter%3E %3Crect width='560' height='380' filter='url(%23c)'/%3E%3Crect width='560' height='380' filter='url(%23v)'/%3E%3C/svg%3E"); }
```

- Careful: with flecks alone the light page looked like speckled paper; the veins and cloud are what make it stone. On a dark sheet the light flecks could read as stars; with `ink: chalk` it is a slate, with glass it is frost. Keep it off any sheet that holds long reading.
- Light and dark: a pale veined stone on a light page; a slate with pale veins on a dark one.
- Personality: serious, dramatic
- Goes with: `materials: sheet plain` or `glass`; `materials: ink chalk`.
- Used on: 1 mockup: a dark, painterly joke site (grain over its stone; the words were on plain dark slabs).

#### Graph
- Id: graph
- Status: draft
- Looks like: a printed grid: a notebook page, an exercise book, a chart.
- Made with: lines every 18 pixels each way, in `--line` (not ink: printed rules are pale), at 0.85.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form): the grain is its `::after`.

```css assemble
.sheet { --materials-grain-ink: var(--line); }   /* printed rules are pale: --line, not the ink */
& { --materials-grain-op: 0.85;
  --materials-grain: repeating-linear-gradient(0deg, black 0 1px, transparent 1px 18px); --materials-grain-2: repeating-linear-gradient(90deg, black 0 1px, transparent 1px 18px); }
```

- Careful: the grid is under every word, so it uses `--line`, which is pale on a light page and dim on a dark one; it passed the check on both. A heavier line every fifth square looked like a table and was taken out.
- Light and dark: pale brown squares on a light page, grey ones on a dark page.
- Personality: calm, friendly
- Goes with: `materials: sheet fine-paper`; `materials: ink pencil`; `materials: fixing clips` or `tape`.
- Used on: 1 mockup: a field notebook (graph-paper pages).

### Fixing
- Layer: fixing
- Owns: how a sheet is laid on: what holds it (tape, pins, a clip, rivets, string from a rail), how far the paper turns, and the room the fixing needs.
- Default: none

#### None
- Id: none
- Status: draft
- Looks like: the sheet lies flat and square; nothing holds it.
- Made with: nothing.

```css assemble
/* fixing: none. The sheet lies flat and square; nothing holds it. */
```

- Careful: the only fixing for a form, a table or a page that must look exact.
- Light and dark: the same.
- Personality: any
- Goes with: `materials: sheet plain` or `fine-paper`.
- Used on: most sheets on most mockups.

#### Tape
- Id: tape
- Status: draft
- Looks like: two strips of see-through tape across the top corners; the paper turned a little.
- Made with: two strips on `.fix`, `--twine` at 45%, with torn ends cut by `clip-path`. The sheet casts its shadow as a filter, so the tape casts with it; the paper turns -0.8 degrees.

- Needs markup: `<span class="materials-fix" aria-hidden="true"></span>` in each sheet that is fixed, holding `<i class="materials-tape materials-tape-l"></i><i class="materials-tape materials-tape-r"></i>`

```css assemble
/* <span class="materials-fix" aria-hidden="true"><i class="materials-tape materials-tape-l"></i><i class="materials-tape materials-tape-r"></i></span> */
.sheet:has(> .materials-fix) { --materials-tilt: -0.8deg;
  box-shadow: none; filter: var(--drop-low, none); }   /* light's low shadow as a filter, so the tape casts with the paper; never both */
.materials-tape { width: 5.5rem; height: 1.6rem; top: -0.15rem; background: color-mix(in oklab, var(--materials-twine) 45%, transparent);
  clip-path: polygon(0 12%, 4% 0, 8% 14%, 12% 2%, 16% 12%, 20% 0, 80% 0, 84% 10%, 88% 0, 92% 12%, 96% 2%, 100% 10%,
    100% 88%, 96% 100%, 92% 86%, 88% 98%, 84% 88%, 80% 100%, 20% 100%, 16% 90%, 12% 100%, 8% 88%, 4% 100%, 0 90%); }
.materials-tape-l { left: -1.6rem; rotate: -38deg; }
.materials-tape-r { right: -1.6rem; rotate: 35deg; }
```

- Careful: the tape reaches 1.6rem past the sheet's sides: give the sheet that much margin, or the tape is cut off on a phone. Keep the first line of words below it. The filter makes the sheet a backdrop root, so tape and glass do not mix. Only the paper turns, never the words (the first shop turned the whole card and its words came out soft).
- Light and dark: a see-through tape a step darker than the sheet on a light page, a step lighter on a dark one.
- Personality: friendly, playful
- Goes with: `materials: sheet fine-paper` or `card`; `light: shadows paper-lift`; `frames: torn-paper`.
- Used on: 4 mockups: a soap maker's shop (taped cards), a field notebook (taped sheets), a volunteer page (a taped sticky note) and a repair café (three small pieces).

#### Pins
- Id: pins
- Status: draft
- Looks like: two pushpins at the top: a notice on a board.
- Made with: a small SVG symbol (a round brass head with a highlight in `--metal-lit` and a rim in `--metal-deep`) in `--metal`, used twice, each casting `filter: var(--drop-low)`; the paper turns 0.7 degrees.

- Needs markup: `<span class="materials-fix" aria-hidden="true"></span>` in each sheet that is fixed, holding `<svg class="materials-pin" viewBox="0 0 24 24" focusable="false"><use href="#materials-pin"/></svg>, twice`

```css assemble
/* <span class="materials-fix" aria-hidden="true"><svg class="materials-pin" viewBox="0 0 24 24" focusable="false"><use href="#materials-pin"/></svg> (twice)</span> */
.sheet:has(> .materials-fix) { --materials-tilt: 0.7deg; }
.materials-pin { top: 0.4rem; width: 1.6rem; height: 1.6rem; color: var(--metal, var(--mark)); filter: var(--drop-low, none); }
.materials-pin:first-child { left: 0.7rem; }
.materials-pin:last-child { right: 0.7rem; }
```

```html assemble
<symbol id="materials-pin" viewBox="0 0 24 24"><circle cx="12" cy="11" r="8" fill="currentColor"/><circle cx="12" cy="11" r="8" fill="none" style="stroke: var(--metal-deep, var(--ink))" stroke-opacity="0.6"/><ellipse cx="9.2" cy="8" rx="2.6" ry="2" style="fill: var(--metal-lit, var(--surface-raised))"/></symbol>
```

- Careful: the pins are decoration (`aria-hidden`); their colour is the metal, never the accent (that is for things to press) and never the danger red. Keep the shared `<symbol>` outside the swatches (or the page's repeated items), since copies strip ids. When the whole notice is the link, put the focus outline on the notice with an offset so the turned paper does not hide it.
- Light and dark: brass pins on both, the highlight brighter on a dark page.
- Personality: friendly, playful
- Goes with: `materials: sheet card`; `background: texture felt-weave`; `light: shadows crisp`.
- Used on: 2 mockups: a volunteer page (notices pinned to a felt board) and a repair café (notices pinned to the pegboard).

#### Clips
- Id: clips
- Status: draft
- Looks like: a bulldog clip gripping the top of the sheet: a list on a clipboard.
- Made with: an SVG symbol (a jaw and two wire handles), filled with `--metal-deep`, with a `--metal-lit` glint on the jaw: a dark brass clip on both pages. It casts `filter: var(--drop-low)`. The sheet does not turn: a clipped sheet hangs straight.

- Needs markup: `<span class="materials-fix" aria-hidden="true"></span>` in each sheet that is fixed, holding `<svg class="materials-clip" viewBox="0 0 64 44" focusable="false"><use href="#materials-clip"/></svg>`

```css assemble
/* <span class="materials-fix" aria-hidden="true"><svg class="materials-clip" viewBox="0 0 64 44" focusable="false"><use href="#materials-clip"/></svg></span> */
.sheet:has(> .materials-fix) { padding-top: calc(var(--pad, 1.5rem) + 0.75rem); }   /* room for the jaw, on top of density's padding */
.materials-clip { top: -1.6rem; left: 50%; translate: -50% 0; width: 5.25rem; color: var(--metal-deep, color-mix(in oklab, var(--ink) 82%, var(--surface))); filter: var(--drop-low, none); }
```

```html assemble
<symbol id="materials-clip" viewBox="0 0 64 44"><path d="M17 20L11 3h16l-4 17M47 20l6-17H37l4 17" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/><path d="M15 18h34l7 24H8Z" fill="currentColor"/><path d="M14 23h36" style="stroke: var(--metal-lit, var(--surface-raised))" stroke-opacity="0.6" stroke-width="1.5"/></symbol>
```

- Careful: the first drawing (a jaw wider at the top, handles in a loop) read as a shopping basket; the jaw must be wider at the bottom, with the two handles folded up apart.
- Light and dark: a dark brass clip on both; it stands off a light sheet more than a dark one.
- Personality: calm, friendly
- Goes with: `materials: sheet fine-paper`; `materials: grain graph`.
- Used on: no mockup yet.

#### Rivets
- Id: rivets
- Status: draft
- Looks like: a round rivet in each corner: a plate fixed to a wall or a machine, a pane in a frame.
- Made with: four radial gradients on `.fix`, each a bright dot, a body and a dark rim, in `--metal-lit`, `--metal` and `--metal-deep`.

- Needs markup: `<span class="materials-fix" aria-hidden="true"></span>` in each sheet that is fixed, with nothing inside it: the four rivets are its background; the sheet also turns only with a `.materials-mat`.

```css assemble
/* <span class="materials-fix" aria-hidden="true"></span>: the four rivets are its background */
.materials-fix { --materials-rv: var(--metal, var(--ink-soft)); --materials-rv-hi: var(--metal-lit, var(--surface-raised)); --materials-rv-lo: var(--metal-deep, var(--ink));
  background: radial-gradient(circle at 0.8rem 0.8rem, var(--materials-rv-hi) 0 1px, var(--materials-rv) 3px 5px, var(--materials-rv-lo) 5.5px 6.5px, transparent 7px),
    radial-gradient(circle at calc(100% - 0.8rem) 0.8rem, var(--materials-rv-hi) 0 1px, var(--materials-rv) 3px 5px, var(--materials-rv-lo) 5.5px 6.5px, transparent 7px),
    radial-gradient(circle at 0.8rem calc(100% - 0.8rem), var(--materials-rv-hi) 0 1px, var(--materials-rv) 3px 5px, var(--materials-rv-lo) 5.5px 6.5px, transparent 7px),
    radial-gradient(circle at calc(100% - 0.8rem) calc(100% - 0.8rem), var(--materials-rv-hi) 0 1px, var(--materials-rv) 3px 5px, var(--materials-rv-lo) 5.5px 6.5px, transparent 7px); }
```

- Careful: rivets sit in the padding; keep 1.5rem of it. Forced colours remove gradients (R22), so the rivets vanish there, which is fine: they are decoration. The heavy metal ring round a window is `frames: riveted-metal`, which brings its own rivets: pick one or the other, not both.
- Light and dark: gold rivets with a bright point on both.
- Personality: serious, dramatic, playful
- Goes with: `materials: sheet glass` or `metal`; `frames: riveted-metal`.
- Used on: 3 mockups: three versions of a game-style joke site (a rivet at each end of every name plate).

#### String
- Id: string
- Status: draft
- Looks like: a tag hung on a string from a wooden rail, through a punched hole with a ring round it. The tag hangs a little crooked from its hole.
- Made with: three pieces on `.fix`: the rail (a 0.7rem bar in `--earth` darkened towards the shadow colour, with wood lines), the string (2 pixels of `--twine`) and the hole (the ground showing through a ring). The paper turns 1.2 degrees about its hole.

- Needs markup: `<span class="materials-fix" aria-hidden="true"></span>` in each sheet that is fixed, holding `<i class="materials-rail"></i><i class="materials-string"></i><i class="materials-hole"></i>; a row of tags is <ul class="materials-tags"> with each <li class="sheet">`

```css assemble
/* <span class="materials-fix" aria-hidden="true"><i class="materials-rail"></i><i class="materials-string"></i><i class="materials-hole"></i></span>;
   a row of tags is <ul class="materials-tags"> with each <li class="sheet"> */
.sheet:has(> .materials-fix) { padding-top: calc(var(--pad, 1.5rem) + 0.9rem); --materials-tilt: -1.2deg; --materials-tilt-at: 50% 1.1rem; }
.materials-rail { top: -2.6rem; left: calc(var(--materials-gap, 1.25rem) / -2); right: calc(var(--materials-gap, 1.25rem) / -2); height: 0.7rem; box-shadow: var(--shadow-low, none);
  background: repeating-linear-gradient(179deg, transparent 0 2px, color-mix(in oklab, rgb(var(--shadow-rgb)) 30%, transparent) 2px 3px),
    color-mix(in oklab, var(--materials-brown) 75%, rgb(var(--shadow-rgb))); }
.materials-string { left: 50%; top: -2rem; width: 2px; height: 2.75rem; translate: -50% 0; background: var(--materials-twine); }
.materials-hole { left: 50%; top: 0.55rem; width: 1.2rem; height: 1.2rem; translate: -50% 0; border-radius: 50%;
  background: radial-gradient(circle, var(--ground) 0 0.24rem, color-mix(in oklab, var(--materials-twine) 60%, var(--materials-sheet, var(--surface))) 0.26rem 0.52rem, transparent 0.55rem); }
/* a list of tags: one rail across the top of every row, at any number of columns; one tag to a row on a phone */
.materials-tags { --materials-gap: 1.25rem; list-style: none; margin: 0; padding: 3rem 0 0; display: grid; gap: 3.75rem var(--materials-gap);
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 15rem), 1fr)); }
.materials-tags > .sheet:nth-child(2n) { --materials-tilt: 1deg; }
.materials-tags > .sheet:nth-child(3n) { --materials-tilt: -0.5deg; }
```

- Careful: **where the rail goes.** One rail runs across the top of every row of tags. Each tag draws its own length of rail, as wide as its column plus half the gap on each side, so the lengths meet along a row and every row has its rail however many columns there are; the row gap (3.75rem) leaves room for the rail and the string. On the night market only the first tag hung from a rail drawn once on the list, and with one tag to a row the rest hung from nothing. **On a phone, one tag to a row**: tags are at least 15rem wide, so a 390-pixel phone shows one. The first version said "two to a row on a phone", and at 390 pixels the tags' display names wrapped a word to a line. The tag turns, its words do not. When the whole tag is a link, stretch the link over the tag and put the focus outline on the tag with an offset.
- Light and dark: a dark oak rail and brown string on a light page; a dark rail with paler string on a dark one.
- Personality: friendly, playful
- Goes with: `materials: sheet kraft`, `card` or `canvas`; `light: shadows paper-lift`; `density: busy`.
- Used on: 4 mockups: a night market (an oak rail with tags on string), two versions of a fair-stall shop, and a repair café (manila tags on string from pegs).

### Wear
- Layer: wear
- Owns: age and handling: darkened edges, folds, stains, scratches. Always at the edges and corners, never across the words.
- Default: none

#### None
- Id: none
- Status: draft
- Looks like: new: nothing has happened to it yet.
- Made with: nothing.

```css assemble
/* wear: none. New: nothing has happened to it yet. */
```

- Careful: the right choice for a shop's products, which should look new, and for anything official.
- Light and dark: the same.
- Personality: any
- Goes with: any sheet.
- Used on: most sheets on most mockups.

#### Soft edges
- Id: soft-edges
- Status: draft
- Looks like: edges gone darker with age and hands; the middle still clean.
- Made with: two gradients in the body layer, darkest at each edge and gone by 1.5 to 1.75rem in, in the shadow colour; and on a dark page, a paler rubbed edge in `--texture-rgb` laid on the sheet itself, since dirt hardly shows on a dark sheet.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form): the wear is its `::before`.

```css assemble
& { --materials-wear: linear-gradient(90deg, black, transparent 1.75rem, transparent calc(100% - 1.75rem), black);
  --materials-wear-2: linear-gradient(black, transparent 1.5rem, transparent calc(100% - 1.5rem), black); }
/* on a dark sheet dirt hardly shows; the worn edge is rubbed paler instead, in the texture colour */
.sheet { --materials-worn: light-dark(transparent, rgb(var(--texture-rgb) / calc(var(--texture-strength) * 1.8)));
  --materials-wear-lit: linear-gradient(90deg, var(--materials-worn), transparent 1.5rem, transparent calc(100% - 1.5rem), var(--materials-worn)),
    linear-gradient(var(--materials-worn), transparent 1.25rem, transparent calc(100% - 1.25rem), var(--materials-worn)); }
```

- Careful: the darkening stays in the padding: keep 1.5rem of it. The first parchment drew this edge with an inset `box-shadow`; a shadow is the light part's, and forced colours remove it anyway; this is a stain, so it is a mask. On a dark page the darkening alone hardly showed, and drawn in the ink colour it glowed like frost; the rubbed edge is the texture colour at under a third, which reads as worn paper. `light-dark()` follows the colour scheme, so the lamplit tone (a dark scheme) gets the paler rim too: on lamplit parchment it reads as a bleached, handled edge inside the darkening.
- Light and dark: a brown-grey edge on a light page; a paler rubbed edge on a dark page; on lamplit parchment a dark edge with a bleached rim.
- Personality: dramatic, calm
- Goes with: `materials: sheet parchment`; `colour: tone lamplit`.
- Used on: 2 mockups: a dark, painterly joke site and a small shop with a dark lead (parchment with a darkened edge).

#### Creased
- Id: creased
- Status: draft
- Looks like: folded once each way and opened out again: a soft shade on one side of each fold and a hard line at it.
- Made with: two gradients, each a sharp line with a soft shade beside it, at 64% across and 46% down.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form): the wear is its `::before`.

```css assemble
& { --materials-wear: linear-gradient(90deg, transparent calc(64% - 9px), color-mix(in srgb, black 30%, transparent) calc(64% - 1px), black 64%, transparent calc(64% + 1.5px));
  --materials-wear-2: linear-gradient(180deg, transparent calc(46% - 9px), color-mix(in srgb, black 30%, transparent) calc(46% - 1px), black 46%, transparent calc(46% + 1.5px)); }
```

- Careful: the only wear that crosses the words; at this strength the check passes, but move the folds if a line of text sits exactly on one.
- Light and dark: a grey fold on a light page; a faint dark one on a dark page.
- Personality: friendly, calm
- Goes with: `materials: sheet fine-paper` or `kraft`; `materials: fixing clips`.
- Used on: no mockup yet.

#### Stained
- Id: stained
- Status: draft
- Looks like: a cup ring in one corner and a soft blot in another.
- Made with: two radial gradients: a ring near the bottom right corner and a soft blot at the top right.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form): the wear is its `::before`.

```css assemble
& { --materials-wear: radial-gradient(circle at calc(100% - 2.75rem) calc(100% - 2.5rem), transparent 1.85rem, color-mix(in srgb, black 55%, transparent) 1.95rem, black 2.05rem, transparent 2.2rem);
  --materials-wear-2: radial-gradient(ellipse 6rem 3.5rem at 100% 0, black, transparent); }
```

- Careful: the stains sit where the words do not: the bottom right of most sheets is empty (the button is on the left). On a sheet with a button on the right, move the ring.
- Light and dark: a brown ring on a light page; a dark one on a dark page.
- Personality: dramatic, playful
- Goes with: `materials: sheet parchment` or `kraft`.
- Used on: 2 mockups: a dark, painterly joke site and a small shop with a dark lead (parchment with mottled stains, there in the sheet's body).

#### Scuffed
- Id: scuffed
- Status: draft
- Looks like: fine scratches, mostly one way, worst at two corners rubbed by hands.
- Made with: a 300-pixel tile of short straight scratches (drawn by script, mostly at one angle, as a thing dragged across a table) and two soft corner rubs.

- Needs markup: `<span class="materials-mat" aria-hidden="true"></span>` as the first child of each sheet that shows the material (without it the sheet is flat in the material's colour, which suits a form): the wear is its `::before`.

```css assemble
& { --materials-wear: var(--materials-tile-scuff); --materials-wear-size: 300px 300px; --materials-wear-repeat: repeat;
  --materials-wear-2: radial-gradient(circle at 0 0, black, transparent 2.5rem), radial-gradient(circle at 100% 100%, black, transparent 2.5rem); }
/* the tile (alpha only) is drawn by tests/parts/source/materials.py; copy it from tests/parts/materials.html if it is redrawn */
& { --materials-tile-scuff: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cg stroke='black' stroke-width='0.8' stroke-linecap='round'%3E%3Cpath d='M211.4 190.4L217.1 164.7' opacity='0.4'/%3E%3Cpath d='M144.6 7.3L154.6 30.0' opacity='0.9'/%3E%3Cpath d='M154.4 170.6L166.8 168.7' opacity='0.4'/%3E%3Cpath d='M297.1 278.1L307.1 277.1' opacity='0.4'/%3E%3Cpath d='M40.3 204.3L56.7 201.8' opacity='0.6'/%3E%3Cpath d='M154.6 129.0L175.2 123.9' opacity='0.4'/%3E%3Cpath d='M190.2 12.3L205.8 9.2' opacity='0.6'/%3E%3Cpath d='M121.6 58.5L133.1 60.1' opacity='0.9'/%3E%3Cpath d='M237.7 97.1L261.9 109.6' opacity='0.9'/%3E%3Cpath d='M281.9 170.9L294.0 172.6' opacity='0.9'/%3E%3Cpath d='M294.8 241.4L317.2 231.8' opacity='0.4'/%3E%3Cpath d='M244.4 121.7L264.7 140.6' opacity='0.9'/%3E%3Cpath d='M208.4 230.2L231.3 223.1' opacity='0.4'/%3E%3Cpath d='M239.2 90.5L245.9 82.8' opacity='0.6'/%3E%3Cpath d='M297.2 270.8L326.3 271.7' opacity='0.6'/%3E%3Cpath d='M101.3 197.9L121.3 193.3' opacity='0.9'/%3E%3Cpath d='M23.1 154.4L31.2 147.6' opacity='0.6'/%3E%3Cpath d='M294.0 6.8L314.3 -0.4' opacity='0.9'/%3E%3Cpath d='M71.1 133.1L79.3 112.4' opacity='0.4'/%3E%3Cpath d='M29.5 75.3L55.5 65.0' opacity='0.9'/%3E%3Cpath d='M162.1 124.7L164.8 114.9' opacity='0.6'/%3E%3Cpath d='M242.9 22.9L261.7 13.2' opacity='0.4'/%3E%3Cpath d='M115.9 281.6L121.8 255.4' opacity='0.9'/%3E%3Cpath d='M183.4 17.6L208.3 31.9' opacity='0.6'/%3E%3Cpath d='M85.3 119.6L100.9 109.3' opacity='0.6'/%3E%3Cpath d='M168.2 85.1L191.4 90.2' opacity='0.6'/%3E%3Cpath d='M8.1 231.7L17.8 217.8' opacity='0.9'/%3E%3Cpath d='M117.0 269.3L135.5 253.3' opacity='0.4'/%3E%3Cpath d='M174.5 216.9L184.2 208.3' opacity='0.9'/%3E%3Cpath d='M143.3 292.0L155.3 297.9' opacity='0.9'/%3E%3Cpath d='M29.5 243.1L58.5 239.7' opacity='0.4'/%3E%3Cpath d='M181.1 34.5L200.2 24.1' opacity='0.6'/%3E%3Cpath d='M35.4 258.3L49.2 250.3' opacity='0.4'/%3E%3Cpath d='M200.4 136.7L214.0 135.0' opacity='0.9'/%3E%3C/g%3E%3C/svg%3E"); }
```

- Careful: scratches cross the words, thin and faint; on a pale sheet they show more than on a dark one.
- Light and dark: grey hairlines on a light page; quiet on a dark one.
- Personality: playful, dramatic
- Goes with: `materials: sheet card` or `glass`; `materials: fixing rivets` or `string`.
- Used on: no mockup yet.

### Ink
- Layer: ink
- Owns: how the marks sit on the material. Only headings and short labels change; reading text is always printed.
- Default: printed

#### Printed
- Id: printed
- Status: draft
- Looks like: clean, even ink: the words as set.
- Made with: nothing.

```css assemble
/* ink: printed. Clean, even ink: the words as set. */
```

- Careful: the only ink for reading text, forms and anything that must look exact.
- Light and dark: the same.
- Personality: any
- Goes with: any sheet.
- Used on: every mockup, for its reading text.

#### Stamped
- Id: stamped
- Status: draft
- Looks like: headings rubber-stamped: a little tilted, letters spaced a little, ink that missed in places and ran thin on one side.
- Made with: two masks on the heading, intersected: a noise tile with small holes (ink that did not take) and a slanting gradient that thins one side. The heading turns -1.5 degrees.

```css assemble
.sheet :is(h1, h2, h3) { width: fit-content; rotate: -1.5deg; transform-origin: 0 50%; letter-spacing: 0.04em;
  --materials-stamp: var(--materials-tile-knock) 0 0 / 200px 200px, linear-gradient(100deg, black 30%, color-mix(in srgb, black 55%, transparent) 75%, black);
  -webkit-mask: var(--materials-stamp); mask: var(--materials-stamp); -webkit-mask-composite: source-in; mask-composite: intersect; }
/* the tile (alpha only) is drawn by tests/parts/source/materials.py; copy it from tests/parts/materials.html if it is redrawn */
& { --materials-tile-knock: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E %3Cfilter id='n' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3' seed='8' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -7.0 0 0 0 4.9'/%3E%3C/filter%3E %3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E"); }
```

- Careful: headings only, at 1.25rem or more and a weight of 600 or more: a thin face loses whole strokes. Large holes (a coarse tile) made the heading look damaged; the holes are small. A "Full" stamp across a notice is also said in words.
- Light and dark: dark, broken ink on a light sheet; pale on a dark one.
- Personality: playful, friendly
- Goes with: `materials: sheet card` or `kraft`; `lettering: poster-face`.
- Used on: 2 mockups: a volunteer page (a stamp across a full event) and a repair café (stamped tags).

#### Letterpress
- Id: letterpress
- Status: draft
- Looks like: words pressed into the sheet: the wall of each letter's dent on the light's side in shade, a lit lip on the far side, the paper round each letter pushed down a little, and the ink a touch heavier, as pressed ink spreads.
- Made with: three text shadows (the inner shade, the lit lip, a three-pixel halo) whose offsets follow the light part's lit edge (`--hx`, `--hy`), so the press agrees with every other shadow on the page; a quarter-pixel stroke for the heavier ink; and the sheet leaned 12% towards `--fibre`, so the lit lip has something to be brighter than. On a dark page the shade and halo are in the shadow colour and the lip is faint ink.

```css assemble
.sheet :is(h1, h2, h3, p) { -webkit-text-stroke: 0.25px currentColor; text-shadow:
  calc(var(--hx, 1) * -0.6px) calc(var(--hy, 1) * -1px) 0 light-dark(color-mix(in oklab, var(--ink) 45%, transparent), color-mix(in oklab, rgb(var(--shadow-rgb)) 90%, transparent)),
  calc(var(--hx, 1) * 0.6px) calc(var(--hy, 1) * 1px) 0 light-dark(var(--surface-raised), color-mix(in oklab, var(--ink) 22%, transparent)),
  0 0 3px light-dark(color-mix(in oklab, var(--ink) 16%, transparent), color-mix(in oklab, rgb(var(--shadow-rgb)) 70%, transparent)); }
.sheet { --materials-sheet: color-mix(in oklab, var(--surface) 88%, var(--materials-fibre)); }   /* a lip needs a sheet a step below the brightest white */
```

- Careful: the first version (one faint shade, one lip) did not show on bright paper at all: a lip cannot be brighter than the brightest sheet. Now the bite shows at a glance and the words still pass the check, but it is a heading-and-short-text finish: on long reading the halo softens the letters. The quarter-pixel stroke changes how heavy the type looks, which is lettering's business; drop it if the face is already heavy. Printers' advice: deep impressions want thick cotton paper, so pair it with laid (R10, R11). Forced colours remove text shadows (R22), which costs nothing.
- Light and dark: a pressed, slightly heavy print on a light page; on a dark page the dark inner edge and halo, quieter.
- Personality: serious, calm
- Goes with: `materials: sheet fine-paper` or `card`; `materials: grain laid`; `lettering: sober-pair`.
- Used on: no mockup yet.

#### Chalk
- Id: chalk
- Status: draft
- Looks like: headings in chalk: rough strokes, broken where the surface did not take it.
- Made with: a noise mask stretched sideways (chalk drags along the stroke), with more holes than the stamp.

```css assemble
.sheet :is(h1, h2, h3) { -webkit-mask: var(--materials-tile-chalk) 0 0 / 160px 160px; mask: var(--materials-tile-chalk) 0 0 / 160px 160px; letter-spacing: 0.02em; }
/* the tile (alpha only) is drawn by tests/parts/source/materials.py; copy it from tests/parts/materials.html if it is redrawn */
& { --materials-tile-chalk: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E %3Cfilter id='n' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8 0.3' numOctaves='2' seed='2' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -4.5 0 0 0 3.25'/%3E%3C/filter%3E %3Crect width='160' height='160' filter='url(%23n)'/%3E%3C/svg%3E"); }
```

- Careful: headings only, large and bold. Chalk belongs on a dark sheet: on a light page it reads as charcoal. Chalk marks drawn on the wall round the sheets are the background part's drawings, not this.
- Light and dark: charcoal on a light sheet; chalk on a dark one (a slate, with `grain: speckle`).
- Personality: playful, dramatic
- Goes with: `materials: sheet plain`; `materials: grain speckle`; `lettering: hand-marks`.
- Used on: 1 mockup: a dark, painterly joke site (chalk marks on its wall; its words were printed).

#### Pencil
- Id: pencil
- Status: draft
- Looks like: headings in soft pencil, underlined by hand: graphite grey, a little broken.
- Made with: the heading in `--ink-soft` with a fine, even noise mask, and a two-pixel underline at 60%.

```css assemble
.sheet :is(h1, h2, h3) { color: var(--ink-soft); -webkit-mask: var(--materials-tile-pencil) 0 0 / 120px 120px; mask: var(--materials-tile-pencil) 0 0 / 120px 120px;
  text-decoration: underline 2px color-mix(in oklab, var(--ink-soft) 60%, transparent); text-underline-offset: 0.2em; }
/* the tile (alpha only) is drawn by tests/parts/source/materials.py; copy it from tests/parts/materials.html if it is redrawn */
& { --materials-tile-pencil: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E %3Cfilter id='n' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.4' numOctaves='1' seed='6' stitchTiles='stitch'/%3E %3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -3.2 0 0 0 2.75'/%3E%3C/filter%3E %3Crect width='120' height='120' filter='url(%23n)'/%3E%3C/svg%3E"); }
```

- Careful: `--ink-soft` passes 4.5 to 1 as text, but the mask takes a little off: keep pencil to headings at 1.25rem or more. A coarse mask (the stamp's) made pencil look stamped; graphite is fine and even.
- Light and dark: grey graphite on a light sheet; silver on a dark one.
- Personality: friendly, calm
- Goes with: `materials: sheet fine-paper`; `materials: grain graph`; `materials: fixing tape` or `clips`.
- Used on: 2 mockups: a soap maker's shop (pen lines and a little handwriting) and a field notebook (pencil notes).

## What the visitor's settings switch off

Every pick keeps these, and the swatch book has them: the glass option goes solid when the visitor asks for less transparency or more contrast (R13, R15, R21), and the Base switches the material layers off in forced colours and halves the turn on a phone.

With forced colours on, the system replaces colours and removes every shadow and gradient, but keeps `url()` images (R22), so a sheet would lose its shadow and keep its noise: here the material layers are switched off and the sheet takes a plain edge, so it is still a sheet and its words are in the system's colours. Nothing in this part moves.

## Starting points

### Fine paper
- Id: fine-paper
- Picks: sheet: fine-paper; grain: fibre
- Personality: serious, calm
- Looks like: quiet, printed, careful: a good sheet on a desk, with fibre you notice only close up. No tape, no tears, no tilt. The quietest material that is still a material; with `frames: none` and no shadow, see the fine-paper sheet's note.
- Used on: a poetry site, an observatory, a quiet gallery of pots.

### Paper and tape
- Id: paper-and-tape
- Picks: sheet: fine-paper; grain: fibre; fixing: tape; ink: pencil
- Personality: friendly, playful
- Looks like: made at a kitchen table by one person: a sheet taped in at the corners, a little crooked, its heading in pencil.
- Used on: a soap maker's shop (taped cards, kraft tags), a volunteer page (a taped sticky note).

### Cut paper on felt
- Id: cut-paper-on-felt
- Picks: sheet: card; fixing: pins
- Personality: friendly, playful
- Looks like: a club's notice board: card notices pinned up a little crooked. The felt is the background part's (`background: texture felt-weave`); the notices are this.
- Used on: a volunteer sign-up page (events as pinned notices on a felt board).

### Parchment and ink
- Id: parchment-and-ink
- Picks: sheet: parchment; grain: fibre; wear: soft-edges
- Personality: dramatic, calm
- Looks like: old, hand-written, worn at the edges: dim warm parchment with slow stains and darker edges, dark ink. Pick it with the colour part's lamplit tone.
- Used on: a dark, painterly joke site; two versions of a small shop with a dark lead; one look of a game-style joke site.

### Stone and chalk
- Id: stone-and-chalk
- Picks: sheet: plain; grain: speckle; wear: scuffed; ink: chalk
- Personality: dramatic, playful
- Looks like: a slab someone has chalked on: on a dark or lamplit page a slate, dark and flecked with pale veins; on a light page a pale veined stone with the headings in charcoal. Printed words, chalked headings. The wall of dressed stone behind it is the background part's (`background: pattern stone-courses`). The first version kept the words off the stone on a plain slab; the slab is now the stone. Looked at both ways, the dark slate is the stronger, so the colour part's dark or lamplit tone suits it best; on a light page it is a fair pale stone, no longer speckled paper.
- Used on: a dark, painterly joke site (a stone wall, chalk on it, words on dark slabs).

### Wood and canvas
- Id: wood-and-canvas
- Picks: sheet: canvas; grain: weave; fixing: string
- Personality: friendly, playful
- Looks like: a market stall: canvas tags hung on string from an oak rail, one rail across the top of every row, one tag to a row on a phone. The striped valance over the stall is `frames: wavy-edge`.
- Used on: a night market; two versions of a fair-stall shop.

### Metal and dark glass
- Id: metal-and-dark-glass
- Picks: sheet: glass; fixing: rivets
- Personality: playful, dramatic
- Looks like: a game's interface: smoked glass panes with a rivet at each corner, over a painted world. The heavy metal ring round the main window is `frames: riveted-metal`; the metal's gold or steel is the colour part's.
- Used on: three versions of a game-style joke site.

### Warm
- Id: warm
- Picks: sheet: card; grain: fibre; fixing: tape; ink: stamped
- Personality: friendly, playful
- Looks like: somebody's hand is visible: card with fibre in it, taped up crooked, its heading stamped.
- Used on: the warm guide ("that somebody's hand is visible"; cut paper, tape, stamps).

### Sorcery
- Id: sorcery
- Picks: sheet: parchment; grain: fibre; fixing: pins; wear: stained
- Personality: dramatic
- Looks like: stained parchment nailed up in a dark room: a cup ring, a blot, two dark nail heads. With the colour part's sorcery start it is dim lamplit parchment in a night-blue hall.
- Used on: the sorcery guide ("aged parchment, and ink ... stained and uneven at the edges"); a dark, painterly joke site.

### Gilded dark
- Id: gilded-dark
- Picks: sheet: glass; grain: speckle; fixing: rivets; wear: scuffed
- Personality: dramatic, playful
- Looks like: battered glass panes in riveted frames: frosted, scratched, well used.
- Used on: the game-interface guide (dark, slightly see-through panels edged in metal); a game-style joke site.

### Lantern fair
- Id: lantern-fair
- Picks: sheet: kraft; grain: fibre; fixing: string; ink: stamped
- Personality: friendly, dramatic
- Looks like: brown paper tags on string at a night market, their names stamped. On the colour part's lantern-fair start (lamplit, wine neutrals) the tags are the lamplit sheet's own brown, darker.
- Used on: a night market (tags on string under one lantern); two versions of a small shop with a dark lead.

### Almanac plate
- Id: almanac-plate
- Picks: sheet: fine-paper; grain: laid; ink: letterpress
- Personality: serious, calm
- Looks like: a printed plate from an old almanac: laid paper, its words pressed in, under the visitor's own sky.
- Used on: an observatory mockup (printed charts on fine paper).

### Catalogue of glazes
- Id: catalogue-of-glazes
- Picks: sheet: card
- Personality: calm, serious
- Looks like: a museum label: plain matte card, short words, nothing else. The colour is in the pots.
- Used on: a quiet gallery of pots; museum label practice (short, plain labels on non-glare card, R12).

### Field journal
- Id: field-journal
- Picks: sheet: fine-paper; grain: graph; fixing: clips; wear: creased; ink: pencil
- Personality: calm, friendly
- Looks like: a notebook page on graph paper clipped to a board, folded once in a pocket, its heading in pencil.
- Used on: a field-notebook mockup (graph paper, pencil, taped sheets; swap `fixing: tape` for the taped look).

### Repair cafe
- Id: repair-cafe
- Picks: sheet: card; grain: fibre; fixing: string; wear: scuffed; ink: stamped
- Personality: playful, friendly
- Looks like: manila repair tags, handled and stamped, on string. The yellow pegboard behind them is the background part's; the notices on it are `{"start": "repair-cafe", "fixing": "pins", "wear": "none"}`.
- Used on: a repair-café mockup (manila tags on string, paper notices with pins and tape on a pegboard).

## Swatch book

`tests/parts/materials.html` shows every option of every layer, then every starting point, each on a light page and a dark one side by side; open it in a browser to choose by eye. Every swatch is one sheet with a heading, a line of text, a line of soft text and a button, on a ground with a disc and stripes behind it (so glass has a world to blur), so the material is the only thing that changes. Each sheet is shown with the grain it is usually seen with, and each grain, wear and ink on the sheet it suits (named under the swatch's title). After the starting points, a row of canvas tags on string shows where the rail goes at every width. It borrows the light part's warm start (top left, paper lift) and draws no border. It writes the layer classes short (`s-kraft` for sheet: kraft, and `g-`, `f-`, `w-`, `i-` for the others) and the material's elements as `.mat` and `.fix`; the assembly blocks are the same code under the part's own names (`.materials-mat`, `.materials-fix`, `--materials-...`), with each option's values on the page root or the sheet instead of a class. It is built by `tests/parts/source/materials.py` from `materials-template.html` beside it; run `python3 materials.py ../materials.html` there to rebuild it. The lamplit tone was checked by eye and by `audit` on a copy with the colour part's sorcery values (parchment reads right leaning towards `--line`, kraft towards `--earth`; glass failed and is marked not for lamplit; kraft's soft text sits at the limit).

## Not covered yet

- **Cork, leather and wood as whole sheets.** `--earth` makes them possible (a cork board is kraft with speckle); none is a sheet here yet.
- **Coloured papers.** The volunteer page's notices were five pastel papers; colour owns colour, and the five would be colour's bands or a new name. Until then, card is one colour per page.
- **Brick, concrete, plastic, leather, felt as a sheet**, and photographed textures. Every material here is drawn in CSS and small SVG tiles.
- **Print**, and **real phones**: looked at in a desktop browser at phone width only; the tiles are small and drawn once, but fifteen glass panes on a slow phone were not tried.
- **Riso and misregistration** (two inks a pixel or two apart, R11) as an ink: seen in research, not yet tried on a heading.
- **Wear that tells a story** (a coffee ring where a hand rests, tape marks where a sheet was moved). The stains here are in fixed places.

## Sources

Read on 2026-10-07. Six kinds of source: writing on flat and skeuomorphic design (R1 to R3), craft writing on textures in CSS and SVG (R4 to R9), print and craft traditions (R10 to R12), how app and game interfaces suggest materials (R13 to R16), speed (R17 to R19), and accessibility (R20 to R22). The mockups made with the skill are the seventh: their CSS and their skill feedback are quoted in each option's "Used on" and "Careful". Pages that would not open or were read only from a search result: Material's material-properties page (only its "1dp thickness" read), Apple's materials page, the V&A label guide (a PDF), the Smithsonian accessible design guide (a PDF), and a Codrops texture article; each is marked below.

- R1 Nielsen Norman Group, flat UI elements attract less attention and cause uncertainty (71 people, 9 pairs of pages; weak signs of clickability: 22% more time, 25% more looks): nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/
- R2 Nielsen Norman Group, flat design: its origins, its problems (skeuomorphism borrows real-world knowledge; "flat 2.0": subtle shadows, highlights and layers): nngroup.com/articles/flat-design/
- R3 Material Design 2, material properties (every surface a sheet 1dp thick; depth by elevation; partly read): m2.material.io/design/environment/material-properties.html
- R4 Codrops, creating texture with feTurbulence (paper from turbulence and lighting; would not open, from search): tympanus.net/codrops/2019/02/19/svg-filter-effects-creating-texture-with-feturbulence/
- R5 CSS-Tricks, grainy gradients (`fractalNoise`, `baseFrequency` 0.65, `numOctaves` 3, `stitchTiles='stitch'`; a commenter on its cost): css-tricks.com/grainy-gradients/
- R6 freeCodeCamp, grainy CSS backgrounds using SVG filters (PNG, file or data URI; higher frequency, finer grain), with a noise generator's advice that grain at 0.03 to 0.12 reads as texture and over 0.15 as dirt (cssmatic.com/gen-noise-texture.html, a weak source): freecodecamp.org/news/grainy-css-backgrounds-using-svg-filters/
- R7 Josh Comeau, next-level frosted glass with backdrop-filter (16px blur; a nearly opaque fallback in `@supports`; browser bugs with clipped parents): joshwcomeau.com/css/backdrop-filter/
- R8 Lea Verou, CSS3 patterns gallery (weave, lined paper and grids from gradients alone, "to make page loading faster"): projects.verou.me/css3patterns/
- R9 the same frosted-glass article and Windows' acrylic page: 8 to 16 pixels of blur; beyond about 20 nobody sees a difference (see R13, R19)
- R10 4over4, what paper types work best for letterpress (cotton stock of 300gsm and over takes a deep impression), and how colour prints on kraft paper (darker, warmer, lower in contrast): 4over4.com/faqs/general/what-paper-types-work-best-for-letterpress and v2.4over4.com/guide/how-color-prints-on-kraft-paper-what-to-expect-and-what-to-avoid
- R11 Briar Press, how do I get a deeper impression (fibres pressed, not punched), and Moniker Press's risograph guide (layers 1 to 2mm apart; ink sitting on the paper): briarpress.org/31071 and monikerpress.ca/printing
- R12 V&A gallery text guide and the Smithsonian guidelines for accessible exhibition design (short, plain labels; non-glare surfaces; no condensed or light type; read from search results): vam.ac.uk/blog/museum-life/getting-it-write
- R13 Microsoft, acrylic material (background, blur, tint, noise; short-lived surfaces only; never stacked; solid with transparency off, battery saver or high contrast; no accent text on it): learn.microsoft.com/en-us/windows/apps/design/style/acrylic
- R14 Microsoft, Mica material (opaque, samples the wallpaper once for speed; once per app; a solid fallback): learn.microsoft.com/en-us/windows/apps/design/style/mica
- R15 Apple Human Interface Guidelines, materials (thicker materials push the background further back; respect Reduce Transparency; from search): developer.apple.com/design/human-interface-guidelines/materials
- R16 nine-slice guides (ornate corners fixed, edges stretched, a plain centre: how game panels carry their material; on the web, `border-image`), and a study of players preferring interfaces built into the game world: generalistprogrammer.com/tutorials/nine-slice-scaling-explained and diglib.eg.org/handle/10.2312/egve20211333
- R17 WebKit bug 5864 (turbulence "could be very expensive on repaint"): bugs.webkit.org/show_bug.cgi?id=5864
- R18 web.dev, stick to compositor-only properties and manage layer count (only transform and opacity animate cheaply; do not promote layers needlessly), and MDN on will-change (a last resort): web.dev/articles/stick-to-compositor-only-properties-and-manage-layer-count
- R19 a lint rule on large animated blurs (backdrop-filter is the costliest common property; area matters more than count; a weak source): react.doctor/prompts/rules/react-doctor/no-large-animated-blur.md
- R20 WCAG 2.2, contrast minimum (4.5 to 1, 3 to 1 for large text; failure F83, a background image without enough contrast) and non-text contrast (3 to 1): w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- R21 MDN, prefers-reduced-transparency (not yet in every major browser; follows the Windows and Apple settings) and prefers-contrast: developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-transparency
- R22 MDN, forced-colors (box-shadow and text-shadow forced to none, gradients removed, `url()` images kept, colours replaced): developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors
