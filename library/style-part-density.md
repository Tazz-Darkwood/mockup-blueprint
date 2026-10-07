---
name: Density (a part guide)
summary: How full a page is - how much of it is left empty, how many things share a screen, how much decoration there is and how big the gaps are. Each option can be picked on its own and used with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: the mockups made with the skill so far, and the guides named in each option
---

# Density

A part guide. It covers how full a page is: how much of the screen is left empty, how many things share a screen, how much decoration fills the gaps and how big the gaps are; it turns the brief's line "How full the page should feel" into choices. A site picks one option in its own guide, and in the blueprint as `project.style.parts`: `{"density": "<option-id>"}`, and the picked option wins over the feel guide for density only, while the feel guide still decides what the page is made of. The general guide's accessibility minimums (contrast, text size, tap size) still hold, and so does its one spacing scale, from `--space-1` (4 pixels) to `--space-9` (96 pixels): the options differ only in which end of it they use.

## Choosing

| Option | What it feels like | Suits best | Fights |
|---|---|---|---|
| Minimal | One thing at a time, on an open page; quiet and slow | Artistic, for a site of single works to look at (poems, prints); the plain pages of any site (signing in) | Warm; a shop with many items; any page whose content is thin, which then looks unfinished |
| Clean | Everything in order, nothing extra; a normal amount on a page, lined up | Professional | Warm: it reads as cold. A dark, painterly lead |
| Balanced | Lively and made by hand, with room to breathe | Warm; artistic; the default when the brief does not say | Little; on a professional site keep its marks few |
| Full but quiet | Every part of the window is used, like a game screen, but each panel is calm inside | A page that is a working tool or a game; a game-style site | Long reading; professional |
| Busy | Fill the frame: every surface worked, narrow filled gaps, calm patches only behind words and controls | A dark, painterly lead; warm when the brief asks for full (filled with warm things) | Professional; a page whose job is one quick form |

How to choose: ask how many things a visitor needs on one screen, and what the space between them is for. One thing to look at closely: minimal. Many facts to compare and trust: clean. A club or a maker with a lot of personality: balanced. A tool used for a long sitting: full but quiet. A world to get lost in: busy.

A page's density can differ from page to page on one site, and that is a decision to write down: one site made its game screen full but quiet and every other page minimal. A sign-in page is usually quieter than the front page whatever was picked; say so in the site's guide rather than letting it happen.

Density is not the template test. A page passes or fails "It must not look like a template" (in the general guide) at any density. The one mockup the owner called a template measured almost exactly like a clean one; see Clean.

## Options

How the numbers under "Measured" were taken. Every option gives signs that can be measured, taken from the mockups, so that "busy" or "minimal" can be checked on a page rather than argued about. All of them are for a window 1280 pixels wide and 800 tall, on each mockup's front page.

- **Open space** is the share of the page that is plain: patches at least about 80 pixels across with no detail in them (no words, no drawing, no grain strong enough to see). The calm patches behind words count only where they are wider than that. It was measured from a picture of the whole page, cut into 16-pixel squares.
- **Things per screen** is the number of separate pieces of text (a heading, a paragraph, a list item, a label) per 800 pixels of page.
- **Decoration per screen** is the number of drawn pieces that carry no meaning (hidden from screen readers, or a background picture on an element) per 800 pixels.
- **Gaps** are the steps of the spacing scale the mockup used between sections, between items, and inside items.

On a phone the options come together: every mockup left 17 per cent of the page open or less, most of them under 10, because a 390-pixel screen has no room for empty margins. On a phone the options differ in the size of the gaps and in how much decoration survives, not in open space.

### Minimal
- Id: minimal
- Status: draft
- Looks like: very few things on the page, with wide open space round each one. One poem, one form, one picture to a screen. The space is part of the design, the way a printed book leaves wide margins.
- Measured: 65 per cent open space on a poetry site's first version (the most of any mockup), 47 per cent on a sign-in page. Two or three pieces of text per screen on the poetry version. Gaps: the top of the scale. Items one under another, `--space-8` (64 pixels) apart, the first `--space-7` below the heading; sections `--space-9` apart. Inside an item, `--space-3`.
- Made with: one column of items with large gaps and no boxes; names and dates set in a margin column beside each item, as in a book, so that the page is not one centred column; a ground with a little grain rather than flat white; one drawn or lettered thing made for the site, set large in the open space.

```css
.feed { display: flex; flex-direction: column; gap: var(--space-8); padding-top: var(--space-7); }
.entry { display: grid; grid-template-columns: 11rem minmax(0, 1fr); column-gap: var(--space-6); }
.entry-meta { font-size: var(--text-s); color: var(--color-ink-soft); }   /* the margin column */
body { background: var(--color-paper) url(art/grain.svg); }               /* the space is a material */
@media (max-width: 40rem) { .entry { grid-template-columns: minmax(0, 1fr); row-gap: var(--space-2); } }
```

