---
name: Materials (a part guide)
summary: What a page is made of: the stuff its panels, sheets and repeated items look like (paper, parchment, felt, stone, wood, metal). Each option can be picked on its own and used with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: the mockups made with the skill so far, and the guides named in each option
---

# Materials

A part guide. It covers what the page is "made of": the stuff of the panels that hold words, of the repeated item (a product, an event, a poem) and of the small fixings that hold them up (tape, pins, string, rivets). A site picks one option in its own guide, and in the blueprint as `project.style.parts`: `{"materials": "<option-id>"}`. The picked option wins over the feel guide for the material only; the feel guide still decides everything else. The general guide's accessibility minimums (contrast, text size, tap size) still hold whatever is picked.

**One material, used consistently.** The warm guide's note "Take a material from the subject" asks for one material from the site's real life, and the general guide gives the lead guide the main material. Each option here is one such material, with the fixings that belong to it: tape comes with paper, pins with the felt board, string with the stall's tags. Pick one. Two materials from this list on one page (stone walls and a felt board) read as stickers from different sets. One shop drawn for a warm lead dropped the dark guide's stone for exactly this reason and kept only parchment. The one exception seen: a market stall is wood and canvas and the paper tags tied to it, because all three are the same real object.

**Texture never sits under words at full strength.** Text on a textured material must reach the contrast minimum against the *worst* of the texture under it, not its average. `check` and `audit` measure this from a picture of the page: each piece of text is photographed with and without its words, and the darkest (or lightest) 5% of what lies under it decides. Every option below says how the mockups kept the texture off the words.

## Choosing

| Option | What it feels like | Suits best | Fights |
|---|---|---|---|
| Fine paper | Quiet, printed, careful: a good sheet on a desk | Professional; artistic | A page that should feel loud or crowded |
| Paper and tape | Made at a kitchen table by one person | Warm; one maker's shop | Professional |
| Cut paper on felt | A club's notice board: bright, crooked, friendly | Warm | Professional; a dark lead |
| Parchment and ink | Old, hand-written, a little worn | A dark, painterly lead; artistic | Professional; a bright warm page, where it looks brown and tired |
| Stone and chalk | A cold wall someone has written on | A dark, painterly lead | Warm; professional |
| Wood and canvas | A market stall at a fair | Warm; a small shop with a dark lead | Professional |
| Metal and dark glass | A game's interface: heavy and shiny | A game-style site | Almost everything else, and any page meant for long reading |

How to choose: ask the warm guide's two questions even when warm is not stacked. What would this organisation pin to a wall, and what is it made of? The answer is usually one of these. If it is not (a seed packet, a ticket, a slate roof), take the nearest option's technique and change the colours and fixings; write the new material in the site's own guide. Then check the lead feel guide: it decides how dark the page is, and a material must sit in that light (see `light` in its own part guide).

## Options

### Fine paper
- Id: fine-paper
- Status: draft
- Looks like: clean sheets of good paper on a page of slightly grained paper, with one soft shadow and dark ink words. No tape, no tears, no tilt. The quietest material that is still a material.
- Made with: a grain tile drawn by `feTurbulence` at low strength on the page, and plain sheets with a thin rule and one soft shadow. A variant is the specimen label: cream paper, a one-pixel ink border, a small capitals heading over a rule, a coloured dot.

```css
:root { --paper: #f6f1e7; --sheet: #fcf9f3; --ink: #22201c; --ink-soft: #5f5a50; --rule: #d9cfbd; }
body { background: var(--paper) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2'/%3E%3CfeColorMatrix values='0 0 0 0 0.3  0 0 0 0 0.25  0 0 0 0 0.15  0 0 0 0.14 0'/%3E%3C/filter%3E%3Crect width='240' height='240' filter='url(%23n)'/%3E%3C/svg%3E"); }
.sheet { background: var(--sheet); color: var(--ink); border: 1px solid var(--rule); border-radius: 3px;
  box-shadow: 0 1px 2px rgb(34 32 28 / 0.08), 0 16px 32px -14px rgb(34 32 28 / 0.25); }
.specimen { background: var(--sheet); border: 1px solid var(--ink); border-radius: 3px; }
```

