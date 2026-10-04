---
name: The browser's own building blocks
summary: What plain HTML gives for free, with no library: pop-up dialogs, fold-out sections, pop-over menus, form checking, buttons and what the keyboard can reach. Read before building any mockup; most use several of these.
always: creating
detect: ["<dialog", "<details", "popover", "<form", "required"]
checked: 2026-10-03
source: tested in the skill's test browser (Chromium); the HTML standard at html.spec.whatwg.org
---

# The browser's own building blocks

Before reaching for a library or writing script, check whether the browser already does it. These pieces are free, work without script, and come with keyboard and screen-reader behaviour built in. They also each have a catch or two, which is what the notes below are for.

Everything here was tested in one browser, Chromium. Safari and Firefox mostly agree, but that has not been checked.

## Use it properly

- A question that must be answered before carrying on: `<dialog>` opened with `showModal()`.
- A section that folds away: `<details>` with a `<summary>`.
- A small menu or hint hanging off a button: the `popover` attribute.
- Checking a form: `required`, `type="email"` and the rest, with messages styled from `:user-invalid`.
- Anything pressable is a `<button>` or an `<a href>`. Nothing else.
- Put `[hidden] { display: none !important; }` in every stylesheet.

## Notes

### A dialog opened with showModal takes the focus, blocks the page behind, and closes on Escape
- Status: approved
- Test: `tests/web-platform/dialog-modal.html` (passed 2026-10-03, in Chromium)
- What happens: after `showModal()`, focus moved to the first button inside the dialog; a click on a button behind it did nothing; Escape closed it, fired one `close` event, and put focus back on the button that opened it.
- What to do: use `showModal()` for anything that must be dealt with before carrying on. Nothing more is needed for focus or the keyboard.
- In someone else's mockup: a hand-made pop-up built from `<div>`s usually does none of this. Tab walks out of it into the page behind.

### A dialog opened with show, or with the open attribute, does none of that
- Status: approved
- Test: `tests/web-platform/dialog-show.html` (passed 2026-10-03, in Chromium)
- What happens: opened with `show()`, the page behind could still be clicked and Escape did not close it.
- What to do: only use `show()` for something that sits beside the page's content, such as a note. For a question, use `showModal()`.
- In someone else's mockup: a dialog that can be clicked past was opened the wrong way.

### Buttons in a form with method dialog close it and say which was pressed
- Status: approved
- Test: `tests/web-platform/dialog-form.html` (passed 2026-10-03, in Chromium)
- What happens: inside `<form method="dialog">`, pressing a button closed the dialog without the page going anywhere, and `dialog.returnValue` held that button's `value`. Closed with Escape instead, `returnValue` was empty.
- What to do: give each button a `value` and read `returnValue` in the dialog's `close` event. Treat an empty value as "cancelled".

### Clicking outside a dialog does not close it
- Status: approved
- Test: `tests/web-platform/dialog-backdrop.html` (passed 2026-10-03, in Chromium)
- What happens: a click on the dimmed page around an open dialog left it open. With a click handler that closes the dialog when the click's target is the dialog element itself, and the dialog's padding moved to an inner wrapper, the same click closed it.
- What to do: decide whether clicking away should close it and say so in the blueprint. For a question with consequences (delete, pay), it should not.

### Details open and close without script, and those sharing a name open one at a time
- Status: approved
- Test: `tests/web-platform/details-name.html` (passed 2026-10-03, in Chromium)
- What happens: pressing a `<summary>` opened its `<details>` and fired a `toggle` event. Opening one of two that shared a `name` closed the other; one with no name was left alone.
- What to do: use `<details>` for questions and answers and anything else that folds. Give a group the same `name` only if seeing one at a time is really wanted: it also closes what the visitor was reading.

### A required field stops the form being sent, and looks wrong before anyone has typed
- Status: approved
- Test: `tests/web-platform/validation.html` (passed 2026-10-03, in Chromium)
- What happens: an empty required field matched `:invalid` the moment the page loaded, and `:user-invalid` only after the visitor had tried to send the form. Pressing the button did not send the form; the browser showed "Please fill out this field." With `novalidate` on the form, it was sent.
- What to do: style mistakes from `:user-invalid`, never `:invalid`, or every empty field is red on arrival. If the mockup shows its own messages, put `novalidate` on the form and check in script, and say in the blueprint that the server must check again.
- In someone else's mockup: a form that greets the visitor with red borders is styled from `:invalid`.

### A button in a form sends the form unless it says type=button, and so does Enter
- Status: approved
- Test: `tests/web-platform/button-type.html` (passed 2026-10-03, in Chromium)
- What happens: a `<button>` with no `type` inside a form sent the form when pressed. One with `type="button"` did not. Pressing Enter in a text field sent it too.
- What to do: give every button in a form a `type`: `submit` for the one that sends it, `button` for the rest (show password, add a row, cancel).
- In someone else's mockup: a form that submits when "Cancel" or an eye icon is pressed.

