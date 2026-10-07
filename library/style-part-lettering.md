---
name: Lettering (a part guide)
summary: The typefaces a site uses and how its name and headings are set: which display face, over which reading face, and what is done to the letters. Its options can be picked on their own and combined with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: the mockups made with the skill so far, and the guides named in each option
---

# Lettering

A part guide. It covers the typefaces and how the name, headings and other short lettered words are set: the face, its weight, what is done to it (an edge, a block behind it, a stamp round it). How large reading text is and how long its lines are stay with the general guide. A site picks one option in its own guide, and in the blueprint as `project.style.parts`: `{"lettering": "<option-id>"}`. The picked option wins over the feel guide for the lettering only; the feel guide still decides everything else, and the general guide's accessibility minimums (contrast, text size, tap target size) still hold.

## Choosing

| Option | What it feels like | Suits best | Fights |
|---|---|---|---|
| Sober pair | A good book or a careful letter: calm, trusted | Professional; an education site | A dark, painterly guide; warm, where it reads as cold |
| Soft serif | Friendly and made with care; one person behind it | Warm; artistic | Nothing strongly; too gentle for a game-style look |
| Lively grotesque | Modern, cheerful, a little playful | A game or an app that should feel light | Artistic; on its own it reads as a template |
| Poster face | A bake-sale poster: fat, soft, loud | Warm | Professional; a dark, painterly guide |
| Bladed letters | A record sleeve or a painted sign: pointed, cut, old | A dark, painterly guide; warm second to it | Professional; anything for children |
| Chiselled metal | A game's title screen: carved capitals in gold or steel | A game-style look, a bright painted world | Professional; warm, unless the joke is the point |
| Hand marks | Somebody wrote on it: a squiggle, a stamp, a note | Warm; a single maker's site; added to any option above | Professional |

How to choose: start from the material the feel guide or the brief names (a poster, a book, a sign, a medal) and take the option whose letters are made of it. Two families at most, as the general guide says: one display face from the option and one plain reading face; hand marks are drawn, not typed in a third face, unless the site's own guide says the handwriting is the point (as one maker's shop did). A site with a second look the visitor can switch to may pick a different option for that look, with its own two families; write both picks in the site's guide, and check each look's count on its own.

Every face named here is free under the SIL Open Font License and comes from Google Fonts. On every mockup the files were downloaded once (the latin `woff2` file is enough for English) and kept in the site's own `fonts/` folder with their licence files, declared with `@font-face` and `font-display: swap`, so nothing is fetched from Google when the page opens (see `google-fonts.md`). A variable family comes as one file for every weight: declare it once with a range (`font-weight: 300 700`).

```css
@font-face { font-family: 'Display'; src: url('fonts/display.woff2') format('woff2');
             font-weight: 400; font-display: swap; }
:root { --font-display: 'Display', Georgia, serif; --font-body: 'Reading', system-ui, sans-serif; }
```

## Options

### Sober pair
- Id: sober-pair
- Status: draft
- Looks like: a readable book serif for headings, figures and the owner's own words, over a plain sans for everything else. Nothing is done to the letters; size, weight and rules do the work.
- Made with: Newsreader (headings, weight 600) over Source Sans 3 on the one mockup. The heading face is also used for numbers that matter (rates, years, counts) and for quoted words, so it appears in more places than the headings. One family carrying everything is allowed too, as the professional guide says ("one or two sober families"), if it reads well at length.
  ```css
  :root { --font-display: 'Newsreader', Georgia, serif; --font-body: 'Source Sans 3', 'Segoe UI', sans-serif; }
  h1, h2, h3 { font-family: var(--font-display); font-weight: 600; text-wrap: balance; }
  .fact b, .price { font: 600 var(--text-xl)/1.1 var(--font-display); }
  .quote { font: italic var(--text-l)/1.4 var(--font-display); }
  ```
