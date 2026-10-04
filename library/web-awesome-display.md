---
name: Web Awesome display and utilities
summary: How Web Awesome's buttons, icons, tags, callouts, avatars, date and number formatters, includes, markdown and layout pieces behave. Read for any mockup that uses them, with library/web-awesome.md.
detect: ["<wa-(button|tag|callout|icon|avatar|format-|relative-time|include|markdown|split-panel|zoomable-frame|spinner|progress|badge|card|qr-code|skeleton|divider|copy-button)"]
version: 3.14.0
checked: 2026-10-03
source: https://webawesome.com/docs/components/
---

# Web Awesome display and utilities

Components that show something or help lay a page out. Several of the notes here are about accessibility and security, where the defaults are not what a mockup author would assume.

## Use it properly

- Give an icon a `label` only when it carries meaning on its own. Leave it off when the icon sits next to text that already says the same thing.
- An icon-only button needs the label: `<wa-button><wa-icon name="gear" label="Settings"></wa-icon></wa-button>`.
- Use `href` on a `<wa-button>` when it goes somewhere, and leave it off when it does something.

## Notes

### A wa-button with href is a link, not a button
- Status: approved
- Test: `tests/web-awesome-display/link-button.html` (passed 2026-10-03, version 3.14.0)
- What happens: with `href`, the component renders a real link inside and is announced as a link.
- What to do: this is correct. In the blueprint, record where it goes, as for any link.

### A disabled or loading button does not pass clicks on
- Status: approved
- Test: `tests/web-awesome-display/disabled-loading-no-click.html` (passed 2026-10-03, version 3.14.0)
- What happens: a click listener on a `disabled` or `loading` button never fires. A loading button is announced with a progress indicator named "Loading".
- What to do: set `loading` on a submit button while a save is in progress; it prevents double submission with no extra code.

### The remove button on a tag only fires wa-remove
- Status: approved
- Test: `tests/web-awesome-display/tag-remove-does-not-remove.html` (passed 2026-10-03, version 3.14.0)
- What happens: on `<wa-tag with-remove>`, pressing the small x fires `wa-remove`. The tag stays on the page.
- What to do: remove the tag yourself in the `wa-remove` handler.
- In someone else's mockup: a removable tag whose x "does nothing" is this. The blueprint must say what removing it means.

### A callout is not announced as an alert
- Status: approved
- Test: `tests/web-awesome-display/callout-has-no-role.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-callout variant="danger">` is plain text to a screen reader. The colour is the only signal that something is wrong.
- What to do: for an error that appears after an action, add `role="alert"`; for a notice, `role="status"`. Include an icon or the word "Error" so colour is not the only cue.

### An icon is hidden from screen readers unless it has a label
- Status: approved
- Test: `tests/web-awesome-display/icon-decorative-unless-label.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-icon name="gear">` is marked hidden from assistive technology. With `label="Settings"` it becomes an image with that name. So a button containing only an unlabelled icon is announced as "button" with no name.
- What to do: label the icon inside every icon-only button.
- In someone else's mockup: the skill's audit reports these as `a11y/control-name`.

### variant and family choose which Font Awesome set an icon comes from
- Status: approved
- Test: `tests/web-awesome-display/icon-variant-family.html` (passed 2026-10-03, version 3.14.0)
- What happens: a plain icon is fetched from the `solid` set. `variant="regular"` fetches the outlined one, and `family="brands"` fetches from the brands set (company logos).
- What to do: use `family="brands"` for company logos such as GitHub. A name that is not found in the chosen set draws nothing (see the unknown-icon note in `web-awesome.md`).

### An avatar whose image fails shows its initials
- Status: approved
- Test: `tests/web-awesome-display/avatar-falls-back-to-initials.html` (passed 2026-10-03, version 3.14.0)
- What happens: if the `image` cannot be loaded, the avatar shows `initials`. It is announced as an image named by `label`; with no `label` it has no name and only the initials are read.
- What to do: always give `initials` as a fallback and `label` with the person's name.