- Careful: the grain is on the page, and the sheets that carry words are plain, so text is measured against a flat colour. Keep the grain faint, so it is felt more than seen; stronger, it looks like dirt on a light page. Muted text (`--ink-soft`) must still reach 4.5 to 1 on the page colour, not only on the sheet.
- Goes with: `frames: none` or `hairline`; `light: flat-and-even`; `density: balanced`.
- Used on: 2 mockups: a poetry site (painted sheets on grained paper), a small browser game's pages (specimen labels for its cards).

### Paper and tape
- Id: paper-and-tape
- Status: draft
- Looks like: cards and notebook pages stuck to a warm paper page with strips of torn tape, a little crooked; prices on brown kraft tags; a torn edge where a coloured band meets the page; pen lines and a little handwriting.
- Made with: a grained paper page, cards whose paper is a `::before` turned a degree or so, a strip of see-through kraft tape with jagged ends from `clip-path`, and a kraft tag cut with a point and a punched hole.

```css
:root { --paper: #f8f0e0; --sheet: #fffaf0; --kraft: #cfae7c; --ink: #1f2a22; }
.card { position: relative; isolation: isolate; padding: var(--space-5); color: var(--ink); }
.card::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--sheet); border-radius: 4px;
  rotate: var(--tilt, -1.3deg); box-shadow: 0 10px 22px -8px rgb(31 42 34 / 0.3); }
.card::after { content: ""; position: absolute; top: -0.7rem; left: 50%; translate: -50% 0; width: 5.5rem; height: 1.5rem;
  background: rgb(207 174 124 / 0.72); rotate: -3deg;
  clip-path: polygon(0 12%, 4% 0, 8% 14%, 12% 2%, 16% 12%, 20% 0, 100% 0, 100% 88%, 96% 100%, 92% 86%, 88% 98%, 84% 88%, 80% 100%, 0 100%); }
.price { display: inline-flex; align-items: center; gap: var(--space-2); padding: var(--space-1) var(--space-4) var(--space-1) var(--space-5);
  background: var(--kraft); color: var(--ink); font-weight: 700; rotate: -2deg; clip-path: polygon(0.9rem 0, 100% 0, 100% 100%, 0.9rem 100%, 0 50%); }
.price::before { content: ""; width: 0.4rem; height: 0.4rem; border-radius: 50%; background: var(--sheet); margin-left: -0.5rem; }
```

- Careful: the first shop to use this turned the whole card, words and all; later mockups turn only the paper (`::before`) so the words stay level and sharp. Do that. The tape overlaps the top of the card: keep the first line of words below it. A tilted price tag is short text; keep it bold and at least 16 pixels. The page grain is strong here (half strength), so words never sit straight on the page: they sit on a card or a tag.
- Goes with: `frames: torn-paper`; `light: flat-and-even` or `daylight`; `density: balanced`.
- Used on: 2 mockups: a one-person handmade shop (taped cards, kraft tags, torn edges), a volunteer page (a taped sticky note).

### Cut paper on felt
- Id: cut-paper-on-felt
- Status: draft
- Looks like: a notice board: a felt-blue ground with a fine woven dot, and on it sheets of coloured paper, each its own colour, cut by hand and pinned up a little crooked with a round pushpin. Small extras from the same board: a sticky note, a round date sticker, a rubber stamp across a full one.
- Made with: the felt is one colour with a tiny repeating radial dot. Each notice's paper is a `::before` clipped to an uneven four-cornered outline and turned under a degree; the shadow is two `drop-shadow()`s on the notice (a `box-shadow` would be cut off by the clip). The pin is a small inline SVG.