### The hidden attribute loses to any display rule in the page's own CSS
- Status: approved
- Test: `tests/web-platform/hidden-loses.html` (passed 2026-10-03, in Chromium)
- What happens: an element with the `hidden` attribute and a class that set `display: flex` was shown. After adding `[hidden] {{ display: none !important; }}` it was hidden.
- What to do: put that one rule at the top of every stylesheet. Then `element.hidden = true` can be trusted.
- In someone else's mockup: something that should have gone away after a press, and has a layout class on it.

### Tab reaches links with an address and buttons, and nothing else
- Status: approved
- Test: `tests/web-platform/not-focusable.html` (passed 2026-10-03, in Chromium)
- What happens: Tab reached an `<a href>`, a `<button>`, and a `<span>` given `tabindex="0"`. It skipped an `<a>` with no `href` and a `<div>` with a click handler. On the span, Enter and Space did nothing.
- What to do: make anything pressable a real `<button>`, or an `<a>` with an `href` if it goes somewhere. Adding `tabindex` to something else gets it focus but not the keys.
- In someone else's mockup: the audit reports clickable things that cannot be focused as `a11y/click-not-focusable`.

### A popover opens from a button, closes on a click outside or Escape, and does not take the focus
- Status: approved
- Test: `tests/web-platform/popover.html` (passed 2026-10-03, in Chromium)
- What happens: a button with `popovertarget` opened an element marked `popover`. A click elsewhere closed it, and so did Escape. Focus stayed on the button that opened it.
- What to do: use it for menus and hints. Because focus does not move in, a keyboard user has to Tab into it: keep it directly after its button in the page so that works.

### Opened from a folder, a page can load scripts and pictures beside it but cannot fetch them
- Status: approved
- Test: `tests/web-platform/fetch-from-a-folder.html` (passed 2026-10-03, in Chromium)
- What happens: on a page opened straight from a folder, a `<script src>` beside the page loaded. `fetch()`, `XMLHttpRequest` and `import()` of a file beside the page were all refused.
- What to do: a mockup that must open from a folder keeps its data in a script file that sets a variable, not in a JSON file it fetches, and keeps its own code in ordinary scripts, not modules. This is why the blueprint's own notes are a `.js` file.
- In someone else's mockup: a mockup that shows nothing and reports a failed fetch was made to be run through a local server.

### Storage is separate for every file in some browsers
- Status: draft
- Source: seen once, by the skill's owner on a mockup of several pages on 2026-10-03, in a browser not yet identified: a page could not read what another page of the same mockup had saved. Reproduced in the test browser only by making it behave that way.
- What would confirm it: opening a two-page test in Firefox and in Safari from a folder.
- Until then: load `assets/carry-storage.js` first on every page of a mockup whose pages share anything. The audit checks for this.

### Mixing opposite hues in oklab gives grey; in oklch it gives another vivid hue
- Status: approved
- Test: `tests/web-platform/colour-mix-oklab.html` (passed 2026-10-03)
- What happens: a warm red (hue 30) and its opposite (hue 210), of the same lightness and strength, were mixed half and half with `color-mix()`. Mixed `in oklab` the browser gave a grey with no colour in it at all. Mixed `in oklch` it gave a vivid colour at hue 120, a yellow-green that neither colour contains.
- What to do: choose on purpose. When a design mixes colours the way paints or genes blend, with opposites cancelling towards mud, mix `in oklab` (or add the colours' a and b values yourself). Mixing `in oklch`, or averaging hue angles, walks round the colour wheel and never cancels.
- Careful: averaging two hue angles as plain numbers has a second fault. 350 and 10, both reds, average to 180, a cyan.

### A canvas turns any CSS colour, oklch() included, into red, green and blue numbers
- Status: approved
- Test: `tests/web-platform/canvas-converts-oklch.html` (passed 2026-10-03)
- What happens: painting one pixel with `fillStyle = 'oklch(0.75 0.18 60)'` and reading it back gave [254, 141, 0], an orange. `oklab(0.6 0 0)` gave an even grey, [128, 128, 128]. A green stronger than a screen can show, `oklch(0.7 0.4 150)`, came back as [0, 214, 0]: the browser brought it into range by itself.
- What to do: this is the cheapest way, in a mockup, to hand a colour worked out in OKLab or OKLCH to something that only takes hex or `rgb()`, such as a PixiJS tint (see `pixi.md`): no library needed. For the real site, where the server must work out the same colour, use a colour library on both sides so the two agree, and decide there how out-of-range colours are brought into range; the browser's own way was not compared with any library's here.

## Questions it raises

- Should clicking outside each dialog close it?
- Does the page show its own messages for mistakes in a form, or the browser's?