### wa-format-date shows the date in the viewer's own time zone
- Status: approved
- Test: `tests/web-awesome-display/format-date-uses-viewer-time-zone.html` (passed 2026-10-03, version 3.14.0)
- What happens: the same moment, 23:30 UTC on 3 October, shows as "October 3" with `time-zone="UTC"` and "October 4" with `time-zone="Asia/Tokyo"`. With no `time-zone` it uses the time zone of whoever is looking.
- What to do: for a date that must read the same for everyone (a deadline, an event day), set `time-zone`. In the blueprint, say for each date whether it is a moment or a calendar day.

### The lang attribute changes how dates and money are written
- Status: approved
- Test: `tests/web-awesome-display/lang-localizes-formatting.html` (passed 2026-10-03, version 3.14.0)
- What happens: with `lang="de"`, a date reads "3. Oktober 2026" and 1234.5 euros reads "1.234,50 €" where English gives "€1,234.50".
- What to do: set `lang` on the page for the audience. Do not format dates or money by hand in a mockup that uses these components.

### wa-include cannot load a file when the page is opened straight from disk
- Status: approved
- Test: `tests/web-awesome-display/include-fails-from-file.html` (passed 2026-10-03, version 3.14.0)
- What happens: opened by double-click (a `file://` address), `<wa-include src="part.html">` fires `wa-include-error` and shows nothing, because browsers block pages on disk from fetching other files.
- What to do: a mockup that uses `wa-include` has to be viewed through a local web server. For a mockup that must open by double-click, do not use it.
- In someone else's mockup: missing headers, footers or whole sections when opened from disk is this. Run a local server before judging the mockup.

### Scripts inside included content do not run
- Status: approved
- Test: `tests/web-awesome-display/include-scripts-do-not-run.html` (passed 2026-10-03, version 3.14.0)
- What happens: the HTML of an included file appears on the page, but a `<script>` inside it is not executed.
- What to do: this is the safe default. The component's definition has an `allow-scripts` attribute that changes it; only consider it for files you wrote.

### wa-markdown only renders markdown placed in a script tag
- Status: approved
- Test: `tests/web-awesome-display/markdown-needs-script-tag.html` (passed 2026-10-03, version 3.14.0)
- What happens: markdown written directly inside `<wa-markdown>` renders nothing. It has to be inside `<script type="text/markdown">` within the component.
- What to do: always use the script tag.

### wa-markdown passes HTML straight through, event handlers included
- Status: approved
- Test: `tests/web-awesome-display/markdown-does-not-sanitize.html` (passed 2026-10-03, version 3.14.0)
- What happens: HTML inside the markdown is put on the page as written. In the test a `<b onclick="...">` kept its handler, and clicking it ran the code.
- What to do: only ever give `wa-markdown` text you wrote yourself. Text from users, a database or another site must be cleaned on the server first. Write this into the blueprint's security section for any build that uses it.
- In someone else's mockup: ask where the markdown will come from in the real site. If the answer is "users", this is a security item.

### A split panel is only as tall as its content unless given a height
- Status: approved
- Test: `tests/web-awesome-display/split-panel-needs-height.html` (passed 2026-10-03, version 3.14.0)
- What happens: with a line of text in each side, a split panel is 19 pixels tall. With `style="height: 240px"` it is 240.
- What to do: give it a height.

### A zoomable frame is 16:9 tall by default
- Status: approved
- Test: `tests/web-awesome-display/zoomable-frame-tall-by-default.html` (passed 2026-10-03, version 3.14.0)
- What happens: a frame holding one line of text is 984 by 554 pixels.
- What to do: set its size in CSS to fit what it shows.

### Spinner and progress bar announce a default name
- Status: approved
- Test: `tests/web-awesome-display/default-accessible-names.html` (passed 2026-10-03, version 3.14.0)
- What happens: a spinner is announced as a progress bar named "Loading". A progress bar with no `label` is named "Progress"; with `label="Uploading photo"` it uses that. A badge is announced as a status.
- What to do: set `label` on a progress bar to say what is progressing.

### A card adds no role or heading of its own
- Status: approved
- Test: `tests/web-awesome-display/card-is-a-plain-container.html` (passed 2026-10-03, version 3.14.0)
- What happens: a card is announced as whatever was put inside it and nothing more. A heading in the `header` slot keeps its own level.
- What to do: put a real heading in each card, at the level that fits the page.

