---
name: Lettering (a part guide)
summary: The typefaces a site uses and how its words are set, in layers that switch on their own - the reading face, the heading face and what is done to it, the type scale, case and spacing, and marks drawn on words - from one sober family to fat poster letters on cut paper, carved capitals or a blackletter name. It owns typefaces, sizes, weights, the scale, case and letter-spacing, and pencil rings, stamps and highlights on words. Each layer works on a light page and a dark one, and can be picked with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: research online (six kinds of source, listed under Sources), the lettering of 15 mockups made with the skill, the four problems their makers met with this part's first version, the feel guides named in each option, and measurements of the font files themselves
---

# Lettering

A part guide. It covers the words as letters: which face is read, which face the headings are in and what is done to it, how big each step is, how labels and headings are cased and spaced, and anything drawn on the words. It is made of five layers, each one decision that switches on its own: **body**, **display**, **scale**, **voice** and **marks**. A site picks a starting point whole, or a starting point with one layer changed, in its own guide and in the blueprint as `project.style.parts`: `{"lettering": "sober-pair"}`, or `{"lettering": {"start": "poster-face", "marks": "pencil"}}`. The pick wins over the feel guide for the lettering only. The general guide's accessibility minimums (contrast, text size, tap size) still hold whatever is picked.

**This part owns typefaces, sizes, weights, the type scale, case and letter-spacing** (the owners table in the general guide), and the marks drawn *on words*: a pencil ring round a word, a wavy line under a phrase, a highlighter, a rubber stamp, a handwritten note. A drawn line between sections is the frames part's; a drawn sign on the ground is the background's; an icon is picture style's.

**It does not own colour or shadows.** Every letter is drawn in the shared colour names: `--ink` on sheets, `--on-ground` straight on the ground, `--ink-soft` for small print, `--mark` for drawn marks and for metal and two-colour lettering, `--band-1` to `--band-3` with `--on-band` for poster blocks. A text shadow (a carved edge, a hard offset) is a shadow, so it falls the way the light part says: every offset is a multiple of `--lx` and `--ly`, in `--shade`. A heading whose shadow fell left on a page lit from the left would argue with every sheet below it.

## How it is built