```css
:root { --felt: #1e3f8f; --ink: #1a2142; --cut: polygon(0.6% 1.4%, 99.5% 0, 100% 98.8%, 0 100%);
  --paper-peach: #ffe0b3; --paper-pink: #ffd9cf; --paper-butter: #fff3c4; --paper-mint: #d9f2d0; --paper-sky: #d6ecff; }
.board { background-color: var(--felt); background-image: radial-gradient(rgb(255 255 255 / 0.07) 1px, transparent 1.3px); background-size: 6px 6px; }
.notice { position: relative; isolation: isolate; padding: var(--space-6) var(--space-4) var(--space-5); color: var(--ink);
  filter: drop-shadow(0 3px 0 rgb(10 18 50 / 0.3)) drop-shadow(0 10px 14px rgb(10 18 50 / 0.28)); }
.notice::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--paper, var(--paper-peach)); clip-path: var(--cut); rotate: var(--tilt, -0.8deg); }
.notice:nth-child(2n) { --tilt: 0.9deg; }
.notice:nth-child(3n) { --tilt: -0.3deg; }
```

```html
<svg class="pin" viewBox="0 0 28 32" aria-hidden="true" focusable="false"><ellipse cx="17" cy="23" rx="8" ry="4" fill="rgb(10 18 50 / 0.3)"/><circle cx="14" cy="13" r="10" fill="var(--pin, #c9321e)"/><circle cx="10.5" cy="9.5" r="3" fill="rgb(255 255 255 / 0.55)"/></svg>
```

- Careful: the papers are pale on purpose, so dark ink passes on all five; a stronger paper colour must be measured. Words go on paper, never straight on the felt: the felt's dot is faint, but white text on it is a heading at most. When a whole notice is the thing to tap, put the focus outline on the notice with an offset so the tilted paper does not hide it. Pins and drawings are decoration (`aria-hidden`); a "Full" stamp is also said in words. On a phone halve the tilts.
- Goes with: `frames: torn-paper` for the edges between sections; `light: daylight` or `flat-and-even`; `density: busy`.
- Used on: 1 mockup: a volunteer sign-up page (events as pinned notices, a sticky note, a full event stamped).

### Parchment and ink
- Id: parchment-and-ink
- Status: draft
- Looks like: old sheets of parchment, dim and warm, with grain, mottled stains and a darkened edge, torn along their sides; dark brown-black ink; the first letter of each title and the small labels in red ink, as a scribe would. Often the same parchment as luggage tags on string.
- Made with: the sheet's own background is the plain parchment colour, and that is the colour the words are chosen against. Grain, large soft stains and the darkened edge are laid over it by a `::before` with `mix-blend-mode: multiply`; the words sit above it (`z-index: 1`). The edge is torn with a `clip-path` polygon; keep four to six different outlines so no two sheets match.

```css
:root { --parchment: #c9b083; --ink: #1d0f08; --rubric: #450c19; }
.sheet { position: relative; isolation: isolate; padding: var(--space-6) var(--space-5); background: var(--parchment); color: var(--ink);
  clip-path: polygon(0 1%, 7% 0, 18% 1.2%, 33% 0.2%, 52% 1%, 70% 0, 88% 0.8%, 100% 0, 99.3% 22%, 100% 47%, 99.2% 74%, 100% 99%,
    81% 100%, 60% 98.8%, 41% 100%, 23% 99%, 6% 100%, 0 99%, 0.8% 70%, 0 45%, 0.7% 20%); }
.sheet::before { content: ""; position: absolute; inset: 0; z-index: 0; pointer-events: none; mix-blend-mode: multiply;
  box-shadow: inset 0 0 18px 3px rgb(96 60 20 / 0.5);          /* the darkened edge: it stays in the padding */
  background-image:
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .35  0 0 0 0 .22  0 0 0 0 .08  0 0 0 .4 -.12'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23g)'/%3E%3C/svg%3E"),
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='520' height='520'%3E%3Cfilter id='m'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.012' numOctaves='3' seed='7' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .35  0 0 0 0 .22  0 0 0 0 .08  0 0 0 .36 -.07'/%3E%3C/filter%3E%3Crect width='520' height='520' filter='url(%23m)'/%3E%3C/svg%3E"); }
.sheet > * { position: relative; z-index: 1; }
.sheet h2::first-letter { color: var(--rubric); }
```

