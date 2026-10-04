---
name: Phones (a general guide)
summary: How any page must work on a phone, whatever it is built with and whatever it is for. Read with the general style guide before creating any mockup. Most of it is measured by the audit, which opens every page at phone width.
kind: general
detect: ["<html"]
checked: 2026-10-03
source: published standards and research, and a study of 26 sites at phone width, listed at the end
---

# Phones

Part of the general layer of the style stack, beside `style-guide.md`. It applies to every site. The stacked guides and the site's own guide can add to it; they cannot switch off its minimums (no sideways scrolling, text size, tap size).

"A phone" here means a screen 390 pixels wide and about 840 tall, held upright. The narrowest width a page must survive is 320 pixels, which is also what a desktop page becomes when someone zooms to 400%.

## Phone first

Draw the phone layout before the wide one. One column, things in the order a visitor needs them, and the first screen decided on purpose. Then widen the window and add columns only where the content gains from them. A page drawn wide and squeezed afterwards puts things in whatever order the columns happened to stack, and that is how a tutor's portrait ends up below the first screen.

## What the audit measures

`audit` and `check` open every page at 390 pixels wide, and once more at 320. Findings appear under "On a phone".

| Finding | Stops the build? | Means |
|---|---|---|
| `mobile/sideways-scroll` | Yes | The page scrolls sideways at 390 wide. It names what sticks out |
| `mobile/tap-size` | Yes | Something to tap is smaller than 24 by 24 pixels |
| `mobile/sideways-scroll-narrow` | No | It scrolls sideways at 320 wide |
| `mobile/tap-height` | No | Something to tap is under 44 pixels tall |
| `mobile/text-size` | No | Reading text is under 16 pixels |
| `mobile/text-small` | No | Some text is under 14 pixels |
| `mobile/input-zoom` | No | A field's text is under 16 pixels, which makes an iPhone zoom in |
| `mobile/first-screen` | No | The page's main heading is not in the first screen |
| `mobile/fixed-bars` | No | Bars that stay on screen take more than a quarter of it |
| `mobile/bar-covers-end` | No | A bar fixed to the bottom hides the last content on the page |

Fix sideways scrolling first: a phone zooms out to fit a page that is too wide, and the other measurements are unreliable until it is gone. Links inside a sentence are not counted as things to tap. The check cannot judge the order things are stacked in, whether the first screen holds the right things, or how the page feels in a hand. Those need a person looking at it.

## What changes on a phone

Seen by opening 26 well-regarded sites at phone width: seven museums and studios, seven shops, six education sites and six tutoring companies.

| Part | On a phone | Seen on |
|---|---|---|
| Columns | One, for anything meant to be read. Two only for small tiles such as products or figures | All 26 |
| Navigation | Behind one menu button, when there are many links | 23 of 26 |
| Header | One row: the name and one to three icons. About 70 pixels tall | Median of 26 |
| Header when scrolling | Stays on screen | 16 of 26, taking 48 to 120 pixels |
| First screen | A heading, and usually a picture sharing the screen with it | Picture on 20 of 26 |
| Largest text | About 36 pixels, against 50 to 65 on a desktop | Median of 26 |
| Reading text | 16 pixels or more | 15 of 23 |
| Page length | Long: about seven screens | Median of 26 |
| Sideways scrolling of the page | None | 25 of 26 |

How the top of each kind of site translated:

- **Artistic.** The signature piece stays and fills the first screen: the painting, the block of colour, the large type. 7 of 7.
- **Shops.** The product picture, a short line and one button. The basket stays in the header. 6 of 7.
- **Education and tutoring.** A heading and one action, with a photograph of people in the first screen on 8 of 12. Three of the six tutoring companies keep a way to call in the header.

## Use it properly

1. Lay the page out at 390 wide first, in one column.
2. Write down what the first screen holds, in order, and why. Put it in the site's own guide.
3. Widen to a desktop and add columns where they help.
4. Run `audit` and clear everything under "On a phone".
5. Look at it at 390 and at 320, and scroll the whole page with a thumb in mind.

## Before showing a mockup

1. No sideways scrolling at 390 or 320.
2. The first screen says what the page is and offers the one action. If the top is meant to show a picture or a face, it is there too.
3. Everything that can be tapped is at least 44 pixels tall and is not crowded by its neighbours.
4. No reading text under 16 pixels and nothing under 14.
5. Bars that stay on screen take less than a quarter of it, and the last thing on the page is not hidden behind one.
6. Nothing needs hovering.

## Notes