Every option's code is written to be lifted into a site's stylesheet by `blueprint.py style css`: it sets values on the page root and styles the shared hooks and plain elements (`h1`, `.label`, `.btn`), and loads only its own face. What every pick needs (the reading face on `body`, headings at the scale's sizes, the measure) is under **Base**. What this part hands to the rest of the page:

| Property | Set by | What it is |
|---|---|---|
| `--font-body` | body | the reading face, with its fallbacks: everything read at length, fields, buttons, labels |
| `--font-display` | display | the heading face: the name, headings, the figures that matter. With `display: one-family` it is the reading face |
| `--text-s`, `--text-m`, `--text-l`, `--text-xl`, `--text-xxl` | scale | label, reading text, subheading, section heading, and the one biggest thing on the first screen |
| `--measure` | this part | the longest line of reading text, `62ch`. Density decides how wide columns are; inside any column, reading text stops here |
| `--lettering-read-weight` | this part | the reading weight: 400, and 370 on a dark page (see "On a dark page") |

A page marks up a few things of lettering's own beside the hooks: `.lettering-fig` on the figures that matter (a price, a date, a count), `.lettering-name` on a name set in the display face outside a heading, `.lettering-word` round each word or line of the biggest heading that gets its own block (`display: fat-poster`, `condensed-gothic`), and the marks (`.lettering-ring`, `.lettering-wave`, `.lettering-hl`, `.lettering-stamp`, `.lettering-hand`).

**Two typefaces at most** (R1: "Most documents can tolerate a second font. Few can tolerate a third"). Body is one, display is the other, or the same one. Marks are drawn, not typed, with one exception (`marks: handwriting`), which counts as a third face and needs the site's own guide to agree. Before adding the second face at all, try the first one's weights, widths and optical sizes (R7).

**The heading rule, settled.** The general guide's template tell counts "the biggest [heading] under three times the body size"; the professional guide asks for headings "about three times body size at most". Both are one rule about two different headings: **the one biggest thing on the first screen (`--text-xxl`) is at least three times body size at a wide window; every other heading (`--text-xl` and below) stays under three times.** The biggest is what stops a page looking like a template; the rest keep the page from shouting. On a phone the biggest comes down to two and a half times (the phone guide: headings come down, reading text does not). No source gives "three"; it is judgement, checked against what design systems do at their largest step: Material's display large is 57 against a 16px body (3.6 times, R17), GOV.UK's largest is 80 against 19 (4.2 times, R14), Carbon's 92 against 16 (R18). All three scales below meet it, and the swatch book's test measures it.

**Loading the faces.** Host the files with the site (`google-fonts.md`): the latin `woff2` from Fontsource (R51), with its licence file beside it. Declare a variable family once, with its range: `font-weight: 200 800`. Use `font-display: swap` for the reading face, so words show at once, and `swap` or `optional` for the display face (R22, R29: `optional` waits at most 100ms and then keeps the fallback for that visit, which suits a face that is only decoration). Preload at most one file, the reading face, with `crossorigin` even on the same site (R23). Pick fallbacks of the same shape (Georgia for a serif, Arial Narrow for a condensed face) so the page jumps less when the face arrives; `size-adjust` on a fallback `@font-face` can close the gap (R30, R31).

```css
@font-face { font-family: 'Newsreader'; src: url('fonts/newsreader-latin-wght-normal.woff2') format('woff2');
             font-weight: 200 800; font-display: swap; }
```
```html
<link rel="preload" href="fonts/source-sans-3-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
```

**Licences and subsetting.** Use only faces under the SIL Open Font License. Self-hosting them is allowed (R50: "loading the fonts dynamically as webfonts through CSS @font-face declarations is a much better method"). Cutting glyphs or axes out of a file is modification (R50, 2.6), and a modified file may not keep a **Reserved Font Name**: read the first line of each `OFL.txt`. Of the faces here, Source Sans 3 ('Source'), Pirata One ('Pirata') and Cinzel ('Cinzel') have one: use their files as downloaded. Fontsource's latin files are already cut to the latin block; cutting them further saved only 2 to 9 per cent in the swatch book (Karla 32 to 30 KB, Caveat 75 to 73 KB), so it is not worth it. Cutting axes is: see `display: soft-serif`.

**On a dark page.** Light letters on a dark ground look heavier and glare ("halation", R10: Lato Regular on dark looks like Semibold on light). So on a dark tone the reading face is set a little lighter, 400 down to 370 (R42 went from 400 to 350), with `--lettering-read-weight`. A face with a grade axis (`GRAD`: Signika, Roboto Flex) can thin its strokes without changing widths, so nothing reflows (R10, R42). One-weight display faces (Caprasimo, Pirata One, Cinzel Decorative) cannot thin: they are set large, where it does not matter.

## Choosing

Start from a starting point (below), then change a layer if the brief asks for it.

| Starting point | What it feels like | Suits best | Fights |
|---|---|---|---|
| Sober pair | A good book or a careful letter: calm, trusted | Professional, education, a single expert | A dark painterly look; warm, where it reads as cold |
| Professional | The same, quieter: a firm that is exact | Services, money, health | Anything hand-made |
| Civic | One plain family anyone can read, even on a bus | Councils, charities, forms | Any page that needs a signature from its type |
| Almanac plate | Figures in a book serif, small capitals labels: a printed almanac | A society, an observatory, a timetable | A shop, a game |
| Soft serif | Friendly and made with care; one person behind it | Warm; artistic; a single maker | Too gentle for a game screen |
| Catalogue of glazes | Soft, light and slow, with an italic turn | A gallery, a craft studio, a quiet shop | Busy pages; anything loud |
| Hand marks | Somebody wrote on it: a ring, a squiggle | A single maker, a club | Professional |
| Field journal | A naturalist's notebook: plain print and pencil marks | A walking club, a garden, a survey | A dark lead |
| Lively grotesque | Modern, cheerful, a little playful | A game or an app | Artistic; on its own it reads as a template |
| Artistic | One family with character, pushed very large | A gallery, a studio, an exhibition | Forms-heavy pages |
| Poster face | A bake-sale poster: fat, soft, loud | Warm; a community hall | Professional |
| Warm | The poster face with pencil marks on it | A street, a club, volunteers | Professional; a dark painterly lead |
| Lantern fair | Poster blocks under one lamp at night | A night market, an evening event | Daytime services |
| Repair cafe | Poster blocks, tracked labels and a stamp | A busy community page | A calm brief |
| Bladed letters | A record sleeve or painted stall sign | A dark painterly guide; a fair stall | Professional; anything for children |
| Sorcery | A blackletter name, huge, over a book face | The sorcery guide | Anything bright and official |
| Chiselled metal | A game's title: carved capitals in metal | A game-interface look | Professional; warm, unless the joke is the point |
| Gilded dark | The same, bigger, with tracked labels | The gilded dark guide | Calm or official sites |

How to choose:

- **Start from the material.** The brief or the feel guide names one (a poster, a book, a sign, a medal, a notebook): take the display face made of it. Wood type was cut for posters because it was "lighter and cheaper than large sizes of metal type" (R43); carved capitals come from Roman inscriptions (R46); blackletter survives on mastheads (R47).
- **Then the reading face, for the reader.** A plain face for long reading; `hyperlegible` when readers are many and varied, or read on a phone in poor light (the night market chose it because "the reading face must survive being read on a phone in the dark").
- **Then the personality.** Every option says which of the five it suits; the display face moves it most.
- **Look at the last mockup's faces.** The same face on two sites with the same lead guide makes them look like one site: one shop chose Grenze Gotisch, saw the last mockup had used it, and swapped to New Rocker.
- **A site with two looks** picks lettering for each look, two faces each, and counts each look on its own (one game-style site set its second look in Cinzel over Spectral).

## Base

Code every pick needs, whatever the faces: the reading face on the page, headings in the display face at the scale's sizes, the measure, labels, and drawn marks hidden until the marks layer shows them. Each option's own code (below) sets `--font-body`, `--font-display` and the sizes, and loads only its own face, so a site copies only the files it uses.

```css assemble
& { --measure: 62ch;
  --lettering-read-weight: calc(400 - 30 * var(--dark, 0)); }   /* thinner on a dark tone: the colour part sets --dark */
body { font-family: var(--font-body); font-weight: var(--lettering-read-weight); font-size: var(--text-m); line-height: 1.5; }
:is(p, li, blockquote, figcaption, .lead) { max-width: var(--measure); text-wrap: pretty; }
.lead { font-size: calc(var(--text-m) * 1.18); line-height: 1.45; }
:is(h1, h2, h3, h4) { font-family: var(--font-display); font-weight: 600; line-height: 1.1; text-wrap: balance; }
h1 { font-size: var(--text-xxl); line-height: 1.05; }   /* the one biggest thing on the first screen */
h2 { font-size: var(--text-xl); }
h3 { font-size: var(--text-l); line-height: 1.2; }
h4 { font-size: var(--text-m); }
:is(.btn, button, input, select, textarea, .field, label) { font-family: var(--font-body); }   /* never the display face */
:is(input, select, textarea, .field) { font-size: max(1rem, var(--text-m, 1rem)); }   /* never under 16px: a phone zooms into a smaller field */
.btn { font-size: var(--text-m); font-weight: 700; line-height: 1.2; }
:is(.label, .tag, .badge) { font: 700 var(--text-s)/1.3 var(--font-body); }
small { font-size: var(--text-s); }
.lettering-fig { font: 600 var(--text-l)/1 var(--font-display); }   /* the figures that matter: <b class="lettering-fig">£2</b> */
:is(.lettering-ring, .lettering-wave) { position: relative; display: inline-block; }
:is(.lettering-ring, .lettering-wave) > svg, .lettering-stamp, .lettering-hand { display: none; }   /* shown by the marks layer */
```

## Layers

### Body
- Layer: body
- Owns: the reading face: everything read at length, and the small things that must be read exactly: fields, buttons, labels, prices beside them. It sets `--font-body`; Base thins it on a dark page.
- Default: humanist-sans

#### Humanist sans
- Id: humanist-sans
- Status: draft
- Looks like: a sans drawn from the pen: open letters with a little difference between thick and thin, calm at any size. The widest-used choice for a reading face.
- Made with: Source Sans 3 (variable, 200 to 900) in the swatch book and on two mockups (a tutor, an observatory). Of the same kind: Signika (on a game-style site; it also has a grade axis for dark pages), Alegreya Sans (another game-style site).

```css assemble
@font-face { font-family: 'Source Sans 3'; src: url('fonts/source-sans-3-latin-wght-normal.woff2') format('woff2'); font-weight: 200 900; font-display: swap; }
& { --font-body: 'Source Sans 3', 'Segoe UI', system-ui, sans-serif; }
```

- Careful: Source Sans 3 has a Reserved Font Name ('Source'): use the file as downloaded, never cut down. Its latin file has no real small capitals, so it cannot do `voice: tracked-capitals` with small capitals; that option uses true capitals.
- Light and dark: on a dark page the weight drops to 370 (`--lettering-read-weight`).
- Personality: serious, calm
- Goes with: `lettering: display book-serif` (the sober pair); `lettering: display chiselled` (Signika on the game-style site).
- Used on: 3 mockups: a private tutor's site, an observatory, a game-style joke site.

#### Grotesque
- Id: grotesque
- Status: draft
- Looks like: a plain sans with a few quirks: flat ends, a narrow `a`, a little stiffness. Reads as made by a person who chose it.
- Made with: Karla (variable, 200 to 800) in the swatch book and on a soap shop. Hanken Grotesk on the quiet gallery.

```css assemble
@font-face { font-family: 'Karla'; src: url('fonts/karla-latin-wght-normal.woff2') format('woff2'); font-weight: 200 800; font-display: swap; }
& { --font-body: 'Karla', 'Helvetica Neue', Arial, sans-serif; }
```

- Careful: next to a heading face that is also a grotesque, two faces with "similar flesh" but different bones look like a mistake (R8). Pair it with a serif.
- Light and dark: on a dark page the weight drops to 370.
- Personality: friendly, calm
- Goes with: `lettering: display soft-serif` (the soap shop, the quiet gallery); `lettering: display condensed-gothic`.
- Used on: 2 mockups: a one-person soap shop, a quiet gallery of pots.

#### Geometric sans
- Id: geometric-sans
- Status: draft
- Looks like: round and even, built from circles and straight lines; modern and clean.
- Made with: Figtree (variable, 300 to 900), on a 3D game in the browser and the first volunteer page.

```css assemble
@font-face { font-family: 'Figtree'; src: url('fonts/figtree-latin-wght-normal.woff2') format('woff2'); font-weight: 300 900; font-display: swap; }
& { --font-body: 'Figtree', 'Segoe UI', system-ui, sans-serif; }
```

- Careful: on its own, under a heading in the same face, it is the template's look; it needs a display face with character.
- Light and dark: on a dark page the weight drops to 370.
- Personality: friendly, playful
- Goes with: `lettering: display quirky-grotesque` (the lively grotesque pair).
- Used on: 2 mockups: a 3D game, the first version of a volunteer page.

#### Book serif
- Id: book-serif
- Status: draft
- Looks like: a serif for reading at length with a calligraphic hand in it and thick strokes. On a dark page it reads like a page of an old book.
- Made with: Alegreya (variable, 400 to 900) in the swatch book and on three mockups. Of the same kind: Vollkorn, Literata (the poetry site), Spectral. Choose strong, even strokes: thin hairlines vanish on a dark ground.

```css assemble
@font-face { font-family: 'Alegreya'; src: url('fonts/alegreya-latin-wght-normal.woff2') format('woff2'); font-weight: 400 900; font-display: swap; }
& { --font-body: 'Alegreya', Georgia, serif; }
```

- Careful: a serif reading face under a serif heading face is two serifs: "aren't so similar as to be indistinguishable" (R7), so the heading must be clearly another kind (a blackletter, a soft display serif), or the same face (`display: one-family`).
- Light and dark: on a dark page the weight drops to 370; Alegreya's lowest weight is 400, so it stays at 400 and the page relies on its own colour (a cream, not white, ink).
- Personality: calm, dramatic
- Goes with: `lettering: display bladed` (every dark painterly mockup); `lettering: display one-family` (artistic).
- Used on: 5 mockups: a dark painterly joke site (Vollkorn), two versions of a shop (Alegreya), a poetry site (Literata), the second look of a game-style site (Spectral).

#### Hyperlegible
- Id: hyperlegible
- Status: draft
- Looks like: a plain sans drawn so that no two letters can be mistaken: `I`, `l` and `1` all differ, `0` and `O` differ, wide open shapes.
- Made with: Atkinson Hyperlegible Next (variable, 200 to 800), made by the Braille Institute with Applied Design Works (R36: "For low-vision readers, certain letters and numbers can be hard to distinguish from one another"); added to Google Fonts in January 2025.

```css assemble
@font-face { font-family: 'Atkinson Hyperlegible Next'; src: url('fonts/atkinson-hyperlegible-next-latin-wght-normal.woff2') format('woff2'); font-weight: 200 800; font-display: swap; }
& { --font-body: 'Atkinson Hyperlegible Next', Verdana, sans-serif; }
```

- Careful: it is for low vision; it is not a dyslexia font, and no face is. Fonts made for dyslexia did not help readers in a controlled study (R38: "no improvement in reading rate or accuracy"). What helps is ordinary: 16 to 19px text, line height 1.5, lines of 60 to 70 characters, no italics or capitals for running text, bold for emphasis (R37, R39). This part meets all of those in every option.
- Light and dark: on a dark page the weight drops to 370.
- Personality: friendly, serious
- Goes with: `lettering: display fat-poster` (three mockups); `lettering: display book-serif` (the field journal set Alegreya headings over it).
- Used on: 4 mockups: a volunteer sign-up page, a night market, a repair café, a field notebook.

### Display
- Layer: display
- Owns: the heading face and what is done to it: weight, tightness, blocks behind it, an edge or a carved shadow. It sets `--font-display`. Used for the name, headings, the repeated item's name and the figures that matter (prices, dates, counts); never for buttons, fields or anything read at length.
- Default: book-serif

#### One family
- Id: one-family
- Status: draft
- Looks like: no second face. The reading face, heavy (700 to 800) and set tight, does the headings, and size does the rest.
- Made with: the body face's own weights.

```css assemble
& { --font-display: var(--font-body); }
h1 { font-weight: 750; letter-spacing: -0.02em; line-height: 1.02; }
:is(h2, h3, .lettering-fig) { font-weight: 700; }
```

- Careful: this is the template tell ("Headings are the reading face made bigger and bolder") unless the face has character and the scale is pushed: the artistic guide found one distinctive family on 5 of 7 studied sites, at three to five times body size. With a plain face it is right only for civic pages, where trust beats character, and those need their signature from somewhere else.
- Light and dark: the same on both.
- Personality: serious, dramatic
- Goes with: `lettering: body book-serif` and `lettering: scale dramatic` (artistic); `lettering: body hyperlegible` and `lettering: scale gentle` (civic).
- Used on: none yet as a pick: the artistic guide's study (5 of 7 sites), and GOV.UK's one family (R14).

#### Book serif
- Id: book-serif
- Status: draft
- Looks like: a readable serif for headings, figures and quoted words, over a sans. Nothing is done to the letters; size, weight and rules do the work.
- Made with: Newsreader at 600 (variable, 200 to 800). It also sets the numbers that matter and quotations, so it appears in more places than the headings. Of the same kind: Alegreya at 700 to 800 (the field notebook), Source Serif 4.

```css assemble
@font-face { font-family: 'Newsreader'; src: url('fonts/newsreader-latin-wght-normal.woff2') format('woff2'); font-weight: 200 800; font-display: swap; }
& { --font-display: 'Newsreader', Georgia, serif; }
h1 { font-weight: 600; letter-spacing: -0.01em; line-height: 1.04; }
```

- Careful: Newsreader also has an optical-size axis (6 to 72), but only in Fontsource's larger file (132 KB against 58 KB); the swatch book uses the smaller, which is right for headings. The earlier version of one page used a grotesque for headings and a code face for labels, and the labels were what made it read as software: no typewriter or code face for labels on a site about people.
- Light and dark: the same on both.
- Personality: serious, calm
- Goes with: `lettering: body humanist-sans` (the sober pair: "When in doubt [...] pair a serif and a sans serif", R7); `lettering: body hyperlegible`.
- Used on: 3 mockups: a private tutor's site (the owner: "way better, cleaner for sure"), an observatory, a field notebook (Alegreya).

#### Soft serif
- Id: soft-serif
- Status: draft
- Looks like: a soft, round, slightly old-fashioned serif with character, set large for headings and names. Friendly and careful at once.
- Made with: Fraunces with its soft axis full on. Fraunces has four axes (R34): `opsz` 9 to 144, `wght` 100 to 900, `SOFT` 0 to 100 ("the softer, rounded forms") and `WONK` 0 to 1 (leaning letters, switched on by itself above optical size 18). **SOFT is what makes it soft**, and it is only in Fontsource's `latin-full` file (121 KB); the usual `latin-wght` file (37 KB) has weight alone, and the letters come out sharp. Set the registered axes with their own properties (`font-weight`, `font-optical-sizing`) and only the custom ones with `font-variation-settings` (R19: it "will always override" the others). Of the same kind, one weight only: Young Serif (a soap shop), Caprasimo's quieter cousins.

```css assemble
@font-face { font-family: 'Fraunces'; src: url('fonts/fraunces-latin-full-normal.woff2') format('woff2'); font-weight: 100 900; font-display: swap; }   /* the full file: SOFT is only in it */
& { --font-display: 'Fraunces', Georgia, serif; }
:is(h1, h2, h3, .lettering-fig) {
  font-optical-sizing: auto;                          /* opsz follows the size: finer when large (R20) */
  font-variation-settings: 'SOFT' 100, 'WONK' 0; }    /* custom axes only: upper case, exactly as the font names them */
h1 { font-weight: 420; letter-spacing: -0.015em; line-height: 1.02; }
:is(h2, h3, .lettering-fig) { font-weight: 500; }
```

- Careful: if `font-variation-settings` sets `'opsz'` or `'wght'` as well, the heading stops following `font-size` and `font-weight`; set only SOFT and WONK there. If only headings use it, a site can pin `opsz` and drop WONK with fontTools' instancer and keep SOFT: the file falls from 121 to 62 KB (`varLib.instancer ... WONK=0 opsz=144 wght=300:700`). The swatch book keeps the full file and tests that SOFT and opsz really change the letters. A one-weight face (Young Serif) must never be asked for bold: the browser fakes it and the letters smear (`font-synthesis: none` stops it).
- Light and dark: the same on both.
- Personality: friendly, calm
- Goes with: `lettering: body grotesque`; `lettering: marks pencil`; `lettering: voice italic-accents` (the italic is a separate file).
- Used on: 3 mockups: a one-person soap shop (Young Serif), a poetry site (Fraunces at 500, sharp: it had the weight-only file), a quiet gallery of pots (Fraunces at 340, SOFT 100, opsz 144, which its maker noted were what make it soft).

#### Quirky grotesque
- Id: quirky-grotesque
- Status: draft
- Looks like: a heavy sans with quirks (ink traps, uneven widths), set tight, for headings and the name.
- Made with: Bricolage Grotesque (variable, 200 to 800) at 700 to 800, letter spacing -0.02 to -0.035em on large sizes. Its full file also has width and optical-size axes (`wdth` 75 to 100, `opsz` 12 to 96, R35) at 132 KB against 41 KB.

```css assemble
@font-face { font-family: 'Bricolage Grotesque'; src: url('fonts/bricolage-grotesque-latin-wght-normal.woff2') format('woff2'); font-weight: 200 800; font-display: swap; }
& { --font-display: 'Bricolage Grotesque', 'Trebuchet MS', sans-serif; }
h1 { font-weight: 800; letter-spacing: -0.035em; line-height: 0.98; }
:is(h2, h3, .lettering-fig) { font-weight: 700; letter-spacing: -0.01em; }
```

- Careful: the quietest option with character, and on its own it did not save a page: the first volunteer page used exactly this pair and was called "very plain ... like I made it with a cheap make-your-own-website tool". It is a face, not a signature.
- Light and dark: the same on both.
- Personality: playful, friendly
- Goes with: `lettering: body geometric-sans`; `lettering: voice tracked-capitals`.
- Used on: 2 mockups: a 3D game, the first version of a volunteer page (the one called plain).

#### Fat poster
- Id: fat-poster
- Status: draft
- Looks like: a fat, soft display face set huge, in pale letters on blocks of cut paper turned a degree or two, like a poster in a community hall.
- Made with: Caprasimo (one weight; it "is based on Fraunces", R35) or Bowlby One (the repair café). The biggest words sit on blocks drawn behind them in the band colours (`::before`, clipped to an uneven outline); only the block is turned, so the letters stay sharp. Each block's shadow follows the light.

- Needs markup: none needed (the biggest heading is one block); to give each word or line its own block, `<h1><span class="lettering-word">Night</span> <span class="lettering-word">market</span></h1>`.

```css assemble
@font-face { font-family: 'Caprasimo'; src: url('fonts/caprasimo-latin-400-normal.woff2') format('woff2'); font-weight: 400; font-display: swap; }
& { --font-display: 'Caprasimo', Georgia, serif; --lettering-cut: polygon(0.6% 2%, 99.4% 0, 100% 97%, 0 100%); }
:is(h1, h2, h3, .lettering-fig) { font-weight: 400; font-synthesis: none; }
h1 { font-size: min(var(--text-xxl), 17cqi); line-height: 1; }   /* every block fits its width: the density part makes the box holding an h1 a container, so cqi is that box */
/* each word or line of the biggest heading on its own turned block: <h1><span class="lettering-word">Night</span> <span class="lettering-word">market</span></h1>;
   a heading with no words marked is one block */
:is(h1 .lettering-word, h1:not(:has(.lettering-word))) { position: relative; isolation: isolate; display: block; width: fit-content;
  padding: 0.04em 0.2em 0.12em; color: var(--on-band); rotate: -2deg; }
:is(h1 .lettering-word, h1:not(:has(.lettering-word)))::before { content: ""; position: absolute; inset: 0; z-index: -1; background: var(--band-1);
  clip-path: var(--lettering-cut);
  filter: var(--drop-low, drop-shadow(calc(var(--lx, 0) * 2px) calc(var(--ly, 1) * 3px) 0 color-mix(in oklab, var(--shade, rgb(var(--shadow-rgb) / 0.6)) 35%, transparent))); }   /* the light part's low shadow */
h1 .lettering-word + .lettering-word { margin: -0.06em 0 0 0.5em; rotate: 1.5deg; }
h1 .lettering-word + .lettering-word::before { background: var(--band-2, var(--band-1)); }
```

- Careful: every block must fit its width: cap the size by the box it is in (`min(var(--text-xxl), 17cqi)` inside a container, or `17vw` on the page), and try the longest word at 320 pixels. The turn is a few degrees and never on reading text or fields. `check` reads the block's colour when it measures contrast.
- Light and dark: **it works on a dark page.** The blocks are the band colours, which the colour part keeps deep and dull on a dark tone, with `--on-band` letters; loud comes from size, not brightness, so poster letters sit under one lamp without becoming the brightest thing (the night market: "Night" on a forest block, "Market" on a tan canvas one, duller than the lantern).
- Personality: playful, friendly
- Goes with: `lettering: body hyperlegible`; `lettering: scale dramatic`; `lettering: marks pencil` or `stamp`; the light part's one light, with dull blocks.
- Used on: 3 mockups: a volunteer sign-up page (the owner: "looks great now, very styled, I love it"), a night market, a repair café (Bowlby One).

#### Condensed gothic
- Id: condensed-gothic
- Status: draft
- Looks like: tall, narrow capitals set very large and tight, like wood type on a theatre bill or a market poster: a lot of word in a little width.
- Made with: League Gothic (variable width, 75 to 100), "a revival of an old classic: Alternate Gothic", drawn by Morris Fuller Benton in 1903 (R52): the narrow poster gothic of the years when bills were set in wood and metal. Capitals, spaced a little (0.015em), line height under 0.9; one word may take `--mark`. Of the same kind: Bebas Neue, Big Shoulders Display, Anton.

- Needs markup: none needed; to set one word of the biggest heading in the mark colour, `<h1><span class="lettering-word">Night</span> <span class="lettering-word">market</span></h1>`.

```css assemble
@font-face { font-family: 'League Gothic'; src: url('fonts/league-gothic-latin-wdth-normal.woff2') format('woff2'); font-weight: 400; font-stretch: 75% 100%; font-display: swap; }
& { --font-display: 'League Gothic', 'Arial Narrow', Impact, sans-serif; }
:is(h1, h2, h3, .lettering-fig) { font-weight: 400; font-synthesis: none; text-transform: uppercase; letter-spacing: 0.015em; }
h1 { font-size: min(var(--text-xxl) * 1.3, 30cqi); line-height: 0.88; }   /* narrow letters can go bigger; cqi is the box holding the h1 (density makes it a container) */
h2 { font-size: calc(var(--text-xl) * 1.2); letter-spacing: 0.03em; }
:is(h3, .lettering-fig) { font-size: calc(var(--text-l) * 1.2); letter-spacing: 0.03em; }
h1 .lettering-word + .lettering-word { color: var(--mark); }   /* one word in the mark colour: <span class="lettering-word"> */
```

- Careful: no mockup has used it yet; it comes from the warm guide's study (826 Valencia's condensed gothic capitals) and from the wood-type tradition (R43, R44: theatre bills needed letters for "a long-winded name"). Capitals only for a few words (R41: all caps for longer passages "is not recommended"). Its partner is judgement: a grotesque or the hyperlegible face, never another narrow face.
- Light and dark: the same on both; a word in `--mark` must reach 3 to 1 at its size.
- Personality: dramatic, playful
- Goes with: `lettering: body grotesque` or `hyperlegible`; `lettering: scale dramatic`.
- Used on: none yet (the warm guide's study, 1 of 12 sites).

#### Bladed
- Id: bladed
- Status: draft
- Looks like: a blackletter or pointed, cut face with blades in it, like a heavy-metal record sleeve or a painted stall sign, for the name and section titles only, over a sturdy book face. On a dark page pale brass with a hard dark offset; on a light page dark ink with a coloured offset, like a two-colour print.
- Made with: Pirata One ("a gothic textura font, simplified and optimized to work well on screen", R35) in the swatch book and on a shop; Grenze Gotisch at 600 (a dark painterly joke site); New Rocker (another shop). The offset falls with the light.

```css assemble
@font-face { font-family: 'Pirata One'; src: url('fonts/pirata-one-latin-400-normal.woff2') format('woff2'); font-weight: 400; font-display: swap; }
& { --font-display: 'Pirata One', 'Palatino Linotype', serif; }
:is(h1, .lettering-name) { font-family: var(--font-display); font-weight: 400; font-synthesis: none; line-height: 0.98; letter-spacing: 0.01em;
  color: light-dark(var(--on-ground), var(--metal, var(--mark)));
  text-shadow: calc(var(--lx, 0) * 3px) calc(var(--ly, 1) * 3px) 0 light-dark(color-mix(in oklab, var(--metal-deep, var(--mark)) 55%, transparent), var(--shade, rgb(var(--shadow-rgb) / 0.6))); }
:is(h2, h3, .lettering-fig) { font-family: var(--font-body); font-weight: 700; }   /* blades for the name only: everything else is read */
```

- Careful: only ever a few words, at heading sizes. Readers unused to blackletter misread some of its letters (R48: a designer redrew "ten letters that are typically misread"), and the sorcery guide warns it is "impossible for some readers at any size". So never for buttons, prices, fields, subheadings or anything read; give the name real text underneath for screen readers if the letters are drawn. Section titles in it ran to seven words on one site, and that site's own guide listed it as a problem. Pirata One has a Reserved Font Name: use the file as downloaded.
- Light and dark: on a dark page metal (`--metal`, falling back to `--mark`) with a `--shade` offset; on a light page `--on-ground` with an offset in the deep metal.
- Personality: dramatic
- Goes with: `lettering: body book-serif`; `lettering: scale dramatic`.
- Used on: 4 mockups: a dark painterly joke site (Grenze Gotisch), two versions of a shop (New Rocker, Pirata One), and one side of a game-style site.

#### Chiselled
- Id: chiselled
- Status: draft
- Looks like: flared, carved capitals in metal with a dark edge all round and a drop below, like the title of a game or letters cut in stone.
- Made with: Cinzel Decorative at 700 (Cinzel is "inspired in first century roman inscriptions", R35), Marcellus, Cinzel, Metamorphous on four looks of game-style sites. The metal is the colour part's `--metal` (gold by default, with `--metal-lit` for the top line and `--metal-deep` for the depth), falling back to `--mark`; the edge is drawn four ways; the depth and the drop follow the light.

```css assemble
@font-face { font-family: 'Cinzel Decorative'; src: url('fonts/cinzel-decorative-latin-700-normal.woff2') format('woff2'); font-weight: 700; font-display: swap; }
& { --font-display: 'Cinzel Decorative', 'Trajan Pro', Georgia, serif; --lettering-chisel-edge: light-dark(var(--ink), var(--shade, rgb(var(--shadow-rgb) / 0.6))); }
:is(h1, h2, h3, .lettering-fig) { font-weight: 700; font-synthesis: none; font-variant-ligatures: no-common-ligatures; }   /* its OO and TH ligatures misread */
h1 { font-size: min(var(--text-xxl) * 0.82, 13cqi); padding-left: 0.22em; line-height: 1.02; letter-spacing: 0.02em;
  color: light-dark(color-mix(in oklab, var(--metal, var(--mark)) 45%, var(--metal-deep, var(--ink))), var(--metal, var(--mark)));   /* old gold on a light page */
  text-shadow: 0 -1px 0 var(--metal-lit, light-dark(var(--surface-raised), var(--ink))),
    1px 1px 0 var(--lettering-chisel-edge), -1px 1px 0 var(--lettering-chisel-edge), 1px -1px 0 var(--lettering-chisel-edge), -1px -1px 0 var(--lettering-chisel-edge),
    calc(var(--lx, 0) * 3px) calc(var(--ly, 1) * 3px) 0 var(--metal-deep, color-mix(in oklab, var(--mark) 45%, var(--shade, rgb(var(--shadow-rgb) / 0.6)))),
    calc(var(--lx, 0) * 6px) calc(var(--ly, 1) * 8px) 12px color-mix(in oklab, var(--shade, rgb(var(--shadow-rgb) / 0.6)) 55%, transparent); }
```

- Careful: the edge drawn all round is what lets metal read over a painted sky; without it the contrast depends on what is behind, so run `check` over the busiest part of the ground. Cinzel and Cinzel Decorative have capitals only: names and short titles, never sentences. Their OO and TH ligatures misread in a heading; switch them off. Never use a real game's own lettering or font files: pick a free face of the same kind and say so in the site's guide. Short button labels in it are fine; anything longer goes in the reading face. Cinzel has a Reserved Font Name: use the file as downloaded. Until the colour part sets `--metal`, the fallback `--mark` gives bronze on a light page and brass on a dark one.
- Light and dark: on a dark page bright gold with a dark edge and a pale top line; on a light page old gold (the metal mixed towards `--metal-deep`), because bright gold is only 2.4 to 1 on a cream page and large text needs 3 to 1 without counting the edge.
- Personality: dramatic, playful
- Goes with: `lettering: body humanist-sans` (Signika, Alegreya Sans); `lettering: voice tracked-capitals`; `lettering: scale dramatic`.
- Used on: 4 looks on 3 mockups: three versions of a game-style joke site and the second look of one.

### Scale
- Layer: scale
- Owns: the type sizes: five steps, each fluid from a phone to a wide window. It sets `--text-s` to `--text-xxl`.
- Default: classic

All three are modular scales (R12: "a prearranged set of harmonious proportions") made fluid the way Utopia does it (R11): one ratio at 320 pixels and a larger one at 1240, joined with `clamp()`. All three start at a ratio of 1.2 on a phone (Utopia's default), and open out on a wide window. Reading text is 17 to 19px on all three (the general guide's body size; the BDA asks for 16 to 19, R37). Every middle value has a `rem` part, so the reader's own text size still counts. The swatch book's builder works them out and prints them.

| Step | Use | Gentle (1.2 to 1.25) | Classic (1.2 to 1.333) | Dramatic (1.2 to 1.414) |
|---|---|---|---|---|
| `--text-s` | labels, captions | 14px | 14px | 14px |
| `--text-m` | reading text | 17 to 19px | 17 to 19px | 17 to 19px |
| `--text-l` | subheadings, figures | 24 to 30px | 24 to 34px | 24 to 38px |
| `--text-xl` | section headings | 29 to 37px (1.9 times) | 29 to 45px (2.4 times) | 29 to 54px (2.8 times) |
| `--text-xxl` | the one biggest thing | 42 to 58px (3.05 times) | 42 to 80px (4.2 times) | 51 to 152px (8 times) |

#### Gentle
- Id: gentle
- Status: draft
- Looks like: headings only a little bigger than the text; the biggest words just reach three times body. Quiet and even.
- Made with: ratio 1.2 on a phone, 1.25 on a wide window; the top step is the fifth.

```css assemble
& { --text-s: 0.875rem; --text-m: clamp(1.0625rem, 1.019rem + 0.217vw, 1.1875rem);
  --text-l: clamp(1.5312rem, 1.4182rem + 0.565vw, 1.8562rem); --text-xl: clamp(1.8375rem, 1.6701rem + 0.837vw, 2.3188rem);
  --text-xxl: clamp(2.6437rem, 2.3024rem + 1.707vw, 3.625rem); }
```

- Careful: it sits on the template line: 3.05 times at 1240 pixels, under three in any narrower window. With a plain face and nothing designed beside it, it is the template; it needs a signature from another part.
- Light and dark: the same on both.
- Personality: serious, calm
- Goes with: `lettering: display book-serif` (professional); `lettering: display one-family` (civic).
- Used on: the professional guide's study (50 to 65px against 16 to 20px); GOV.UK's heading XL is 48 against 19 (R14).

#### Classic
- Id: classic
- Status: draft
- Looks like: a clear ladder of sizes with one big heading: the proportion of a good book's title page.
- Made with: ratio 1.2 on a phone, 1.333 (a fourth) on a wide window; the top step is the fifth. Utopia's own blog post used 1.2 to 1.333 (R11).

```css assemble
& { --text-s: 0.875rem; --text-m: clamp(1.0625rem, 1.019rem + 0.217vw, 1.1875rem);
  --text-l: clamp(1.5312rem, 1.3291rem + 1.011vw, 2.1125rem); --text-xl: clamp(1.8375rem, 1.4984rem + 1.696vw, 2.8125rem);
  --text-xxl: clamp(2.6437rem, 1.8242rem + 4.098vw, 5rem); }
```

- Careful: the top step is 80px on a wide window: one thing only. The observatory let its name reach 3.6 times and kept other headings under three, which is this scale.
- Light and dark: the same on both.
- Personality: any
- Goes with: any display face.
- Used on: 5 mockups at about this proportion: a tutor (68px against 19), a soap shop (68 against 19), an observatory, a quiet gallery (72 against 19), a field notebook (64 against 19).

#### Dramatic
- Id: dramatic
- Status: draft
- Looks like: the biggest words fill the first screen: a poster or a title page. Section headings stay under three times so the rest of the page can be read.
- Made with: ratio 1.2 on a phone, 1.414 on a wide window; the top step is the sixth, so the biggest words reach eight times body.

```css assemble
& { --text-s: 0.875rem; --text-m: clamp(1.0625rem, 1.019rem + 0.217vw, 1.1875rem);
  --text-l: clamp(1.5312rem, 1.2378rem + 1.467vw, 2.375rem); --text-xl: clamp(1.8375rem, 1.3092rem + 2.641vw, 3.3563rem);
  --text-xxl: clamp(3.175rem, 0.9772rem + 10.989vw, 9.4938rem); }
```

- Careful: at 152px a long word does not fit: cap it by its box (`min(var(--text-xxl), 17cqi)`, and carved capitals `13cqi`) and try the longest word at 320 pixels. Two big things on one screen fight (the general guide: "at most two large elements").
- Light and dark: the same on both.
- Personality: dramatic, playful
- Goes with: `lettering: display fat-poster`, `condensed-gothic`, `bladed`, `chiselled`; `lettering: display one-family` (artistic).
- Used on: 4 mockups: a volunteer page (seven times), a night market (`--text-poster`, 58 to 144px), a repair café, a dark painterly joke site (88px). The warm guide's study saw 86 to 152px on 5 of 12 sites.

### Voice
- Layer: voice
- Owns: case and letter-spacing on labels and headings, and where italic is used.
- Default: sentence-case

#### Sentence case
- Id: sentence-case
- Status: draft
- Looks like: headings, labels and buttons written as sentences: "See the stalls", not "See The Stalls" or "SEE THE STALLS". Labels are told apart by weight, not case.
- Made with: no transform; labels in the reading face at 700, `--text-s`.

```css assemble
/* voice: sentence case. Nothing to add: labels in the reading face at 700 are in Base, and nothing is transformed. */
```

- Careful: GOV.UK asks for it on every heading and button (R15), and the BDA advises against capitals for continuous text (R37). Title Case Is For Book Titles.
- Light and dark: the same on both.
- Personality: any
- Goes with: everything.
- Used on: most mockups.

#### Tracked capitals
- Id: tracked-capitals
- Status: draft
- Looks like: short labels and navigation in capitals, spaced a tenth of an em apart, like the small print on a ticket.
- Made with: `text-transform: uppercase` and `letter-spacing: 0.1em` on labels under a line long (R4: "5–12% extra space with caps"; R9: more at small sizes). The reading face at 700.

```css assemble
:is(.label, .tag, .badge) { text-transform: uppercase; letter-spacing: 0.1em; }
nav a { text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700; }
```

- Careful: never for anything longer than a line, or for headings over a few words (R41). Not small capitals: none of the faces here has real ones in its latin file (no `smcp` feature), and the browser's fake ones "are too tall, and their vertical strokes are too light" (R5). Ask for `font-variant-caps: all-small-caps` only with a face that has them, and with `font-synthesis: none`. Keep labels at 14px or more; capitals do not make small text bigger.
- Light and dark: on a dark page tracked capitals glare a little less with the lighter weight; add 0.02em more spacing if they clot.
- Personality: serious, playful
- Goes with: `lettering: display chiselled`, `quirky-grotesque`, `fat-poster`.
- Used on: 5 mockups: a 3D game and the first volunteer page (labels, 0.08em), a night market (navigation, 0.08em), a repair café (tag labels, 0.1em), a quiet gallery (labels, 0.08em).

#### Capital headings
- Id: capital-headings
- Status: draft
- Looks like: short headings in capitals, spaced a little, like an inscription or a label on a drawer.
- Made with: `text-transform: uppercase; letter-spacing: 0.06em` on headings of a few words, set a fifth smaller, since capitals are big for their size.

```css assemble
:is(h1, h2) { text-transform: uppercase; letter-spacing: 0.06em; }
h1 { font-size: calc(var(--text-xxl) * 0.8); line-height: 1.04; }   /* capitals are big for their size */
```

- Careful: "DO NOT USE BLOCK CAPITALS FOR LARGE AMOUNTS OF TEXT" (R16). A screen reader may spell out a word typed in capitals; type the heading in sentence case and let CSS make the capitals. With a face that is all capitals already (Cinzel, League Gothic) this layer adds nothing.
- Light and dark: the same on both.
- Personality: serious, dramatic
- Goes with: `lettering: display book-serif` (an almanac or museum look); `lettering: display one-family`.
- Used on: none yet as a pick; the professional and education studies' engraved-looking headings.

#### Italic accents
- Id: italic-accents
- Status: draft
- Looks like: one phrase in a heading turned into the display face's real italic: "Glazes, *slowly*". A voice that leans in.
- Made with: `<em>` in the heading and the display face's italic file. In the swatch book, Fraunces italic, cut down to SOFT 100, opsz 144, weight 300 to 500 (40 KB from 150), since it is only ever a few soft, large words.

```css assemble
@font-face { font-family: 'Fraunces'; src: url('fonts/fraunces-latin-italic-soft100-opsz144.woff2') format('woff2'); font-weight: 300 500; font-style: italic; font-display: swap; }   /* the italic file, cut to SOFT 100, opsz 144 */
:is(h1, h2) em { font-style: italic; font-weight: 340; font-synthesis: none; }
```

- Careful: the italic is a separate file; without it the browser slants the upright letters and calls it italic. `font-synthesis: none` (R21) keeps the upright letters instead, which is the honest failure. One phrase per heading, never running text (R37, R39: italics slow readers with dyslexia).
- Light and dark: the same on both.
- Personality: calm, friendly
- Goes with: `lettering: display soft-serif`, `book-serif`.
- Used on: 2 mockups: a quiet gallery (the second half of its heading in italic Fraunces), a poetry site (Fraunces italic).

### Marks
- Layer: marks
- Owns: what is drawn on words: a ring round a word, a wavy line under a phrase, a highlighter, a rubber stamp, a few handwritten words. Drawn in `--mark`, hidden from screen readers, and never on fields.
- Default: none

The marks are their own layer so that any faces can carry them: the old "hand marks" option had no faces of its own, and the field notebook's maker had to choose some. They are drawn as small inline SVGs or CSS, not typed in a handwriting face (the warm guide: "hand-made marks are drawn, not typed in a third, handwriting face"). Shared SVG shapes sit once in the page as `<symbol>`s and are drawn with `<use>`.

#### None
- Id: none
- Status: draft
- Looks like: typed words only.
- Made with: nothing.

```css assemble
/* marks: none. Typed words only; Base keeps any drawn marks hidden. */
```

- Careful: most serious and calm sites want none; their detail goes elsewhere.
- Light and dark: the same on both.
- Personality: serious, calm
- Goes with: everything.
- Used on: most mockups.

#### Pencil
- Id: pencil
- Status: draft
- Looks like: somebody went over the page with a pencil: a loose ring round one word in a heading, a wavy line under a phrase, a ringed step number, tally marks for a count.
- Made with: a ring and a wave drawn once as symbols and stretched over the word with `preserveAspectRatio="none"`, stroke 2.5 to 3 in `--mark`, round caps. Rough Notation (R49, MIT, 3.8 KB) draws and animates the same marks, but its docs say nothing about screen readers; plain SVG is enough.

- Needs markup: round the one word that matters, `<span class="lettering-ring">market<svg aria-hidden="true" focusable="false"><use href="#lettering-ring"/></svg></span>`, or under it `<span class="lettering-wave">one car park<svg aria-hidden="true" focusable="false"><use href="#lettering-wave"/></svg></span>`; the symbols come in `parts.js`.

```css assemble
.lettering-ring > svg { display: block; position: absolute; inset: -0.16em -0.2em -0.1em; width: calc(100% + 0.4em); height: calc(100% + 0.26em);
  color: var(--mark); fill: none; stroke: currentColor; stroke-width: 2.5; stroke-linecap: round; overflow: visible; pointer-events: none; }
h1 .lettering-ring { margin-left: 0.12em; }
.lettering-wave { padding-bottom: 0.1em; }
.lettering-wave > svg { display: block; position: absolute; left: 0; bottom: -0.12em; width: 100%; height: 0.28em;
  color: var(--mark); fill: none; stroke: currentColor; stroke-width: 3; stroke-linecap: round; overflow: visible; pointer-events: none; }
```
```html
<span class="lettering-ring">market<svg aria-hidden="true" focusable="false"><use href="#lettering-ring"/></svg></span>
<span class="lettering-wave">one car park<svg aria-hidden="true" focusable="false"><use href="#lettering-wave"/></svg></span>
```
```html assemble
<symbol id="lettering-ring" viewBox="0 0 100 50" preserveAspectRatio="none"><path d="M58 3C25 1 3 12 4 26c1 15 31 21 56 19 23-2 38-11 36-23C94 9 70 2 42 6"/></symbol>
<symbol id="lettering-wave" viewBox="0 0 300 12" preserveAspectRatio="none"><path d="M3 7c20-7 30 5 50 0s30-7 50-1 30 5 50 0 30-6 50-1 30 4 46 0 30-5 46-1"/></symbol>
```

- Careful: a wavy line under words in running text looks like a link ("Underline means link and nothing else", the general guide; R6). Draw it under a heading's phrase, not in a paragraph. One or two rings on a page, not on every heading. The drawing is `aria-hidden`; what it points at must be clear without it.
- Light and dark: `--mark` is a pencil brown on a light page and a pale brass on a dark one; the strokes are thick enough to show on both.
- Personality: friendly, playful
- Goes with: `lettering: display soft-serif` (the hand-marks start); `lettering: display fat-poster`; `lettering: display book-serif` with `lettering: body hyperlegible` (the field journal).
- Used on: 3 mockups: a volunteer page (a squiggle), a field notebook (wavy underlines, rings round two birds, ringed step numbers, tallies), a soap shop (pen lines).

#### Highlighter
- Id: highlighter
- Status: draft
- Looks like: one phrase in a paragraph gone over with a highlighter: a band behind the letters, a little uneven, as if by hand. On a dark page it glows: a light band with the letters turned dark on it.
- Made with: a tilted gradient behind the phrase and `box-decoration-break: clone` so every wrapped line gets its own ends (R27). On a light page the band is `--mark` at about a third and the letters stay `--ink`; on a dark page it is `--mark` lifted towards `--ink` (a light band) and the letters take `--ground`, so they keep 4.5 to 1 on it. `light-dark()` picks them from the page's colour scheme.

- Needs markup: `<span class="lettering-hl">most stalls take cards</span>` round the phrase that matters, in reading text.

```css assemble
.lettering-hl { padding: 0 0.15em; margin: 0 -0.15em; border-radius: 0.3em 0.15em 0.35em 0.2em;   /* the stroke's own uneven ends, not a corner */
  -webkit-box-decoration-break: clone; box-decoration-break: clone;
  --lettering-hl: light-dark(color-mix(in oklab, var(--mark) 34%, transparent), color-mix(in oklab, var(--mark) 72%, var(--ink)));
  color: light-dark(var(--ink), var(--ground));
  background: linear-gradient(178deg, transparent 0 3%, var(--lettering-hl) 5% 95%, transparent 97%); }
```
```html
Bring a bag; <span class="lettering-hl">most stalls take cards</span>, a few take only coins.
```

- Careful: one phrase per section at most; it is emphasis, and "if everything is contrasted, then nothing stands out". The text over it must still reach 4.5 to 1: keep the band pale on a light page, and on a dark page turn the letters dark rather than leave light letters on a light band. A tutor's site used a yellow one, kept for evidence only: the subject in the heading and the tutor's own method (`box-shadow: inset 0 -0.3em 0`, a straight band).
- Light and dark: a pale band under dark letters on a light page; a glowing band under dark letters on a dark page (a dull band under light letters, the first try, hardly showed).
- Personality: friendly, calm
- Goes with: `lettering: display book-serif`; `marks` alone on a professional page that wants one human touch.
- Used on: 1 mockup: a private tutor's site (a straight yellow band under the subject in the heading and under the tutor's method).

