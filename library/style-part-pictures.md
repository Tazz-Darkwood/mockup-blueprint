---
name: Picture style (a part guide)
summary: How pictures and icons are drawn - the technique of the drawings, what is done to a photograph or drawing after it is made, how icons are drawn and how heavy every drawn line is, how people are shown, and what fills a photograph's place in a mockup - in layers that switch on their own, from flat shapes and plain outline icons to old painted pictures, engravings and real photographs in two inks. Every layer draws with the shared colour names, works on a light page and a dark one, and can be picked with any feel guide. Also the rules every picture keeps whatever is picked - alt text, no words inside pictures, scripts that redraw the art, stand-ins said as stand-ins, size and loading, licences, and never imitating a living artist.
kind: part
detect: []
checked: 2026-10-07
source: research online (six kinds of source, listed under Sources), the pictures of 15 mockups made with the skill and the scripts that drew them, and the feel guides named in each option
---

# Picture style

A part guide. It covers how the pictures and icons on a page are drawn: the illustration technique, what is done to a photograph or a drawing after it is made, how icons are drawn, the weight of every drawn line, how people are shown, and what stands in for a photograph that does not exist yet. It is made of six layers, each one decision that switches on its own: **technique**, **treatment**, **icons**, **stroke**, **figures** and **stand-in**. A site picks a starting point whole, or a starting point with one layer changed, in its own guide and in the blueprint as `project.style.parts`: `{"pictures": "repair-cafe"}`, or `{"pictures": {"start": "warm", "icons": "outline"}}`. The pick wins over the feel guide for the pictures only. The general guide's accessibility minimums (contrast, text size, tap size) still hold whatever is picked, and so do the rules under "Every picture, whatever is picked" below.

**This part draws the picture, not what is round it.** The frame round a picture is the frames part; its mask or silhouette (a blob, an arch, a circle) is corners and shapes; what lies behind the sections is the background; the shadow a cut-out casts is the light part's (`--drop-low`); and every colour is the colour part's. Pictures here are coloured only with the shared colour names (see "Parts, layers and the shared colour names" in the general guide), and a photograph's duotone or riso inks are shared names too, so a picture never brings a colour the page does not have. Where the background part draws signs and small things to find on the ground, it decides how many and where; this part decides how they are drawn (their technique and line), so a site's signs and its pictures look made by one hand.

**Pictures on a dark page.** A photograph never changes with the page. A drawing made from the band colours (`--band-1` to `--band-3`, deep on both pages) and the pale on them (`--on-band`, pale on both) stays the same picture on a light page and a dark one: a painting hung on a dark wall. A drawing made in the page's own ink on its own paper (`--ink` on `--surface`) turns over on a dark page, like chalk on a board. Each technique says which it does; the flat, cut-paper and painted techniques stay put, the line techniques turn over. The swatch book shows both.

**One picture style per site.** One technique for every drawing, one icon set, one line weight: the general guide's "one radius, one shadow, one border, one icon set" holds for pictures too, and every design system read for this guide asks for it (R1, R3, R5: "one visual family"). Photographs and drawings can live together when each has its own job: photographs for the real people and things, drawings for what a photograph cannot show (the soap shop drew the herbs in each bar; the tutor site would photograph the tutor).

## Every picture, whatever is picked

These hold on every site and every option below. `check` and `audit` test the first two.