- Careful: this is the material where contrast is most often lost. The stains darken the sheet unevenly, so choose the ink against the darkest patch under any words, not the plain colour: on one site, ink that gave 7 to 1 on the plain sheet gave 5.4 to 1 on the worst stain, and the two thinner inks only just passed at 4.6. Measure again if the staining gets heavier. Keep the darkened edge inside the padding, where there are no words. Colours carried over from elsewhere (a rarity ladder, a kind's colour) must be darkened, keeping the hue, until they pass on parchment. Keep the parchment dim on a dark page, or it outshines everything; a bright parchment on a bright page looks brown and tired. Links on parchment are ink-coloured with a coloured underline, not the page's link colour. On one shop, 35 pieces of text on parchment could not be measured by the script at the time and were checked only by eye. The swatch book's sheet is measured; check that `audit` counts the text on your sheets as measured, not as unmeasured.
- Goes with: `frames: torn-paper` or `inked-panel`; `light: one-light` (the parchment dimmer than the light); `density: busy`; `background: detailed-ground`, with the sheets as the calm patches.
- Used on: 4 mockups: a dark, painterly joke site (every word on torn parchment), two versions of a small shop of handmade goods (parchment notices and tags), one look of a game-style joke site (parchment sheets for reading).

### Stone and chalk
- Id: stone-and-chalk
- Status: draft
- Looks like: a wall of dressed stone blocks in a few close dark shades, with hairline cracks and mortar between them, and marks chalked on it by hand at half strength: tallies, arrows, signs. The words do not go on the stone; they sit on a calm, plain dark slab with an ink edge.
- Made with: a small SVG tile of rectangles in three or four near shades over a mortar colour, with a crack or two, repeated as the ground; a fine grain over it. Chalk marks are inline SVGs, stroked in the chalk colour at `opacity: 0.5`, each placed by hand at its own size and tilt.

```css
:root { --wall: #131129; --slab: #0e0c20; --pen: #07060f; --text: #efe4c8; --chalk: #a9b4e6; }
.wall { background: var(--wall) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='80'%3E%3Crect width='160' height='80' fill='%23131129'/%3E%3Crect x='1' y='1' width='70' height='37' fill='%23181540'/%3E%3Crect x='73' y='1' width='86' height='37' fill='%231e1a48'/%3E%3Crect x='0' y='41' width='38' height='38' fill='%231a1740'/%3E%3Crect x='40' y='41' width='64' height='38' fill='%23211d4c'/%3E%3Crect x='106' y='41' width='54' height='38' fill='%23181540'/%3E%3Cpath d='M30 4l5 14l-2 16' stroke='%230a0919' stroke-width='1.3' fill='none'/%3E%3C/svg%3E"); }
.slab { background: var(--slab); color: var(--text); border: 3px solid var(--pen); border-radius: 2px; box-shadow: 5px 6px 0 #06050f; padding: var(--space-5); }
.chalk { position: absolute; pointer-events: none; color: var(--chalk); opacity: 0.5; fill: none; stroke: currentColor; stroke-width: 2.5; stroke-linecap: round; }
```

- Careful: no words on the stone, ever: the blocks change shade under each letter. Chalk marks are decoration (`aria-hidden`, `pointer-events: none`) and never cross a word or a control. On a phone there is almost no wall left at the sides (about 12 pixels on the one site), so the chalk becomes slivers in the gaps; let marks inside the panels' margins do the work there. A wall wider than the page clips its marks with `overflow-x: clip`, not `hidden`, so sticky things still stick (`css-layout.md`). Pale text on the slab is easy to pass (15 to 1 on the one site).
- Goes with: `frames: inked-panel` or `carved-plate`; `light: one-light` or `moonlight`; `density: busy`. With `parchment-and-ink` only where the stone is the room and the parchment is what is written on, as on the one site; otherwise pick one.
- Used on: 1 mockup: a dark, painterly joke site (the stone wall, chalk on the wall and lintel). A shop led by warm dropped it to keep one material.

### Wood and canvas
- Id: wood-and-canvas
- Status: draft
- Looks like: a market stall: a striped canvas valance with a scalloped edge across the top, dark oak for the rail things hang from and for a name plank held by two pegs, and the stall's tags of paper or parchment tied on with string.
- Made with: the valance is one repeating stripe gradient, scalloped by a mask; the plank is a dark gradient with a faint grain of stripes and two round pegs; the rail is an 8-pixel gradient at the top of the list; each tag's string is a 2-pixel line from the rail, and the tag is cut like a luggage tag and hung a little crooked.

```css
:root { --oak: #3d2614; --oak-hi: #5a3a20; --stripe-a: #7a1f24; --stripe-b: #e8d9b5; --tag: #d6c294; --ink: #1d0f08; --string: #8a6a44; }
.valance { height: 40px; background: repeating-linear-gradient(90deg, var(--stripe-a) 0 24px, var(--stripe-b) 24px 48px);
  -webkit-mask: linear-gradient(#000 0 0) top / 100% 28px no-repeat, radial-gradient(circle 12px at 12px 0, #000 98%, transparent) 0 28px / 24px 12px repeat-x;
          mask: linear-gradient(#000 0 0) top / 100% 28px no-repeat, radial-gradient(circle 12px at 12px 0, #000 98%, transparent) 0 28px / 24px 12px repeat-x; }
.plank { position: relative; padding: var(--space-1) var(--space-6) var(--space-2); border: 2px solid #4e3219; outline: 1px solid #000;
  background: repeating-linear-gradient(178deg, rgb(255 255 255 / 0.03) 0 3px, transparent 3px 9px), linear-gradient(#1b0d08, #120806); }
.plank::before, .plank::after { content: ""; position: absolute; top: 50%; translate: 0 -50%; width: 10px; height: 10px; border-radius: 50%;
  background: #6e5432; box-shadow: inset 0 0 0 2px #2a180a; }
.plank::before { left: 8px; } .plank::after { right: 8px; }
.rail { padding-top: var(--space-5); background: linear-gradient(var(--oak-hi), var(--oak)) top / 100% 8px no-repeat; }
.tag { position: relative; isolation: isolate; padding: var(--space-5) var(--space-3) var(--space-4); color: var(--ink); }
.tag::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--tag);
  clip-path: polygon(14% 0, 86% 0, 100% 6%, 100% 100%, 0 100%, 0 6%); rotate: var(--tilt, -1.2deg); transform-origin: 50% 0;
  filter: drop-shadow(0 6px 8px rgb(0 0 0 / 0.6)); }
.tag::after { content: ""; position: absolute; left: 50%; top: calc(-1 * var(--space-5)); width: 2px; height: calc(var(--space-5) + 8px); background: var(--string); }
```

- Careful: the tag turns, the words on it do not. The pale lettering on the plank is the only text on wood; keep any grain on the wood faint (the swatch uses stripes of 3 percent white) so the lettering stays easy to read and to measure. The valance is a frame across the top of a section, not a place for words; with `frames: wavy-edge` it can also be that guide's scallops. When the whole tag is the link, stretch the link over the tag (`::after` with `inset: 0`) and put the focus outline on the tag, with an offset. On a phone the tags go two to a row and the strings stay short.
- Goes with: `parchment-and-ink`'s sheet style for the tags (the stall's own paper); `frames: carved-plate` round product pictures; `light: one-light` (a lantern) or `daylight`; `density: busy`.
- Used on: 2 mockups: two versions of a small shop of handmade goods sold from a fair stall (oak rail, name plank and tags in one; the striped valance in the other).