#### Stamp
- Id: stamp
- Status: draft
- Looks like: a rubber stamp on the edge of a sheet: a word in bold spaced capitals inside a double rule, tilted, in one ink: FULL, SOLD OUT, NEW.
- Made with: the reading face at 800 in capitals, `letter-spacing: 0.14em`, a `3px double` border, rotated 6 to 9 degrees, `--mark` on `--surface`.

- Needs markup: `<span class="lettering-stamp" aria-hidden="true">Full</span>` as a direct child of the sheet or panel it is stamped on, with the same news in words in the sheet.

```css assemble
:is(.sheet, .panel):has(> .lettering-stamp) { position: relative; }   /* the stamp sits on the sheet's edge */
.lettering-stamp { display: inline-block; position: absolute; right: 1rem; top: -0.9rem; padding: 0.1rem 0.5rem;
  border: 3px double var(--mark); border-radius: min(var(--radius-small, 3px), 3px);
  background: var(--surface); color: var(--mark); font: 800 1.125rem/1.3 var(--font-body); letter-spacing: 0.14em; text-transform: uppercase; rotate: 8deg; }
```
```html
<div class="sheet"><span class="lettering-stamp" aria-hidden="true">Full</span> ... <p>Saturday is full; Sunday still has room.</p></div>
```

