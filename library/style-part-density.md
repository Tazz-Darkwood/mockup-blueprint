---
name: Density (a part guide)
summary: How much space a page leaves and how it is used, in layers that switch on their own - the spacing scale, how full each screen is, how things are arranged, how wide the page runs and the rhythm from section to section - from one thing at a time on an open page to a packed screen with every gap filled. It owns every gap, the page width and the columns; other parts decide what fills the space. Each layer works on a light page and a dark one, and can be picked with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: research online (six kinds of source, listed under Sources), measurements of 13 mockups made with the skill, the problems four of them met with this part's first version, and the feel guides named in each option
---

# Density

A part guide. It covers the space on a page: the size of every gap, how much of each screen is left open, how things are arranged across the screen, how wide the page runs, and how one section follows the next. It is made of five layers, each one decision that switches on its own: **spacing**, **fill**, **layout**, **width** and **rhythm**. A site picks a starting point whole, or a starting point with one layer changed, in its own guide and in the blueprint as `project.style.parts`: `{"density": "balanced"}`, or `{"density": {"start": "busy", "layout": "single-column"}}`. The pick wins over the feel guide for density only. The general guide's accessibility minimums (contrast, text size, tap size) still hold whatever is picked, and so do its rules on space: one spacing scale, more space between groups than within them, a maximum width for reading text.

**This part owns how much and where, never what.** It decides how big the gaps are, how much of each screen is open, whether the gaps hold decoration, and where that decoration may go. What the decoration *is* belongs to other parts: the drawings on the ground to background, the bands and ornaments between sections to frames, what sheets are made of to materials, the marks drawn on headings to lettering, pictures to picture style. So "busy" here means every gap holds something; the background's detailed ground or a frame's drawn band is what is in it.

**This part does not decide how bright or dark a page is.** That is the colour part's tone (and, when guides are stacked, the lead's). The first version of this guide said a busy page "keeps one bright thing and the rest stays dark or muted"; on a bright repair-café page led by the warm guide that sentence fought the lead's bold colour. A packed page can be a sunflower pegboard or a dark stone wall. Every layer here is drawn with the shared colour names, and its swatch book shows each one on a light page and a dark one.

**Words never lose their calm patch.** However full the page, reading text, fields and buttons sit on something plain (`--surface`), padded by the page's `--pad`, so their contrast is measured on a known colour.

## How it is built

The spacing layer sets the scale and five names for how it is used. Every other part uses these names for its gaps, never its own numbers, so that changing the spacing changes the whole page at once.

| Property | Set by | What it is |
|---|---|---|
| `--space-1` to `--space-9` | spacing | the one scale. Steps 1 to 6 (4, 8, 12, 16, 24, 32 pixels) are the same in every option; steps 7 to 9 change with the option and grow with the screen |
| `--gap-inside` | spacing | between the parts of one thing: a label and its field, a name and its date |
| `--gap-items` | spacing | between things in a list or a row of tiles |
| `--gap-groups` | spacing | between groups inside a section, and below a section's heading |
| `--gap-sections` | spacing | between sections. A section gap with a drawn band in it (frames) still counts as this |
| `--pad` | spacing | inside a sheet, panel or card: the calm patch round words |
| `--gutter` | spacing | the page's side margin, smallest on a phone |
| `--page` | width | the widest the page's content runs (`none` on a full-bleed page's bands) |
| `--edge` | width | the space from the window's edge to the content: `max(var(--gutter), (100cqi - var(--page)) / 2)` |
| `--density-tile` | fill | the narrowest a tile in a grid may be before the row wraps |

Two choices run through the whole guide:

- **Small steps never change.** Steps 1 to 6 are the space inside a control and between things you tap (8 pixels at least, R26), so a snug page and an airy one have the same buttons and fields. Only the large steps move. GOV.UK's responsive scale does the same: units 0 to 3 are equal at every size, and only the larger ones grow on a wide screen (R2).
- **Large steps grow with the container, not with breakpoints.** Each is a `clamp()` from its phone value at 390 pixels to its wide value at 1440 (R10, R14), written in `cqi`: a hundredth of the nearest container's width, and of the window when there is none (R11). So the same tokens work for a whole page and for a panel in a sidebar. Put the container on a wrapper round the sections, not on `<body>`: a size container is a containing block for `position: fixed`, which would catch the page's fixed bars.

