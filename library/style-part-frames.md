---
name: Frames and edges (a part guide)
summary: What goes round a panel, a card, a picture or a whole section, and what the edge between two sections looks like. Each option can be picked on its own and used with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: the mockups made with the skill so far, and the guides named in each option
---

# Frames and edges

A part guide. It covers what is drawn round things on a page (a panel of text, a repeated item, a picture, a whole section) and the line where one section meets the next. A site picks one option in its own guide, and in the blueprint as `project.style.parts`: `{"frames": "<option-id>"}`. The picked option wins over the feel guide for frames and edges only; the feel guide still decides everything else. A site may pick a second option for the edges between sections only, when the first is a frame (say `inked-panel` with `wavy-edge`); write both in the site's guide. The general guide's accessibility minimums still hold.

One rule for every option: **frames never go round fields people type in.** A field keeps a plain border that reaches 3 to 1 against what is next to it, so that it looks like a field and nothing else. The frame goes round the form's panel, not round each box in it. The same holds for buttons: a button is not framed like a picture.

## Choosing

| Option | What it feels like | Suits best | Fights |
|---|---|---|---|
| None | Calm and printed; space does the grouping | Professional; artistic when the work itself is the frame | A busy page, where groups blur without a line |
| Hairline | Orderly, exact, like a well-set form or a ledger | Professional | Warm: it reads as cold |
| Card | Tidy and familiar | Professional; a shop's tiles | Warm and artistic as the repeated item: it is the template's card |
| Torn paper | Made by hand, pinned up | Warm; artistic | Professional |
| Inked panel | Bold and printed, like a comic page or a woodcut | Artistic; warm with the pen-drawn line | Professional |
| Carved plate | Old and precious, framed as a work | Artistic; a dark, painterly lead; a shop's product pictures | Professional; a bright warm page |
| Riveted metal | A game's interface: loud, heavy, shiny | A game-style site | Almost everything else, and any page meant for long reading |
| Wavy edge | Soft and playful | Warm; a game-style site | Professional |

How to choose: ask what the site's repeated item is made of when it is not on a screen (a notice, a print, a plate in a book, a window in a game), and pick the frame that object has. Then ask where the frame goes. A frame on everything is no longer a frame: put it on the one thing each section is about, and let the rest sit on space. Most sites need one frame and at most one kind of edge.

## Options

