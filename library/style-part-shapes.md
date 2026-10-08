---
name: Corners and shapes (a part guide)
summary: The corners of every box and the outline of small things, in layers that switch on their own - corners, controls, labels and pictures - from square printed boxes to round friendly ones, hand-cut corners, tickets, luggage tags, seals and pictures in an arch. It sets the page's radius values for every other part to use, and keeps tap size, focus rings and forced colours working whatever the outline. Each layer works on a light page and a dark one, and can be picked with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: research online (six kinds of source, listed under Sources), the corners and shapes of 15 mockups made with the skill, and the feel guides named in each option
---

# Corners and shapes

A part guide. It covers the corners of every box on a page and the outline of the small things on it: buttons, fields, tick boxes, tags, badges, avatars and the shape a picture is cut to. It is made of four layers, each one decision that switches on its own: **corners**, **controls**, **labels** and **pictures**. A site picks a starting point whole, or a starting point with one layer changed, in its own guide and in the blueprint as `project.style.parts`: `{"shapes": "warm"}`, or `{"shapes": {"start": "lantern-fair", "controls": "plain"}}`. The pick wins over the feel guide for corners and outlines only. The general guide's accessibility minimums (contrast, text size, tap size, a visible focus ring) still hold whatever is picked.

**This part owns corner radius and the outline of small things** (the owners table in the general guide). It sets `--radius` and its two neighbours for every other part to use, so a frame's border, a material's sheet and the light's shadow all bend round the same corner. It does not draw lines: a border, a perforation down a ticket, the string a tag hangs from, a torn or wavy edge on a sheet and the edge between sections are the frames part's. It does not cast shadows: a cut shape takes the light part's `filter: var(--drop-low)`. It does not choose colours: every shape is filled with the shared colour names, and its masks are written in black and transparent, because a mask uses only the alpha.

**Corners decide how serious a page feels, with type and colour.** "If those corners are very rounded, the app will feel playful. If those corners are square, or perhaps only slightly rounded, the app will feel serious" (R5). A national archive chose its buttons on exactly this line: square read as "more formal" and "can sometimes appear scary", so it took "a small but noticeable" radius (R4). The research behind it is real but small, so this guide leans on it lightly: people prefer curved shapes to angular ones in the lab, with 14 to 36 people per experiment and abstract shapes (R17, R18), and round logos call up softness and angular ones hardness, though the effect vanished when the reader's attention was busy elsewhere (R19). So a corner nudges; it does not overrule the words or the colour. Pick the site's personality first (the general guide), then the option whose Personality line names it.

## How it is built

The corners layer sets three radii on the element that carries the look (the `<body>`, or a wrapper round the sections), sized by how big a thing is, not by what it is; the other layers set the outline of particular things from them. Every other part reads these, never a number of its own:

| Property | Set by | What it is for |
|---|---|---|
| `--radius-small` | corners | small things: labels, chips, a picture or a box inside a card, a menu item |
| `--radius` | corners | the general guide's one radius: buttons, fields, cards and sheets |
| `--radius-large` | corners | big things: a panel holding a form, a dialog, a sheet that fills a column |
| `--radius-check` | corners | the tick box: never more than 5px, so it never looks like a round choice (R2) |
| `--corner-shape` | corners | `round`, or `bevel` for cut corners where the browser can draw them |
| `--radius-control`, `--radius-field` | controls | the main button and a field; they fall back to `--radius` |

