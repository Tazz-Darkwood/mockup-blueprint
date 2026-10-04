---
name: Warm (a feel guide)
summary: Stack on top of the general style guide when the site belongs to a club, a volunteer group, a charity, a community project or any small organisation that should feel like the people in it, not like a company. Says where the hand-made detail goes and how much; the specifics belong to each site's own guide.
kind: feel
detect: []
checked: 2026-10-03
source: a study of twelve community organisations' sites, listed at the end
---

# Warm

A feel guide. It is stacked on `style-guide.md` (the general guide) when a site should feel warm, neighbourly and made by its own people, and it gives way to the site's own guide wherever that says something more specific. The general guide's accessibility minimums (contrast, text size, tap target size) still hold.

It exists because of one mockup. A volunteer sign-up page was made with no feel guide, since none on the shelf fitted, and every rule it followed told it to stay tidy and quiet. The owner's verdict: "very plain and used the same format a lot of websites do, so it looked like I made it with a cheap make-your-own-website tool." Tidy and quiet is the wrong default for a club. Twelve well-known community sites were then studied, and almost none of them is tidy.

Like the other feel guides, this one does not describe a look. Chalk on tarmac, cut paper on dark green, red slanted blocks over a photo of runners: the twelve look nothing alike. What they share is **that somebody's hand is visible, and where they let it show**.

## Levels of detail

Every part of a page gets one of three levels:

- **Signature.** One custom piece, unique to this site, that a visitor would describe to someone else.
- **Styled.** A designed treatment that echoes the signature in material, colour or shape.
- **Quiet.** Plain. Tokens only, no decoration.

## The detail map for a warm site

| Part of the page | Level | Seen on |
|---|---|---|
| Top of the first page | Signature: the real people or the real place, with a few very large words | Photographs of the organisation's own people on about 10 of 12 |
| Something made by hand | Styled, in two or three places: lettering, a squiggle, cut paper, chalk, a torn edge | About 9 of 12 |
| Shapes and edges | Styled: at least one frame or edge that is not a straight rectangle | About 8 of 12 |
| Colour | Bold and flat, in big areas. Not pastel, not white with one accent | Most of the 12 |
| Headline typeface | A face with character, set very large, over a plain face for reading | Most of the 12; the largest text was 86 to 152px on 5 |
| A material from the subject | Styled: the page is "made of" something from the organisation's real life | Clearly on 4 of 12 |
| The headline's words | A slogan someone would say out loud, not a description of the page | About 6 of 12 |
| The repeated item (an event, a project, a group) | Styled: an object from the organisation's real life | Little evidence; from the volunteer page |
| Navigation, forms, fields, buttons, footer | Quiet in shape; the bold colour is allowed | Not recorded in the study; assumed |

## Use it properly

1. In the design brief, answer two questions before drawing: **what would this organisation pin to a wall?** (a poster, a sign-up sheet, a banner, a chalkboard) and **what is it made of?** (paper and pins, chalk, paint, felt). The signature and the material come from those answers.
2. Go down the detail map and decide, for this site, what each row will be. Write the answers in the site's own guide.
3. Spend the effort in this order: the top, then the repeated item, then two or three hand-made marks. Then stop. Forms and controls stay quiet.
4. Before showing the mockup, run the template test in the general guide ("It must not look like a template"). A warm site that fails it has not used this guide.

## Notes

### The top shows the people or the place
- Status: draft
- Source: study, about 10 of 12 opened with a photograph of the organisation's own people doing the thing: volunteers in red shirts (GoodGym), a child writing (826 Valencia), a beekeeper (Hackney City Farm), people walking (parkrun), a crowd holding painted banners (Camerados). None used a picture that could have come from a photo library.
- Rule: the first screen is built round a picture of the real people or the real place, with the headline on or beside it. Plan the slot for it at full size.
- In a mockup: there are no real photographs yet, and a stock photograph is worse than none. Fill the slot with artwork made for this site in its own material (cut paper, a drawing), say in the blueprint that a real photograph belongs there, and ask who has photographs and whether the people in them agreed to be shown.

