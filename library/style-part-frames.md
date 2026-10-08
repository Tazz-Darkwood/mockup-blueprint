---
name: Frames and edges (a part guide)
summary: Every line and edge drawn on a page - the border round a sheet, the edge of the sheet itself, the edge between two sections, ornament on a border, the dividers between items and the edge of a field - in layers that switch on their own, from no line at all to torn parchment inked round or a gilded ring with a jewel. Each layer works on a light page and a dark one, and can be picked with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: research online (six kinds of source, listed under Sources), a test of SVG border images in the browser, the frames of 15 mockups made with the skill and their feedback, and the feel guides named in each option
---

# Frames and edges

A part guide. It covers every line and edge drawn on a page: the border round a sheet, a panel or a control; the outline of the sheet itself (straight, cut, torn); the edge where one section meets the next; pieces set on a border (corner pieces, studs, a jewel); and the dividers between items. It is made of six layers, each one decision that switches on its own: **border**, **edge**, **section edge**, **ornament**, **dividers** and **controls**. A site picks a starting point whole, or a starting point with one layer changed, in its own guide and in the blueprint as `project.style.parts`: `{"frames": "torn-paper"}`, or `{"frames": {"start": "sorcery", "ornament": "none"}}`. The pick wins over the feel guide for lines and edges only. The general guide's accessibility minimums still hold whatever is picked.

**This part owns border width and style, and every edge** (the owners table in the general guide). It does not own:

- **Colour.** Every line is drawn with the shared colour names: `--line` for dividers and decorative borders, `--ink-soft` (or `--ink`) for the edge of a field or tick box, because `--line` does not reach 3 to 1 and the edge of a control must (WCAG 1.4.11, F26), and `--accent-edge` for the border of an accent button. Ornament and metal take `--mark`, the colour for drawn decoration.
- **Shadows.** A sheet's shadow is the light part's: `box-shadow: var(--shadow-low)` on a straight sheet, `filter: var(--drop-low)` on a torn, cut or deckled one. A hard offset shadow under an inked panel is the light part's `crisp` shadows, not a border.
- **Corner radius and small shapes.** Corners come from the corners and shapes part as `var(--radius, 0)`; the outline of buttons, tags and badges is that part's too. This part only follows the radius it is given.
- **Spacing.** Density sets the padding of a sheet and the gaps between items. A thick frame adds its own width to that padding (a 9-pixel ring adds 9 pixels), so the words keep the room density gave them.

So a fine-paper sheet under `border: none` has no border, whatever the material's own recipe once said (the quiet gallery met this, and its review said "I let frames win"); and when torn paper and taped paper ask for different shadows, the light part's is used.

**Frames never go round fields or buttons.** A field keeps a plain border (the controls layer below) so that it looks like a field and nothing else; a button keeps `border: 2px solid var(--accent-edge)` (the width and style here, in Base; the colour from the colour part). The frame goes round the form's sheet. The artistic and sorcery guides say the same: no decoration on navigation, buttons, fields, menus or dialogs.

## How it is built