- What keeps it from looking like a template: a minimal page has fewer places to show a choice, so the few it has must all show one. The general guide's first tell, a heading, a sentence and a button with nothing made for the site beside them, is where a minimal page ends up when nothing was chosen. So:
  1. The open space is a material, not blank white: paper with grain, or a deep colour. A pale ground with white boxes is tell 7.
  2. One thing made for this site sits in the space, large: a brush mark, a lettered name, a single picture. On the poetry site it was a brush circle beside the heading, and the owner said "the fancy top part was really good".
  3. It leaves the centred column: a margin column, or things set off-centre. One centred column with straight edges is tell 8.
  4. No boxes. Minimal with a white rounded card round every item is tell 2; let space group things instead (`frames: none`).
  5. The headline is a chosen face, three times the body size or more (tell 6).
- Careful: this is the option most likely to look unfinished. The poetry site's first version, set like a printed book with large poems on an open page, was liked for its feel ("the whole feel of the mockup is way better") and still read as "too empty"; it went to balanced, keeping the paper, ink and type. Use minimal only where the content is worth looking at closely on its own, or for pages with one job (signing in). On a phone it loses most of its open space anyway; keep the large gaps between items there (`--space-7` at least) or it becomes a plain list. The open space must not push the main heading or the one action below the first phone screen.
- Goes with: `frames: none`, `background: grain` or `plain`, `lettering: soft-serif` or `poster-face`, `light: flat-and-even`.
- Used on: 2 mockups: the first version of a poetry site (judged too empty for its front page), and the inner pages of a small shared-world game site (signing in, signing up, choosing), whose brief said "every other page is spare".

### Clean
- Id: clean
- Status: draft
- Looks like: a normal amount on each screen, all of it lined up. Facts in a row, lists in ruled rows, columns that share edges. Generous space between sections, closer space inside them, and almost no decoration. Order, not emptiness, is what makes it feel calm.
- Measured: 41 to 52 per cent open space (a tutor's site 52, a game site's front page 41). Six or seven pieces of text per screen; about one piece of decoration per screen or less. Gaps: sections `--space-9` (96 pixels) apart top and bottom; groups inside a section `--space-7` to `--space-8` (48 to 64); items in a list `--space-4` apart, with a thin rule between; inside an item `--space-1` to `--space-3`.
- How it differs from minimal: clean holds a full page of content, arranged; minimal holds very little. Clean has about three times the things per screen and uses rules and a grid to group them; minimal uses space alone and has no grid to speak of.
- Made with: sections with deep padding; a grid for anything side by side; thin rules instead of boxes for rows and columns; a plain ground in two bands at most.

```css
.section { padding-block: var(--space-9); display: flex; flex-direction: column; gap: var(--space-7); }
.cols-2 { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-7) var(--space-8); }
.facts { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 2px solid var(--color-ink); }
.fact { padding: var(--space-5) var(--space-5) var(--space-5) 0; }
.fact + .fact { border-left: 1px solid var(--color-line); padding-left: var(--space-5); }
.entry { display: flex; gap: var(--space-5); padding-block: var(--space-4); border-top: 1px solid var(--color-line); }
@media (max-width: 40rem) { .section { padding-block: var(--space-7); } .cols-2 { grid-template-columns: minmax(0, 1fr); } }
```

- Careful: clean is the density of a template. The volunteer page the owner called "very plain and used the same format a lot of websites do" measured 38 per cent open space, 15 pieces of text per screen and no decoration: clean numbers. What made the tutor's site clean and not a template was what it chose, not how full it was: ruled rows and columns instead of twenty rounded cards, three facts set large across the full width, a serif chosen for the headings, the tutor's portrait in the first screen. Run the template test on a clean page before anything else. The rules between rows are decoration to a screen reader and need no label; a rule that marks a group still needs the group to have a heading.
- Goes with: `frames: hairline`, `background: plain`, `lettering: sober-pair`, `materials: fine-paper`, `light: flat-and-even`.
- Used on: 2 mockups: a tutor's site, and the front page of a small shared-world game site. Also the general guide's starting set of tokens and the professional guide's "orderly grid, generous space".

