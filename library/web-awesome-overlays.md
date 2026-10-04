---
name: Web Awesome pop-ups
summary: How Web Awesome's dialogs, drawers, dropdown menus, tooltips, popovers and toasts open, close and are announced. Read for any mockup that uses them, with library/web-awesome.md.
detect: ["<wa-(dialog|drawer|dropdown|popover|tooltip|popup|toast)"]
version: 3.14.0
checked: 2026-10-03
source: https://webawesome.com/docs/components/dialog/
---

# Web Awesome pop-ups

Anything that appears over the page. Mockups usually show these in one state, so the blueprint has to say what opens each one, every way it can close, and what happens to unsaved input.

## Use it properly

A dialog opened and closed with no script:

```html
<wa-button data-dialog="open confirm">Delete</wa-button>

<wa-dialog id="confirm" label="Delete this colony?">
  This cannot be undone.
  <wa-button slot="footer" data-dialog="close">Cancel</wa-button>
  <wa-button slot="footer" variant="danger">Delete</wa-button>
</wa-dialog>
```

Always give a dialog or drawer a `label`. A tooltip or popover points at its anchor with `for="the-anchor-id"`.

## Notes

### A button opens and closes a dialog with data-dialog attributes and no script
- Status: approved
- Test: `tests/web-awesome-overlays/data-dialog-opens-and-closes.html` (passed 2026-10-03, version 3.14.0)
- What happens: a button with `data-dialog="open the-id"` opens that dialog. A button inside it with `data-dialog="close"` closes it.
- What to do: use these in mockups so dialogs work without any JavaScript.

### Focus moves into a dialog when it opens and back to the opener when it closes
- Status: approved
- Test: `tests/web-awesome-overlays/focus-moves-in-and-back.html` (passed 2026-10-03, version 3.14.0)
- What happens: on opening, keyboard focus moves inside the dialog. On closing, it returns to the button that opened it.
- What to do: nothing; this is the correct behaviour and comes for free. Do not add focus code of your own on top.

### The Escape key closes a dialog
- Status: approved
- Test: `tests/web-awesome-overlays/escape-closes.html` (passed 2026-10-03, version 3.14.0)
- What happens: pressing Escape closes an open dialog.
- What to do: if a dialog holds unsaved input, decide what Escape should do and see the note on cancelling `wa-hide`.

### Clicking outside a dialog closes it only with the light-dismiss attribute
- Status: approved
- Test: `tests/web-awesome-overlays/outside-click-needs-light-dismiss.html` (passed 2026-10-03, version 3.14.0)
- What happens: a click on the dimmed area around a plain dialog does nothing. With `light-dismiss` on the dialog, it closes.
- What to do: add `light-dismiss` for information-only dialogs. Leave it off for forms and confirmations.
- In someone else's mockup: "does clicking outside close it?" is a question to ask; the mockup's answer is whichever default the author happened to leave.

### Cancelling the wa-hide event keeps a dialog open
- Status: approved
- Test: `tests/web-awesome-overlays/prevent-hide-keeps-open.html` (passed 2026-10-03, version 3.14.0)
- What happens: calling `event.preventDefault()` in a `wa-hide` listener stops the dialog closing, whatever triggered it. The event's `detail.source` says what asked for the close.
- What to do: use this for "you have unsaved changes" guards.

### A dialog without a label has no accessible name
- Status: approved
- Test: `tests/web-awesome-overlays/dialog-needs-label.html` (passed 2026-10-03, version 3.14.0)
- What happens: without `label`, a dialog is announced as just "dialog" with an empty heading. With `label="Delete colony"` it is announced by that name and shows it as the title.
- What to do: always set `label`.
- In someone else's mockup: look for `<wa-dialog` and `<wa-drawer` tags with no `label`.

### A dialog with the open attribute is shown as soon as the page loads
- Status: approved
- Test: `tests/web-awesome-overlays/open-attribute-shows-at-load.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-dialog open>` is showing when the page appears.
- What to do: useful for mocking the open state. Remove `open` before it becomes the real page unless the dialog should greet every visitor.
- In someone else's mockup: an `open` attribute usually means "this is what it looks like", not "show this on load". Ask.