### A button group is a named group; arrow keys do not move between its buttons
- Status: approved
- Test: `tests/web-awesome-display/button-group-is-a-group.html` (passed 2026-10-03, version 3.14.0)
- What happens: with `label` it is announced as a group with that name; without, as an unnamed group. Focus moves between its buttons with Tab, not the arrow keys.
- What to do: always set `label`.

### A vertical divider is only one line of text tall unless it sits in a flex row
- Status: approved
- Test: `tests/web-awesome-display/vertical-divider-needs-flex.html` (passed 2026-10-03, version 3.14.0)
- What happens: in an ordinary block, `<wa-divider orientation="vertical">` is 19 pixels tall. Inside a 60 pixel flex row it stretches to 60.
- What to do: put vertical dividers inside a flex row.

### A skeleton is hidden from screen readers and does not animate unless effect is set
- Status: approved
- Test: `tests/web-awesome-display/skeleton-hidden-and-static.html` (passed 2026-10-03, version 3.14.0)
- What happens: it is announced as nothing at all. With no `effect` it is a still grey bar; `effect="sheen"` animates it.
- What to do: since a skeleton says nothing, tell assistive technology that content is loading some other way, for example `aria-busy="true"` on the region being filled.

### A progress ring is named Progress unless given a label
- Status: approved
- Test: `tests/web-awesome-display/progress-ring-names.html` (passed 2026-10-03, version 3.14.0)
- What happens: with no `label` it is announced as a progress bar named Progress; with `label="Upload"`, by that name. Text placed inside it is shown in the middle. It is 128 pixels across by default.
- What to do: set `label` to say what is progressing.

### A QR code is announced by its value unless given a label
- Status: approved
- Test: `tests/web-awesome-display/qr-code-name-is-its-value.html` (passed 2026-10-03, version 3.14.0)
- What happens: with no `label`, a screen reader reads out the whole encoded address. With a `label` it reads that. With no `value` it is a blank, unnamed image. It is drawn on a canvas.
- What to do: set `label` to say what scanning it does, and put the same address on the page as a normal link for people who cannot scan.

### A copy button copies its value, or the text or a property of the element named in from
- Status: approved
- Test: `tests/web-awesome-display/copy-button-sources.html` (passed 2026-10-03, version 3.14.0)
- What happens: `value="..."` copies that text. `from="words"` copies the text of the element with that id. `from="field.value"` copies that element's `value` property. A `from` that names no element fires `wa-error` and copies nothing; success fires `wa-copy`.
- What to do: use `from="id.value"` to copy what is in an input. In testing, copying failed until the browser was allowed clipboard access, so check it on the real site's address.

### A copy button has no accessible name
- Status: approved
- Test: `tests/web-awesome-display/copy-button-has-no-name.html` (passed 2026-10-03, version 3.14.0)
- What happens: it is announced as "button" with no name, with or without `copy-label`.
- What to do: record it as a known accessibility gap. Until the component fixes it, put visible text beside the button saying what it copies.
- In someone else's mockup: raise it wherever a copy button is the only way to get at something.

### A comparison's handle moves with the arrow keys and is announced as an unnamed scrollbar
- Status: approved
- Test: `tests/web-awesome-display/comparison-handle.html` (passed 2026-10-03, version 3.14.0)
- What happens: the divider starts at 50. With focus on the handle, the right arrow moves it to 51 and fires `change`. The handle is announced as a scrollbar with no name.
- What to do: give the before and after content its own descriptions in text, since the control does not explain itself.

### A scroller is a named region that can be reached and scrolled by keyboard
- Status: approved
- Test: `tests/web-awesome-display/scroller-is-focusable-region.html` (passed 2026-10-03, version 3.14.0)
- What happens: it is announced as a region named "Scrollable region" and can take keyboard focus, so wide content can be scrolled without a mouse.
- What to do: use it for wide tables and code. A plain `overflow: auto` box does not get this for free.

### wa-relative-time writes a phrase like '7 years ago' in the page's language
- Status: approved
- Test: `tests/web-awesome-display/relative-time.html` (passed 2026-10-03, version 3.14.0)
- What happens: it shows "7 years ago" in English and "vor 7 Jahren" with `lang="de"`, inside a real `<time>` element that keeps the exact moment.
- What to do: use it for "when" text. In the blueprint, say when a relative time should give way to a full date.