The code that puts them on the page's hooks is under "Base" below; each option's own code is in a ` ```css assemble ` block that `blueprint.py style css` lifts into a site's stylesheet.

The rules every layer keeps:

- **One family of corners.** The general guide's "one radius": three sizes of the same kind of corner, never a soft card with a sharp button beside it. The other layers give a few named things their own outline (a ticket button, a seal); those are shapes, not a second set of corners.
- **A box inside a box: the inner radius is the outer one less the gap.** "outerRadius - gap = innerRadius" (R6): two rounded corners only look parallel when their radii differ by the space between them. Write it as `border-radius: max(0px, var(--radius-large) - var(--space-4))`, or use `--radius-small` for the inner one. The game-style mockup did this by eye: 12px panels with 8, 6 and 3px things inside.
- **People are round, things are square.** A circle means a person: avatars, a portrait, a name (R3 keeps its full radius "for user/people related" things). A tick box never becomes round and a round choice never becomes square, whatever the corners layer says, so the two are never confused (R2).
- **The shape goes behind the words, never on the element you press.** A cut or masked outline (a ticket, a tag, a ribbon) is drawn on the element's `::before`, and `::after` when it needs an edge, both `position: absolute; z-index: -1` behind the words. The element itself stays a plain box, for three reasons. Clipping hides "content, background, borders, text decoration, outline" outside the clip, so a clipped button loses its focus ring (R13). Pointer events "must not be dispatched on the clipped-out regions" (R13), so a clipped button is smaller to tap than it looks, while WCAG measures the target by its bounding box (R15). And the light part's shadow for a cut shape, `filter: var(--drop-low)`, goes on the element, so it follows the cut drawn inside it. Frames already keeps its torn paper the same way.
- **A rounded outline is drawn with `border-radius`, not a clip.** The focus ring follows `border-radius` in every current browser (Chrome 94, Firefox 88, Safari 16.4, R14) and follows `corner-shape` too (R10), so a round, pill or cut-cornered button needs nothing more. Only shapes that radius cannot make (bites, points, holes, V-cuts) need the `::before`.
- **Words clear the cuts.** Padding keeps text off every bite, point and hole: at least the depth of the cut plus the usual padding. A ribbon whose text can wrap gives its ends in `lh` so they grow with the lines (R8).
- **Holes are holes.** A punched hole or a ticket's bite is cut out with a mask, so whatever is behind shows through. Painting a circle in the ground's colour "doesn't work when the background color change[s]" (R7), and the background part, the light's sky and a dark page all change it.
- **Forced colours.** In forced-colours mode backgrounds and gradients are replaced and shadows removed, but borders are kept and recoloured (R16). So a shape drawn as a background vanishes and its words stand alone. Give every pressable shape a real border, transparent when the shape draws its own edge (the browser colours it in forced colours), and give labels `@media (forced-colors: active) { .tag, .badge { border: 1px solid; } }` (under "Base").

**`corner-shape`: use it, only as an extra.** It sets the curve of a corner inside its `border-radius`: `round`, `squircle`, `bevel` (cut straight across), `scoop`, `notch` and `square` (R10). Unlike `clip-path`, borders, outlines, shadows and backgrounds all follow it (R9, R10), so a cut corner keeps its focus ring and its shadow. It runs in Chrome and Edge from 139 and Firefox from 160, and in no released Safari yet (about 70% of visitors, R11). Where it is missing the corner is simply round at the same radius, which is a fair stand-in, so it needs no `@supports`. This guide uses it for one option, `corners: cut`. Leave `squircle` alone: at the radii used here it is hard to see, and Safari visitors get round anyway. Do not build a silhouette that must be exact (a notched ticket) on `scoop` or `notch` until Safari has it; use the mask recipes below.

## Choosing

Start from a starting point (below), then change a layer if the brief asks for it.

| Starting point | What it feels like | Suits best | Fights |
|---|---|---|---|
| Professional | Small, even rounding; pictures softly rounded | Professional; a service with a booking form | Anything hand-made |
| Civic | Square everything: plain, exact, the same for everyone | A council, a charity's forms, a reference site | Warm, playful |
| Warm | Corners cut by hand, a pebble of a picture | Warm; one person or a small group | Professional, civic |
| Soft and round | Round all through, pill buttons and chips | A playful app, a club for children | Serious, dramatic |
| Artistic | Near-square boxes and the maker's seal | Artistic; a gallery, a poet, a potter | Soft and round |
| Sorcery | A scene in an arch, a wax seal, plain controls | The dark, painterly guide | Professional, civic |
| Gilded dark | Cut-cornered panels, a round portrait, ribbons | The game-interface guide | Calm or official sites |
| Lantern fair | Stall tags on string, links cut like tags | A night market; a small shop with a dark lead | Professional |
| Field journal | Plain pages with luggage tags | A walking club, a naturalist, a garden | A dark lead |
| Repair cafe | Square notices and brown repair tags tied on | A bright community page, busy and hand-made | Professional |

How to choose:

- **Most sites need only the corners layer.** The other three are for the one or two things the brief makes special: the signature or the repeated item. A page with a ticket button, luggage-tag labels, a seal and an arched picture is a costume, not a look. Move at most two of controls, labels and pictures away from plain; the soft-and-round start moves three, and gets away with it only because all three say the same thing (round).
- **The amount of rounding is a choice, and the round end is the template's.** In a survey of 514 design systems, 32% made their main button a pill and another 27% rounded it 7 to 12px (R20). That is the look a visitor has seen most, so `soft` and `round` read as calm and familiar, not as chosen. A page that must not look like a template (the general guide's tells) gets its character from the shape of its repeated item, not from rounding everything.
- **The shape comes from the subject.** A luggage tag belongs to something that travels or is tied to a broken thing at the door; a ticket to an event; a seal to a maker who signs; an arch to a window, a chapel or a stone hall. Say in the site's guide what real thing the shape is.

## Base

Code every pick needs, whatever the options. It puts the corners layer's radii on the page's hooks: `.sheet` takes `--radius`, `.panel` and a dialog `--radius-large`, every `.btn` `--radius-control` and every field `--radius-field`; a tick box takes `--radius-check` and a round choice is always round. Each takes `corner-shape` beside its radius, so `corners: cut` reaches them all. Labels (`.tag`, `.badge`) and pictures (`.picture`) take their outline from their own layers. A label cut to a shape draws its fill on a `::before` in `--shapes-label-fill`, which defaults to a pale wash of the mark colour and which a site or the colour part may set to its own tag colour (keep the words 4.5 to 1 on it). In forced colours a shape drawn as a background vanishes, so labels keep a real edge.

```css assemble
& { --corner-shape: round; --shapes-label-fill: color-mix(in oklab, var(--mark) 24%, var(--surface)); }
.sheet { border-radius: var(--radius); corner-shape: var(--corner-shape, round); }
.panel, dialog { border-radius: var(--radius-large); corner-shape: var(--corner-shape, round); }
.btn { border-radius: var(--radius-control, var(--radius)); corner-shape: var(--corner-shape, round);
  display: inline-flex; align-items: center; justify-content: center; text-decoration: none; cursor: pointer; }   /* a button is a box, never underlined words; its height and padding are density's, its edge frames' */
.field, select, textarea, input:not([type="checkbox"], [type="radio"]) { border-radius: var(--radius-field, var(--radius)); corner-shape: var(--corner-shape, round); }
input[type="checkbox"] { border-radius: var(--radius-check, 2px); corner-shape: var(--corner-shape, round); }
input[type="radio"] { border-radius: 50%; corner-shape: round; }   /* a round choice is always round, whatever the corners */
@media (forced-colors: active) { .tag, .badge { border: 1px solid; } }
```

## Layers

### Corners
- Layer: corners
- Owns: the radius of every box that is not one of the named shapes below: sheets, cards, panels, dialogs, buttons, fields, tick boxes, chips. It sets `--radius-small`, `--radius`, `--radius-large`, `--radius-check` and `--corner-shape`.
- Default: slight

#### Sharp
- Id: sharp
- Status: draft
- Looks like: square corners on every box. Exact and printed: a form from a public office, a page of a catalogue, a timetable.
- Made with: every radius zero. The tick box is square too; a round choice stays round.

```css assemble
& { --radius-small: 0px; --radius: 0px; --radius-large: 0px; --radius-check: 0px; }
```

- Careful: "square buttons are perceived as more formal ... and so they can sometimes appear scary" (R4), and sharp corners are now rare (3% of 514 systems, R20), so they read as a choice: official, or deliberately severe. On a warm page they fight everything else. A focus ring round a square box is square too; give it an offset so it does not merge with the border.
- Light and dark: the same on both. On a dark page a square sheet's edge is crisp; nothing to tune.
- Personality: serious, dramatic
- Goes with: a hairline or ruled frame (frames); `light: shadows none`; the professional or civic colour starts.
- Used on: 1 mockup in part: the poetry site's second look sets `--radius: 0px`.

#### Slight
- Id: slight
- Status: draft
- Looks like: square at a glance, but not raw. Two to four pixels: the corner of a printed card that has been handled.
- Made with: 2, 3 and 4 pixels.

```css assemble
& { --radius-small: 2px; --radius: 3px; --radius-large: 4px; --radius-check: 2px; }
```

- Careful: the most-used corner in this skill, which is a reason to check it is chosen and not left over. A slight corner on a big panel looks accidental; if the panels are large and the brief is calm, step up to soft.
- Light and dark: the same on both.
- Personality: serious, calm, dramatic
- Goes with: almost anything; it is the quiet choice under hand-made labels (luggage tags, hanging tags, seals), which then carry the character.
- Used on: 9 mockups: a night market, an observatory, a quiet gallery, a repair café, a sorcery joke site, two versions of a small shop with a dark lead, the game-style joke site in its tavern look, and a poetry site (2 or 3px each).

#### Soft
- Id: soft
- Status: draft
- Looks like: the calm interface most people use every day: six pixels on buttons and cards, ten on big panels. Friendly without saying so.
- Made with: 4, 6 and 10 pixels, close to the steps two design systems settled on for labels, buttons and cards (4, 6 and 8px, R3; 4 to 12px, R1).

```css assemble
& { --radius-small: 4px; --radius: 6px; --radius-large: 10px; --radius-check: 3px; }
```

- Careful: the safest choice and the most anonymous. On a page with no designed signature, soft corners, white cards and a soft shadow are the template (tell 2 in the general guide); keep it for a page whose character comes from elsewhere.
- Light and dark: the same on both.
- Personality: calm, friendly, serious
- Goes with: `light: shadows soft`; the professional feel; `shapes: pictures rounded`.
- Used on: 2 mockups: a tutoring site (`--radius: 6px`) and the 3D game's pages (4 and 6px).

#### Round
- Id: round
- Status: draft
- Looks like: plainly rounded: 12px on buttons and fields, 20px on panels. Soft, friendly, easy to like; the look of a phone app.
- Made with: 8, 12 and 20 pixels. Large panels use the large radius so they do not look boxier than the buttons on them.

```css assemble
& { --radius-small: 8px; --radius: 12px; --radius-large: 20px; --radius-check: 5px; }
```

- Careful: a big radius on a small thing turns it into a pill, and on a box nested in a card it pinches unless the inner radius is reduced by the gap (see "How it is built"). Very rounded corners "will feel playful" (R5): wrong for a serious brief.
- Light and dark: the same on both.
- Personality: friendly, playful
- Goes with: `shapes: controls pill`; `shapes: labels pill`; `shapes: pictures circle` or `rounded`.
- Used on: 1 mockup: the game-style joke site in its screen look (12px panels with 8, 6 and 3px things inside them, nested by eye).

#### Hand-cut
- Id: hand-cut
- Status: draft
- Looks like: every corner a little different, as if the card were cut with scissors: one corner nearly square, the next well rounded.
- Made with: each radius written as four horizontal and four vertical values (`border-radius: a b c d / e f g h`), uneven on purpose. The browser draws it like any radius, so the border, the focus ring and the shadow follow it.

```css assemble
& { --radius-small: 2px 7px 3px 6px / 6px 2px 7px 3px; --radius: 3px 12px 5px 10px / 10px 4px 13px 5px;
  --radius-large: 4px 22px 8px 18px / 18px 6px 24px 9px; --radius-check: 2px 5px 2px 4px; }
