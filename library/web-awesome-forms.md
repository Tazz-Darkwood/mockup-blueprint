---
name: Web Awesome forms
summary: How Web Awesome's form fields behave (input, textarea, select, radio, checkbox, switch, slider, number, tag input). Read for any mockup with a wa- form field, with library/web-awesome.md.
detect: ["<wa-(input|textarea|select|option|checkbox|radio|switch|slider|rating|color-picker|number-input|otp-input|known-date|time-input|tag-input)"]
version: 3.14.0
checked: 2026-10-03
source: https://webawesome.com/docs/form-controls/
---

# Web Awesome forms

Web Awesome's fields work inside a normal `<form>` and submit like native ones. Most surprises come from the places where they differ from the native element with the same job. The basics (fields need a `name`, the submit button needs `type="submit"`, typing fires `input` and `change`, `required` blocks submit) are in `web-awesome.md`.

## Use it properly

```html
<form>
  <wa-input name="email" type="email" label="Email" required></wa-input>
  <wa-select name="plan" label="Plan">
    <wa-option value="free">Free</wa-option>
    <wa-option value="pro">Pro</wa-option>
  </wa-select>
  <wa-textarea name="notes" label="Notes" value="Starting text goes here"></wa-textarea>
  <wa-button type="submit" variant="brand">Send</wa-button>
</form>
```

Every field has a `name` and a `label`, every option has a `value`, and starting text goes in the `value` attribute.

## Notes

### An option with no value attribute submits an empty value
- Status: approved
- Test: `tests/web-awesome-forms/option-needs-value.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-option>Sky blue</wa-option>` can be chosen and the select shows "Sky blue", but the select's value is an empty string and the form sends `colour=`. A native `<option>` would send its text.
- What to do: give every `<wa-option>` a `value`.
- In someone else's mockup: options without `value` are common in mockups. List the real values in the blueprint, because the mockup has none.

### Choosing an option fires input and change and updates the form data
- Status: approved
- Test: `tests/web-awesome-forms/select-fires-input-change.html` (passed 2026-10-03, version 3.14.0)
- What happens: a select with nothing chosen is left out of the form data. Choosing an option fires `input` and `change` on the select and the form then sends it. Opening and closing the list fires `wa-show` and `wa-hide`.
- What to do: listen for `change`. When testing, note that calling `.click()` on an option from script did not select it; a real mouse click did.

### Preselect several options with selected on each option
- Status: approved
- Test: `tests/web-awesome-forms/multiple-preselect.html` (passed 2026-10-03, version 3.14.0)
- What happens: on a `multiple` select, `value="x y"` selects nothing. Putting `selected` on each `<wa-option>` selects them, the value is a list, and the form sends one entry per choice.
- What to do: use `selected` on the options to preselect.

### A radio group carries the name, and sends nothing until one is chosen
- Status: approved
- Test: `tests/web-awesome-forms/radio-group-name.html` (passed 2026-10-03, version 3.14.0)
- What happens: `name` goes on `<wa-radio-group>`, not on each `<wa-radio>`. With nothing chosen the group is absent from the form data. Choosing a radio fires `input` and `change` on the group.
- What to do: set `value` on the group to start with one chosen, or add `required` if a choice is mandatory.

### A slider with no value starts at 0 and always submits
- Status: approved
- Test: `tests/web-awesome-forms/slider-starts-at-zero.html` (passed 2026-10-03, version 3.14.0)
- What happens: an untouched `<wa-slider>` has the value 0 and sends `0`. A native range input starts in the middle (50). A slider with `range` sends two entries under the same name, the low and high ends.
- What to do: always set `value`. In the blueprint, say what an untouched slider should mean, since the form cannot tell "left at 0" from "chose 0".

### Text written between wa-textarea tags is ignored
- Status: approved
- Test: `tests/web-awesome-forms/textarea-ignores-content.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-textarea>Some text</wa-textarea>` starts empty. A native `<textarea>` would show the text. Only the `value` attribute sets the starting text.
- What to do: put starting text in `value`.
- In someone else's mockup: a textarea that looks empty in the browser but has text in the source is this.

### A disabled field is left out of the form data, a readonly one is kept
- Status: approved
- Test: `tests/web-awesome-forms/disabled-omitted-readonly-kept.html` (passed 2026-10-03, version 3.14.0)
- What happens: the same as native fields. `disabled` removes the field from what is sent; `readonly` keeps it.
- What to do: use `readonly` for a value that must be shown, not edited, and still sent.