### An open dialog adds the wa-scroll-lock class to the html element
- Status: approved
- Test: `tests/web-awesome-overlays/scroll-lock-class.html` (passed 2026-10-03, version 3.14.0)
- What happens: while a dialog is open, `<html>` has the class `wa-scroll-lock`; it is removed on close.
- What to do: if the page behind should stop scrolling, that class is the hook. The rule that does the locking is in `utilities.css`, not the theme.

### A drawer is announced as a dialog and closes with Escape
- Status: approved
- Test: `tests/web-awesome-overlays/drawer-is-a-dialog.html` (passed 2026-10-03, version 3.14.0)
- What happens: a `<wa-drawer label="Filters">` behaves like a dialog that slides in: same announcement, same Escape behaviour.
- What to do: treat drawers and dialogs the same in the blueprint.

### Choosing a dropdown item fires wa-select on the dropdown, then closes it
- Status: approved
- Test: `tests/web-awesome-overlays/dropdown-select-event.html` (passed 2026-10-03, version 3.14.0)
- What happens: clicking the trigger opens the menu. Clicking an item fires `wa-select` on the `<wa-dropdown>`, with the item in `event.detail.item`, and the menu closes. It is announced as a menu of menu items.
- What to do: listen for `wa-select` on the dropdown and switch on `event.detail.item.value`. Give every item a `value`.

### A dropdown item with type="checkbox" toggles when chosen
- Status: approved
- Test: `tests/web-awesome-overlays/dropdown-checkbox-item.html` (passed 2026-10-03, version 3.14.0)
- What happens: choosing `<wa-dropdown-item type="checkbox">` flips its `checked` state. It is announced as a checkbox menu item.
- What to do: use it for on/off options inside a menu, and read `checked` in the `wa-select` handler.

### A tooltip shows on hover and on keyboard focus
- Status: approved
- Test: `tests/web-awesome-overlays/tooltip-hover-and-focus.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-tooltip for="a">` opens when the element with id `a` is hovered or focused, and closes when the pointer leaves.
- What to do: put the tooltip on something that can take focus, such as a button, so keyboard users get it too. Never put essential information only in a tooltip: touch screens have no hover.

### A popover opens when its anchor is clicked and closes on a click outside
- Status: approved
- Test: `tests/web-awesome-overlays/popover-click-toggle.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-popover for="a">` opens on a click of its anchor and closes on a click elsewhere.
- What to do: use a popover, not a tooltip, when the floating content has links or buttons in it.

### toast.create() shows a message that removes itself and never blocks the page
- Status: approved
- Test: `tests/web-awesome-overlays/toast-create.html` (passed 2026-10-03, version 3.14.0)
- What happens: with one `<wa-toast>` on the page, `toast.create('Saved', { duration: 1000 })` adds a message that disappears after the duration. The toast area ignores clicks, so it never covers the page's controls.
- What to do: keep one `<wa-toast>` per page and call `create()` for each message. In the blueprint, say which actions show a toast and what it says.

### wa-popup only positions content: it has no role and nothing dismisses it
- Status: approved
- Test: `tests/web-awesome-overlays/popup-is-only-positioning.html` (passed 2026-10-03, version 3.14.0)
- What happens: content inside `<wa-popup>` shows only while it has the `active` attribute, placed beside its anchor. It is announced as ordinary text, and neither Escape nor a click elsewhere hides it.
- What to do: do not build menus, tooltips or dialogs from `wa-popup`. Use `wa-dropdown`, `wa-tooltip`, `wa-popover` or `wa-dialog`, which add the keyboard and screen-reader behaviour.
- In someone else's mockup: a bare `wa-popup` used as a menu or dialog is an accessibility problem. Raise it.

## Questions it raises

- For each dialog and drawer: what opens it, and does a click outside close it?
- If it contains a form: what happens to typed input when it is closed without saving?
- Which actions confirm with a toast, and what does each say?