```

- Careful: subtle values disappear: the first try here, with corners between 5 and 10px, looked like a plain soft corner. Make the smallest and largest corner of each box differ by at least three times. A value with eight numbers cannot go through `calc()`, so a box nested in another takes `--radius-small` instead of the "less the gap" rule. On a whole page of identical cards the same unevenness repeats and looks mechanical: vary it per card with a custom property, or keep it for the few things that are cut paper.
- Light and dark: the same on both.
- Personality: friendly, playful
- Goes with: the warm feel; `shapes: pictures pebble`; materials that are paper; `light: shadows paper-lift`.
- Used on: 2 mockups: a volunteer page (`--radius: 10px 14px 11px 13px / 13px 10px 14px 11px`) and a poetry site's sheets (`7px 9px 6px 10px`).

#### Cut
- Id: cut
- Status: draft
- Looks like: every corner cut straight across, like a metal plate, a ticket machine's token or a game's panel. Hard and deliberate.
- Made with: `corner-shape: bevel` inside the usual radius, so the cut is as deep as the radius and the border, focus ring and shadow follow it (R9, R10). Where `corner-shape` is missing (Safari, for now, R11) the same corners are drawn round: the page looks `soft`, not broken.

```css assemble
& { --radius-small: 4px; --radius: 8px; --radius-large: 14px; --radius-check: 3px; --corner-shape: bevel; }
```

- Careful: every box needs `corner-shape: var(--corner-shape, round)` beside its radius, or it stays round. Do not cut corners with `clip-path` instead: it hides the focus ring and the shadow (R13). Gold edges and rivets on the cut are the frames and materials parts' (one metal, one kind of corner, as the game-interface guide asks).
- Light and dark: the same on both. On a dark page a cut corner with a lit edge (the light part's `--edge-lit`) reads as metal.
- Personality: dramatic, playful
- Goes with: the game-interface feel; `frames` that draw metal; `shapes: pictures circle` (round portraits) or `cut-corner`.
- Used on: no mockup yet. The game-interface guide's "chunky metal ... corner pieces" and "one kind of corner for the site" are where it came from.

### Controls
- Layer: controls
- Owns: the outline of the main button and of fields: `--radius-control` and `--radius-field`, and for a ticket or a tag the shape drawn behind the button's words. Tick boxes and round choices are not here: they keep their own shapes (see "How it is built").
- Default: plain

#### Plain
- Id: plain
- Status: draft
- Looks like: buttons and fields with the same corners as every other box.
- Made with: both radii follow `--radius`.

```css assemble
& { --radius-control: var(--radius); --radius-field: var(--radius); }
```

- Careful: none of its own; the corners layer decides how it feels.
- Light and dark: the same on both.
- Personality: any
- Goes with: everything. The sorcery guide asks for it outright: buttons and fields "plain, straight", never framed.
- Used on: every mockup so far, for the buttons of its forms.

#### Pill
- Id: pill
- Status: draft
- Looks like: the button fully round at its ends. Fields stay boxes with the page's corners, so a field is never mistaken for a button.
- Made with: a radius far larger than the button (`999px`); the browser caps it at half the height.

```css assemble
& { --radius-control: 999px; --radius-field: var(--radius); }
```

- Careful: the commonest main button there is (32% of 514 systems, R20), so it reads as an app and as a template. A pill button beside square cards looks borrowed. A lone search field may be a pill too; a form of fields stays boxes. A pill with a long label grows a long, flat middle: keep button labels short.
- Light and dark: the same on both.
- Personality: friendly, playful
- Goes with: `shapes: corners round` or `soft`; `shapes: labels pill`.
- Used on: 2 mockups: a soap shop (filter chips, a basket count and round turn buttons, all `999px`) and the 3D game's points badge.

#### Ticket
- Id: ticket
- Status: draft
- Looks like: the main button is a ticket: a half-circle bitten out of each end. For a page whose main action is getting in: a show, a fair, a talk.
- Made with: two layers behind the words. `::before` is the edge, in `--accent-edge`, two pixels larger all round; `::after` is the fill, in `--accent`. Each is cut by a mask of two radial gradients, one bite per end, the inner bite two pixels larger so the edge runs round it. The button keeps its 2px border, transparent, so forced colours still draw an edge. It is pressed anywhere in its box, and its focus ring is the box's.

```css assemble
/* the main button only: one ticket per page. Its own fill, border colour and box shadow are cleared so the cut shape
   behind the words shows; the 2px border stays, transparent, so forced colours still draw an edge. */
