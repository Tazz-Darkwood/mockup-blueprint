---
name: Style guide (general)
summary: How any mockup should look, whatever it is built with and whatever it is for. Type, space, layout, hierarchy, colour and finish. The bottom layer of the style stack; read before creating any mockup and when reviewing how one looks.
kind: general
detect: ["<html"]
checked: 2026-10-03
source: sources are listed at the end of the file
---

# Style guide

The general layer of the style stack. A site's look is decided by up to four layers, read in this order:

1. **This guide**, and `style-mobile.md` beside it, which says how any page must work on a phone. True of any site.
2. **Stacked guides**, chosen in the design brief. Three shelves: what the site is *for* (`style-purpose-...`, such as sales), how it should *feel* (`style-feel-...`: artistic, professional or warm), and what *field* it is in (`style-field-...`, such as education). Guides are made to be mixed. A site may take any number, from any shelf, two of the same kind included: warm with artistic, sales with a booking guide. That is how two sites for the same trade end up looking nothing alike. Not every site needs all three shelves. The brief names the guides, puts the lead first, and says which parts of the site each one governs; in the blueprint, `project.style.guides` lists them in that order. How they combine is under "When guides are stacked" below. The shelves hold the guides that come with the skill and the ones the user has made, which are kept in their own folder outside the skill; `blueprint.py style` lists both. Where a field guide and a feel guide disagree, the field guide wins, because it knows what that trade's visitors expect.
   **Parts** sit beside the shelves: one guide for each part of a page (colour, background, light, materials, frames and edges, corners and shapes, lettering, density, picture style, motion), each made of layers with a few named options, and starting points that set every layer at once. A site picks an option for a part on its own, with any guides: "warm, but with the detailed ground and busy". The pick goes in the site's own guide and in the blueprint as `project.style.parts` (`{"background": "detailed-ground", "density": "busy"}`), and it wins over the stacked guides for that part only. A part with layers can be picked by one layer: the detailed ground without its drawings is `{"background": {"start": "detailed-ground", "drawings": "none"}}`. How parts are built and how they agree is under "Parts, layers and the shared colour names" below. Each part has a swatch book, `tests/parts/<part>.html`, that shows every option so the owner can choose by looking. The owner's reason for them: "instead of making each style from scratch you can grab stuff for each part that applies ... I really like the detail in the background of [one guide] but I don't want to have to use that style just to get that background."
3. **The site's own guide**, kept in the site's folder beside its blueprint (`<name>.style.md`). It holds the brief, the tokens, and every decision that only makes sense for that site.

When they disagree, the more specific wins: the site's guide over the stacked guides, the stacked guides over this one. Between stacked guides, see "When guides are stacked". Mixing is for the look only. The tools a site is built with are not mixed this way: they are a build decision recorded in the blueprint, and the library's notes on a tool apply whenever that tool is used. The one exception: the accessibility minimums in this guide (text contrast, minimum text size, tap target size) are never overridden.

Criticism of a mockup goes to the lowest layer where it is still true. "The poems are too big" belongs to that site. "Artistic sites need a designed frame around each item" belongs to the artistic guide. "The brief must say how dense the page is" belongs here. Ask which it is before writing a rule, and when unsure put it in the site's guide: a rule can be promoted later, but a rule wrongly made general gets applied to every site.

The rules here are about design decisions, not about any tool: they apply the same in plain CSS, Web Awesome, Tailwind or anything else. How to carry a decision out in a particular tool belongs in that tool's own library page.

Two kinds of rule are mixed here, and each note says which it is:

- **From a source.** A published standard or design system gives the number. These are unlikely to change.
- **Judgement.** No source was read for it; it is this guide's own position. These are the ones most likely to be rewritten after critique.

Every rule starts as `draft`. A rule becomes `approved` when it has been applied on two different kinds of site and the skill's owner has agreed with the result on both, recorded on an `Approved by` line. One site cannot show whether a rule is general or only suits that site. Rules that critique shows to be wrong are rewritten, moved to a more specific layer, or removed.

## When guides are stacked

Learned from two mockups of the same shop made with the same three guides in two orders (2026-10-05). With warm leading, the page still came out dark and full like the one with a dark, painterly guide leading, only weaker. The owner: "B just kinda looks like a worse version of A ... nothing really feels warm about B". The order had been followed on small things and lost on the ones that set the feel. So:

