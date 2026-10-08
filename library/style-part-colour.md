---
name: Colour (a part guide)
summary: The colour of the whole page, picked from five small choices instead of a hand-made palette - tone (light, toned, mid, dark, lamplit), neutrals (the hue in the greys, or a sunflower board), accent, strength and bands, and a small sixth for metal (gold, brass, silver, iron). Every colour is worked out from the picks in plain CSS, so any combination is readable, and the result is the shared colour names every other part draws with.
kind: part
detect: []
checked: 2026-10-07
source: research online (six kinds of source, listed under Sources), the colour of 13 mockups made with the skill, and the seven style guides they were made with
---

# Colour

A part guide, and the one the others lean on. It sets the shared colour names (`--ground`, `--surface`, `--ink`, `--accent` and the rest; see "Parts, layers and the shared colour names" in the general guide) for the whole site. Every other part draws only with those names, so whatever is picked here, the background, frames, materials and light follow it. It is the only part allowed to write raw colours.

A site picks colour the way it picks any layered part, in its own guide and in the blueprint as `project.style.parts`: `{"colour": "field-journal"}`, or a starting point with one layer changed, `{"colour": {"start": "warm", "bands": "none"}}`. When guides are stacked, the lead guide decides the colour of the page (the general guide's "When guides are stacked", rule 1); a pick here is how that decision is written down, and it wins over the feel guides for colour only. The accessibility minimums (4.5 to 1 for text, 3 to 1 for the edges of controls and focus rings) hold whatever is picked, and the swatch book checks them for every combination.

**Why layers and not palettes.** Design systems that serve thousands of sites do not hand-make a palette for each one. They ask a few questions and work the colours out: Radix Themes asks for an appearance (light or dark), an accent and a grey, and pairs the grey to the accent's hue (R2, R3); Material builds every role from a seed colour by moving along a scale of lightness (R6, R7); Linear rebuilt its themes from three inputs, a base colour, an accent and a contrast, in place of 98 hand-set values per theme (R21). That is what this part does, with one more question that matters on a made-by-hand site: how coloured the page itself is.

## How it works

Every colour is written as `oklch(lightness chroma hue)`. **Lightness** comes from the tone, **chroma** (how coloured) from the strength times a number the option carries, and **hue** from the neutrals or the accent.

OKLCH is used because its lightness is the lightness the eye sees. In HSL, yellow and blue at "50% lightness" look nothing alike, "clearly the yellow looks much lighter than the blue" (R16; also R17, R18, R20). In OKLCH two colours with the same lightness look about equally light whatever their hue, so a tone can fix the lightness of every role once and any accent can be dropped in. Contrast follows from the gap in lightness, which is how Material, the US government's design system and Stripe guarantee it: "A difference of 40 in HCT tone guarantees a contrast ratio >= 3.0, and a difference of 50 guarantees a contrast ratio >= 4.5" (R6); "any two colors are guaranteed to have sufficient contrast for small text if they are at least five levels apart" (R20; the same idea in R13). The gaps in each tone here are wider than those minimums, and the swatch book still measures every combination, because the two do not line up exactly once a colour has chroma.

One thing OKLCH does not do for you: each hue can only be so colourful at each lightness before it falls off what an ordinary screen shows ("there's no such thing as 'very colorful dark yellow'", R20; "for each hue, there is a different maximum chroma", R14). Past that edge a browser cuts the colour back in its own way and the contrast changes. So the chroma each accent and band carries is worked out once, per tone, a little inside that edge, by `tests/parts/source/colour.py`, and the swatch book checks that nothing falls outside.

Each option below sets only numbers, on the page root (`& { ... }`, which `style css` writes as `:root`). The sums that turn the numbers into the shared names are under **Base**, below, and are lifted whatever is picked; they sit on the same root as the picks, so they always see all six. In the swatch book the same numbers are classes on one element (`<div class="tone-light neutrals-paper accent-brick strength-natural bands-none metal-gold">`) so that many combinations fit on one page; the numbers there have short names (`--l-ground`, `--n-h`), and here each begins `--colour-`, so no other part can set one by accident. A site's second look (`project.style.looks`) is a second stylesheet, or the second tone's block under a class or media query of the site's own.

Seven things in the sums (under Base) are new, and each is said again where it matters:

- **`--on-ground`**, the colour of words straight on the ground. On every tone but one it is `--ink`. On a lamplit page the ground is dark and the sheets are pale paper, so words on the ground are pale and words on a sheet are dark: one `--ink` cannot be both. This guide sets `--on-ground` for that, and it is one of the shared names.
- **`--accent-edge`**, the edge of a control drawn in the accent (a button's border). On most picks it is the accent itself, so it does not show. Where the accent cannot stand 3 to 1 off the ground or a sheet by its fill, the edge carries it: gold on a pale page gets a dark ochre edge, and on a lamplit page the dark button gets an edge in the lamp colour. It is one of the shared names; any part that draws a button gives it `border: 2px solid var(--accent-edge)`.
- **Material colours: `--metal` (with `--metal-deep`, `--metal-lit` and `--on-metal`) and `--earth` (with `--on-earth`).** The neutrals give paper and greys; they cannot give gilt or kraft, and a part that borrowed `--mark` for them got brown rings on a light page and blue ones on night paper. Metal is the colour of rings, studs, keystones and plates, from the `metal` layer below; its shade is 0.24 darker and its highlight 0.2 lighter. Earth is one warm brown (hue 68) for kraft, card, cork, wood and leather, whatever the neutrals: pale kraft by day and under a lamp, a darker card on a mid board, dark wood at night. Words on either use their partner, measured at 4.5 to 1. Both are shared names.
- **`--accent-hover` and `--accent-pressed`**, the accent under a pointer and while pressed: one and two steps in lightness away from the words on it (darker on light, toned and mid pages; lighter on dark and lamplit, where a darker step on a near-black fill would not show; the ink button at night steps darker, as it is near white). Moving away from the words means they only gain contrast; both pairs are measured. Motion's feedback and every part's buttons use these, not a filter or an opacity.
- **`--dark`**, a number: 0 on light, toned and mid pages, 1 on dark and lamplit. For sums in other parts that change with the polarity of the page, such as lettering thinning reading text on a dark page: `font-weight: calc(400 - 30 * var(--dark))`.
- **`--texture-rgb` and `--shadow-rgb`** are written with CSS relative colour (`from oklch(...) r g b`), so they are three numbers worked out from the neutrals, and `rgb(var(--texture-rgb) / 0.2)` in the other parts works unchanged. It needs a browser from 2024 or later (Chrome 119, Safari 18, Firefox 128).
- **`--shadow-strength` and `--texture-strength`** are given a value for each tone, as a starting point. The light part owns shadows and may set its own; the colour part only says how dark a shadow's colour is.

## Choosing

Pick a starting point (below) nearest the brief, then change one layer at a time. The table gives the one sentence for each.

| Starting point | What it feels like | From |
|---|---|---|
| Warm | Cream paper, a bold red and deep bands of colour | the warm guide; a soap shop, a volunteer page |
| Artistic | Grey-white paper and one seal red | the artistic guide; a poetry site |
| Professional | Cool white and one quiet teal-blue | the professional guide |
| Civic | Plain, cool and very clear, with a green go button | research: public-service design systems |
| Sorcery | A night-blue room, warm parchment, one lamp of gold | the sorcery guide; a dark, painterly joke site |
| Gilded dark | Dark brown panes, bright gold, jewel-coloured bands | the game-interface guide (gilded dark) |
| Lantern fair | An oxblood night market: canvas, lantern amber, deep bands | a night-market mockup; a shop with a dark lead |
| Almanac plate | Blue-grey star-chart paper and a red torch | an observatory mockup |
| Catalogue of glazes | Bisque paper and iron red, very quiet | a quiet gallery of pots |
| Field journal | Notebook paper, green-black ink, a kingfisher blue | a field-notebook mockup; a tutoring site |
| Repair café | A sunflower board, black buttons, a red banner | a repair-café mockup |

How to choose, in order:

1. **Tone first: what is the page?** Paper (light), toned paper (toned), card or board (mid), a room at night (dark), or a room at night with the words on lit paper (lamplit). It is the biggest decision in this part and the one that sets the feel: of 13 mockups, 6 were light, 2 mid-tone and 5 dark, and 4 of the 5 dark ones put their reading text on pale paper.
2. **Neutrals: what is the paper made of?** The hue in the greys (or, with marigold, a painted yellow board at mid). Pick it from the subject (sage for a nature site, clay for pottery), or to sit near the accent's hue: Radix pairs every accent with "the gray scale which is saturated with the hue closest to your accent hue" (R2). A warm accent on cool greys (brick on stone) is a deliberate contrast, and works.
3. **Accent: what can be pressed?** One colour, used for things you can press and nothing else (the general guide's "A colour means the same thing everywhere"). Brick red came up most on the mockups (6 of 13), then lantern amber on every dark one.
4. **Strength: how loud?** Muted for calm and serious, natural for most, vivid for bold and playful. On a mid page it also sets how coloured the ground is.
5. **Bands: is there colour in big areas?** None keeps it to the accent; the warm guide asks for "one strong colour ... a whole band or block, not only the buttons".
6. **Metal: only if the page has any.** Rings, studs, plates and gilt take it; gold unless the subject says otherwise (brass for instruments, iron for a workshop).

**A site with a second look** (a dark mode, a night version) keeps its neutrals, accent, strength and bands and changes only the tone: light, toned and mid go to dark; dark and lamplit go to light. Everything else is worked out again by the same sums, so the second look is readable too. Record it in `project.style.looks` with its own colour pick, `{"colour": {"start": "field-journal", "tone": "dark"}}`. The swatch book shows each tone and starting point beside this other look.

## Base

Lifted into every site's stylesheet, whatever is picked. First the sums, which work out every shared name from the picks' numbers; then the few things on the page whose colour is this part's decision and no one else's: the page itself, words on sheets and panels, the main button's fill and words, the focus ring, links, the native controls' tick colour, the drawn decorations and the selection. Fills of sheets are the materials part's, borders and dividers are drawn by frames (this part only gives them their colour, so a border drawn later in `--accent-edge` or `--line` agrees), and coloured bands are drawn by the background part.

```css assemble
/* colour: the sums. Lightness from the tone, chroma from the strength and the option, hue from the neutrals or the accent */
& {
  --ground: oklch(var(--colour-l-ground) calc(var(--colour-n-c) * var(--colour-k-ground) * var(--colour-k-ground-strength)) var(--colour-g-h));
  --surface: oklch(var(--colour-l-surface) calc(var(--colour-s-c) * var(--colour-k-sheet)) var(--colour-s-h));
  --surface-raised: oklch(var(--colour-l-raised) calc(var(--colour-s-c) * var(--colour-k-sheet) * 0.3) var(--colour-s-h));
  --ink: oklch(var(--colour-l-ink) calc(var(--colour-s-c) * 1.5) var(--colour-s-h));
  --ink-soft: oklch(var(--colour-l-soft) calc(var(--colour-s-c) * 2) var(--colour-s-h));
  --line: oklch(var(--colour-l-line) calc(var(--colour-s-c) * 2.5) var(--colour-s-h));
  --accent: oklch(var(--colour-l-accent) calc(var(--colour-c-accent) * var(--colour-k)) var(--colour-h-accent));
  --on-accent: oklch(var(--colour-l-on-accent) var(--colour-c-on-accent) var(--colour-h-accent));
  --accent-hover: oklch(var(--colour-l-hover) calc(var(--colour-c-hover) * var(--colour-k)) var(--colour-h-accent));   /* a pointer over it */
  --accent-pressed: oklch(var(--colour-l-pressed) calc(var(--colour-c-pressed) * var(--colour-k)) var(--colour-h-accent));   /* while pressed */
  --accent-edge: oklch(var(--colour-l-edge) calc(var(--colour-c-edge) * var(--colour-k)) var(--colour-h-accent));   /* the edge of a control in the accent */
  --focus: oklch(var(--colour-l-focus) var(--colour-c-focus) var(--colour-focus-h, var(--colour-h-accent)));
  --mark: oklch(var(--colour-l-mark) calc(var(--colour-mark-c) * var(--colour-k)) var(--colour-n-h));
  --band-1: oklch(var(--colour-l-band) calc(var(--colour-b1-c) * var(--colour-k)) var(--colour-b1-h));
  --band-2: oklch(var(--colour-l-band) calc(var(--colour-b2-c) * var(--colour-k)) var(--colour-b2-h));
  --band-3: oklch(var(--colour-l-band) calc(var(--colour-b3-c) * var(--colour-k)) var(--colour-b3-h));
  --on-band: oklch(var(--colour-l-on-band) 0.01 var(--colour-n-h));
  --metal: oklch(calc(var(--colour-l-metal) + var(--colour-metal-dl)) var(--colour-c-metal) var(--colour-m-h));   /* metal and gilt: rings, studs, plates */
  --metal-deep: oklch(calc(var(--colour-l-metal) + var(--colour-metal-dl) - 0.24) var(--colour-c-metal-deep) var(--colour-m-h));
  --metal-lit: oklch(min(0.95, calc(var(--colour-l-metal) + var(--colour-metal-dl) + 0.2)) var(--colour-c-metal-lit) var(--colour-m-h));
  --on-metal: oklch(var(--colour-l-on-metal) 0.01 var(--colour-m-h));
  --earth: oklch(var(--colour-l-earth) var(--colour-c-earth) 68);   /* kraft, card, cork, wood, leather */
  --on-earth: oklch(var(--colour-l-on-earth) 0.01 68);
  --texture-rgb: from oklch(var(--colour-l-texture) calc(var(--colour-n-c) * 2) var(--colour-n-h)) r g b;   /* three numbers, for rgb(var(--texture-rgb) / a) */
  --shadow-rgb: from oklch(var(--colour-l-shadow) calc(var(--colour-n-c) * 2) var(--colour-n-h)) r g b;
  --scrim: rgb(var(--shadow-rgb) / var(--colour-scrim-a));
  background-color: var(--ground); color: var(--on-ground);   /* the page itself: html paints the whole window */
  accent-color: var(--accent);   /* native tick boxes, radios and sliders */
}
```

```css assemble
/* colour: what is coloured whatever is picked */
.sheet, .panel { color: var(--ink); }   /* words on a sheet; on a lamplit page they are dark while the ground's are pale */
.sheet :is(.label, figcaption, small), .panel :is(.label, figcaption, small) { color: var(--ink-soft); }
.btn-main { background-color: var(--accent); color: var(--on-accent); border-color: var(--accent-edge); }
.btn-main:hover { background-color: var(--accent-hover); }
.btn-main:active { background-color: var(--accent-pressed); }
.btn:not(.btn-main) { color: inherit; border-color: currentColor; }
.field { background-color: var(--surface-raised); color: var(--ink); border-color: var(--ink-soft); }   /* the edge of a control is 3 to 1 */
a:not(.btn) { color: inherit; text-decoration-color: var(--accent-edge); }   /* links are underlined words in the text's colour: the accent is not 4.5 to 1 as text */
.sheet a:not(.btn), .panel a:not(.btn) { text-decoration-color: currentColor; }   /* on lamplit parchment the lamp-gold underline would vanish */
:focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; }
.deco, .mark { color: var(--mark); }   /* drawn decoration, never meaning; it draws in currentColor */
.rule, hr { border-color: var(--line); }
::selection { background-color: var(--accent); color: var(--on-accent); }
```

## Layers

### Tone
- Layer: tone
- Owns: how light the page is, and so the lightness of every colour on it: ground, sheets, ink, accent, bands, focus ring and the status colours. Also the light-or-dark pairing the other parts' swatch books show: on a colour page, the tone takes its place.
- Default: light

#### Light
- Id: light
- Status: draft
- Looks like: a pale paper page (lightness 0.965), whiter sheets on it, near-black ink with a little of the paper's hue in it, and an accent at middle lightness with white words. The page most sites have, and the easiest to read.
- Made with: lightness of each role, as in every tone below. The accent sits at 0.50 so white words on it pass and it still stands 3 to 1 off the paper.

```css assemble
/* colour / tone: light */
& { color-scheme: light;
  --colour-l-ground: 0.965; --colour-g-h: var(--colour-n-h); --colour-l-surface: 0.99; --colour-l-raised: 0.997; --colour-l-ink: 0.23; --colour-l-soft: 0.46; --colour-l-line: 0.86;
  --colour-l-accent: var(--colour-accent-l-light, 0.5); --colour-c-accent: var(--colour-accent-c-light); --colour-h-accent: var(--colour-accent-h-light, var(--colour-a-h));
  --colour-l-on-accent: var(--colour-on-accent-l-light, 0.98); --colour-c-on-accent: 0.008; --colour-l-edge: var(--colour-edge-l-light, var(--colour-l-accent)); --colour-c-edge: var(--colour-edge-c-light, var(--colour-c-accent)); --colour-l-focus: 0.42; --colour-c-focus: var(--colour-focus-c-light);
  --colour-l-mark: 0.52; --colour-l-band: var(--colour-band-l-light, 0.42); --colour-l-on-band: var(--colour-on-band-l-light, 0.965); --colour-l-texture: 0.3; --colour-l-shadow: 0.25;
  --colour-k-ground: 1; --colour-k-ground-strength: 1; --colour-k-sheet: 0.3; --colour-s-h: var(--colour-n-h); --colour-s-c: var(--colour-n-c);
  --on-ground: var(--ink);
  --danger: oklch(0.5 0.16 27); --success: oklch(0.5 0.132 150); --warning: oklch(0.5 0.104 70);
  --colour-l-hover: calc(var(--colour-l-accent) + var(--colour-step-light, -0.05)); --colour-l-pressed: calc(var(--colour-l-accent) + 2 * var(--colour-step-light, -0.05)); --colour-c-hover: var(--colour-hover-c-light, var(--colour-c-accent)); --colour-c-pressed: var(--colour-pressed-c-light, var(--colour-c-accent)); --dark: 0;
  --colour-l-metal: 0.7; --colour-c-metal: var(--colour-metal-c-light); --colour-c-metal-deep: var(--colour-metal-deep-c-light); --colour-c-metal-lit: var(--colour-metal-lit-c-light); --colour-l-on-metal: var(--colour-on-metal-l-light);
  --colour-l-earth: 0.7; --colour-c-earth: 0.08; --colour-l-on-earth: 0.18;
  --colour-scrim-a: 0.45; --texture-strength: 0.1; --shadow-strength: 0.18; }
```

- Careful: a pale ground with white boxes and one accent on the buttons is the template look (tell 7 in the general guide). Light is not the problem; having nothing else chosen is. Give it bands, a toned neutral, or a signature from another part. Amber is the one accent that is bright here: a gold fill with dark words on it and a dark ochre edge (`--accent-edge`), because gold cannot be dark enough to stand 3 to 1 off a pale page and still be gold. Any part drawing a button must draw the edge, or the gold button floats.
- Light and dark: its other look is `tone: dark`.
- Personality: serious, calm, friendly
- Goes with: `background: texture none` or `background: texture grain`; `materials: fine-paper`; `light: flat-and-even`.
- Used on: 6 of 13 mockups (a soap shop, a tutoring site, a poetry site in all three of its looks, a volunteer page, the sheets of an observatory, a field notebook's sheets); the professional, artistic, sales and education guides all ask for a white or near-white ground (10 of 12 and 7 of 7 of the sites they studied).

#### Toned
- Id: toned
- Status: draft
- Looks like: toned paper, a step down from white (lightness 0.89): cream, bisque, notebook paper, a soft grey-green. The sheets on it are lighter and the ink is the same near-black. Calmer and more made than white.
- Made with: the ground darker and nearly twice as coloured as on light; sheets near white.

```css assemble
/* colour / tone: toned */
& { color-scheme: light;
  --colour-l-ground: 0.89; --colour-g-h: var(--colour-n-h); --colour-l-surface: 0.972; --colour-l-raised: 0.99; --colour-l-ink: 0.22; --colour-l-soft: 0.44; --colour-l-line: 0.79;
  --colour-l-accent: var(--colour-accent-l-toned, 0.47); --colour-c-accent: var(--colour-accent-c-toned); --colour-h-accent: var(--colour-accent-h-toned, var(--colour-a-h));
  --colour-l-on-accent: var(--colour-on-accent-l-toned, 0.98); --colour-c-on-accent: 0.008; --colour-l-edge: var(--colour-edge-l-toned, var(--colour-l-accent)); --colour-c-edge: var(--colour-edge-c-toned, var(--colour-c-accent)); --colour-l-focus: 0.36; --colour-c-focus: var(--colour-focus-c-toned);
  --colour-l-mark: 0.48; --colour-l-band: var(--colour-band-l-toned, 0.4); --colour-l-on-band: var(--colour-on-band-l-toned, 0.965); --colour-l-texture: 0.3; --colour-l-shadow: 0.25;
  --colour-k-ground: 1.8; --colour-k-ground-strength: 1; --colour-k-sheet: 0.8; --colour-s-h: var(--colour-n-h); --colour-s-c: var(--colour-n-c);
  --on-ground: var(--ink);
  --danger: oklch(0.47 0.16 27); --success: oklch(0.47 0.124 150); --warning: oklch(0.47 0.098 70);
  --colour-l-hover: calc(var(--colour-l-accent) + var(--colour-step-toned, -0.05)); --colour-l-pressed: calc(var(--colour-l-accent) + 2 * var(--colour-step-toned, -0.05)); --colour-c-hover: var(--colour-hover-c-toned, var(--colour-c-accent)); --colour-c-pressed: var(--colour-pressed-c-toned, var(--colour-c-accent)); --dark: 0;
  --colour-l-metal: 0.68; --colour-c-metal: var(--colour-metal-c-toned); --colour-c-metal-deep: var(--colour-metal-deep-c-toned); --colour-c-metal-lit: var(--colour-metal-lit-c-toned); --colour-l-on-metal: var(--colour-on-metal-l-toned);
  --colour-l-earth: 0.67; --colour-c-earth: 0.08; --colour-l-on-earth: 0.18;
  --colour-scrim-a: 0.45; --texture-strength: 0.11; --shadow-strength: 0.18; }
```

- Careful: with wine or night neutrals the ground reads as pink or lavender; that is a choice, not a paper. Soft text straight on the ground passes, but only just less well than on a sheet.
- Light and dark: its other look is `tone: dark`.
- Personality: calm, friendly
- Goes with: `background: texture grain`; `materials: paper-and-tape`; `frames: hairline`.
- Used on: 3 mockups (a quiet gallery on bisque, a field notebook on gridded paper, a poetry site's "press" look on warmer paper).

#### Mid
- Id: mid
- Status: draft
- Looks like: the ground is a colour, not a paper: kraft card, terracotta, a slate or sage board, a yellow pegboard. Pale sheets are pinned on it, the ink is dark, and the accent is deep (lightness 0.37) so it stands off the ground.
- Made with: a ground at lightness 0.75, five times as coloured as on light, and more again with `strength: vivid`. A neutral can carry its own mid ground (`--colour-mid-l`, `--colour-mid-k`, `--colour-mid-h`): night and wine are greyer and a little deeper, marigold lighter and much yellower (see each). Printers' advice for kraft is the rule here: dark inks only, "black, navy, deep red, forest green ... Light and pastel inks tend to sink into the brown" (R36). So everything that must be seen on a mid ground is dark: ink, accent, focus ring, marks and bands.

```css assemble
/* colour / tone: mid */
& { color-scheme: light;
  --colour-l-ground: var(--colour-mid-l, 0.75); --colour-g-h: var(--colour-mid-h, var(--colour-n-h)); --colour-l-surface: 0.96; --colour-l-raised: 0.98; --colour-l-ink: 0.2; --colour-l-soft: 0.42; --colour-l-line: 0.7;
  --colour-l-accent: var(--colour-accent-l-mid, 0.37); --colour-c-accent: var(--colour-accent-c-mid); --colour-h-accent: var(--colour-accent-h-mid, var(--colour-a-h));
  --colour-l-on-accent: var(--colour-on-accent-l-mid, 0.98); --colour-c-on-accent: 0.008; --colour-l-edge: var(--colour-edge-l-mid, var(--colour-l-accent)); --colour-c-edge: var(--colour-edge-c-mid, var(--colour-c-accent)); --colour-l-focus: 0.25; --colour-c-focus: var(--colour-focus-c-mid);
  --colour-l-mark: 0.36; --colour-l-band: var(--colour-band-l-mid, 0.36); --colour-l-on-band: var(--colour-on-band-l-mid, 0.965); --colour-l-texture: 0.25; --colour-l-shadow: 0.22;
  --colour-k-ground: var(--colour-mid-k, 5); --colour-k-ground-strength: var(--colour-k-mid-ground); --colour-k-sheet: 1; --colour-s-h: var(--colour-n-h); --colour-s-c: var(--colour-n-c);
  --on-ground: var(--ink);
  --danger: oklch(0.46 0.16 27); --success: oklch(0.46 0.122 150); --warning: oklch(0.46 0.096 70);
  --colour-l-hover: calc(var(--colour-l-accent) + var(--colour-step-mid, -0.05)); --colour-l-pressed: calc(var(--colour-l-accent) + 2 * var(--colour-step-mid, -0.05)); --colour-c-hover: var(--colour-hover-c-mid, var(--colour-c-accent)); --colour-c-pressed: var(--colour-pressed-c-mid, var(--colour-c-accent)); --dark: 0;
  --colour-l-metal: 0.63; --colour-c-metal: var(--colour-metal-c-mid); --colour-c-metal-deep: var(--colour-metal-deep-c-mid); --colour-c-metal-lit: var(--colour-metal-lit-c-mid); --colour-l-on-metal: var(--colour-on-metal-l-mid);
  --colour-l-earth: 0.6; --colour-c-earth: 0.08; --colour-l-on-earth: 0.18;
  --colour-scrim-a: 0.5; --texture-strength: 0.12; --shadow-strength: 0.22; }
```

- Careful: soft text and status colours are measured on the sheets, not on the ground; on the ground they fall under 4.5 to 1, so keep them on a sheet. A mid ground may be light (marigold's sunflower is 0.81): everything that must show on it is dark, so a lighter ground only helps; it is a darker one that fails, which is why wine stops at 0.66. Mid grounds are rare in design systems (none of those read has one) and rare on the web ("brown is one of the least used colors in website design", R41), which is exactly why they make a site look made. The accent is dark on this tone except amber, which stays gold with a dark edge; for other bright patches use bands or the materials part.
- Light and dark: its other look is `tone: dark`; the kraft becomes a dark room of the same hue.
- Personality: friendly, playful
- Goes with: `background: texture felt-weave` or `background: pattern coloured-bands`; `materials: paper-and-tape` or `materials: cut-paper-on-felt`; `frames: torn-paper`.
- Used on: 2 mockups (a repair café on a sunflower pegboard, `neutrals: marigold`; a quiet gallery whose bisque sits between toned and mid), and the kraft tags and manila on several others.

#### Dark
- Id: dark
- Status: draft
- Looks like: a room at night with a colour of its own (lightness 0.19, never black): oxblood, night blue, dark brown, slate. The sheets are a step lighter than the room, the words on them are pale and warm or cool, and the accent is bright (0.72; amber at 0.80, brick and forest lower and earthier) with dark words on it.
- Made with: the dark ground carries more of the neutral's hue than a light one, because a grey at that lightness reads as black. Raised things are lighter, not shadowed.

```css assemble
/* colour / tone: dark */
& { color-scheme: dark;
  --colour-l-ground: 0.19; --colour-g-h: var(--colour-n-h); --colour-l-surface: 0.235; --colour-l-raised: 0.29; --colour-l-ink: 0.93; --colour-l-soft: 0.79; --colour-l-line: 0.4;
  --colour-l-accent: var(--colour-accent-l-dark, 0.72); --colour-c-accent: var(--colour-accent-c-dark); --colour-h-accent: var(--colour-accent-h-dark, var(--colour-a-h));
  --colour-l-on-accent: var(--colour-on-accent-l-dark, 0.2); --colour-c-on-accent: 0.008; --colour-l-edge: var(--colour-edge-l-dark, var(--colour-l-accent)); --colour-c-edge: var(--colour-edge-c-dark, var(--colour-c-accent)); --colour-l-focus: 0.88; --colour-c-focus: var(--colour-focus-c-dark);
  --colour-l-mark: 0.76; --colour-l-band: var(--colour-band-l-dark, 0.31); --colour-l-on-band: var(--colour-on-band-l-dark, 0.95); --colour-l-texture: 0.92; --colour-l-shadow: 0.08;
  --colour-k-ground: 1.6; --colour-k-ground-strength: 1; --colour-k-sheet: 1.4; --colour-s-h: var(--colour-n-h); --colour-s-c: var(--colour-n-c);
  --on-ground: var(--ink);
  --danger: oklch(0.8 0.11 27); --success: oklch(0.8 0.16 150); --warning: oklch(0.8 0.156 70);
  --colour-l-hover: calc(var(--colour-l-accent) + var(--colour-step-dark, 0.05)); --colour-l-pressed: calc(var(--colour-l-accent) + 2 * var(--colour-step-dark, 0.05)); --colour-c-hover: var(--colour-hover-c-dark, var(--colour-c-accent)); --colour-c-pressed: var(--colour-pressed-c-dark, var(--colour-c-accent)); --dark: 1;
  --colour-l-metal: 0.74; --colour-c-metal: var(--colour-metal-c-dark); --colour-c-metal-deep: var(--colour-metal-deep-c-dark); --colour-c-metal-lit: var(--colour-metal-lit-c-dark); --colour-l-on-metal: var(--colour-on-metal-l-dark);
  --colour-l-earth: 0.36; --colour-c-earth: 0.05; --colour-l-on-earth: 0.96;
  --colour-scrim-a: 0.6; --texture-strength: 0.16; --shadow-strength: 0.45; }
```

- Careful: not pure black and not pure white. Material's dark theme uses a dark grey "because it's easier to see shadows on gray (instead of black)" and because light text on black glares (R9); Apple says dark colours "aren't necessarily inversions" of light ones (R27). Every dark mockup here had a hued ground (oxblood, night blue, brown), never grey. WCAG's ratio overstates contrast near black ("4.5:1 can be functionally unreadable when a color is near black", R28), so the words here are kept well above it (the lowest pair, soft text on a sheet, is near 9 to 1). A dark page where everything glows has no light (the sorcery guide): keep the accent to the things you press. Lifting a colour for a dark page also makes it sweeter: red goes coral and green goes mint. So brick and forest are lifted less (0.64 and 0.66), with less chroma, and turned warmer (rust and moss); Material asks for "desaturated colors" on dark themes for the same reason (R9).
- Light and dark: its other look is `tone: light`.
- Personality: dramatic, serious
- Goes with: `light: one-light` or `light: glow-on-edges`; `materials: metal-and-dark-glass`; `frames: riveted-metal`.
- Used on: 2 mockups with dark sheets (a game-style joke site in its gold and its steel looks, on dark panes); the dark grounds of all 5 dark mockups.

#### Lamplit
- Id: lamplit
- Status: draft
- Looks like: a dark room (the same as dark), and the words on warm paper held up to a lamp: parchment, canvas or a chart read by torchlight, at lightness 0.80, with dark brown ink. The button is turned round: dark, in the accent's hue, with words and an edge in the lamp colour, so it stands off the parchment and still shows a lit rim on the dark ground.
- Made with: the ground, line, texture and shadow take the neutral's hue; the sheets are always warm paper (hue 75), because lamplight is warm whatever the room. Words straight on the ground use `--on-ground`, a pale cream, because `--ink` is dark for the sheets. The accent is at 0.30 with words at 0.85 in its hue (`--on-accent` carries colour here, nowhere else), and `--accent-edge` is the lamp colour itself, the dark tone's accent.

```css assemble
/* colour / tone: lamplit */
& { color-scheme: dark;
  --colour-l-ground: 0.19; --colour-g-h: var(--colour-n-h); --colour-l-surface: 0.8; --colour-l-raised: 0.86; --colour-l-ink: 0.2; --colour-l-soft: 0.37; --colour-l-line: 0.56;
  --colour-l-accent: var(--colour-accent-l-lamplit, 0.3); --colour-c-accent: var(--colour-accent-c-lamplit); --colour-h-accent: var(--colour-accent-h-lamplit, var(--colour-a-h));
  --colour-l-on-accent: var(--colour-on-accent-l-lamplit, 0.85); --colour-c-on-accent: calc(var(--colour-on-accent-c-lamplit, 0.008) * var(--colour-k)); --colour-l-edge: var(--colour-edge-l-lamplit, var(--colour-l-accent)); --colour-c-edge: var(--colour-edge-c-lamplit, var(--colour-c-accent)); --colour-l-focus: 0.88; --colour-c-focus: var(--colour-focus-c-lamplit);
  --colour-l-mark: 0.76; --colour-l-band: var(--colour-band-l-lamplit, 0.31); --colour-l-on-band: var(--colour-on-band-l-lamplit, 0.95); --colour-l-texture: 0.92; --colour-l-shadow: 0.08;
  --colour-k-ground: 1.8; --colour-k-ground-strength: 1; --colour-k-sheet: 3.2; --colour-s-h: 75; --colour-s-c: 0.022;
  --on-ground: oklch(0.91 0.02 75);
  --danger: oklch(0.4 0.156 27); --success: oklch(0.4 0.106 150); --warning: oklch(0.4 0.083 70);
  --colour-l-hover: calc(var(--colour-l-accent) + var(--colour-step-lamplit, 0.06)); --colour-l-pressed: calc(var(--colour-l-accent) + 2 * var(--colour-step-lamplit, 0.06)); --colour-c-hover: var(--colour-hover-c-lamplit, var(--colour-c-accent)); --colour-c-pressed: var(--colour-pressed-c-lamplit, var(--colour-c-accent)); --dark: 1;
  --colour-l-metal: 0.74; --colour-c-metal: var(--colour-metal-c-lamplit); --colour-c-metal-deep: var(--colour-metal-deep-c-lamplit); --colour-c-metal-lit: var(--colour-metal-lit-c-lamplit); --colour-l-on-metal: var(--colour-on-metal-l-lamplit);
  --colour-l-earth: 0.68; --colour-c-earth: 0.08; --colour-l-on-earth: 0.18;
  --colour-scrim-a: 0.6; --texture-strength: 0.16; --shadow-strength: 0.45; }
```

- Careful: the parchment is dim on purpose; the sorcery guide's paper "never becomes a white page", and one mockup set it at two-thirds of the lamp's brightness. A bright lamp-coloured button is so close to the parchment in lightness that it vanishes on a sheet (the first version did exactly that), which is why the button is dark here: it works on a sheet and on the ground alike. Draw its edge (`--accent-edge`), or on the dark ground it is only gold words. Links on a sheet are `--ink`, underlined, not the accent. Status colours are dark here, for the sheets; on the ground they would fail. Any other part that writes words straight on the ground must use `--on-ground`.
- Light and dark: its other look is `tone: light`: the same paper hue becomes the page.
- Personality: dramatic
- Goes with: `materials: parchment-and-ink`; `light: one-light`; `background: texture mottled-and-hatched`; `frames: inked-panel`.
- Used on: 4 of the 5 dark mockups (a dark, painterly joke site with parchment in a night-blue hall, a small shop with parchment tags in an oxblood stall, a night market with canvas and paper tags, an observatory whose sheets stay light under a night sky "like a chart read by torchlight").

### Neutrals
- Layer: neutrals
- Owns: the hue in the greys, and how much: the ground, the sheets, the ink, soft text, lines, texture, shadows and the drawn marks all take it. It is what the page is made of.
- Default: paper

#### Paper
- Id: paper
- Status: draft
- Looks like: warm cream paper and brown-black ink by day; kraft at mid; dark brown at night.
- Made with: a yellow-orange hue at a whisper of chroma. Tinted greys in systems sit at about 0.002 to 0.03 chroma (R5); Material tints its greys with the seed's hue at a low chroma (R7). "Add a small amount of colour saturation to a grey background" (R24); greys should lean warm or cool "but only slightly" (R26).

```css assemble
/* colour / neutrals: paper */
& { --colour-n-h: 80; --colour-n-c: 0.012; --colour-mark-c: 0.072; }
```

- Careful: the safe default; if every site takes it they will look alike. With amber or brick it is all warm: give it a cool band or a cool mark if it needs air.
- Light and dark: cream (`#f8f3eb`) by day, kraft (`#c2aa83`) at mid, dark brown (`#18130a`) at night.
- Personality: friendly, calm
- Goes with: `materials: paper-and-tape`; `background: texture grain`.
- Used on: most light mockups (cream from `#f6f1e7` to `#fffaf0` on 6 of 7 light sites), the kraft tags on several, and the warm, artistic and sales guides.

#### Stone
- Id: stone
- Status: draft
- Looks like: cool, nearly plain grey: white with a hint of blue by day, slate at mid, blue-black at night. The most neutral, so the accent does all the talking.
- Made with: a blue hue at the lowest chroma of the set.

```css assemble
/* colour / neutrals: stone */
& { --colour-n-h: 250; --colour-n-c: 0.007; --colour-mark-c: 0.098; }
```

- Careful: this is where the template look lives (a cool white page and a blue button). Pair it with a warm accent (brick, amber) or a strong signature.
- Light and dark: cool white (`#f0f4f8`), slate (`#9eb0c4`), blue-black (`#101419`).
- Personality: serious, calm
- Goes with: `materials: fine-paper`; `light: flat-and-even`; `frames: hairline`.
- Used on: the professional and education guides ("one institutional colour on a white or near-white ground", 10 of 12 sites each); from research: Carbon's "neutral gray family is dominant" (R11).

#### Sage
- Id: sage
- Status: draft
- Looks like: grey-green: pale celadon paper, green-black ink, a sage board at mid, a deep forest room at night.
- Made with: a green hue at low chroma.

```css assemble
/* colour / neutrals: sage */
& { --colour-n-h: 150; --colour-n-c: 0.011; --colour-mark-c: 0.095; }
```

- Careful: with the forest accent the page is all green; pick kingfisher or brick for a second colour.
- Light and dark: `#eff6f0`, toned `#d2dfd4`, at mid `#96b89c`, night `#0e1610`.
- Personality: calm, friendly
- Goes with: `materials: fine-paper` or `materials: paper-and-tape`; `background: texture grain`.
- Used on: 3 mockups (green-black ink on a soap shop and a field notebook, grey-green bands on a tutoring site). From research: Radix pairs its sage grey with green and teal accents (R2).

#### Clay
- Id: clay
- Status: draft
- Looks like: bisque and terracotta: a warm, pinkish paper by day, terracotta at mid, burnt umber at night, with brown ink.
- Made with: an orange hue, a little more chroma than paper.

```css assemble
/* colour / neutrals: clay */
& { --colour-n-h: 55; --colour-n-c: 0.016; --colour-mark-c: 0.086; }
```

- Careful: at toned it is a warm bisque, a little pinker than the gallery it came from (`#ddd3c1`); for a greyer one use paper. At mid it is terracotta, which is loud for a quiet site.
- Light and dark: `#fdf1ea`, toned bisque `#ebd6c9`, terracotta `#d6a17d`, umber `#1d1108`.
- Personality: calm, friendly
- Goes with: `materials: fine-paper`; `light: flat-and-even`; `background: texture grain`.
- Used on: 1 mockup (a quiet gallery of pots on bisque, with iron-red glaze as its accent).

#### Night
- Id: night
- Status: draft
- Looks like: blue-grey star-chart paper by day, a slate-blue board at mid, and night blue at night, the colour of a hall lit by one orb.
- Made with: a blue-violet hue. At mid it turns bluer (252), greyer (2.6 times its chroma, not 5) and a little deeper (0.72): at the usual mid it was periwinkle.

```css assemble
/* colour / neutrals: night */
& { --colour-n-h: 275; --colour-n-c: 0.014; --colour-mark-c: 0.11; --colour-mid-l: 0.72; --colour-mid-k: 2.6; --colour-mid-h: 252; }
```

- Careful: at mid it is a slate board, quiet; with `strength: vivid` it goes towards denim. At night it is the commonest dark ground on the mockups after oxblood.
- Light and dark: `#f0f3fd`, at mid `#95a7bb`, night `#11131e`.
- Personality: calm, dramatic
- Goes with: `light: moonlight` or `light: one-light`; `materials: parchment-and-ink`.
- Used on: 3 mockups at night (a dark, painterly joke site's night-blue hall `#131129`, the steel look of a game-style joke site `#050c1c`, an observatory's night sky), and one by day (a volunteer page's navy ink).

#### Wine
- Id: wine
- Status: draft
- Looks like: a blush of red: rose-white by day, a rosewood board at mid, oxblood at night.
- Made with: a red hue. At mid it turns browner (22), greyer (2.7 times, not 5) and deeper (0.66, as deep as a mid ground can go with a dark accent still 3 to 1 off it): at the usual mid it was dusty rose.

```css assemble
/* colour / neutrals: wine */
& { --colour-n-h: 15; --colour-n-c: 0.015; --colour-mark-c: 0.11; --colour-mid-l: 0.66; --colour-mid-k: 2.7; --colour-mid-h: 22; }
```

- Careful: by day it reads as pink; it is chosen for its dark side. The mid board is still a little rosy: a true oxblood board would be too dark for dark ink, so for that use `tone: dark`. A red accent on it has little contrast of hue; amber or forest stand off it better.
- Light and dark: `#fdf0f0`, at mid `#aa8987`, oxblood `#1d0f10`.
- Personality: dramatic, friendly
- Goes with: `light: one-light`; `materials: wood-and-canvas`; `background: pattern coloured-bands`.
- Used on: 3 mockups at night (a night market `#4a1219` and two versions of a small shop, `#1e0e11` and `#1a0b12`). The sorcery guide names wine first among its dark grounds.

#### Marigold
- Id: marigold
- Status: draft
- Looks like: a painted yellow board at mid, a sunflower pegboard, bold and cheerful, with pale sheets pinned on it; butter-cream paper by day; dark honey-brown at night.
- Made with: a warm yellow hue at a little more chroma than paper, and its own mid ground: lighter than any other (0.81) and six and a half times as coloured, at hue 80. A mid ground can be this light because everything on it is dark; it is darker grounds that fail. At `strength: vivid` it is sunflower (`#f5b42e`), at natural a softer marigold.

```css assemble
/* colour / neutrals: marigold */
& { --colour-n-h: 85; --colour-n-c: 0.016; --colour-mark-c: 0.071; --colour-mid-l: 0.81; --colour-mid-k: 6.5; --colour-mid-h: 80; }
```

- Careful: made for its mid board; by day it is close to paper. A whole page of vivid yellow is loud: the repair café holds it with black buttons and black lettering and pale sheets for the reading. Amber on it is gold on gold, held apart only by the edge; use `accent: ink` or a deep accent.
- Light and dark: `#f8f3e8`, toned `#e3dac6`, at mid `#e4ba70` (vivid `#f5b42e`), night `#191306`.
- Personality: playful, friendly
- Goes with: `accent` ink; `bands` poster; `materials: paper-and-tape`; `frames: torn-paper`.
- Used on: 1 mockup (a repair café on a sunflower pegboard `#f4b62f`); the volunteer page's poster yellow.

### Accent
- Layer: accent
- Owns: `--accent` (things you can press), `--on-accent` (the words on it) and `--focus` (the keyboard ring). The accent's hue is fixed; its lightness comes from the tone and its chroma from the strength.
- Default: brick

Every accent holds 4.5 to 1 for words on it, and stands 3 to 1 off the ground and off a sheet by its fill or by its edge (`--accent-edge`), at every tone and strength (WCAG 1.4.3 and 1.4.11, R29, R30). WCAG itself asks less: a button with words on it needs no boundary at all, since "the button's text is sufficient to indicate the presence of the control" (R29). The edge is kept because a button that blends into its paper looks like a label. One accent is the rule. Systems keep added colour "sparingly and purposefully" (R11); designers who build good palettes start from "an interface with one color and many modifications" (R23). A second colour for a different job (a drawn mark, a band) comes from the mark or the bands, never a second accent.

#### Brick
- Id: brick
- Status: draft
- Looks like: rust and seal red by day (`#9a4632`), deeper on kraft, terracotta-rust at night (`#c17656`). The red of a stamp, a rubric or a seal.
- Made with: hue 35, and the most chroma that hue holds at each tone's lightness. On dark pages it is lifted less (0.64, not 0.72), held to 0.15 chroma and turned towards rust (44): lifted like the others it was coral.

```css assemble
/* colour / accent: brick */
& { --colour-a-h: 35;
  --colour-accent-l-dark: 0.64; --colour-accent-h-dark: 44; --colour-accent-h-lamplit: 44;
  --colour-accent-c-light: 0.168; --colour-accent-c-toned: 0.158; --colour-accent-c-mid: 0.125; --colour-accent-c-dark: 0.15; --colour-accent-c-lamplit: 0.084;
  --colour-focus-c-light: 0.141; --colour-focus-c-toned: 0.121; --colour-focus-c-mid: 0.084; --colour-focus-c-dark: 0.065; --colour-focus-c-lamplit: 0.065;
  --colour-hover-c-light: 0.152; --colour-pressed-c-light: 0.135; --colour-hover-c-toned: 0.141; --colour-pressed-c-toned: 0.125; --colour-hover-c-mid: 0.108; --colour-pressed-c-mid: 0.091;
  --colour-hover-c-dark: 0.15; --colour-pressed-c-dark: 0.15; --colour-hover-c-lamplit: 0.084; --colour-pressed-c-lamplit: 0.084;
  --colour-edge-l-lamplit: 0.64; --colour-edge-c-lamplit: 0.15; --colour-on-accent-c-lamplit: 0.084; }
```

- Careful: red means danger to many people. The danger colour here is a purer red at another lightness, and errors always carry a word or an icon as well (the general guide's "Never colour alone").
- Light and dark: rust by day, a lighter rust at night; on lamplit a dark rust button with peach words and a rust edge.
- Personality: friendly, serious, dramatic
- Goes with: `lettering: soft-serif`; `materials: fine-paper`.
- Used on: 6 of 13 mockups (iron red, seal red, torch red, ember, a poster red, a robin rust); the commonest accent by far. From research: red is "the typographer's habitual second color" (R40); two-colour printing in red and black is the oldest tradition there is (R39).

#### Amber
- Id: amber
- Status: draft
- Looks like: gold at every tone, with dark words on it: lamp gold at night (`#ebb268`), a brighter, yellower gold by day (`#e7b968`) with a dark ochre edge (`#5e4926`). On lamplit, a dark bronze button with gold words and a gold edge.
- Made with: hue 72 at night, 80 by day (yellower reads as gold on paper), always bright (0.80 to 0.81), because a darker gold is brown. On light, toned and mid pages the words on it are dark (0.22) and the edge carries the 3 to 1 against the page. Yellow and amber are the colours design systems give dark words: Radix's yellow and amber are "designed for dark foreground text" (R1); Bootstrap works out dark or light words from the fill's contrast (R43); GOV.UK's focus state pairs a yellow fill with a thick black border so it shows on light and dark grounds alike (R42).

```css assemble
/* colour / accent: amber */
& { --colour-a-h: 72;
  --colour-accent-l-light: 0.81; --colour-accent-l-toned: 0.81; --colour-accent-l-mid: 0.81; --colour-accent-l-dark: 0.8; --colour-accent-h-light: 80; --colour-accent-h-toned: 80; --colour-accent-h-mid: 80; --colour-on-accent-l-light: 0.22; --colour-on-accent-l-toned: 0.22; --colour-on-accent-l-mid: 0.22;
  --colour-accent-c-light: 0.161; --colour-accent-c-toned: 0.161; --colour-accent-c-mid: 0.161; --colour-accent-c-dark: 0.161; --colour-accent-c-lamplit: 0.062;
  --colour-focus-c-light: 0.084; --colour-focus-c-toned: 0.072; --colour-focus-c-mid: 0.05; --colour-focus-c-dark: 0.092; --colour-focus-c-lamplit: 0.092;
  --colour-hover-c-light: 0.151; --colour-pressed-c-light: 0.141; --colour-hover-c-toned: 0.151; --colour-pressed-c-toned: 0.141; --colour-hover-c-mid: 0.151; --colour-pressed-c-mid: 0.141;
  --colour-hover-c-dark: 0.117; --colour-pressed-c-dark: 0.075; --colour-hover-c-lamplit: 0.062; --colour-pressed-c-lamplit: 0.062;
  --colour-edge-l-light: 0.42; --colour-edge-c-light: 0.084; --colour-edge-l-toned: 0.38; --colour-edge-c-toned: 0.076; --colour-edge-l-mid: 0.3; --colour-edge-c-mid: 0.06; --colour-edge-l-lamplit: 0.8; --colour-edge-c-lamplit: 0.161; --colour-on-accent-c-lamplit: 0.117; }
```

- Careful: on pale pages the gold button needs its dark edge: without it the fill is under 2 to 1 against the page. Never use the gold for text or thin lines on a pale page; the focus ring is the dark ochre. "Gold on dark at small sizes is often too faint" (the game-interface guide): it is for buttons and the lamp, not small text. At `strength: muted` it is a sandy gold; vivid is the brightest. The guides ban glossy gold; this is a flat lamp colour.
- Light and dark: gold at night, gold with a dark edge by day.
- Personality: dramatic, playful
- Goes with: `light: one-light`; `materials: parchment-and-ink` or `materials: metal-and-dark-glass`.
- Used on: every dark mockup (5 of 5: lantern `#f2a541`, orb `#ffb030`, lantern `#ffcf5a`, main action `#ffc93a`), where it is also the one light on the page.

#### Forest
- Id: forest
- Status: draft
- Looks like: deep green by day (`#38714e`), very deep on kraft, moss green at night (`#7a9f66`). The colour of a go button and a herb garden.
- Made with: hue 155. On dark pages it is lifted less (0.66), held to 0.13 chroma and turned towards moss (135): lifted like the others it was mint.

```css assemble
/* colour / accent: forest */
& { --colour-a-h: 155;
  --colour-accent-l-dark: 0.66; --colour-accent-h-dark: 135; --colour-accent-h-lamplit: 135;
  --colour-accent-c-light: 0.119; --colour-accent-c-toned: 0.112; --colour-accent-c-mid: 0.088; --colour-accent-c-dark: 0.13; --colour-accent-c-lamplit: 0.084;
  --colour-focus-c-light: 0.1; --colour-focus-c-toned: 0.085; --colour-focus-c-mid: 0.059; --colour-focus-c-dark: 0.15; --colour-focus-c-lamplit: 0.15;
  --colour-hover-c-light: 0.107; --colour-pressed-c-light: 0.095; --colour-hover-c-toned: 0.1; --colour-pressed-c-toned: 0.088; --colour-hover-c-mid: 0.076; --colour-pressed-c-mid: 0.064;
  --colour-hover-c-dark: 0.13; --colour-pressed-c-dark: 0.13; --colour-hover-c-lamplit: 0.084; --colour-pressed-c-lamplit: 0.084;
  --colour-edge-l-lamplit: 0.66; --colour-edge-c-lamplit: 0.13; --colour-on-accent-c-lamplit: 0.15; }
```

- Careful: green means success. The success colour is a different lightness, and always has a tick or a word.
- Light and dark: deep green by day, moss at night; on lamplit a dark green button with pale green words.
- Personality: calm, serious, friendly
- Goes with: `neutrals` stone or paper; `materials: fine-paper`.
- Used on: 2 mockups (a tutoring site's green `#1d6a43`, a soap shop's herb-green band). From research: public-service systems use a green start button.

#### Kingfisher
- Id: kingfisher
- Status: draft
- Looks like: teal-blue, a bird's wing (`#376b7b` by day), light teal at night.
- Made with: hue 220. It holds less chroma than most hues, so even vivid it is quiet.

```css assemble
/* colour / accent: kingfisher */
& { --colour-a-h: 220;
  --colour-accent-c-light: 0.087; --colour-accent-c-toned: 0.082; --colour-accent-c-mid: 0.065; --colour-accent-c-dark: 0.126; --colour-accent-c-lamplit: 0.052;
  --colour-focus-c-light: 0.073; --colour-focus-c-toned: 0.063; --colour-focus-c-mid: 0.044; --colour-focus-c-dark: 0.083; --colour-focus-c-lamplit: 0.083;
  --colour-hover-c-light: 0.079; --colour-pressed-c-light: 0.07; --colour-hover-c-toned: 0.073; --colour-pressed-c-toned: 0.065; --colour-hover-c-mid: 0.056; --colour-pressed-c-mid: 0.047;
  --colour-hover-c-dark: 0.126; --colour-pressed-c-dark: 0.126; --colour-hover-c-lamplit: 0.052; --colour-pressed-c-lamplit: 0.052;
  --colour-edge-l-lamplit: 0.72; --colour-edge-c-lamplit: 0.126; --colour-on-accent-c-lamplit: 0.105; }
```

- Careful: quiet; for a loud site pick cobalt.
- Light and dark: slate-teal by day, clear light teal at night.
- Personality: calm, serious
- Goes with: `neutrals` sage or paper; `materials: paper-and-tape`.
- Used on: 1 mockup (a field notebook's kingfisher `#1d5a72`, for things to press only).

#### Cobalt
- Id: cobalt
- Status: draft
- Looks like: printer's blue by day (`#3760ae`), ink blue on kraft, ice blue at night.
- Made with: hue 262. Blue holds the most chroma at middle and low lightness and the least near white.

```css assemble
/* colour / accent: cobalt */
& { --colour-a-h: 262;
  --colour-accent-c-light: 0.19; --colour-accent-c-toned: 0.19; --colour-accent-c-mid: 0.164; --colour-accent-c-dark: 0.139; --colour-accent-c-lamplit: 0.133;
  --colour-focus-c-light: 0.15; --colour-focus-c-toned: 0.15; --colour-focus-c-mid: 0.111; --colour-focus-c-dark: 0.056; --colour-focus-c-lamplit: 0.056;
  --colour-hover-c-light: 0.19; --colour-pressed-c-light: 0.178; --colour-hover-c-toned: 0.186; --colour-pressed-c-toned: 0.164; --colour-hover-c-mid: 0.142; --colour-pressed-c-mid: 0.12;
  --colour-hover-c-dark: 0.112; --colour-pressed-c-dark: 0.086; --colour-hover-c-lamplit: 0.133; --colour-pressed-c-lamplit: 0.133;
  --colour-edge-l-lamplit: 0.72; --colour-edge-c-lamplit: 0.139; --colour-on-accent-c-lamplit: 0.071; }
```

- Careful: a cobalt button on a cool white page is the most template look there is. Use it on a warm or toned paper, or with bands. Links default to blue in every browser, so a blue accent also reads as "a link".
- Light and dark: deep blue by day; ice blue at night, the steel-and-ice look.
- Personality: serious, playful
- Goes with: `neutrals` paper; `lettering: poster-face`.
- Used on: 2 mockups (a poetry site's print-studio look, cobalt beside two spot colours; a game-style joke site's ice-blue main action at night). From research: federal and medium blues are standard riso inks (R35).

#### Plum
- Id: plum
- Status: draft
- Looks like: red-violet by day (`#8c4387`), orchid at night. The riso pink and burgundy family, calmed down.
- Made with: hue 330.

```css assemble
/* colour / accent: plum */
& { --colour-a-h: 330;
  --colour-accent-c-light: 0.19; --colour-accent-c-toned: 0.19; --colour-accent-c-mid: 0.162; --colour-accent-c-dark: 0.19; --colour-accent-c-lamplit: 0.131;
  --colour-focus-c-light: 0.15; --colour-focus-c-toned: 0.15; --colour-focus-c-mid: 0.109; --colour-focus-c-dark: 0.1; --colour-focus-c-lamplit: 0.1;
  --colour-hover-c-light: 0.19; --colour-pressed-c-light: 0.175; --colour-hover-c-toned: 0.184; --colour-pressed-c-toned: 0.162; --colour-hover-c-mid: 0.14; --colour-pressed-c-mid: 0.118;
  --colour-hover-c-dark: 0.19; --colour-pressed-c-dark: 0.159; --colour-hover-c-lamplit: 0.131; --colour-pressed-c-lamplit: 0.131;
  --colour-edge-l-lamplit: 0.72; --colour-edge-c-lamplit: 0.19; --colour-on-accent-c-lamplit: 0.128; }
```

- Careful: vivid plum is loud; muted it is quiet and grown-up.
- Light and dark: deep plum by day, orchid at night.
- Personality: playful, dramatic
- Goes with: `neutrals` stone or night; `lettering: poster-face`.
- Used on: from research: fluorescent pink and burgundy riso inks (R35); no mockup yet.

#### Ink
- Id: ink
- Status: draft
- Looks like: the button is the ink itself: near-black with pale words by day, near-white with dark words at night. No colour at all for actions.
- Made with: the neutral's own hue and the ink's lightness; the focus ring is a separate blue, because a ring the colour of the ink is lost against the words.

```css assemble
/* colour / accent: ink */
& { --colour-a-h: var(--colour-n-h); --colour-focus-h: 262; --colour-accent-l-light: 0.27; --colour-accent-l-toned: 0.26; --colour-accent-l-mid: 0.24; --colour-accent-l-dark: 0.93; --colour-accent-l-lamplit: 0.27;
  --colour-accent-c-light: calc(var(--colour-n-c) * 1.5 / var(--colour-k)); --colour-accent-c-toned: calc(var(--colour-n-c) * 1.5 / var(--colour-k)); --colour-accent-c-mid: calc(var(--colour-n-c) * 1.5 / var(--colour-k)); --colour-accent-c-dark: calc(var(--colour-n-c) * 1.5 / var(--colour-k)); --colour-accent-c-lamplit: calc(var(--colour-n-c) * 1.5 / var(--colour-k));
  --colour-focus-c-light: 0.15; --colour-focus-c-toned: 0.15; --colour-focus-c-mid: 0.111; --colour-focus-c-dark: 0.056; --colour-focus-c-lamplit: 0.056; --colour-step-dark: -0.05;
  --colour-edge-l-lamplit: 0.93; --colour-edge-c-lamplit: calc(var(--colour-n-c) * 1.5 / var(--colour-k)); }
```

- Careful: with no colour on the buttons, the colour has to be somewhere else: bands, a bold mid ground or the materials. On its own it is the plainest option.
- Light and dark: black buttons by day, white buttons at night; on lamplit a black button with cream words and a cream edge.
- Personality: serious, playful
- Goes with: `bands` poster; `frames: torn-paper`.
- Used on: 1 mockup (a repair café: ink buttons with yellow lettering on a yellow board, and a separate blue focus ring `#1f4f86`).

### Strength
- Layer: strength
- Owns: how coloured the accent, the drawn marks and the bands are, as a share of the most each hue can hold; and on a mid page, how coloured the ground is.
- Default: natural

#### Muted
- Id: muted
- Status: draft
- Looks like: under half the colour there is room for: dusty, quiet, grown-up. Pottery glazes, an old map, a professional page.
- Made with: 0.45 of the accent's and bands' chroma; a mid ground at 0.7 of its colour.

```css assemble
/* colour / strength: muted */
& { --colour-k: 0.45; --colour-k-mid-ground: 0.7; }
```

- Careful: muted is not faded: lightness, and so contrast, stays the same. Muted colour sits back; "weakly saturated inducers produced ... background effects" (R32).
- Light and dark: on a dark page, muted is what Material asks of a dark theme: "desaturated colors" that do not vibrate against the dark (R9).
- Personality: serious, calm
- Goes with: `light: flat-and-even`; `materials: fine-paper`.
- Used on: 2 mockups (a quiet gallery, a poetry site's ink look).

#### Natural
- Id: natural
- Status: draft
- Looks like: most of the colour there is room for: clear and confident, not loud.
- Made with: 0.7 of the chroma.

```css assemble
/* colour / strength: natural */
& { --colour-k: 0.7; --colour-k-mid-ground: 1; }
```

- Careful: none; the default.
- Light and dark: on a dark page it is a little bright for a big area; bands at natural are fine, a large accent area may want muted.
- Personality: any
- Goes with: any.
- Used on: most mockups.

#### Vivid
- Id: vivid
- Status: draft
- Looks like: all of it: a poster, a fair, a game. On a mid page the ground itself turns bold (kraft becomes mustard, slate becomes denim, marigold becomes sunflower).
- Made with: the full chroma each hue holds at that lightness (capped at 0.19 for accents and 0.13 for bands); a mid ground at 1.5 times its colour.

```css assemble
/* colour / strength: vivid */
& { --colour-k: 1; --colour-k-mid-ground: 1.5; }
```

- Careful: vivid colour in large areas shouts: "reduce the saturation and the brightness to avoid the 'screaming for attention' effect" (R33). Vivid bands are deep, so they stay calm; keep vivid for small things (the accent) or for a page meant to shout. On a P3 screen the colours could go further; they are kept inside sRGB so contrast is the same on every screen.
- Light and dark: at night vivid accents are very bright; check the button is still the one bright thing.
- Personality: playful, dramatic
- Goes with: `background: pattern coloured-bands`; `lettering: poster-face`; `density: busy`.
- Used on: 4 mockups (a repair café's yellow board, a volunteer page's poster yellow and felt blue, a game-style joke site's painted world, a small shop's bands); the warm guide's "bold and flat, in big areas".

### Bands
- Layer: bands
- Owns: `--band-1`, `--band-2`, `--band-3` and `--on-band`: up to three strong grounds for whole sections, and the words on them.
- Default: none

Bands are where a second and third colour belong: big areas, each for a section, never for meaning. They are always deep (lightness 0.31 to 0.42) with pale words, except `pale`. Their chroma is the strength times a number each band carries, kept inside the gamut at every tone.

#### None
- Id: none
- Status: draft
- Looks like: no coloured bands on the page. The band names still hold a quiet trio, for a part that needs three colours (a duotone picture, a riso print): the accent's hue, the neutral's hue and the hue opposite the accent, deep, with `--on-band` words on them. "None" means none are drawn, not that the names are empty.
- Made with: the tone's band lightness and a chroma every hue holds there (0.05, times the strength), so whatever the accent and neutrals, the trio is inside sRGB and the words on it pass.

```css assemble
/* colour / bands: none */
& { --colour-b1-h: var(--colour-a-h); --colour-b2-h: var(--colour-n-h); --colour-b3-h: calc(var(--colour-a-h) + 180); --colour-b1-c: 0.05; --colour-b2-c: 0.05; --colour-b3-c: 0.05; }
```

- Careful: with no bands and a light tone, the colour is a pale ground and one accent: the template tell. Something else must carry colour. A part that draws band names as big areas (a background of coloured bands) should not be picked with `bands: none`: it would show the quiet trio, which is meant for small pictures, not whole sections.
- Light and dark: the trio is deep on every tone, like the other bands.
- Personality: any
- Goes with: `background: pattern none`.
- Used on: most mockups.

#### Poster
- Id: poster
- Status: draft
- Looks like: madder red, forest green and night blue, deep and flat: a printed poster or a market's awnings.
- Made with: hues 20, 150 and 268.

```css assemble
/* colour / bands: poster */
& { --colour-b1-h: 20; --colour-b1-c: 0.12; --colour-b2-h: 150; --colour-b2-c: 0.082; --colour-b3-h: 268; --colour-b3-c: 0.13; }
```

- Careful: three strong colours is the most a page should hold; the accent must still be the only thing you press. Under a dark lead the bands go deeper by themselves (the dark tones set them at 0.31).
- Light and dark: `#822b31`, `#275934`, `#2f4693` on light at vivid; nearly black-red, green and navy at night.
- Personality: friendly, playful
- Goes with: `background: pattern coloured-bands`; `frames: wavy-edge` or `frames: torn-paper`; `density: balanced`.
- Used on: 3 mockups (a night market's oxblood, forest and night bands; a small shop's madder and forest; a soap shop's herb-green band), and the swatch books' stand-in bands.

#### Earth
- Id: earth
- Status: draft
- Looks like: terracotta, olive and umber: a pottery, a farm, a garden in autumn.
- Made with: hues 45, 110 and 62. Earth hues hold little chroma when deep, so even vivid they stay quiet.

```css assemble
/* colour / bands: earth */
& { --colour-b1-h: 45; --colour-b1-c: 0.085; --colour-b2-h: 110; --colour-b2-c: 0.065; --colour-b3-h: 62; --colour-b3-c: 0.068; }
```

- Careful: next to a brown ink and paper neutrals it can all go brown: pick a cooler accent.
- Light and dark: terracotta, olive and umber by day; near-black versions of each at night.
- Personality: calm, friendly
- Goes with: `materials: wood-and-canvas`; `background: texture grain`.
- Used on: from research: the "nature" palettes of brown sites (R41); a small shop's umber kind colour.

#### Jewel
- Id: jewel
- Status: draft
- Looks like: plum, teal and sapphire: a painted fantasy world, stained glass.
- Made with: hues 330, 200 and 262.

```css assemble
/* colour / bands: jewel */
& { --colour-b1-h: 330; --colour-b1-c: 0.13; --colour-b2-h: 200; --colour-b2-c: 0.051; --colour-b3-h: 262; --colour-b3-c: 0.13; }
```

- Careful: the teal holds little chroma when deep, so it is the quietest of the three.
- Light and dark: rich by day, deep and glowing at night.
- Personality: dramatic, playful
- Goes with: `background: scene painted-ground`; `materials: metal-and-dark-glass`.
- Used on: 1 mockup (a game-style joke site's painted world in "purples, oranges, deep blues, greens").

#### Pale
- Id: pale
- Status: draft
- Looks like: sky, butter and mint, light, with dark words: the quiet end of bands, a tinted section or a coloured notice.
- Made with: hues 230, 95 and 160 at low chroma, near white on light pages, with dark words; on dark pages they become dim tinted bands with pale words.

```css assemble
/* colour / bands: pale */
& { --colour-b1-h: 230; --colour-b1-c: 0.026; --colour-b2-h: 95; --colour-b2-c: 0.059; --colour-b3-h: 160; --colour-b3-c: 0.065;
  --colour-band-l-light: 0.93; --colour-on-band-l-light: 0.23; --colour-band-l-toned: 0.955; --colour-on-band-l-toned: 0.22; --colour-band-l-mid: 0.93; --colour-on-band-l-mid: 0.2; --colour-band-l-dark: 0.3; --colour-on-band-l-dark: 0.95; --colour-band-l-lamplit: 0.3; --colour-on-band-l-lamplit: 0.95; }
```

- Careful: on a toned page the pale bands are lighter than the ground, so they read as sheets. That is fine; it is what a pale band is.
- Light and dark: pastel by day; at night, dim bands of the same hues.
- Personality: calm, friendly
- Goes with: `frames: hairline`; `density: clean`.
- Used on: 2 mockups (a tutoring site's one pale grey-green band, a volunteer page's coloured notices).

### Metal
- Layer: metal
- Owns: `--metal`, `--metal-deep`, `--metal-lit` and `--on-metal`: the colour of metal and gilt (frames' rings, studs and keystones, materials' plates), its shade, its highlight, and words on a plate. `--earth` and `--on-earth` are not a choice; they are set by the tone.
- Default: gold

Metal reads as metal from three things together: a colour, a darker shade and a lighter highlight in the same hue. Its middle lightness comes from the tone (0.70 light, 0.68 toned, 0.63 mid, 0.74 dark and lamplit), so it sits mid-way on every page and its shade and highlight both show. It does not follow the strength: gilt is not louder on a vivid page.

#### Gold
- Id: gold
- Status: draft
- Looks like: warm, strong gilt (`#cb931a` on a light page): a picture frame, a gilded ring, a keystone.
- Made with: hue 80 at the most chroma it holds at each lightness, up to 0.15; dark words on it.

```css assemble
/* colour / metal: gold */
& { --colour-m-h: 80; --colour-metal-dl: 0;
  --colour-metal-c-light: 0.139; --colour-metal-deep-c-light: 0.091; --colour-metal-lit-c-light: 0.09; --colour-metal-c-toned: 0.135; --colour-metal-deep-c-toned: 0.087; --colour-metal-lit-c-toned: 0.09; --colour-metal-c-mid: 0.125; --colour-metal-deep-c-mid: 0.078; --colour-metal-lit-c-mid: 0.09;
  --colour-metal-c-dark: 0.147; --colour-metal-deep-c-dark: 0.099; --colour-metal-lit-c-dark: 0.053; --colour-metal-c-lamplit: 0.147; --colour-metal-deep-c-lamplit: 0.099; --colour-metal-lit-c-lamplit: 0.053;
  --colour-on-metal-l-light: 0.18; --colour-on-metal-l-toned: 0.18; --colour-on-metal-l-mid: 0.18; --colour-on-metal-l-dark: 0.18; --colour-on-metal-l-lamplit: 0.18; }
```

- Careful: next to the amber accent it is the same family: keep gold for decoration and amber for things you press, or pick brass. The guides ban glossy gold; this is a flat colour with a drawn shade and highlight, not a gradient sheen.
- Light and dark: the same gold on every tone; a little brighter at night.
- Personality: dramatic, playful
- Goes with: `frames: gilded-dark`; `materials: metal-and-dark-glass`.
- Used on: a game-style joke site's gilded rings and keystone; the gilded-dark frames.

#### Brass
- Id: brass
- Status: draft
- Looks like: a greener, quieter gold: an instrument, a ship's fitting, an old lamp.
- Made with: hue 90, up to 0.10 chroma, a little darker than gold.

```css assemble
/* colour / metal: brass */
& { --colour-m-h: 90; --colour-metal-dl: -0.03;
  --colour-metal-c-light: 0.1; --colour-metal-deep-c-light: 0.084; --colour-metal-lit-c-light: 0.06; --colour-metal-c-toned: 0.1; --colour-metal-deep-c-toned: 0.08; --colour-metal-lit-c-toned: 0.06; --colour-metal-c-mid: 0.1; --colour-metal-deep-c-mid: 0.071; --colour-metal-lit-c-mid: 0.06;
  --colour-metal-c-dark: 0.1; --colour-metal-deep-c-dark: 0.085; --colour-metal-lit-c-dark: 0.06; --colour-metal-c-lamplit: 0.1; --colour-metal-deep-c-lamplit: 0.085; --colour-metal-lit-c-lamplit: 0.06;
  --colour-on-metal-l-light: 0.18; --colour-on-metal-l-toned: 0.18; --colour-on-metal-l-mid: 0.18; --colour-on-metal-l-dark: 0.18; --colour-on-metal-l-lamplit: 0.18; }
```

- Careful: on a mid board it is close to the board; its shade carries it.
- Light and dark: olive-gold by day, pale brass at night.
- Personality: calm, serious
- Goes with: `frames: hairline`; `materials: fine-paper`.
- Used on: an observatory's brass instruments (the almanac plate starting point).

#### Silver
- Id: silver
- Status: draft
- Looks like: pale, cool and nearly grey: steel, tin, pewter.
- Made with: hue 250 at a whisper of chroma, a step lighter than gold.

```css assemble
/* colour / metal: silver */
& { --colour-m-h: 250; --colour-metal-dl: 0.05;
  --colour-metal-c-light: 0.012; --colour-metal-deep-c-light: 0.01; --colour-metal-lit-c-light: 0.007; --colour-metal-c-toned: 0.012; --colour-metal-deep-c-toned: 0.01; --colour-metal-lit-c-toned: 0.007; --colour-metal-c-mid: 0.012; --colour-metal-deep-c-mid: 0.01; --colour-metal-lit-c-mid: 0.007;
  --colour-metal-c-dark: 0.012; --colour-metal-deep-c-dark: 0.01; --colour-metal-lit-c-dark: 0.007; --colour-metal-c-lamplit: 0.012; --colour-metal-deep-c-lamplit: 0.01; --colour-metal-lit-c-lamplit: 0.007;
  --colour-on-metal-l-light: 0.18; --colour-on-metal-l-toned: 0.18; --colour-on-metal-l-mid: 0.18; --colour-on-metal-l-dark: 0.18; --colour-on-metal-l-lamplit: 0.18; }
```

- Careful: on a cool white page it can look like a disabled control; give it its shade.
- Light and dark: cool grey by day, near white at night.
- Personality: serious, calm
- Goes with: `materials: metal-and-dark-glass`; the steel-and-ice look.
- Used on: the steel look of a game-style joke site.

#### Iron
- Id: iron
- Status: draft
- Looks like: dark blue-grey with pale words: a workshop, a pegboard hook, a cast plate.
- Made with: hue 245, a little chroma, 0.22 darker than gold; pale words on it.

```css assemble
/* colour / metal: iron */
& { --colour-m-h: 245; --colour-metal-dl: -0.22;
  --colour-metal-c-light: 0.018; --colour-metal-deep-c-light: 0.015; --colour-metal-lit-c-light: 0.011; --colour-metal-c-toned: 0.018; --colour-metal-deep-c-toned: 0.015; --colour-metal-lit-c-toned: 0.011; --colour-metal-c-mid: 0.018; --colour-metal-deep-c-mid: 0.015; --colour-metal-lit-c-mid: 0.011;
  --colour-metal-c-dark: 0.018; --colour-metal-deep-c-dark: 0.015; --colour-metal-lit-c-dark: 0.011; --colour-metal-c-lamplit: 0.018; --colour-metal-deep-c-lamplit: 0.015; --colour-metal-lit-c-lamplit: 0.011;
  --colour-on-metal-l-light: 0.96; --colour-on-metal-l-toned: 0.96; --colour-on-metal-l-mid: 0.96; --colour-on-metal-l-dark: 0.96; --colour-on-metal-l-lamplit: 0.96; }
```

- Careful: on a dark page it is only a step off the ground; its highlight carries it.
- Light and dark: dark iron by day, a lighter gunmetal at night.
- Personality: serious, playful
- Goes with: `frames: riveted-metal`; `frames: torn-paper`.
- Used on: a repair café's hooks and tools (the repair café starting point).

## Starting points

### Warm
- Id: warm
- Picks: tone: light; neutrals: paper; accent: brick; strength: vivid; bands: poster
- Personality: friendly, playful
- Looks like: cream paper, a bold brick red for actions, and deep bands of red, green and blue for whole sections. "Bold and flat, in big areas. Not pastel, not white with one accent."
- Used on: the warm guide; a soap shop (cream, ember, herb-green band) and a volunteer page (cream, red, poster yellow and felt blue).

### Artistic
- Id: artistic
- Picks: tone: light; neutrals: stone; accent: brick; strength: natural; bands: none
- Personality: calm, serious
- Looks like: a near-grey page and one seal red. The colour comes from the work shown, so the page itself stays neutral.
- Used on: the artistic guide ("a neutral base; colour comes from the content", 7 of 7 sites); a poetry site's ink look (ink grey and one red seal).

### Professional
- Id: professional
- Picks: tone: light; neutrals: stone; accent: kingfisher; strength: muted; bands: none
- Personality: serious, calm
- Looks like: cool white and one quiet teal-blue, nothing else. Even and exact.
- Used on: the professional guide ("one institutional colour on a white or near-white ground", 10 of 12 sites).

### Civic
- Id: civic
- Picks: tone: light; neutrals: stone; accent: forest; strength: natural; bands: none
- Personality: serious
- Looks like: a plain, cool, very clear page with a green go button: the look of a public service, where being read by everyone matters more than being remembered.
- Used on: from research: public-service design systems grade every colour for contrast and keep colour for actions (R13); a tutoring site's green on white is close.

### Sorcery
- Id: sorcery
- Picks: tone: lamplit; neutrals: night; accent: amber; strength: natural; bands: none
- Personality: dramatic
- Looks like: a night-blue room, dim warm parchment with dark ink, and gold as the one light: the main button is dark bronze, lettered and rimmed in lamp gold, so it shows on the parchment and glows at the rim on the night-blue ground. "Mostly dark, in two or three hues, with the light as the one bright thing."
- Used on: the sorcery guide (dark, painterly old wizard art); a dark, painterly joke site (night-blue hall, parchment, gold orb). For its wine room, change the neutrals: `{"start": "sorcery", "neutrals": "wine"}`.

### Gilded dark
- Id: gilded-dark
- Picks: tone: dark; neutrals: paper; accent: amber; strength: vivid; bands: jewel
- Personality: dramatic, playful
- Looks like: dark brown panes, bright gold for the main action, and jewel-coloured bands for the painted world behind. The steel-and-ice look is `{"start": "gilded-dark", "neutrals": "night", "accent": "cobalt"}`.
- Used on: the game-interface guide; a game-style joke site in both its looks (gold and steel).

### Lantern fair
- Id: lantern-fair
- Picks: tone: lamplit; neutrals: wine; accent: amber; strength: natural; bands: poster
- Personality: dramatic, friendly
- Looks like: an oxblood night market: canvas and paper tags, lantern amber, and deep bands of red, green and night for the stalls.
- Used on: a night-market mockup; two versions of a small shop of handmade goods with a dark lead.

### Almanac plate
- Id: almanac-plate
- Picks: tone: light; neutrals: night; accent: brick; strength: natural; bands: none; metal: brass
- Personality: calm, serious
- Looks like: blue-grey star-chart paper, near-black ink, brass for the instruments and a red torch for the one button. Red because a dim red light keeps the eye used to the dark (R38).
- Used on: an observatory mockup (sheets that stay light under a day or night sky, torch red `#9a2b1f`).

### Catalogue of glazes
- Id: catalogue-of-glazes
- Picks: tone: toned; neutrals: clay; accent: brick; strength: muted; bands: none
- Personality: calm
- Looks like: a quiet bisque page and iron red, nothing else; the colour is in the pots.
- Used on: a quiet gallery of pots ("a toned paper, not a pale one and not a bold one").

### Field journal
- Id: field-journal
- Picks: tone: toned; neutrals: sage; accent: kingfisher; strength: natural; bands: none
- Personality: calm, friendly
- Looks like: notebook paper with green in it, green-black ink, and a kingfisher blue for things to press.
- Used on: a field-notebook mockup; a tutoring site and a soap shop share its green-black ink.

### Repair cafe
- Id: repair-cafe
- Picks: tone: mid; neutrals: marigold; accent: ink; strength: vivid; bands: poster; metal: iron
- Personality: playful, friendly
- Looks like: a sunflower-yellow board, black buttons, iron hooks, and a red band for the banner. Busy, bright and made by hand.
- Used on: a repair-café mockup (a sunflower pegboard `#f4b62f`; here `#f5b42e`). With paper neutrals it was mustard (`#cca86a`); the marigold neutral was added so a mid ground could be sunflower and still hold dark words, a dark focus ring and black buttons.

## Swatch book

`tests/parts/colour.html` shows every option of every layer, then every starting point. Each swatch is a small page: the ground, a sheet with a heading, body text, soft text, a line, a button in the accent with its edge, the three status colours, a focus ring and a drawn mark on the ground, a metal plate and a kraft tag with words on them, and the bands where they are on. The colour part sets the shared names itself, so its swatches do not use tokens.css's stand-ins, and the light-and-dark pairing of the other books is replaced by the tone: each option is drawn at all five tones, and each tone and starting point beside its other look. The page is built by `tests/parts/source/colour.py` from `colour-template.html` beside it; run `python3 colour.py ../colour.html` there to rebuild it, which also checks every combination in Python first.

Its test works out every combination of the layers (5 tones, 7 neutrals, 7 accents, 3 strengths, 5 bands and 4 metals: 14,700), reads the colours the browser paints for each, and fails if any of these pairs misses: words on the ground, ink on a sheet and on a raised sheet, soft text on a sheet, words on the accent and on its hover and pressed colours, the three status colours on a sheet, words on each band, and words on metal and on earth, at 4.5 to 1; the accent against the ground and against a sheet at 3 to 1, by its fill or its edge, whichever is better; and the focus ring against the ground at 3 to 1. It also fails if any colour falls outside sRGB, or if `--texture-rgb` does not resolve.

## Not covered yet

- **Buttons in the other parts** draw only `--accent` so far. `--accent-edge` is now a shared name; each part's turn adds the edge to its buttons.
- **The page checker cannot read `oklch()` colours.** `audit` and `check` measure contrast from colours written as `rgb()`; a colour the browser keeps as `oklch(...)` is skipped without a word. The swatch book writes each swatch's colours back as `rgb()` so it can be audited; a real site made with this part needs the checker fixed first.
- **A second accent with a job of its own** (the field notebook's rust for marks only, an observatory's lamp orange). Here `--mark` takes the neutral's hue; a mark in another hue is a site's own decision.
- **Colour sets for things** (a rarity ladder, dye colours for kinds of ware, glazes, coloured notices). They are content, kept by the site; they should take their lightness from the tone so they pass, and that rule is not written yet.
- **A painted or photographed ground** (a sky, a painted world): the light and background parts draw them; this part only gives the colours.
- **APCA.** WCAG 2's ratio is the rule the skill checks; APCA says it misjudges dark pages (R28). The dark tones are kept well above the minimum for that reason, but nothing measures APCA yet.
- **Wide-gamut (P3) colour.** Everything is kept inside sRGB, so vivid is not as vivid as a modern screen could show.
- **How it looks on a whole page.** The swatches are small. No mockup has yet been built from these picks; the first should be one of the existing looks rebuilt from its starting point and put beside the original.

## Sources

Read on 2026-10-07. Six kinds of source, as the research job asks: design-system documents (R1 to R13), colour science and CSS (R14 to R19), craft writing by designers (R20 to R26), dark pages (R9, R10, R27, R28), evidence for and against colour harmony (R31 to R34), and traditions people recognise (R35 to R41). WCAG (R29, R30) for the minimums. For gold buttons on pale pages, added later the same day: R1, R29, R42, R43. Pages that would not open: m3.material.io (an archived page and Material's code were used instead), the Refactoring UI book and its Medium summary (403), a critique of 60-30-10 (403), and the contrast table on Carbon's page (garbled).

- R1 Radix Colors, understanding the scale: radix-ui.com/colors/docs/palette-composition/understanding-the-scale
- R2 Radix Colors, composing a palette: radix-ui.com/colors/docs/palette-composition/composing-a-palette
- R3 Radix Themes, colour: radix-ui.com/themes/docs/theme/color
- R4 Tailwind CSS v4 release: tailwindcss.com/blog/tailwindcss-v4
- R5 Tailwind colours: tailwindcss.com/docs/colors
- R6 Material HCT source with comments: developer.android.com (material-hct-source reference)
- R7 Material colour utilities (code): github.com/material-foundation/material-color-utilities
- R8 Android Material 3 colour guide: developer.android.com/design/ui/mobile/guides/styles/color
- R9 Material dark theme (archived): web.archive.org copy of material.io/design/color/dark-theme.html
- R10 Material Android dark theme: github.com/material-components/material-components-android/blob/master/docs/theming/Dark.md
- R11 IBM Carbon colour: carbondesignsystem.com/elements/color/overview/
- R12 Adobe Leonardo: leonardocolor.io
- R13 US Web Design System, colour tokens: designsystem.digital.gov/design-tokens/color/overview/
- R14 Evil Martians, OKLCH in CSS: evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl
- R15 MDN, oklch(): developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch
- R16 CSS Color 4: w3.org/TR/css-color-4/
- R17 Björn Ottosson, Oklab: bottosson.github.io/posts/oklab/
- R18 Lea Verou, LCH colours in CSS: lea.verou.me/blog/2020/04/lch-colors-in-css-what-why-and-how/
- R19 Josh Comeau, colour formats: joshwcomeau.com/css/color-formats/
- R20 Stripe, accessible colour systems: stripe.com/blog/accessible-color-systems
- R21 Linear, how we redesigned the Linear UI: linear.app/now/how-we-redesigned-the-linear-ui
- R22 Refactoring UI, building your colour palette: refactoringui.com/previews/building-your-color-palette
- R23 Erik Kennedy, colour in UI design: learnui.design/blog/color-in-ui-design-a-practical-framework.html
- R24 Anthony Hobday, add colour to grey backgrounds: anthonyhobday.com/sideprojects/visualtechniques/techniques/colour/add-colour-to-grey-backgrounds
- R25 Penpot, saturating greys: penpot.app/courses/block-1/saturating-grays/
- R26 OneSignal, 11 shades of grey: onesignal.com/blog/11-shades-of-gray-a-color-system-story/
- R27 Apple Human Interface Guidelines, dark mode: developer.apple.com/design/human-interface-guidelines/dark-mode
- R28 APCA, why APCA: git.apcacontrast.com/documentation/WhyAPCA
- R29 WCAG 2.2, 1.4.11 non-text contrast: w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- R30 WCAG 2.2, 1.4.3 contrast (minimum): w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- R31 Mahyar, Cheung, Westland and Henry (2007), complementary colours and colour wheels: eprints.whiterose.ac.uk/83854/
- R32 Dresp-Langley and Reeves (2014), colour and figure-ground: frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.01136/full
- R33 EU data-visualisation guide, colour harmonies: data.europa.eu/apps/data-visualisation-guide/colour-harmonies
- R34 Paige Brunton, the 60-30-10 rule for web designers: paigebrunton.com/blog/60-30-10-color-rule-for-web-designers/
- R35 Riso ink colours (Matt DesLauriers' list): unpkg.com/riso-colors/riso-colors.json
- R36 4over4, colours for kraft printing: 4over4.com/faqs/general/what-colors-work-best-for-kraft-printing
- R37 Mental Floss, why blackboards are green: mentalfloss.com/article/504699/why-are-so-many-blackboards-green
- R38 US National Park Service, dark adaptation and red light: nps.gov/articles/dark-adaptation-of-the-human-eye-and-the-value-of-red-flashlights.htm
- R39 Wikipedia, rubric: en.wikipedia.org/wiki/Rubric
- R40 Gwern, red: gwern.net/red
- R41 HubSpot, brown websites: blog.hubspot.com/website/brown-websites
- R42 GOV.UK Design System, focus states: design-system.service.gov.uk/get-started/focus-states/ ("The yellow has a high contrast with dark backgrounds and the thick black border has a high contrast against light backgrounds")
- R43 Bootstrap, the color-contrast function: getbootstrap.com/docs/5.3/customize/sass/ (returns light, dark or black words from the fill's WCAG contrast)

What the research settled, and how many kinds of source agreed:

- **Work colours out from a few inputs, not by hand** (4 of 6 kinds: design systems R2, R3, R6, R7, R12, R13; craft R20, R21; colour science R14; dark pages R27). Refactoring UI disagrees in part: "you can't rely purely on math" (R22). So the numbers here are worked out, and the swatch book is there to be looked at.
- **Contrast comes from a gap in perceived lightness** (3 of 6: R6, R13, R20; R16, R17; R29, R30).
- **Greys carry a little of a hue, matched to or set against the accent** (3 of 6: R2, R5, R7; R22, R24, R25, R26; and the mockups, whose dark grounds always had a hue).
- **One accent; extra colour only in large, quiet areas or for meaning** (4 of 6: R11; R23; R33; R39, R40). Colour-wheel harmony did not hold up: colour wheels disagree with each other, and "opposite relationships in CIELAB colour space do not accurately predict for complementary relationships" (R31); a designer gives split-complementary schemes "about 0%" predictive value (R23). So no layer here is chosen by harmony; the neutrals are matched by hue nearness (as Radix does), and the bands are named sets taken from traditions.
- **Dark pages are not black, raise with lighter surfaces, and calm their colours** (2 of 6, with every dark mockup: R9, R10, R27; R28).
- **A yellow or gold fill takes dark words, and an edge where the ground is pale** (3 of 6: R1, R43; R42; R29, which notes that words alone already mark a button).
- **Mid-tone grounds want dark inks only** (1 of 6: R36, with the two mid-tone mockups). Systems do not cover them (none of R1 to R13 has one).