& { --radius-control: var(--radius-small); --radius-field: var(--radius); --shapes-bite: 0.6rem; }
.btn.btn-main { position: relative; isolation: isolate; padding-inline: 1.75rem; }
.btn.btn-main, .btn.btn-main:is(:hover, :active, :focus-visible) { background: none; border: 2px solid transparent; box-shadow: none; }
.btn-main::before, .btn-main::after { content: ""; position: absolute; z-index: -1; border-radius: var(--radius-small); }
.btn-main::before { inset: -2px; background: var(--accent-edge);
  mask: radial-gradient(circle var(--shapes-bite) at 0 50%, transparent 97%, black) left / 51% 100% no-repeat,
        radial-gradient(circle var(--shapes-bite) at 100% 50%, transparent 97%, black) right / 51% 100% no-repeat; }
.btn-main::after { inset: 0; background: var(--accent);
  mask: radial-gradient(circle calc(var(--shapes-bite) + 2px) at -2px 50%, transparent 97%, black) left / 51% 100% no-repeat,
        radial-gradient(circle calc(var(--shapes-bite) + 2px) at calc(100% + 2px) 50%, transparent 97%, black) right / 51% 100% no-repeat; }
.btn-main:hover::after { background: var(--accent-hover, var(--accent)); }
.btn-main:active::after { background: var(--accent-pressed, var(--accent)); }
```

- Careful: the bites must be big enough to read (a 0.5rem bite on a 44px button looked like a speck), and the padding must clear them. A ticket lies flat: the light part's drop shadow fills small bites and they read as holes, so it takes no shadow. A dashed tear line across the stub is a line, and lines are the frames part's. One ticket per page: it is the main action, and a row of them is a strip of raffle tickets.
- Light and dark: the same; the bites show whatever is behind, light or dark.
- Personality: playful, friendly
- Goes with: `shapes: labels ticket` (the dates of the same event); `shapes: corners slight`.
- Used on: no mockup yet as a button. Built here from the masks in R7 because events are a common brief.

#### Tag
- Id: tag
- Status: draft
- Looks like: a link or button cut like a luggage tag: a pointed end with a punched hole, the words level beside it. For "ways in" (the kinds of thing a shop sells, the stalls of a fair) more than for a form's main button.
- Made with: the same two layers as the ticket, cut with `clip-path: polygon()` to a point at the start, and a mask for the hole; the light part's `filter: var(--drop-low)` on the element, so the shadow follows the point. It cuts every `.btn`: the main one from the accent, the others from `--surface-raised` with the `--ink-soft` edge of a control.

```css assemble
/* every button, the ways in: the point and hole are drawn behind the words; the button's own fill and box shadow are
   cleared, its border kept transparent for forced colours, and the light part's drop shadow follows the point.
   The main button is cut from the accent; any other button from the raised surface with the soft ink edge of a control. */
& { --radius-control: var(--radius-small); --radius-field: var(--radius); --shapes-point: 0.9rem; }
.btn { --shapes-btn-fill: var(--surface-raised); --shapes-btn-edge: var(--ink-soft);
  --shapes-btn-hover: color-mix(in oklab, var(--surface-raised) 90%, var(--ink)); --shapes-btn-pressed: color-mix(in oklab, var(--surface-raised) 82%, var(--ink)); }
.btn.btn-main { --shapes-btn-fill: var(--accent); --shapes-btn-edge: var(--accent-edge);
  --shapes-btn-hover: var(--accent-hover, var(--accent)); --shapes-btn-pressed: var(--accent-pressed, var(--accent)); }
.btn { position: relative; isolation: isolate; padding-inline: calc(var(--shapes-point) + 1.1rem) 1.25rem; filter: var(--drop-low, none); }
.btn, .btn:is(:hover, :active, :focus-visible) { background: none; border: 2px solid transparent; box-shadow: none; }
.btn::before, .btn::after { content: ""; position: absolute; z-index: -1; }
.btn::before { inset: -2px; background: var(--shapes-btn-edge);
  clip-path: polygon(var(--shapes-point) 0, 100% 0, 100% 100%, var(--shapes-point) 100%, 0 50%);
  mask: radial-gradient(circle 0.22rem at calc(var(--shapes-point) + 0.15rem) 50%, transparent 95%, black); }
.btn::after { inset: 0; background: var(--shapes-btn-fill);
  clip-path: polygon(calc(var(--shapes-point) - 1px) 0, 100% 0, 100% 100%, calc(var(--shapes-point) - 1px) 100%, 0 50%);
  mask: radial-gradient(circle calc(0.22rem + 2px) at calc(var(--shapes-point) + 0.15rem - 2px) 50%, transparent 95%, black); }