1. **The lead sets the feel.** Three things come from the lead guide whatever the others say: the colour of the page (its ground, and how dark or bright it is), what fills the top of the first page, and the main material. If warm leads, it is a warm site with a hint of the others; if a dark, painterly guide leads, a dark, painterly site with a hint of the others.
2. **The others flavour it, in the lead's terms.** A guide later in the order keeps its rules, but carries them out with the lead's colour, material and voice. The owner's own example: a dark guide that fills every gap, placed after warm, still fills it, "but with warm things" (cut paper, bunting, the members' own drawings) on warm's bold colour; its one light becomes a lantern in a bright scene. Warm after a dark guide keeps the dark, full room, and brings into it the people, their names and voice, and the group's own things. Each feel guide has a section, "When this guide is not the lead", saying what it keeps and how it flavours; read it for every guide that is not first. What a guide keeps in second place is never one of the three things the lead decides: not its own picture at the top, its own colour or its own material. On the first site where a second guide kept its figure and its light for the top, the owner found it "seems to be leading it most of all".
3. **Each guide governs the parts its detail map gives it.** Where two claim the same part, the earlier in the order wins, all the way down the list, not only the lead.
4. **A purpose guide decides where things go on its own steps**: the layout of a product, a basket, a booking form, what must be shown and in what order, and that nothing covers a product picture. The feel guides decide what those things are made of. A field guide wins over a feel guide on what that trade's visitors expect. Both hold whatever the order.
5. **Write it down.** The site's own guide has a table, "How the guides were combined": one row for each part where two guides met, what each asked for, what was done, and which of the rules above settled it. A builder reading only the blueprint would otherwise apply the order alone.
6. **Test it.** Picture the first screen with the order swapped. If someone could not tell which guide led, the lead is not leading: go back to rule 1. This is a first pass, made by whoever drew the page, and it has passed while the owner saw the opposite: twice, a page was judged to be led by its first guide and the owner said the second "seems to be leading it most of all". The owner's eye is the test; say in the report that yours was only a first pass.

## A site with two looks

Some sites have a second look the visitor can switch to: a dark theme that is designed rather than only darkened, a mode for a season, a secret version behind a code. Learned on a joke site whose secret code turned it into "a whole new site" (2026-10-05).

- **Each look has its own brief line and its own stack.** Say in the brief what the second look is and how it is reached. It may stack its guides in another order, or other guides. Record it in the blueprint as `project.style.looks`, one entry per extra look: `{"name": "mana side", "reached_by": "the Konami code, or ten taps on the emblem", "guides": ["tavern-epic"]}`.
- **Each look is checked on its own.** The template test, the test of which guide leads, and the counts of typefaces and colours apply to each look by itself. `audit --after <steps>` checks the page after the steps that reach a look, before any context exists; once it does, list those steps in `project.check_states` so `check` looks at it every time.
- **Pictures of both, side by side,** when the owner is shown the look.

## Parts, layers and the shared colour names

A look made of parts holds together only if the parts share a language and never fight over the same decision. Real design systems work the same way (Material, Carbon, Atlassian, Radix, shadcn; see Sources): a few separate foundations, a small set of colour names whose values change between light and dark, and themes made of a few choices that can be changed one at a time.

**The colour part sets every name.** It is picked from a few choices (tone, the hue in the greys, an accent, strength, bands), written in `oklch()` so any combination stays readable; its swatch book checks every combination. A site's dark look is the same picks with the tone changed. `check` and `audit` measure `oklch()` colours like any other.

**Choose the personality first.** One word for the whole site, before any part: serious, calm, friendly, playful or dramatic. Corners, typefaces and colour together decide how serious or playful a page feels, so picking them one by one without this lands on a page that argues with itself. It goes in the brief and in the blueprint as `project.style.personality`. Every option and starting point in a layered part says which personalities it suits; `check` flags a pick that pulls against the site's (`style/personality-clash`), and the site guide says why if it stays.

**A part is made of layers.** Each layer is one decision with a few options and a default, and switches on its own. The background, for example, is texture, pattern, drawings and things to find: "grain, no drawings" is a pick, not a new guide. A **starting point** is a saved set of layer picks with a name ("detailed ground" is mottled texture, lots of drawings, finds on); a site picks it whole or changes one layer: `{"start": "detailed-ground", "drawings": "none"}`. Where two options of one layer work together, a site lists them (`"marks": ["pencil", "stamp"]`) and a starting point writes `marks: pencil + stamp`.

**Every part draws with the shared colour names, never raw colours.** The colour part sets them for the site; every other part uses only these, so each layer works on a light page and a dark one without being rewritten:

| Name | What it is for |
|---|---|
| `--ground` | the page behind everything |
| `--surface` | sheets, panels and cards: where words sit |
| `--surface-raised` | things lifted above a surface: menus, popovers, a card in focus |
| `--ink` | main text, on surfaces |
| `--on-ground` | words straight on the ground. The same as `--ink` on most pages; different when the ground and the sheets are far apart, such as a dark room with words on pale parchment |
| `--ink-soft` | secondary text and captions (still 4.5 to 1) |
| `--line` | dividers and decorative borders. It is not 3 to 1: the edge of a control (a field, a checkbox) uses `--ink-soft` |
| `--accent` | the one colour for things you can press |
| `--on-accent` | text and icons on the accent |
| `--accent-edge` | the edge of a button or control in the accent: the accent itself, or a darker edge when a bright fill (gold, yellow) cannot stand 3 to 1 off the page. Every part that draws an accent control gives it a border in this |
| `--mark` | drawn decoration: signs, pencil marks, specks. Never used for meaning |
| `--focus` | the keyboard focus ring |
| `--danger`, `--success`, `--warning` | errors, success and caution only, never decoration |
| `--scrim` | the dim layer behind a dialog |
| `--band-1`, `--band-2`, `--band-3`, `--on-band` | up to three strong grounds for whole bands of the page, and the words on them (4.5 to 1 on each) |
| `--accent-hover`, `--accent-pressed` | the accent one step lighter or darker for a control being pointed at or pressed (text on them still 4.5 to 1) |
| `--metal`, `--metal-deep`, `--metal-lit`, `--on-metal` | metal and gilt: rings, studs, plates, chiselled letters (gold, brass, silver or iron, picked in the colour part), its shade and highlight, and words on it |
| `--earth`, `--on-earth` | one warm brown at each tone, whatever the neutrals: kraft, card, cork, wood, leather; and words on it |