### Something on the page was made by hand
- Status: draft
- Source: study, about 9 of 12. Hand-drawn circles and a squiggle arrow round words (826 Valencia), hand-lettered banners (parkrun), cut-paper lettering and drawings (Incredible Edible), a brushed logo, bunting and a torn edge (Camerados), chalk writing and a chalk line that wanders between sections (Playing Out), a stencilled heading (Hackney City Farm).
- Rule: two or three things on the page are visibly made by a hand: drawn, cut, lettered, stuck on. Draw them for the site; do not use an icon set. They sit on headings, on the edges of sections and on the repeated item, never on form fields.
- Why: it is the plainest sign that people, not a product, are behind the site. It is also the thing a site-builder template cannot supply.

### Break the rectangle
- Status: draft
- Source: study, about 8 of 12. Photographs in blob-shaped masks (Men's Sheds, Eden Project Communities), headings on tilted blocks (GoodGym, Incredible Edible), a band with a wavy edge (Men's Sheds), a torn-paper edge (Camerados), a big curve across a band (Eden Project Communities), a blob behind overlapping cards (Buy Nothing).
- Rule: at least one edge between sections is not a straight line, and at least one thing is tilted, overlapping or cut to a shape. Tilts are small (one to three degrees) and never on text meant for reading or on anything typed into.
- How, learned on the volunteer page: draw the paper as a shape behind the words (`::before`, clipped to an uneven outline) and turn only that. The paper looks pinned up crooked and the words stay level and sharp. `check` reads the colour of a shape drawn this way when it measures contrast, and of one drawn as an empty element laid over the whole box (`position: absolute; inset: 0`) behind the words.