### Metal and dark glass
- Id: metal-and-dark-glass
- Status: draft
- Looks like: a game's interface: dark, nearly solid panes edged in bands of gold or steel, name plates of bevelled metal with a rivet at each end, buttons set in metal rings, and headings lettered in the metal colour with a dark edge. The heavy riveted ring round a whole window is `frames: riveted-metal`; this is the stuff the rest is made of.
- Made with: three metal tokens (highlight, body, shadow) and a dark edge, swapped together for gold or steel. Bands of metal are stacked `box-shadow` rings, so they need no file and follow the corner radius. A plate is a metal gradient with two radial-gradient rivets. The pane is a dark colour at 90 percent or more.

```css
:root { --metal-hi: #fff2b8; --metal: #e2ad3b; --metal-lo: #8a5c14; --metal-dark: #3a2405;   /* steel: #ffffff, #a9b8ca, #4f5f75, #121b29 */
  --glass: rgb(22 10 20 / 0.92); --ink: #f7efe1; --head: #f4c75a; --head-edge: #2a1206; }
.pane { background: var(--glass); color: var(--ink); border-radius: 6px; margin: 9px;
  box-shadow: 0 0 0 3px var(--metal-dark), 0 0 0 7px var(--metal), 0 0 0 9px var(--metal-dark), inset 0 0 0 1px rgb(255 255 255 / 0.12); }
.pane h2 { color: var(--head); text-shadow: 0 2px 0 var(--head-edge), 0 0 2px var(--head-edge); }
.plate { color: var(--metal-dark); font-weight: 700; padding: var(--space-1) var(--space-4); border-radius: 4px; box-shadow: 0 0 0 2px var(--metal-dark);
  background: radial-gradient(circle at 8px 50%, var(--metal-dark) 0 2px, transparent 2.5px), radial-gradient(circle at calc(100% - 8px) 50%, var(--metal-dark) 0 2px, transparent 2.5px),
    linear-gradient(170deg, var(--metal-hi), var(--metal) 30%, #c9932e 60%, var(--metal-hi)); }
.btn { margin: 5px; border: 3px solid var(--metal-dark); border-radius: 8px;
  box-shadow: 0 0 0 3px var(--metal), 0 0 0 5px var(--metal-dark), inset 0 2px 0 rgb(255 255 255 / 0.35), inset 0 -4px 0 rgb(0 0 0 / 0.35); }
```