So there are three tiers: raw values live only in the colour part; the shared names above; and a part's own custom properties, made from the shared names. `style check` flags a raw colour in a layered part's CSS. A few values travel with the names because they differ between light and dark: `--shadow-rgb` (shadows take the page's hue, never pure black), set by the colour part, and `--shadow-strength`, set by the light part; `--texture-rgb`, the colour of grain, mottling and specks, darker than a light ground and lighter than a dark one, so texture never vanishes; and `--texture-strength`, how strongly it shows. Written as `rgb(var(--texture-rgb) / var(--texture-strength))`.

`--dark` is 1 on a dark or lamplit tone and 0 otherwise, for the few things that change by number rather than by colour (reading text a little thinner on a dark page).

**The light part hands every page a few more values,** so other parts draw shadows and lit edges that agree: `--lx` and `--ly` (which way shadows fall: every offset is a multiple of them), `--hx` and `--hy` (the edge that catches the light), `--light-at` (where the light is, for gradients), `--shadow-low`, `--shadow-mid` and `--shadow-high` (what raised things cast at three heights), `--drop-low` and `--drop-rim` (the low shadow and the lit rim as a `filter`, for torn, clipped or taped shapes, which `box-shadow` would draw as a rectangle), `--edge-lit` (a one-pixel lit edge, seen on dark pages) `--shade` (the colour of shadows), and `--lamp` with its numbers `--lamp-lch` (the colour of light things give off: tungsten gold by default, turned by the sky; a site that wants its light in its own colour sets `--lamp: var(--accent)`). Paper lying on paper takes the low shadow, as `box-shadow` for plain rectangles and `filter: var(--drop-low)` for any other shape, never both. Colours of light are written as numbers inside `oklch(var(...))`. A page that goes dark at night is the colour part's tone switching, driven by the light part's clock.

**The other parts hand on values the same way,** so no part guesses at another's decisions:

| Values | Set by | For |
|---|---|---|
| `--radius-small`, `--radius`, `--radius-large`, `--radius-check` (never over 5px), `--radius-control`, `--radius-field`, `--corner-shape` | corners and shapes | every rounded thing: labels, buttons and sheets, panels, tick boxes, the main button, fields; `round` or `bevel` |
| `--space-1` to `--space-9`, `--gap-inside`, `--gap-items`, `--gap-groups`, `--gap-sections`, `--pad`, `--gutter`, `--page`, `--edge` | density | spacing by use (each gap at least 1.5 times the one inside it), a sheet's padding (a thick frame adds its own width to it), page width and side margin |
| `--measure` | lettering | the longest line of reading text |
| `--dur-short`, `--dur-medium`, `--dur-long`, `--dur-step`, `--ease-out`, `--ease-in`, `--ease-in-out`, `--ease-spring` | motion | every transition and animation; all zero unless the visitor's device allows motion |

**Decorations come in tiers.** Every decoration a part draws (background drawings, frame ornaments, lettering marks) carries `data-deco="few"`, `"more"` or `"most"`; density's fill decides which tiers show, and a phone drops one. The background decides what drawings exist; the fill decides how many of them show.

**Goes with** lines in a layered guide name another part's option by layer: `density: fill open`, `light: glow lamp`; a part with plain options is named `part: option`.

**On a dark page, shadows hardly show.** Raised things get a lighter `--surface-raised` instead, and texture is tuned separately: grain set for a light page looks muddy on a dark one. Every layered option has a "Light and dark" line saying what changes, and its swatch book shows it on both.

**Each decision has one owner.** Where two parts reach for the same thing, the owner wins, whatever the order:

| Decision | Owner |
|---|---|
| Page colour, text colours, accent | colour |
| Shadows, glow, where light falls | light |
| Every drawn line and edge: borders, ornaments on them, dividers, torn or wavy edges of sheets and between sections | frames (the colours are `--line`, `--ink-soft` for a control's edge, `--accent-edge`, from colour) |
| Corner radius (`--radius`) and the silhouettes of small things: buttons, fields, tags, badges, picture masks | corners and shapes (`shapes`) |
| Spacing, how full the page is (how many of the other parts' decorations show: each is tagged `data-deco="few|more|most"`), page width, columns and gutters | density |
| What surfaces seem made of: their texture and how they are laid on | materials |
| What lies behind the sections | background |
| Typefaces, sizes, weights, the type scale and the reading measure (`--measure`) | lettering |
| How pictures and icons are drawn, and stand-in art | picture style (`pictures`) |
| What moves, and how | motion |

So a fine-paper sheet under "no frames" has no border, and when torn paper and paper-and-tape give different shadows, the light part's shadow is used. A site guide that settles a clash some other way says why.

**A layered part guide** has, in order: `## Choosing`; `## Layers`, each layer a `### ` heading with `- Layer:`, `- Owns:` and `- Default:` lines, then its options as `#### ` headings with `- Id`, `- Status`, `- Looks like`, `- Made with`, `- Careful`, `- Light and dark`, `- Personality`, `- Goes with` and `- Used on`; `## Starting points`, each with `- Id`, `- Picks` (`texture: grain; drawings: lots`), `- Personality`, `- Looks like` and `- Used on`; `## Swatch book`; `## Not covered yet`. Its swatch book loads `tokens.css` and `swatches.js` from `tests/parts/`, marks each option `data-option="<layer>:<id>"` and each starting point `data-option="start:<id>"`, and is tested with `swatchTest()`, which draws everything on a light page and a dark one. `style check <part>` checks all of this. Two things the pilot found: a tile drawn as an SVG data URI cannot read CSS custom properties, so draw texture tiles as a `mask-image` over a background colour from the shared names (a list of masks starts with a transparent layer, or an all-`none` pick paints a solid sheet over everything); and `swatches.js` copies each swatch for the dark page and strips ids inside it, so shared SVG symbols and filters (`<symbol>`, `#pen`) sit outside the swatches.

## Writing a part's code to be lifted out

`blueprint.py style css` writes a site's starter stylesheet from its picks (`style css <mockup folder>`, or `style css --recipe <name> --out <file>`): it takes each picked option's code from its part guide, in the owners' order (colour, light, density, shapes, lettering, background, materials, frames, pictures, motion), adds the recipe's tuned values, copies the fonts it loads, and lists anything it could not find. For that to work, every option in a layered part carries its code in a block fenced as ` ```css assemble `, written so it can be lifted out alone:

- **`&` is the page root.** `& { --ground: ...; }` becomes `:root { ... }`. Values go there.
- **Style only the shared hooks, plain elements and your own classes.** The hooks are the page's pieces, the same on every site: `.page` (the wrapper inside `<body>`), `.band` (a section of the page), `.sheet` (a surface with words), `.panel` (a raised box: a dialog, a menu), `.btn` and `.btn-main` (buttons, and the one main one), `.field`, `.tag` and `.badge` (labels), `.label`, `.lead`, `.picture` (a picture and its frame), `.deco` (any decoration, with `data-deco="few|more|most"`), `.rule`, `.icon`, `.mark`. Anything else a part needs is named after it: `.background-sign`, `.frames-corner`, `.materials-tape`.
- **Set only shared names and values, or your own beginning with the part's name:** `--frames-ring-width`, never `--grain`, which two parts once both used.
- **Name animations after the part** (`@keyframes motion-breathe`), and load only `fonts/<file>` (copied in from `library/tests/parts/fonts/`) or data addresses.
- **Respect the owners.** Materials paints a sheet's fill; frames draws its border and edge (a torn edge is the material's `--sheet-fill` painted on the sheet's `::before` through `--sheet-mask`, so the sheet itself is never cut); light gives every shadow; shapes gives every radius. Code that reaches into another part's decision is a clash, whichever order it lands in.
- **An option that draws nothing** still has a block, holding only a comment, so the stylesheet says it was chosen.
- **SVG pieces** an option draws with (a pen filter, a sign as a `<symbol>`) go in a block fenced ` ```html assemble `; `style css` puts them into `parts.js`, which adds them to the page.
- **Code every option needs, whatever the pick,** goes under `## Base` in the part guide, in the same kinds of block.

**Who draws where.** Parts share a page, so each invisible layer of a hook belongs to one part, and the stacking order is fixed:

| Layer | Belongs to | For |
|---|---|---|
| the root's background | colour | the page colour |
| `.page::before`, `.page::after` | background | texture, and the tile of small signs |
| `.band` background, `.band::after` | background | a band's colour (`--band-*`) and its texture; the band's drawings (`aria-hidden`) at `z-index: 0` |
| `.band::before` | frames | the edge between this section and the one above |
| `body::before`, `body::after` | light | the lamp, sky and vignette, fixed over the bands and under the sheets (blend layers at `z-index: 1`) |
| `.sheet`, `.panel`, and every child of a band that is not `aria-hidden` | stacked at `z-index: 2`, above light's layers (the rule is in light's Base and background's Base) | words keep their colour; neither `.page` nor `.band` may be a stacking layer (no `isolation`, `z-index`, `filter`, `transform` or `opacity` on them), or a blend cannot reach the bands and the sheets in them go under the light |
| `.sheet` background | materials, as `--sheet-fill` | what the paper is |
| `.sheet::before` | frames | a shaped sheet's paper (torn, cut, deckled): it paints `var(--sheet-fill)` through the shape `--sheet-mask`, so the sheet itself is never cut and its shadow and tape stay whole |
| `.sheet::after` | frames | rings and an outline drawn along the shape |
| `.materials-mat` (a span inside the sheet) | materials | texture, wear and tilt; masked with `var(--sheet-mask, none)` |
| `.materials-fix` (a span inside the sheet) | materials | tape, pins, clips, string: never masked |
| `.btn::before`, `.btn::after` | shapes | a cut button's silhouette (motion eases colours instead of using a veil) |
| `filter` on `.sheet`, `.panel`, `.btn` | light | shadows, so they follow any shape |

Motion may animate any of these layers (an `animation` or `transition`, nothing else) without owning them: the lamp breathes on light's layer. `.page` and `.band` are never stacking layers (no `isolation`, `z-index`, `filter` or `transform`), or light's layers could not sit between a band and its sheets. `style check` flags a part that draws on another's layer, and a stacking layer on `.page` or `.band`.

**Markup an option needs** beyond the hooks (a sign, an ornament, a texture span) is written on a `- Needs markup:` line in the option; `style css` lists those for the picks, so the builder knows what to add to the page.

**Scripts** an option needs (a clock that turns the sky) go in a block fenced ` ```js assemble `; `style css` writes them, with the SVG pieces, into `parts.js` beside the stylesheet, which works from a page opened from a folder.

`style check <part>` checks each block against these rules. The swatch book stays the place to see an option; the assembly block is the same code, tidied so it stands alone.

## Recipes

A **recipe** is a whole look written as part picks: a short page, `style-recipe-<name>.md`, instead of a long feel guide. Most of a look is in the parts already; what a recipe adds is the two to four things made for that look that no part can give (the field journal's one sunny sketch taped in; its pencil marks that count things). A site names one in the blueprint as `project.style.recipe` and may change it one part, or one layer, at a time: `{"recipe": "field-journal", "parts": {"light": {"sky": "dusk"}}}` keeps the recipe's light and changes its sky. A pick for a part that names a starting point replaces the recipe's pick for that part.

A recipe may also tune shared values for its look under a `"values"` key in its picks (`"values": {"texture-strength": "0.06"}`), which `style css` writes last. A recipe has, in order: front matter (`name: <Name> (a recipe)`, `summary`, `kind: recipe`, `personality` (one of the five), `checked`, `source`); `# <Name>` and two or three sentences on what it is for; `## Picks`, one JSON block of part picks in the same form as `project.style.parts`, at least three parts and usually colour, light, lettering and density; `## What makes it`, two to four things made for the look, beyond the picks; `## Notes from the owner`, the owner's words about it, where there are any; `## Used on`; `## Not covered yet`. `style check <recipe>` checks that every pick exists and suits the recipe's personality (or that "What makes it" says why one does not). Recipes the user makes are kept in their own styles folder, like their guides.

A new look starts as a recipe: pick the personality, then a starting point or layers for each part, look at it, and write down what had to be made for it. A recipe becomes a feel guide only if the look needs rules the parts cannot hold.

## Use it properly

Before drawing anything, write the design brief (first note) and set the tokens. Everything on the page then uses a token; nothing gets a one-off size, colour or gap. A starting set, to be changed for each project:

```css
:root {
  /* type: two families at most, one scale */
  --font-body: 'Source Serif 4', Georgia, serif;
  --font-display: 'Fraunces', Georgia, serif;
  --text-s: 0.875rem;                               /* captions, labels */
  --text-m: clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem);  /* body, 17 to 19px */
  --text-l: clamp(1.375rem, 1.2rem + 0.8vw, 1.75rem);   /* subheadings */
  --text-xl: clamp(2rem, 1.5rem + 2.5vw, 3.25rem);      /* page heading */
  --measure: 66ch;                                  /* longest line of reading text */

  /* space: one scale, used for every margin, padding and gap */
  --space-1: 0.25rem;  --space-2: 0.5rem;  --space-3: 0.75rem;  --space-4: 1rem;
  --space-5: 1.5rem;   --space-6: 2rem;    --space-7: 3rem;     --space-8: 4rem;  --space-9: 6rem;

  /* colour: two neutrals and one accent, each named for its job. These are the shared names
     ("Parts, layers and the shared colour names"); when the colour part is picked, it sets them all */
  --ground: #f7f4ee;          /* about 60% of the page */
  --surface: #ffffff;         /* about 30% */
  --ink: #1c1f23;
  --ink-soft: #565d66;        /* still at least 4.5:1 on the ground colour */
  --line: #d8d2c6;
  --accent: #2f5d50;          /* about 10%: actions and the one thing to notice */
  --on-accent: #ffffff;
  --accent-edge: #2f5d50;

  /* finish: one of each. When the light part is picked, it sets --shadow-low, --shadow-mid and --shadow-high */
  --radius: 10px;
  --shadow-mid: 0 1px 2px rgb(0 0 0 / 0.06), 0 8px 24px rgb(0 0 0 / 0.06);
}
```

## Before showing a mockup

1. Squint at it, or blur a screenshot. The most important thing should still stand out, and groups should still read as groups.
2. Count: typefaces (two at most), text sizes in view (about three), accent colours (one, unless a stacked guide asks for more), primary buttons in view (one).
3. Measure the longest line of reading text. Over 75 characters is too long.
4. Look at it at phone width and at a very wide window, and run the list in `style-mobile.md`.
5. Put it next to the last mockup made of a different site (not another version of this one). If they could swap skins without anyone noticing, the brief was not followed. If the two share a lead guide, they will share its feel; what must differ is what the site is about (its subject, its people, its signature), and the site's guide says what does.
6. Run the template test (see "It must not look like a template" below): count the tells on the page, and name three things on it that were made for this site alone. Write the three in the site's own guide. If there are not three, it is not ready to show.
7. With more than one feel guide stacked, run the test under "When guides are stacked": could someone tell which one leads?

## Notes

### Write a design brief before any HTML
- Status: draft
- Source: judgement
- Rule: eight lines, written down and shown to the user before drawing. Who it is for. Who is behind it: one person, a small team or a company. The one thing a visitor must be able to do. The tone in three words. The one thing people should remember about how it looks. What it must not look like. How full the page should feel: spare, balanced or dense. Which guides are stacked, and how far each one reaches: name the parts of the site each guide governs.
- Learned on Greenfire Herbs, 2026-10-03: the first version followed its brief ("warm, earthy, handmade") and still came out "too clean and cold, more like a professional site", because the brief never said one person makes the soap at home, and because the sales guide was allowed to govern the whole site when it should only have governed the buying steps.
- Why: a mockup with no brief gets the default look: a centred heading, three cards, a blue button. The brief is where the decisions that make one site different from the next are taken.

### Decide where the detail goes
- Status: draft
- Source: the owner's critique of the first three artistic mockups, 2026-10-03, and a study of seven acclaimed sites
- Rule: before styling, give every part of the page one of three levels. Signature: one custom piece unique to this site. Styled: a designed treatment that echoes the signature. Quiet: tokens only. The feel guide that is stacked says which parts get which level. Never go without one. If no guide fits, ask the user which they want: a guide made for this kind of site (`references/jobs/style-guide.md` in the skill folder), or the nearest one, with the brief saying what it lacks and this site's own detail map giving it a signature piece at the top and a styled repeated item. Do not choose for them. Spend the effort in that order and stop.
- Learned on the volunteer sign-up page, 2026-10-03: no feel guide was stacked because none fitted, so everything was quiet except one detail. The owner: "very plain and used the same format a lot of websites do, so it looked like I made it with a cheap make-your-own-website tool."
- Why: a page where everything is quiet reads as plain, and a page where everything is styled reads as noise. What separates good sites is where the detail was put.

### It must not look like a template
- Status: draft
- Source: the owner's critique of the volunteer sign-up page, 2026-10-03: "very plain and used the same format a lot of websites do, so it looked like I made it with a cheap make-your-own-website tool." The list of tells is judgement, written by comparing that page with the sites studied for the feel guides.
- Rule: a page passes when a visitor could not have guessed its look before opening it. Two checks, both before anyone is shown the mockup.
  - **Count the tells.** Each of these is what a site-builder gives you before you have decided anything. One or two on a page are harmless. Three or more and the page reads as a template, however carefully the rest is done.
    1. The top is a heading, a sentence and a button, with nothing made for this site beside or behind them.
    2. Every repeated item is the same white box with rounded corners and a soft shadow.
    3. A row of three equal boxes, each an icon over a heading over two lines.
    4. The logo is a letter in a circle or a square.
    5. A count or a state is a thin bar or a small pill.
    6. Headings are the reading face made bigger and bolder, and the biggest is under three times the body size.
    7. The colour is a pale ground, white boxes and one accent that appears only on buttons and links.
    8. Every section is the same width, in one centred column, with a straight edge between it and the next.
    9. Nothing on the page was drawn, lettered or photographed for it: no picture that could only belong to this site.
    10. The words would fit any organisation: "Welcome to", "Get started", "Learn more", "Submit".
  - **Name three things a template would not have.** Three things on the page that exist only because of what this site is about: a signature piece, the way the repeated item is drawn, a headline in the owner's voice, a material. Write them in the site's guide under "Not a template because". If you cannot name three, go back to the detail map.
- Careful: this is not a call for decoration everywhere. A professional site passes with one strong signature, a designed repeated item and chosen type; the rest stays quiet. The tells are about nothing having been chosen, not about there being too little.
- Why: every other rule in this guide can be met by a template. Tidy spacing, good contrast and one accent colour are exactly what site-builders are good at, so following them alone produces their look.

### Who is behind the site sets how polished it is
- Status: draft
- Source: the owner's critique of the first Greenfire Herbs mockup, 2026-10-03
- Rule: a site made by one person shows the person: their voice in the first person, their name, their hand in the details, and edges that are not machine-straight. A company's site is even and exact. A mockup that is more polished than the business behind it reads as cold, however warm its colours.
- Why: tidy alignment, uniform cards and a neutral voice are what "professional" looks like. They are right for a firm and wrong for a kitchen table.

### The look comes from the subject
- Status: draft
- Source: judgement
- Rule: choose the typeface, palette and imagery because of what the site is about, and be able to say why in a sentence. A haiku site and a tutoring site should not be the same page with different words.
- Why: reusing the last mockup's look is what makes mockups feel copied.

### Let the content choose the layout
- Status: draft
- Source: judgement
- Rule: decide the layout after listing the real content, not before. A page of long reading text, a page of many short items and a page with one form are three different layouts. Do not start from "hero, three cards, footer".
- Why: the same skeleton filled with different words is the other half of the copied feeling.

### Body text is at least 16px, and 17 to 20px on pages meant for reading
- Status: draft
- Source: USWDS typography ("at least an effective size of 16px"); Practical Typography ("15–25 pixels on the web"); GOV.UK type scale (body is 19px)
- Rule: never set running text below 16px. Captions and labels may go down to 14px.
- Check: measurable. Smallest font size used for paragraph text.

### Lines of reading text are 45 to 75 characters long
- Status: draft
- Source: USWDS ("most lines of text should be 45–90 characters", 66 recommended); web.dev Learn Design (45–75, 66 ideal); WCAG 1.4.8 (no more than 80)
- Rule: set a maximum width on text in `ch`, about `66ch`, then count. `ch` is the width of the digit 0, and letters are narrower: 66ch held 78 characters in IBM Plex Sans. Expect to end up between 50ch and 60ch. Short passages such as a caption or a card may be narrower. Nothing meant to be read runs the full width of a wide screen.
- Check: measurable. Characters per line in the widest paragraph.

### Line height is 1.5 for body text and tighter for headings
- Status: draft
- Source: USWDS (body "at least 1.5", headings between 1 and 1.35); web.dev (unitless values); WCAG 1.4.8 (space-and-a-half)
- Rule: body text `line-height: 1.5`, written without a unit. Headings 1.1 to 1.3. The larger the text, the tighter the line height.
- Check: measurable.

### One type scale with few steps
- Status: draft
- Source: Nielsen Norman Group ("use no more than 3 sizes: small, medium and large"; "limit how many elements are big to a maximum of 2"); GOV.UK type scale (16, 19, 24, 36, 48)
- Rule: define the sizes once as tokens: one for small text, one for body, and two or three for headings. A single view should not have more than about three sizes competing. Every piece of text uses a token.
- Check: measurable. Number of distinct font sizes on a page.
- Seen so far: Greenfire Herbs and the AP Biology tutor site each use five sizes on the page and both show all five in the first screen, with two of them large. "About three in view" has not been met on a site yet and may need rewording to "two large, and no more than five tokens". Not changed until the skill's owner has agreed.

### Two typefaces at most, and choose them
- Status: draft
- Source: Practical Typography ("the easiest and most visible improvement you can make to your typography is to use a professional font"); the limit of two is judgement
- Rule: one typeface for body text and at most one more for headings. Pick them for the subject; do not fall back to the system font because it is there. If a web font is used, host the files with the site (see `google-fonts.md` for why) and show text straight away while it loads.
- A site with a second look the visitor can switch to (a secret mode, a dark theme that is designed, not only darkened) may give that look its own two; count per look.
- Check: measurable. Number of font families in use.

### Text is aligned left and never justified
- Status: draft
- Source: USWDS (flush left, avoid justified); WCAG 1.4.8 (text is not justified); Practical Typography ("use centered text sparingly")
- Rule: reading text is left-aligned. Centre only short, self-contained things: a heading over a centred block, a single line under it.

### Emphasis is rare
- Status: draft
- Source: Practical Typography ("use bold or italic as little as possible, and not together"; "never underline, except perhaps for web links"; "all caps are fine for less than one line of text"; "5–12% extra letterspacing with all caps")
- Rule: bold or italic, not both, and not for whole paragraphs. Underline means link and nothing else. Capitals only for labels shorter than a line, with a little extra letter spacing.

### More space above a heading than below it
- Status: draft
- Source: USWDS (paragraphs "at least 1em" and "no more than 1.5em" apart; space above a heading "at least 1.5 times" the space below)
- Rule: a heading sits close to the text it introduces and well clear of the text before it. Paragraphs are one line-height apart or a little less.

### Real punctuation
- Status: draft
- Source: Practical Typography ("use curly quotation marks, not straight ones"; "don't confuse hyphens and dashes"; "make ellipses using the proper character")
- Rule: curly quotes and apostrophes, a real dash where a dash is meant, the single ellipsis character.

### Sizes scale smoothly, never with the window alone
- Status: draft
- Source: web.dev Learn Design (use `clamp()`; do not rely only on viewport units, which stop the reader resizing text)
- Rule: large text sizes use `clamp(minimum, preferred, maximum)` with a `rem` part in the middle value. Never `font-size` in `vw` alone.

### One spacing scale, used for everything
- Status: draft
- Source: GOV.UK spacing scale (0, 5, 10, 15, 20, 25, 30, 40, 50, 60px); choosing one scale and keeping to it is the point, the exact steps are judgement
- Rule: define about nine steps once. Every margin, padding and gap is one of them. No in-between values.
- Check: measurable. Distinct spacing values in the stylesheet that are not on the scale.

### Space shows what belongs together
- Status: draft
- Source: Nielsen Norman Group ("items that are visually closer together are perceived as part of the same group"; "an element that has more space around it ... will receive more attention")
- Rule: the gap inside a group is always smaller than the gap between groups. A label is nearer to its field than to the field above. Sections are separated by clearly more space than anything inside them.

### Use space before lines and boxes
- Status: draft
- Source: Nielsen Norman Group (use "borders or backgrounds" as containers when "varying whitespace alone is not enough")
- Rule: try separating things with space first. Add a border or a background only when space alone does not make the grouping clear. Not everything needs to be a card.

### Margins grow with the screen and content has a maximum width
- Status: draft
- Source: USWDS (horizontal margins from 1 unit on mobile up to 4–5 units on desktop); the maximum width follows from the line-length rule
- Rule: side margins are smallest on a phone and larger on wider screens. The page content stops growing at a set width and centres.

### Edges line up
- Status: draft
- Source: judgement
- Rule: the left edges of headings, text, fields and cards fall on a small number of shared vertical lines. A new indent needs a reason.

### Choose symmetry or asymmetry on purpose
- Status: draft
- Source: Nielsen Norman Group (symmetrical balance reads as static and quiet, asymmetrical as dynamic)
- Rule: decide which suits the tone in the brief and keep to it across the site.

### One thing per screen is the most important
- Status: draft
- Source: Nielsen Norman Group ("make the most important element biggest"; "limit how many elements are big to a maximum of 2")
- Rule: for each screen, name the single most important element and make it win on size, weight, colour or position. At most two large elements on a screen.

### No more than three levels of emphasis
- Status: draft
- Source: Nielsen Norman Group ("use no more than 3 contrast variations ... if everything is contrasted, then nothing stands out"; do not reduce text contrast to de-emphasise)
- Rule: primary, secondary and quiet. Make something quieter with size, weight or position; never by fading text below the contrast minimum.

### One primary button in view
- Status: draft
- Source: judgement
- Rule: one filled, accent-coloured button per view for the main action. Other actions are outlined or plain. Destructive actions are never the most prominent thing unless the screen exists to confirm one.

### Start with three colours
- Status: draft
- Source: Nielsen Norman Group ("limit your palette to three colors"; the 60-30-10 proportion; dominant and secondary usually neutral, accent for key interactive elements)
- Rule: two neutrals and one accent, in roughly 60, 30 and 10 percent of the page. Further colours are added only for meaning (success, warning, error) and only where that meaning occurs.

### A colour means the same thing everywhere
- Status: draft
- Source: Nielsen Norman Group ("if you use bright blue for your calls to action on one screen, that same color should be used for calls to action everywhere")
- Rule: the accent marks things that can be acted on. Do not also use it for decoration.

### Text contrast is at least 4.5 to 1
- Status: draft
- Source: WCAG 2.2 success criterion 1.4.3 (4.5:1; 3:1 for large text, meaning at least 24px, or 18.5px bold)
- Rule: every text and background pair meets it, including muted text, placeholder-style hints and text on coloured buttons.
- Check: measurable. The skill's audit already reports it.

### Edges of controls, icons and focus rings are at least 3 to 1
- Status: draft
- Source: WCAG 2.2 success criterion 1.4.11
- Rule: the border that shows where a field is, an icon that carries meaning, and the focus outline all reach 3:1 against what is next to them.

### Never colour alone
- Status: draft
- Source: Nielsen Norman Group ("do not rely only on color to communicate visual hierarchy")
- Rule: an error has an icon or the word as well as red. A selected item has a mark or weight change as well as a colour.

### Things you tap are at least 24 pixels, and main actions 44
- Status: draft
- Source: WCAG 2.2 success criteria 2.5.8 (24 by 24 CSS pixels minimum) and 2.5.5 (44 by 44 enhanced)
- Rule: buttons, links that stand alone and icons that can be pressed are at least 24 by 24. The main actions on a page, and anything in a phone layout, are at least 44 tall.
- Check: measurable. Size of each interactive element.

### One radius, one shadow, one border, one icon set
- Status: draft
- Source: judgement
- Rule: pick each once as a token and use only that. Mixed corner radii and shadows pointing different ways are the quickest tell of an unfinished design.

### No library defaults showing
- Status: draft
- Source: judgement, from the first redesign made with this guide
- Rule: when a component library or framework is used, every colour, font and corner radius on the page comes from the project's tokens. A default blue button, a default grey border or the library's own font next to a chosen design is a leak. Map the tokens onto the library once, in one place (for Web Awesome, see the theming note in `web-awesome.md`), then look for anything still wearing the default.
- Why: leftover defaults are what make a designed page look like a template again.

### Real words at real lengths
- Status: draft
- Source: judgement
- Rule: no filler text. Write plausible content for the subject, and include the awkward cases: a long name, a long title, a number with many digits, an empty list. Then look at each awkward case at phone width: in the first redesign a poem line that fitted on a desktop wrapped mid-phrase on a phone, and the layout needed a rule for what a too-long line does.

### Draw the other states
- Status: draft
- Source: judgement
- Rule: hover, keyboard focus, pressed, disabled, error and empty are part of the design. If a state is not drawn, the blueprint describes it.

## Sources

Read on 2026-10-03:

- Practical Typography, summary of key rules: practicaltypography.com/summary-of-key-rules.html
- US Web Design System, typography: designsystem.digital.gov/components/typography/
- GOV.UK Design System, type scale and spacing: design-system.service.gov.uk/styles/
- Nielsen Norman Group: 5 principles of visual design; visual hierarchy; using colour
- web.dev, Learn Design, typography
- WCAG 2.2 Understanding documents: 1.4.3, 1.4.8, 1.4.11, 2.5.5, 2.5.8

Read on 2026-10-07, for "Parts, layers and the shared colour names":

- W3C Design Tokens format, first stable version: w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/
- Nathan Curtis, Tokens in design systems (options and decisions): eightshapes.com/articles/tokens-in-design-systems/
- Material 3 colour roles (developer.android.com/develop/ui/compose/designsystems/material3) and Material dark theme (m2.material.io/design/color/dark-theme)
- Radix Colors, understanding the scale; Radix Themes, theme settings: radix-ui.com
- shadcn/ui theming: ui.shadcn.com/docs/theming
- Carbon colour overview: carbondesignsystem.com/elements/color/overview/
- Atlassian foundations: atlassian.design/foundations
- Open Props (noise and shadow strength): open-props.style
- MDN, light-dark(): developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark
- Josh W. Comeau, designing shadows: joshwcomeau.com/css/designing-shadows/
- Refactoring UI, choose a personality (a community summary of the book): rfui-docs.onrender.com/choose-a-personality

Not yet researched, and so not covered: data-heavy pages such as tables and dashboards.

## Questions it raises

- What three words describe how this site should feel?
- Is there an existing logo, colour or typeface to start from?
- Which existing sites does the owner like the look of, and which do they dislike?