The code every pick needs (the fixed steps, the page as a container, each band's place on the page) is under Base, below.

### Space shows what belongs together

The general guide's rule, made exact: **each of the four gaps is at least one and a half times the one inside it on a wide screen, and never equal to it on a phone.** That is what lets a reader see a group without a box round it (R17). The options below all keep it. When a page feels crowded or loose, check this before changing anything else: the usual fault is a gap between items as large as the gap between groups, so everything floats apart at the same distance.

## How full: two ways to check it

The first version of this guide gave figures ("7 to 15 per cent open space", "five to sixteen pieces of decoration per screen") that came from a one-off script, and no command could measure them, so a site could not be checked against them. Both ways below can be checked: the first by anyone with a screenshot, the second by a script, written as a proposal for `audit`.

**The box count, by eye.** Take a screenshot of the first screen at a desktop size (1280 by 800, or the swatch book's 1600 by 900). Lay a grid of 10 by 6 boxes over it. Count two things: **empty boxes**, holding nothing but the ground, a plain band or the plain part of a sheet; and **decoration-only boxes**, holding drawn things but no words, pictures or controls. A box with any word, picture or control in it counts as content. The swatch book draws this grid on every fill swatch and starting point and gives both numbers.

| Fill | Empty boxes (of 60) | Decoration-only boxes | Swatch book |
|---|---|---|---|
| Open | 15 or more | none | 18 to 31 on the open starting points |
| Balanced | about 12 to 25 | 1 to 4 | 18 to 26 empty, 2 to 4 decoration |
| Full | under 10 | 0 to 2 | 4 to 6 |
| Packed | under 10 | 5 or more, where there are margins to fill | 2 to 10 empty, 5 to 13 decoration (2 on the fill swatch, which runs wide and has almost no margin) |

**A measure from a screenshot, for `audit`.** Tried as a prototype on 13 mockups (the figures below). It follows the white-space measure of Miniukovich and De Angeli as coded in Aalto's interface metrics (R20, R21), with the page's own boxes standing in for their element detector.

1. Open the page at 1280 by 800 (and again at 390 by 844) and take a whole-page picture.
2. Mark **content**: every box of visible text (each line, from the text's own client rects), every image, video, canvas, control and SVG that is not `aria-hidden`, each grown by 4 pixels.
3. Cut the picture into 16-pixel cells. A cell is **plain** if it is not content and the standard deviation of its luminance (0 to 255, sampled every other pixel) is under 5; grain at the default strength stays under that, graph-paper lines and drawn signs do not.
4. **Open space** is plain cells that lie inside some 5-by-5-cell square (80 pixels) that is plain all through: an opening, in image terms, so a 20-pixel gap between two tiles is not open space. **Decoration** is cells that are neither content nor plain.
5. Report open, decoration and content as shares of each screen (800 pixels down) and of the whole page, and compare them with the picked fill.

What the prototype found (whole page at 1280; open / decoration per cent):

| Mockup | Picked or judged | Open | Decoration |
|---|---|---|---|
| A tutor's site | clean | 66 | 4 |
| A quiet gallery of pots | minimal | 62 | 1 |
| An observatory | clean, with a scene | 56 | 8 |
| A small game's front page | clean | 47 | 3 |
| A soap maker's shop | balanced | 45 | 9 |
| A volunteer page | balanced | 42 | 7 |
| A poetry site | balanced | 30 | 19 |
| A night market | busy | 25 | 17 |
| A field notebook | balanced | 15 | 36 |
| A dark, painterly joke site | busy | 15 | 32 |
| A repair café | busy | 7 | 33 |
| A game-interface page | full but quiet | 45 (first screen 20) | 21 (first screen 35) |

So, at 1280 wide: **open** is open space 50 per cent or more with decoration 10 or less; **balanced** is 25 to 50 open; **full** and **packed** are under 25 open, told apart by decoration (under 20 for full, 25 or more for packed). Two lessons from it:

- **The measure sees the background.** The field notebook picked balanced, but its ground is graph paper, and ruled lines everywhere measure as packed; a painted scene behind a game screen measures as decoration too. That is right: the eye sees them as fullness. A site that wants balanced on a ruled or painted ground lowers the ground's strength (the colour part's `--texture-strength`) or accepts that it is fuller than it said.
- **On a phone, open space no longer tells the options apart.** At 390 wide every mockup was under 30 per cent open, most under 20, because a phone has no room for empty margins (the first version's finding, confirmed). Decoration still does: 7 per cent or less on the open and clean pages, 24 to 33 on the packed ones. So on a phone, check the decoration share and the gaps, not the open space.

Building it into `audit` needs no new library: the browser draws the picture into a canvas and does the counting, in about sixty lines. It cannot judge whether the open space is well placed; the general guide's squint test still does that.

## Choosing

Start from a starting point (below), then change a layer if the brief asks for it.

| Starting point | What it feels like | Suits best | Fights |
|---|---|---|---|
| Minimal | One thing at a time on an open page; quiet and slow | Single works to look at; pages with one job (signing in) | A shop with many items; thin content, which looks unfinished |
| Clean | Everything in order, nothing extra | Professional; facts to compare and trust | Warm, where it reads as cold |
| Balanced | Lively, with room to breathe | Warm; artistic; the default when the brief does not say | Little |
| Full but quiet | The whole window used, like a game screen or a tool, every panel calm inside | A working tool; a game screen | Long reading; professional |
| Busy | Fill the frame: narrow gaps, every one holding something | A detailed ground of any colour; a world to get lost in | Professional; a page whose job is one quick form |
| Warm | Bands edge to edge, people at the top, a few marks | The warm guide | A spare brief |
| Artistic | The work large, set off the centred column | The artistic guide | Many small items to compare |
| Professional | An orderly grid with generous space | The professional guide | Warm, unless the signature is designed |
| Civic | One readable column, nothing extra | Public services, forms, guidance | Shops, play |
| Sorcery | A scene at the top, then every gap filled | The sorcery guide | Anything calm or official |
| Gilded dark | Heavy panels over one big painted world | The game-interface guide | Long reading |
| Lantern fair | Bands of stalls, bunting in every gap | A night market; a festival | Daytime services |
| Almanac plate | Sheets on one half, a scene on the other, turn about | A society, an observatory, a garden | Shops |
| Catalogue of glazes | One piece to a screen, particulars in the margin | A small gallery or maker | Many items to compare |
| Field journal | Pages laid down a little out of line | A club, a naturalist | Professional |
| Repair cafe | A full board: tags four across, a band at every break | A busy, hand-made community page | A calm brief |

How to choose:

- **Ask how many things a visitor needs on one screen, and what the space between them is for.** One thing to look at closely: minimal. Many facts to compare and trust: clean. A club or a maker with personality: balanced. A tool used for a long sitting: full but quiet. A world to get lost in: busy. Then the brief's line on how full the page should feel names the fill.
- **Fill and spacing go together.** Open fill wants airy or standard spacing; packed wants snug. A packed page with airy gaps has wide empty bands between its full sections and reads as unfinished; an open page with snug gaps reads as cramped and empty at once.
- **Density is not the template test.** A page passes or fails "It must not look like a template" (the general guide) at any density. The one mockup the owner called a template (a volunteer page, "very plain ... like I made it with a cheap make-your-own-website tool") measured almost exactly like a clean one; what made the tutor's site clean and not a template was what it chose, not how full it was.
- **One site may use two densities,** page by page, and that is a decision to write down. A small game made its game screen full but quiet and every other page minimal; a sign-in page is usually quieter than the front page whatever was picked.
- **A site picked from parts alone still needs this part.** With no feel guide stacked, nothing else decides the page width or the columns; a parts-only gallery had to settle its margin column and page width itself. Pick at least a starting point here.

## Base

The code every pick needs, lifted into a site's stylesheet whatever the layers say (`blueprint.py style css`). It expects the shared hooks: a `.page` wrapper round everything (the container; fixed bars sit outside it), the page's sections as `.band`s (directly in `.page`, or in a `<main>` there), words on `.sheet`s and `.panel`s. A group of sheets (any element in a band holding two or more `.sheet`s) is the list or the tiles, as the layout says. Density's own classes, for where the hooks are not enough: `.density-list`, `.density-tiles` (with `.density-small`), `.density-spread`, `.density-particulars` (margin column), `.density-weighted` (a 2:1 band), `.density-moment`, `.density-bleed` and `.density-bleed-right`.

Two things other parts need from layout are here too. Lettering caps its biggest heading by the width of the box it is in (`cqi`), so a band, sheet or panel holding an `h1` is an inline-size container; only those, since inside a container every fluid step written in `cqi` follows that box, not the page (a panel that sizes to its content, a popover say, needs a width of its own if it holds an `h1`). And a button's box (its height and padding) is spacing; its shape and edge are the shapes and frames parts'. A sheet's first child is its first one a reader sees: the empty spans other parts put in a sheet (`aria-hidden`) do not count.

**Density lays no colour.** Where a layout or a fill needs something behind a section (every other band, a band laid out as a panel, a patch behind words straight on a busy band), it reads the background part's `--background-alternate`, `--background-patch` and `--background-patch-ink`, falling back to `--surface` and `--ink` when no background is picked, and the fill of every other band is written so that any band colour the background sets wins.

How a band keeps to the page: it stands in from each side by `--edge - --density-band-inset` and pads its content in by `--density-band-inset`. The inset is 0 unless the width is full bleed, which sets it to `--edge`, so the band meets the window and its content still lines up with the page.

```css assemble
/* density's base: steps 1 to 6 (the same in every option), the page as a container, and each band's place */
& {
  --space-1: 0.25rem; --space-2: 0.5rem; --space-3: 0.75rem; --space-4: 1rem; --space-5: 1.5rem; --space-6: 2rem;
  --page: 72rem; --density-tile: 15rem; --density-band-inset: 0px;
  --edge: max(var(--gutter, 1rem), (100cqi - var(--page)) / 2);   /* cqi resolves where it is used: inside .page */
}
body { margin: 0; }                                  /* the side margin is --gutter, nothing else */
.page { container: page / inline-size; }             /* the sections' wrapper, not <body>: a size container would catch fixed bars */
.band { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--gap-groups); align-content: start;
  margin-block: 0 var(--gap-sections);
  margin-inline: calc(var(--edge) - var(--density-band-inset)); padding-inline: var(--density-band-inset); }
.page > .band:last-child { margin-block-end: 0; }
:where(.page > header, .page > footer).band { padding-block: var(--space-5); }   /* the bars at the top and foot */
.band .band { margin-inline: 0; padding-inline: 0; }
:is(.sheet, .panel) { padding: var(--pad); }         /* the calm patch round words */
:is(.sheet, .panel) > :not([aria-hidden="true"]):not(:not([aria-hidden="true"]) ~ *) { margin-block-start: 0; }   /* the first child a reader sees */
:is(.band, .sheet, .panel):has(> h1) { container-type: inline-size; }   /* lettering caps the biggest heading by cqi: its own box, not the window */
.btn { min-height: max(44px, 2.75rem); padding: var(--space-2) var(--space-5); gap: var(--space-2); }   /* 44 pixels to tap; the shape is the shapes part's */
:is(.field, select, textarea, input:not([type="checkbox"], [type="radio"], [type="submit"], [type="button"], [type="reset"], [type="hidden"])) { min-height: max(44px, 2.75rem); padding: var(--space-2) var(--space-3); box-sizing: border-box; max-width: 100%; }
input:is([type="checkbox"], [type="radio"]) { width: 1.5rem; height: 1.5rem; margin: 0 var(--space-2) 0 0; vertical-align: middle; }   /* at least 24 pixels */
label:has(> input:is([type="checkbox"], [type="radio"])) { display: inline-flex; align-items: center; min-height: max(44px, 2.75rem); }   /* the whole label is the target */
nav a { display: inline-flex; align-items: center; min-height: max(44px, 2.75rem); }   /* links in a bar are things to tap */
:is(.sheet, .panel) > :last-child { margin-block-end: 0; }
[data-deco] { pointer-events: none; }
```

## Layers

### Spacing
- Layer: spacing
- Owns: the size of every gap: steps 7 to 9 of the spacing scale, the side margin, and which step each of the five gaps (inside, items, groups, sections, padding) takes. It does not own the size of text (lettering) or of controls (steps 1 to 6 never change).
- Default: standard

#### Airy
- Id: airy
- Status: draft
- Looks like: large gaps that grow most on a wide screen: sections 72 to 144 pixels apart, things in a list 40 to 64, a wide margin. One thing at a time, read slowly, the way a printed book leaves wide margins.
- Made with: steps 7 to 9 at their largest, each a `clamp()` from its phone value to its wide value, and a side margin that grows to 7rem. Items take step 7, so even a list reads as a sequence of separate things.

```css assemble
/* spacing: airy. Steps 7 to 9 at their largest; items take step 7, so even a list reads as separate things */
& {
  --space-7: clamp(2.5rem, 1.943rem + 2.29cqi, 4rem);     /* 40 to 64 */
  --space-8: clamp(3.5rem, 2.571rem + 3.81cqi, 6rem);     /* 56 to 96 */
  --space-9: clamp(4.5rem, 2.829rem + 6.86cqi, 9rem);     /* 72 to 144 */
  --gutter: clamp(1.25rem, -0.886rem + 8.76cqi, 7rem);
  --gap-inside: var(--space-3); --gap-items: var(--space-7); --gap-groups: var(--space-8);
  --gap-sections: var(--space-9); --pad: var(--space-6);
}
```

- Careful: the spacing most likely to look unfinished. A poetry site's first version, set like a book with large poems on an open page, was liked for its feel and still read as "too empty"; it went to standard spacing, keeping the paper, ink and type. Use it where each thing is worth looking at on its own, or for pages with one job. On a phone it shrinks nearly to standard by itself; keep at least `--space-7` between items there or it becomes a plain list. The open space must not push the main heading or the one action below the first phone screen (`mobile/first-screen`).
- Light and dark: the same gaps. On a dark page large empty areas read as darker and heavier than the same area on a light one; a dark airy page needs the ground to carry a little texture or tone (background), or the open space reads as a hole.
- Personality: calm, serious
- Goes with: `density: fill open`; `density: width standard` or `narrow`; `background: grain` (the space is a material, not blank); `frames: none` (let space group things).
- Used on: a quiet gallery of pots (pieces `--space-9` apart), the first version of a poetry site (items `--space-8` apart, sections `--space-9`), an observatory (96 pixels between bands), and the inner pages of a small game site.

#### Standard
- Id: standard
- Status: draft
- Looks like: the general guide's scale: generous between sections (56 to 96 pixels), closer inside them, 24 between things in a list. A normal page.
- Made with: the general guide's steps, with 7 to 9 made fluid so a phone does not inherit a desktop's 96-pixel gaps (GOV.UK's scale does the same, R2).

```css assemble
/* spacing: standard. The general guide's scale, with 7 to 9 fluid */
& {
  --space-7: clamp(2rem, 1.629rem + 1.52cqi, 3rem);       /* 32 to 48 */
  --space-8: clamp(2.5rem, 1.943rem + 2.29cqi, 4rem);     /* 40 to 64 */
  --space-9: clamp(3.5rem, 2.571rem + 3.81cqi, 6rem);     /* 56 to 96 */
  --gutter: clamp(1rem, -0.114rem + 4.57cqi, 4rem);       /* 16 on a phone, as Material's compact margin */
  --gap-inside: var(--space-2); --gap-items: var(--space-5); --gap-groups: var(--space-7);
  --gap-sections: var(--space-9); --pad: var(--space-5);
}
```

- Careful: the tightest ratio is between items and groups on a phone (24 to 32). Where a list sits right under another group, give the list its own heading, or the two run together.
- Light and dark: the same on both.
- Personality: any
- Goes with: `density: fill open` or `balanced`; any background, frames or material.
- Used on: a tutor's site, a volunteer page, a soap maker's shop, a field notebook (sections `--space-8`, items `--space-7` on a phone), the final version of a poetry site; and the general guide's starting tokens.

#### Snug
- Id: snug
- Status: draft
- Looks like: small gaps, nothing over 48 pixels: sections 32 to 48 apart, things in a list 16. A full page that still groups clearly.
- Made with: steps 8 and 9 held to 48 at most, so nothing larger exists, and a margin of 12 pixels on a phone. The gap between sections is small enough that it needs help: a line, a band or a change of ground at each break (frames or background).

```css assemble
/* spacing: snug. Nothing over 48 pixels; each section break needs a line, band or change of ground (frames, background) */
& {
  --space-7: clamp(1.75rem, 1.471rem + 1.14cqi, 2.5rem);  /* 28 to 40 */
  --space-8: clamp(2rem, 1.629rem + 1.52cqi, 3rem);       /* 32 to 48: the largest step */
  --space-9: var(--space-8);
  --gutter: clamp(0.75rem, 0.286rem + 1.9cqi, 2rem);
  --gap-inside: var(--space-2); --gap-items: var(--space-4); --gap-groups: var(--space-5);
  --gap-sections: var(--space-8); --pad: var(--space-4);
}
```

- Careful: "more space between groups than within" still holds, inside a smaller range: 8, 16, 24, 32 to 48. With this little space, a section break needs a visible edge as well; without one, sections run together. Tap targets keep 8 pixels between them (steps 1 to 6 do not change). On a phone the margin is 12 pixels, so there is almost no ground at the sides to decorate.
- Light and dark: the same on both. Narrow gaps on a dark page read as seams; on a light page as joins. Both work.
- Personality: playful, dramatic, friendly
- Goes with: `density: fill full` or `packed`; `frames: wavy-edge`, `torn-paper` or `carved-plate` for the section breaks; `background: detailed-ground`.
- Used on: a repair café (the scale stops at `--space-7`; sections `--space-5` apart with a drawn band), a night market (stops at `--space-7`; gutters 16, 32 and 48), a dark, painterly joke site, a small shop in two versions, and a game-style joke site.

#### Compact
- Id: compact
- Status: draft
- Looks like: the smallest gaps: rows 8 apart, panels 16, sections 24. For tools, tables and readouts used for a long sitting, where seeing many things at once is the job.
- Made with: steps 7 to 9 held to 32, and the gaps taken from the bottom of the scale. Controls stay their full size: compact moves things closer, it does not shrink them. Material's density scale takes 4 pixels off a component's height per step (R6) and Gmail's compact view drops the space between messages (R7); both are for pointers, not fingers.

```css assemble
/* spacing: compact. Things closer, never smaller: controls keep their size */
& {
  --space-7: clamp(1.5rem, 1.314rem + 0.76cqi, 2rem);     /* 24 to 32: the largest step */
  --space-8: var(--space-7); --space-9: var(--space-7);
  --gutter: clamp(0.75rem, 0.471rem + 1.14cqi, 1.5rem);
  --gap-inside: var(--space-1); --gap-items: var(--space-2); --gap-groups: var(--space-4);
  --gap-sections: var(--space-5); --pad: var(--space-3);
}
@media (pointer: coarse) { & { --gap-items: var(--space-3); } }  /* fingers: a little more room between rows */
```

- Careful: never for reading. Rows of controls stay 44 pixels tall on a touch screen and 24 at the least anywhere (the phone guide); in a table of rows, the row is the target. Use it for one screen (the tool, the game, the dashboard), and link from it to pages with another spacing for anything long.
- Light and dark: the same on both. Dark tools are common; with gaps this small, the edge of each panel (frames) does the grouping.
- Personality: serious, dramatic
- Goes with: `density: fill full`; `density: layout panels`; `frames: hairline` or `riveted-metal`; `materials: metal-and-dark-glass`.
- Used on: the game screen of a small shared-world game (19 controls and readouts to a screen, gaps `--space-3` to `--space-5`) and the interface version of a game-style joke site.

### Fill
- Layer: fill
- Owns: how much of each screen is left open, how much optional content is shown, whether the gaps hold decoration, and where it may go. Not what the decoration is: that is the part that draws it.
- Default: balanced

How the parts share it. Every piece of decoration any part draws carries `data-deco` with the least fill that shows it: `few` (balanced and up), `more` and `most` (packed only). Content that only a full page shows (a second panel of readouts, a sidebar of facts) carries `data-fill="full"`. **The background decides what drawings exist; the fill decides how many of them show**, through these tiers: the background draws its signs and tags each one, and the fill picks the tier. The fill then shows or hides whole tiers, and a phone drops one tier. So the background's drawings, the frames' ornaments and the lettering's marks all obey one count. So a background with `drawings: lots` under `fill: balanced` shows only its `few` tier; to show them all, pick `fill: packed`.

Each fill option's code hides the tiers it does not show with `!important`, so a part that draws a sign never has to know the fill, whatever order the stylesheet lands in.

#### Open
- Id: open
- Status: draft
- Looks like: most of each screen is open: nothing in the gaps but the ground. Tiles are large and few to a row. Measured: open space 50 per cent or more, decoration 10 or less; 15 or more empty boxes in the box count, none with decoration alone.
- Made with: every `data-deco` tier hidden, and a wide minimum tile so rows hold few things. The space itself is not blank white: pick a ground with a tone or a little grain (background), or the page is the general guide's "pale ground, white boxes, one accent".

```css assemble
/* fill: open. Nothing in the gaps but the ground; large tiles, few to a row */
& { --density-tile: 19rem; }
[data-deco] { display: none !important; }            /* every tier hidden, whatever part drew it */
[data-fill="full"] { display: none !important; }     /* content only a full page shows */
```

- Careful: an open page has fewer places to show a choice, so the few it has must all show one. With nothing in the gaps, the page needs its signature (one thing made for the site, set large) and a designed repeated item, or it is the template's first tell. A gallery built from parts alone used this part's old list as its plan for where the detail goes: the space is a material, one thing made for the site sits large in it, the page leaves the centred column, no boxes, and the headline is a chosen face. That list now belongs to `start: minimal`.
- Light and dark: on a light page the open space is paper; on a dark page it is a room. Both need tone or texture from the background part to read as chosen.
- Personality: calm, serious
- Goes with: `density: spacing airy` or `standard`; `background: grain` or `plain` on a toned ground; `frames: none` or `hairline`.
- Used on: a tutor's site (66 open, 4 decoration), a quiet gallery of pots (62, 1), an observatory's sheets (56, 8), a small game's front page (47, 3).

#### Balanced
- Id: balanced
- Status: draft
- Looks like: room round each thing, and a few drawn marks per screen: two or three, on headings and at the edges of sections, never on fields. The open space is there, often coloured or grained. Measured: 25 to 50 per cent open; about 12 to 25 empty boxes, one to four with decoration alone.
- Made with: the `few` tier shown; tiles of a middling size. Marks sit beside words, never under them.

```css assemble
/* fill: balanced. The few tier only; on a phone, one mark to a group */
& { --density-tile: 15rem; }
[data-deco]:not([data-deco="few"]) { display: none !important; }
[data-fill="full"] { display: none !important; }
@container page (width < 40rem) { [data-deco="few"] ~ [data-deco="few"] { display: none !important; } }
```

- Careful: the warm guide's "two or three hand-made marks, then stop". When it starts to feel crowded, check the gaps (inside smaller than between) before taking marks away. A ruled or painted ground makes a balanced page measure as packed (the field notebook); decide which it is meant to be.
- Light and dark: the same marks in `--mark` on both.
- Personality: friendly, calm, playful
- Goes with: `density: spacing standard`; `background: grain`, `coloured-bands` or `material-ground`; `lettering: hand-marks` or `poster-face`.
- Used on: a soap maker's shop (45 open, 9 decoration), a volunteer page (42, 7), a poetry site's final version (30, 19), a field notebook (picked balanced; measures 15, 36 because of its graph-paper ground).

#### Full
- Id: full
- Status: draft
- Looks like: every region of the screen holds content, on plain panels; the gaps between panels are narrow and stay plain. A game screen or a working tool: the fullness comes from what is there to use, not from ornament. Measured: under 25 per cent open, decoration under 20 (a painted scene behind the panels measures as decoration and belongs to the background); under 10 empty boxes.
- Made with: optional content shown (`data-fill="full"`), smaller tiles so more fit, every piece of reading text on a panel, the gap between sections capped at `--space-7`, and no decoration in the gaps.

```css assemble
/* fill: full. Optional content shown, smaller tiles, no wide empty gaps, no decoration; words on a calm patch */
& { --density-tile: 11rem; --gap-sections: min(var(--space-9), var(--space-7)); }
[data-deco] { display: none !important; }
.band > :is(h1, h2, h3, p, .lead) { justify-self: self-start; padding: var(--space-2) var(--space-3);   /* words straight on a band get a calm patch; sheets are painted by materials */
  background: var(--background-patch, var(--surface)); color: var(--background-patch-ink, var(--ink)); border-radius: var(--radius-small, 3px); }   /* its colour is the background part's */
```

- Careful: panels over a picture are at least 90 per cent opaque, or contrast changes with whatever passes behind them (`check` measures it from a picture). Bars that stay on screen take less than a quarter of a phone's screen. On a phone the panels stack in one column; decide the order. Long reading text does not belong here; link to a page with another fill.
- Light and dark: on a light page the panels are sheets on a desk; on a dark page they are lit screens. The gaps stay the ground on both.
- Personality: serious, dramatic, playful
- Goes with: `density: spacing compact` or `snug`; `density: layout panels` or `grid`; `frames: hairline` or `riveted-metal`; `background: painted-ground` for a game.
- Used on: the interface version of a game-style joke site (its brief: "something in every part of the window, but every panel calm enough to read in"; first screen 20 open), and the game screen of a small shared-world game (its brief: "busy but quiet").

#### Packed
- Id: packed
- Status: draft
- Looks like: full, and every gap holds something: a drawn band at each section break, signs in the margins, a worked ground. The only calm patches are behind words and controls, each just big enough for what is on it. Measured: under 25 per cent open with decoration 25 or more; under 10 empty boxes and 5 or more with decoration alone where the page has margins to fill.
- Made with: every tier shown; the gap between sections capped at `--space-7` and holding a band (frames); every piece of reading text, every field and button on a calm patch in one shared colour (`--surface`), padded by `--pad`. Signs are placed one by one (each its own size, place and tilt, never in rows), more on a wide screen and fewer on a phone. What they are comes from the background, frames and lettering parts; how many and where comes from here.

```css assemble
/* fill: packed. Every tier shown, the phone drops the most tier; words on calm patches; signs may run off the edge */
& { --density-tile: 11rem; --gap-sections: min(var(--space-9), var(--space-7)); }
.band > :is(h1, h2, h3, p, .lead) { justify-self: self-start; padding: var(--space-2) var(--space-3);
  background: var(--background-patch, var(--surface)); color: var(--background-patch-ink, var(--ink)); border-radius: var(--radius-small, 3px); }   /* its colour is the background part's */
.band { position: relative; }                     /* signs are placed inside their band */
.page { overflow-x: clip; }                       /* clip, not hidden, so sticky still works */
@container page (width < 40rem) { [data-deco="most"] { display: none !important; } }
```

- Careful: packed means full of detail, not full of light or dark: the colour part decides how bright the page is. A bright repair café and a dark wizard's hall are both packed. Signs sit behind or beside things, never over words or controls, and none looks like something to press; they are `aria-hidden`, and text drawn inside them (the numbers on a drawn tape measure) is decoration too, which the audit once counted as small text. Contrast is measured on the calm patch's own colour; a patch too small to hold its words is the usual failure. On a phone the margins are about 12 pixels, so the bands and the marks inside the calm patches' margins do most of the work. Packed takes the most drawing of any fill; picked without the time to draw it, it comes out as clutter, which is the failure maximalist design is warned about (R24): density is a tool to shape the experience, and every piece in the gaps should belong to the site's world.
- Light and dark: the same tiers on both; the signs are `--mark`, the bands `--line` or `--mark`. On a dark page the calm patches are the lighter `--surface`; on a light page they are paler than the worked ground.
- Personality: dramatic, playful
- Goes with: `density: spacing snug`; `background: detailed-ground`; `frames: carved-plate`, `inked-panel` or `wavy-edge`; `materials: parchment-and-ink` or `stone-and-chalk` on a dark page, `cut-paper-on-felt` or `paper-and-tape` on a bright one.
- Used on: a repair café on a sunflower pegboard (7 open, 33 decoration), a dark, painterly joke site (15, 32), a night market (25, 17), two versions of a small shop and a game-style joke site.

### Layout
- Layer: layout
- Owns: how things are arranged across a wide screen: how many columns, what sits beside what, and how it comes down to a phone. Not the width of the page (width) or the gaps (spacing).
- Default: single-column

Every layout comes down to one column on a phone (the phone guide: one column for anything meant to be read, two across only for small tiles), and the order things stack in is decided, not left to the columns. Use container queries so a layout changes where its own space runs out (R11, R12), and `grid-template-columns: minmax(0, 1fr)` so long words never push a column wider.

#### Single column
- Id: single-column
- Status: draft
- Looks like: one column, things in the order a visitor needs them; reading text held to the measure, pictures and lists the full width of the page.
- Made with: one track; repeated items as rows, a small picture beside the words.

```css assemble
/* layout: single column. One track; a group of sheets is a list of rows, a small picture beside the words */
.band :is(p, .lead) { max-width: var(--measure, 66ch); }   /* the measure is lettering's; density only reads it */
:is(.density-list, .band > :has(> .sheet ~ .sheet)) { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--gap-items); }
:is(.density-list, .band > :has(> .sheet ~ .sheet)) > :has(> .picture) { display: grid; grid-template-columns: 10rem minmax(0, 1fr); column-gap: var(--gap-items); align-content: start; }
:is(.density-list, .band > :has(> .sheet ~ .sheet)) > :has(> .picture) > * { grid-column: 2; }
:is(.density-list, .band > :has(> .sheet ~ .sheet)) > :has(> .picture) > .picture { grid-column: 1; grid-row: 1 / span 3; margin: 0; }
@container page (width < 40rem) { :is(.density-list, .band > :has(> .sheet ~ .sheet)) > :has(> .picture) { grid-template-columns: 7rem minmax(0, 1fr); } }
```

- Careful: one centred column with straight edges is the template's tell 8 (the general guide). On a wide screen with `width: standard`, a single column leaves wide empty sides; pick `width: narrow` with it, or give the column something that leaves it (a picture that bleeds, a margin note).
- Light and dark: the same on both.
- Personality: any
- Goes with: `density: width narrow`; any fill.
- Used on: the default of the phone guide; a dark, painterly joke site (one column of sheets on a wall); a civic, form-led page.

#### Margin column
- Id: margin-column
- Status: draft
- Looks like: headings, names, dates and particulars in a narrow column beside the main one, as in a book or a museum catalogue. The page leaves the centred column without any tilt or overlap.
- Made with: two tracks, a narrow one of 10 to 15rem and the rest; section headings and particulars go in the first.

```css assemble
/* layout: margin column. Headings and particulars in a narrow column beside the main one */
.band:not(header, footer) { grid-template-columns: minmax(10rem, 15rem) minmax(0, 1fr); column-gap: var(--gap-groups); }
.band:not(header, footer) > * { grid-column: 2; }
.band:not(header, footer) > :is(h2, .label, .density-particulars) { grid-column: 1; }
.band :is(p, .lead) { max-width: var(--measure, 66ch); }
:is(.density-list, .band > :has(> .sheet ~ .sheet)) { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--gap-items); }
@container page (width < 46rem) { .band:not(header, footer) { grid-template-columns: minmax(0, 1fr); } .band:not(header, footer) > * { grid-column: 1; } }
```

- Careful: on a phone the particulars come under or over the thing they describe; decide which (the gallery put each pot first, then its caption). The margin column holds short text only; anything long belongs in the main column.
- Light and dark: the same on both.
- Personality: calm, serious
- Goes with: `density: spacing airy`; `density: fill open`; `lettering: soft-serif` or `sober-pair`.
- Used on: a quiet gallery of pots (particulars in a 13rem column, 16rem from 64rem); the first version of a poetry site (names and dates in an 11rem column).

#### Two columns
- Id: two-columns
- Status: draft
- Looks like: the main thing and what goes with it, side by side: a heading beside its picture, a passage beside its facts, a list two across.
- Made with: two tracks of equal or 2:1 weight; at narrow widths, one. Every Layout's Switcher does it without a breakpoint (R13).

```css assemble
/* layout: two columns. A band holding two or more sheets, panels or pictures sets them side by side; a list runs two across */
.band:has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)) { grid-template-columns: repeat(2, minmax(0, 1fr)); align-items: center; }
.band:has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)) > :not(.sheet, .panel, .picture) { grid-column: 1 / -1; }   /* its heading and anything else run across both */
.band.density-weighted { grid-template-columns: minmax(0, 2fr) minmax(0, 1fr); }
:is(.density-list, .band > :has(> .sheet ~ .sheet)) { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--gap-items); }
@container page (width < 48rem) { .band:has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)), .band.density-weighted, :is(.density-list, .band > :has(> .sheet ~ .sheet)) { grid-template-columns: minmax(0, 1fr); } }
```

- Careful: decide the phone order (the phone guide: photograph or heading first was split evenly on the sites studied). The sales guide's product page is this layout and is not to be reinvented.
- Light and dark: the same on both.
- Personality: any
- Goes with: `density: width standard`; any fill.
- Used on: a tutor's site (portrait beside the heading); a night market's first band (name left, copy right, from 48rem); the sales guide's product page (5 of 5 shops).

#### Grid
- Id: grid
- Status: draft
- Looks like: many like things in tiles that wrap, as many across as fit: products, events, people, pieces.
- Made with: `auto-fill` tracks with a minimum from the fill (`--density-tile`), so the number across follows the space, with no breakpoint (R14). `min(100%, ...)` keeps one tile from overflowing a narrow screen.

```css assemble
/* layout: grid. A group of sheets wraps as tiles, as many across as fit (the fill sets --density-tile); two sheets or panels side by side */
:is(.density-tiles, .band > :has(> .sheet ~ .sheet)) { display: grid; gap: var(--gap-items); grid-template-columns: repeat(auto-fill, minmax(min(100%, var(--density-tile, 15rem)), 1fr)); }
.band:has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)) { grid-template-columns: repeat(2, minmax(0, 1fr)); align-items: center; }
.band:has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)) > :not(.sheet, .panel, .picture) { grid-column: 1 / -1; }
@container page (width < 40rem) {
  .band:has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)) { grid-template-columns: minmax(0, 1fr); }
  .density-tiles.density-small { grid-template-columns: repeat(2, minmax(0, 1fr)); }   /* small tiles stay two across */
}
```

- Careful: twenty identical rounded cards is the template's tell 2; the grid is the arrangement, and the item must still be designed (the artistic and warm guides). On a phone, only small tiles stay two across.
- Light and dark: the same on both.
- Personality: any
- Goes with: `density: fill balanced`, `full` or `packed`; `frames: card` or `torn-paper`.
- Used on: a repair café (tags four across from 62rem), a night market (bays two then four across; tags two then three), a soap maker's shop, the professional guide's "orderly grid".

#### Staggered
- Id: staggered
- Status: draft
- Looks like: things of different sizes, set off the straight lines: a large piece beside a small one, the next row offset, like an editorial spread or sheets laid on a table.
- Made with: a six-column grid with items spanning different numbers of columns and starting at different lines, some pulled down by a step. The editorial habit of combining four- and six-column grids (R23) and named grid lines for full, content and split areas (R22).

```css assemble
/* layout: staggered. A six-column grid, things spanning different widths and pulled up or down by a step */
:is(.density-spread, .band > :has(> .sheet ~ .sheet)) { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: var(--gap-groups) var(--gap-items); }
:is(.density-spread, .band > :has(> .sheet ~ .sheet)) > :nth-child(6n+1) { grid-column: 1 / span 3; }
:is(.density-spread, .band > :has(> .sheet ~ .sheet)) > :nth-child(6n+2) { grid-column: 5 / span 2; margin-top: var(--gap-groups); }
:is(.density-spread, .band > :has(> .sheet ~ .sheet)) > :nth-child(6n+3) { grid-column: 2 / span 2; }
:is(.density-spread, .band > :has(> .sheet ~ .sheet)) > :nth-child(6n+4) { grid-column: 4 / span 3; margin-top: calc(var(--gap-groups) * -1); }
:is(.density-spread, .band > :has(> .sheet ~ .sheet)) > :nth-child(6n+5) { grid-column: 1 / span 2; }
:is(.density-spread, .band > :has(> .sheet ~ .sheet)) > :nth-child(6n) { grid-column: 3 / span 3; margin-top: var(--gap-groups); }
.band:has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)) { grid-template-columns: repeat(6, minmax(0, 1fr)); align-items: end; }
.band:has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)) > :is(.sheet, .panel, .picture):nth-of-type(odd) { grid-column: 1 / span 3; }
.band:has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)) > :is(.sheet, .panel, .picture):nth-of-type(even) { grid-column: 4 / span 3; }
.band:has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)) > :not(.sheet, .panel, .picture) { grid-column: 1 / -1; }
@container page (width < 40rem) {
  :is(.density-spread, .band > :has(> .sheet ~ .sheet)), .band:has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)) { grid-template-columns: minmax(0, 1fr); }
  :is(.density-spread, .band > :has(> .sheet ~ .sheet)) > *, .band:has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)) > * { grid-column: auto !important; margin-top: 0; }
}
```

- Careful: the reading order is the source order, whatever the eye sees; keep them the same, or the tab order jumps about. Reading text inside a staggered piece keeps its measure and stays level (tilts belong to materials and never touch reading text). A stagger that looks accidental is worse than a straight grid: offset by whole steps of the scale.
- Light and dark: the same on both.
- Personality: playful, friendly, dramatic
- Goes with: `density: spacing airy` (artistic) or `standard` (a journal); `materials: paper-and-tape`.
- Used on: a field notebook (sheets that overlap and tilt), a quiet gallery (pots set left, centre and right in turn), and the artistic guide ("leave the centred column", 5 of 7 sites).

#### Panels
- Id: panels
- Status: draft
- Looks like: a screen laid out to the window, not to the content: a main panel, a column of smaller ones, a bar of controls, so everything used often is in the first screen.
- Made with: a grid with named regions, as tall as the window (`100dvh`), each region a plain panel; on a phone the regions stack and the page scrolls.

```css assemble
/* layout: panels. The page laid out to the window: a bar across the top, a main panel, a side column, a bar of
   controls; every band a plain panel. On a phone the regions stack and the page scrolls. */
.page { display: grid; min-height: 100dvh; gap: var(--gap-groups); align-content: stretch;
  padding-inline: max(var(--gutter), calc(var(--edge) - var(--density-band-inset)));
  grid-template-columns: minmax(0, 2fr) minmax(0, 1fr); grid-template-rows: auto minmax(0, 1fr) auto; }
.page > main { display: contents; }
.page .band { margin: 0; padding: var(--pad); }
:where(.page .band) { background-color: var(--background-patch, var(--surface)); color: var(--background-patch-ink, var(--ink)); }   /* the panel's fill is the background part's; any band colour it sets wins */
.page > :is(header, footer).band { grid-column: 1 / -1; }
.page > main > .band:nth-of-type(1) { grid-column: 1; grid-row: 2; }
.page > main > .band:nth-of-type(2) { grid-column: 2; grid-row: 2 / span 2; align-content: start; }
.page > main > .band:nth-of-type(3) { grid-column: 1; grid-row: 3; }
.page > main > .band:nth-of-type(n+4) { grid-column: 1 / -1; }
@media (width < 48rem) {   /* .page is the container, so its own grid answers to the window */
  .page { grid-template-columns: minmax(0, 1fr); grid-template-rows: none; min-height: 0; }
  .page > main > .band:nth-of-type(n) { grid-column: 1; grid-row: auto; }
}
```

- Careful: the window's height is not the page's: on a phone the bars of the browser come and go, which is why `dvh`. Bars that stay on screen take under a quarter of a phone's screen. Decide the stacking order for the phone; the main panel usually comes first, shrunk to a strip.
- Light and dark: the same on both. Panels need an edge on a dark page (frames: hairline at least), where `--surface` is close to the ground.
- Personality: serious, dramatic, playful
- Goes with: `density: spacing compact`; `density: fill full`; `frames: riveted-metal` or `hairline`.
- Used on: the interface version of a game-style joke site, and the game screen of a small shared-world game (a 3D view beside a column of readouts).

### Width
- Layer: width
- Owns: how wide the page's content runs (`--page`), the space from the window's edge to it (`--edge`), and whether bands and pictures stop at the page or run to the window's edges. Not the longest line of reading text: `--measure` belongs to lettering (the owners table), and every passage here reads it as `var(--measure, 66ch)`.
- Default: standard

The general guide's rule, made exact: side margins grow with the screen (the spacing's `--gutter`) and the content stops at `--page` and centres. Reading text keeps to lettering's `--measure` (45 to 75 characters; R9, R18) whatever the width; density never sets it.

#### Narrow
- Id: narrow
- Status: draft
- Looks like: the page is one reading column: the measure and its margins, centred, with the ground at the sides. A letter, a form, a guide.
- Made with: `--page` at 44rem. Use it with a measure of about 60ch from lettering, so the column is the line of text plus a little.

```css assemble
/* width: narrow. The page is one reading column */
& { --page: 44rem; }
```

- Careful: on a wide screen it leaves most of the window empty; that is the point on a form or guidance page, and wrong for a shop. Pictures are as narrow as the text.
- Light and dark: the same on both.
- Personality: serious, calm
- Goes with: `density: layout single-column`; `density: fill open`.
- Used on: public-service design (GOV.UK's main reading column is two-thirds of a 960-pixel page, R2); a sign-in page.

#### Standard
- Id: standard
- Status: draft
- Looks like: the page stops at 72rem (1152 pixels) and centres; on a wide window the ground shows at the sides.
- Made with: `--page` at 72rem. Six of the eight mockups that set a page width used 72 to 76rem.

```css assemble
/* width: standard */
& { --page: 72rem; }
```

- Careful: at 1280 wide the sides are only 64 pixels each; at 1920 they are nearly 400. Look at the page at both (the general guide's "Before showing").
- Light and dark: the same on both.
- Personality: any
- Goes with: anything.
- Used on: a night market, an observatory, a volunteer page (72rem); a field notebook, a repair café (74rem); a quiet gallery (76rem).

#### Wide
- Id: wide
- Status: draft
- Looks like: the page runs to 92rem (1472 pixels): pictures and tiles fill a large screen, and reading text still keeps its measure inside it.
- Made with: `--page` at 92rem; reading text in its own column at lettering's measure.

```css assemble
/* width: wide. Pictures and tiles fill a large screen; reading text keeps its measure */
& { --page: 92rem; }
.band :is(p, .lead) { max-width: var(--measure, 66ch); }
```

- Careful: wide pages tempt text to run wide; every passage keeps its measure (the audit's `style/line-length`). Use it where pictures are the content.
- Light and dark: the same on both.
- Personality: playful, dramatic
- Goes with: `density: layout grid` or `staggered`.
- Used on: the artistic guide's museums and studios, which run their work to the edge; no mockup yet at this width.

#### Full bleed
- Id: full-bleed
- Status: draft
- Looks like: bands and pictures run to the window's edges; the content inside each band keeps to the page width. Poster blocks, a picture at the top that meets the sides, a scene down the page.
- Made with: each band takes the whole width and pads its content in by `--edge`, so the content lines up with the page; a picture that should meet the edge takes a negative margin of `--edge` on that side. Named grid lines do the same with subgrid (R22).

```css assemble
/* width: full bleed. Bands meet the window's edges and pad their content in by --edge, so it lines up with the page */
& { --page: 72rem; --density-band-inset: var(--edge); }
.page { overflow-x: clip; }                                          /* no sideways scroll at 320 */
.band > .density-bleed-right { margin-inline-end: calc(var(--edge) * -1); }   /* a picture that meets the window's edge */
.band > .density-bleed { margin-inline: calc(var(--edge) * -1); }
```

- Careful: `100cqi` in `--edge` measures the container, so the bands' wrapper must be as wide as the window. Anything that runs off the edge is clipped on a wrapper with `overflow-x: clip` (no sideways scroll at 320). On a phone full bleed and standard look the same; the difference is all on a wide screen.
- Light and dark: the same on both. Bands in `--band-1` to `--band-3` (colour) carry it best.
- Personality: friendly, playful, dramatic
- Goes with: `background: coloured-bands` or `one-long-scene`; `density: rhythm alternating`.
- Used on: a night market (four full-width bands), an observatory (one long scene, band by band), a soap maker's shop, the warm guide's bands.

### Rhythm
- Layer: rhythm
- Owns: how one section follows the next down the page: whether the sections are all alike, alternate, or build to one large thing per screen. It owns the spacing and arrangement of the change; the colour of a band is the colour part's, and its edge is frames'.
- Default: even

#### Even
- Id: even
- Status: draft
- Looks like: every section the same gap, the same width and the same alignment. Calm and orderly; sections told apart by their headings.
- Made with: one gap between all sections, and nothing else.

```css assemble
/* rhythm: even. The base already puts one gap (--gap-sections) under every band, and nothing else. */
```

- Careful: on a long page an even rhythm can feel like one long scroll; give every section a clear heading, and look for the one thing per screen the general guide asks for.
- Light and dark: the same on both.
- Personality: serious, calm
- Goes with: `density: layout grid` or `single-column`; `density: spacing standard`.
- Used on: a tutor's site, a repair café (every section the same width in one column, with a drawn band at each break), the professional guide.

#### Alternating
- Id: alternating
- Status: draft
- Looks like: a beat down the page: every other section sits on a band, and in two-part sections the sides swap, picture left then picture right.
- Made with: `:nth-of-type(even)` sections on the background part's `--background-alternate` (`--surface` unless the background says otherwise; a band colour it sets wins), padded by `--gap-groups`; `direction: rtl` on the grid to swap the sides without changing the source order.

```css assemble
/* rhythm: alternating. Every other band sits on the background's alternate fill, and in two-part bands (two sheets, panels or pictures) the sides swap */
.band:not(header, footer):nth-of-type(even) { padding-block: var(--gap-groups); padding-inline: max(var(--pad), var(--density-band-inset)); }
:where(.band:not(header, footer):nth-of-type(even)) { background-color: var(--background-alternate, var(--surface)); color: var(--ink); }   /* the fill is the background part's; any band colour it sets wins */
.band:not(header, footer):nth-of-type(even):has(> :is(.sheet, .panel, .picture) ~ :is(.sheet, .panel, .picture)) { direction: rtl; }
.band:not(header, footer):nth-of-type(even) > * { direction: ltr; }   /* swap the sides, keep the reading order */
```

- Careful: swapping sides changes what the eye sees, not the order a screen reader or a phone reads; that is why it is done with `direction` and not by moving things. On a phone only the bands remain; that is enough.
- Light and dark: the bands are `--surface` on a light page (paler than the ground) and on a dark page (lighter than it).
- Personality: friendly, playful
- Goes with: `density: width full-bleed`; `background: coloured-bands`.
- Used on: a night market (oxblood, tarmac, forest, night blue), an observatory (sheets on the half the scene leaves empty, turn about), a quiet gallery (pots left, centre and right in turn), the warm guide's bands.

#### One big moment
- Id: one-big-moment
- Status: draft
- Looks like: sections are even, and one thing per screen is set large with space round it: the picture at the top, a scene halfway down, a large figure or a quote. The general guide's "one thing per screen is the most important", carried out with space.
- Made with: the moment takes the full width and up to 70 per cent of the screen's height, with half a section gap more above and below it.

- Needs markup: one `<section class="band">` holding only a `<figure class="picture">` (or a band marked `class="band density-moment"`); a drawn picture in it is an SVG with `preserveAspectRatio="xMidYMid slice"` and fills the band (the code sizes it).

```css assemble
/* rhythm: one big moment. A band holding only a picture (or marked .density-moment) runs to the window's edges,
   up to 70 per cent of the screen tall, with half a section gap more above and below */
:is(.density-moment, .band:has(> .picture:only-child)) { margin-block: calc(var(--gap-sections) * 0.5) calc(var(--gap-sections) * 1.5); }
:is(.density-moment, .band:has(> .picture:only-child)) > .picture { min-height: min(70svh, 36rem); margin-block: 0;
  margin-inline: calc(var(--edge) * -1); }
:is(.density-moment, .band:has(> .picture:only-child)) > .picture > :is(img, svg, video) { display: block; width: 100%; height: min(70svh, 36rem); object-fit: cover; }   /* the picture fills it; a drawn one slices */
```

- Careful: one per screen, and never two in a row; the general guide allows two large things on a screen at most. The moment must not push the main heading or the action below the first phone screen.
- Light and dark: the same on both.
- Personality: dramatic, calm
- Goes with: `density: fill open` (minimal) or `packed` (sorcery); a signature picture (picture style).
- Used on: the sorcery guide (the first screen is a picture of a place with the name inside its frame), the first version of a poetry site (one brush circle set large by the heading), the artistic guide (the signature piece fills the first screen, 7 of 7).

## On a phone

At 390 wide every option converges: margins of 12 to 20 pixels, one column, the large steps at their small ends. What is left to tell the options apart is the gaps between things, how much decoration survives (a phone drops one tier), and the order of what stacks. Write the phone's first screen and stacking order in the site's guide (the phone guide). Two things to check by hand: nothing scrolls sideways at 320 (signs off the edge are clipped), and every tap target keeps 8 pixels from the next (steps 1 to 6 do not change, so this holds in every option).

## Starting points

### Minimal
- Id: minimal
- Picks: spacing: airy; fill: open; layout: margin-column; width: standard; rhythm: one-big-moment
- Personality: calm, serious
- Looks like: one thing at a time on an open page; names and dates in a margin column; one thing made for the site set large in the space. What keeps it from looking like a template: the space is a material, not blank white; one drawn or lettered thing made for the site sits large in it; it leaves the centred column; no boxes; the headline is a chosen face at three times the body size or more. Box count 28 empty, none decoration.
- Used on: the first version of a poetry site (judged too empty for a front page) and the inner pages of a small game site, whose brief said "every other page is spare".

### Clean
- Id: clean
- Picks: spacing: standard; fill: open; layout: two-columns; width: standard; rhythm: even
- Personality: serious, calm
- Looks like: a normal amount on each screen, all of it lined up: facts in a row, lists in ruled rows, columns that share edges. Order, not emptiness, makes it calm. Box count 18 empty, none decoration.
- Used on: a tutor's site and a small game's front page; an observatory's sheets.

### Balanced
- Id: balanced
- Picks: spacing: standard; fill: balanced; layout: grid; width: full-bleed; rhythm: alternating
- Personality: friendly, playful
- Looks like: coloured bands edge to edge, a few marks per screen, tiles with room round them. Box count 18 empty, 4 decoration.
- Used on: a soap maker's shop, a volunteer page, a poetry site's final version. The poetry site's and the tutor's briefs both said "balanced", and the tutor's measured as clean: the word alone in a brief is not enough; say which option.

### Full but quiet
- Id: full-but-quiet
- Picks: spacing: compact; fill: full; layout: panels; width: full-bleed; rhythm: even
- Personality: serious, dramatic
- Looks like: a game screen or a working tool: the whole window used, plain panels in every region, narrow plain gaps. Box count 4 empty, none decoration.
- Used on: the interface version of a game-style joke site, the game screen of a small shared-world game.

### Busy
- Id: busy
- Picks: spacing: snug; fill: packed; layout: grid; width: standard; rhythm: even
- Personality: dramatic, playful
- Looks like: fill the frame: narrow gaps, each holding a drawn band or signs, calm patches only behind words and controls. Bright or dark, as the colour part decides. Box count 6 empty, 13 decoration.
- Used on: a dark, painterly joke site, a small shop in two versions (the busy one was the one the owner chose), a game-style joke site, and a bright repair café.

### Warm
- Id: warm
- Picks: spacing: standard; fill: balanced; layout: two-columns; width: full-bleed; rhythm: alternating
- Personality: friendly, playful
- Looks like: bands of bold colour edge to edge, the people's picture beside the headline at the top, two or three marks, then stop.
- Used on: the warm guide (bands, a picture of real people at full size, "two or three hand-made marks, then stop").

### Artistic
- Id: artistic
- Picks: spacing: airy; fill: open; layout: staggered; width: wide; rhythm: one-big-moment
- Personality: calm, dramatic
- Looks like: the work shown large, off the centred column, things of different sizes; reading text still at its measure.
- Used on: the artistic guide ("leaves the centred column", 5 of 7; the signature fills the first screen, 7 of 7).

### Professional
- Id: professional
- Picks: spacing: airy; fill: open; layout: grid; width: standard; rhythm: even
- Personality: serious, calm
- Looks like: an orderly grid with generous space; identical repeated items; nothing in the gaps.
- Used on: the professional guide ("one accent colour, an orderly grid, generous space").

### Civic
- Id: civic
- Picks: spacing: standard; fill: open; layout: single-column; width: narrow; rhythm: even
- Personality: serious
- Looks like: one readable column, nothing extra: guidance, a form, the next step.
- Used on: from research: public-service design systems (GOV.UK, USWDS) keep reading to a two-thirds column and spacing to one scale (R2, R4); a tutoring site's forms.

### Sorcery
- Id: sorcery
- Picks: spacing: snug; fill: packed; layout: single-column; width: full-bleed; rhythm: one-big-moment
- Personality: dramatic
- Looks like: a scene filling the first screen, then one column of calm sheets with every gap between and beside them filled.
- Used on: the sorcery guide ("as little clear space as we can", the owner; 5 of 6 pictures); a dark, painterly joke site.

### Gilded dark
- Id: gilded-dark
- Picks: spacing: snug; fill: full; layout: panels; width: full-bleed; rhythm: one-big-moment
- Personality: dramatic, playful
- Looks like: heavy panels in the regions of the screen, standing over one big painted world.
- Used on: the game-interface guide; a game-style joke site in both its looks.

### Lantern fair
- Id: lantern-fair
- Picks: spacing: snug; fill: packed; layout: grid; width: full-bleed; rhythm: alternating
- Personality: dramatic, friendly
- Looks like: full-width bands of stalls in turn, tags in a grid, bunting and chalk signs in every gap.
- Used on: a night market (four bands, gaps stopping at `--space-7`, bunting on every wave, chalk signs in the margins).

### Almanac plate
- Id: almanac-plate
- Picks: spacing: airy; fill: balanced; layout: two-columns; width: full-bleed; rhythm: alternating
- Personality: calm, serious
- Looks like: sheets of facts on one half of each band, a spare drawing of the scene on the other, swapping sides down the page; 96 pixels between bands.
- Used on: an observatory ("balanced at the scene, clean on the sheets").

### Catalogue of glazes
- Id: catalogue-of-glazes
- Picks: spacing: airy; fill: open; layout: margin-column; width: standard; rhythm: alternating
- Personality: calm
- Looks like: one piece to a screen, its particulars in a margin column, pieces set left, centre and right in turn.
- Used on: a quiet gallery of pots ("one pot to a screen", `--space-9` between pieces, a 76rem page).

### Field journal
- Id: field-journal
- Picks: spacing: standard; fill: balanced; layout: staggered; width: standard; rhythm: alternating
- Personality: calm, friendly
- Looks like: pages laid down a little out of line, two or three drawn marks per screen, on a page that is itself the notebook.
- Used on: a field notebook (sections `--space-8` apart, items `--space-7` on a phone, sheets that overlap and tilt).

### Repair cafe
- Id: repair-cafe
- Picks: spacing: snug; fill: packed; layout: grid; width: standard; rhythm: alternating
- Personality: playful, friendly
- Looks like: a full, bright board: tags four across, a drawn band (a tape measure, bunting) at every break, things hung in every gap. Busy on a light page.
- Used on: a repair-café mockup (the scale stops at `--space-7`; sections `--space-5` apart with a drawn band; a 74rem page; tags four across from 62rem; 7 per cent open, 33 decoration).

## Swatch book

`tests/parts/density.html` shows every option of every layer, then every starting point, each on a light page and on a dark one (side by side for the spacing swatches; the page miniatures are stacked, light above dark, at full width so they show larger); open it in a browser to choose by eye. The spacing options are shown in words at real size, with a key giving the four gaps measured at the swatch's width. The other layers are shown as a page in miniature: the same generic page (a header, a heading with a picture, a row of items, a large moment, a passage with a side panel, a short form) laid out at full size in a window 1600 pixels wide and on a phone 390 wide, then scaled down, with words as bars and pictures as tinted blocks, so only the space and the arrangement change. The fill swatches and the starting points draw the box count over the first screen and print both numbers. The fill swatches are shown with `layout: grid` and `width: wide`, and the rhythm swatches with `layout: grid`, so one screen holds enough to compare. It writes the layer classes short (`sp-`, `fi-`, `la-`, `wi-`, `rh-`) on its own miniature markup; the assembly blocks above are the same decisions written for the shared hooks, so a real page takes them. It is built by `tests/parts/source/density.py` from `density-template.html` beside it; run `python3 density.py ../density.html` there to rebuild it.

## Not covered yet

- **The measure in `audit`.** The algorithm under "How full" was tried as a prototype on 13 mockups; it is not yet a command. Until it is, use the box count and say in the site's guide that it was counted by eye.
- **Data-heavy pages** (tables, dashboards, account pages), where many things per screen is the job. Compact spacing is written for them from research (Material's density scale, Gmail's compact view, R6, R7), not from a mockup.
- **Full at the top and balanced below,** on one page. Tried once, on a shop where a warm guide led and a dark guide came second; the owner found it "a worse version" of the busy one, but which guide led changed at the same time.
- **Masonry.** A catalogue of pictures of different heights wants a masonry grid; CSS for it is not settled in every browser, so staggered uses a plain grid.
- **Whether open space helps reading.** The often-repeated "white space improves comprehension by almost 20 per cent" traces to a 2004 paper about older readers and hypertext that does not test margins (R16); the study that did (four white-space layouts) found margins helped speed and comprehension and leading only preference (R15). Treat open space as a matter of feel and grouping, not a proven aid to understanding.
- **How visual complexity affects first impressions.** Reinecke and others found appeal falls most at high complexity, while low and medium complexity are liked about equally (R19). That argues for a ceiling on fullness rather than a target, but it was measured on ordinary websites at a glance, not on pages built to be full; the owner chose packed pages twice.

## Sources

Read on 2026-10-07. Six kinds of source: design-system documents (R1 to R8), the web platform's references and layout writing (R9 to R14), research on space, density and complexity (R15 to R21), editorial design and typography (R18, R22, R23, R25), writing on full and maximal design (R24, R28), and accessibility and touch (R26, R27). The mockups made with the skill are the seventh: their CSS, their site guides and the prototype measurements are quoted in each option's "Used on". Pages that would not open: several Material pages (their figures are from search results and are marked), Every Layout's Center, Grid, Stack and Sidebar pages (paywalled), and a Codrops article (blocked).

- R1 Atlassian Design System, spacing (8-pixel base; tokens 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80): atlassian.design/foundations/spacing
- R2 GOV.UK Design System, spacing (a responsive scale whose units 0 to 3 stay the same and units 4 to 9 grow above 640 pixels, 15 to 25 up to 40 to 60; a static scale 0 to 60): design-system.service.gov.uk/styles/spacing/
- R3 IBM Carbon, spacing (2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 160; the larger steps "used to control the density of a design") and the 2x grid (8-pixel mini unit; 4, 8 and 16 columns): carbondesignsystem.com/elements/spacing/overview/ and carbondesignsystem.com/elements/2x-grid/overview/
- R4 USWDS, spacing units ("based on multiples of 8px"; named widths mobile 320, tablet 640, desktop 1024): designsystem.digital.gov/design-tokens/spacing-units/
- R5 Android, window size classes (compact under 600dp, "99.96% of phones in portrait"; medium, expanded, large, extra-large) and Material 3's medium layout (24dp margins and 24dp between panes; read from a search result): developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes and m3.material.io/foundations/layout/breakpoints/medium
- R6 Material density on the web ("each whole number step down ... reduces the affected sizes by 4px"; read from a search result): m2.material.io/blog/material-density-web
- R7 Gmail display density (default, comfortable, compact; compact "does not show space between messages"; read from a help page): gmail.googleblog.com/2011/11/changing-information-density-in-gmails.html
- R8 Android, adaptive Material codelab (16dp inside panes, 24dp between them, a 60-character line on large screens): developer.android.com/codelabs/adaptive-material-guidance
- R9 Every Layout, axioms ("the measure should never exceed 60ch"; Bringhurst's 45 to 75) and modular scale ("it is in the strict adherence to whichever ratio you choose that harmony is created"): every-layout.dev/rudiments/axioms/ and every-layout.dev/rudiments/modular-scale/
- R10 MDN, clamp() (resolved as `max(MIN, min(VAL, MAX))`): developer.mozilla.org/en-US/docs/Web/CSS/clamp
- R11 MDN, container queries (`cqi` is 1% of the container's inline size; `inline-size` queries): developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries
- R12 web.dev, Learn Design: macro layouts (`repeat(auto-fill, minmax(15em, 1fr))`; layouts "without any media queries"): web.dev/learn/design/macro-layouts
- R13 Every Layout, the Switcher (`flex-basis: calc((30rem - 100%) * 999)`; "quantum layouts existing simultaneously in different states"): every-layout.dev/layouts/switcher/
- R14 Utopia, fluid space calculator (space pairs that grow from a small to a large screen with `clamp()`): utopia.fyi/space/calculator/ ; and web.dev on min(), max() and clamp() (`width: clamp(45ch, 50%, 75ch)`): web.dev/articles/min-max-clamp
- R15 Chaparro, Baker, Shaikh, Hull and Brady, "Reading Online Text: A Comparison of Four White Space Layouts" (2004; margins and leading varied; margins affected speed and comprehension, leading only preference): portfolio.erau.edu/en/publications/reading-online-text-a-comparison-of-four-white-space-layouts/
- R16 Lin (2004), "Evaluating older adults' retention in hypertext perusal" (the paper the "20 per cent" claim is pinned on; it compares animated graphs, pictures and text, not margins; read from its abstract): doi.org/10.1016/j.chb.2003.10.024
- R17 Nielsen Norman Group, proximity ("Using varying amounts of whitespace to either unite or separate elements is key to communicating meaningful groupings"), the visual-design glossary (density: "the number of visual elements in a given area"), and heuristic 8 ("every extra unit of information ... diminishes their relative visibility"): nngroup.com/articles/gestalt-proximity/ , nngroup.com/articles/visual-design-cheat-sheet/ , nngroup.com/articles/aesthetic-minimalist-design/
- R18 Butterick, Practical Typography, line length ("45–90 characters, including spaces") and page margins ("web pages need big margins too"): practicaltypography.com/line-length.html and practicaltypography.com/page-margins.html
- R19 Reinecke, Yeh, Miratrix and others, "Predicting users' first impressions of website aesthetics" (CHI 2013; 450 sites, 548 people, 500 ms; complexity from text area, non-text area, space-based decomposition, text groups and image areas, R² .65; "websites with low levels of complexity are similarly liked to those with a medium complexity"; a quadtree alone r = .28): kgajos.seas.harvard.edu/papers/reinecke13aesthetics.pdf
- R20 Miniukovich and De Angeli, "Computation of Interface Aesthetics" (CHI 2015; eight metrics, up to 49% of variance) and "Quantification of Interface Visual Complexity" (AVI 2014; read from abstracts): doi.org/10.1145/2702123.2702575 and doi.org/10.1145/2598153.2598173
- R21 Aalto Interface Metrics (open code for white space, "the proportion of white space", contour density, feature congestion and grid quality): github.com/aalto-ui/aim ; and Rosenholtz, Li and Nakano, "Measuring visual clutter" (2007; clutter from colour, contrast and orientation predicts search time): news.mit.edu/2007/mits-clutter-detector-could-cut-confusion and dspace.mit.edu/handle/1721.1/37593
- R22 Rachel Andrew, editorial design patterns with grid, subgrid and named lines (`content-start`, `content-end`; full, content and split areas): smashingmagazine.com/2019/10/editorial-design-patterns-css-grid-subgrid-naming/
- R23 Andy Clarke, inspired design decisions ("the combination of four and six-column grids is the one I use most often"; "Whitespace opens up around running copy"): smashingmagazine.com/2019/07/inspired-design-decisions-pressing-matters/
- R24 LogRocket, maximalism in UI design ("increased complexity as a fundamental design rule"; suits entertainment and creative brands, can "negatively affect usability" in finance, health and law): blog.logrocket.com/?p=201834 ; and Codrops on maximalism ("density the way a minimalist chooses emptiness — as a tool"; read from a search result): tympanus.net/codrops/?p=64129
- R25 Wikipedia, canons of page construction (margins in the ratio 2:3:4:6, inner to bottom; Tschichold), and Müller-Brockmann ("The grid system is an aid, not a guarantee"): en.wikipedia.org/wiki/Canons_of_page_construction and goodreads.com/work/quotes/341206
- R26 WCAG 2.2, target size minimum (24 by 24, or spaced so 24-pixel circles do not meet) and Android's touch targets ("at least 48x48dp, separated by 8dp of space or more, to ensure balanced information density and usability"): w3.org/WAI/WCAG22/Understanding/target-size-minimum.html and support.google.com/accessibility/android/answer/7101858
- R27 Apple Human Interface Guidelines, accessibility (controls 44 by 44 points by default, 28 at the least) and layout (layout guides "restrict the width of text for optimal readability"): developer.apple.com/design/human-interface-guidelines/accessibility and developer.apple.com/design/human-interface-guidelines/layout
- R28 Matt Ström, "UI Density" ("the value a user gets from the interface divided by the time and space the interface occupies"; visual, information, design and temporal density; the Bloomberg Terminal): mattstromawn.com/writing/ui-density