### Lay out the phone first
- Status: draft
- Source: web.dev ("design the content to fit on a small screen size first, then expand the screen until a breakpoint becomes necessary")
- Rule: the first layout drawn is the phone's. Columns are added as the window widens.
- Learned on the AP Biology tutor site, 2026-10-03: drawn wide first, its portrait fell below the first screen on a phone and nobody had decided that.

### Change the layout where the content needs it, not at device sizes
- Status: draft
- Source: web.dev ("don't define breakpoints based on device classes ... let the content determine how its layout changes"; consider a breakpoint when a line of text grows past about ten words)
- Rule: widen the window slowly and change the layout at the width where it starts to look wrong. Two or three such points are normal.

### The page fits the screen and can be zoomed
- Status: draft
- Source: web.dev (the viewport tag with `width=device-width, initial-scale=1`; "we don't recommend" settings that "prevent the user from zooming")
- Rule: every page carries the viewport tag, and never switches off pinch-zoom.
- Check: the audit reports a missing tag and blocks the build if zoom is switched off.

### No sideways scrolling, down to 320 pixels
- Status: draft
- Source: WCAG 2.2 success criterion 1.4.10 (content shown "without requiring scrolling in two dimensions" at "a width equivalent to 320 CSS pixels"). Study: 25 of 26.
- Rule: nothing is wider than the screen. Give pictures a maximum width of 100%, let long words and addresses break, and avoid fixed widths. Things that need two dimensions, such as a data table, a map or a diagram, scroll inside their own box while the page stays still.
- Check: `mobile/sideways-scroll`, `mobile/sideways-scroll-narrow`.

### One column for anything meant to be read
- Status: draft
- Source: study, all 26. Nielsen Norman Group ("screen size is a serious limitation"; consider "the opportunity cost of each new element").
- Rule: reading text, forms and steps run in one column. Two side by side is for small, similar tiles only, and only if each still holds its content comfortably.

### Decide what the first screen holds
- Status: draft
- Source: Nielsen Norman Group's eye-tracking ("users spent about 57% of their page-viewing time above the fold", 74% in the first two screens; measured on desktops, so treat it as a direction, not a number for phones). Study: 20 of 26 put a picture in the first screen with the heading.
- Rule: the first phone screen says what the page is and offers the one action. Where a stacked guide says the top must show something, a signature picture, the product, a face, that is in the first screen as well, made smaller if need be. Write the list in the site's guide.
- Check: `mobile/first-screen` checks only that the main heading is there. The rest needs looking at.

### The order things stack in is a decision
- Status: draft
- Source: study. The tutoring and education sites went both ways: photograph then heading on Imperial, SOAS and Mathnasium; heading and button then photograph on Hull and Kumon.
- Rule: when columns become one, choose the order for a visitor arriving cold: what is this, can I trust it, what do I do. Do not accept the order the columns fell in.

### Reading text does not shrink; headings do
- Status: draft
- Source: the general guide's minimum of 16 pixels. Study: reading text was 16 or more on 15 of 23, and the largest text in the first screen had a median of 36 pixels.
- Rule: reading text is 16 pixels or more on a phone, labels 14 or more. Headings come down to roughly two-thirds of their desktop size, so that a heading is two or three lines, not five.
- Careful: eight of the studied sites set reading text at 15 or below, and fifteen had text under 14 in the first screen. Do not copy them.
- Check: `mobile/text-size`, `mobile/text-small`.

### Things to tap are 44 pixels tall, never under 24, and not crowded
- Status: draft
- Source: WCAG 2.2 success criteria 2.5.8 (24 by 24) and 2.5.5 (44 by 44). web.dev ("around 48 device independent pixels ... about the size of a person's finger pad area"; "spaced about 8 pixels apart"). Nielsen Norman Group (at least 1cm by 1cm).
- Rule: every button, standalone link, menu item and field is at least 44 pixels tall on a phone, with about 8 pixels between neighbours. Nothing that can be tapped is under 24 in either direction.
- Careful: this is the rule well-known sites break most. 24 of the 26 had something under 44 pixels in the first screen and 18 had something under 24. Do not copy them.
- Check: `mobile/tap-size`, `mobile/tap-height`. Spacing is not measured.

### Four links or fewer stay visible; more go behind a menu button
- Status: draft
- Source: Nielsen Norman Group ("if your site has 4 or fewer top-level navigation links, display them as visible links. If your site has more than 4 ... the only reasonable solution is to hide some of these"; hidden navigation cost "a more than 20% drop in discoverability" and made people 15% slower on phones). Study: 23 of 26 used a menu button, and all of those have many links.
- Rule: a small site shows its few links on a phone, in a row under the name. A site with more puts them behind one button that says "Menu" or carries a label for screen readers, and keeps the main action outside it.