- Careful: a stamp repeats a state; it never carries it alone. Write the state in words where a screen reader reads it ("Saturday is full; Sunday still has room") and hide the stamp (`aria-hidden="true"`). It is small text: 4.5 to 1 against its own ground. The rule round it is lettering's, since it belongs to the word; a frame round a sheet is the frames part's.
- Light and dark: the stamp keeps the sheet's colour behind it, so its ink reads on both.
- Personality: playful, friendly
- Goes with: `lettering: display fat-poster`; `lettering: marks pencil` (a layer may take two: `marks: pencil + stamp`, as the field journal does, and as a volunteer page did).
- Used on: 4 mockups: a volunteer page and a field notebook (FULL), two versions of a shop.

#### Handwriting
- Id: handwriting
- Status: draft
- Looks like: a few words in a handwriting face beside the typed ones, with a drawn arrow: a maker's note in the margin.
- Made with: Caveat at 600 (variable, 400 to 700), about 26px, in `--mark`, turned three degrees, with a hand-drawn arrow symbol.

- Needs markup: `<p class="lettering-hand"><svg aria-hidden="true" focusable="false"><use href="#lettering-arrow"/></svg>bring a torch!</p>` beside the thing it points at; the arrow comes in `parts.js`.

```css assemble
@font-face { font-family: 'Caveat'; src: url('fonts/caveat-latin-wght-normal.woff2') format('woff2'); font-weight: 400 700; font-display: swap; }
.lettering-hand { display: flex; align-items: flex-end; gap: 0.25rem; margin: 0.5rem 0 -0.25rem 0.5rem; width: fit-content;
  font: 600 1.625rem/1.1 'Caveat', 'Segoe Print', cursive; color: var(--mark); rotate: -3deg; }
.lettering-hand > svg { display: block; flex: none; width: 2.5rem; height: 1.75rem; color: var(--mark);
  fill: none; stroke: currentColor; stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }
```
```html
<p class="lettering-hand"><svg aria-hidden="true" focusable="false"><use href="#lettering-arrow"/></svg>bring a torch!</p>
```
```html assemble
<symbol id="lettering-arrow" viewBox="0 0 40 28"><path d="M37 4C26 3 13 8 8 22M8 22l-1-9M8 22l8-5"/></symbol>
```