.btn:hover::after { background: var(--shapes-btn-hover); }
.btn:active::after { background: var(--shapes-btn-pressed); }
```

- Careful: a tag points; make it point the way it leads, or at the start as here, never at something else. A row of tag links is a menu: each still needs a clear name and 44px of height. The string a tag hangs from is a line (frames), and tilting the tag is a materials choice (the words stay level whatever).
- Light and dark: the same; the hole shows whatever is behind.
- Personality: friendly, playful
- Goes with: `shapes: labels luggage-tag` or `hanging-tag`; the warm feel; wood and paper materials.
- Used on: 1 mockup: a small shop with a dark lead (its "ways in", links laid on the picture, are parchment tags cut at one corner, each with a punched hole).

### Labels
- Layer: labels
- Owns: the outline of tags and badges: things that name, count or mark, and are never pressed. A date, a price, "new", a category, a maker's mark. Not the words' typeface (lettering) or their colours (colour).
- Default: plain

#### Plain
- Id: plain
- Status: draft
- Looks like: small boxes in the small corners of every other box.
- Made with: `--radius-small` on the label's background.

```css assemble
.tag, .badge { border-radius: var(--radius-small); corner-shape: var(--corner-shape, round); }
```

- Careful: a label must not look like a button: no accent fill, no button-sized padding. Atlassian keeps its labels on a smaller radius than its buttons for the same reason (R3).
- Light and dark: the same on both.
- Personality: any
- Goes with: everything.
- Used on: most mockups (a night market's diet marks, an observatory, a tutoring site's subjects).

#### Pill
- Id: pill
- Status: draft
- Looks like: a label fully round at its ends: the usual chip and status badge.
- Made with: `border-radius: 999px` on the label's background, a little more padding at the ends.

```css assemble
.tag, .badge { border-radius: 999px; padding-inline: 0.75rem; }
```

- Careful: "a count or a state is a thin bar or a small pill" is one of the general guide's template tells. Fine on an app or a shop's filters; on a page that must feel made for its subject, draw the count as something from the subject (a tally, a tag, a seal).
- Light and dark: the same on both.
- Personality: friendly, playful, calm
- Goes with: `shapes: corners round`; `shapes: controls pill`.
- Used on: 2 mockups: a soap shop (filter chips and the basket count) and the 3D game (a points badge).

#### Luggage tag
- Id: luggage-tag
- Status: draft
- Looks like: a small luggage tag: two corners cut off at one end and a hole punched through, the ground showing in the hole. Laid on slightly turned.
- Made with: `clip-path: polygon()` for the cut corners and a mask for the hole, both on the `::before`; the turn on the label; the light part's `filter: var(--drop-low)`.

```css assemble
.tag, .badge { position: relative; isolation: isolate; display: inline-flex; align-items: center; justify-content: center; background: none; }
.tag::before, .badge::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--shapes-label-fill); }
.tag, .badge { padding: 0.3rem 0.75rem 0.3rem 1.5rem; rotate: -2deg; filter: var(--drop-low, none); }
:is(.tag, .badge) + :is(.tag, .badge) { rotate: 1.5deg; }
.tag::before, .badge::before { clip-path: polygon(0.55rem 0, 100% 0, 100% 100%, 0.55rem 100%, 0 calc(100% - 0.55rem), 0 0.55rem);
  mask: radial-gradient(circle 0.2rem at 0.7rem 50%, transparent 92%, black); }
```

- Careful: the hole is cut, not painted (R7). The fill (`--tag-fill`) is the colour part's (a kraft or manila is a materials choice); keep the words 4.5 to 1 on it. A tag cut to one point instead of two corners is the same label (the field notebook's walks): change the polygon to `0.9rem 0, 100% 0, 100% 100%, 0.9rem 100%, 0 50%`.
- Light and dark: on a dark page the hole shows the dark sheet behind and reads as a hole straight away; on a light one it is a pale dot, so do not make it smaller than 0.4rem across.
- Personality: friendly, calm
- Goes with: `shapes: controls tag`; `shapes: corners slight`; paper materials; the field-journal and warm starts.
- Used on: 3 mockups: a field notebook (each walk's tag, cut to a point with a hole), a repair café (the next date on a big tag cut at two corners with a hole) and a soap shop (each price on a kraft tag cut to a point, `polygon(0.9rem 0, 100% 0, 100% 100%, 0.9rem 100%, 0 50%)`).

#### Hanging tag
- Id: hanging-tag
- Status: draft
- Looks like: an upright tag, its two top corners cut off at a slant and a hole at the top centre for the string. Small, it is a price tag; large, the same cut makes a whole card hung on a rail.
- Made with: a polygon with sloping shoulders and a mask for the hole on the `::before`; each tag turned a little about its hole (`transform-origin` at the hole), so it hangs.

```css assemble
.tag, .badge { position: relative; isolation: isolate; display: inline-flex; align-items: center; justify-content: center; background: none; }
.tag::before, .badge::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--shapes-label-fill); }
.tag, .badge { flex-direction: column; vertical-align: top; min-width: 4.75rem; padding: 1.2rem 0.6rem 0.5rem; rotate: -2.5deg; transform-origin: 50% 0.5rem;
  filter: var(--drop-low, none); }
:is(.tag, .badge) + :is(.tag, .badge) { rotate: 2deg; }
.tag::before, .badge::before { clip-path: polygon(22% 0, 78% 0, 100% 0.9rem, 100% 100%, 0 100%, 0 0.9rem);
  mask: radial-gradient(circle 0.2rem at 50% 0.5rem, transparent 92%, black); }
```

- Careful: the shoulders are given in `rem`, so every tag has the same slope whatever its size. The night market and the repair café wrote them in per cent of the height, so a tall tag got deep shoulders and a short one shallow ones. As a card it holds reading text: keep its tilt under 2 degrees and the words level (the tilt on a `::before`, as the frames part does with paper). The string is a line, the frames part's; the rail it hangs from is the materials part's.
- Light and dark: the same; the hole shows what is behind.
- Personality: friendly, playful
- Goes with: `shapes: controls tag`; the lantern-fair and repair-cafe starts; wood and paper materials.
- Used on: 4 mockups: a repair café ("what you can bring", eight manila tags on string), a night market (stall tags on an oak rail) and two small shops with a dark lead (parchment price tags tied under each ware).

#### Ticket
- Id: ticket
- Status: draft
- Looks like: a small ticket: a half-circle bitten out of each end. For dates, times and places at an event.
- Made with: two radial gradients in a mask, one per end, on the `::before`.

```css assemble
.tag, .badge { position: relative; isolation: isolate; display: inline-flex; align-items: center; justify-content: center; background: none; }
.tag::before, .badge::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--shapes-label-fill); }
.tag, .badge { min-height: 1.5rem; padding-inline: 0.95rem; filter: var(--drop-low, none); }
.tag::before, .badge::before { border-radius: var(--radius-small);
  mask: radial-gradient(circle 0.42rem at 0 50%, transparent 96%, black) left / 51% 100% no-repeat,
        radial-gradient(circle 0.42rem at 100% 50%, transparent 96%, black) right / 51% 100% no-repeat; }