### Bars that stay on screen are small and solid
- Status: draft
- Source: Nielsen Norman Group on sticky headers (keep them small; "an opaque color, different from the background of main content areas"; "it's best to not use animation at all"; ask whether its contents are "likely to be needed often"). Study: 16 of 26 kept a header on screen, taking 48 to 120 pixels. The limit of a quarter is judgement.
- Rule: everything fixed to the top or bottom, added together, takes less than a quarter of the screen, and a tenth is better. Bars are solid, not see-through. The page leaves room at its end so a bottom bar never covers the last content.
- Check: `mobile/fixed-bars`, `mobile/bar-covers-end`.

### The one action stays within reach on a long page
- Status: draft
- Source: an observational study of 1,333 people (Hoober, UXmatters: of those touching the screen, "one handed, 49%", "cradled, 36%", "two handed, 15%"; the author warns against designing from thumb-reach charts alone). Study: pages had a median of seven screens; three of six tutoring companies kept a way to call in the header.
- Rule: on a long page whose job is one action, keep that action on screen: in the header that stays, or in a bar at the bottom. One of the two, not both.
- Judgement, and thinly supported: only a few of the studied sites used a bar at the bottom.

### Fields are easy to fill with thumbs
- Status: draft
- Source: Nielsen Norman Group ("touch typing is impossible ... keys are crowded"). CSS-Tricks, on iPhones ("as soon as the font-size is 15px or less, the viewport will zoom into that input"). The iPhone behaviour was read, not tested here: the test browser is not an iPhone.
- Rule: ask for as little typing as possible. Text in fields is 16 pixels or more. Labels sit above their fields. Each field says what kind it is (email, telephone, number) so the right keyboard appears.
- Check: `mobile/input-zoom`.

### Nothing depends on hovering
- Status: draft
- Source: judgement. A finger cannot hover.
- Rule: anything revealed by pointing at it on a desktop is either always visible on a phone or opens with a tap.

### Do not hide content on a phone
- Status: draft
- Source: web.dev ("don't hide content just because you can't fit it on the screen. Screen size doesn't predict what a user might want to see")
- Rule: a phone visitor gets everything a desktop visitor gets. Shorten, reorder or fold things into sections that open, but do not remove them. A control that only repeats another one may be dropped.

### Pictures are cropped for an upright screen
- Status: draft
- Source: web.dev (give images a maximum width of 100% and state their width and height so the page does not jump as they load). The cropping is judgement.
- Rule: a wide desktop picture rarely survives being shrunk to a phone. Decide the phone crop: closer in, and usually taller.

### Long pages are fine; order them by importance
- Status: draft
- Source: study, a median of about seven screens and up to fourteen. Nielsen Norman Group (attention falls with depth; avoid "false floors" that look like the end of the page).
- Rule: do not shorten a page for phones by cutting it. Put what matters most first, give every section a heading that can be scanned, and make sure no section looks like the end when it is not.

### Nothing covers the page on arrival
- Status: draft
- Source: study. On four of the 26 a notice or sign-up box covered a quarter or more of the first screen. The sales guide has the same rule for shops.
- Rule: a phone's first screen is too small to give away. No pop-ups on arrival; any notice the law requires is a thin strip.

## Not covered yet

- Screens between a phone and a desktop, such as tablets.
- A phone held sideways.
- Speed and data use on a slow connection, which matters more on phones than anywhere and has not been researched.
- Real phones. Everything here was measured in a desktop browser pretending to be one.
- Motion and gestures such as swiping.

## How these notes get approved

A note here is approved when it has held on two different kinds of site and the skill's owner has agreed with the result on both. For the notes with a check, "held" means the audit passes and the page still looks right.

## Sources

Read on 2026-10-03:

- WCAG 2.2 Understanding documents: 1.4.10 Reflow; 2.5.5 and 2.5.8 Target Size
- web.dev: Responsive web design basics; Accessible tap targets
- Nielsen Norman Group: Hamburger menus and hidden navigation; Mobile navigation patterns; Mobile user experience; Sticky headers; Scrolling and attention
- Steven Hoober, "How do users really hold mobile devices?", UXmatters, 2013
- CSS-Tricks, "16px or larger text prevents iOS form zoom"

Studied the same day at 390 pixels wide, the first screen and one further down: the 26 sites already listed in `style-feel-artistic.md`, `style-purpose-sales.md` and `style-field-education.md`.

## Questions it raises

- What should the first screen on a phone hold?
- Should the main action stay on screen as people scroll?
- Will people fill in the forms on a phone, and can any field be dropped?