1. **Every picture has a text alternative, or is marked as decoration** (WCAG 1.1.1, R7). An `<img>` has `alt`; an inline `<svg>` that carries meaning has `role="img"` and an `aria-label` or a `<title>` (R10); a picture that adds nothing (a sign on the ground, a flourish, an icon beside its own word) has `alt=""`, or `aria-hidden="true"` and `focusable="false"` on an inline SVG (R8). An icon that is the only content of a button names the action, not the drawing: "Search", not "magnifying glass" (R9). The quiet gallery's pots carry `role="img"` with a title that says what the pot is; the repair café's fixers say what they are doing; every sign and find on the detailed grounds is hidden.
2. **No words inside a picture.** Labels, prices, names and numbers are real text laid over or beside the picture, so they can be read aloud, translated, enlarged and measured (WCAG 1.4.5, R7; Material's illustration guidance, R3). The ant game's nest drawing has its room names baked into the SVG file; on the real site they become text over it. Two exceptions: a logo, and marks that are pure decoration (the numbers on a drawn tape measure), which go in a CSS background or an `aria-hidden` drawing so `audit` does not count them as text (the repair café found this).
3. **A picture drawn by script can be drawn again.** The script lives beside the art it draws, in the site's `art/` folder (`art/make-scene.py`, or `art/source/ground.py` writing `art/ground.svg`), uses only the standard library, fixes its random seed so the same file comes out every time, and says in its first lines what it draws and how to run it. The blueprint's `picture.made` names the script. Every scene on the mockups so far was made this way (the sorcery joke site, both faire shops, the game-style site, the repair café's pegboard), and it is what let each be redrawn three times after the owner's critique. A drawing pasted inline once, with no script, is fine for something small (an icon, a pot); say so in `made`.
4. **A stand-in is said to be one.** Wherever a drawing or a box stands for a photograph or a painting that does not exist yet, the blueprint says so in `picture.made` ("a stand-in: a photograph of the real fixers replaces it"), and a question asks who will take or paint it and when. The stand-in layer below decides what the page itself says.
5. **Pictures cost little and never move the page.** Every `<img>` has `width` and `height`, so the browser saves its space before it loads (R26); a picture box has an `aspect-ratio`. Pictures below the first screen take `loading="lazy"`; the picture in the first screen never does, and takes `fetchpriority="high"` (R27, R28). Photographs are served as AVIF or WebP with a JPEG fallback in `<picture>`, at several widths with `srcset` and `sizes` (R29, R30). A drawing used more than once is a `<symbol>`, drawn once and placed with `<use>`; filters are shared. SVG files go through SVGO before the site is built (R31). Judgement: a drawing over about 150 KB as SVG (the faire shop's scene was 600 KB) is loaded as an `<img>` from a file, never inline, and is a candidate for a WebP of the same picture on a phone.
6. **Never imitate a named living artist.** A style itself is not property in law (R32), but drawing "in the style of" a living illustrator takes the thing they make their living by, and illustrators' own codes ask that it not be done (R33). Describe a style by its technique, its era and its tradition ("painted fantasy pictures of the 1970s and 80s", "a Japanese ink painting"), never by a person's name. Never put the pictures a guide was studied from into a site: they are looked at, not used (the sorcery guide and the job notes on research say the same).
7. **Every reused picture has its licence written down.** In the blueprint, beside the picture: who made it, where it came from, the licence, and what was changed (Creative Commons' "title, author, source, licence", R35). Public domain and CC0 need no credit but get one anyway; CC BY needs it; "non-commercial" licences do not suit a shop; Wikimedia Commons files are checked one by one (R36); the Unsplash licence allows commercial use without credit but not selling the photograph itself (R37). A photograph of a person also needs that person's agreement to be shown, and of a child, a parent's (the warm and education guides).
8. **A picture carries something.** People look at pictures of real people and real things and skip pictures put in "to jazz up" a page (R24). Design systems ask the same of illustration: it supports the words, never pure decoration (R1), and carries nothing the words do not also say (R2). Decoration is the background part's job and is hidden from screen readers.

## How it is built

A picture is a `.picture`: a `<figure>` holding the picture and perhaps its caption, or the `<img>` or `<svg>` itself. Drawings are inline SVG, or symbols placed with `<use>`, coloured by the Base palette's classes, which read the shared names; or SVG files loaded as images (which cannot read the page's custom properties: draw those in their final colours, or as masks the way the background part does). Every class and filter id this part uses begins `pictures-`, so a site's drawing script writes `class="pictures-deep-2"` and `filter="url(#pictures-pen)"`, and `style css` supplies both.

```html
<figure class="picture"><img src="pictures/wheel-900.jpg" srcset="pictures/wheel-600.jpg 600w, pictures/wheel-900.jpg 900w"
  sizes="(min-width: 48rem) 50vw, 100vw" width="900" height="600" alt="Two clay-covered hands shaping a pot on a wheel" loading="lazy"></figure>
<figure class="picture"><svg viewBox="0 0 320 220" role="img" aria-label="Drawing of a jug and a cup on a table"><use href="#jug"/></svg>
  <figcaption>Drawn for now: a photograph of the studio table goes here.</figcaption></figure>
<p><svg class="icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><use href="#icon-basket"/></svg> Basket</p>
```

Three things learned building the swatch book and the stylesheet. **A drawing used as a `<symbol>` takes its colours by inheritance:** custom properties and `fill` set on the `<use>` reach inside it, and so do rules with a single class (`.pictures-deep-2`), but a rule with an ancestor in it (`.dark .pictures-deep-2`) does not, because inside a `<use>` the drawing's ancestors are the symbol's. So colour the drawing with plain classes whose values are shared names, and switch a style with a custom property (the icons do this). **An SVG gradient, pattern or clip defined inside a swatch loses its id** when `swatches.js` copies it for the dark page, and an SVG gradient's `stop-color` reads the custom properties where the gradient is defined, not where it is used: shade drawings with flat shapes, opacity and `color-mix()`, and keep clips and filters in one `<defs>` at the top of the page. **For the same reason a treatment's inks follow the page, not the section:** the treatments are SVG filters whose colours (`flood-color`) are set by CSS on the filter in `parts.defs.html`, so they take the root's colours. That is what a site wants (one set of inks for the page), and it is why a filter can act on the picture itself and keep any shape the shapes part gives it, with no extra markup. The swatch book shows the same looks with blend layers over the picture, because it shows a light and a dark page side by side on one page, which a filter cannot.

## Choosing

Start from a starting point (below), then change a layer if the brief asks for it.

| Starting point | What it feels like | Suits best | Fights |
|---|---|---|---|
| Warm | Cut paper and marker, friendly people; photographs of the real people later | Warm; a community group | Professional, a dark lead |
| Artistic | One made picture in brush and ink, a lot left empty | Artistic; words as the content | A shop's product pages |
| Professional | Real, named people photographed; plain outline icons | Professional; education | Anything hand-made |
| Civic | Few pictures, each carrying information; solid icons with labels | A public service, a council, a charity's forms | A brand that wants to charm |
| Sorcery | An old painted picture with a robed figure; every mark shows the hand | The sorcery guide | Anything clean or official |
| Gilded dark | A bright painted world, chunky solid icons, heroes against the light | The game-interface guide | Calm or official sites |
| Lantern fair | Cut-paper lanterns and dishes, chalk signs, no people | A night market, a fair, a dark shop of handmade things | Daytime services |
| Almanac plate | Fine ruled lines, like a printed star chart | A society, an observatory, a garden | Shops (products need photographs) |
| Catalogue of glazes | Each piece drawn flat in its own colour; no icons | A maker's portfolio | A page with many controls |
| Field journal | A coloured sketch taped in, one thing ringed in pencil | A walking club, a naturalist, a garden | A dark lead |
| Repair cafe | Marker drawings with flat colour, friendly people at a table | A bright community page, busy and hand-made | Professional; a calm brief |

How to choose:

- **First ask whether the real site will have photographs.** The warm, professional, education and sales guides all want real photographs of the real people or the real goods (10 of 12, 11 of 12, 10 of 12 and 7 of 7 sites studied). If it will, the technique for the photographs is `photograph`, and the drawings in the mockup are stand-ins: pick the stand-in layer with care. If it will not (a joke site, a game, a society with no photographer), the drawing is the real picture and gets the care a painting would.
- **The technique comes from what the site is made of.** The general guide asks every brief what the organisation is made of; the picture is drawn in that: cut paper for a group that pins paper to a wall, marker for a pegboard, pencil and wash for a notebook, flat glaze colours for a potter, paint for a fantasy world.
- **Icons are chosen with the lettering.** A hairline icon beside a heavy poster face looks lost; a bold filled icon beside a fine book serif looks shouted. The stroke layer sets both icons and drawn lines, so they agree.
- **Change single layers.** A warm site that needs an official form keeps its cut-paper pictures and takes `icons: outline`. A professional site with no photographer yet keeps `technique: photograph` and `stand-in: brief-box`, which tells everyone what to shoot.

## Base

What every pick needs, lifted by `style css` whatever is picked: the picture box (`.picture`, a figure or the picture itself), the place the treatment layer fills, the drawing palette (one plain class per colour, `.pictures-sky` to `.pictures-hair-3`, which the techniques and figures draw with), the line drawing at the stroke layer's weight, and the icon geometry the icons and stroke layers set. The three filters most options share (a pen, a finer pen for icons, and a wash) go in `parts.defs.html`. A site's drawing script writes its SVG with these class names and filter ids, so the stylesheet colours it.

```css assemble
/* pictures, base. A picture is .picture: a <figure> holding an <img>, an <svg> or a <picture> (and perhaps a <figcaption>),
   or the <img> or <svg> itself. Its shape (radius, mask, ratio) is the shapes part's, its frame the frames part's, its shadow the light part's. */
.picture { margin: 0; }
.picture > picture { display: block; }
.picture > :is(img, svg, video), .picture > picture > img { display: block; width: 100%; height: auto; }
.picture > figcaption { margin-top: var(--gap-inside, 0.5rem); }
/* the treatment layer fills --pictures-treatment with an SVG filter; it acts on the picture itself, so it follows any shape put on it */
:is(.picture > :is(img, svg, video), .picture > picture > img, :is(img, svg, video).picture) { filter: var(--pictures-treatment, none); }
.pictures-plain { --pictures-treatment: none; }   /* a product photograph or a crowd: shown as taken, whatever the treatment */
& { --pictures-shade: var(--shade, rgb(var(--shadow-rgb)));
  --pictures-wash-base: light-dark(var(--surface), color-mix(in oklab, var(--ink-soft) 50%, var(--surface)));   /* tints stay visible under pale lines on a dark page */
  --pictures-icon-ground: var(--ground);
  /* the two inks a duotone, halftone or riso prints with: deep and pale on both pages, so a treated picture does not flip.
     A site with bands: none still has two, from the accent and the page. */
  --pictures-dark-ink: var(--band-3, color-mix(in oklab, var(--accent) 55%, rgb(var(--shadow-rgb))));
  --pictures-paper-ink: var(--on-band, light-dark(var(--surface), var(--ink))); }

/* the drawing palette: one plain class per colour, so each reaches inside a <use> (a selector with an ancestor in it does not).
   Deep band colours and their pale stay put on a dark page; the page's own ink and paper turn over. */
.pictures-sky   { fill: color-mix(in oklab, var(--on-band) 86%, var(--mark)); }
.pictures-sun   { fill: color-mix(in oklab, var(--mark) 50%, var(--on-band)); }
.pictures-hill  { fill: color-mix(in oklab, var(--band-2) 30%, var(--on-band)); }
.pictures-earth { fill: color-mix(in oklab, var(--mark) 72%, var(--pictures-shade)); }   /* a table, the ground */
.pictures-warm  { fill: color-mix(in oklab, var(--mark) 55%, var(--on-band)); }          /* bare clay, wood, a basket */
.pictures-leaf  { fill: color-mix(in oklab, var(--band-2) 62%, var(--on-band)); }
.pictures-deep-1 { fill: var(--band-1); }
.pictures-deep-2 { fill: var(--band-2); }
.pictures-deep-3 { fill: var(--band-3); }
.pictures-paper { fill: var(--surface); }
/* the same colours as lines (the width is the drawing's own stroke-width attribute) */
:is(.pictures-line-1, .pictures-line-2, .pictures-line-3, .pictures-line-earth) { fill: none; stroke-linecap: round; stroke-linejoin: round; }
.pictures-line-1 { stroke: var(--band-1); }
.pictures-line-2 { stroke: var(--band-2); }
.pictures-line-3 { stroke: var(--band-3); }
.pictures-line-earth { stroke: color-mix(in oklab, var(--mark) 72%, var(--pictures-shade)); }
/* pale tints under a line drawing (ink line, pencil) */
.pictures-tint-1    { fill: color-mix(in oklab, var(--band-1) 42%, var(--pictures-wash-base)); }
.pictures-tint-2    { fill: color-mix(in oklab, var(--band-2) 42%, var(--pictures-wash-base)); }
.pictures-tint-sun  { fill: color-mix(in oklab, var(--mark) 45%, var(--pictures-wash-base)); }
.pictures-tint-warm { fill: color-mix(in oklab, var(--mark) 38%, var(--pictures-wash-base)); }
.pictures-tint-leaf { fill: color-mix(in oklab, var(--band-2) 30%, var(--pictures-wash-base)); }
.pictures-tint-earth { fill: color-mix(in oklab, var(--mark) 26%, var(--pictures-wash-base)); }
/* people: skin and hair in a range of tones mixed from the mark, so people are many on either page; clothes are deep colours, never the accent */
.pictures-skin-1 { fill: color-mix(in oklab, var(--mark) 22%, var(--on-band)); }
.pictures-skin-2 { fill: color-mix(in oklab, var(--mark) 58%, var(--on-band)); }
.pictures-skin-3 { fill: color-mix(in oklab, var(--mark) 68%, var(--pictures-shade)); }
.pictures-hair-1 { fill: color-mix(in oklab, var(--mark) 22%, var(--pictures-shade)); }
.pictures-hair-2 { fill: color-mix(in oklab, var(--on-band) 72%, var(--pictures-shade)); }   /* grey */
.pictures-hair-3 { fill: color-mix(in oklab, var(--on-band) 52%, var(--mark)); }
/* a drawing in lines only, at the stroke layer's weight */
.pictures-line-art { fill: none; stroke: var(--ink); stroke-width: calc(var(--pictures-sw, 2) * 1.1); stroke-linecap: round; stroke-linejoin: round; }
.pictures-line-art :is(path, circle, ellipse, line, polyline) { vector-effect: var(--pictures-ve, none); }   /* inline drawings only: it does not reach into a <use> */

/* icons: one geometry on a 24 grid. The <svg class="icon"> sits beside its word (aria-hidden). Inside it, .pictures-icon-body is the closed
   shape, .pictures-icon-cut a detail inside it (cut out when filled), .pictures-icon-line a detail outside it (always a line).
   The icons layer fills the body; the stroke layer sets the weight. Custom properties inherit into a <use>, so a symbol takes them. */
.icon { width: 1.5em; height: 1.5em; flex: none; overflow: visible; vertical-align: -0.35em; fill: none; stroke: currentColor;
  stroke-width: var(--pictures-sw, 2); stroke-linecap: round; stroke-linejoin: round; filter: var(--pictures-icon-filter, none); }
:is(.pictures-icon-body, .pictures-icon-cut, .pictures-icon-line) { fill: none; stroke: currentColor; vector-effect: var(--pictures-ve, none); }
.pictures-icon-body { fill: var(--pictures-icon-fill, none); }
.pictures-icon-cut { stroke: var(--pictures-icon-cut, currentColor); }
:is(.sheet, .panel) { --pictures-icon-ground: var(--surface); }   /* what a filled icon's cut-outs show: the colour behind it */
.btn-main { --pictures-icon-ground: var(--accent); }
```

```html assemble
<filter id="pictures-pen" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.09" numOctaves="2" seed="4" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="pictures-pen-ic" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.2" numOctaves="2" seed="21" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="2.8" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="pictures-wash" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="1.6" result="b"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" seed="2" result="n"/>
  <feDisplacementMap in="b" in2="n" scale="9" xChannelSelector="R" yChannelSelector="G"/></filter>
```

## Layers

### Technique
- Layer: technique
- Owns: how a drawing or picture is made: its tradition and its marks. Flat shapes, cut paper, an ink line, a pencil sketch, brush and ink, paint, an engraving, or a photograph. Not its frame, mask or colour.
- Default: flat-shapes

#### Flat shapes
- Id: flat-shapes
- Status: draft
- Looks like: clean flat shapes in a few colours, no outlines and no shading; a jug is a silhouette in its glaze with a wavy dip line, the sun a plain disc. Calm and exact; the shapes do all the work.
- Made with: closed paths, each filled with one class whose colour is a shared name or a mix of two. Three to five colours; the deep ones from the bands so the picture keeps its colours on a dark page. Detail comes from the outline of each shape (a wavy dip line, a foot ring), never from texture or gradients.

```css assemble
/* pictures / technique: flat shapes. Drawn with the Base palette (.pictures-sky, .pictures-deep-2, ...): no filter, no outline, no texture. */
```

- Careful: flat shapes are what generic illustration kits are made of, so the template look is near. What saves it is a subject only this site has, drawn from life (the potter's own dip line, the reservoir's own shore), and few colours. Keep shapes few and large; a flat picture with forty small pieces turns into clip-art. Polaris and Atlassian both ask for flat, simple shapes and a small palette less saturated than the page round it (R1, R5).
- Light and dark: stays put. The bands and their pale are the same on both pages, so the picture is the same; on a dark page it sits as a lit rectangle, and the frames part may give it an edge.
- Personality: calm, serious, friendly
- Goes with: `pictures: stroke hairline`; `pictures: icons none` or `pictures: icons outline`; `light: flat-and-even`; `background: grain`.
- Used on: 3 mockups: a quiet gallery of pots (each pot a flat silhouette in its glaze, dipped to a wavy line, with bare clay below), an observatory (a plain moon disc and flat land silhouettes), and a field notebook's taped-in sketch of the reservoir (flat shapes in sky, water and reed colours, the heron a grey shape).

#### Cut paper
- Id: cut-paper
- Status: draft
- Looks like: layered paper: every shape is its own sheet, cut or torn with a slightly uneven edge, a thin pale core showing where the paper was torn, and a fine shadow where it lies on the sheet behind. Three to five layers deep (a backdrop, the sun and the far hills, the near hill and the table, the jug and the cup, the clay over the jug), and a faint paper grain over all. Made by hand, bright and cheerful.
- Made with: each piece a `<g class="cut">` holding the shape twice: first in the pale on the bands, a little larger and pushed out of shape by its own noise (the torn core, which peeks out unevenly), then the coloured shape over it. The group takes one gentle displacement filter for the edge (an `feTurbulence` near 0.045, displacement 3 to 4) and the light part's paper shadow, with a fallback so a site without the light part still sees layers. A handle is its own crescent of paper, not a stroke. Turn a sheet by 2 or 3 degrees. Last, a rectangle of the shade masked by noise for the grain.

- Needs markup: a drawing (inline SVG in the `.picture`, or a `<symbol>` placed with `<use>`) whose shapes take these classes by what they are: `pictures-cut` on each cut piece, `pictures-core` on the pale torn core, `pictures-paper-grain` over the paper, `pictures-tilt` on a piece laid crooked; the filters come in `parts.js`.

```css assemble
.pictures-cut  { filter: url(#pictures-torn) var(--drop-low, drop-shadow(1px 2px 1px color-mix(in oklab, rgb(var(--shadow-rgb)) 30%, transparent))); }
.pictures-core { fill: var(--on-band); stroke: var(--on-band); stroke-width: 3.5; stroke-linejoin: round; filter: url(#pictures-core); }   /* the pale core of torn paper */
.pictures-paper-grain { fill: color-mix(in oklab, rgb(var(--shadow-rgb)) 55%, transparent); opacity: 0.35; filter: url(#pictures-paper-grain); }
.pictures-tilt { rotate: -2deg; transform-box: fill-box; transform-origin: center; }
```

```html assemble
<filter id="pictures-torn" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.045" numOctaves="2" seed="9" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3.5" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="pictures-core" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.09" numOctaves="2" seed="31" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="4" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="pictures-paper-grain"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch" result="n"/>
  <feColorMatrix in="n" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  2.4 0 0 0 -0.95" result="a"/><feComposite in="SourceGraphic" in2="a" operator="in"/></filter>
```

- Careful: flat shapes with a rough edge are not yet paper; the first version here was exactly that. What makes it paper is the layering: separate sheets, each casting on the one behind, and the pale core at a torn edge. Matisse's cut-outs, the tradition here, are "drawing with scissors": flat painted paper with no outline (R20); scissors cut cleanly, tearing leaves the core, and a site picks one. Too strong a displacement reads as chewed. The shadow is the light part's, never a second one made here.
- Light and dark: stays put; the cores are the pale on the bands on both pages. The shadow under each piece is the light part's, faint on a dark page, so there the cores carry the layering.
- Personality: friendly, playful
- Goes with: `pictures: treatment grain`; `pictures: icons hand-drawn`; `materials: paper-and-tape` or `materials: cut-paper-on-felt`; `light: warm`.
- Used on: 1 mockup and a guide: a volunteer page (a crowd of cut-paper arms standing in for a photograph of the club's helpers), and the warm guide's study (cut-paper lettering and drawings on 9 of 12 sites' hand-made marks). The night market's cut poster blocks are the lettering part's.

#### Ink line
- Id: ink-line
- Status: draft
- Looks like: a pen or marker outline with loose flat colour under it, the colour a few pixels off the line as in a quick print. Clear and lively; reads well small.
- Made with: the outline as separate open strokes (each mark of the pen its own path) in `--ink`, round caps, through one gentle displacement filter so no line is ruled; under it the same shapes filled with pale mixes of the band colours, moved 3 to 5 pixels down and to one side. The pale mixes are made with a page value, `--wash-base`, so they stay visible under pale lines on a dark page.

- Needs markup: a drawing (inline SVG in the `.picture`, or a `<symbol>` placed with `<use>`) whose shapes take these classes by what they are: `pictures-ink` on the lines, `pictures-slip` on the colour under them; the filters come in `parts.js`.

```css assemble
.pictures-ink  { fill: none; stroke: var(--ink); stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round; filter: url(#pictures-pen); }
.pictures-slip { translate: 5px 4px; }   /* the colour under the line (Base tints: .pictures-tint-2, ...) slips off it */
```

- Careful: one line weight across all the pictures (the stroke layer); a drawing at two sizes on one page needs `vector-effect: non-scaling-stroke` or two drawings, or the lines will not match. Keep the colour under the line pale: strong fills fight the line.
- Light and dark: turns over. Dark lines on pale paper on a light page; pale lines on a dark page, with the colour under them lifted by `--wash-base` (on a dark page the plain mix with `--surface` was almost black).
- Personality: friendly, playful
- Goes with: `pictures: stroke bold` (marker) or `pictures: stroke regular` (pen); `pictures: icons hand-drawn`; `pictures: figures simple`; `background: drawings lots`.
- Used on: 2 mockups: a repair café (the tools drawn round in marker on the pegboard, the fixers at their table) and a soap shop (each herb drawn in a fine line over flat colour, and each bar drawn beside its herbs).

#### Pencil
- Id: pencil
- Status: draft
- Looks like: a graphite sketch with a light wash of colour under it: lines that break and go over themselves, a little hatching on the shaded side, colour that bleeds past the edges. One thing ringed in pencil, as a naturalist rings what they saw. Drawn on the spot.
- Made with: the outline twice, in `--ink-soft`, each through its own filter: a displacement with a different seed, and a fine noise used as alpha so the line breaks like graphite on paper. A few lines of hatching on the shaded side, clipped to the shape. The wash under it is the same shapes, blurred a little and pushed out of shape by a slow noise, so the colour runs past the line. The ring is the mark colour.

- Needs markup: a drawing (inline SVG in the `.picture`, or a `<symbol>` placed with `<use>`) whose shapes take these classes by what they are: `pictures-graphite` on the lines, `pictures-graphite-again` on a second pass, `pictures-graphite-light` on hatching, `pictures-bleed` on the tints, `pictures-ring` on a mark round the subject; the filters come in `parts.js`.

```css assemble
.pictures-graphite { fill: none; stroke: var(--ink-soft); stroke-width: 1.4; stroke-linecap: round; filter: url(#pictures-pencil); }
.pictures-graphite-again { filter: url(#pictures-pencil-b); opacity: 0.5; }   /* the second pass of the pencil */
.pictures-graphite-light { stroke-width: 0.9; opacity: 0.7; }                 /* hatching on the shaded side */
.pictures-bleed { filter: url(#pictures-wash); opacity: 0.9; }               /* the tints, blurred and pushed past the line */
.pictures-ring  { fill: none; stroke: var(--mark); stroke-width: 2.6; stroke-linecap: round; filter: url(#pictures-pen); }
```

```html assemble
<filter id="pictures-pencil" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="1" seed="3" result="g"/>
  <feColorMatrix in="g" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.9" result="gaps"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="5" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="2.5" xChannelSelector="R" yChannelSelector="G" result="d"/>
  <feComposite in="d" in2="gaps" operator="in"/></filter>
<filter id="pictures-pencil-b" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="1" seed="8" result="g"/>
  <feColorMatrix in="g" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.9" result="gaps"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="12" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3.5" xChannelSelector="R" yChannelSelector="G" result="d"/>
  <feComposite in="d" in2="gaps" operator="in"/></filter>
```

- Careful: the graphite is `--ink-soft`, which is 4.5 to 1 on the page; pencil lighter than that disappears on a phone in daylight. The ring is decoration in `--mark`, never a sign of anything a visitor must notice; say what is ringed in words too (the field notebook's caption names the heron).
- Light and dark: turns over: grey pencil on pale paper, pale chalk-like pencil on dark paper, with the wash lifted by `--wash-base` as for the ink line.
- Personality: calm, friendly
- Goes with: `pictures: icons hand-drawn`; `materials: paper-and-tape`; `light: field-journal`.
- Used on: 1 mockup: a field notebook (a pencil ring round the heron and the osprey, a pencilled route map on the next walk's notice). Its main sketch was flat shapes; this option is what the notebook's pencil marks ask the sketch to be.

#### Ink wash
- Id: ink-wash
- Status: draft
- Looks like: brush and ink: a few strong strokes that swell and taper, a grey wash bleeding round them, distant hills as soft mist, one red disc, and a lot of the paper left empty. Quiet and confident.
- Made with: washes first, as a painter lays them: a pale first wash a little off the shape, a darker second on the shaded side, a darker rim just inside each edge (a wash dries darker where it stops) and ink pooled at the foot, all clipped to the shape and softened by a blur; a fine noise taken out of the washes for the granulation of pigment in the paper's grain. Then the lines: every stroke a filled shape that swells in the middle and comes to a point at both ends (a script widens each line along its length), the same shapes behind it blurred for the ink that bleeds. Last, the ground in dry-brush strokes broken by a noise stretched along the stroke. The red disc is a band colour, never the accent.

- Needs markup: a drawing (inline SVG in the `.picture`, or a `<symbol>` placed with `<use>`) whose shapes take these classes by what they are: `pictures-wash-1` and `pictures-wash-2` on the washes (grouped in `pictures-washes`), `pictures-wet-edge`, `pictures-pool`, `pictures-dry`, `pictures-mist` and `pictures-mist-far`, `pictures-sumi` and `pictures-sumi-bleed` on the ink, `pictures-seal` on the seal; the filters come in `parts.js`.

```css assemble
.pictures-wash-1   { fill: color-mix(in oklab, var(--ink) 9%, transparent); filter: url(#pictures-wash); }    /* the first, pale wash */
.pictures-wash-2   { fill: color-mix(in oklab, var(--ink) 14%, transparent); filter: url(#pictures-wash); }   /* the second, on the shaded side */
.pictures-wet-edge { fill: none; stroke: color-mix(in oklab, var(--ink) 26%, transparent); stroke-width: 6; filter: url(#pictures-soft); }   /* clipped: only the inner half shows */
.pictures-pool     { fill: color-mix(in oklab, var(--ink) 20%, transparent); filter: url(#pictures-soft); }
.pictures-washes   { filter: url(#pictures-granulation); }   /* on the group of washes */
.pictures-sumi     { fill: var(--ink); filter: url(#pictures-pen); }
.pictures-sumi-bleed { fill: color-mix(in oklab, var(--ink) 30%, transparent); filter: url(#pictures-wash); }
.pictures-dry      { filter: url(#pictures-dry); }   /* a noise stretched along the stroke: only on strokes that run the same way */
.pictures-mist     { fill: color-mix(in oklab, var(--ink) 13%, transparent); filter: url(#pictures-mist); }   /* a large blur */
.pictures-mist-far { fill: color-mix(in oklab, var(--ink) 7%, transparent); }
.pictures-seal     { fill: color-mix(in oklab, var(--band-1) 70%, var(--mark)); }
```

```html assemble
<filter id="pictures-soft" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="2.2"/></filter>
<filter id="pictures-mist" x="-20%" y="-30%" width="140%" height="160%"><feGaussianBlur stdDeviation="5"/></filter>
<filter id="pictures-granulation" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="1" seed="4" result="n"/>
  <feColorMatrix in="n" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -1.6 0 0 0 1.55" result="a"/><feComposite in="SourceGraphic" in2="a" operator="in"/></filter>
<filter id="pictures-dry" x="-5%" y="-20%" width="110%" height="140%"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.55" numOctaves="2" seed="6" result="s"/>
  <feColorMatrix in="s" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -3.2 2.2" result="streaks"/>
  <feComposite in="SourceGraphic" in2="streaks" operator="in"/></filter>
```

- Careful: few strokes. The empty paper is the point; a busy ink picture is a different technique. A dry-brush filter streaks in one direction, so it looks like a bar code across strokes that run the other way (the first version did): keep it for strokes that run with it (the ground), and roughen the rest with an even noise. A wash of one flat grey looks printed; the second wash, the wet edge and the pool are what make it read as water and ink. Large blurs cost the browser; draw the mist once.
- Light and dark: turns over: black ink on pale paper, pale ink on a dark one, like white ink on black paper. The red disc stays red.
- Personality: calm, serious
- Goes with: `pictures: stroke brush`; `pictures: icons none`; `pictures: treatment none`; `background: grain`.
- Used on: 1 mockup: a poetry site (an ink circle drawn in one stroke, a branch, a moon, rain and waves in brush and wash, and a red sun).

#### Painted
- Id: painted
- Status: draft
- Looks like: opaque paint in big shapes: light from one side, shade on the other, a lit rim and a glint, a cast shadow on the table; brush marks you can see in the sky and on the wood. Like gouache or a book-cover painting.
- Made with: big shapes in three or four values first, detail second, as the background part's painted ground is made. Each shape is a band colour; the shade is a mix with `--shade` laid over the far side (clipped to the shape); the lit side is strokes that follow the form (curved down a jug, along a plank) in a lighter mix. One gentle displacement filter roughens every edge like a loaded brush. The light comes from the light part's side (`--lx`), the same for every picture on the page.

- Needs markup: a drawing (inline SVG in the `.picture`, or a `<symbol>` placed with `<use>`) whose shapes take these classes by what they are: `pictures-painted` on the whole drawing, `pictures-shade-side`, `pictures-dark-side`, `pictures-lit`, `pictures-glint`, `pictures-cast` and `pictures-halo` on the light and shade, `pictures-sky-light`, `pictures-sky-low` and `pictures-sky-warm` on the sky; the filters come in `parts.js`.

```css assemble
.pictures-painted   { filter: url(#pictures-brush); }   /* on the whole drawing: a small, even roughening, like a loaded brush */
.pictures-shade-side { fill: color-mix(in oklab, var(--pictures-shade) 45%, transparent); }   /* the side away from the light, clipped to the shape */
.pictures-dark-side  { fill: none; stroke: color-mix(in oklab, var(--band-2) 60%, var(--pictures-shade)); stroke-linecap: round; }
.pictures-lit   { fill: none; stroke: color-mix(in oklab, var(--band-2) 45%, var(--on-band)); stroke-linecap: round; opacity: 0.75; }   /* strokes that follow the form */
.pictures-glint { fill: none; stroke: color-mix(in oklab, var(--on-band) 85%, transparent); stroke-linecap: round; }
.pictures-cast  { fill: color-mix(in oklab, var(--pictures-shade) 40%, transparent); }   /* on the table, away from the light */
.pictures-sky-low   { fill: color-mix(in oklab, var(--on-band) 78%, var(--mark)); }
.pictures-sky-light { fill: none; stroke: color-mix(in oklab, var(--on-band) 85%, var(--band-3)); stroke-linecap: round; opacity: 0.8; }
.pictures-sky-warm  { fill: none; stroke: color-mix(in oklab, var(--on-band) 62%, var(--mark)); stroke-linecap: round; opacity: 0.7; }
.pictures-halo  { fill: color-mix(in oklab, var(--mark) 22%, var(--on-band)); }
```

```html assemble
<filter id="pictures-brush" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.06 0.12" numOctaves="3" seed="13" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="4" xChannelSelector="R" yChannelSelector="G"/></filter>
```

- Careful: gouache is opaque and matte: colour covers colour, nothing shows through (R18). A few hundred near-flat strokes at random strengths read as "flat horizontal smears" (the background part found this); so did the first version here. What reads as paint: big shapes, strokes with a direction that follows the form, one light side, a little detail where the eye goes. For a scene that carries the page, the sorcery guide asks for more: hatching and stippling for shade, pattern on every surface, things in front of other things; build it with a script (rule 3). Never a smooth picture made by a machine.
- Light and dark: stays put: a painting is the same on any wall. On a dark page the brightest thing in it may be the brightest thing on the page; the light part decides whether that is wanted.
- Personality: dramatic, playful
- Goes with: `pictures: figures detailed` or `pictures: figures silhouettes`; `pictures: treatment aged`; `pictures: stroke brush`; `light: one-light`; `background: painted-ground`; `frames: carved-plate` or `frames: riveted-metal`.
- Used on: 5 mockups: a dark, painterly joke site (a wizard at a desk under one orb, built in layers with grain, rough edges, hatching and stippling), two versions of a small shop with a dark lead (a robed maker at a stall lit by one lantern), and two game-style joke sites (a hooded figure against a painted sunset, the world behind the panels: rough shapes with jittered edges and overlapping see-through strokes).

#### Engraved
- Id: engraved
- Status: draft
- Looks like: black lines only, on paper: tone made by ruled lines, closer together where it is darker, curving round a jug to show its roundness, crossing on the shaded side; a ruled sky, a sun left white with short rays. Like a plate in an old almanac or natural history.
- Made with: a script that rules the lines: parallel lines for the sky, curved lines across each body (each a gentle arc, so they wrap the form), a second set at an angle for the shade, a third for the darkest part, each set clipped to its shape by a `clipPath` kept in the shared `<defs>`. Outlines a little heavier than the hatching. Everything is `--ink` on `--surface`.

- Needs markup: a drawing (inline SVG in the `.picture`, or a `<symbol>` placed with `<use>`) whose shapes take these classes by what they are: `pictures-outline` on the outlines, `pictures-hatch` on hatching across the forms, `pictures-hatch-fine` on the sky; the filters come in `parts.js`.

```css assemble
.pictures-hatch-fine { fill: none; stroke: var(--ink); stroke-width: 0.5; opacity: 0.6; }   /* the sky */
.pictures-hatch      { fill: none; stroke: var(--ink); stroke-width: 0.8; }                 /* hatching on the forms */
.pictures-outline    { fill: none; stroke: var(--ink); stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
```

- Careful: in an engraving the burin's pressure makes lines swell and thin (R16); ruled lines of one width read as a newer, mechanical version, which is what this option draws. Hatching at about 3 to 4 pixels apart at its final size: closer, and it turns to grey and shimmers when the picture is scaled. A ruled picture is heavy in SVG (the swatch's is about 6 KB, with every line cut to the box it shades); a large one goes in a file. A woodcut is the bolder cousin: broad black cut marks and white lines cut out of black (R14, R15); not drawn yet.
- Light and dark: turns over: black lines on paper, pale lines on a dark page, like a chalk plate or a negative.
- Personality: serious, calm
- Goes with: `pictures: stroke hairline`; `pictures: treatment aged` for an old plate; `lettering: sober-pair`; `light: almanac-plate`.
- Used on: no mockup yet. Closest: the observatory's constellations in hairline, a printed star chart's look, and the sorcery scenes' hatching for shade. From research (R14 to R16).

#### Photograph
- Id: photograph
- Status: draft
- Looks like: a real photograph of the real people, place or thing. Nothing else does what it does for trust (the professional guide's credibility research) or for selling (the sales guide).
- Made with: the site's own photographs, never a library's for people or products. Each at several widths in a modern format with a fallback, `width` and `height` set, cropped for a phone (the phone guide: closer in and taller). A shop shoots every product on the same ground in the same light (the sales guide, 6 of 7).

```html
<picture>
  <source type="image/avif" srcset="p/wheel-600.avif 600w, p/wheel-1200.avif 1200w" sizes="(min-width: 48rem) 50vw, 100vw">
  <img src="p/wheel-1200.jpg" srcset="p/wheel-600.jpg 600w, p/wheel-1200.jpg 1200w" sizes="(min-width: 48rem) 50vw, 100vw"
       width="1200" height="800" alt="Ruth's hands shaping a bowl on the wheel" loading="lazy" decoding="async">
</picture>
```

```css assemble
/* pictures / technique: photograph. Nothing to add: the Base box holds an <img> or a <picture> at full width, its own ratio from width and height. */
```

- Careful: in a mockup there are almost never photographs yet, and a stock photograph is worse than none (warm guide); the stand-in layer decides what goes there. Text over a photograph fails contrast somewhere: put words on a sheet beside or over it (the background part's "words never sit on a busy ground"). The swatch book's photograph is a CC0 picture from Wikimedia Commons, credited on the page; a real site uses its own.
- Light and dark: never changes. On a dark page a bright photograph may need the frames part's edge or the light part's dimming; never invert or tint a photograph for a dark mode unless a treatment is picked.
- Personality: any
- Goes with: `pictures: figures photographed`; `pictures: treatment none` or `pictures: treatment duotone`; `pictures: stand-in brief-box` or `pictures: stand-in captioned`; `pictures: icons outline`.
- Used on: no mockup had real photographs. Asked for by four guides: warm (10 of 12 sites opened on a photograph of the organisation's own people), professional (10 of 12), education (10 of 12), sales (7 of 7 opened on the products photographed in a scene). The tutor site left boxes for them.

### Treatment
- Layer: treatment
- Owns: what is done to a picture after it is made, to a photograph or a drawing alike: two-colour, grain, a printed screen of dots, two inks out of register, age. Each is one SVG filter on the picture, coloured by CSS from the shared names, so the original stays as it was.
- Default: none

#### None
- Id: none
- Status: draft
- Looks like: the picture as it was made or taken.
- Made with: nothing.

```css assemble
& { --pictures-treatment: none; }
```

- Careful: none.
- Light and dark: nothing changes.
- Personality: any
- Goes with: any.
- Used on: almost every picture on the mockups.

#### Duotone
- Id: duotone
- Status: draft
- Looks like: the picture in two colours from the page: its darks in a deep band colour, its lights in the pale that sits on the bands. A set of different photographs suddenly looks like one set.
- Made with: one filter: the picture's lightness becomes how much of the light ink shows over the dark one, so white becomes the light colour and black the dark one (the same as a grey picture laid with `multiply` over the light colour and the dark laid over with `lighten`, R11, R12; the swatch book does it that way). Both inks are shared names that are the same on both pages (`--band-3` and `--on-band`), so a duotone does not flip on a dark page. A site with `bands: none` may not set them, so each is read with a fallback that is also dark, or pale, on both pages: the accent deepened with the shade, and the page's paper or ink, whichever is pale. A drawing takes it the same way.

```css assemble
& { --pictures-treatment: url(#pictures-duotone); }
.pictures-dark-ink { flood-color: var(--pictures-dark-ink); }
.pictures-paper-ink { flood-color: var(--pictures-paper-ink); }
```

```html assemble
<filter id="pictures-duotone" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
  <feColorMatrix in="SourceGraphic" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0.2126 0.7152 0.0722 0 0"/>
  <feComponentTransfer result="lum"><feFuncA type="gamma" amplitude="1.08" exponent="1.4" offset="-0.03"/></feComponentTransfer>
  <feFlood class="pictures-paper-ink"/><feComposite in2="lum" operator="in" result="lights"/>
  <feFlood class="pictures-dark-ink"/><feComposite in="lights" operator="over"/>
  <feComposite in2="SourceAlpha" operator="in"/></filter>
```

- Careful: faces in a duotone lose their colour, and with it some warmth: fine for a set of places or objects, think twice for the photograph of the founder. Pick a dark band deep enough that the picture keeps its shape (the jug read best on night blue). The SVG way (`feColorMatrix` to grey, then `feComponentTransfer` tables) does the same in one filter (R13), but its colours are written in the filter, not shared names. `mix-blend-mode` needs `isolation: isolate` on the box (R11).
- Light and dark: the same on both: the band and its pale do not change with the page.
- Personality: serious, calm, dramatic
- Goes with: `pictures: technique photograph`; `pictures: figures photographed`; `background: coloured-bands` (the picture in the band's own colours).
- Used on: no mockup yet. The warm guide's study saw it in spirit (red slanted blocks over a photograph of runners); from research (R11 to R13).

#### Grain
- Id: grain
- Status: draft
- Looks like: a fine speckle over the picture, so a clean photograph or a flat drawing sits in a page that is made of paper or plaster.
- Made with: a filter that lays specks of `rgb(var(--texture-rgb))` over the picture at 2.4 times the page's `--texture-strength`, from the same noise as the background part's grain tile, so picture and page share one grain (the noise is the one CSS-Tricks describes for grainy gradients, R25).

```css assemble
& { --pictures-treatment: url(#pictures-grain); }
.pictures-speck { flood-color: rgb(var(--texture-rgb)); flood-opacity: calc(var(--texture-strength) * 2.4); }
```

```html assemble
<filter id="pictures-grain" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
  <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch"/>
  <feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  2.4 0 0 0 -0.95" result="specks"/>
  <feFlood class="pictures-speck"/><feComposite in2="specks" operator="in"/>
  <feComposite in2="SourceAlpha" operator="in"/><feComposite in2="SourceGraphic" operator="over"/></filter>
```

- Careful: never over a picture that is all detail (a crowd, small print); never over a product photograph, where the buyer wants to see the thing. At more than about 2.5 times the page's strength it reads as noise (the first version here, at 3.5, did).
- Light and dark: dark specks over the picture on a light page, pale ones on a dark page; the dark page's grain is a little stronger, as for the ground.
- Personality: calm, friendly, playful
- Goes with: `pictures: technique cut-paper` or `pictures: technique flat-shapes`; `background: grain`; `materials: paper-and-tape`.
- Used on: 2 mockups: a poetry site (a grain tile over the whole page and its ink drawings) and a dark, painterly joke site (its scene "a ground with grain in it"). The cut-paper warm sites lay grain on their bands.

#### Halftone
- Id: halftone
- Status: draft
- Looks like: the picture printed in dots, as in a newspaper or a cheap poster: big dots in the shadows, small ones in the half-tones, none in the lights. In one ink on pale paper.
- Made with: one filter (R21 does it in CSS; the swatch book does it that way): the picture in grey, averaged half and half with a tiled screen of round dots (dark at each dot's centre), then a steep threshold makes everything darker than the middle ink and everything lighter paper, so each dot grows with the darkness under it. The ink and paper are the duotone's.

```css assemble
& { --pictures-treatment: url(#pictures-halftone); }
.pictures-dark-ink { flood-color: var(--pictures-dark-ink); }
.pictures-paper-ink { flood-color: var(--pictures-paper-ink); }
```

```html assemble
<filter id="pictures-halftone" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
  <feColorMatrix in="SourceGraphic" values="0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0 0 0 0 1" result="grey"/>
  <feImage width="5" height="5" preserveAspectRatio="none" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='5' height='5'%3E%3CradialGradient id='d' r='0.7071'%3E%3Cstop offset='0'/%3E%3Cstop offset='1' stop-color='%23fff'/%3E%3C/radialGradient%3E%3Crect width='5' height='5' fill='url(%23d)'/%3E%3C/svg%3E"/>
  <feTile result="dots"/>
  <feComposite in="grey" in2="dots" operator="arithmetic" k2="0.5" k3="0.5"/>
  <feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  18 0 0 0 -8.5" result="paper"/>
  <feFlood class="pictures-paper-ink"/><feComposite in2="paper" operator="in" result="lights"/>
  <feFlood class="pictures-dark-ink"/><feComposite in="lights" operator="over"/>
  <feComposite in2="SourceAlpha" operator="in"/></filter>
```

- Careful: the dots must be laid at half strength (`opacity`), not blended with `screen`: screen puts every tone lighter than the middle into paper, so half the picture vanished in the first version. A 5 pixel screen suits a picture 300 to 600 pixels wide; scale the screen with the picture or small pictures turn to mush. It is decoration over a real picture: the alt text describes the picture, not the dots.
- Light and dark: the same on both: band ink on pale paper.
- Personality: playful, dramatic
- Goes with: `pictures: technique photograph`; `lettering` with a poster face; `background: coloured-bands`.
- Used on: no mockup yet; from research (R21).

#### Riso
- Id: riso
- Status: draft
- Looks like: two inks printed one over the other on pale paper, slightly out of register, with a grainy stencil texture: blue in the shadows, red in the middle tones, and where they overlap a third colour. The look of a risograph print or a screen-printed poster.
- Made with: one filter: the darkest tones become the first ink, the middle tones the second, moved 3 by 2 pixels; both are laid with `multiply` on the pale paper, and a paper-coloured grain over the top breaks the ink like a stencil. (The swatch book, and a site doing it in CSS, uses two copies of the picture, the second `aria-hidden` with empty alt; the filter needs no copy.)

```css assemble
& { --pictures-treatment: url(#pictures-riso); }
.pictures-dark-ink { flood-color: var(--pictures-dark-ink); }
.pictures-paper-ink { flood-color: var(--pictures-paper-ink); }
.pictures-riso-a { flood-color: color-mix(in oklab, var(--pictures-dark-ink) 80%, var(--pictures-paper-ink)); }   /* the shadows */
.pictures-riso-b { flood-color: color-mix(in oklab, var(--band-1, var(--accent)) 55%, var(--mark)); }                   /* the middle tones */
```

```html assemble
<filter id="pictures-riso" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
  <feColorMatrix in="SourceGraphic" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -0.802 -2.696 -0.272 0 1.8" result="a-cover"/>
  <feColorMatrix in="SourceGraphic" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -0.351 -1.18 -0.119 0 1.25"/>
  <feOffset dx="3" dy="2" result="b-cover"/>
  <feFlood class="pictures-riso-a"/><feComposite in2="a-cover" operator="in" result="ink-a"/>
  <feFlood class="pictures-riso-b"/><feComposite in2="b-cover" operator="in" result="ink-b"/>
  <feFlood class="pictures-paper-ink" result="paper"/>
  <feBlend in="ink-a" in2="paper" mode="multiply"/><feBlend in="ink-b" mode="multiply" result="printed"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch"/>
  <feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1.32 0 0 0 -0.52" result="gaps"/>
  <feFlood class="pictures-paper-ink"/><feComposite in2="gaps" operator="in"/>
  <feComposite in2="printed" operator="over"/>
  <feComposite in2="SourceAlpha" operator="in"/></filter>
```

- Careful: riso inks are see-through and overlap into new colours, and misregistration grows with every extra colour (R22); two inks is the honest number. Avoid big solid areas, which print blotchy and look wrong when imitated. In CSS it costs two copies of every picture; the filter costs only the browser's time, still a reason to keep it for a few.
- Light and dark: the same on both: band inks on pale paper.
- Personality: playful, friendly
- Goes with: `pictures: technique photograph` or `pictures: technique flat-shapes`; `background: coloured-bands`; a poster face.
- Used on: no mockup yet; from research (R22, R23).

#### Aged
- Id: aged
- Status: draft
- Looks like: faded and warmed: colours drained, the whole picture toned toward brown (the shared `--earth`, which is brown whatever the neutrals; the mark colour can be violet on a night page, and aged toward it the picture went lilac), darker and browner at the edges, with grain. An old print, or a painting from a book cover of the 1970s.
- Made with: the picture with its saturation and contrast lowered; then one filter lays over it, with `multiply`, a warm tone (a pale mix of `--earth`) and a soft darker edge, and grain on top. How old is `--pictures-age`, from 0 to 1 (1 when unset): every step scales with it.

```css assemble
/* --pictures-age, 0 to 1 (1 if unset), is how old: a dark painted scene wants about 0.5, or it greys */
& { --pictures-treatment: saturate(calc(1 - 0.65 * var(--pictures-age, 1))) contrast(calc(1 - 0.14 * var(--pictures-age, 1)))
    brightness(calc(1 + 0.06 * var(--pictures-age, 1))) url(#pictures-aged); }
.pictures-age-tone  { flood-color: color-mix(in oklab, var(--earth, var(--mark)) 32%, var(--on-band)); flood-opacity: var(--pictures-age, 1); }   /* toward brown on any page: the earth colour is brown whatever the neutrals */
.pictures-age-edge  { flood-color: var(--earth, var(--mark)); flood-opacity: calc(0.6 * var(--pictures-age, 1)); }
.pictures-age-speck { flood-color: rgb(var(--texture-rgb)); flood-opacity: calc(var(--texture-strength) * 3 * var(--pictures-age, 1)); }
```

```html assemble
<filter id="pictures-aged" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
  <feFlood class="pictures-age-tone"/><feBlend in2="SourceGraphic" mode="multiply" result="toned"/>
  <feImage preserveAspectRatio="none" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' preserveAspectRatio='none'%3E%3CradialGradient id='v' cy='0.45' r='0.72'%3E%3Cstop offset='0.5' stop-opacity='0'/%3E%3Cstop offset='1'/%3E%3C/radialGradient%3E%3Crect width='100' height='100' fill='url(%23v)'/%3E%3C/svg%3E" result="edge"/>
  <feFlood class="pictures-age-edge"/><feComposite in2="edge" operator="in"/>
  <feBlend in2="toned" mode="multiply" result="aged"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch"/>
  <feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  2.4 0 0 0 -0.95" result="specks"/>
  <feFlood class="pictures-age-speck"/><feComposite in2="specks" operator="in"/>
  <feComposite in2="aged" operator="over"/>
  <feComposite in2="SourceAlpha" operator="in"/></filter>
```

- Careful: at full strength over an already dark painted scene it greys the whole picture (the second rebuild of the dark painterly site found this): set `--pictures-age` near 0.5 there. Age is a look, not damage: no fake tears, stains or folds across faces or products. The darker edge is part of the picture, not the page's light (that is the light part's vignette); do not use both.
- Light and dark: nearly the same on both (the tone is mixed into the pale on the bands); the grain is light specks on the dark page.
- Personality: dramatic, calm
- Goes with: `pictures: technique painted` or `pictures: technique engraved`; `materials: parchment-and-ink`; `light: one-light`.
- Used on: 3 mockups in spirit: a dark, painterly joke site and two versions of a small shop with a dark lead, whose guide asks for the look of painted pictures from the 1970s and 80s, aged parchment and ink. They aged the page, not the picture; this is the picture's own version.

### Icons
- Layer: icons
- Owns: how the small signs in menus, buttons and lists are drawn: open outlines, solid shapes, two tones, a hand's line, or none. Their weight is the stroke layer's.
- Default: outline

All five draw the same geometry, kept once (see Base): the body of each icon is a closed shape (`.pictures-icon-body`), a detail inside it is `.pictures-icon-cut` (cut out of it when filled) and a detail outside it is `.pictures-icon-line` (always a line). The style is a few custom properties (`--pictures-icon-fill`, `--pictures-sw`, `--pictures-icon-filter`), which reach inside each `<use>`. The swatch book names them `.b`, `.k` and `.o`.

Every icon sits beside its word. An icon alone is understood only for a handful of things (home, print, search), and even those are clearer with a word (R9); Atlassian pairs icons with text labels as a rule (R4). An icon beside its word is decoration (`aria-hidden="true"`); an icon that is all a button has needs the button's name in words (`aria-label`). Icons are drawn for the site or taken from one open set with a licence that allows it; never mixed from several sets.

#### Outline
- Id: outline
- Status: draft
- Looks like: open shapes drawn in one even line with round ends: a house, a magnifying glass, a basket, a calendar, a pencil. Light, modern, quiet.
- Made with: a 24 by 24 grid with at least a pixel of padding, one stroke weight from the stroke layer, round caps and joins, corners rounded a little, as the common open sets draw them (Lucide: 2px; Heroicons: 1.5px; R31).

```css assemble
& { --pictures-icon-fill: none; }
```

- Careful: the line must stand 3 to 1 against what is behind it (the general guide); `currentColor` from text that passes 4.5 to 1 does. At 16 pixels a 2px line closes small gaps (a calendar's dates turn to a smudge): draw a simpler icon for small sizes, or use a 20 grid. Outline icons are the default because they agree with most lettering; they are also the most generic, which the warm and sorcery guides say to avoid.
- Light and dark: the icons are `currentColor`, so they take the text colour on either page.
- Personality: calm, serious, friendly
- Goes with: `pictures: stroke regular` or `pictures: stroke hairline`; `pictures: technique photograph` or `pictures: technique flat-shapes`.
- Used on: 2 mockups: an observatory (24-grid icons beside each link, hidden from screen readers) and a tutoring site (a camera drawn in a 1.6 line on each photograph box).

#### Filled
- Id: filled
- Status: draft
- Looks like: solid shapes with their details cut out: a black house with a white door. Heavy and clear; reads at a glance and from across a room.
- Made with: the body filled with `currentColor` and inner details stroked in the colour behind the icon (`--icon-ground`), so they look cut out. Outer details stay lines.

```css assemble
& { --pictures-icon-fill: currentColor; }
.icon { --pictures-icon-cut: var(--pictures-icon-ground); }   /* set on the icon, so it reads the ground of the sheet or button it sits on */
```

- Careful: a filled icon next to an outline one means "chosen" in many systems: Material uses its fill axis "to convey a state transition" (R28). So a site that is all filled cannot use fill to show the current page; use the frames part's underline or a mark instead. The cut-out colour must be the real colour behind the icon; on a picture or gradient, draw the detail as a hole in the path instead.
- Light and dark: dark shapes on a light page, pale shapes on a dark one; the cut-outs follow the sheet behind.
- Personality: playful, dramatic, serious
- Goes with: `pictures: stroke bold`; `pictures: technique painted` or `pictures: technique flat-shapes`; `frames: riveted-metal` (an icon in a ring).
- Used on: 2 mockups: two game-style joke sites (solid class emblems and resource signs set in thick metal rings), and the game-interface guide ("everything drawn is a little too big and too thick").

#### Duotone
- Id: duotone
- Status: draft
- Looks like: an outline with a pale fill of its own colour inside: a little softer and friendlier than a bare outline, and still light.
- Made with: the outline, with the body filled at about a quarter of the line's colour.

```css assemble
& { --pictures-icon-fill: color-mix(in oklab, currentColor 24%, transparent); }
```

- Careful: the pale fill is decoration; the line alone still has to stand 3 to 1. Not a second colour: a fill in the accent makes every icon look pressable.
- Light and dark: the fill follows the line's colour, so it is a pale grey on a light page and a dim one on a dark page.
- Personality: friendly, calm
- Goes with: `pictures: stroke regular`; `pictures: technique flat-shapes` or `pictures: technique ink-line`.
- Used on: no mockup yet. One of the six weights of a common open set (Phosphor's "duotone", read from a search result, R30).

#### Hand-drawn
- Id: hand-drawn
- Status: draft
- Looks like: the same shapes drawn by a hand: the line wavers, ends do not quite meet, each icon sits a degree or two off straight. Made for this site, not taken from a pack.
- Made with: the outline through a fine displacement filter sized for 24-pixel icons (a noise at about 0.2 and a displacement of about 3 units; the background's pen, sized for big signs, barely moved them), and every other icon turned a few degrees.

```css assemble
& { --pictures-icon-filter: url(#pictures-pen-ic); }
:nth-child(odd) > .icon { rotate: -4deg; }
:nth-child(even) > .icon { rotate: 3deg; }
```

- Careful: the warm guide asks for marks drawn for the site, never an icon set; an icon set roughened by a filter is the cheap version of that, so draw the icons for the subject where you can (a kettle for "repairs", a notebook for "sightings"). The wobble must not close a small gap: test at the smallest size used.
- Light and dark: as outline.
- Personality: friendly, playful
- Goes with: `pictures: technique cut-paper`, `pictures: technique ink-line` or `pictures: technique pencil`; `pictures: stroke bold` (marker) or `pictures: stroke regular` (pen).
- Used on: 4 mockups: a repair café (a kettle with a darned patch as its mark), a field notebook (a drawn notebook as its mark), a dark, painterly joke site (a drawn book, bottles and a quill beside each menu word), and the warm guide's rule ("draw them for the site; do not use an icon set").

#### None
- Id: none
- Status: draft
- Looks like: no icons: words carry the menu and the buttons. The page is quieter, and the typography does the work.
- Made with: nothing.

- Needs markup: none; a sign that must stay (a close cross, a basket count) takes `class="icon pictures-keep"`.

```css assemble
.icon:not(.pictures-keep) { display: none; }   /* a close cross, a basket count or a phone menu keeps its sign: class="icon pictures-keep" */
```

- Careful: still keep a symbol where the convention is strong and the space small (a basket count in a shop's header, a close button's ×, a menu on a phone), written as text or one drawn sign, with its name.
- Light and dark: nothing changes.
- Personality: calm, serious
- Goes with: `pictures: technique flat-shapes` or `pictures: technique ink-wash`; `pictures: stroke hairline` or `pictures: stroke brush`.
- Used on: 2 mockups: a quiet gallery of pots (four words in the menu and nothing else) and a poetry site.

### Stroke
- Layer: stroke
- Owns: the weight of every drawn line in icons and drawings: from one fine pixel to a fat marker, or a brush that swells and tapers. Not the borders of boxes, which are the frames part's.
- Default: regular

#### Hairline
- Id: hairline
- Status: draft
- Looks like: one pixel at every size: constellations, a height marker beside a pot, an icon drawn with a fine pen. Exact and quiet.
- Made with: a 1 pixel line that does not grow when the drawing is scaled up.

```css assemble
& { --pictures-sw: 1; --pictures-ve: non-scaling-stroke; }
```

- Careful: a 1px line in `--line` fails 3 to 1; a hairline icon or a line that means something is drawn in `--ink` or `--ink-soft`. On a phone outdoors hairlines vanish: keep meaning out of them.
- Light and dark: a fine dark line on a light page, a fine pale one on a dark page, where it looks a little bolder (light on dark spreads).
- Personality: calm, serious
- Goes with: `pictures: technique flat-shapes` or `pictures: technique engraved`; `pictures: icons outline` or `pictures: icons none`; a fine book serif.
- Used on: 2 mockups: an observatory (two constellations in hairline over the sky) and a quiet gallery of pots (a hairline height marker beside each piece).

#### Regular
- Id: regular
- Status: draft
- Looks like: two pixels at 24: the common weight of icons and line drawings.
- Made with: a 2 unit line on a 24 grid, so 2 pixels at 24 pixels; drawings scale their line with them (or keep it with `non-scaling-stroke`).

```css assemble
& { --pictures-sw: 2; }
```

- Careful: decide the weight once against the reading face: a light serif wants 1.5, a sturdy sans 2. Material's icons are a 2dp line on a 24dp grid (R26, read from a search result).
- Light and dark: as hairline.
- Personality: any
- Goes with: any.
- Used on: most mockups' icons and drawn marks (the observatory's icons, the tutor site's camera at 1.6, the field notebook's marks).

#### Bold
- Id: bold
- Status: draft
- Looks like: three pixels at 24, or a fat marker in a drawing: chunky, cheerful, reads from across a room.
- Made with: a 3 unit line; drawings in marker at 4 to 6.

```css assemble
& { --pictures-sw: 3; }
```

- Careful: small gaps close at this weight; simplify the icon (fewer slats in a basket) rather than thin the line. Bold lines want a bold face: next to a fine serif they shout.
- Light and dark: as hairline; on a dark page bold pale lines can glare, so the colour part may soften `--ink` there.
- Personality: playful, friendly
- Goes with: `pictures: icons filled` or `pictures: icons hand-drawn`; `pictures: technique ink-line` or `pictures: technique cut-paper`; a poster face.
- Used on: 2 mockups and a guide: a repair café (tool outlines in marker on the pegboard), the game-style joke sites, and the game-interface guide ("Thin hairlines and delicate detail belong to other guides").

#### Brush
- Id: brush
- Status: draft
- Looks like: lines that swell in the middle and come to a point at each end, as a brush makes them: an ink circle in one stroke, a jug in a few marks.
- Made with: in drawings, each line drawn as a filled shape whose width follows the line (a script widens it: thin at the ends, full in the middle, a little uneven). Icons cannot take a real brush line at 24 pixels: under brush they take the regular weight through the fine pen filter, so they belong with the drawings.

- Needs markup: a drawing made of filled brush shapes, its group or shapes classed `pictures-line-art`.

```css assemble
& { --pictures-sw: 2.4; --pictures-icon-filter: url(#pictures-pen-ic); }   /* icons cannot take a real brush line at 24 pixels */
.pictures-line-art { fill: var(--ink); stroke: none; }   /* the drawing is filled brush shapes, not strokes */
```

- Careful: brush shapes are heavier files than lines (the swatch's jug is about 5 KB against 1 KB); draw them once as symbols. A brush line for every small thing becomes calligraphy for its own sake: keep it for the signature drawing.
- Light and dark: black brush on a light page, pale brush on a dark one.
- Personality: calm, dramatic
- Goes with: `pictures: technique ink-wash` or `pictures: technique painted`; `pictures: icons none` or `pictures: icons hand-drawn`.
- Used on: 2 mockups: a poetry site (an ink circle in one stroke, an ink branch) and a dark, painterly joke site (the sorcery guide's "every picture and ornament shows how it was made: a brush mark, a pen line, an uneven edge").

### Figures
- Layer: figures
- Owns: how people are shown in the pictures: not at all, as dark shapes, as simple friendly figures, as particular people, or photographed.
- Default: none

People drawn for a site are many kinds of people: skin, hair, age and build vary, as Intuit asks of its illustrators (a range of natural skin tones and a palette for them, R6) and Polaris (people in more organic shapes than objects, R5). With only shared names, skin is a range of tones mixed from `--mark` toward `--on-band` (lighter) and toward the shade (darker); clothes are band colours, never the accent, which would make a person look pressable. The tones are in the Base palette (`.pictures-skin-1` to `-3`, `.pictures-hair-1` to `-3`).

#### None
- Id: none
- Status: draft
- Looks like: no people in the pictures: things and places only. The visitor brings themselves.
- Made with: nothing.

```css assemble
/* pictures / figures: none. No people are drawn, so nothing is added. */
```

- Careful: a site about people (a club, a café, a tutor) with no people in its pictures feels empty; the warm and professional guides both open on people. Here the people may be in words instead (names, voices).
- Light and dark: nothing changes.
- Personality: any
- Goes with: `pictures: technique flat-shapes`, `pictures: technique engraved` or `pictures: technique ink-wash`.
- Used on: 5 mockups: a quiet gallery of pots, an observatory, a night market, a field notebook (a heron, but no people) and a poetry site.

#### Silhouettes
- Id: silhouettes
- Status: draft
- Looks like: people as dark shapes against the light: a low sun, a lit window. No faces; the shape tells who they are (a bun, a cap, a hood). Mysterious, or simply anyone.
- Made with: each figure one flat shape (a head, a neck, the shoulders) in a dark mix of a band and the shade, against a bright shape behind (the sun, a doorway), so the outline reads.

- Needs markup: figures drawn as shapes classed `pictures-silhouette`.

```css assemble
.pictures-silhouette { fill: color-mix(in oklab, var(--band-3) 65%, var(--pictures-shade)); stroke: color-mix(in oklab, var(--band-3) 65%, var(--pictures-shade)); stroke-linecap: round; }
```

- Careful: a silhouette is only as good as its outline: give each figure one thing that tells it apart (a hat, a bag, a stance). Blobs with round heads read as eggs (the first version here did). Never two figures touching, or they merge into one shape.
- Light and dark: stays put: dark shapes against a pale sun on both pages.
- Personality: dramatic, calm
- Goes with: `pictures: technique painted` or `pictures: technique flat-shapes`; `light: one-light` or `light: daylight`.
- Used on: 2 mockups and two guides: two game-style joke sites (a hooded figure dark against a painted sunset), and the sorcery guide's study (three hoods, each empty but for one glowing line).

#### Simple
- Id: simple
- Status: draft
- Looks like: round heads, dot eyes, a curve for a smile, a block for a jumper; three people at a table, each a different age and skin. Friendly, and anyone could be them.
- Made with: a circle for the head, a shape for the hair, two dots and a curve, and one shape for the body, in flat fills from the tones above; one detail each (glasses, a cap, grey hair).

- Needs markup: figures drawn in the Base tones, their eyes classed `pictures-feature` and a smile `pictures-smile`.

```css assemble
.pictures-feature { fill: color-mix(in oklab, var(--mark) 22%, var(--pictures-shade)); }   /* dot eyes; skin and hair are the Base tones */
.pictures-smile   { fill: none; stroke: color-mix(in oklab, var(--mark) 22%, var(--pictures-shade)); stroke-width: 2; stroke-linecap: round; }
```

- Careful: simple is not childish: keep proportions true (Polaris: "realistic proportions", R5) and expressions calm. Vary the people on purpose, and say in the brief that the real photographs will show the real group.
- Light and dark: stays put: the figures are band colours and skin tones mixed into the pale.
- Personality: friendly, playful
- Goes with: `pictures: technique ink-line`, `pictures: technique cut-paper` or `pictures: technique flat-shapes`; `pictures: stand-in captioned`.
- Used on: 2 mockups: a repair café (three fixers at a trestle table mending a lamp, a jumper and a bicycle wheel, each with a different skin tone) and a volunteer page (a crowd of cut-paper arms).

#### Detailed
- Id: detailed
- Status: draft
- Looks like: particular people: faces with brows, a nose and a mouth, hair with strands, an ear, clothes with folds and a shaded side, hands resting on the table. Someone you could recognise again.
- Made with: the simple figure built up: an oval head with a neck and an ear, features in fine lines, the far side of the face and body shaded with a mix of the shade, folds as lines, hair with a few lighter strands. In a painted picture the same, in paint.

- Needs markup: figures drawn in the Base tones, with `pictures-face-line`, `pictures-body-shade`, `pictures-fold` and `pictures-strand` on the detail.

```css assemble
.pictures-face-line { fill: none; stroke: color-mix(in oklab, var(--mark) 22%, var(--pictures-shade)); stroke-width: 1.6; stroke-linecap: round; }
.pictures-body-shade { fill: color-mix(in oklab, var(--pictures-shade) 24%, transparent); }
.pictures-fold   { fill: none; stroke: color-mix(in oklab, var(--pictures-shade) 45%, transparent); stroke-width: 1.5; stroke-linecap: round; }
.pictures-strand { fill: none; stroke: color-mix(in oklab, var(--on-band) 35%, transparent); stroke-width: 1.2; stroke-linecap: round; }
```

- Careful: a script draws simple figures well; detailed ones need a real illustrator or a photograph. The swatch's detailed pair is as far as drawing in code goes, and it is still stiff beside a person's drawing. In a mockup, a detailed figure drawn by script is a stand-in for an illustrator's (say so, as for any stand-in); a detailed face drawn badly is worse than a simple one, so if it is not good enough, step down to simple. A detailed figure standing for a real person (the potter, the tutor) is a stand-in for their photograph and is said to be one. Never draw a real, named person's likeness without asking them.
- Light and dark: stays put.
- Personality: dramatic, serious
- Goes with: `pictures: technique painted`; `pictures: treatment aged`; `light: one-light`.
- Used on: 3 mockups: a dark, painterly joke site (a wizard at his desk with spectacles, a beard and a red hood, lit from below by the orb) and two versions of a small shop with a dark lead (a robed maker at the stall); the sorcery guide's six pictures each have a robed figure.

#### Photographed
- Id: photographed
- Status: draft
- Looks like: the real people, photographed doing the thing: at the wheel, at the table, on the walk. Named, and asked first.
- Made with: the photograph technique; the names in the caption or beside the picture, with what qualifies them where that matters (the professional guide).

```css assemble
/* pictures / figures: photographed. Nothing to draw: the names go in the <figcaption>, in words. */
```

- Careful: written agreement from everyone shown, and from a parent for a child (the education guide). Never a stock photograph standing in for staff or members (the professional and warm guides). Crop hands and work, not only faces, when people prefer not to be shown.
- Light and dark: never changes.
- Personality: any
- Goes with: `pictures: technique photograph`; `pictures: stand-in brief-box` or `pictures: stand-in captioned` in the mockup.
- Used on: no mockup yet (no real photographs); asked for by the warm, professional and education guides.

### Stand-in
- Layer: stand-in
- Owns: what fills a photograph's (or a painting's) place in a mockup until the real one exists, and what the page says about it. Rule 4 above holds whatever is picked: the blueprint always says.
- Default: captioned

#### None
- Id: none
- Status: draft
- Looks like: nothing stands in: the drawing is the site's real picture, and its caption is an ordinary caption.
- Made with: the drawing, with `picture.made` saying it is the site's own art and `page_relies_on` what the page needs from it.

```css assemble
/* pictures / stand-in: none. The drawing is the site's own picture; its caption is an ordinary one. */
```

- Careful: only when nobody will replace it: a sky drawn for an observatory, a game's own world, a club's own sketch. If anyone means to photograph it later, it is a stand-in.
- Light and dark: nothing changes.
- Personality: any
- Goes with: `pictures: technique engraved`, `pictures: technique pencil` or `pictures: technique painted`.
- Used on: 3 mockups: an observatory (the sky behind the page is the art), a field notebook (the sketch is a member's) and a night market (the lantern and the dishes).

#### Brief box
- Id: brief-box
- Status: draft
- Looks like: a box the exact size and shape of the photograph, faintly striped, with a camera sign and what the photograph must show in words: "Photo: hands at the wheel, from above. Daylight from the left; 3:2, 1800 by 1200 or larger."
- Made with: a box with the photograph's `aspect-ratio`, a dashed edge in `--ink-soft`, a stripe in `--line`, and two lines of text: the subject in bold, then the direction (light, crop, what to include and leave out, size). The same in the blueprint, as the brief for the photographer.

- Needs markup: in place of each missing picture, `<div class="picture pictures-brief"><strong>What goes here</strong> ...</div>`.

```css assemble
.pictures-brief { aspect-ratio: 3 / 2; display: flex; flex-direction: column; justify-content: center; align-items: flex-start;
  gap: var(--gap-inside, 0.5rem); padding: var(--pad, 1rem); border: 2px dashed var(--ink-soft); color: var(--ink-soft);
  background: var(--surface) repeating-linear-gradient(135deg, transparent 0 14px, color-mix(in oklab, var(--line) 45%, transparent) 14px 15px); }
.pictures-brief strong { color: var(--ink); }
```

- Careful: honest and useful, and it looks unfinished: show it where trust matters more than charm (a tutor, a clinic, a shop's product page). The box is `role="img"` with a label saying a photograph goes there, so a screen reader is not told it is a picture of a camera. Balsamiq's crossed box is the same idea, and its advice: a sketch when the concept matters, the final picture only when it is decided (R31).
- Light and dark: a pale striped box on a light page, a dark one on a dark page; the text is the page's soft ink.
- Personality: serious, calm
- Goes with: `pictures: technique photograph`; `pictures: figures photographed`; `pictures: icons outline`.
- Used on: 1 mockup: a tutoring site ("Photo: portrait of the tutor. Warm, well lit, looking at the camera. This is the first thing a parent sees.", and three more for the gallery).

#### Captioned
- Id: captioned
- Status: draft
- Looks like: a drawing in the site's own technique and material, where the photograph will go, with a plain caption that says so: "Drawn for now: a photograph of our own fixers goes here."
- Made with: the drawing at the photograph's size and crop, its alt text saying it is a drawing and what of ("Drawing of three volunteers at a trestle table ... A photograph of the real fixers belongs here."), and the caption under it in the page's caption style.

```css assemble
/* pictures / stand-in: captioned. Nothing to add: the caption that says a photograph goes here is words in the <figcaption>. */
```

- Careful: the warm guide's way: "Fill the slot with artwork made for this site in its own material ... say in the blueprint that a real photograph belongs there". The caption is for the owner and their first readers; take it out when the photograph arrives, not before.
- Light and dark: the drawing follows its technique; the caption is page text.
- Personality: friendly, playful, calm
- Goes with: `pictures: technique cut-paper` or `pictures: technique ink-line`; `pictures: figures simple`.
- Used on: 2 mockups: a repair café ("Drawn for now: a photograph of our own fixers goes here.") and a volunteer page (its crowd of cut-paper arms, said in a comment and in the blueprint, not on the page).

#### Quiet
- Id: quiet
- Status: draft
- Looks like: a drawing with an ordinary caption ("Moon jar, shino glaze. 34 cm."). Nothing on the page says it stands in; the alt text says "Drawing of", and the blueprint says a photograph or a painting replaces it.
- Made with: the drawing, alt text that begins "Drawing of" (or "illustration"), and `picture.made` in the blueprint: "Drawn in code because there are no photographs yet; real photographs replace them", with how they must be taken to keep the page's look.

```css assemble
/* pictures / stand-in: quiet. Nothing to add: the alt text begins "Drawing of", and the blueprint says what replaces it. */
```

- Careful: only where a caption would spoil the page and the owner already knows: an artistic site, a shop shown to its maker. Never where a visitor might take the drawing for the product itself on a live site: a quiet stand-in never goes live.
- Light and dark: as the drawing's technique.
- Personality: calm, serious, dramatic
- Goes with: `pictures: technique flat-shapes` or `pictures: technique painted`.
- Used on: 4 mockups: a quiet gallery of pots (each pot drawn because there are no photographs yet; the site guide says how the real ones must be shot), a soap shop (each bar's alt ends "(illustration)"), a small shop with a dark lead (each ware drawn alone, "stand-ins for photographs", in its script), and a dark, painterly joke site (its scene, "a stand-in a painting may replace").

## Starting points

### Warm
- Id: warm
- Picks: technique: cut-paper; treatment: grain; icons: hand-drawn; stroke: bold; figures: simple; stand-in: captioned
- Personality: friendly, playful
- Looks like: cut paper and marker, grained like the page, with friendly people at a table and a caption saying the real people's photograph goes there. On the real site, change the technique to `photograph` and figures to `photographed`, and keep the rest.
- Used on: the warm guide (about 10 of 12 sites opened on a photograph of the organisation's own people; 9 of 12 had marks drawn by hand; "a stock photograph is worse than none"); a volunteer page (cut-paper crowd).

### Artistic
- Id: artistic
- Picks: technique: ink-wash; icons: none; stroke: brush; stand-in: quiet
- Personality: calm, serious
- Looks like: one made picture in brush and ink, a lot of paper left empty, no icons; the words and the picture carry the page.
- Used on: the artistic guide ("if it has none, the signature has to be drawn, lettered or composed"); a poetry site (an ink circle, branch, moon, rain and a red sun).

### Professional
- Id: professional
- Picks: technique: photograph; stroke: regular; figures: photographed; stand-in: brief-box
- Personality: serious, calm
- Looks like: real, named people photographed; plain outline icons in a regular line; in the mockup, boxes that say exactly what to photograph.
- Used on: the professional guide ("photographs of the actual people, named ... never stock photographs"); the education guide; a tutoring site (its brief boxes).

### Civic
- Id: civic
- Picks: technique: flat-shapes; icons: filled; stroke: bold; stand-in: brief-box
- Personality: serious, calm
- Looks like: few pictures, each one carrying information (a diagram, a map, a photograph that shows the place); solid icons, always with their words, reading at a glance.
- Used on: from research: GOV.UK's guidance (do not carry information in a picture without saying it in words; charts and diagrams as SVG; photographs at least 960 by 640, R2), Carbon's pictograms (simple, never in place of interface icons, R4) and NN/g on icons with labels (R9). No mockup yet.

### Sorcery
- Id: sorcery
- Picks: technique: painted; treatment: aged; icons: hand-drawn; stroke: brush; figures: detailed; stand-in: quiet
- Personality: dramatic
- Looks like: an old painted picture with a robed figure in it, faded and warm, every mark showing the hand; icons drawn, not taken from a pack.
- Used on: the sorcery guide (a robed figure in 6 of 6 pictures; "every picture and ornament shows how it was made"; "no clip-art"); a dark, painterly joke site; two versions of a small shop with a dark lead.

### Gilded dark
- Id: gilded-dark
- Picks: technique: painted; icons: filled; stroke: bold; figures: silhouettes; stand-in: quiet
- Personality: dramatic, playful
- Looks like: a bright, saturated painted world; heroes dark against the sunset; chunky solid icons set in metal rings (the ring is the frames part's).
- Used on: the game-interface guide (painted, saturated, "over-the-top, over-proportioned"); two game-style joke sites.

### Lantern fair
- Id: lantern-fair
- Picks: technique: cut-paper; treatment: grain; icons: hand-drawn; stand-in: none
- Personality: friendly, dramatic
- Looks like: cut-paper lanterns, dishes on tags and chalk signs on a dark page, grained, no people; the drawings are the site's own.
- Used on: a night-market mockup (one paper lantern, a drawn dish on each stall tag, chalk signs in the margins).

### Almanac plate
- Id: almanac-plate
- Picks: technique: engraved; stroke: hairline; stand-in: none
- Personality: calm, serious
- Looks like: fine ruled lines in ink on paper, like a printed star chart or a plate in an old almanac; outline icons in a hairline.
- Used on: an observatory mockup (constellations in hairline, sheets of fine paper); the engraving itself is a step further than the mockup went.

### Catalogue of glazes
- Id: catalogue-of-glazes
- Picks: technique: flat-shapes; icons: none; stroke: hairline; stand-in: quiet
- Personality: calm, serious
- Looks like: each piece drawn flat in its own glaze, large, one to a screen, with a hairline beside it; no icons; the alt text and the blueprint say the drawings stand for photographs to come.
- Used on: a quiet gallery of pots.

### Field journal
- Id: field-journal
- Picks: technique: pencil; icons: hand-drawn; stand-in: none
- Personality: calm, friendly
- Looks like: a coloured pencil sketch taped into the page, one thing ringed in pencil, small drawn marks for the menu.
- Used on: a field-notebook mockup (the ringed heron, the pencilled route map, a drawn notebook as its mark).

### Repair cafe
- Id: repair-cafe
- Picks: technique: ink-line; icons: hand-drawn; stroke: bold; figures: simple; stand-in: captioned
- Personality: playful, friendly
- Looks like: marker drawings with flat colour, friendly fixers at a table, a caption saying their photograph goes there; drawn icons.
- Used on: a repair-café mockup (the fixers at the trestle table, the tools drawn round on the pegboard, a kettle with a darned patch as its mark).

## Swatch book

`tests/parts/pictures.html` shows every option of every layer, then every starting point, each on a light page and on a dark one side by side; open it in a browser to choose by eye. One subject is drawn in every technique (a jug dipped in glaze and a cup on a table, a sprig in the jug, the sun behind), so the technique is the only thing that changes; the treatments are shown on a photograph and on the flat drawing; the icon and stroke swatches show the same five icons, each with its word, and the stroke swatches the jug as a line drawing; the figures swatches show people at a table. The photograph is "Making pottery" by Jared Sluyter (Unsplash, via Wikimedia Commons, CC0), kept at 600 by 400 as `tests/parts/source/pictures.jpg`. It is built by `tests/parts/source/pictures.py` from `pictures-template.html` beside it, which draws every picture as a symbol in one shared `<defs>`; run `python3 pictures.py ../pictures.html` there to rebuild it.

## Not covered yet

- **Pictures made in 3D.** Two mockups made their pictures as live 3D (a soap shop's turning bars, an ant game's nest and meadow). They are scenes, described with the blueprint's `scene`; how they are lit is the light part's, and their models' look (low-poly, smooth, painted textures) is not yet a layer here.
- **A woodcut.** Bold black cut marks and white lines cut out of black (R14, R15). Close to engraved, heavier; not drawn.
- **Watercolour** as its own technique: the pencil's wash is a little of it.
- **A shared drawing helper.** Every scene so far was drawn by its own script, each with its own wobble, hatching, stipple and brush helpers (the second faire shop's feedback asked for one shared pen). This part's builder has a tapered brush line and a hatching ruler; a small shared module for site scripts would save the next scene most of its time.
- **Charts, maps and diagrams.** Pictures that carry data belong with the dataviz guidance; a drawn map (the field notebook's route) sits between the two.
- **Animated pictures.** Motion is the motion part's; a picture that moves stops under reduced motion.
- **Measuring a stand-in.** `check` cannot tell a stand-in from the real picture; it relies on `picture.made`.
- **Approved by the owner.** Every option is a draft; none has been chosen on a site from this part yet.

## Sources

Read on 2026-10-07, for this part. Six kinds of source: published standards (R7, R8, R9, R10, R29, R30), design systems (R1 to R6, R26 to R28), craft writing by people who build interfaces (R11 to R13, R21), the speed of pages (R26 to R31), traditions of picture-making from museums and printers (R14 to R20, R22, R23), and research and law (R24, R25, R32 to R37). The mockups made with the skill and their scripts are the seventh; they are quoted in each option's "Used on". Pages that would not open, or were only seen in search results, are marked; their claims are kept only where another source agrees.

- R1 Atlassian Design System, illustrations (illustration supports the words and the user's context, never pure decoration; spot illustrations for empty, error and success states): atlassian.design/foundations/illustrations
- R2 GOV.UK, publishing guidance on images (do not carry information in an image without saying it in text; SVG for charts and diagrams; photographs at least 960 by 640; credit Creative Commons images; rights must be perpetual and worldwide): guidance.publishing.service.gov.uk/formatting-content/images/
- R3 Material Design 2, imagery (illustrations consistent, one style, no text in them, light deliberately; only the headings could be read): m2.material.io/design/communication/imagery.html
- R4 Carbon (IBM), pictograms (separate from icons, "Don't use pictograms as a replacement for UI icons"; 48px minimum; must pass contrast) and Atlassian iconography (1.5px stroke, flat, pair icons with labels): carbondesignsystem.com/elements/pictograms/usage/ and atlassian.design/foundations/iconography
- R5 Shopify Polaris, illustrations (one visual family; a few colours, less saturated than the page; simple geometric shapes, realistic proportions, people in more organic shapes; flat perspective; read from a search result, the page would not open): polaris-react.shopify.com/design/illustrations
- R6 Intuit QuickBooks, illustration (true-to-life proportions, natural skin tones, a palette of skin and hair tones; read from a search result, the page now redirects): design.intuit.com/quickbooks/brand/design-foundations/illustrations
- R7 WCAG 2.2, 1.1.1 non-text content (a text alternative; decoration "implemented in a way that it can be ignored by assistive technology") and 1.4.5 images of text (real text, except logos): w3.org/WAI/WCAG22/Understanding/non-text-content.html and w3.org/WAI/WCAG22/Understanding/images-of-text.html
- R8 W3C WAI images tutorial, decorative images (`alt=""`; a missing alt makes some screen readers read the file name) and the decision tree: w3.org/WAI/tutorials/images/decorative/ and w3.org/WAI/tutorials/images/decision-tree/
- R9 W3C WAI, functional images (the alt says the action, not the picture) and Nielsen Norman Group, icon usability ("a text label must be present alongside an icon"; only a few icons are universal): w3.org/WAI/tutorials/images/functional/ and nngroup.com/articles/icon-usability/
- R10 Deque, axe rule svg-img-alt (`role="img"` needs a title, `aria-label` or `aria-labelledby`): dequeuniversity.com/rules/axe/4.13/svg-img-alt
- R11 web.dev, Learn CSS, blend modes (`mix-blend-mode` blends the whole element with its pseudo-elements; `isolation: isolate` contains it): web.dev/learn/css/blend-modes
- R12 egghead, duotone with pseudo-elements and `mix-blend-mode` (darken and lighten layers over a grey picture; read from a search result): egghead.io/lessons/css-use-css-pseudo-elements-and-mix-blend-mode-to-create-a-duotone-style-effect
- R13 Codrops (Sara Soueidan), duotone with `feComponentTransfer` (grey with `feColorMatrix`, then tables; `discrete` posterises; the page refused the fetch, read from a search result): tympanus.net/codrops/2019/02/05/svg-filter-effects-duotone-images-with-fecomponenttransfer/
- R14 Tate, woodcut ("relief printing from a block of wood cut along the grain"): tate.org.uk/art/art-terms/w/woodcut
- R15 Tate, wood engraving (cut into the end grain, so "extremely fine detail is possible"; white-line engraving): tate.org.uk/art/art-terms/w/wood-engraving
- R16 Tate, engraving (the burin's pressure and angle give lines "variations in width and darkness"): tate.org.uk/art/art-terms/e/engraving
- R17 Wikipedia, wood engraving (Bewick's white-line method; read from a search result): en.wikipedia.org/wiki/Wood_engraving
- R18 Tate, gouache ("unlike watercolour, is opaque so the white of the paper surface does not show through"): tate.org.uk/art/art-terms/g/gouache
- R19 V&A, a Bewick block (eagle owl; read from a search result): collections.vam.ac.uk/item/O106856/eagle-owl-print-bewick-thomas
- R20 MoMA, Henri Matisse: The Cut-Outs (paper painted with gouache and cut with scissors, "drawing with scissors"; read from a search result): moma.org/interactives/exhibitions/2014/matisse/the-cut-outs.html
- R21 Frontend Masters, a pure CSS halftone in three declarations, and Lean Rada's notes on it (a dot pattern, the picture, and `contrast()` as a threshold; read from search results): frontendmasters.com/blog/pure-css-halftone-effect-in-3-declarations/ and leanrada.com/notes/pure-css-halftone/
- R22 Calverts, risograph printing (see-through inks that overlap into new colours, "some misregistration" growing with each colour, stencil grain, avoid big solid blocks): calverts.coop/portfolio/risograph
- R23 College for Creative Studies, registration and trapping in riso (about 20 inks; overlap hides misregistration; read from a search result): campus.collegeforcreativestudies.edu/imaging-center/2021/06/22/registration-trapping/
- R24 Nielsen Norman Group, photos as web content (users study pictures of real people and products, and ignore "fluffy pictures used to 'jazz up' web pages"): nngroup.com/articles/photos-as-web-content/
- R25 Jimmy Chion, grainy gradients (an `feTurbulence` noise under a picture; Chrome and Safari render it a little differently): css-tricks.com/grainy-gradients/
- R26 web.dev, optimise CLS (width and height give the box its ratio before the picture loads), and Material system icons (24dp, 2dp stroke; read from a search result): web.dev/articles/optimize-cls and material.io/design/iconography/system-icons.html
- R27 web.dev, browser-level lazy loading ("Don't lazy-load images that are likely to be in-viewport ... especially LCP images"): web.dev/articles/browser-level-image-lazy-loading
- R28 web.dev, fetch priority (`fetchpriority="high"` on the largest picture), and Material Symbols (fill, weight, grade and optical size axes; "To convey a state transition, use the fill axis"): web.dev/articles/fetch-priority and developers.google.com/fonts/docs/material_symbols
- R29 web.dev, AVIF (serve through `<picture>` with a fallback): web.dev/learn/images/avif
- R30 MDN, responsive images (`srcset` with widths and `sizes`; `<picture>` with `media` for a different crop), MDN `decoding` (a hint only), and Phosphor icons (six weights including duotone; read from a search result): developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images, developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/decoding and phosphoricons.com
- R31 SVGO, preset-default (comments, metadata and editor data removed, paths merged), Lucide's icon guide (24 grid, 2px stroke, round caps and joins), Heroicons (24 outline at 1.5, 24 solid, 20 mini, 16 micro) and Balsamiq on images in wireframes (a crossed box for "image goes here"; a sketch when the concept matters): svgo.dev/docs/preset-default/, lucide.dev/contribute/icon-design-guide, github.com/tailwindlabs/heroicons and balsamiq.com/learn/ui-control-guidelines/images/
- R32 US Copyright Office, what copyright protects ("does not protect ideas, concepts, systems, or methods of doing something"): copyright.gov/help/faq/faq-protect.html
- R33 Graphic Artists Guild, ethical guidelines ("Do not use GenAI to mimic or generate content that exploits an artist's style or likeness"; ask first): graphicartistsguild.org/general-ai-ethical-use-guidelines/
- R34 Creative Commons, the licences (six licences and CC0): creativecommons.org/share-your-work/cclicenses/
- R35 Creative Commons, recommended practices for attribution (title, author, source, licence): wiki.creativecommons.org/wiki/Recommended_practices_for_attribution
- R36 Wikimedia Commons, reusing content outside Wikimedia (check each file's licence; credit the author; trademark and personality rights still apply): commons.wikimedia.org/wiki/Commons:Reusing_content_outside_Wikimedia
- R37 Unsplash licence (free for commercial use without credit; not for selling the photographs as they are): unsplash.com/license

Not found: Mailchimp's own illustration guidelines (only press about its 2018 brand, where illustration is the flexible part), Microsoft Fluent's illustration page, a museum source for ink line and pencil sketching, and a published size budget for SVG (rule 5's 150 KB is judgement).