### What each kind of field sends when nobody has touched it
- Status: approved
- Test: `tests/web-awesome-forms/untouched-fields.html` (passed 2026-10-03, version 3.14.0)
- What happens: untouched, an input, textarea, colour picker and one-time-code field each send an empty value; a slider and a rating send `0`; a select, radio group, checkbox and switch are left out entirely.
- What to do: the server has to cope with both "sent empty" and "not sent at all". Write that into the form's `rules` in the blueprint.

### A number above max is kept, not clamped, and makes the form invalid
- Status: approved
- Test: `tests/web-awesome-forms/number-over-max-invalid.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-number-input value="200" max="10">` still holds 200. The field and the form report themselves invalid, so submit is blocked.
- What to do: do not rely on `min` and `max` to correct a value. They only reject it.

### Resetting the form puts a field back to its value attribute
- Status: approved
- Test: `tests/web-awesome-forms/form-reset-restores.html` (passed 2026-10-03, version 3.14.0)
- What happens: after `form.reset()`, a changed `<wa-input value="Leeds">` returns to "Leeds".
- What to do: a native reset button or `form.reset()` works as expected.

### A field with only a placeholder has no accessible name
- Status: approved
- Test: `tests/web-awesome-forms/placeholder-is-not-a-label.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-input placeholder="Search">` is announced as an unnamed text box. With `label="Email"` it is announced as "Email", and a `hint` is read after it.
- What to do: always set `label`. If the design has no visible label, still give the field one and hide it visually.
- In someone else's mockup: the skill's audit reports a `wa-` field with no label as `a11y/input-label`.

### A required field is invalid from the start; user-invalid only after a failed submit
- Status: approved
- Test: `tests/web-awesome-forms/user-invalid-state.html` (passed 2026-10-03, version 3.14.0)
- What happens: an empty required field matches `:state(invalid)` as soon as the page loads. It matches `:state(user-invalid)` only after the person has tried to submit.
- What to do: style errors with `:state(user-invalid)`. Styling `:state(invalid)` or `:invalid` paints every required field red before anyone has typed.

### In a submit handler the submitter is a stand-in for the button
- Status: approved
- Test: `tests/web-awesome-forms/submitter-is-not-the-button.html` (passed 2026-10-03, version 3.14.0)
- What happens: in the form's `submit` event, `event.submitter` is a native button Web Awesome creates, not the `<wa-button>` that was pressed. A `name` and `value` on the pressed button are missing from `new FormData(form)` and present in `new FormData(form, event.submitter)`.
- What to do: when a form has several submit buttons (Save, Save and close), read which one was pressed with `new FormData(form, event.submitter)`.

### Pressing Enter in a wa-input submits the form
- Status: approved
- Test: `tests/web-awesome-forms/enter-submits.html` (passed 2026-10-03, version 3.14.0)
- What happens: typing in a `<wa-input>` and pressing Enter submits its form, even when the form has no submit button.
- What to do: expect it, as with native inputs. A search box inside a larger form will submit the whole form.

### Checkbox and switch toggle with the space bar and are announced with their roles
- Status: approved
- Test: `tests/web-awesome-forms/space-toggles-checkbox-switch.html` (passed 2026-10-03, version 3.14.0)
- What happens: both can be focused and toggled with Space. A checkbox is announced as a checkbox and a switch as a switch, each named by the text inside the tag.
- What to do: put the label text inside the tag: `<wa-checkbox>I agree</wa-checkbox>`.

### The clear button empties the field and fires wa-clear, input and change
- Status: approved
- Test: `tests/web-awesome-forms/clear-button-events.html` (passed 2026-10-03, version 3.14.0)
- What happens: with `with-clear`, pressing the small clear button sets the value to empty and fires `wa-clear`, `input` and `change`.
- What to do: a live search that listens for `input` also reacts to clearing, with no extra code.

### A tag input sends one form entry per tag
- Status: approved
- Test: `tests/web-awesome-forms/tag-input-one-entry-per-tag.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-tag-input name="topic" value="ants,bees">` has a list as its value and sends `topic=ants` and `topic=bees` as two entries.
- What to do: read it on the server as a repeated field, the same way as a multiple select.

### A colour picker rewrites its value into the chosen format
- Status: approved
- Test: `tests/web-awesome-forms/color-value-follows-format.html` (passed 2026-10-03, version 3.14.0)
- What happens: whatever colour it is given, the picker stores it in its `format` (hex unless told otherwise). `value="rebeccapurple"` becomes `#663399`; `value="#ff0000"` with `format="rgb"` becomes `rgb(255, 0, 0)`; with `opacity` the value gains a transparency part, such as `#ff000080`.
- What to do: decide the format the server expects and set `format` to match. With `opacity` on, the server must accept the longer form.