### wa-format-bytes counts in thousands
- Status: approved
- Test: `tests/web-awesome-display/format-bytes-decimal-units.html` (passed 2026-10-03, version 3.14.0)
- What happens: 1024 bytes is shown as "1.02 kB" and 1,500,000 as "1.5 MB". `display="long"` gives "1.5 megabytes" and `unit="bit"` gives "1.5 Mb".
- What to do: expect sizes to differ slightly from tools that count in 1024s. Say in the blueprint which the site should match.

### wa-animation does nothing until it has the play attribute, which it removes when finished
- Status: approved
- Test: `tests/web-awesome-display/animation-needs-play.html` (passed 2026-10-03, version 3.14.0)
- What happens: without `play` no animation runs and no events fire. With it, the animation runs and fires `wa-start` and `wa-finish`, and the `play` attribute is then removed.
- What to do: set `play` again each time it should run. Keep animation off anything a person has to read.

### An animated image starts paused and is a play button
- Status: approved
- Test: `tests/web-awesome-display/animated-image-starts-paused.html` (passed 2026-10-03, version 3.14.0)
- What happens: on load it is still. It is announced as a button named "Play animation" followed by the `alt` text, and clicking it starts the animation.
- What to do: always set `alt`. This is the accessible way to show a GIF: nothing moves until the person asks.

### wa-random-content shows one child, hides the rest, and announces the change
- Status: approved
- Test: `tests/web-awesome-display/random-content-shows-one.html` (passed 2026-10-03, version 3.14.0)
- What happens: of three children it shows one and gives the others the `hidden` attribute. `randomize()` swaps in a different one and fires `wa-content-change`. The shown content is also read out through a status region.
- What to do: use it for rotating tips or testimonials. Because every change is announced, do not rotate quickly.

### wa-mutation-observer fires wa-mutation when its content changes
- Status: approved
- Test: `tests/web-awesome-display/mutation-observer.html` (passed 2026-10-03, version 3.14.0)
- What happens: with `child-list`, adding an element inside it fires `wa-mutation`, with the change records in `event.detail.mutationList`.
- What to do: rarely needed in a mockup. If one appears, ask what it is reacting to and write that behaviour into the blueprint.

### wa-resize-observer fires wa-resize when its content changes size
- Status: approved
- Test: `tests/web-awesome-display/resize-observer.html` (passed 2026-10-03, version 3.14.0)
- What happens: widening the element inside it fires `wa-resize`, with the new size in `event.detail.entries`.
- What to do: as above: describe in the blueprint what should happen at which size.

### wa-intersection-observer adds a class while its content is on screen
- Status: approved
- Test: `tests/web-awesome-display/intersection-observer-class.html` (passed 2026-10-03, version 3.14.0)
- What happens: with `intersect-class="seen"`, the element inside gets the class `seen` when scrolled into view and loses it when scrolled away. `wa-intersect` fires each time, with `event.detail.entry.isIntersecting`.
- What to do: use the class for reveal-on-scroll effects with no script. Content must still be readable if the class is never added.

### wa-page supplies the page landmarks and a skip link
- Status: approved
- Test: `tests/web-awesome-display/page-landmarks.html` (passed 2026-10-03, version 3.14.0)
- What happens: it adds a "Skip to content" link and wraps its slots as banner, navigation, main and footer landmarks. A `<nav>` element placed in the `navigation` slot is announced as a navigation inside a navigation.
- What to do: put a plain `<div>` or list in the `navigation` slot, not a `<nav>`.
- In someone else's mockup: doubled landmarks inside a `wa-page` are this.

### Below its mobile-breakpoint, wa-page hides the navigation behind a toggle button
- Status: approved
- Test: `tests/web-awesome-display/page-mobile-view.html` (passed 2026-10-03, version 3.14.0)
- What happens: when the window is narrower than `mobile-breakpoint`, the page reports `view="mobile"` and offers a "Toggle navigation drawer" button. `showNavigation()` opens the drawer and Escape closes it.
- What to do: check the mockup at phone width. In the blueprint, say what the navigation becomes on a phone.

## Questions it raises

- For each date shown: a moment in time, or a calendar day that should read the same everywhere?
- Which language and region is the site for?
- Where does any markdown or included content come from in the real site?
- Does each coloured callout need to be announced, and as an error or a notice?