- Careful: **this is a third typeface**, against the general guide's two; take it only when the site's own guide says the handwriting is the point (as one soap maker's did) and record it there. Never for anything read at length, labels on fields, or prices alone. It is real text (not hidden): it must reach 4.5 to 1, or 3 to 1 at 24px and over. Caveat's file is the largest here (75 KB) for a few words; it cannot be cut much (its handwriting comes from alternate letters).
- Light and dark: the same on both.
- Personality: friendly, playful
- Goes with: `lettering: display soft-serif`; a single maker's site.
- Used on: 1 mockup: a one-person soap shop (a note on each soap, price tags, the maker's note; agreed in that site's guide).

## Starting points

### Sober pair
- Id: sober-pair
- Picks: body: humanist-sans; display: book-serif; scale: classic; voice: sentence-case; marks: none
- Personality: serious, calm
- Looks like: a readable book serif for headings, figures and the owner's words, over a plain sans. Nothing is done to the letters.
- Used on: a private tutor's site and an observatory (Newsreader 600 over Source Sans 3).

### Professional
- Id: professional
- Picks: body: humanist-sans; display: book-serif; scale: gentle; voice: sentence-case; marks: none
- Personality: serious, calm
- Looks like: the sober pair, quieter: the biggest heading just three times body, every other heading well under. Even and exact.
- Used on: the professional guide ("One or two sober families; headings about three times body size at most"; 50 to 65px against 16 to 20px on the education sites studied).

### Civic
- Id: civic
- Picks: body: hyperlegible; display: one-family; scale: gentle; voice: sentence-case; marks: none
- Personality: serious, friendly
- Looks like: one plain face for everything, headings bold, sizes calm, every heading and button in sentence case: a council page anyone can read on a bus. It carries one template tell (headings in the reading face) on purpose; the page's signature comes from another part.
- Used on: GOV.UK's one family and sentence case (R14, R15), the BDA's style guide (R37); no mockup yet.

### Almanac plate
- Id: almanac-plate
- Picks: body: humanist-sans; display: book-serif; scale: classic; voice: tracked-capitals; marks: none
- Personality: calm, serious
- Looks like: a printed almanac: every figure that matters (times, dates, prices) in the book serif, small tracked labels over them, the name a little bigger than the rest.
- Used on: an observatory mockup (Newsreader for the name, headings and every time and date; the name at 3.6 times body).

### Soft serif
- Id: soft-serif
- Picks: body: grotesque; display: soft-serif; scale: classic; voice: sentence-case; marks: none
- Personality: friendly, calm
- Looks like: a soft, round serif for headings and names over a plain grotesque: friendly and careful at once.
- Used on: a one-person soap shop (Young Serif over Karla) and a poetry site (Fraunces over Literata).

### Catalogue of glazes
- Id: catalogue-of-glazes
- Picks: body: grotesque; display: soft-serif; scale: classic; voice: italic-accents; marks: none
- Personality: calm
- Looks like: the soft serif set light and slow, its soft axis full on, half the heading turned into italic, over a quiet grotesque. Spare and unhurried.
- Used on: a quiet gallery of pots (Fraunces at 340, SOFT 100, opsz 144, italic for the second half of the heading, over Hanken Grotesk).

### Hand marks
- Id: hand-marks
- Picks: body: grotesque; display: soft-serif; scale: classic; voice: sentence-case; marks: pencil
- Personality: friendly, playful
- Looks like: the soft serif with pencil on it: a ring round a word in the heading, a wavy line under a phrase. The old option of this name had no faces of its own; these are the ones its swatch always showed.
- Used on: a volunteer page (the squiggle), a soap shop, and a field notebook, whose maker asked for exactly this default.

### Field journal
- Id: field-journal
- Picks: body: hyperlegible; display: book-serif; scale: classic; voice: sentence-case; marks: pencil + stamp
- Personality: calm, friendly
- Looks like: a naturalist's notebook: plain, clear print for reading outdoors, bold serif headings, pencil rings, wavy lines and tallies in robin rust, and a FULL stamp on the walk that is full.
- Used on: a field-notebook mockup (Alegreya 700 and 800 over Atkinson Hyperlegible Next; wavy underlines, rings round two birds, ringed step numbers, tallies, a FULL stamp).

### Lively grotesque
- Id: lively-grotesque
- Picks: body: geometric-sans; display: quirky-grotesque; scale: classic; voice: tracked-capitals; marks: none
- Personality: playful, friendly
- Looks like: a heavy sans with quirks for headings and the name, over a round modern sans, with tracked capitals for labels. It is a face, not a signature.
- Used on: a 3D game and the first version of a volunteer page (Bricolage Grotesque over Figtree); the second was called plain.

### Artistic
- Id: artistic
- Picks: body: book-serif; display: one-family; scale: dramatic; voice: sentence-case; marks: none
- Personality: dramatic, calm
- Looks like: one family with character carrying the whole site, its heaviest weight pushed to many times the body size at the top of the first page.
- Used on: the artistic guide ("One family with character carrying the whole site", 5 of 7 sites; the largest text 3 to 5 times body on 4 of 7); no mockup yet.

### Poster face
- Id: poster-face
- Picks: body: hyperlegible; display: fat-poster; scale: dramatic; voice: sentence-case; marks: none
- Personality: playful, friendly
- Looks like: fat, soft letters set huge on cut-paper blocks turned a degree or two, over a face drawn to be easy to read: a poster in a community hall.
- Used on: a volunteer sign-up page (Caprasimo over Atkinson Hyperlegible Next; "looks great now, very styled, I love it").

### Warm
- Id: warm
- Picks: body: hyperlegible; display: fat-poster; scale: dramatic; voice: sentence-case; marks: pencil
- Personality: friendly, playful
- Looks like: the poster face with pencil marks on it: the headline far bigger than a template would make it, words someone would say, a ring round one of them.
- Used on: the warm guide (a display face chosen for the material, "four or more times the body size", hand-made marks drawn, not typed); a volunteer page and a repair café, both with warm leading.

### Lantern fair
- Id: lantern-fair
- Picks: body: hyperlegible; display: fat-poster; scale: dramatic; voice: tracked-capitals; marks: none
- Personality: playful, dramatic
- Looks like: poster letters on dull blocks under one lamp at night, tracked capitals in the navigation, a reading face that survives a phone in the dark.
- Used on: a night-market mockup ("Night" and "Market" on two turned blocks; every section heading on its own block; navigation in capitals at 0.08em).

### Repair cafe
- Id: repair-cafe
- Picks: body: hyperlegible; display: fat-poster; scale: dramatic; voice: tracked-capitals; marks: stamp
- Personality: playful, friendly
- Looks like: a cut-card slogan ("Toss it? No way!") on blocks, tag labels in spaced capitals, and a rubber stamp on the sheet that is full.
- Used on: a repair-café mockup (Bowlby One over Atkinson Hyperlegible Next; tag labels uppercase at 0.1em; a 5.5rem slogan).

### Bladed letters
- Id: bladed-letters
- Picks: body: book-serif; display: bladed; scale: classic; voice: sentence-case; marks: none
- Personality: dramatic
- Looks like: a blackletter name and section titles with a hard offset, over a sturdy book face: a painted stall sign or a record sleeve.
- Used on: two versions of a shop (New Rocker over Alegreya; Pirata One over Alegreya) and one side of a game-style site.

### Sorcery
- Id: sorcery
- Picks: body: book-serif; display: bladed; scale: dramatic; voice: sentence-case; marks: none
- Personality: dramatic
- Looks like: a blackletter name, huge, pale brass on a dark wall, over a book face for everything read: the title on an old book's cover.
- Used on: the sorcery guide ("Lettering with blades in it for names and titles only; a plain face for everything that is read"); a dark painterly joke site (Grenze Gotisch 600 over Vollkorn, up to 88px).

### Chiselled metal
- Id: chiselled-metal
- Picks: body: humanist-sans; display: chiselled; scale: classic; voice: tracked-capitals; marks: none
- Personality: dramatic, playful
- Looks like: flared, carved capitals in metal with an edge and a drop, over a friendly sans, like a game's title screen.
- Used on: three versions of a game-style joke site (Cinzel Decorative over Signika; Marcellus over Alegreya Sans).

### Gilded dark
- Id: gilded-dark
- Picks: body: humanist-sans; display: chiselled; scale: dramatic; voice: tracked-capitals; marks: none
- Personality: dramatic, playful
- Looks like: the chiselled title bigger, gold on dark panels, with white tracked labels: a game interface. Its gold is the colour part's `--metal`.
- Used on: the gilded dark (game-interface) guide ("names and headings in a flared or chiselled serif, in gold with a dark edge"; labels white); a game-style joke site in both its looks.

## Swatch book

`tests/parts/lettering.html` shows every option of every layer, then every starting point, each on a light page and on a dark one side by side; open it in a browser to choose by eye. Every swatch holds the same things: a label, a heading in the display face, a sheet with a subheading, a paragraph in the reading face, a figure and a button. An option is shown with the partners it is usually paired with (named in the line at the top of each swatch), not with faces it fights; the marks are all shown over the soft serif. The scale swatches show the five steps as a ladder with their sizes at 320 and 1240 pixels. It stands in for two values other parts hand over: the light part's direction (top left) and `--dark`, which the colour part does not set yet. Its test checks, beside every swatch being drawn on both pages: that all 14 faces load from `fonts/`, that Fraunces's SOFT and optical size, Newsreader's weight and League Gothic's width really change the letters (and that the pinned italic does not), that no reading text is under 16px, and the heading rule at the window's width. It writes the layer classes short (`display-fat-poster` for `lettering-display-fat-poster`). It is built by `tests/parts/source/lettering.py` from `lettering-template.html` beside it; run `python3 lettering.py ../lettering.html` there to rebuild it. The page is 67 KB and its fonts 545 KB (14 files); where each came from, with its licence and size, is in `tests/parts/fonts/SOURCES.txt`.

## Not covered yet

- **`--metal` and `--dark` from the colour part.** The colour part is adding `--metal` (gold by default on every tone, with `--metal-deep` and `--metal-lit`) and `--dark` (1 on a dark tone). Every rule here reads them with a fallback (`var(--metal, var(--mark))`, `var(--dark, 0)`), so it works before and after; until `tokens.css` carries them, the swatch book sets `--dark: 1` on its dark copy itself and its metal is the stand-in `--mark` (bronze and brass, not gold).
- **A high-contrast serif** (a fashion or editorial display face, thin hairlines) and **a slab**: common on the web, but no mockup or studied site here used one. A stencil and a typewriter face, seen in the warm guide's study, are also not drawn.
- **Lettering drawn as a picture** (a logo traced by hand, letters cut from paper as SVG). Every mockup typed its lettering.
- **Pairings by source.** The pairs here are the ones the mockups used and their owners kept, checked against the rules in R1, R7 and R8 (two faces, each with one job, different enough, a serif with a sans when in doubt, the same skeleton). No published source names any of these exact pairs; Fonts In Use, which records real pairings, would not open.
- **Languages other than English.** Every file kept only the latin block, which lacks many accented letters for central European and Vietnamese text; those sites need the `latin-ext` file too, loaded by `unicode-range` (R29).
- **Windows and phones.** Every picture was taken in the skill's test browser; hinting on Windows makes thin display strokes (Fraunces at opsz 144, Cinzel's serifs) look different.
- **`text-box-trim`**, which trims the space above capitals so a heading lines up with the top of a box, reached every browser in August 2026 (R25). Not yet tried.