Each option's code is a ` ```css assemble ` block that `blueprint.py style css` lifts into a site's stylesheet as it is (the general guide's "Writing a part's code to be lifted out"). It styles only the shared hooks (`.sheet`, `.panel`, `.band`, `.rule`, `.field`) and plain elements, plus one class of this part's own, `.frames-ornament`; it sets only this part's own values (`--frames-…`) on the page root, and an option that must agree with another layer (studs that sit in a metal ring, an outline that follows a torn edge) reads a value the other layer sets. Each thing has one place it is drawn, so layers never fight over the same pseudo-element:

| What | Drawn on | Why there |
|---|---|---|
| A plain border (none, hairline, rule, inked) | the sheet's own `border` | it survives forced colours, and needs nothing else |
| A ring border (double, pen line, carved band, metal ring) | the sheet's `::after`, laid over the border area | the words are not touched, and a mask can hollow it out |
| A shaped edge (cut, torn, deckled) | the sheet's `::before`, which paints the material's `var(--sheet-fill)` through the shape `--sheet-mask`; the border is redrawn along the shape on its `::after` | the sheet itself is never cut, so its shadow (the light part's, as a `filter`) and the tape or pins that overhang it stay whole; the materials part's texture span takes the same mask; the words are not turned |
| A button's edge | the button's own `border`, 2 pixels wide (Base); its colour is the colour part's (`--accent-edge` on the main button) | a cut button's shape and edge are the shapes part's, on the button's `::before` and `::after`, which this part never uses |
| Ornament | one empty `<span class="frames-ornament" aria-hidden="true">` inside the sheet or panel | it can sit over the ring and past the edge |
| The edge between sections | the lower band's `::before`, poking up over the seam in the band's own colour | it belongs to the section it is the edge of, and needs no extra element |
| Dividers | the item's `border-top`, or its `::before`; an `<hr class="rule">` | between items only (`li + li`) |

The part's own names, made from the shared ones, are set once on the page root (under Base below): `--frames-line` (hairlines and dividers), `--frames-strong` (a rule that must be seen: double, dashed, crop marks), `--frames-metal`, `--frames-metal-lit` and `--frames-metal-deep` (metal and gilt), `--frames-edge-ink` and `--frames-edge-width` (the border as an outline on a shaped sheet, set by the border layer) and `--frames-field-edge` (set by the controls layer). The sheet's fill, shadow, radius and padding are other parts': padding is read as `var(--pad, 1.25rem)`, corners as `var(--radius, 0)`.

Metal and gilt read the shared `--metal`, `--metal-lit` and `--metal-deep`, which the colour part sets, and fall back to mixes of `--mark` until it does (`light-dark()` picks a pale tone on either page, so metal catches light on both). This part never sets them itself, so the colour part's values always win.

**Why not SVG border images.** Several mockups drew their frames as an SVG file used as `border-image` (a nine-slice: four corners kept whole, four sides repeated, the middle dropped, F12, F13, F30). It works, but an SVG used as an image cannot read the page's custom properties, so its colour is fixed: one file per colour, and a dark page needs another. Every option here is drawn in CSS from the shared names instead. When a site does use an SVG `border-image` (a hand-drawn frame no CSS can make), three things were met and tested:

- **Give the SVG a `width` and `height`, or slice in percent.** With only a `viewBox`, the image has no size of its own, so its pixels are counted at the size of the box it decorates (F14). A slice of `32` then cuts 32 pixels from a picture the size of the whole panel: the corners shrink to nothing and the sides break into gaps. Tested for this guide in Chromium: a 96-unit frame with `width='96' height='96'` and `slice 32` draws correctly; the same file with only a `viewBox` draws blobs; with only a `viewBox` and `slice 33.3%` it draws correctly again. Two mockups still carry the broken kind (a soap shop's pen frame, the gold and silver frames of a game-style joke site).
- **`border-image` ignores `border-radius`** (F10, F12), and it needs a real `border-style` and width or some browsers draw nothing (F12). Add `background-clip: padding-box`, or the background shows through the transparent border.
- **Forced colours keep `border-image`** (it is not one of the properties the browser overrides, F17), so a frame drawn in fixed colours stays in a high-contrast theme. Set `border-image: none` there.

`mask-border`, the same nine-slice used as a mask (which would let a CSS colour show through an SVG frame), is not yet in every browser (F15); do not rely on it.

## Choosing

Start from a starting point (below), then change a layer if the brief asks for it.

| Starting point | What it feels like | Suits best | Fights |
|---|---|---|---|
| None | Calm and printed: space does the grouping, a printer's mark between items | Artistic, when the work is the frame; a booklet | A busy page, where groups blur without a line |
| Hairline | Orderly and exact, like a well-set form | Professional | Warm: it reads as cold |
| Card | Tidy and familiar; the light and the corners do the work | A panel holding a form or a summary | Warm and artistic as the repeated item: it is the template's card |
| Torn paper | Made by hand, pinned up | Warm, artistic | Professional |
| Inked panel | Bold and printed, like a comic page or a woodcut | Artistic; a dark, painterly lead | Professional |
| Carved plate | Old and precious, framed as a work | A shop's product pictures; a dark, painterly lead | Professional; a bright warm page |
| Riveted metal | A game's interface: heavy and shiny | A game-style site | Almost everything else, and any page meant for long reading |
| Wavy edge | Soft and playful between sections | Warm; a game-style site | Professional |
| Warm | Cut paper, a torn band, dashed lines | The warm guide; a volunteer group | A dark lead |
| Artistic | One pen-drawn frame, printer's marks | The artistic guide | Shops' grids, where every item gets the frame |
| Professional | A ledger: a heavy rule over, thin ones under | The professional guide | Warm, hand-made |
| Civic | Almost nothing drawn; fields with a firm edge | Public services, forms | Anything meant to feel crafted |
| Sorcery | Torn parchment inked round, a carved band below | The dark, painterly guide | Anything bright |
| Gilded dark | A gilded ring with a jewel, over a rolling land | The game-interface guide | Calm or official sites |
| Lantern fair | An awning's scallops over the stalls | A night market; a shop with a dark lead | Daytime services |
| Almanac plate | A printed plate: hairlines, crop marks, a skyline traced in ink | A society, an observatory, a garden | Shops |
| Catalogue of glazes | Nothing drawn at all | A gallery that lets its pieces speak | A page of many small items |
| Field journal | Torn-out pages, ruled lines in the log | A walking club, a naturalist | Professional |
| Repair cafe | Cut card pinned up, a strip of pattern, firm edges | A bright community page | A calm brief |

How to choose:

- **Ask what the repeated item is made of when it is not on a screen** (a notice, a print, a plate in a book, a window in a game), and pick the frame that object has.
- **Space first.** Try grouping with space before any line (the general guide's "Use space before lines and boxes"; GOV.UK's section break is "only visible by its margin" until you ask for the line, F5). Add a border when space alone does not make the group clear.
- **One frame, on the one thing.** A frame on everything is no longer a frame: put it on the thing each section is about, and let the rest sit on space. The sorcery guide: "One kind of frame for the site." Most sites need one border, one kind of section edge and one divider.
- **One weight of line.** Print keeps its rules between half a point and one point, "Thicker borders are counterproductive" (F18); design systems give one width (1 pixel) to every standard border and divider, and 2 only to what is selected or focused (F2, F1). The heavy options here (inked, carved, metal) are for frames that are meant to be seen as frames, not for every line.

## Base

Code every pick needs, whatever is picked: the part's own names, made from the shared ones; the place an ornament sits; the edge every field takes; and what the visitor's settings change.

```css assemble
& { --frames-line: var(--line);                                               /* hairlines and dividers */
  --frames-strong: color-mix(in oklab, var(--line), var(--ink) 45%);              /* a rule that must be seen: double, dashed, crop marks */
  --frames-metal: var(--metal, var(--mark));                                      /* the colour part's metal, or the mark colour until it sets one */
  --frames-metal-lit: var(--metal-lit, color-mix(in oklab, var(--metal, var(--mark)) 40%, light-dark(var(--surface-raised), var(--ink))));
  --frames-metal-deep: var(--metal-deep, color-mix(in oklab, var(--metal, var(--mark)) 45%, rgb(var(--shadow-rgb))));
  --frames-edge-ink: transparent; --frames-edge-width: 0px;                       /* the border as an outline on a shaped sheet: set by the border */
  --frames-field-edge: 1px solid var(--ink-soft); }                               /* set by the controls layer */
:is(.sheet, .panel) { position: relative; isolation: isolate; }
.btn { border-style: solid; border-width: 2px; }   /* a button's edge: the colour part gives its colour (--accent-edge on the main one); a cut button's edge is the shapes part's */
.frames-ornament { position: absolute; pointer-events: none; z-index: 2; }
:is(.field, select, textarea, input:not([type="submit"], [type="button"], [type="reset"], [type="image"], [type="range"], [type="color"], [type="file"])) { border: var(--frames-field-edge); }
.rule { border: 0; margin-inline: 0; }   /* a divider in running text: the dividers layer draws it */
@media (forced-colors: active) {   /* the browser drops gradients, masks' pictures and shadows, and paints every border in CanvasText */
  :is(.sheet, .panel) { border: 1px solid CanvasText; mask: none; filter: none; }
  .sheet::before { mask: none; }   /* a shaped sheet's paper is a plain box again */
  :is(.sheet, .panel)::after, .frames-ornament, .band::before { display: none; }
  .rule { border-top: 1px solid CanvasText; }
}
@media (prefers-contrast: more) {
  & { --frames-line: var(--frames-strong); }
}
```

## Layers

### Border
- Layer: border
- Owns: the line round a sheet or panel: its width, its style and whether it is one line or a ring. Not its colour (the colour part) or its corners (corners and shapes).
- Default: none

#### None
- Id: none
- Status: draft
- Looks like: no line. The sheet is told from the ground by its colour, its shadow (the light part's) and the space round it. Reading text on it stays left-aligned; only a printer's mark between items is centred (the first swatch book centred everything, and the quiet gallery's review caught it).
- Made with: a transparent border one pixel wide. It draws nothing, but in forced colours (Windows high contrast) the browser paints every border in the text colour, transparent ones included, and drops every shadow and background picture (F17, F11); so the sheet keeps an edge there with no extra rule. The light part asked for exactly this: "a raised sheet with no border becomes invisible: frames must give it an edge there."

```css assemble
:is(.sheet, .panel) { border: 1px solid transparent; }   /* seen only in forced colours, where the sheet needs an edge */
```

- Careful: `border: none` loses the forced-colours edge; keep the transparent one (F11). On a pale ground with a white sheet and no shadow, the sheet can vanish; give it a colour a clear step from the ground (the colour part's toned tone) or pick a hairline.
- Light and dark: on a dark page a sheet with no line relies on `--surface` against `--ground` and the light part's lit edge; check it there first.
- Personality: calm, serious, any
- Goes with: `frames: dividers space` or `ornament`; `light: shadows soft` or `none`; `materials: fine-paper`.
- Used on: 4 mockups: a quiet gallery of pots (no borders at all, "pots are drawn flat"), a night market ("the material does the framing"), a volunteer page and a repair café (paper sheets told apart by colour and shadow).

#### Hairline
- Id: hairline
- Status: draft
- Looks like: one thin line all round, in the line colour. Exact and quiet, like a well-set form or a specimen label.
- Made with: a one-pixel border in `--line`, the width every design system gives its standard borders (F2, F1, F7).

```css assemble
:is(.sheet, .panel) { border: 1px solid var(--frames-line); }
& { --frames-edge-ink: var(--frames-strong); --frames-edge-width: 1px; }   /* on a shaped sheet */
```

- Careful: `--line` is a decorative colour and is not 3 to 1; a hairline that shows where something can be pressed or typed in needs the controls layer's edge, not this. A specimen label (the meridian mockup) may draw its hairline in `--ink` for a sharper print look.
- Light and dark: the dark page's `--line` is a soft grey-violet and reads well; on a light page it is a pale fawn line, fine against a white sheet, faint against a cream one.
- Personality: serious, calm
- Goes with: `frames: dividers hairline`; `light: shadows none` or `soft`; `materials: fine-paper`.
- Used on: 5 mockups: an observatory (cream sheets with a hairline over a starry sky), a tutor's site, a 3D game's pages, a poetry site (its quiet look), a soap shop.

#### Rule
- Id: rule
- Status: draft
- Looks like: a ledger or a table of figures: a heavy rule across the top of the sheet and a hairline round the rest. The heavy line says "a new group starts here".
- Made with: two borders. The professional mockups wrote it as two tokens, `--rule` and `--rule-heavy`.

```css assemble
:is(.sheet, .panel) { border: 1px solid var(--frames-line); border-top: 4px solid var(--ink); }
& { --frames-edge-ink: var(--frames-strong); --frames-edge-width: 1px; }
@media (forced-colors: active) { :is(.sheet, .panel) { border-top-width: 4px; } }
```

- Careful: four pixels is the top of the scale (USWDS's border widths go 1, 2, 4, 8, F4); heavier and it reads as a coloured bar, which is the template's "card with a thin coloured bar" the warm guide warns against. The heavy rule is ink, never the accent: the accent means "press this".
- Light and dark: on a dark page the heavy rule is the pale ink: a bright line across a dark sheet, stronger than on light. That is right for a ledger; soften it with `--frames-strong` if it shouts.
- Personality: serious
- Goes with: `frames: dividers hairline` or `double-rule`; `frames: controls firm`.
- Used on: 3 mockups: a tutor's site ("Ruled rows and columns; one corner size", which the owner called "way better, cleaner for sure"), an art-paint site (figures and steps under a heavy rule), an observatory (facts under a heavy rule).

#### Double
- Id: double
- Status: draft
- Looks like: a heavy line and a thin one just inside it, like the frame round a plate in an old book or a certificate. In print, a thick and a thin rule side by side is the Oxford rule (F23).
- Made with: the sheet's border is the heavy line; a thin line on `::after`, three pixels inside it. Not `border-style: double`, which splits one width into two equal lines (F16) and cannot be thick and thin. Not an `outline` pulled inside with a negative offset: one shop did that, and it took the outline away from focus.

```css assemble
:is(.sheet, .panel) { border: 3px solid var(--frames-strong); padding: calc(var(--pad, 1.25rem) + 4px); }
:is(.sheet, .panel)::after { content: ""; position: absolute; inset: 3px; pointer-events: none;
  border: 1px solid var(--frames-strong); border-radius: max(0px, calc(var(--radius, 0px) - 6px)); }
& { --frames-edge-ink: var(--frames-strong); --frames-edge-width: 1px; --frames-ring: 4px; }
@media (forced-colors: active) { :is(.sheet, .panel) { border-width: 3px; } }
```

- Careful: the inner line's corners must be the outer radius less the gap, or they bulge. In forced colours only the outer line stays, which is enough.
- Light and dark: the same; `--frames-strong` is halfway between the line and the ink on both pages.
- Personality: serious, calm, dramatic
- Goes with: `frames: dividers double-rule`; `frames: ornament corners` or `studs`; `materials: parchment-and-ink`.
- Used on: 3 mockups: a shop with a warm lead (a brass rule inside an ink one on the plate, the board and the basket), a field notebook (a double-ruled stamp), a poetry site (a double rule under its header).

#### Inked
- Id: inked
- Status: draft
- Looks like: a thick, flat line in the ink colour, as if printed: a panel on a comic page, a woodcut, a print studio's boxes. With the light part's crisp shadows, a hard offset block beneath it.
- Made with: a three-pixel border in `--ink`. On a torn or cut sheet the line follows the shape: four one-and-a-half-pixel `drop-shadow`s on the sheet trace its outline, before the light's shadow.

```css assemble
:is(.sheet, .panel) { border: 3px solid var(--ink); }
& { --frames-edge-ink: var(--ink); --frames-edge-width: 2.5px; }   /* torn parchment inked round */
@media (forced-colors: active) { :is(.sheet, .panel) { border-width: 3px; } }
```

- Careful: the ink line reaches 3 to 1 against the ground on both pages, so it can stand without a shadow. The hard offset shadow is the light part's `crisp`; a pressed button in the same style moving into its shadow is the motion part's, and stops under reduced motion.
- Light and dark: on a dark page the ink is pale, so the panel is outlined in cream: a chalk or white-line print look, still bold.
- Personality: playful, dramatic, friendly
- Goes with: `light: shadows crisp`; `frames: controls firm`; `frames: section-edge band` or `wavy`.
- Used on: 4 mockups: a dark, painterly joke site (every panel inked, torn sheets inked round), a poetry site's print look (the owner: "I really like the boxes for the print studio one"), a game-style joke site (three-pixel dark edges), a shop with a warm lead.

#### Pen line
- Id: pen-line
- Status: draft
- Looks like: a line drawn round the sheet by hand with a fountain pen, wobbling a little, gone over twice: one firm line and a fainter one just inside, not quite on top of each other.
- Made with: the line on `::after`, with a second, fainter line as its `outline` a few pixels in, both roughened by an SVG `feTurbulence` displacement filter kept once on the page (outside any repeated item). The filter is read by the CSS, so the line keeps the shared colour on both pages, which an SVG `border-image` cannot.

```css assemble
:is(.sheet, .panel) { border: 2px solid transparent; }
:is(.sheet, .panel)::after { content: ""; position: absolute; inset: -4px; pointer-events: none;
  border: 2px solid var(--ink); border-radius: var(--radius, 0); filter: url(#frames-pen);
  outline: 1px solid color-mix(in oklab, var(--ink) 45%, transparent); outline-offset: -5px; }
& { --frames-edge-ink: var(--frames-strong); --frames-edge-width: 1px; }
```

```html assemble
<filter id="frames-pen" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="4"/>
  <feDisplacementMap in="SourceGraphic" scale="5" xChannelSelector="R" yChannelSelector="G"/></filter>
```

- Careful: one filter id per page, and a different `seed` if two frames sit side by side so their wobbles differ. A filter is repainted whenever the box changes size; keep it to a few frames, never on something that animates (F24, F25). Forced colours keep the filter; the transparent border becomes the plain line there.
- Light and dark: dark ink on a light page, pale ink on a dark one; both read as a drawn line.
- Personality: friendly, calm, playful
- Goes with: `frames: section-edge torn`; `frames: dividers ornament`; `light: shadows paper-lift`.
- Used on: 1 mockup: a soap shop (a pen-drawn frame round its story, drawn there as an SVG `border-image` with only a `viewBox`, the broken kind above).

#### Carved band
- Id: carved-band
- Status: draft
- Looks like: a band of carved beads round the sheet between two fine rules, like a carved wooden picture frame or the beaded border of an old book's plate. The beads are lit from the light part's side.
- Made with: a ring on `::after`: a bead drawn as one `radial-gradient` and repeated with `round`, so whole beads fit each side and land on the corners (the same job `border-image ... round` does, F13), over a pale band of `--mark`. A mask hollows out the middle. The bead's bright spot is placed by the light part's `--hx` and `--hy`.

```css assemble
:is(.sheet, .panel) { border: 1px solid var(--frames-strong); padding: calc(var(--pad, 1.25rem) + 16px); }
:is(.sheet, .panel)::after { content: ""; position: absolute; inset: 3px; padding: 12px; pointer-events: none; border-radius: inherit;
  background: radial-gradient(circle at calc(50% - var(--hx, 0) * 14%) calc(50% - var(--hy, 1) * 14%), var(--frames-metal-lit) 0 12%,
      var(--mark) 38%, var(--frames-metal-deep) 58%, transparent 64%) 0 0 / 12px 12px round border-box,
    color-mix(in oklab, var(--mark) 22%, var(--surface));
  outline: 1px solid var(--frames-strong); outline-offset: -1px;
  mask: linear-gradient(var(--ink) 0 0) content-box exclude, linear-gradient(var(--ink) 0 0); }
& { --frames-edge-ink: var(--frames-strong); --frames-edge-width: 1px; --frames-ring: 16px; --frames-orn-at: 5px; --frames-stud-at: 5px; }
```

- Careful: a mask reads only how opaque a colour is, so any shared name does (`--ink` here). The ring's width must be one bead, or the beads land half inside the hole. A product picture is shown whole (sales guide): the band goes outside the picture, never over it. On a phone the band eats width on both sides; keep it to 12 pixels there. Forced colours drop the gradient and keep the fine rule.
- Light and dark: on a light page the beads are carved wood; on a dark page, with the dark page's gold `--mark`, they read as gilt beads. Both read as carving.
- Personality: dramatic, calm
- Goes with: `frames: ornament corners`; `frames: section-edge band`; `materials: wood-and-canvas`; `background: detailed-ground`.
- Used on: 3 mockups: two versions of a small shop of handmade goods (carved frames with corner bosses round every product picture), a dark, painterly joke site (a band of thorns round the first screen). All three drew it as an SVG `border-image`.

#### Metal ring
- Id: metal-ring
- Status: draft
- Looks like: a bevelled metal ring round the panel with a dark line outside it, like a window in a game's interface. Each side of the ring is a rounded bar with a bright stripe along it; the sides facing the light are brighter.
- Made with: CSS alone. The sheet's border is the dark outer line; a ring on `::after`, nine pixels wide, is four gradients, one per side, hollowed by a mask. The metal is `var(--metal, var(--mark))`: the colour part's metal when it sets one, else `--mark`, so a dark page's gold gives gold and a light page's brown gives bronze. Studs and a jewel come from the ornament layer.

```css assemble
:is(.sheet, .panel) { border: 2px solid var(--frames-metal-deep); padding: calc(var(--pad, 1.25rem) + 9px); }
:is(.sheet, .panel)::after { content: ""; position: absolute; inset: 0; padding: 9px; pointer-events: none; border-radius: inherit;
  background:   /* each side a rounded bar with a bright stripe; the sides facing the light brighter */
    linear-gradient(var(--frames-metal), var(--frames-metal-lit) 35%, var(--frames-metal) 70%, var(--frames-metal-deep)) top / 100% 9px no-repeat,
    linear-gradient(to top, var(--frames-metal-deep), var(--frames-metal) 40%, var(--frames-metal-deep)) bottom / 100% 9px no-repeat,
    linear-gradient(to right, var(--frames-metal), var(--frames-metal-lit) 35%, var(--frames-metal) 70%, var(--frames-metal-deep)) left / 9px 100% no-repeat,
    linear-gradient(to left, var(--frames-metal-deep), var(--frames-metal) 40%, var(--frames-metal-deep)) right / 9px 100% no-repeat;
  box-shadow: inset 0 0 0 1px var(--frames-metal-deep);   /* the ring's own dark line, not a shadow */
  mask: linear-gradient(var(--ink) 0 0) content-box exclude, linear-gradient(var(--ink) 0 0); }
& { --frames-edge-ink: var(--frames-strong); --frames-edge-width: 1px; --frames-ring: 9px; --frames-stud-at: 0px; }
```

- Careful: the heaviest option. Use it on the few panels that are windows (a dialog, the player's own panel, a section's main window), not on every item. The panel behind words is close to opaque, so contrast holds over any painting behind it. On a phone the ring stays nine pixels; the padding inside it gives way. The bright sides are top and left whatever the light part says; a site lit from the right swaps the two pairs. Forced colours drop the gradients and keep the outer line.
- Light and dark: bronze on the light page, gold on the dark one (from `--mark`); the dark page is where it belongs.
- Personality: dramatic, playful
- Goes with: `frames: ornament studs` or `keystone`; `frames: controls firm`; `materials: metal-and-dark-glass`; `light: shadows deep`.
- Used on: 3 mockups: three versions of a game-style joke site (gold and silver rings as SVG `border-image` on two, the CSS ring with rivets and a gem on the third).

### Edge
- Layer: edge
- Owns: the outline of the sheet itself: straight, cut, torn or deckled, and whether the paper is laid a little crooked.
- Default: straight

**On a shaped sheet**, the sheet itself is never cut. The option sets `--sheet-mask` (an SVG shape stretched to the sheet) on each sheet, clears the sheet's own background, and paints the paper on the sheet's `::before`: `background: var(--sheet-fill)` (the fill and any texture the materials part lays as background) through that mask. The materials part's texture span (`.materials-mat`) takes the same mask, so grain and stains are cut with the paper, while its fixings (`.materials-fix`: tape, pins, a clip) are never masked and overhang the edge. The words are never turned. A plain border cannot follow the shape, so the border is hidden and redrawn along the shape on the sheet's `::after`: the same shape, less a smaller copy of it, in `--frames-edge-ink`, `--frames-edge-width` wide (the border layer sets both: 2.5 pixels of ink for inked, one of `--frames-strong` for the others, none for none). Ring borders (double, pen line, carved, metal) need a straight edge and are not drawn on a shaped sheet. The sheet, uncut, carries the light part's low shadow as `filter: var(--drop-low)` (never `box-shadow`, which would draw a rectangle), so the shadow follows the torn paper, its tape and its pins together.

#### Straight
- Id: straight
- Status: draft
- Looks like: a machine-cut sheet with straight sides, square to the page.
- Made with: nothing: the sheet keeps its own box, background, border and the light part's `box-shadow`.

```css assemble
/* edge: straight. Nothing is drawn: the sheet keeps its own straight box. */
```

- Careful: every edge straight is the general guide's eighth template tell when the sections are too ("a straight edge between it and the next"). A warm site wants at least one edge that is not (warm guide).
- Light and dark: the same.
- Personality: any
- Goes with: any border.
- Used on: most mockups: every professional and civic one, the observatory, the 3D game.

#### Cut
- Id: cut
- Status: draft
- Looks like: cut by hand with scissors: not quite square, laid a little crooked on the page.
- Made with: a four-point mask a percent or two out of true, so the sheet looks laid a little crooked while the words stay level; every second sheet takes a different outline.

```css assemble
& { --frames-shape: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100' preserveAspectRatio='none'%3E%3Cpolygon points='0,2.2 98.9,0 100,97.6 1.2,100'/%3E%3C/svg%3E");
  --frames-stud-at: 12px; }   /* pins go through the paper, not past its edge */
.sheet:nth-of-type(even) { --frames-shape: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100' preserveAspectRatio='none'%3E%3Cpolygon points='1.1,0 100,1.8 98.8,100 0,98.2'/%3E%3C/svg%3E"); }   /* no two cut alike */
.sheet { --sheet-mask: var(--frames-shape) 0 0 / 100% 100% no-repeat; border-color: transparent; border-width: 1px; background: none; }   /* the sheet is never cut */
.sheet, .sheet .sheet { box-shadow: none; filter: var(--drop-low, opacity(1)) var(--drop-rim, opacity(1)); }   /* the light part's shadow as a filter: it follows the paper and its tape */
.sheet::before { content: ""; position: absolute; inset: -1px; z-index: -1; pointer-events: none;   /* the paper: the material's fill through the shape */
  background: var(--sheet-fill, var(--surface)); -webkit-mask: var(--sheet-mask); mask: var(--sheet-mask); }
.sheet::after { content: ""; position: absolute; inset: -1px; pointer-events: none; z-index: 1;   /* the border, redrawn along the shape */
  padding: 0; border: 0; outline: 0; border-radius: 0; box-shadow: none; filter: none; opacity: 1; translate: none; rotate: none;
  background: var(--frames-edge-ink); mask: var(--frames-shape) 0 0 / 100% 100% no-repeat, var(--frames-shape) center / calc(100% - 2 * var(--frames-edge-width)) calc(100% - 2 * var(--frames-edge-width)) no-repeat; mask-composite: exclude; }
```

- Careful: tilts stay between half a degree and three, and never touch reading text or anything typed into (warm guide). The outline varies between sheets (`:nth-of-type(even)`) so neighbours do not match. The swatch book turns the paper on a `::before` too; lifted out, the `::before` keeps the words straight and the sheet uncut.
- Light and dark: on a dark page a cut sheet reads by its colour step and the light part's lit edge; with `border: hairline` its outline helps.
- Personality: friendly, playful
- Goes with: `frames: section-edge torn`; `frames: dividers dashed`; `frames: ornament studs` (pins); `materials: paper-and-tape`.
- Used on: 2 mockups: a volunteer page (events as cut-paper notices), a repair café (cut card on pegboard).

#### Torn
- Id: torn
- Status: draft
- Looks like: torn from a pad or a book: a ragged edge all round, deeper in a few places.
- Made with: a polygon of thirty or so small steps per side, used as a mask and written once as `--frames-shape` (the swatch book's builder draws it at random and keeps the corners nearly whole, so no torn spike lands on a corner). Points in percent stretch with the sheet; for a very tall sheet the side tears grow with it.

```css assemble
& { --frames-shape: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100' preserveAspectRatio='none'%3E%3Cpolygon points='0.0,0.3 3.3,0.3 6.7,1.6 10.0,0.2 13.3,0.3 16.7,1.4 20.0,0.7 23.3,0.8 26.7,1.5 30.0,1.5 33.3,0.7 36.7,1.4 40.0,0.4 43.3,0.7 46.7,0.9 50.0,3.1 53.3,1.1 56.7,1.0 60.0,0.4 63.3,0.1 66.7,0.9 70.0,1.0 73.3,0.8 76.7,0.0 80.0,2.9 83.3,1.5 86.7,1.2 90.0,0.8 93.3,0.1 96.7,0.8 100.0,0.3 99.3,6.7 99.3,13.3 97.3,20.0 98.8,26.7 99.3,33.3 99.1,40.0 99.6,46.7 99.5,53.3 98.7,60.0 99.5,66.7 98.9,73.3 99.2,80.0 99.2,86.7 99.7,93.3 100.0,99.7 96.7,98.6 93.3,99.8 90.0,99.8 86.7,99.2 83.3,99.6 80.0,99.6 76.7,97.6 73.3,98.6 70.0,98.6 66.7,96.9 63.3,98.7 60.0,98.8 56.7,99.9 53.3,98.9 50.0,98.3 46.7,99.3 43.3,97.7 40.0,98.8 36.7,98.8 33.3,98.7 30.0,99.0 26.7,98.8 23.3,99.8 20.0,99.6 16.7,99.5 13.3,99.1 10.0,99.3 6.7,98.9 3.3,98.4 0.0,99.7 1.2,93.3 2.9,86.7 0.5,80.0 2.5,73.3 0.5,66.7 1.0,60.0 0.3,53.3 0.1,46.7 0.6,40.0 0.8,33.3 0.3,26.7 0.9,20.0 0.2,13.3 0.8,6.7'/%3E%3C/svg%3E");
  --frames-stud-at: 12px; }   /* pins go through the paper, not past its edge */
.sheet { --sheet-mask: var(--frames-shape) 0 0 / 100% 100% no-repeat; border-color: transparent; border-width: 1px; background: none; }   /* the sheet is never cut */
.sheet, .sheet .sheet { box-shadow: none; filter: var(--drop-low, opacity(1)) var(--drop-rim, opacity(1)); }   /* the light part's shadow as a filter: it follows the paper and its tape */
.sheet::before { content: ""; position: absolute; inset: -1px; z-index: -1; pointer-events: none;   /* the paper: the material's fill through the shape */
  background: var(--sheet-fill, var(--surface)); -webkit-mask: var(--sheet-mask); mask: var(--sheet-mask); }
.sheet::after { content: ""; position: absolute; inset: -1px; pointer-events: none; z-index: 1;   /* the border, redrawn along the shape */
  padding: 0; border: 0; outline: 0; border-radius: 0; box-shadow: none; filter: none; opacity: 1; translate: none; rotate: none;
  background: var(--frames-edge-ink); mask: var(--frames-shape) 0 0 / 100% 100% no-repeat, var(--frames-shape) center / calc(100% - 2 * var(--frames-edge-width)) calc(100% - 2 * var(--frames-edge-width)) no-repeat; mask-composite: exclude; }
```

- Careful: the mask cuts anything that pokes past the sheet (a focus ring at the very edge, a shadow), so keep controls inside the padding. With `border: inked` it is torn parchment inked round, the sorcery look. Text near the torn edge needs the padding density gives plus the depth of the tear.
- Light and dark: on a dark page the torn sheet is a dark sheet on a darker ground; the tear shows less. An outline (`border: hairline` or `inked`) brings it back.
- Personality: friendly, playful, dramatic
- Goes with: `frames: section-edge torn`; `frames: border inked` or `none`; `materials: paper-and-tape` or `parchment-and-ink`.
- Used on: 4 mockups: a field notebook (torn tops on taped-in pages), a dark, painterly joke site (six parchment tears, inked round), a shop with a warm lead (torn sheets with nails), a small shop of handmade goods.

#### Deckled
- Id: deckled
- Status: draft
- Looks like: handmade paper: a soft, feathered edge, uneven in small fibres rather than torn in big steps. Before paper machines every sheet had one; now it says "made by hand, with care" (F21).
- Made with: a mask that is an SVG rectangle roughened by a filter inside it: `feTurbulence` in several octaves (big clumps and small fibres) displacing the edge up to nine pixels, then a slight blur so the fibres feather. The outer five pixels of the paper are a fringe mixed a little towards the ink (7 percent on a light page, 26 on a dark one), as the thin, fibrous edge of real deckle is a step lighter or darker than the sheet; the fringe is drawn on `::after` with a second, smaller deckle cut out of it, so the edge reads even where sheet and ground are close. The filter travels inside the mask's own SVG, so nothing is added to the page.

```css assemble
& { --frames-shape: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='d' x='-3%25' y='-3%25' width='106%25' height='106%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.05' numOctaves='4' seed='7'/%3E%3CfeDisplacementMap in='SourceGraphic' scale='9' xChannelSelector='R' yChannelSelector='G'/%3E%3CfeGaussianBlur stdDeviation='0.7'/%3E%3C/filter%3E%3Crect x='6' y='6' style='width:calc(100%25 - 12px);height:calc(100%25 - 12px)' filter='url(%23d)'/%3E%3C/svg%3E");
  --frames-stud-at: 12px; }   /* pins go through the paper, not past its edge */
.sheet { --sheet-mask: var(--frames-shape) 0 0 / 100% 100% no-repeat; border-color: transparent; border-width: 1px; background: none; }   /* the sheet is never cut */
.sheet, .sheet .sheet { box-shadow: none; filter: var(--drop-low, opacity(1)) var(--drop-rim, opacity(1)); }   /* the light part's shadow as a filter: it follows the paper and its tape */
.sheet::before { content: ""; position: absolute; inset: -1px; z-index: -1; pointer-events: none;   /* the paper: the material's fill through the shape */
  background: var(--sheet-fill, var(--surface)); -webkit-mask: var(--sheet-mask); mask: var(--sheet-mask); }
.sheet::after { content: ""; position: absolute; inset: -1px; pointer-events: none; z-index: 1;   /* a fringe a step off the sheet, so the edge reads on a near ground */
  padding: 0; border: 0; outline: 0; border-radius: 0; box-shadow: none; filter: none; opacity: 1; translate: none; rotate: none;
  background: light-dark(color-mix(in oklab, var(--ink) 9%, transparent), color-mix(in oklab, var(--ink) 26%, transparent)); mask: var(--frames-shape) 0 0 / 100% 100% no-repeat, url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='d' x='-3%25' y='-3%25' width='106%25' height='106%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.05' numOctaves='4' seed='7'/%3E%3CfeDisplacementMap in='SourceGraphic' scale='9' xChannelSelector='R' yChannelSelector='G'/%3E%3CfeGaussianBlur stdDeviation='0.7'/%3E%3C/filter%3E%3Crect x='11' y='11' style='width:calc(100%25 - 22px);height:calc(100%25 - 22px)' filter='url(%23d)'/%3E%3C/svg%3E") 0 0 / 100% 100% no-repeat; mask-composite: exclude; }
```

- Careful: a filter on a large sheet is repainted whenever the sheet changes size; fine for a few sheets, slow on a long scrolling list (F24). Keep it off anything that animates. The blur softens only the mask's edge, never the words.
- Light and dark: on a light page the fringe is a faint darker fibre round cream paper; on a dark page it is a paler fibrous rim, which is what makes the edge visible against a near ground without changing any colour.
- Personality: calm, friendly
- Goes with: `frames: border none`; `materials: fine-paper`; `frames: dividers ornament`.
- Used on: no mockup yet. From print: invitations, letterpress cards and fine editions use deckled paper as a sign of care (F21).

### Section edge
- Layer: section-edge
- Owns: the line where one section meets the next across the whole page: straight, torn, a wave, a skyline, a valance or a carved strip. Not the bands of colour themselves (background part).
- Default: straight

**How every shaped seam is built.** Every band but the first on the page gets a `::before` 24 pixels high, laid over the seam with one pixel inside the band (so no hairline of the wrong colour shows at some zoom levels), painted in the band's own colour (`background-color: inherit`) and cut to shape by an SVG mask stretched across. A fixed height in pixels means the shape flattens on a wide window and deepens on a phone, rather than growing huge. It shows only where the band has a colour of its own; between two bands of the same colour it draws nothing. It needs the band not to clip what pokes out of it (`overflow: clip` hides it).

#### Straight
- Id: straight
- Status: draft
- Looks like: one section stops where the next begins, along a straight line.
- Made with: nothing.

```css assemble
/* section-edge: straight. Nothing is drawn: one band stops where the next begins. */
```

- Careful: GOV.UK separates sections with space alone until a line is needed (F5); a straight edge between two bands of colour is the plainest choice and the template's.
- Light and dark: the same.
- Personality: any
- Goes with: anything.
- Used on: most mockups.

#### Torn
- Id: torn
- Status: draft
- Looks like: the band below has been torn across: a ragged line of small peaks.
- Made with: an SVG path of random steps (the builder draws it) as the mask.

```css assemble
.page .band:not(.page > :first-child, .band .band) { position: relative; }
.page .band:not(.page > :first-child, .band .band)::before { content: ""; position: absolute; left: 0; top: -23px; width: 100%; height: 24px; pointer-events: none;
  background-color: inherit; background-image: none; mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 24' preserveAspectRatio='none'%3E%3Cpath d='M0 24V14L44 16L61 11L89 10L107 5L135 6L164 2L180 13L208 10L245 8L261 15L294 13L328 18L353 14L379 11L414 7L431 10L468 11L496 12L516 5L541 15L561 4L578 3L601 11L641 7L667 7L691 14L722 6L740 15L776 15L798 11L841 11L886 5L931 3L958 2L998 13L1043 15L1088 11L1133 14L1158 18L1184 5L1200 9V24Z'/%3E%3C/svg%3E") 0 0 / 100% 100% no-repeat; }   /* the band's own colour, over the seam */
```

- Careful: stretched across a wide window the peaks get wide and soft; draw the path for the widest page, or repeat a short one as a `mask` tile. Leave the band's top padding deeper than the tear.
- Light and dark: the tear is in the band's colour, so it reads on both.
- Personality: friendly, playful
- Goes with: `frames: edge torn` or `cut`; `materials: paper-and-tape`.
- Used on: 5 mockups: a volunteer page ("Torn paper, never a straight line"), a field notebook (above the kraft footer), a repair café (a torn red footer), a soap shop (under the first picture), a small shop.

#### Wavy
- Id: wavy
- Status: draft
- Looks like: a soft wave, as if the band below were a hill in front of the one above.
- Made with: an SVG wave of quadratic curves as the mask. A wave can also be two radial gradients used as a `mask` on the band itself (F8).

```css assemble
.page .band:not(.page > :first-child, .band .band) { position: relative; }
.page .band:not(.page > :first-child, .band .band)::before { content: ""; position: absolute; left: 0; top: -23px; width: 100%; height: 24px; pointer-events: none;
  background-color: inherit; background-image: none; mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 24' preserveAspectRatio='none'%3E%3Cpath d='M0 24V12Q150 0 300 10T600 12T900 8T1200 12V24Z'/%3E%3C/svg%3E") 0 0 / 100% 100% no-repeat; }   /* the band's own colour, over the seam */
```

- Careful: it is an edge, not a frame: pair it with a border for panels, or with none. Keep words out of the wave's height.
- Light and dark: the same.
- Personality: friendly, playful, calm
- Goes with: `frames: border metal-ring` or `none`; `background: pattern coloured-bands`.
- Used on: 2 mockups: a night market (a wave at the foot of every band, bunting riding it), a game-style joke site (waves between bands of painted landscape).

#### Contour
- Id: contour
- Status: draft
- Looks like: the skyline of the land, hills and ridges in straight steps, with a fine line traced along its top like a line on a chart or the horizon in an engraving.
- Made with: the wavy seam's method with straight segments, and the traced line drawn over it as one thin diagonal `linear-gradient` per segment in `--frames-strong` (a stroke inside the mask's SVG could not take a shared colour), each in a box from one point to the next so it keeps its width when the shape stretches.

```css assemble
.page .band:not(.page > :first-child, .band .band) { position: relative; }
.page .band:not(.page > :first-child, .band .band)::before { content: ""; position: absolute; left: 0; top: -23px; width: 100%; height: 24px; pointer-events: none;
  background: linear-gradient(to bottom right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 0% 9px / 7.5% 7px no-repeat,
    linear-gradient(to top right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 8.04% 9px / 6.66667% 4px no-repeat,
    linear-gradient(to bottom right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 15.32% 4px / 7.5% 9px no-repeat,
    linear-gradient(to top right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 23.01% 4px / 5.83333% 6px no-repeat,
    linear-gradient(to bottom right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 29.73% 7px / 7.5% 3px no-repeat,
    linear-gradient(to top right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 38.18% 7px / 8.33333% 8px no-repeat,
    linear-gradient(to bottom right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 46.85% 6px / 7.5% 9px no-repeat,
    linear-gradient(to top right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 54.95% 6px / 7.5% 5px no-repeat,
    linear-gradient(to bottom right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 63.06% 2px / 7.5% 9px no-repeat,
    linear-gradient(to top right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 71.17% 2px / 7.5% 10px no-repeat,
    linear-gradient(to bottom right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 78.57% 9px / 6.66667% 3px no-repeat,
    linear-gradient(to top right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 87.27% 9px / 8.33333% 5px no-repeat,
    linear-gradient(to bottom right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 93.81% 6px / 5.83333% 8px no-repeat,
    linear-gradient(to top right, transparent calc(50% - 0.8px), var(--frames-strong) 0 calc(50% + 0.8px), transparent 0) 100% 6px / 5.83333% 5px no-repeat;
  background-color: inherit; mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 24' preserveAspectRatio='none'%3E%3Cpath d='M0 24V0 15L90 8L170 12L260 3L330 9L420 6L520 14L610 5L700 10L790 1L880 11L960 8L1060 13L1130 5L1200 10V24Z'/%3E%3C/svg%3E") 0 0 / 100% 100% no-repeat; }   /* the land in the band's colour, its skyline traced in ink */
```

- Careful: the skyline should be this site's land (the hills behind the observatory, the town's roofs), not a stock range; draw it once from the picture at the top.
- Light and dark: the traced line is grey on both pages; against a dark band it is quiet.
- Personality: calm, serious
- Goes with: `frames: border hairline`; `frames: ornament crop-marks`.
- Used on: 1 mockup: an observatory (the land's contour filled in the next band's colour with a one-pixel line along it).

#### Valance
- Id: valance
- Status: draft
- Looks like: a row of scallops hanging from the section above into the one below, like the edge of a market awning or a canopy (the valance is an awning's front edge).
- Made with: a strip at the top of the lower band in the ground's colour, cut into half circles by one repeated `radial-gradient` mask; `round` fits whole scallops across any width.

```css assemble
.page .band:not(.page > :first-child, .band .band) { position: relative; }
.page .band:not(.page > :first-child, .band .band) { padding-top: calc(var(--gap-groups, 2rem) + 15px); }
.page .band:not(.page > :first-child, .band .band)::before { content: ""; position: absolute; left: 0; top: -1px; width: 100%; height: 15px; pointer-events: none; background: var(--ground);
  mask: radial-gradient(circle 14px at 50% 0, var(--ink) 96%, transparent) 0 0 / 28px 14px round no-repeat; }   /* scallops in the ground's colour, hanging into the band */
```

- Careful: stripes on the awning are a material (`materials: wood-and-canvas`), not this. Scallops under 20 pixels wide look like a zip; over 60 they look like a cloud.
- Light and dark: the scallops are the ground's colour; on a dark page they are dark tongues into the band, quieter than on light.
- Personality: playful, friendly
- Goes with: `frames: dividers dashed`; `materials: wood-and-canvas`; `light: one-light`.
- Used on: 2 mockups: a night market (a striped canvas valance scalloped by a mask), a shop with a warm lead (an SVG valance over its first picture).

#### Band
- Id: band
- Status: draft
- Looks like: a strip of repeated pattern between two fine rules across the whole page, like a carved moulding, a rope, or a tape measure laid between sections.
- Made with: a strip in the gap above the lower section: a `repeating-linear-gradient` of `--mark` shaded dark to pale and back, so each diagonal reads as a strand of twisted rope, between rules in `--frames-strong`. The room for it is a margin, not a transparent border (which forced colours would draw thick).

```css assemble
.page .band:not(.page > :first-child, .band .band) { position: relative; }
.page .band:not(.page > :first-child, .band .band) { margin-top: 18px; }   /* room for the strip; a transparent border would show in forced colours */
.page .band:not(.page > :first-child, .band .band)::before { content: ""; position: absolute; left: 0; top: -18px; width: 100%; height: 18px; pointer-events: none;
  border-block: 1px solid var(--frames-strong);
  background: repeating-linear-gradient(-55deg, var(--frames-metal-deep) 0, var(--mark) 2px, var(--frames-metal-lit) 3.5px, var(--mark) 5px, var(--frames-metal-deep) 7px); }   /* a twisted rope */
```

- Careful: the same strip, a short length of it, makes a rule under each heading (the sorcery mockup used a 7rem length); that is a divider, so write it in the site's guide as such. On a phone keep it at 12 to 14 pixels.
- Light and dark: on the dark page with a gold `--mark` it reads as a gilt rope; on the light page as carved wood.
- Personality: dramatic, playful
- Goes with: `frames: border carved-band` or `inked`; `frames: ornament corners`.
- Used on: 3 mockups: a small shop of handmade goods (a carved chevron band between every section), a dark, painterly joke site (a band of thorns), a repair café (a tape-measure strip).

### Ornament
- Layer: ornament
- Owns: pieces set on a border: corner pieces, studs, a jewel on the top edge, printer's marks outside the corners. Not tape, pins drawn as pictures or wax seals (materials and picture style).
- Default: none

Every ornament is one empty element, the first thing inside the sheet or panel, `aria-hidden`, absolutely placed; it is decoration, so screen readers never meet it, and forced colours hide it. An ornament needs a line to sit on: with `border: none` it floats.

```html
<div class="sheet"><span class="frames-ornament" aria-hidden="true"></span> ... </div>
```

#### None
- Id: none
- Status: draft
- Looks like: nothing on the border.
- Made with: no element; leave it out of the page.

```css assemble
/* ornament: none. Nothing on the border; leave out the ornament element. */
```

- Careful: the professional guide: "Ornament that has no job is removed."
- Light and dark: the same.
- Personality: any
- Goes with: anything.
- Used on: most mockups.

#### Corners
- Id: corners
- Status: draft
- Looks like: a drawn piece in each corner: an L that curls at its ends with a small leaf in the angle, as on a book's plate or a certificate.
- Made with: one corner drawing as an SVG used as a `mask` (only its shape counts), over a `--mark` background, placed four times, flipped for each corner. Because the colour is CSS, one file serves light and dark.

- Needs markup: `<span class="frames-ornament" aria-hidden="true"></span>` as a direct child of the one sheet or panel that takes the frame (it needs nothing inside).

```css assemble
& { --frames-corner-tl: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'%3E%3Cg transform=''%3E%3Cg fill='none' stroke='black' stroke-width='2.2' stroke-linecap='round'%3E%3Cpath d='M3 27V9Q3 3 9 3H27'/%3E%3Cpath d='M27 3q2 4 -2 6'/%3E%3Cpath d='M3 27q4 2 6 -2'/%3E%3Cpath d='M8 20V12Q8 8 12 8H20' stroke-width='1.2'/%3E%3C/g%3E%3Cpath d='M10 10q7 0 8 8q-8 -1 -8 -8z'/%3E%3C/g%3E%3C/svg%3E");
  --frames-corner-tr: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'%3E%3Cg transform='translate(30 0) scale(-1 1)'%3E%3Cg fill='none' stroke='black' stroke-width='2.2' stroke-linecap='round'%3E%3Cpath d='M3 27V9Q3 3 9 3H27'/%3E%3Cpath d='M27 3q2 4 -2 6'/%3E%3Cpath d='M3 27q4 2 6 -2'/%3E%3Cpath d='M8 20V12Q8 8 12 8H20' stroke-width='1.2'/%3E%3C/g%3E%3Cpath d='M10 10q7 0 8 8q-8 -1 -8 -8z'/%3E%3C/g%3E%3C/svg%3E");
  --frames-corner-bl: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'%3E%3Cg transform='translate(0 30) scale(1 -1)'%3E%3Cg fill='none' stroke='black' stroke-width='2.2' stroke-linecap='round'%3E%3Cpath d='M3 27V9Q3 3 9 3H27'/%3E%3Cpath d='M27 3q2 4 -2 6'/%3E%3Cpath d='M3 27q4 2 6 -2'/%3E%3Cpath d='M8 20V12Q8 8 12 8H20' stroke-width='1.2'/%3E%3C/g%3E%3Cpath d='M10 10q7 0 8 8q-8 -1 -8 -8z'/%3E%3C/g%3E%3C/svg%3E");
  --frames-corner-br: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'%3E%3Cg transform='translate(30 30) scale(-1 -1)'%3E%3Cg fill='none' stroke='black' stroke-width='2.2' stroke-linecap='round'%3E%3Cpath d='M3 27V9Q3 3 9 3H27'/%3E%3Cpath d='M27 3q2 4 -2 6'/%3E%3Cpath d='M3 27q4 2 6 -2'/%3E%3Cpath d='M8 20V12Q8 8 12 8H20' stroke-width='1.2'/%3E%3C/g%3E%3Cpath d='M10 10q7 0 8 8q-8 -1 -8 -8z'/%3E%3C/g%3E%3C/svg%3E"); }
.frames-ornament { inset: var(--frames-orn-at, 4px); background: var(--mark);
  mask: var(--frames-corner-tl) top left / 34px no-repeat, var(--frames-corner-tr) top right / 34px no-repeat,
    var(--frames-corner-bl) bottom left / 34px no-repeat, var(--frames-corner-br) bottom right / 34px no-repeat; }
:is(.sheet, .panel):has(> .frames-ornament) { padding: calc(var(--pad, 1.25rem) + max(14px, var(--frames-ring, 0px) + 6px)); }   /* room for the pieces */
```

- Careful: the sheet needs room for the pieces, or they sit on the heading (the first swatch had that). Draw the piece for the site (a sorcery site's corner stones, a garden's leaves); the swatch's is a placeholder. One kind of corner per site (the game-interface guide: "One metal and one kind of corner").
- Light and dark: `--mark` is brown on light and gold on dark; both read as drawn ornament.
- Personality: dramatic, calm
- Goes with: `frames: border double` or `carved-band`; `frames: section-edge band`.
- Used on: 3 mockups: a dark, painterly joke site (corner stones that make the top an arch), a small shop (corner bosses on the oak frames), a repair café (tool marks in the corners, drawn as pictures).

#### Studs
- Id: studs
- Status: draft
- Looks like: a round stud, rivet or pin in each corner, domed, lit from the light's side.
- Made with: one `radial-gradient` dome placed four times as backgrounds of the ornament element, its bright spot set by the light part's `--hx`, `--hy`. On a metal ring the studs sit in the ring; on a shaped sheet they move inward, so pins go through the paper, not past its edge.

- Needs markup: `<span class="frames-ornament" aria-hidden="true"></span>` as a direct child of each sheet or panel that takes the studs.

```css assemble
.frames-ornament { inset: var(--frames-stud-at, 6px);
  --frames-stud: radial-gradient(circle at calc(50% - var(--hx, 0) * 18%) calc(50% - var(--hy, 1) * 18%),
    var(--frames-metal-lit) 0 18%, var(--frames-metal) 45%, var(--frames-metal-deep) 70%, transparent 74%);
  background: var(--frames-stud) top left / 14px 14px no-repeat, var(--frames-stud) top right / 14px 14px no-repeat,
    var(--frames-stud) bottom left / 14px 14px no-repeat, var(--frames-stud) bottom right / 14px 14px no-repeat; }
```

- Careful: four is enough; studs every few centimetres along each side turn a panel into a door. A coloured pin (a repair café's red map pin) is the accent's colour only if it can be pressed; otherwise draw it in `--mark`.
- Light and dark: bronze on the light page, gold on the dark one.
- Personality: playful, dramatic
- Goes with: `frames: border metal-ring`; `frames: edge cut` (pins).
- Used on: 3 mockups: a game-style joke site (four rivets on the ring), a small shop (studded plates), a repair café (pins).

#### Keystone
- Id: keystone
- Status: draft
- Looks like: one jewel set in the middle of the top edge, standing half above it, ringed in metal: the piece at the top of a window in a game's interface.
- Made with: the ornament element as a small square turned 45 degrees, a `radial-gradient` jewel in `--mark` with a metal outline.

- Needs markup: `<span class="frames-ornament" aria-hidden="true"></span>` as a direct child of the one sheet or panel that takes the jewel.

```css assemble
.frames-ornament { top: -12px; left: 50%; width: 22px; height: 22px; translate: -50% 0; rotate: 45deg;
  border: 2px solid var(--frames-metal-deep); outline: 2px solid var(--frames-metal);
  background: radial-gradient(circle at 35% 35%, var(--frames-metal-lit) 0 14%, var(--mark) 55%, var(--frames-metal-deep) 100%); }
:is(.sheet, .panel):has(> .frames-ornament) { margin-top: 0.75rem; }   /* the jewel stands half above the edge */
```

- Careful: it sticks up by half its size: leave room above the panel. One per window. A jewel in the accent colour would say "press me"; keep it in `--mark`.
- Light and dark: reads on both; strongest on dark.
- Personality: dramatic, playful
- Goes with: `frames: border metal-ring`; `frames: section-edge wavy`.
- Used on: 1 mockup: a game-style joke site (a gem turned 45 degrees at the top of each main panel).

#### Crop marks
- Id: crop-marks
- Status: draft
- Looks like: the fine marks a printer puts just outside each corner of a sheet to show where to cut: two short lines per corner that stop short of it. A printed plate or chart, not a screen.
- Made with: eight one-pixel `linear-gradient` lines on an ornament element set 14 pixels outside the sheet.

- Needs markup: `<span class="frames-ornament" aria-hidden="true"></span>` as a direct child of each sheet or plate that takes the marks.

```css assemble
.frames-ornament { inset: -14px; --frames-c: var(--frames-strong);
  background: linear-gradient(var(--frames-c) 0 0) 0 13px / 9px 1px no-repeat, linear-gradient(var(--frames-c) 0 0) 13px 0 / 1px 9px no-repeat,
    linear-gradient(var(--frames-c) 0 0) 100% 13px / 9px 1px no-repeat, linear-gradient(var(--frames-c) 0 0) calc(100% - 13px) 0 / 1px 9px no-repeat,
    linear-gradient(var(--frames-c) 0 0) 0 calc(100% - 13px) / 9px 1px no-repeat, linear-gradient(var(--frames-c) 0 0) 13px 100% / 1px 9px no-repeat,
    linear-gradient(var(--frames-c) 0 0) 100% calc(100% - 13px) / 9px 1px no-repeat, linear-gradient(var(--frames-c) 0 0) calc(100% - 13px) 100% / 1px 9px no-repeat; }
```

- Careful: the marks sit outside the sheet: leave 14 pixels of space round it, or they touch the next thing. They are quiet; with `border: none` they alone mark the sheet's corners, a nice effect on a pale ground.
- Light and dark: fine grey lines on both pages.
- Personality: serious, calm
- Goes with: `frames: border hairline` or `none`; `frames: section-edge contour`; `frames: dividers double-rule`.
- Used on: no mockup yet. Suggested for the observatory's printed charts ("a printed plate"); from print practice.

### Dividers
- Layer: dividers
- Owns: what separates items in a list or a run of entries: space, a line, a double rule or a printer's mark.
- Default: space

Dividers between items are drawn in CSS, which screen readers do not read. A divider that marks a real change of subject in running text is an `<hr>` (a "thematic break", role `separator`, F28); design systems mark the decorative kind `role="none"` (F6). Every divider goes between items (`li + li` in any list but the menu), never above the first or below the last; an `<hr class="rule">` takes the same line or mark.

#### Space
- Id: space
- Status: draft
- Looks like: space alone between items.
- Made with: a gap clearly larger than the gaps inside an item. The gap's size is density's.

```css assemble
:is(ul, ol):not(nav *, .page > header *) > li + li { margin-top: var(--gap-items, 1.25rem); }
.rule { height: 0; margin-block: var(--gap-items, 1.25rem); }   /* in forced colours it is still a line */
```

- Careful: the gap between items must be at least twice the gap inside one, or the list reads as one block.
- Light and dark: the same.
- Personality: any
- Goes with: `frames: border none`.
- Used on: a quiet gallery of pots (its only line is a measuring line beside each pot, which carries meaning), a poetry site.

#### Hairline
- Id: hairline
- Status: draft
- Looks like: a thin line between items, the width of a page.
- Made with: a one-pixel `border-top` in `--line`, the divider every design system uses (Material: one pixel, full width between unrelated things, inset within a section, F1; Atlassian: one pixel "for all standard component borders and dividers", F2).

```css assemble
:is(ul, ol):not(nav *, .page > header *) > li + li { margin-top: 0.75rem; padding-top: 0.75rem; border-top: 1px solid var(--frames-line); }
.rule { height: 0; border-top: 1px solid var(--frames-line); }
```

- Careful: inset the line (start it at the text, not the edge) when the items belong to one section; run it full width between unrelated groups (F1).
- Light and dark: reads on both.
- Personality: serious, calm
- Goes with: `frames: border hairline` or `rule`.
- Used on: 5 mockups: a field notebook (its log), an observatory (ruled rows), a tutor's site, an art-paint site, a 3D game.

#### Dashed
- Id: dashed
- Status: draft
- Looks like: a dashed line between items, like a form to fill in or a page to cut along. Homely, not official.
- Made with: a two-pixel dashed `border-top` in `--frames-strong`; a fainter `--line` disappears when dashed.

```css assemble
:is(ul, ol):not(nav *, .page > header *) > li + li { margin-top: 0.75rem; padding-top: 0.75rem; border-top: 2px dashed var(--frames-strong); }
.rule { height: 0; border-top: 2px dashed var(--frames-strong); }
```

- Careful: browsers space the dashes their own way; for an even dash, use a `repeating-linear-gradient` as the background of a one-pixel strip. A dashed box round a field means "drop a file here" on many sites; keep dashes for dividers.
- Light and dark: reads on both.
- Personality: friendly, playful
- Goes with: `frames: edge cut`; `frames: section-edge torn` or `valance`.
- Used on: 5 mockups: a repair café, a volunteer page (dotted), a small shop of handmade goods, a shop with a warm lead, a soap shop (a dashed caption rule).

#### Double rule
- Id: double-rule
- Status: draft
- Looks like: a thick rule over the list with a thin one just under it (an Oxford rule, F23), then thin rules between the items: a table in an almanac or an old annual report.
- Made with: the list's `border-top` for the thick line, a one-pixel background line two pixels under it for the thin one, and hairlines between.

```css assemble
:is(ul, ol):not(nav *, .page > header *) { border-top: 3px solid var(--frames-strong); padding-top: 0.875rem;   /* an Oxford rule: thick, then thin */
  background: linear-gradient(var(--frames-strong) 0 0) 0 2px / 100% 1px no-repeat; }
:is(ul, ol):not(nav *, .page > header *) > li + li { margin-top: 0.75rem; padding-top: 0.75rem; border-top: 1px solid var(--frames-line); }
.rule { height: 3px; border-top: 3px solid var(--frames-strong); background: linear-gradient(var(--frames-strong) 0 0) 0 2px / 100% 1px no-repeat; }
```

- Careful: the heavy line is at the head of the group only, never between every item, or it is a stack of bars.
- Light and dark: reads on both.
- Personality: serious, calm
- Goes with: `frames: border hairline` or `double`; `frames: ornament crop-marks`.
- Used on: 3 mockups: an observatory (a heavy rule over thin ones), a tutor's site, a poetry site (a double rule under its header).

#### Ornament
- Id: ornament
- Status: draft
- Looks like: a printer's mark between items: an asterism (⁂), a dinkus of three spaced stars, or a fleuron (❦), centred in the gap. Used in books since the 1850s to mark a break in the story (F19, F20).
- Made with: a character in `content`, with empty alternative text after the slash so screen readers stay silent (F29). The mark is centred; the items' text stays left-aligned.

```css assemble
:is(ul, ol):not(nav *, .page > header *) > li + li { margin-top: 0.5rem; }
:is(ul, ol):not(nav *, .page > header *) > li + li::before { content: "\2042" / ""; display: block; margin-bottom: 0.5rem; text-align: center; font-size: 1.25rem; line-height: 1; color: var(--mark); }
.rule { height: auto; overflow: visible; text-align: center; color: var(--mark); }
.rule::before { content: "\2042" / ""; font-size: 1.25rem; line-height: 1; }
```

- Careful: the old swatch for "none" centred the items' text as well; only the mark is centred. Pick a mark the site's typeface has, or the browser borrows one from another font. Some screen readers ignore the `/ ""`; where that matters, draw the mark as a background picture.
- Light and dark: `--mark` reads on both.
- Personality: calm, dramatic, serious
- Goes with: `frames: border none` or `pen-line`; `frames: edge deckled`.
- Used on: 2 mockups: a poetry site (⁂ between entries, ❦ under the page heading), a dark, painterly joke site (a row of marks between sections). A quiet gallery rejected it: its line beside each pot carried meaning, and a mark there would not have.

### Controls
- Layer: controls
- Owns: the edge of a field, a select and a tick box: its width and which ink it is drawn in. Buttons always take `border: 2px solid var(--accent-edge)` (Base) and are not part of this choice.
- Default: fine

The edge of a control shows where to type or tick, so it must reach 3 to 1 against the sheet (WCAG 1.4.11: "Where a text-input has an indicator such as a complete border, that indicator must meet 3:1", F26). Carbon keeps a separate "strong" border token for exactly this, apart from its decorative ones (F3). That is why this is never `--line`. The focus ring is the colour part's `--focus` as an `outline`, which forced colours keep (F27).

#### Fine
- Id: fine
- Status: draft
- Looks like: a one-pixel line in the soft ink round every field and tick box.
- Made with: one value, `--frames-field-edge`, which every field, select and tick box reads (Base).

```css assemble
& { --frames-field-edge: 1px solid var(--ink-soft); }   /* read by every field, select and tick box (Base) */
```

- Careful: `--ink-soft` reaches 4.5 to 1, so the edge passes with room to spare on both pages. A tick box drawn with `appearance: none` keeps this edge and fills with `--accent` when ticked.
- Light and dark: the same on both.
- Personality: calm, serious, friendly
- Goes with: `frames: border none`, `hairline` or `pen-line`.
- Used on: most mockups.

#### Firm
- Id: firm
- Status: draft
- Looks like: a two-pixel line in the ink round every field: plain, unmissable, made to be written in.
- Made with: the same property, heavier. GOV.UK and Atlassian draw fields and selected things two pixels thick (F2).

```css assemble
& { --frames-field-edge: 2px solid var(--ink); }
```

- Careful: next to a two-pixel field, a one-pixel decorative border looks weak; pair it with a border that is quiet on purpose (none) or as bold as it is (inked, metal ring).
- Light and dark: on a dark page the edge is pale ink: a bright box, very clear.
- Personality: serious, playful
- Goes with: `frames: border inked`, `rule` or `metal-ring`.
- Used on: 2 mockups: a repair café (black-edged sign-up lines), a game-style joke site (fields in a metal edge).

## What the visitor's settings change

The rules are under Base, with the forced-colours widths of rule, double and inked in their own options. In forced colours (F17) the browser drops shadows, gradients and masks' pictures and paints every border in `CanvasText`; this part also drops its masks, its `::after` and the seams. With more contrast asked for, the line colour becomes `--frames-strong`. A site that uses an SVG `border-image` sets `border-image: none` in forced colours, since it keeps its own colours.

With forced colours on, every sheet keeps a plain edge, and the ring borders, ornaments and shaped edges go. Tested in the swatch book with forced colours emulated: every sheet, field, tick box and button keeps its edge, and a transparent border is drawn in the text colour as F11 says. Nothing in this part moves; a pressed button sinking into an inked shadow is the motion part's.

## Starting points

### None
- Id: none
- Picks: border: none; dividers: ornament
- Personality: calm, serious
- Looks like: no frames: no border, no box, groups made by space, a printer's mark between items. The swatch shows it with no shadow, as a printed page. Reading text is left-aligned; only the mark is centred.
- Used on: a poetry site's printed-booklet look; the general guide's default.

### Hairline
- Id: hairline
- Picks: border: hairline; dividers: hairline
- Personality: serious, calm
- Looks like: a thin line round each sheet and between items, like a well-set form.
- Used on: a tutor's site, a 3D game's pages, a poetry site.

### Card
- Id: card
- Picks: border: none
- Personality: calm, serious
- Looks like: a lighter box on the ground with rounded corners and a soft shadow. This part draws nothing for it (a transparent border for forced colours); the box is the light part's soft shadow and the corners part's radius, which the swatch stands in for. It is the template's card ("every repeated item is the same white box with rounded corners and a soft shadow"): fine for a panel that holds a form or a summary, never the repeated item on a warm or artistic site. If the card can be tapped, its edge must reach 3 to 1: pick `border: rule`, or give it a border in `--ink-soft`.
- Used on: the first version of a volunteer page (called "very plain"), a poetry site (one look), a soap shop's order panels.

### Torn paper
- Id: torn-paper
- Picks: edge: torn; section-edge: torn
- Personality: friendly, playful
- Looks like: sheets of paper with ragged edges, laid a little crooked, and a torn edge where one band of colour meets the next.
- Used on: a volunteer page, a handmade shop, a small shop of handmade goods, a dark, painterly joke site.

### Inked panel
- Id: inked-panel
- Picks: border: inked; dividers: hairline; controls: firm
- Personality: playful, dramatic
- Looks like: a thick printed line round each panel, firm fields, thin lines between items. With `light: shadows crisp`, the hard block beneath.
- Used on: a dark, painterly joke site, a poetry site's print look, a game-style joke site.

### Carved plate
- Id: carved-plate
- Picks: border: carved-band; ornament: corners; section-edge: band
- Personality: dramatic, calm
- Looks like: framed like a plate in an old book: a carved band of beads with corner pieces, and a strip of the same carving between sections.
- Used on: two versions of a small shop of handmade goods; a dark, painterly joke site.

### Riveted metal
- Id: riveted-metal
- Picks: border: metal-ring; ornament: studs; controls: firm
- Personality: dramatic, playful
- Looks like: a bevelled metal ring with a rivet in each corner round a dark panel, as on a game's interface.
- Used on: three versions of a game-style joke site.

### Wavy edge
- Id: wavy-edge
- Picks: section-edge: wavy
- Personality: friendly, playful
- Looks like: plain sheets; a soft wave between sections, as if each band were a hill in front of the next.
- Used on: a game-style joke site, a night market.

### Warm
- Id: warm
- Picks: edge: cut; section-edge: torn; dividers: dashed
- Personality: friendly, playful
- Looks like: notices cut from paper with scissors, a torn band between sections, dashed lines between items. The warm guide's "at least one frame or edge that is not a straight rectangle" and "at least one edge between sections is not a straight line".
- Used on: the warm guide; a volunteer page and a repair café.

### Artistic
- Id: artistic
- Picks: border: pen-line; section-edge: torn; dividers: ornament
- Personality: calm, dramatic
- Looks like: one frame drawn round by hand on the thing that matters, a torn edge under the first picture, printer's marks between entries. The artistic guide: "The repeated item gets a designed frame"; 7 of 7 sites studied, and none used a plain card.
- Used on: the artistic guide; a soap shop (pen frame, torn edge), a poetry site (marks between entries).

### Professional
- Id: professional
- Picks: border: rule; dividers: hairline
- Personality: serious
- Looks like: ruled like a ledger: a heavy rule over each group, thin ones under and between, one quiet line round the sheet.
- Used on: the professional guide; a tutor's site (replacing "about twenty rounded cards"), an art-paint site.

### Civic
- Id: civic
- Picks: dividers: hairline; controls: firm
- Personality: serious, calm
- Looks like: almost nothing drawn: sections separated by space, thin lines between items, and fields with a firm two-pixel edge you cannot miss. Public-service design systems keep lines for where they help someone fill in a form (F5, F4). The swatch shows it with no shadow.
- Used on: research only (GOV.UK, USWDS); the education guide's tutor site comes closest.

### Sorcery
- Id: sorcery
- Picks: border: inked; edge: torn; section-edge: band; ornament: corners; dividers: ornament
- Personality: dramatic
- Looks like: torn parchment inked round, corner pieces, a carved band between sections, a row of marks between items. The sorcery guide: sections "divided by something drawn (a carved band, a row of marks, the edge of a panel), not by a straight grey line"; parchment "stained and uneven at the edges".
- Used on: the sorcery guide; a dark, painterly joke site.

### Gilded dark
- Id: gilded-dark
- Picks: border: metal-ring; ornament: keystone; section-edge: wavy; controls: firm
- Personality: dramatic, playful
- Looks like: a gilded ring with a jewel at the top round each main window, over bands of rolling land. The game-interface guide: "a thick bevelled border in gold, bronze or steel, with rivets, a gem or a carved cap ... One metal and one kind of corner", and "Thin hairlines ... belong to other guides".
- Used on: the game-interface guide; a game-style joke site.

### Lantern fair
- Id: lantern-fair
- Picks: section-edge: valance; dividers: dashed
- Personality: playful, friendly
- Looks like: an awning's scallops hanging over the stalls, no borders (the canvas and wood do the framing), dashed lines between items.
- Used on: a night-market mockup ("the material does the framing").

### Almanac plate
- Id: almanac-plate
- Picks: border: hairline; ornament: crop-marks; section-edge: contour; dividers: double-rule
- Personality: calm, serious
- Looks like: a printed plate: hairline sheets with printer's marks at the corners, an Oxford rule over each table, and the skyline of the land traced in ink between sections.
- Used on: an observatory mockup (hairline sheets, heavy-over-thin rules, the land's contour traced with a line).

### Catalogue of glazes
- Id: catalogue-of-glazes
- Picks: border: none; dividers: space
- Personality: calm, serious
- Looks like: nothing drawn at all: no border, no shadow, space between every piece; only the fields keep their edge. The pots are the frame. The swatch shows it with no shadow.
- Used on: a quiet gallery of pots ("no shadow at all ... nothing is raised"; the one line on the page measures the pot).

### Field journal
- Id: field-journal
- Picks: edge: torn; section-edge: torn; dividers: hairline
- Personality: friendly, calm
- Looks like: pages torn out and taped in, a torn edge above the footer, and ruled lines in the log.
- Used on: a field-notebook mockup.

### Repair cafe
- Id: repair-cafe
- Picks: edge: cut; section-edge: band; ornament: studs; dividers: dashed; controls: firm
- Personality: playful, friendly
- Looks like: cut card pinned to a board, a strip of pattern (a tape measure) between sections, dashed lines between items, and firm black edges to write your name in.
- Used on: a repair-café mockup.

## Swatch book

`tests/parts/frames.html` shows every option of every layer, then every starting point, each on a light page and on a dark one side by side; open it in a browser to choose by eye. Every swatch has the same things in it, so the frame is the only thing that changes: a sheet with a short form (a field, a tick box, a button), a list of three items, and the next section below on a band of colour. Ornaments are shown on a hairline border, since an ornament needs a line to sit on. Shadows are a stand-in for the light part's soft shadow from overhead; a few starting points also show stand-ins for other parts (card has rounded corners; none, civic and catalogue of glazes have no shadow). It writes the layer classes short (`bo-` for border, and `ed-`, `se-`, `or-`, `dv-`, `co-` for the others). Its code is the first draft of each option's assembly block; two things differ when lifted out: a shaped sheet is a mask on the sheet (the swatch paints its paper on `::before`, with a shadow), and a seam is the band's `::before` (the swatch uses an extra element). It is built by `tests/parts/source/frames.py` from `frames-template.html` beside it; run `python3 frames.py ../frames.html` there to rebuild it. The torn outline, the seams and the corner pieces are drawn by the builder.

## Not covered yet

- **Frames round pictures, video, maps and tables.** The carved band is the shop's picture frame, but how a frame meets a picture's own shape (the corners part's masks) has not been drawn.
- **A frame that changes with state** (selected, full, disabled). A volunteer page lit a yellow sheet behind a chosen notice; one site is not enough for a rule. Atlassian's selected border is two pixels (F2), a starting idea.
- **Diagonal cuts across a whole band.** No mockup used one; the seam method draws it.
- **Hand-drawn frames in SVG** that no CSS can make (a vine, a scroll). The rules for doing it safely are under "Why not SVG border images"; there is no option for it, since the colour is fixed in the file.
- **Firefox and Safari.** The swatch book was looked at in Chromium only; masks with `mask-composite` and SVG filters on pseudo-elements should work in both, but were not seen.
- **Printing.** Filters and masks print; whether a torn sheet prints well was not tried.
- **Real phones.** Looked at in a desktop browser at phone width.

## Sources

Read on 2026-10-07. Six kinds of source: design-system documents (F1 to F7), craft writing by people who make interfaces (F8 to F11), the web platform's own references (F12 to F17), print and editorial tradition (F18 to F23), speed (F24, F25) and accessibility (F11, F17, F26 to F29); and game-interface practice (F30). The fifteen mockups made with the skill and their feedback are the seventh, quoted in each option's "Used on". F23 and the valance definition are from search results only: the pages would not open.

- F1 Material components, divider (one pixel, full width between unrelated content, inset within a section; heavy divider 8dp): github.com/material-components/material-components-android/blob/master/docs/components/Divider.md
- F2 Atlassian Design System, border (1px "the default width for all standard component borders and dividers"; 2px for selected and focused): atlassian.design/foundations/border
- F3 Carbon, colour tokens (border-subtle for decoration; border-strong, such as an input's edge, at 3:1): carbondesignsystem.com/elements/color/tokens/
- F4 US Web Design System, border utilities (widths 1, 2, 4, 8 ... 24 pixels): designsystem.digital.gov/utilities/border/
- F5 GOV.UK Design System, section break ("only visible by its margin" unless made visible): design-system.service.gov.uk/styles/section-break/
- F6 Radix Primitives, separator (decorative separators are `role="none"`): radix-ui.com/primitives/docs/components/separator
- F7 shadcn/ui, separator (a one-pixel line in the border colour): ui.shadcn.com/docs/components/separator
- F8 Temani Afif, wavy shapes and patterns in CSS ("two gradients ... apply to any element using the mask property"): css-tricks.com/how-to-create-wavy-shapes-patterns-in-css/
- F9 Temani Afif, CSS shapes (wavy, zig-zag, scalloped and ragged edges, one element each): css-shape.com
- F10 Temani Afif, the border-image property (nine regions; ignores border-radius; a later `border` shorthand resets it): smashingmagazine.com/2024/01/css-border-image-property
- F11 You want border-color: transparent, not border: none (transparent borders show in high contrast): blog.master.dev/you-want-border-color-transparent-not-border-none/
- F12 MDN, border-image ("border-radius has no effect on the border image"; some browsers draw nothing without a border style; assistive technology cannot read it): developer.mozilla.org/en-US/docs/Web/CSS/border-image
- F13 MDN, border-image-slice (four corners, four sides, the middle dropped unless `fill`): developer.mozilla.org/en-US/docs/Web/CSS/border-image-slice
- F14 Tab Atkins on www-style, sizing an SVG with no intrinsic size in border-image: lists.w3.org/Archives/Public/www-style/2015Aug/0122.html
- F15 MDN, mask-border (limited availability): developer.mozilla.org/en-US/docs/Web/CSS/mask-border
- F16 MDN, border-style (`double` is "two straight lines that add up to the pixel size defined by border-width"): developer.mozilla.org/en-US/docs/Web/CSS/border-style
- F17 MDN, forced-colors, and CSS Color Adjustment level 1 (border and outline colours replaced; box-shadow none; background-image none unless it is a url): developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors and w3.org/TR/css-color-adjust-1/
- F18 Typography for Lawyers, rules and borders (use sparingly; half a point to one point, "Thicker borders are counterproductive"): typographyforlawyers.com/rules-and-borders.html
- F19 Wikipedia, dinkus ("three spaced asterisks"; the asterism ⁂): en.wikipedia.org/wiki/Dinkus
- F20 Wikipedia, fleuron (printers' flower ornaments, as borders and as section breaks; ❦ the hedera): en.wikipedia.org/wiki/Fleuron_(typography)
- F21 Wikipedia, deckle edge ("a feathered edge ... in contrast to a cut edge"; machines removed it, so it became a sign of care): en.wikipedia.org/wiki/Deckle_edge
- F22 Western Australian Museum, text and labels in museum exhibitions (labels must not dominate the object): museum.wa.gov.au/research/development-service/text-and-labels-museum-exhibitions
- F23 The Oxford (Scotch) rule, a thick and a thin rule side by side (from search results; printmag.com would not open)
- F24 Chrome for Developers, hardware-accelerated animations (only opacity, filter and transform; clip-path still paints on the main thread): developer.chrome.com/blog/hardware-accelerated-animations
- F25 web.dev, animations guide (animate opacity and transform; blur-type effects cost more to paint): web.dev/articles/animations-guide
- F26 WCAG 2.1 Understanding 1.4.11 non-text contrast ("Where a text-input has an indicator such as a complete border, that indicator must meet 3:1"): w3.org/WAI/WCAG21/Understanding/non-text-contrast.html
- F27 Sara Soueidan, focus indicators (outline is kept in forced colours, where borders and shadows are overridden): sarasoueidan.com/blog/focus-indicators/
- F28 MDN, the hr element (a thematic break, role separator; for a line purely for looks, use CSS): developer.mozilla.org/en-US/docs/Web/HTML/Element/hr
- F29 MDN, content (alternative text after a slash: `content: "❦" / ""`): developer.mozilla.org/en-US/docs/Web/CSS/content
- F30 Phaser, nine-slice (corners unscaled, sides stretched one way, the middle both; the smallest size is the sum of the corners): docs.phaser.io/phaser/concepts/gameobjects/nine-slice