- Careful: the earlier version of that page used a grotesque for headings and a code typeface for labels, and the labels were the main thing that made it read as a software product. No typewriter or code face for labels on a site about people. Headings stay at about three times body size at most, as the professional guide says.
- Goes with: `density: minimal`; plain ruled frames rather than boxes.
- Used on: 1 mockup: a private tutor's site (the owner: "way better, cleaner for sure").

### Soft serif
- Id: soft-serif
- Status: draft
- Looks like: a soft, round, slightly old-fashioned serif with character, set large for headings and names, over a plain reading face. Friendly and careful at once.
- Made with: Young Serif (one weight, 400) over Karla on one mockup; Fraunces (variable, set at weight 500) over Literata on the other. The heading face also sets the brand name and each repeated item's name. Headings are set a little tight and balanced.
  ```css
  :root { --font-display: 'Young Serif', Georgia, serif; --font-body: 'Karla', system-ui, sans-serif; }
  h1 { font: 400 var(--text-xl)/1.06 var(--font-display); letter-spacing: -0.01em; text-wrap: balance; }
  h2 { font: 400 var(--text-l)/1.2 var(--font-display); }
  h3 { font: 700 var(--text-m)/1.3 var(--font-body); }   /* small headings fall back to the reading face */
  ```
- Careful: with only one weight (Young Serif), do not ask for bold: the browser fakes it and the letters smear. The artistic guide asks for the heading to be at least three times body size on the top of the first page; these did it (68px against 19px).
- Goes with: hand marks; a paper ground; `density: balanced`.
- Used on: 2 mockups: a one-person soap shop, a small poetry site.

### Lively grotesque
- Id: lively-grotesque
- Status: draft
- Looks like: a sans with quirks (ink traps, uneven widths) in a heavy weight for headings and the name, over a plain modern sans.
- Made with: Bricolage Grotesque (variable, 700 to 800) over Figtree, on both mockups. Tight letter spacing on the large sizes; small capitals labels in the reading face.
  ```css
  :root { --font-display: 'Bricolage Grotesque', 'Trebuchet MS', sans-serif; --font-body: 'Figtree', 'Segoe UI', sans-serif; }
  h1, h2 { font-family: var(--font-display); font-weight: 700; line-height: 1.1; }
  h1, .brand { letter-spacing: -0.02em; }
  .label { font: 700 var(--text-s)/1 var(--font-body); letter-spacing: 0.08em; text-transform: uppercase; }
  ```
- Careful: this is the quietest option with character, and on its own it did not save a page. The first volunteer page used exactly this pair and was called "very plain ... like I made it with a cheap make-your-own-website tool". It is a face, not a signature; the page needs its signature from somewhere else.
- Goes with: `density: balanced`; a game or an app where the playfulness is in the drawings.
- Used on: 2 mockups: a small online game, the first version of a volunteer page (the one called plain).

### Poster face
- Id: poster-face
- Status: draft
- Looks like: a fat, soft display face set huge, white on blocks of cut paper that are turned a degree or two, over a face drawn to be easy to read. Like a poster in a community hall.
- Made with: Caprasimo (one weight) for anything lettered: headings, the repeated item's name, the day number, the main button. Atkinson Hyperlegible Next for everything else. The biggest words sit on blocks drawn behind them (`::before`, clipped to an uneven outline); only the block is turned, so the letters stay sharp. The headline reached seven times the reading size on a wide screen. The warm guide's study also saw a stencilled heading for a farm; no mockup has used a stencil face yet, but it belongs here, chosen the same way, for the material.
  ```css
  :root { --font-display: 'Caprasimo', Georgia, serif; --font-body: 'Atkinson Hyperlegible Next', system-ui, sans-serif;
          --text-poster: clamp(3.5rem, 1.6rem + 9vw, 8.5rem); --cut: polygon(0.6% 1.4%, 99.5% 0, 100% 98.8%, 0 100%); }
  h1, h2, h3 { font-family: var(--font-display); font-weight: 400; line-height: 1.1; }
  .block { position: relative; z-index: 0; display: block; width: fit-content; padding: 0.06em 0.2em 0.12em;
           font-size: var(--text-poster); line-height: 1; color: var(--paper); rotate: -2.5deg; }
  .block::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--felt); clip-path: var(--cut); }
  .block + .block { margin: -0.07em 0 0 0.55em; rotate: 1.5deg; }
  ```