- Careful: the words sit on the dark glass, never on the metal or straight on the painting behind it; at 90 percent or more the glass holds contrast over any picture, and `check` measures it from the picture. Metal lettering gets its dark edge (`text-shadow`) because the gold is close to the bright parts of a sunset; on a pale pane it would fail. Box-shadow rings take no space: give the element a margin as wide as the rings, or neighbours and the page's edge cut them off on a phone. Shine or glints that move stop under reduced motion. Keep gradients on the metal only. On the version of the site that stacked a dark, painterly guide with it, that guide asked for "no glossy gold, no glowing glass", and the metal was drawn as rough strokes instead: the same material in a hand-drawn finish.
- Goes with: `frames: riveted-metal` on the main windows; `light: daylight` or `glow-on-edges`; `density: busy`; `frames: wavy-edge` between bands of painted landscape.
- Used on: 3 mockups: three versions of a game-style joke site (gold on one side, steel on the other).

## Swatch book

`tests/parts/materials.html` shows every option live; open it in a browser to choose by eye.

## Not covered yet

- Chalk on a blackboard or on tarmac as the whole material, and painted wooden planks: the warm guide's study saw both (a street-play charity, a city farm), but no mockup has used them. Stone and chalk here is chalk on a dark wall, with the words kept off it.
- Brick, fabric (other than canvas and felt), glass that is clear, plastic, concrete, and any material from a modern trade (a workshop's steel, a clinic's surfaces).
- Photographed textures. Every material here is drawn in CSS or small SVG; a real photograph of wood or paper behaves differently under words and weighs more.
- A material for professional sites beyond fine paper: the professional guide does not name one.
- How each material prints, and how it looks with the browser's forced colours on, where background images and masks are dropped. Not tested.
- Speed on a slow phone: `feTurbulence` grain and `mix-blend-mode` are worked out as the page is drawn. One site with fifteen textured sheets did not try a real phone.
- Real phones. Everything here was looked at in a desktop browser pretending to be one.