### Colour is bold and flat, in big areas
- Status: draft
- Source: study, most of the 12: bright yellow across the whole first screen (Camerados), red and black blocks (GoodGym), deep blue with orange (Repair Café), dark green bands (Incredible Edible), orange and teal (parkrun, Men's Sheds).
- Rule: choose one strong colour and give it a whole band or block, not only the buttons. A second and third strong colour are allowed where each belongs to a thing: one per event, per project, per section. This widens the general guide's three colours; it does not lift the contrast minimums, so check every text and background pair.
- Why: a pale ground with one accent on the buttons is what every template looks like before anyone has chosen anything.

### A headline face with character, very large
- Status: draft
- Source: study. Most paired a characterful display face with a plain one for reading: condensed gothic capitals (826 Valencia), a cut-paper face (Incredible Edible, Londrina Solid), a stencil (Hackney City Farm), a soft serif (Men's Sheds, Moranga; Buy Nothing, Lora), rounded (Eden Project Communities, Rubik). The largest text was 86 to 152px on 5 of the 12.
- Rule: the display face is chosen for the material (a poster face for a poster, a stencil for a crate) and the headline is far larger than a template would make it: at a wide window, four or more times the body size. The reading face is plain and comfortable. Still two families at most: hand-made marks are drawn, not typed in a third, handwriting face.

### The headline is something a person would say
- Status: draft
- Source: study, about 6 of 12: "Toss it? No way!" (Repair Café), "If you eat you're in" (Incredible Edible), "Free, for everyone, forever" (parkrun), "Do good, get fit" (GoodGym), "Let's walk" (parkrun).
- Rule: the largest words on the page are a short line in the organisation's own voice, the kind painted on a banner. What the page is for ("Volunteer sign-up") goes in the title and a smaller line.

### Take a material from the subject
- Status: draft
- Source: study, clearly on 4 of 12: chalk on tarmac for a street-play charity (Playing Out), painted wooden planks for a city farm (Hackney City Farm), cut paper and garden things for a growing project (Incredible Edible), a brick wall and bunting for a street-level movement (Camerados).
- Rule: name one material from the organisation's real life and make the page out of it: its ground, its edges, the frame of its repeated item. One material, used consistently, is what stops hand-made details looking like stickers.

### The repeated item is an object from the organisation's real life
- Status: draft
- Source: judgement, from the volunteer page. The first version listed events as white cards with rounded corners, a soft shadow and a thin bar, and was called plain. The study adds little: only first screens were looked at.
- Rule: ask what this item is when it is not on a screen (a notice pinned to a board, a ticket, a seed packet, a name on a sheet) and draw that. Each one may have its own colour and its own small drawing. Design one until it could stand alone as a picture, then repeat it.

### Numbers and states are drawn in the material too
- Status: draft
- Source: judgement, from the volunteer page, where "4 of 12 helpers still needed" was a thin bar and "last place" a pill.
- Rule: a count, a progress or a state is shown the way the organisation would show it by hand: names on a sheet, a row of places ticked off, a "FULL" stamp. The number is always also written in words, so nothing depends on the drawing.
- Seen on the volunteer page, second version: one paper hand for each helper needed, solid when taken and dotted when still wanted, with a stamp across a full event. Awaiting the owner's critique.

### Hand-made is not harder to use
- Status: draft
- Source: judgement. Several studied sites set text over busy photographs or in novelty faces where it was hard to read; that is not copied.
- Rule: fields, labels, buttons, error messages and long text are plain, straight and in the reading face. Decoration is hidden from screen readers and nothing a person needs is only in a drawing. Movement, if any, stops under the reduced-motion setting. The phone guide's sizes hold.

## What this guide does not give you

- It is built from organisations, not from one person's business. A single maker's site also needs the maker's own voice and name; see "Who is behind the site sets how polished it is" in the general guide. On the one maker's site made so far, a soap maker's shop, what worked was tape, pen lines, a little handwriting and the maker speaking in the first person.
- It will not suit an organisation that needs to look official first: a school's admissions page, a clinic, a grant-giving body. Use the professional guide there, and borrow at most the photograph of real people.

## Not covered yet

- Where each repeated item's colour and drawing come from on the real site. On the volunteer page it became a blueprint question: somebody has to pick a drawing when an event is added.
- Phones. The twelve were studied at 1440 pixels wide only. How much of the hand-made detail survives on a phone has only been tried on the volunteer page.
- Inner pages and forms. Only first screens, and one screen further down, were looked at.
- Motion.

## How these notes get approved

A note here is approved when it has held on two different sites built with this guide and the skill's owner has agreed with the result on both. First site: the volunteer sign-up page, agreed by the owner on 2026-10-03 ("looks great now, very styled, I love it"). A second site is still needed. One site is not enough: it cannot show whether the rule is about warm sites or only about that one.

## Sources

Studied on 2026-10-03 by opening each home page in a browser at 1440 pixels wide and looking at the first screen and one screen further down:

826 Valencia (826valencia.org), GoodGym (goodgym.org), Repair Café (repaircafe.org), Little Free Library (littlefreelibrary.org), parkrun (parkrun.org.uk), Incredible Edible (incredibleedible.org.uk), Men's Sheds (menssheds.org.uk), Camerados (camerados.org), Eden Project Communities (edenprojectcommunities.com), Playing Out (playingout.net), Hackney City Farm (hackneycityfarm.co.uk), Buy Nothing Project (buynothingproject.org).

How they were chosen: as community organisations known for their sites, not from an award list. A search for well-designed volunteer and community sites returned only site-builder companies' own blog posts, which were not used. So the set is one person's choice and leans British. Two were partly hidden when viewed (Repair Café by a cookie dialog, Little Free Library by a newsletter pop-up), which is why the counts say "about".

## Questions it raises

- Who has photographs of the organisation's own people and events, and did the people in them agree to be shown on the site?
- Is there an existing logo, banner or poster whose lettering or colours the site should take up?
- What would this organisation pin to a wall, and what is it made of?