- Careful: the turn is a few degrees and never on reading text or fields. `check` reads the colour of the block drawn this way when it measures contrast. On a phone the poster size comes down with `clamp`, and each block must still fit the width: try the longest word at 320 pixels.
- Goes with: hand marks; `density: busy`; bold flat colour.
- Used on: 1 mockup: a volunteer sign-up page (the owner: "looks great now, very styled, I love it").

### Bladed letters
- Id: bladed-letters
- Status: draft
- Looks like: a blackletter or pointed, cut face with blades in it, like a heavy-metal record sleeve or a painted stall sign, for the name and section titles only, over a sturdy book face for everything read. Often pale metal or brass with a hard dark offset edge.
- Made with: Grenze Gotisch (weight 600) over Vollkorn; New Rocker over Alegreya; Pirata One over Alegreya; Pirata One over EB Garamond. The colour is a pale metal or brass, flat, never a gradient, with a sharp offset shadow in the darkest ink. The reading face was chosen with thick strokes, because thin strokes vanish on a dark ground.
  ```css
  :root { --font-display: 'Pirata One', 'Palatino Linotype', serif; --font-body: 'Alegreya', Georgia, serif;
          --letter: #c9a25a; --pen: #000; }
  h1, h2, .mark { font-family: var(--font-display); font-weight: 400; color: var(--letter); text-shadow: 2px 2px 0 var(--pen); }
  h1 { font-size: var(--text-xl); line-height: 0.98; letter-spacing: 0.01em; text-shadow: 3px 3px 0 var(--pen); }
  .sheet h2 { color: var(--ink); text-shadow: none; }   /* on a light sheet, plain ink */
  ```
  A softer cut edge, for pewter on a dark plank: `text-shadow: 0 1px 0 #6e6656, 0 -1px 0 #fffaf0, 0 3px 6px rgb(0 0 0 / 0.7)`.
- Careful: only ever a few words, and at heading sizes (one mockup set a three-line headline in it at up to 88px and it still read). Never for buttons, prices, fields or anything read at length: those are in the reading face. The same face on two sites with the same lead guide makes them look like one site; one shop chose Grenze Gotisch, saw that the last mockup used it, and swapped to New Rocker. Look at the last mockup's faces before choosing.
- Goes with: `frames: inked-panel`; a detailed dark ground; `density: busy`.
- Used on: 4 mockups: a dark, painterly joke site, two versions of a small shop, one side of a game-style joke site.

### Chiselled metal
- Id: chiselled-metal
- Status: draft
- Looks like: flared, carved capitals in gold (or cold steel) with a dark edge all round and a deep drop below, like the title of a game. A friendly sans or a bookish serif for reading.
- Made with: Cinzel Decorative (700 and 900) over Signika on two mockups, Marcellus over Alegreya Sans on the third; on their second looks, Metamorphous over Philosopher and Cinzel over Spectral. The metal is made with stacked text shadows: a light line above, a dark edge drawn four ways, a lower tone for depth, then a soft drop.
  ```css
  :root { --font-display: 'Cinzel Decorative', Georgia, serif; --font-body: 'Signika', 'Trebuchet MS', sans-serif;
          --metal: #ffd76a; --metal-hi: #fff2b8; --metal-lo: #8a5c14; --metal-edge: #3a2405; }
  .title { font: 900 var(--text-xl)/0.95 var(--font-display); color: var(--metal);
           text-shadow: 0 -1px 0 var(--metal-hi),
             2px 2px 0 var(--metal-edge), -2px 2px 0 var(--metal-edge), 2px -2px 0 var(--metal-edge), -2px -2px 0 var(--metal-edge),
             0 4px 0 var(--metal-lo), 0 7px 0 var(--metal-edge), 0 12px 18px rgb(0 0 0 / 0.55); }
  h2, h3 { font-family: var(--font-display); color: var(--metal); text-shadow: 0 2px 0 var(--metal-edge); }
  ```
  For steel, keep the shadows and swap the four colours (`#bdeaff`, `#ffffff`, `#4f5f75`, `#121b29`).