```

- Careful: masks with radial gradients keep their circles round however wide the ticket grows, where a stretched SVG path does not (R7, who tried four ways and preferred this). On a label under 1.5rem tall the bites read as dots; keep labels at least that tall. The light part's small drop shadow is fine here, unlike on the ticket button, because the bites on a small label are shallow.
- Light and dark: the same on both.
- Personality: playful, friendly
- Goes with: `shapes: controls ticket`; an events page.
- Used on: no mockup yet. Built from R7 for event dates.

#### Ribbon
- Id: ribbon
- Status: draft
- Looks like: a strip of ribbon with a V cut into each end: a prize, a banner, the label over a panel in a game.
- Made with: one `clip-path: polygon()` with a notch at each end.

```css assemble
.tag, .badge { position: relative; isolation: isolate; display: inline-flex; align-items: center; justify-content: center; background: none; }
.tag::before, .badge::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--shapes-label-fill); }
.tag, .badge { padding-inline: 1.15rem; filter: var(--drop-low, none); }
.tag::before, .badge::before { clip-path: polygon(0 0, 100% 0, calc(100% - 0.55rem) 50%, 100% 100%, 0 100%, 0.55rem 50%); }
```

- Careful: a ribbon that folds round a box needs shading on the fold, which is the light part's, and a ribbon across a corner is a frame's ornament. This is the flat strip only. If its words can wrap, give the notch in `lh` so it grows with the lines (R8).
- Light and dark: the same on both.
- Personality: playful, dramatic
- Goes with: the game-interface feel; `shapes: corners cut`.
- Used on: no mockup yet. The game-interface guide's winged end caps and title banners are where it came from.

#### Seal
- Id: seal
- Status: draft
- Looks like: a round stamp, a little uneven, pressed on slightly turned: a wax seal, a potter's mark, a poet's chop. Holds one or two short words.
- Made with: a fixed width with `aspect-ratio: 1`, and a radius just off a circle (`52% 48% 50% 47% / 47% 53% 46% 54%`), so it looks pressed by hand. A rosette for a prize is the same with a scalloped `clip-path: polygon()` of 24 to 32 points, alternately at 50% and 44% from the middle.

```css assemble
.tag, .badge { position: relative; isolation: isolate; display: inline-flex; align-items: center; justify-content: center; background: none; }
.tag::before, .badge::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--shapes-label-fill); }
/* as narrow as its longest word, never under 3.75rem, and always square, so two short words stack into a round stamp */
.tag, .badge { width: min-content; min-width: 3.75rem; aspect-ratio: 1; padding: 0.4rem; text-align: center; line-height: 1.05; vertical-align: middle;
  rotate: -8deg; filter: var(--drop-low, none); }
:is(.tag, .badge) + :is(.tag, .badge) { rotate: 6deg; }
.tag::before, .badge::before { border-radius: 52% 48% 50% 47% / 47% 53% 46% 54%; }
```

- Careful: a circle is the shape for people (see "How it is built"): a seal stands for a maker, which fits; a seal on a product category does not. Two words at most, and test the longest at the smallest size: "14 June" wraps to two lines and fits, "Saturday 14 June" does not. A seal drawn as a picture (the sorcery site's wax with a sigil) is the picture-style part's; this is its outline only. A square seal (the poetry site's printed look) is `labels: plain` with a fixed square size.
- Light and dark: the same on both. A dark seal on a dark sheet needs a fill a clear step from the sheet.
- Personality: calm, serious, dramatic
- Goes with: the artistic and sorcery feels; `shapes: pictures arch` or `plain`.
- Used on: 5 mockups: two small shops with a dark lead (a dye seal per kind of ware, `border-radius: 50% 46% 52% 48%`), a sorcery joke site (drawn wax seals), a poetry site (each poet's seal, square or round by look) and a quiet gallery (the potter's seal, a ring left open where the thumb lifted).

### Pictures
- Layer: pictures
- Owns: the outline a picture is cut to: photographs, drawings and avatars. Not the frame drawn round it (frames) or how it is drawn (picture style).
- Default: plain

#### Plain
- Id: plain
- Status: draft
- Looks like: a rectangle, with the small corners of the boxes round it.
- Made with: `--radius-small` and `overflow: hidden` (or `border-radius` on the `<img>` itself).

```css assemble
:is(img, svg, video).picture, .picture > :is(img, svg, video) { border-radius: var(--radius-small); corner-shape: var(--corner-shape, round); overflow: hidden; }
```

- Careful: a picture inside a padded card takes the small radius, or the card's radius less the padding, never the card's own (see "How it is built").
- Light and dark: the same; a dark picture on a dark sheet loses its outline, which is fine for a rectangle and not for the shapes below.
- Personality: any
- Goes with: everything.
- Used on: most mockups.

#### Rounded
- Id: rounded
- Status: draft
- Looks like: a clearly rounded rectangle, like a photograph on a phone.
- Made with: a radius of 1.25rem whatever the corners, so it reads as a shape and not as the page's corners.

```css assemble
:is(img, svg, video).picture, .picture > :is(img, svg, video) { border-radius: 1.25rem; overflow: hidden; }
```

- Careful: with `corners: sharp` or `slight` the soft picture argues with the square boxes; use it with soft or round corners. Inside a card, the card's radius must be larger than the picture's plus the gap.
- Light and dark: the same on both.
- Personality: friendly, calm
- Goes with: `shapes: corners soft` or `round`; the professional start.
- Used on: no mockup on purpose yet. It is the default look of many apps' photographs.

#### Circle
- Id: circle
- Status: draft
- Looks like: a circle. A person: an avatar, a portrait, a fixer, a tutor. Or one thing seen up close, as through a lens.
- Made with: `aspect-ratio: 1` and `border-radius: 50%`; `object-fit: cover` on an `<img>`.

```css assemble
:is(img, svg, video).picture, .picture > :is(img, svg, video) { aspect-ratio: 1; height: auto; border-radius: 50%; object-fit: cover; overflow: hidden; }
```

- Careful: the circle cuts off the corners of the picture: keep what matters in the middle two thirds (a face, the moon in the swatch book's drawing had to be moved in). Circles mean people (R3), so a product in a circle reads as a person's avatar. A thick ring round a portrait is a frame.
- Light and dark: the same; on a dark sheet a dark picture's circle fades at the edge, so give it a frame or a lighter sky.
- Personality: friendly, playful, calm
- Goes with: `shapes: corners round`; the gilded-dark start (round portraits in rings); people pages.
- Used on: 2 mockups: both looks of the game-style joke site (a 64px round portrait on its screen look, a 72px portrait in a ring on its tavern look).

#### Arch
- Id: arch
- Status: draft
- Looks like: round at the top and flat at the foot, like a window or a doorway in stone. A scene seen through it.
- Made with: a radius far larger than the picture on the two top corners (`999px`), which the browser caps at half the width, so the top is a half circle; the small radius at the foot. The focus ring and a frame's border follow it, because it is a radius and not a clip.

```css assemble
/* taller than wide, or the half circle eats the top of the picture */
:is(img, svg, video).picture, .picture > :is(img, svg, video) { aspect-ratio: 4 / 5; height: auto; object-fit: cover;
  border-radius: 999px 999px var(--radius-small) var(--radius-small); overflow: hidden; }
