---
name: Web Awesome navigation
summary: How Web Awesome's tabs, accordions, details, trees, pagination, breadcrumbs, steppers and carousels behave. Read for any mockup that uses them, with library/web-awesome.md.
detect: ["<wa-(tab|accordion|details|tree|pagination|breadcrumb|stepper|step|carousel)"]
version: 3.14.0
checked: 2026-10-03
source: https://webawesome.com/docs/components/tab-group/
---

# Web Awesome navigation

Components that show part of the content at a time or move between parts.

## Use it properly

Tabs link to panels by matching the tab's `panel` to the panel's `name`:

```html
<wa-tab-group active="billing">
  <wa-tab panel="profile">Profile</wa-tab>
  <wa-tab panel="billing">Billing</wa-tab>
  <wa-tab-panel name="profile">Profile settings</wa-tab-panel>
  <wa-tab-panel name="billing">Billing settings</wa-tab-panel>
</wa-tab-group>
```

## Notes

### Clicking a tab shows the panel whose name matches its panel attribute
- Status: approved
- Test: `tests/web-awesome-navigation/tabs-click-shows-panel.html` (passed 2026-10-03, version 3.14.0)
- What happens: the first tab's panel shows on load. Clicking another tab swaps the panel and fires `wa-tab-hide` then `wa-tab-show` on the group, each with the panel name in `event.detail.name`. Tabs are placed in the tab strip automatically; `slot="nav"` does not have to be written.
- What to do: listen for `wa-tab-show` to load a panel's content when it is first opened.

### Arrow keys move between tabs and switch the panel straight away
- Status: approved
- Test: `tests/web-awesome-navigation/tabs-arrow-keys-activate.html` (passed 2026-10-03, version 3.14.0)
- What happens: with focus on a tab, the right arrow moves to the next tab and shows its panel immediately.
- What to do: if showing a panel is expensive (it fetches data), set `activation="manual"` on the group. That attribute exists in the component's definition; its behaviour has not been tested here.

### A tab whose panel name matches nothing shows an empty space
- Status: approved
- Test: `tests/web-awesome-navigation/tab-missing-panel-blank.html` (passed 2026-10-03, version 3.14.0)
- What happens: if a tab says `panel="tow"` and the panel says `name="two"`, clicking the tab hides every panel and shows nothing. There is no error.
- What to do: check each tab's `panel` against a panel `name`.
- In someone else's mockup: a tab that shows a blank area is almost always a mismatched name.

### The active attribute on the tab group chooses which tab starts open
- Status: approved
- Test: `tests/web-awesome-navigation/tabs-active-attribute.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-tab-group active="two">` starts with the panel named `two` showing.
- What to do: use it instead of script to pick the starting tab.

### An accordion lets several items be open at once unless mode is set
- Status: approved
- Test: `tests/web-awesome-navigation/accordion-multiple-by-default.html` (passed 2026-10-03, version 3.14.0)
- What happens: by default, opening a second item leaves the first open. Each header is announced as a level 3 heading containing a button.
- What to do: set `heading-level` on the accordion so its headers fit the page's heading order. For one-at-a-time behaviour see the next note.

### With mode="single", the open item cannot be closed
- Status: approved
- Test: `tests/web-awesome-navigation/accordion-single-stays-open.html` (passed 2026-10-03, version 3.14.0)
- What happens: with `mode="single"`, opening one item closes the other, and clicking the open item again leaves it open, so one is always showing.
- What to do: the component's definition also lists `mode="single-collapsible"`, which by its name allows closing the open one; not tested here.
- In someone else's mockup: ask which of the three behaviours is wanted. The mockup shows whichever the author left as default.

### Details that share a name close each other
- Status: approved
- Test: `tests/web-awesome-navigation/details-name-exclusive.html` (passed 2026-10-03, version 3.14.0)
- What happens: two `<wa-details name="faq">` elements behave as a set: opening one closes the other.
- What to do: give a list of questions the same `name` for one-at-a-time behaviour, or no `name` to let any number stay open.

### Clicking a parent tree item selects it without expanding it
- Status: approved
- Test: `tests/web-awesome-navigation/tree-click-selects-not-expands.html` (passed 2026-10-03, version 3.14.0)
- What happens: clicking a parent item's label selects it and fires `wa-selection-change` on the tree, with the selected items in `event.detail.selection`. Its children stay hidden; expanding is done with the small arrow.
- What to do: start an item open with the `expanded` attribute when its children should be visible from the start.

### Pagination only reports the page chosen
- Status: approved
- Test: `tests/web-awesome-navigation/pagination-only-reports.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-pagination total="95" page-size="10">` draws page buttons 1 to 10. Choosing one fires `wa-before-page-change` then `wa-page-change`, with `event.detail.page`, and updates its `page`. It does not show or hide any content.
- What to do: in the `wa-page-change` handler, load or show that page of the list yourself. In the blueprint, say where the rows come from and how many there are per page.

### A breadcrumb item without href is announced as a button
- Status: approved
- Test: `tests/web-awesome-navigation/breadcrumb-last-is-button.html` (passed 2026-10-03, version 3.14.0)
- What happens: the breadcrumb is announced as a navigation landmark named by its `label`. Items with `href` are links. An item with no `href`, as the last one usually is, is announced as a button and is not marked as the current page.
- What to do: the blueprint should ask for the current page to be marked for screen readers. How best to do that with this component has not been tested.

### Steps cannot be clicked unless the stepper is clickable
- Status: approved
- Test: `tests/web-awesome-navigation/stepper-not-clickable-by-default.html` (passed 2026-10-03, version 3.14.0)
- What happens: calling `next()` on a `<wa-stepper>` moves it to the next step. Clicking an earlier step does nothing by default.
- What to do: move the stepper from your own Next and Back buttons with `next()` and `previous()`. The component's definition has a `clickable` attribute for letting people jump between steps; not tested here.

### A carousel is 16:9 tall by default, whatever it contains
- Status: approved
- Test: `tests/web-awesome-navigation/carousel-16-9-by-default.html` (passed 2026-10-03, version 3.14.0)
- What happens: a carousel with two one-word slides is 984 by 521 pixels, because it keeps a 16:9 shape (`--aspect-ratio: 16 / 9`).
- What to do: set `--aspect-ratio` in CSS on the carousel to fit the content.
- In someone else's mockup: a carousel with a lot of empty space under short content is this default.

## Questions it raises

- Tabs: does each panel load its content when opened, or is everything loaded with the page?
- Accordion: several open at once, exactly one, or at most one?
- Pagination: how many items per page, and where do they come from?
- Stepper: can people jump back to an earlier step?