## Sources

Read on 2026-10-07. Six kinds of source, all six used: design systems (R14 to R18), craft writing by typographers (R1 to R13, R34), the web platform's own references (R19 to R28, R32, R35), speed (R29 to R33, R50, R51), legibility and accessibility research (R36 to R42), and the traditions the display faces come from (R43 to R49, R52). The mockups made with the skill are the seventh: their CSS and site guides are quoted in each option's "Used on". Pages that would not open: the BDA's own style-guide page (404; read from a copy that cites it, R37), the ACM page for R39 (403; read from summaries), Fonts In Use, Material's pages and Google Fonts' specimen and Knowledge pages (JavaScript only; Material was read from its source code and Knowledge from its public text in the google/fonts repository). Measured here: every font file's axes, size and source, with fontTools 4.66 and the Fontsource API.

- R1 Practical Typography, mixing fonts ("Most documents can tolerate a second font. Few can tolerate a third"; "each font has a consistent role"): practicaltypography.com/mixing-fonts.html
- R2 Practical Typography, line length ("45–90 characters"): practicaltypography.com/line-length.html
- R3 Practical Typography, line spacing ("between 120% and 145% of the point size"): practicaltypography.com/line-spacing.html
- R4 Practical Typography, letterspacing ("5–12% extra space with caps"): practicaltypography.com/letterspacing.html
- R5 Practical Typography, small caps (fake ones "are too tall, and their vertical strokes are too light"): practicaltypography.com/small-caps.html
- R6 Practical Typography, underlining ("don't underline. Ever"): practicaltypography.com/underlining.html
- R7 Google Fonts Knowledge, pairing typefaces ("Do we really need a secondary typeface?"; Jason Santa Maria: "don't compete too much ... but aren't so similar as to be indistinguishable ... pair a serif and a sans serif"): fonts.google.com/knowledge/choosing_type/pairing_typefaces (text from github.com/google/fonts, cc-by-sa/knowledge)
- R8 Google Fonts Knowledge, pairing by construction ("Typefaces from the same form model most likely will go together"; similar flesh, different bones is "irritating"): same repository, lesson pairing_typefaces_based_on_their_construction_using_the_font_matrix
- R9 Google Fonts Knowledge, track carefully ("a more open ... tracking value to all-caps or small caps"; display sizes "a little negative tracking"): same repository, modules/using_type
- R10 Google Fonts Knowledge, weights and grades ("light type on a dark background appears to glare ... 'halation'"; "grade alters only the thickness ... without changing the width"): same repository
- R11 Utopia, designing with fluid type scales (1.2 at 320px, 1.333 at 1500px; calculator 1.2 to 1.25): utopia.fyi/blog/designing-with-fluid-type-scales/ and utopia.fyi/type/calculator/
- R12 Tim Brown, More meaningful typography (modular scales): alistapart.com/article/more-meaningful-typography/
- R13 Typewolf, Fraunces ("inspired by quirky 'Old Style' serifs"): typewolf.com/fraunces
- R14 GOV.UK Design System, type scale (body 19px; heading XL 48px; largest 80px): design-system.service.gov.uk/styles/type-scale/
- R15 GOV.UK Design System, headings and buttons ("Write all headings in sentence case"): design-system.service.gov.uk/styles/headings/
- R16 GOV.UK style guide A to Z ("DO NOT USE BLOCK CAPITALS FOR LARGE AMOUNTS OF TEXT"): guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/
- R17 Material 3 type scale tokens (display large 57, body large 16): github.com/androidx/androidx, compose/material3/.../tokens/TypeScaleTokens.kt
- R18 Carbon, type sets (body 14 and 16px; fluid display up to 92px): carbondesignsystem.com/elements/typography/type-sets/
- R19 MDN, font-variation-settings ("only use it when no basic properties exist"; "will always override"; custom axes upper case): developer.mozilla.org/en-US/docs/Web/CSS/font-variation-settings
- R20 MDN, font-optical-sizing ("enabled by default for fonts that have an optical size variation axis"): developer.mozilla.org/en-US/docs/Web/CSS/font-optical-sizing
- R21 MDN, font-synthesis: developer.mozilla.org/en-US/docs/Web/CSS/font-synthesis
- R22 MDN, font-display (swap, fallback, optional): developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display
- R23 MDN, preload (crossorigin "even when the fetch is not cross-origin"): developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/preload
- R24 MDN, text-wrap (balance limited to six lines in Chromium; pretty for body copy): developer.mozilla.org/en-US/docs/Web/CSS/text-wrap
- R25 MDN, text-box-trim (Baseline since August 2026): developer.mozilla.org/en-US/docs/Web/CSS/text-box-trim
- R26 MDN, text-underline-offset (use em): developer.mozilla.org/en-US/docs/Web/CSS/text-underline-offset
- R27 MDN, box-decoration-break (clone draws each fragment's background): developer.mozilla.org/en-US/docs/Web/CSS/box-decoration-break
- R28 MDN, aria-hidden ("Purely decorative content"): developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-hidden
- R29 web.dev, font best practices (optional waits at most 100ms; WOFF2 30% smaller than WOFF; unicode-range): web.dev/articles/font-best-practices
- R30 web.dev, CSS size-adjust for @font-face: web.dev/articles/css-size-adjust
- R31 Chrome for Developers, font fallbacks in frameworks (size-adjust and the override descriptors): developer.chrome.com/blog/framework-tools-font-fallback
- R32 Google Fonts CSS2 API (an axis not asked for is fixed at its default; text= can cut a file by up to 90%): developers.google.com/fonts/docs/css2
- R33 glyphhanger and fontTools' subsetter (pyftsubset `--flavor=woff2`): github.com/zachleat/glyphhanger, fonttools.readthedocs.io/en/latest/subset/
- R34 Fraunces (opsz 9 to 144, SOFT 0 to 100, WONK automatic above opsz 18): github.com/undercasetype/Fraunces
- R35 Google Fonts METADATA.pb and DESCRIPTION files (axes of Bricolage Grotesque, Newsreader, Source Serif 4, Roboto Flex; Cinzel, Pirata One, Caprasimo, Young Serif described): github.com/google/fonts, ofl/<family>/
- R36 Braille Institute, Atkinson Hyperlegible ("certain letters and numbers can be hard to distinguish"; seven weights; variable) and its Google Fonts metadata (added 2025-01-07): brailleinstitute.org/freefont/
- R37 British Dyslexia Association, dyslexia style guide 2023 (16 to 19px; letter spacing about 35% of letter width; 1.5 line spacing; no underlining, italics or capitals for running text; headings at least 20% larger; 60 to 70 characters): bdadyslexia.org.uk (read from bumc.bu.edu/jmedday/files/2025/05/Dyslexia-friendly-style-guide.docx)
- R38 Wery and Diliberto, the effect of a specialized dyslexia font, OpenDyslexic, Annals of Dyslexia 2017 ("no improvement in reading rate or accuracy"): pmc.ncbi.nlm.nih.gov/articles/PMC5629233/
- R39 Rello and Baeza-Yates, Good fonts for dyslexia, ASSETS 2013 (sans serif, monospaced and roman styles read better; italics worse; read from summaries): dl.acm.org/doi/10.1145/2513383.2513447
- R40 WCAG 2.2, text spacing (1.4.12) and visual presentation (1.4.8: no more than 80 characters; not justified): w3.org/WAI/WCAG22/Understanding/text-spacing.html
- R41 Nielsen Norman Group, glanceable fonts (all caps for longer passages "not recommended"): nngroup.com/articles/glanceable-fonts/
- R42 Adam Argyle, perceived weight for dark mode with GRAD (nerdy.dev/adjust-perceived-typepace-weight-for-dark-mode-without-layout-shift); Robin Rendle, dark mode and variable fonts, 400 to 350 (css-tricks.com/?p=306566)
- R43 Wikipedia, wood type ("lighter and cheaper than large sizes of metal type"; narrow theatre bills): en.wikipedia.org/wiki/Wood_type
- R44 Hamilton Wood Type & Printing Museum (1.5 million pieces of wood type): woodtype.org/pages/about
- R45 Letterform Archive, sign painting's Casual letter: letterformarchive.org/events/view/introduction-to-sign-painting-casual-letters
- R46 Wikipedia, Trajan (capitals from the inscription on Trajan's Column): en.wikipedia.org/wiki/Trajan_(typeface)
- R47 Wikipedia, blackletter (textura, fraktur; mastheads): en.wikipedia.org/wiki/Blackletter
- R48 Typography.Guru, a smart blackletter font (ten letters "typically misread"): typography.guru/journal/a-smart-blackletter-font-7-questions-for-gerrit-ansmann-r69/
- R49 Rough Notation (underline, box, circle, highlight, bracket; 3.8 KB; MIT): roughnotation.com
- R50 SIL OFL FAQ (webfonts allowed, 2.1; subsetting is modification, 2.6; Reserved Font Names, 2.2): openfontlicense.org/ofl-faq/
- R51 Fontsource (Google Fonts packaged for self-hosting; its API lists each family's source and licence): fontsource.org/docs/getting-started/introduction, api.fontsource.org/v1/fonts/<id>
- R52 Google Fonts, League Gothic's description ("a revival of an old classic: Alternate Gothic ... originally designed by Morris Fuller Benton ... in 1903"): github.com/google/fonts, ofl/leaguegothic/DESCRIPTION.en_us.html
