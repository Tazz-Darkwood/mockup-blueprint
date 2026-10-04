---
name: CSS layout
summary: The layout mistakes that keep turning up in mockups: columns that will not stay equal, things that stick out sideways, heights that collapse, sticky bars that do not stick. Read before writing a mockup's CSS, and when a page scrolls sideways on a phone.
always: creating
detect: ["<style", "stylesheet", "display: grid", "display: flex"]
checked: 2026-10-03
source: tested in the skill's test browser (Chromium). Several of these were first met as bugs in this folder's own mockups.
---

# CSS layout

This is not a guide to CSS. It is a list of the specific things that have gone wrong, each with the one line that fixes it. Most of them end the same way: something is wider than the screen, and the page scrolls sideways on a phone.

When the audit reports `mobile/sideways-scroll`, it names what sticks out. Look that element up here.

## Use it properly

A stylesheet that starts with these avoids half the notes below:

```css
*, *::before, *::after { box-sizing: border-box; }
img, svg, video { display: block; max-width: 100%; height: auto; }
[hidden] { display: none !important; }
body { overflow-wrap: break-word; }
```

And two habits:

- Write grid columns as `minmax(0, 1fr)`, not `1fr`.
- Give a flex item that holds text `min-width: 0`.

## Notes

### A grid column of 1fr will not shrink below what is in it
- Status: approved
- Test: `tests/css-layout/grid-1fr-overflow.html` (passed 2026-10-03, in Chromium)
- What happens: a 400-pixel grid of `1fr 1fr` with a 300-pixel picture in the second column came out as columns of 100 and 300. Written as `minmax(0, 1fr)` twice, with the picture allowed to shrink, the columns were 200 and 200.
- What to do: write equal columns as `repeat(n, minmax(0, 1fr))`. Plain `1fr` means "at least as wide as the content".
- In someone else's mockup: columns meant to be equal that are not, or a grid wider than its page.

### A flex item will not shrink below its content until it is given min-width 0
- Status: approved
- Test: `tests/css-layout/flex-min-width.html` (passed 2026-10-03, in Chromium)
- What happens: in a 200-pixel row, an item holding a long unbroken piece of text pushed the row 415 pixels too wide. With `min-width: 0` on the item (and the text allowed to be cut short), nothing spilled and the button beside it stayed in view.
- What to do: put `min-width: 0` on any flex item that holds text or a picture. The same goes for `min-height: 0` in a column.
- In someone else's mockup: a row where a long name or address pushes the buttons off the screen.

### A picture wider than its box sticks out unless it has max-width 100%
- Status: approved
- Test: `tests/css-layout/image-overflow.html` (passed 2026-10-03, in Chromium)
- What happens: a 600 by 300 picture with its width and height given, in a 300-pixel box, was drawn 600 wide. With `max-width: 100%` it was 300 wide but still 300 tall, squashed. With `height: auto` as well it was 300 by 150.
- What to do: always both: `max-width: 100%; height: auto`. Keep the `width` and `height` attributes on the tag, so the page does not jump as pictures load.

### A long unbroken word or address sticks out of a narrow box
- Status: approved
- Test: `tests/css-layout/long-word.html` (passed 2026-10-03, in Chromium)
- What happens: a long web address in a 200-pixel box stuck out by 341 pixels. With `overflow-wrap: anywhere` it wrapped inside the box.
- What to do: set `overflow-wrap: break-word` on the body, and `anywhere` on anything that shows addresses, emails or other text typed by visitors.
- In someone else's mockup: this was the account page of the Meridian mockup, where an email address broke its column.

### Width 100% plus padding is wider than its parent unless box-sizing is border-box
- Status: approved
- Test: `tests/css-layout/border-box.html` (passed 2026-10-03, in Chromium)
- What happens: a child with `width: 100%` and 20 pixels of padding each side, in a 200-pixel parent, was 240 wide. With `box-sizing: border-box` it was 200.
- What to do: set `box-sizing: border-box` on everything, once, at the top of the stylesheet.