### None
- Id: none
- Status: draft
- Looks like: no border, no box, no shadow. Groups are made by space, a heading and, where a page wants a mark between items, a small printed ornament (a fleuron or three stars) centred in the gap.
- Made with: more space between groups than inside them (the general guide's "Use space before lines and boxes"). The ornament is a character, not a picture.

```css
.item + .item { margin-top: var(--space-7); }
.item:not(:last-child)::after {           /* an optional printer's mark between items */
  content: "\2042"; display: block; margin-top: var(--space-6);
  text-align: center; color: var(--color-ink-soft);
}
```

- Careful: without lines, the space has to be unmistakable: the gap between items at least twice the gap inside one. An ornament made with `content` is read aloud by some screen readers; if it must be silent, use `content: "\2042" / ""`.
- Goes with: `density: minimal`. Between sections: none, or `wavy-edge` on a warm site.
- Used on: 1 mockup, a poetry site (one of its three looks, set like a printed booklet). It is also the general guide's default.

### Hairline
- Id: hairline
- Status: draft
- Looks like: a thin line, one pixel, in the ink colour or a soft line colour. Round a small box, or only above and below a row of facts, like a table without its sides.
- Made with: a token for the line, used for every rule on the page; a heavier rule (two or three pixels) only at the top of a group.

```css
:root { --rule: 1px solid var(--color-line); --rule-heavy: 2px solid var(--color-ink); }
.facts { border-top: var(--rule-heavy); border-bottom: var(--rule); }
.fact + .fact { border-left: var(--rule); padding-left: var(--space-5); }
.specimen { border: 1px solid var(--color-ink); border-radius: 3px; padding: var(--space-4); }
```

- Careful: a hairline that only decorates may be faint, but a line that shows where something is (a box you can tap, a field) must reach 3 to 1. On a phone, side-by-side cells with left rules become a stack; turn the left rule into a top rule there, or the lines point at nothing.
- Goes with: `density: balanced`. Between sections: a full-width hairline or nothing.
- Used on: 3 mockups: a tutor's site, a browser game's sign-up and account pages, a poetry site.

### Card
- Id: card
- Status: draft
- Looks like: a lighter box on the ground, rounded corners, a soft shadow.
- Made with: the general guide's starting tokens, `--radius` and `--shadow`, on the surface colour.

```css
.card { background: var(--color-surface); border-radius: var(--radius); box-shadow: var(--shadow); padding: var(--space-5); }
```

- Careful: this is the second tell in the general guide's template list: "every repeated item is the same white box with rounded corners and a soft shadow". It is fine for a panel that holds a form or a summary. On a warm or artistic site it must not be the repeated item; the first version of a volunteer page used it for every event and was called "very plain". The shadow is not an edge: if the card is something to tap, it also needs a border or colour that reaches 3 to 1.
- Goes with: `density: balanced`. Between sections: none or `hairline`.
- Used on: 3 mockups: the first version of a volunteer page, a poetry site (one look), a handmade shop's order panels.

### Torn paper
- Id: torn-paper
- Status: draft
- Looks like: a sheet of paper or card with uneven, cut or torn edges, laid a little crooked, sometimes held by a strip of tape or a pin. As an edge between sections: a ragged line where one band of colour has been torn across.
- Made with: the paper is a `::before` behind the words, clipped to an uneven outline with `clip-path: polygon()`, and only the paper is turned. The words stay level and sharp. The shadow goes on the element as `filter: drop-shadow()`, because a `box-shadow` is cut off by the clip. Use two or three outlines and tilts so no two sheets match. The edge between sections is an inline SVG at the top of the lower section, filled with its colour (`currentColor`), stretched across and overlapping the section above by a pixel.

```css
:root { --cut: polygon(0.6% 1.4%, 99.5% 0, 100% 98.8%, 0 100%); }
.paper { position: relative; isolation: isolate; padding: var(--space-5); color: var(--color-ink);
  filter: drop-shadow(0 3px 0 rgb(0 0 0 / 0.25)) drop-shadow(0 10px 14px rgb(0 0 0 / 0.2)); }
.paper::before { content: ""; position: absolute; inset: 0; z-index: -1;
  background: var(--color-paper); clip-path: var(--cut); rotate: var(--tilt, -0.8deg); }
.paper.tear::before { clip-path: polygon(0 1%, 7% 0, 18% 1.2%, 33% 0.2%, 52% 1%, 70% 0, 88% 0.8%, 100% 0,
  99.3% 22%, 100% 47%, 99.2% 74%, 100% 99%, 81% 100%, 60% 98.8%, 41% 100%, 23% 99%, 6% 100%, 0 99%, 0.8% 70%, 0 45%, 0.7% 20%); }
.tape { position: absolute; top: -0.7rem; left: 50%; translate: -50% 0; width: 5rem; height: 1.4rem;
  background: rgb(207 174 124 / 0.75); rotate: -3deg; }
.section-edge { position: absolute; left: 0; top: -27px; width: 100%; height: 28px; color: var(--section-colour); }   /* at the top of the section it belongs to */
```

```html
<svg class="section-edge" viewBox="0 0 1200 28" preserveAspectRatio="none" aria-hidden="true">
  <path fill="currentColor" d="M0 28V11L32 17L61 10L93 5L123 12L162 4L186 3L225 13L242 18L285 12L318 5L352 5L404 9L478 10L536 18L580 15L638 7L683 16L750 2L801 18L862 14L910 17L971 4L1038 5L1108 4L1160 18L1200 8V28Z"/>
</svg>
```

- Careful: put the clip on `::before`, never on the element itself: a clipped element loses its focus outline and its shadow. Tilts stay between one and three degrees and never touch reading text or anything typed into (warm guide, "Break the rectangle"). Anything fixed to the screen must not sit inside a turned sheet (`css-layout.md`). The audit measures contrast from a picture, so text on a sheet is measured against the paper actually drawn. On a phone, keep the tilts but halve them; a full-width sheet turned by two degrees pokes past the screen's edge.
- Goes with: `density: busy`; `background: detailed-ground` on a dark page, where the sheet is the calm patch reading gets. Between sections: the torn edge above.
- Used on: 4 mockups: a volunteer page (events as cut-paper notices, torn edges between sections), a handmade shop (taped cards, a torn edge above the footer), a small shop of handmade goods (torn sheets and luggage tags), a dark, painterly joke site (torn sheets with an ink outline).

### Inked panel
- Id: inked-panel
- Status: draft
- Looks like: a thick, flat, dark line round the panel and a hard shadow offset to one side, with no blur: a panel on a comic page or a block print. For a hand-made site the same idea in a thinner pen line that wobbles, as if drawn round the box with a fountain pen.
- Made with: a border token and a shadow token with no blur. The pen-drawn line is an SVG used as `border-image`, its rectangle roughened with an `feTurbulence` displacement filter. To ink round a shape that is not a rectangle (a torn sheet), stack four one-pixel `drop-shadow()`s.

```css
:root { --edge: 3px solid var(--color-pen); --shadow-ink: 5px 6px 0 var(--color-pen); }
.inked { border: var(--edge); box-shadow: var(--shadow-ink); background: var(--color-surface); padding: var(--space-5); }
.inked-shape { filter: drop-shadow(1.5px 0 0 var(--color-pen)) drop-shadow(-1.5px 0 0 var(--color-pen))
  drop-shadow(0 1.5px 0 var(--color-pen)) drop-shadow(0 -1.5px 0 var(--color-pen)) drop-shadow(5px 6px 0 var(--color-pen)); }
.pen-drawn { border: 10px solid transparent; background-clip: padding-box;
  border-image: url("pen-frame.svg") 30 / 14px / 3px stretch; }
```

```html
<!-- pen-frame.svg: two loose rectangles, roughened -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160"><filter id="r"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="5"/><feDisplacementMap in="SourceGraphic" scale="3.5"/></filter>
<g fill="none" stroke="#1f2a22" filter="url(#r)"><rect x="8" y="8" width="144" height="144" rx="10" stroke-width="2.2"/><rect x="10.5" y="6.5" width="141" height="146" rx="12" stroke-width="1.1" stroke-opacity="0.4"/></g></svg>
```

- Careful: the ink line should reach 3 to 1 against the ground, or it reads as a smudge. A pressed button in the same style moves into its shadow (`translate: 2px 3px` and a smaller shadow); that movement stops under reduced motion. An SVG used as `border-image` needs a `width` and `height`, not only a `viewBox`: without them the browser stretches it to the box before slicing, and the corners shrink to nothing and the line breaks into gaps (met while drawing the swatch book). `border-image` ignores `border-radius`, and without `background-clip: padding-box` the background shows through the transparent border. The hard shadow sticks out by its offset: leave that much room at the side on a phone.
- Goes with: `density: busy`; `background: detailed-ground`. Between sections: `wavy-edge`, or a short length of rule under each heading.
- Used on: 4 mockups: a dark, painterly joke site (every panel inked, torn sheets inked round), a poetry site (its bold print look), a game-style joke site (a warmer version, three-pixel dark edges on every panel), a handmade shop (the pen-drawn frame).

### Carved plate
- Id: carved-plate
- Status: draft
- Looks like: a frame like a plate in an old book or a picture in a carved wooden frame: a band of repeated ornament (beads, studs, thorns, a twisted rope) with corner pieces, round a dark or plain inner field. The plain form is a double rule: a heavy outer line and a thin inner one in a metal colour. A strip of the same carving can run between sections.
- Made with: for the ornament, a small square SVG tile used as `border-image` with `round`, so whole repeats fit each side and the corners stay corners. For the double rule, a border and an `outline` pulled inside with a negative offset.

```css
.plate { border: 12px solid var(--color-wood); border-image: url("frame.svg") 18 / 12px round; background-clip: padding-box;
  background: radial-gradient(circle at 35% 30%, var(--color-plate-hi), var(--color-plate) 75%); padding: 8%; }
.plate img { width: 100%; height: 100%; object-fit: contain; }
.plate-plain { border: 3px solid var(--color-ink); box-shadow: inset 0 0 0 5px var(--color-surface), inset 0 0 0 7px var(--color-brass); }
.band { height: 22px; background: url("band.svg") left center / auto 22px repeat-x; border-block: 1px solid var(--color-pen); }
```

- Careful: a product picture is shown whole (sales guide): the frame goes outside the picture, never over it, and the picture is fitted with `object-fit: contain`. One shop drew the inner rule with `outline` and an offset; that takes the outline away from focus, so on anything that can be focused draw the inner rule with an inset `box-shadow` instead, as above. The tile SVG needs a `width` and `height` (see the inked panel); without them the studs and corners vanish and the frame shows as a plain brown border. On a phone the band eats width on both sides: keep it to 12 to 14 pixels there. The ornament is decoration, so it lives in CSS, which screen readers do not read.
- Goes with: `background: detailed-ground`; `density: busy`. Between sections: the carved band.
- Used on: 3 mockups: two versions of a small shop of handmade goods (carved frames round every product picture and a carved band between sections; a brass double rule in the other), a dark, painterly joke site (one carved band round the whole first screen).

### Riveted metal
- Id: riveted-metal
- Status: draft
- Looks like: a chunky metal ring round a dark, nearly opaque panel, as on a game's interface: bevelled gold or steel, a rivet in each corner, a cut gem set into the top edge, a dark line round it all.
- Made with: CSS alone. A `::before` covers the panel with a metal gradient and four small radial-gradient rivets, then a mask cuts its middle out, leaving a ring as thick as its padding. The gem is an `::after` square turned 45 degrees. Swap gold for steel by changing the three metal tokens. Two of the mockups drew the ring as an SVG `border-image` instead; that allows hand-drawn wear but needs a file per metal.

```css
.metal { position: relative; background: var(--panel); border-radius: 12px; padding: var(--space-6) var(--space-5);
  box-shadow: 0 0 0 3px var(--metal-dark), 0 10px 28px rgb(0 0 0 / 0.5); }
.metal::before { content: ""; position: absolute; inset: 0; border-radius: inherit; padding: 8px; pointer-events: none;
  background:
    radial-gradient(circle at 7px 7px, var(--metal-hi) 0 1.5px, var(--metal-dark) 2.5px 4px, transparent 4.5px),
    radial-gradient(circle at calc(100% - 7px) 7px, var(--metal-hi) 0 1.5px, var(--metal-dark) 2.5px 4px, transparent 4.5px),
    radial-gradient(circle at 7px calc(100% - 7px), var(--metal-hi) 0 1.5px, var(--metal-dark) 2.5px 4px, transparent 4.5px),
    radial-gradient(circle at calc(100% - 7px) calc(100% - 7px), var(--metal-hi) 0 1.5px, var(--metal-dark) 2.5px 4px, transparent 4.5px),
    linear-gradient(170deg, var(--metal-hi), var(--metal) 22%, var(--metal-lo) 48%, var(--metal) 70%, var(--metal-hi) 92%);
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); mask-composite: exclude; }
.metal.gem::after { content: ""; position: absolute; top: -13px; left: 50%; width: 26px; height: 26px; border-radius: 3px;
  transform: translateX(-50%) rotate(45deg); border: 3px solid var(--metal-dark);
  background: radial-gradient(circle at 35% 35%, #fff 0 10%, var(--gem) 32%, var(--gem-lo) 95%);
  box-shadow: 0 0 0 3px var(--metal), 0 0 0 5px var(--metal-dark); }
```

- Careful: it is the heaviest option. Use it on the few panels that are windows (a dialog, the player's own panel, a section's main window), not on every item, or the page is all frame. The panel behind words is close to opaque (90 percent or more), so contrast holds over any painting behind it. The gem sticks up by half its size: leave room above the panel. Shine that moves (a glint sweeping the metal) stops under reduced motion. On a phone the ring stays at 8 pixels; the padding inside it, not the ring, gives way.
- Goes with: `density: busy`; `background: detailed-ground`. Between sections: `wavy-edge` between bands of landscape.
- Used on: 3 mockups: three versions of a game-style joke site (gold and silver rings drawn as SVG on two, the CSS ring with rivets and gems on the third).

### Wavy edge
- Id: wavy-edge
- Status: draft
- Looks like: the edge between two sections is a soft wave, as if one band of colour were a hill in front of the next, or a row of scallops like the edge of a canopy or a pie crust.
- Made with: an inline SVG at the foot of each band, stretched across with `preserveAspectRatio="none"`, filled with the next section's colour and laid one pixel over it. Vary the wave between sections so they do not repeat. Scallops are one repeated radial gradient, no file needed.

```css
.band { position: relative; isolation: isolate; padding: var(--space-8) var(--gutter); background: var(--this-colour); }
.band > .edge { position: absolute; bottom: -1px; left: 0; width: 100%; height: 56px; z-index: -1; color: var(--next-colour); }
.scallops { height: 24px; background: radial-gradient(circle at 50% 0, var(--this-colour) 0 70%, transparent 71%)
  0 0 / 40px 24px repeat-x; }
```

```html
<svg class="edge" viewBox="0 0 1600 80" preserveAspectRatio="none" aria-hidden="true" focusable="false">
  <path fill="currentColor" d="M0 80 V46 Q80 20 190 48 Q320 86 480 50 Q630 14 780 52 Q930 92 1080 56 Q1220 18 1360 46 Q1500 74 1600 34 V80 Z"/>
</svg>
```

- Careful: give the edge a fixed height in pixels, so the wave flattens on a wide window and deepens on a phone rather than growing huge. Without the one-pixel overlap a thin seam of the wrong colour shows between the edge and the next section on some zoom levels. Leave the section padding deep enough that no words sit in the wave. It is an edge, not a frame: pair it with a frame for panels, or with `none`.
- Goes with: `density: balanced` or `busy`; any frame in this guide except `hairline`.
- Used on: 2 mockups: a game-style joke site (waves between bands of landscape), a small shop of handmade goods (a scalloped canopy edge over its first picture).

## Swatch book

`tests/parts/frames.html` shows every option live; open it in a browser to choose by eye.

## Not covered yet

- Frames round video, maps and tables. None of the mockups framed one.
- A frame that changes with the state of what is inside (selected, full, disabled). The volunteer page lit a yellow sheet behind a chosen notice; one site is not enough for a rule.
- Rounded or blob-shaped masks on photographs, which the warm guide's study saw on several sites. No mockup here has used one.
- Diagonal and curved cuts across a whole band, as opposed to a wave at its foot.
- How frames print, and how they look with the browser's forced colours (high contrast) on, where `border-image`, masks and backgrounds are dropped. Not tested.
- Real phones. Everything here was looked at in a desktop browser pretending to be one.