- Careful: the edge drawn all round is what lets gold read over a painted sky; without it the contrast depends on what is behind. `check` and `audit` measure it from a picture, so run them over the busiest part of the ground. Cinzel and Cinzel Decorative have capitals only: names and short titles, never sentences. Never use a real product's own lettering or font files; pick a free face of the same kind and say so in the site's guide. One of the mockups set buttons in the display face; short labels are fine, anything longer goes in the reading face.
- Goes with: `frames: riveted-metal` or another game-interface frame; a bright painted ground.
- Used on: 3 mockups: three versions of a game-style joke site.

### Hand marks
- Id: hand-marks
- Status: draft
- Looks like: typed words with something drawn by hand on or round them: a wavy line under a phrase, a word in a tilted rubber stamp, a few words of handwriting with an arrow. It is added to whichever option the site picked.
- Made with: the squiggle is a small inline SVG path under the words; the stamp is the reading face in bold capitals with a border (double, for a rubber stamp), tilted three to fourteen degrees; handwriting, where the site's own guide allows a third face, was Caveat for a few words at a time.
  ```css
  .rest { position: relative; display: block; width: fit-content; padding-bottom: 0.3em; }
  .squiggle { position: absolute; left: 0; bottom: 0; width: 100%; height: 0.3em; }
  .squiggle path { fill: none; stroke: var(--felt); stroke-width: 4; stroke-linecap: round; }
  .stamp { display: inline-block; padding: 2px var(--space-2); border: 3px double var(--stamp); color: var(--stamp);
           font: 700 var(--text-s)/1.2 var(--font-body); letter-spacing: 0.12em; text-transform: uppercase; rotate: -6deg; }
  .hand { font: 600 var(--text-hand)/1.15 var(--font-hand); }   /* only where the site's guide allows a third face */
  ```
  ```html
  <span class="rest">at our next event<svg class="squiggle" viewBox="0 0 300 14" preserveAspectRatio="none" aria-hidden="true">
    <path d="M3 8c20-8 30 6 50 0s30-8 50-1 30 6 50 0 30-7 50-1 30 5 46 0 30-6 46-1"/></svg></span>
  ```
- Careful: the drawing is hidden from screen readers (`aria-hidden="true"`), and the stamp's word is also written somewhere a screen reader reads it ("Full", "Sold out"). A stamp is small text: it needs 4.5 to 1 against its own ground. Handwriting is never for anything read at length, labels on fields, or prices alone. Drawn marks sit on headings, edges and the repeated item, never on form fields, as the warm guide says.
- Goes with: soft serif; poster face; bladed letters on a shop; `density: busy`.
- Used on: 4 mockups: a volunteer page (the squiggle, a "Full" stamp), two versions of a small shop (a stamp), a one-person soap shop (handwriting as a third face, agreed in that site's guide).

## Swatch book

`tests/parts/lettering.html` shows every option live; open it in a browser to choose by eye.

## Not covered yet

- A stencil face, a typewriter face and a condensed gothic poster face: seen in the warm guide's study, never used on a mockup.
- One family carrying the whole site, as the artistic guide describes: no mockup has done it yet.
- Lettering drawn as a picture (a logo traced by hand, letters cut from paper as SVG). Every mockup typed its lettering.
- Languages other than English: every mockup kept only the latin file, which lacks many accented letters in some faces.
- How these faces look on Windows and on a phone's own browser; every picture so far was taken in the skill's test browser.
- Whether the downloaded files are the best formats for every browser: `google-fonts.md` still marks self-hosting as unconfirmed in a real build.