```

- Careful: the picture must be taller than it is wide (4 by 5 or taller), or the half circle eats the picture's top third. The carved stone round the arch (spandrels, a keystone) is frames and picture style; this is the opening.
- Light and dark: the same; on a dark page give the sky in the picture a step of light so the curve shows.
- Personality: calm, dramatic
- Goes with: the sorcery feel ("what frames it? an arch"); `shapes: labels seal`.
- Used on: 1 mockup: a sorcery joke site (the scene under a lintel, its arch made by drawn spandrels laid over a rectangle). The sorcery guide's pictures have stone arches behind the figures in 3 of 6.

#### Cut corner
- Id: cut-corner
- Status: draft
- Looks like: two opposite corners cut straight across: a print trimmed for a scrapbook, a card from a game, a museum's index card.
- Made with: `clip-path: polygon()` on the picture. A picture is not focusable and casts no shadow of its own, so a clip is fine here.

```css assemble
/* on the picture itself, never on a link round it, so the link keeps its whole box and its focus ring */
:is(img, svg, video).picture, .picture > :is(img, svg, video) { clip-path: polygon(1.5rem 0, 100% 0, 100% calc(100% - 1.5rem), calc(100% - 1.5rem) 100%, 0 100%, 0 1.5rem); }
```

- Careful: if the picture is a link, the clip shrinks what can be pressed and hides its focus ring: put the clip on the image inside the link, never on the link. A shadow under it is the light part's `--drop-low` on a wrapper.
- Light and dark: the same on both.
- Personality: dramatic, playful, serious
- Goes with: `shapes: corners cut`; the gilded-dark start.
- Used on: no mockup yet.

#### Pebble
- Id: pebble
- Status: draft
- Looks like: a round shape that no compass drew: a pebble, a cut-out photograph, a blob of paint.
- Made with: a nearly round radius written as eight uneven values, turned a few degrees.

```css assemble
:is(img, svg, video).picture, .picture > :is(img, svg, video) { aspect-ratio: 1 / 1.05; height: auto; object-fit: cover; border-radius: 55% 45% 52% 48% / 46% 54% 46% 54%; rotate: -4deg; overflow: hidden; }
```

- Careful: too uneven and it reads as an egg (the first try here did). Turn the picture, not the words beside it. One per page, as the signature or the person behind the site: a row of pebbles is a row of blobs.
- Light and dark: the same; as the circle, give a dark picture a lighter edge on a dark page.
- Personality: friendly, playful
- Goes with: `shapes: corners hand-cut`; the warm start; paper materials.
- Used on: 2 mockups, on small things only: a soap shop's numbered steps and a small shop's dye seals (`50% 46% 52% 48%`). No picture yet.

## Starting points

### Professional
- Id: professional
- Picks: corners: soft; controls: plain; labels: plain; pictures: rounded
- Personality: serious, calm
- Looks like: small, even rounding on every box, nothing cut or tied on, photographs softly rounded. Even and exact, and not cold.
- Used on: the professional guide (one institutional look, no decoration) and a tutoring site (`--radius: 6px`).

### Civic
- Id: civic
- Picks: corners: sharp; controls: plain; labels: plain; pictures: plain
- Personality: serious
- Looks like: square everything: plain, exact, the same for everyone. A form from a public office.
- Used on: no mockup yet takes it whole; it goes with the colour part's civic start. A national archive found square buttons too formal for its visitors (R4): pick it where formal is the point.

### Warm
- Id: warm
- Picks: corners: hand-cut; controls: plain; labels: plain; pictures: pebble
- Personality: friendly, calm
- Looks like: corners cut by hand, every one a little different, and one picture cut to a pebble: things made at a kitchen table.
- Used on: the warm guide (cut paper, notes, bunting); a volunteer page and a poetry site used uneven radii.

### Soft and round
- Id: soft-and-round
- Picks: corners: round; controls: pill; labels: pill; pictures: circle
- Personality: playful, friendly
- Looks like: round all through: pill buttons and chips, big soft corners, round pictures. An app that wants to be liked.
- Used on: no mockup whole; a soap shop and the 3D game took its pills. It is the commonest look of the 514 systems in R20, so pair it with a strong signature.

### Artistic
- Id: artistic
- Picks: corners: slight; controls: plain; labels: seal; pictures: plain
- Personality: calm, serious
- Looks like: near-square boxes that leave the work to speak, and the maker's seal on the work.
- Used on: the artistic guide ("none used a plain white card with rounded corners"); a quiet gallery (2px corners, the potter's seal), a poetry site (each poet's seal) and an observatory (3px, plain plates). The almanac-plate and catalogue-of-glazes looks of other parts take this one.

### Sorcery
- Id: sorcery
- Picks: corners: slight; controls: plain; labels: seal; pictures: arch
- Personality: dramatic
- Looks like: a scene seen through an arch, wax seals on the sheets, and plain straight controls that never wear a frame.
- Used on: the sorcery guide (stone arches in 3 of 6 pictures; "fields, labels, buttons ... plain, straight"); a sorcery joke site (the scene under a lintel, wax seals on the vows).

### Gilded dark
- Id: gilded-dark
- Picks: corners: cut; controls: plain; labels: ribbon; pictures: circle
- Personality: dramatic, playful
- Looks like: panels and buttons with their corners cut like metal plates, round portraits, ribbons for titles.
- Used on: the game-interface guide (round portraits in thick rings, one kind of corner, winged end caps); the game-style joke site's two looks took the round portraits.

### Lantern fair
- Id: lantern-fair
- Picks: corners: slight; controls: tag; labels: hanging-tag; pictures: plain
- Personality: friendly, dramatic
- Looks like: stall tags hung on string, and the ways in cut like tags with a punched hole.
- Used on: a night-market mockup (stall tags on an oak rail) and two versions of a small shop with a dark lead (tags as the ways in, price tags tied under each ware).

### Field journal
- Id: field-journal
- Picks: corners: slight; controls: plain; labels: luggage-tag; pictures: plain
- Personality: calm, friendly
- Looks like: plain taped-in pages, each walk marked with a small kraft luggage tag.
- Used on: a field-notebook mockup (the walk tags).

### Repair cafe
- Id: repair-cafe
- Picks: corners: slight; controls: plain; labels: hanging-tag; pictures: plain
- Personality: playful, friendly
- Looks like: square paper notices pinned up, and brown repair tags tied to everything a visitor could bring.
- Used on: a repair-café mockup (the next date on a big luggage tag, eight hanging manila tags for "what you can bring", plain 3px notices and buttons).

## Swatch book

`tests/parts/shapes.html` shows every option of every layer, then every starting point, each on a light page and a dark one side by side; open it in a browser to choose by eye. Every swatch holds the same things, so only the shapes change: a sheet, a small picture (a night view drawn once and coloured by the band names), two labels (a date and "New"), a field drawn as if it had the keyboard so its focus ring shows, the main button, a tick box and a round choice. It borrows the light part's warm shadows and draws no frames. It writes the layer classes short (`co-hand-cut` for corners: hand-cut, and `ct-`, `la-`, `pi-` for the others) and calls its labels `.label` and its picture `.pic`; the assembly code is the same CSS on the page's own hooks, `.tag` and `.badge` for labels and `.picture` (or the image inside it) for pictures, with the layer's values on the page root. It is built by `tests/parts/source/shapes.py` from `shapes-template.html` beside it; run `python3 shapes.py ../shapes.html` there to rebuild it.

## Not covered yet

- **Shapes on whole sections.** A section cut at a slant, a band with a rounded top, a wave between sections: those are edges between sections, the frames part's.
- **Icons.** An icon's own corners (rounded or square line ends) belong to picture style; it should agree with the corners here, and nothing checks that it does.
- **`corner-shape` everywhere.** When Safari ships it, the ticket, the notch and the tag's point could be drawn with `scoop`, `notch` and `bevel`, so the edge, focus ring and shadow follow the shape with no `::before`. Recheck R11 then.
- **`shape()` and `border-shape`.** Newer CSS for drawing any outline with responsive units; not tried here.
- **Measured checks.** Nothing in `check` or `audit` counts the radii on a page or flags a clipped button. Both would be easy: a mixed set of radii is the general guide's "one radius" tell, and a clipped element with a focus ring is a bug.
- **A real page.** The swatches are small. The first site made from these layers should be one of the existing mockups rebuilt from its starting point and put beside the original.

## Sources

Read on 2026-10-07. Six kinds of source: design systems (R1 to R4), craft writing by people who make interfaces (R5 to R9), the web platform's own references (R10 to R14, R16), accessibility (R13 to R16), research on how shapes are felt (R17 to R19), and a survey of what products do (R20). The mockups made with the skill are the seventh: their CSS is quoted in each option's "Used on". Material's own shape page would not open (its values here are from a search result and from Material Web's theming page).

- R1 Material Design 3, shape: corner radius scale (none, 4, 8, 12, 16, 28dp, full; read from a search result) and Material Web, theming: shape ("'cut' corners are not supported"): m3.material.io/styles/shape/corner-radius-scale, material-web.dev/theming/shape
- R2 Radix Themes, radius (none, small, medium, large, full; "when set to full, a Button becomes pill-shaped, while a Checkbox will never become fully rounded to prevent any confusion between it and a Radio"): radix-ui.com/themes/docs/theme/radius
- R3 Atlassian Design System, radius (2, 4, 6, 8, 12, 16px and full; small for "labels, lozenges, timestamps, tags", medium for "buttons, inputs", large for "cards"; full for "avatars, names, user-related UI"; a focus radius 2px larger): atlassian.design/foundations/radius
- R4 The National Archives, designing our button ("square buttons are perceived as more formal than rounded buttons and so they can sometimes appear scary"; a small but noticeable radius): nationalarchives.gov.uk/blogs/digital/designing-our-button/
- R5 Refactoring UI, choose a personality, a community summary ("If those corners are very rounded, the app will feel playful. If those corners are square, or perhaps only slightly rounded, the app will feel serious"; "choosing a value and sticking with it"): rfui-docs.onrender.com/choose-a-personality
- R6 Cloud Four, the math behind nesting rounded corners ("outerRadius - gap = innerRadius"): cloudfour.com/thinks/the-math-behind-nesting-rounded-corners/
- R7 Ahmad Shadeed, a football ticket in CSS and SVG (four ways to cut the notches; masks with radial gradients keep their circles; painted circles fail "when the background color change[s]"): ishadeed.com/article/football-ticket-css-svg/
- R8 Smashing Magazine, responsive multi-line ribbon shapes, part 2 (clip-path for the ends, masks for the cuts, `padding-inline: 1lh` so the ends grow with the text): smashingmagazine.com/2023/11/css-responsive-multi-line-ribbon-shapes-part2/
- R9 Smashing Magazine, beyond border-radius: what corner-shape unlocks ("it does apply to ... outlines, box shadows, and backgrounds. That's the thing that the clip-path property could never do"; use it as progressive enhancement): smashingmagazine.com/2026/03/beyond-border-radius-css-corner-shape-property-ui/
- R10 MDN, corner-shape (round, squircle, bevel, scoop, notch, square, superellipse(); background, border, outline, box-shadow and overflow follow it; needs a border-radius): developer.mozilla.org/en-US/docs/Web/CSS/corner-shape
- R11 Can I use, corner-shape (Chrome and Edge 139+, Firefox 160+, Safari in Technology Preview only, about 70% of visitors): caniuse.com/mdn-css_properties_corner-shape
- R12 MDN, clip-path (circle, ellipse, polygon, inset and rect with `round`, path, shape()): developer.mozilla.org/en-US/docs/Web/CSS/clip-path
- R13 W3C, CSS Masking Level 1 (a clip hides "content, background, borders, text decoration, outline ... of the element"; "pointer-events must not be dispatched on the clipped-out (non-visible) regions"): w3.org/TR/css-masking-1/
- R14 Outline and border-radius in browsers (outlines follow border-radius from Chrome 94, Firefox 88 and Safari 16.4; WebKit bug 20807): docs.w3cub.com/css/outline, webkit.org/b/20807
- R15 WCAG 2.2, understanding target size (minimum) (for a target that "is clipped, has rounded corners, or ... a more complex clickable SVG shape", measure its bounding box): w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- R16 MDN, forced-colors (background-color, border-color and outline-color forced to system colours; box-shadow and gradients removed; "use a border instead"): developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors
- R17 Bar and Neta, humans prefer curved visual objects, Psychological Science 2006 (14 people, 140 pairs; read from a summary): nmr.mgh.harvard.edu/publications/journal_articles/743
- R18 Bertamini, Palumbo and others, do observers like curvature or do they dislike angularity?, British Journal of Psychology 2016 (a preference for curves, not a fear of angles; 14 to 36 people per experiment, abstract shapes): pmc.ncbi.nlm.nih.gov/articles/PMC4975689
- R19 Jiang, Gorn, Galli and Chattopadhyay, does your company have the right logo?, Journal of Consumer Research 2016 (round logos call up softness, angular ones hardness; no effect when visual memory was busy; read from the abstract): research.polyu.edu.hk/en/publications/does-your-company-have-the-right-logo-how-and-why-circular-and-an/
- R20 Lazyweb Research, what corner radius do modern products use for primary buttons? (514 design systems, July 2026: 32.3% pill, 27.0% 7 to 12px, 18.3% 21 to 40px, 10.9% 1 to 6px, 8.6% 13 to 20px, 2.9% square): experiments.lazyweb.com/research/what-button-corner-radius-is-standard