### A colour picker keeps and submits a value that is not a colour
- Status: approved
- Test: `tests/web-awesome-forms/color-accepts-non-colour.html` (passed 2026-10-03, version 3.14.0)
- What happens: `value="not-a-colour"` is kept as written, the field reports itself valid, and the form sends it.
- What to do: check on the server that what arrives is a colour. The picker gives no guarantee.
- In someone else's mockup: note it in the form's `rules`: colour fields need server-side validation like any text field.

### A colour picker is a button that opens a panel; the panel's text box has no name
- Status: approved
- Test: `tests/web-awesome-forms/color-picker-panel.html` (passed 2026-10-03, version 3.14.0)
- What happens: closed, it is a button named by its `label`. Clicking opens a panel with a colour area, a hue slider, a copy button, a text box holding the value, a format button and a screen-picker button. Escape closes it. The text box is announced with no name.
- What to do: always set `label`. The unnamed text box is inside the component and cannot be fixed from a mockup; record it as a known accessibility gap if the build uses a colour picker.

### Clicking the current rating again clears it to zero
- Status: approved
- Test: `tests/web-awesome-forms/rating-click-again-clears.html` (passed 2026-10-03, version 3.14.0)
- What happens: clicking the third star sets 3. Clicking the third star again sets 0. The arrow keys change it by one step and End jumps to the maximum. It fires `change`, never `input`.
- What to do: expect ratings to be clearable, and treat 0 as "no rating" on the server. Listen for `change`.

### A rating is announced as a slider, and has no name without a label
- Status: approved
- Test: `tests/web-awesome-forms/rating-needs-label.html` (passed 2026-10-03, version 3.14.0)
- What happens: with `label="Quality"` it is announced as a slider named Quality. Without `label` it is an unnamed slider.
- What to do: always set `label`, even when a visible heading sits next to it.

### A one-time-code field refuses wrong characters and is invalid until full
- Status: approved
- Test: `tests/web-awesome-forms/otp-partial-is-invalid.html` (passed 2026-10-03, version 3.14.0)
- What happens: typing `12a3` into a numeric field gives `123`: the letter is refused. A part-filled field is invalid, though the form would still send the part typed. When the last box is filled it becomes valid and fires `wa-complete`.
- What to do: listen for `wa-complete` to move on. Set `length` to the real code length and `type` to `alpha` or `alphanumeric` if codes contain letters.

### With autosubmit, a one-time-code field submits the form when the last character is typed
- Status: approved
- Test: `tests/web-awesome-forms/otp-autosubmit.html` (passed 2026-10-03, version 3.14.0)
- What happens: nothing is submitted while characters are missing. Typing the final one submits the form with no button press.
- What to do: use it only when the code is the last thing on the form. In the blueprint, say whether the code submits itself.

### A known-date is three labelled boxes, holds an ISO date, and refuses an impossible one
- Status: approved
- Test: `tests/web-awesome-forms/known-date-fields.html` (passed 2026-10-03, version 3.14.0)
- What happens: it is a group named by its `label` containing Month, Day and Year boxes. The stored value is in the form `2000-01-31`. With `lang="de"` the boxes are ordered Day, Month, Year, though their names stayed in English. Typing 30 February leaves the value empty and the field invalid.
- What to do: use it for dates people know by heart, such as a birthday. The server always receives year-month-day whatever order was shown.
- In someone else's mockup: if the site is not in English, check the box names in that language before launch.

### A time input always stores 24-hour time, however it is displayed
- Status: approved
- Test: `tests/web-awesome-forms/time-input-24h-value.html` (passed 2026-10-03, version 3.14.0)
- What happens: `value="14:30"` is displayed as 02:30 PM in an English-language page and as 14:30 with `hour-format="24"`. Both store and submit `14:30`. The up arrow on the hour changes it and fires `input` and `change`.
- What to do: write values and read them on the server as 24-hour `HH:MM`. Set `hour-format` if the display must not follow the visitor's language.

### required on a checkbox group adds an asterisk but does not stop the form submitting
- Status: approved
- Test: `tests/web-awesome-forms/checkbox-group-required-not-enforced.html` (passed 2026-10-03, version 3.14.0)
- What happens: a `required` checkbox group shows its label with an asterisk. With nothing ticked, the form is still valid and submits.
- What to do: to insist on at least one, check it in script before submit and again on the server.
- In someone else's mockup: a starred checkbox group in a mockup is a promise the mockup does not keep. Put "at least one required" in the form's `rules`.

## Questions it raises

- For each select: what are the real option values?
- For each form with more than one button: which buttons submit, and does the server need to know which was pressed?
- What should the server do with a field that arrives empty, and with one that does not arrive?