### In a column flex box with align-items set, a child with nothing solid in it collapses to no width
- Status: approved
- Test: `tests/css-layout/flex-column-shrink.html` (passed 2026-10-03, in Chromium)
- What happens: a child with an aspect ratio, whose only content was positioned absolutely, came out 0 by 0 in a column with `align-items: flex-start`. With `width: 100%` on the child, or with `align-items` left alone, it was 300 by 150.
- What to do: in a column, `align-items: flex-start` (or `center`) makes every child only as wide as its content. Give a child that has no content of its own a width.
- In someone else's mockup: a picture frame or 3D stage that has vanished. This happened on Greenfire Herbs.

### height 100% means nothing when the parent's height comes from min-height
- Status: approved
- Test: `tests/css-layout/percent-height.html` (passed 2026-10-03, in Chromium)
- What happens: inside a parent with `min-height: 300px`, a child with `height: 100%` was 22 pixels tall. With the parent made a flex or grid container and no height on the child, it was 300.
- What to do: to make a child fill its parent, make the parent `display: grid` or `flex`. Do not chase percentages up the page.

### A first child's top margin pushes its parent down instead of making room inside it
- Status: approved
- Test: `tests/css-layout/margin-collapse.html` (passed 2026-10-03, in Chromium)
- What happens: a paragraph with a 40-pixel top margin, first in a coloured box, sat right at the top of the box: the margin had moved outside. With `display: flow-root` on the box, the 40 pixels were inside it.
- What to do: space things inside a box with the box's `padding` or with `gap`, not with margins on the first and last children.
- In someone else's mockup: an unexplained gap above a coloured section, and none inside it.

### A picture leaves a few pixels of gap under it unless it is display block
- Status: approved
- Test: `tests/css-layout/inline-image-gap.html` (passed 2026-10-03, in Chromium)
- What happens: a 100-pixel picture alone in a box made the box 106.4 pixels tall. With `display: block` on the picture the box was 100.
- What to do: `display: block` on every picture, as in the starter rules above.
- In someone else's mockup: a thin strip of background colour under a picture.

### Sticky stops working inside anything that has overflow set
- Status: approved
- Test: `tests/css-layout/sticky-overflow.html` (passed 2026-10-03, in Chromium)
- What happens: a bar with `position: sticky; top: 0` stayed at the top of the window in a plain section. Inside a section with `overflow: hidden` it scrolled away with the page.
- What to do: check every ancestor of a sticky element for `overflow`. `overflow: hidden` is often added to a wrapper to stop sideways scrolling, and quietly breaks every sticky thing inside it. Use `overflow: clip` if clipping is all that is wanted.
- In someone else's mockup: a header that used to stick and stopped after a "fix" for sideways scrolling.

### A link to a part of the page lands under a sticky header
- Status: approved
- Test: `tests/css-layout/anchor-under-header.html` (passed 2026-10-03, in Chromium)
- What happens: with an 80-pixel header fixed to the top, following a link to a heading put that heading at the very top of the window, behind the header. A heading with `scroll-margin-top: 90px` landed at 90.
- What to do: give every element that can be linked to a `scroll-margin-top` a little larger than the header.

### Something fixed to the screen is fixed to its ancestor instead, if that ancestor is rotated or moved
- Status: approved
- Test: `tests/css-layout/fixed-inside-transform.html` (passed 2026-10-03, in Chromium)
- What happens: a message with `position: fixed; bottom: 10px` sat 10 pixels from the bottom of the window inside a plain card, and 202 pixels from it inside a card with `rotate: 1deg`: it was placed against the card.
- What to do: keep anything fixed to the screen (messages, bars, dialogs made by hand) as a direct child of the body, never inside something rotated, scaled, moved with `transform`, or filtered.
- In someone else's mockup: relevant wherever cards are tilted for a hand-made look, as on Greenfire Herbs.

### 100vw is wider than the page when there is a scrollbar
- Status: draft
- Source: widely reported; not shown here. The test browser's scrollbars lie over the page and take no room, so the test could not show the problem and was removed.
- What would confirm it: a test in a browser whose scrollbars take up room, such as most on Windows.
- Until then: use `width: 100%`, not `100vw`, for anything meant to span the page.

## Questions it raises

- Does the header stay on screen as the page scrolls?
- What is the longest name, address or number this layout must hold?