### Balanced
- Id: balanced
- Status: draft
- Looks like: the page is coloured and textured all over, with hand-made marks here and there and the repeated items drawn as objects, but there is still room round each thing. Bands of colour carry the sections; open space is there, but it is coloured or grained, not blank.
- Measured: 29 to 39 per cent open space (a soap maker's shop 29, a volunteer page 34, a poetry site 39), and much of that is grain or colour: counted strictly, with fine grain as detail, the poetry site falls to 6 per cent. Six to nine pieces of text per screen. Decoration: two to three hand-made marks per screen, more where the repeated item carries its own drawing (the volunteer page drew a paper hand for every helper, sixteen to a screen). Gaps: sections `--space-8` (64 pixels) apart; items `--space-5` to `--space-6` (24 to 32) on a phone and up to `--space-7` (48) on a wide screen; inside an item `--space-3` to `--space-4`.
- Made with: one band per section, each in a flat colour or a grained paper, with a shaped edge between some of them; the repeated item framed in the site's material and tilted a degree or two; two or three marks drawn for the site per screen, on headings and on the edges of sections, never on fields.

```css
.section { padding-block: var(--space-8); }
.band { background: var(--color-band) url(art/grain.svg); color: var(--color-band-ink); }
.items { display: grid; gap: var(--space-6); grid-template-columns: repeat(auto-fill, minmax(min(100%, 15rem), 1fr)); }
@media (min-width: 64rem) { .items { gap: var(--space-7); } }
.item { padding: var(--space-4); }
h2::after {                                   /* one hand-drawn mark under a heading */
  content: ""; display: block; width: 7rem; height: 0.75rem; margin-top: var(--space-2);
  background: url(art/squiggle.svg) left center / contain no-repeat;
}
```

- Careful: the general guide's "the gap inside a group is smaller than the gap between groups" is what keeps a lively page readable; check it first when it starts to feel crowded. Marks sit beside words, not under them, and are hidden from screen readers. Contrast is measured on every band's colour, and over grain from a picture (`check` does this). Tilts are small and never on text meant for reading or on a field. On a phone, keep the marks but halve the gaps between sections to `--space-7`.
- Goes with: `background: coloured-bands` or `grain`, `frames: torn-paper` or `wavy-edge`, `materials: paper-and-tape`, `lettering: poster-face` or `hand-marks`.
- Used on: 3 mockups: a soap maker's shop, a volunteer page and a poetry site (its final version, after the first was too empty), and below the top of a small dark shop. Also the warm guide's "two or three hand-made marks, then stop". The poetry site's and the tutor's briefs both say "balanced"; the tutor's site measured as clean, so the word alone in a brief is not enough. Say which option.

### Full but quiet
- Id: full-but-quiet
- Status: draft
- Looks like: a game screen or a working tool. The whole window is used: a scene or a working picture fills it, and panels, readouts and controls sit in every region of it. But nothing between the panels is decorated, and each panel is plain and solid inside, calm enough to read in.
- Measured: 8 per cent open space in the first screen of a game-interface page, whose scene fills the window behind its panels; 26 per cent on the game screen of a small shared-world game, a 3D view beside a column of readouts, with about 19 controls and readouts to a screen and the whole page fitting in 1.3 screens. Gaps: small, `--space-3` to `--space-5` (12 to 24 pixels) between panels; inside a panel `--space-2` to `--space-4`.
- How it differs from busy: the fullness comes from the number of panels and readouts and from the picture behind them, not from ornament. There is no texture or drawn sign in the gaps; the gaps are narrow and plain.
- Made with: a layout sized to the window, not to the content, so the first screen holds everything that is used often; a scene or picture as the ground; panels with solid backgrounds placed in the regions of a grid; small gaps.

```css
.screen {
  display: grid; gap: var(--space-4); padding: var(--space-4); min-height: 100dvh;
  grid-template-columns: minmax(0, 2fr) minmax(0, 1fr);
  background: var(--color-sky) url(art/scene.svg) center bottom / cover no-repeat;
}
.panel { background: rgb(14 16 24 / 0.92); color: var(--color-panel-ink); padding: var(--space-4); border-radius: var(--radius); }
.readouts { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: var(--space-3); }
@media (max-width: 48rem) { .screen { grid-template-columns: minmax(0, 1fr); min-height: 0; } }
```

- Careful: panels over a picture are at least 90 per cent opaque, or contrast changes with whatever passes behind them; `check` measures it from a picture. Bars that stay on the screen take less than a quarter of a phone's screen, and the last thing on the page is not hidden behind one (the phone guide). On a phone the panels stack in one column and the scene shrinks to a strip at the top: decide the order. Decoration in the scene is hidden from screen readers. Anything that moves in the scene stops under reduced motion. Long reading text does not belong on this page; link to a page with another density.
- Goes with: `background: one-long-scene` or `painted-ground`, `frames: riveted-metal`, `materials: metal-and-dark-glass`, `light: daylight`.
- Used on: 2 mockups: the interface version of a game-style joke site (its brief: "dense, like a game screen: something in every part of the window, but every panel calm enough to read in"), and the game screen of a small shared-world game site (its brief: "busy but quiet").

### Busy
- Id: busy
- Status: draft
- Looks like: fill the frame. No part of the page is left flat and empty: the ground has grain and pattern, borders are carved or drawn, the margins and the gaps between sections hold small drawn things. The gaps are narrow and filled. The only calm patches are the ones behind words and controls, each just big enough for what is on it.
- Measured: 7 to 15 per cent open space over the whole page (a dark, painterly joke site 7, a dark shop 10 and 15 in its two versions, two game-style joke sites 9 and 10), and 0 to 21 per cent in the first screen, where the calm patches are. Ten to eighteen pieces of text per screen, the most of any option. Five to sixteen pieces of decoration per screen. Gaps: the scale stops at `--space-7` (48 pixels); nothing larger is used. Sections `--space-5` (24) apart with a drawn band in the gap; items `--space-2` to `--space-5` (8 to 24) apart; the calm patch round words padded `--space-5` to `--space-6`.
- Made with:
  1. A ground with grain over a pattern or a painted surface, never flat.
  2. A drawn band between sections, in place of open space.
  3. Small drawn signs (circles, stars, marks, little diagrams) set down by hand in the margins and gaps, each with its own size, place and tilt, never in rows. More of them on a wide screen, fewer on a phone.
  4. A calm patch behind every piece of reading text, every field and every button: a plain panel or sheet in one token colour, so contrast is measured on a known colour.

```css
:root { --gap-section: var(--space-5); }                        /* the small end of the one scale */
body { background: var(--color-ground) url(art/grain.svg), url(art/pattern.svg); }
.wall { overflow-x: clip; }                    /* signs may run off the edge; clip, not hidden, so sticky still works */
.rule {                                        /* a drawn band in the gap between sections */
  height: 26px; margin-block: var(--gap-section);
  background: url(art/band.svg) repeat-x center / auto 26px;
}
.calm { position: relative; padding: var(--space-5); background: var(--color-calm); color: var(--color-calm-ink); }
.calm > :not(.sign) { position: relative; z-index: 1; }
.sign {                                        /* a drawn sign in a margin; decoration only */
  position: absolute; z-index: 0; pointer-events: none;
  fill: none; stroke: currentColor; stroke-width: 2; color: var(--color-chalk); opacity: 0.5;
}
.s1 { width: 120px; left: -34px; top: -66px; rotate: -14deg; }    /* each sign its own place, size and tilt */
.s2 { width: 86px; right: -30px; top: 12px; rotate: 20deg; }
@media (max-width: 40rem) { .s2 { display: none; } }                /* fewer on a phone */
```

```html
<svg class="sign s1" viewBox="0 0 100 100" aria-hidden="true" focusable="false">
  <circle cx="50" cy="50" r="40"/><path d="M50 10 L50 90 M10 50 L90 50 M22 22 L78 78"/>
</svg>
```

- Careful: busy means full of detail, not full of light or colour: the page keeps one bright thing and the rest stays dark or muted. Signs sit behind or beside things, never over words or controls, and none looks like something to press. They are hidden from screen readers. Contrast is measured on the calm patch's own colour, and over the texture from a picture by `check` and `audit`; a patch too small to hold its words at 4.5 to 1 is the usual failure. The general guide's "more space between groups than within" still holds, inside a smaller range: within a group `--space-2` to `--space-3`, between groups `--space-5`. On a phone the margins shrink to about 12 pixels each side, so there is almost no ground to fill: signs there are slivers in the gaps, and marks inside the margins of the calm patches do most of the work. Signs running off the edge cause sideways scrolling; clip them on a wrapper with `overflow-x: clip`. Busy takes the most drawing of any option, and an option picked without the time to draw it comes out as clutter.
- Goes with: `background: detailed-ground`, `frames: carved-plate` or `inked-panel`, `materials: parchment-and-ink` or `stone-and-chalk`, `light: one-light`, `lettering: bladed-letters`.
- Used on: 5 mockups: a dark, painterly joke site, a small dark shop in two versions (one busy all through, one only at the top), and two versions of a game-style joke site. On the shop, the busy version was the one the owner chose. When warm leads and the brief asks for busy, the page is still filled, "but with warm things": cut paper, bunting, the members' own drawings (the general guide, "When guides are stacked").

## Swatch book

`tests/parts/density.html` shows every option live, each with the same small piece of content; open it in a browser to choose by eye.

## Not covered yet

- Full at the top and balanced below, on one page. Tried once, on a shop where a warm guide led and a dark guide came second; the owner found it "a worse version" of the busy one. Which guide led was changed at the same time, so the result says little about density. Not an option yet.
- Data-heavy pages (tables, dashboards, account pages), where many things per screen is the job. No mockup has had one large enough to measure.
- How density should change between a phone and a wide window beyond the gaps. Every option ends up nearly full on a phone; whether minimal or clean should keep more open space there has not been asked.
- The numbers come from twelve mockups and one window size. They are signs to check a page against, not limits; a page can be busy at 18 per cent open space.
- Measuring it automatically. The open-space figure was taken with a one-off script, not with `check` or `audit`.
