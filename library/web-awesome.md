---
name: Web Awesome
summary: Web component library (wa-button, wa-input, wa-dialog and so on) from the Font Awesome team. Start here for any mockup that uses wa- tags; setup, loading and the rules that apply to every component.
detect: ["<wa-", "webawesome"]
version: 3.14.0
checked: 2026-10-03
source: https://webawesome.com/docs/
---

# Web Awesome

A library of ready-made interface pieces written as custom HTML tags that start with `wa-`. It is the successor to Shoelace. The free version loads from a CDN with two tags and needs no build step, which is why it suits mockups.

It changes often: there were six releases between 18 June and 24 September 2026. Pin the version in the URL, and re-run the tests when moving to a newer one.

This file covers setup and what is true of every component. Four more files cover the components by family, and `blueprint.py library <mockup>` lists the ones a given mockup needs:

- `web-awesome-forms.md`: inputs, selects, radios, checkboxes, sliders and how they submit.
- `web-awesome-overlays.md`: dialogs, drawers, dropdown menus, tooltips, popovers, toasts.
- `web-awesome-navigation.md`: tabs, accordions, details, trees, pagination, breadcrumbs, steppers, carousels.
- `web-awesome-display.md`: buttons, icons, tags, callouts, avatars, date and number formatting, includes, markdown.

Version 3.14.0 has 73 components. All of them were loaded and given the same basic checks, and every one is covered by at least one behaviour note.

## Use it properly

For a mockup, put these in the `<head>`. Tested with 3.14.0 (see the first note):

```html
<link rel="stylesheet" href="https://ka-f.webawesome.com/webawesome@3.14.0/styles/themes/default.css">
<script type="module" src="https://ka-f.webawesome.com/webawesome@3.14.0/webawesome.loader.js"></script>
```

Optional stylesheets, from the same `styles/` folder (per the documentation, read 2026-10-03):

- `utilities.css`: layout and helper classes, and the `wa-cloak` loading helper.
- `native.css`: restyles plain HTML elements to match.
- `webawesome.css`: all of the above plus the default theme in one file. Checked by reading the file: it only imports the others.

Rules that save time, each explained in the notes below:

- Always write a closing tag: `<wa-icon name="gear"></wa-icon>`, never `<wa-icon name="gear" />`.
- Give every submit button `type="submit"`.
- Give every field a `name` and a `label`.
- Listen for `input` and `change` on fields, and for `wa-` events on everything else.
- Wait for `customElements.whenDefined(...)` before calling anything on a component from a script.

Two things seen in the cold test of 2026-10-03 and not yet given tests of their own: a page that uses `wa-cloak` is still seen by the skill's audit, which waits before looking; and only a handful of the theme's variables have tests here, so after mapping tokens onto it, look for defaults that leaked through. Hint text under a field kept its own size until `--wa-font-size-smaller` was set.

## Notes

### The theme stylesheet plus the loader script is enough to start
- Status: approved
- Test: `tests/web-awesome/setup-loads.html` (passed 2026-10-03, version 3.14.0)
- What happens: with only the two tags above, a `<wa-button>` on the page registers and renders. No other setup is needed for the free CDN version.
- What to do: start every Web Awesome mockup from those two tags, with the version pinned.
- In someone else's mockup: if components show as plain unstyled text, check both tags are present, that the script has `type="module"`, and that both URLs carry the same version.

### All 73 components load from the free CDN
- Status: approved
- Test: `tests/web-awesome/every-component-loads.html` (passed 2026-10-03, version 3.14.0)
- What happens: every component named in the library's own manifest registers when loaded from the free CDN with the two tags above. None needed a paid plan to load.
- What to do: run this test first against a new version. A component that has been renamed or removed shows up here.

### Colour, font and corner radius are set with CSS variables on the page
- Status: approved
- Test: `tests/web-awesome/theme-with-variables.html` (passed 2026-10-03, version 3.14.0)
- What happens: setting variables on `:root` in the page's own stylesheet restyles every component. Tested: `--wa-color-brand-fill-loud` and `--wa-color-brand-on-loud` (the filled brand button and its text), `--wa-font-family-body` (component text), `--wa-border-radius-scale` (0 makes every corner square), `--wa-form-control-border-color` and `--wa-form-control-background-color` (fields).
- What to do: this is how a design from `style-guide.md` is applied to Web Awesome. Map the project's own tokens onto these variables once, at the top of the stylesheet, and never restyle components one at a time. The theme defines many more variables in the same families (`--wa-color-brand-...`, `--wa-color-text-...`, `--wa-color-surface-...`, `--wa-space-...`); read the theme file for the names, and check the result by eye, since only the six above have a test.
- In someone else's mockup: default blue buttons and the system font beside a carefully chosen page design mean these variables were never set.

### A self-closing component tag swallows everything after it
- Status: approved
- Test: `tests/web-awesome/self-closing-swallows.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-icon name="gear" />` is not closed by the slash. The browser ignores it, so everything that follows in the same parent becomes a child of the icon. In the test, the paragraph written after the icon ended up inside it and was not visible on the page.
- What to do: always write `<wa-icon name="gear"></wa-icon>`. This is true of every custom element, not only Web Awesome.
- In someone else's mockup: the sign is content that exists in the source but is missing on screen, starting just after a component. The skill's `audit` reports it as `html/self-closing` with the line number.

### A misspelled component tag never loads, and the page shows no error
- Status: approved
- Test: `tests/web-awesome/typo-tag-silent.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-buton>` stays an unknown element for ever. Its text still shows, as plain text with no styling, so it is easy to miss. The only message is a warning in the browser console ("Unable to autoload").
- What to do: after loading a page, check for components that never loaded: `document.querySelectorAll(':not(:defined)')` should be empty.
- In someone else's mockup: the skill's `check` and `audit` report these as `html/never-loaded` when a browser is available, and the viewer's Checks tab lists them. The same sign appears when a real tag is used but the loader script is missing.

### Components are not ready when the page is first parsed
- Status: approved
- Test: `tests/web-awesome/not-ready-at-parse.html` (passed 2026-10-03, version 3.14.0)
- What happens: a plain script placed right after a `<wa-button>` finds it unregistered and unrendered. A moment later it is both.
- What to do: before a script reads or calls anything on a component, wait: `await customElements.whenDefined('wa-button')`. The documentation also describes an `allDefined()` helper exported by the loader (not tested here).
- In someone else's mockup: the sign is script that works on a second click or after a refresh but not on first load, or an error such as "is not a function" at start-up.

### A component added to the page later is loaded automatically
- Status: approved
- Test: `tests/web-awesome/added-later-loads.html` (passed 2026-10-03, version 3.14.0)
- What happens: adding a `<wa-badge>` with script, when no badge was on the page before, registers and renders it within a couple of seconds. The loader watches the page.
- What to do: nothing special is needed for content inserted by script. Allow for the short delay the first time a kind of component appears.

### A wa-button inside a form does not submit it unless it has type="submit"
- Status: approved
- Test: `tests/web-awesome/button-does-not-submit.html` (passed 2026-10-03, version 3.14.0)
- What happens: a native `<button>` inside a form submits it by default. A `<wa-button>` is the opposite: its default type is `button`, so pressing it does nothing to the form. With `type="submit"` it submits.
- What to do: put `type="submit"` on the button meant to send the form.
- In someone else's mockup: a form whose button "does nothing" is usually this. Record in the blueprint which button submits, since the mockup may not show it.

### Web Awesome fields are included in the form's data, if they have a name
- Status: approved
- Test: `tests/web-awesome/form-data.html` (passed 2026-10-03, version 3.14.0)
- What happens: inside a native `<form>`, a `<wa-input name="email">` and a checked `<wa-checkbox name="agree">` appear in the form's data like native fields (the checkbox as `on`). An unchecked checkbox is left out, and so is any field with no `name`.
- What to do: give every field a `name`. Read the values with `new FormData(form)` as usual.
- In someone else's mockup: fields with no `name` will be silently missing from what the form sends. List the fields and their names in the blueprint element.

### A required empty field blocks submit and fires wa-invalid
- Status: approved
- Test: `tests/web-awesome/required-blocks-submit.html` (passed 2026-10-03, version 3.14.0)
- What happens: with `required` on a `<wa-input>`, pressing the submit button while it is empty does not submit the form, the form reports itself invalid, and the field fires `wa-invalid` (and the native `invalid`). Once filled in, the form submits.
- What to do: use the standard attributes (`required`, `pattern`, `minlength`, `maxlength`). The documentation is explicit that this is a convenience and not a replacement for checking input on the server.
- In someone else's mockup: validation shown in the mockup is browser-side only. The blueprint's `rules` for the form still has to say what the server checks.

### Typing in a field fires the native input and change events, not wa- ones
- Status: approved
- Test: `tests/web-awesome/native-event-names.html` (passed 2026-10-03, version 3.14.0)
- What happens: typing in a `<wa-input>` fires `focus`, `input`, `change` and `blur` on the component. Listeners for `wa-input` and `wa-change` never fire.
- What to do: listen for `input` and `change` on fields.
- In someone else's mockup: script that listens for `wa-input`, `wa-change`, or the older Shoelace names will sit there doing nothing. Search the scripts for those names.

### A dialog fires wa-show, wa-after-show, wa-hide and wa-after-hide
- Status: approved
- Test: `tests/web-awesome/dialog-events.html` (passed 2026-10-03, version 3.14.0)
- What happens: setting `open = true` on a `<wa-dialog>` fires `wa-show` then `wa-after-show`. Setting `open = false` fires `wa-hide` then `wa-after-hide`. Events that belong to a component, as opposed to field typing, keep the `wa-` prefix.
- What to do: open and close with the `open` property or attribute. Use `wa-after-show` and `wa-after-hide` for anything that should wait for the animation.

### Icons are fetched from a second outside host
- Status: approved
- Test: `tests/web-awesome/icons-second-host.html` (passed 2026-10-03, version 3.14.0)
- What happens: components load from `ka-f.webawesome.com`, but a `<wa-icon>` fetches its picture from `ka-f.fontawesome.com`. A page with one icon made 30 requests in total.
- What to do: in the blueprint's security section list both hosts as third parties, and allow both in any Content-Security-Policy. Each sees every visitor's IP address.
- In someone else's mockup: the skill's audit names the hosts a page loads from, but only the ones written in the HTML. The icon host is contacted by script, so add it by hand.

### An unknown icon name shows nothing and fires wa-error
- Status: approved
- Test: `tests/web-awesome/unknown-icon-blank.html` (passed 2026-10-03, version 3.14.0)
- What happens: `<wa-icon name="no-such-icon">` draws nothing at all, with no placeholder. The icon fires `wa-error`, and never `wa-load`.
- What to do: check every icon name against the Font Awesome free set. In an icon-only button, a wrong name leaves an empty button.
- In someone else's mockup: look for empty gaps where an icon should be, especially inside buttons, which then have no visible content and no accessible name.

### Adding the wa-dark class to the html element switches to dark mode
- Status: approved
- Test: `tests/web-awesome/dark-mode-class.html` (passed 2026-10-03, version 3.14.0)
- What happens: with `class="wa-dark"` on `<html>`, the theme's surface colour changes from white to a near-black (`#101219`), and components follow.
- What to do: toggle that one class for dark mode. Colours written by hand in the mockup's own CSS do not follow; use the theme's `--wa-color-...` variables for anything that should.

### wa-cloak hides the page until components are ready
- Status: approved
- Test: `tests/web-awesome/cloak-hides-until-ready.html` (passed 2026-10-03, version 3.14.0)
- What happens: with `class="wa-cloak"` on `<html>` and `utilities.css` loaded, the page is invisible while components load and appears once they are ready, which avoids the flash of unstyled text. The stylesheet caps the wait at 2 seconds.
- What to do: add it to any mockup that will be shown to people, together with `utilities.css`.

### wa-cloak does nothing unless utilities.css is loaded
- Status: approved
- Test: `tests/web-awesome/cloak-needs-utilities.html` (passed 2026-10-03, version 3.14.0)
- What happens: with only the theme stylesheet, `class="wa-cloak"` has no effect: the page is fully visible while components are still loading. The rule that does the hiding lives in `utilities.css`.
- What to do: load `utilities.css` (or `webawesome.css`) whenever `wa-cloak` is used.
- In someone else's mockup: a `wa-cloak` class with no utilities stylesheet is a sign the author expected a clean load and is not getting one.

### Hosting the files yourself needs a base path
- Status: draft
- Test: none. Needs a copy of the package served from our own folder.
- What happens: according to the documentation (read 2026-10-03), when the files are not loaded from the CDN the library has to be told where they are, either with a `data-webawesome="/path/to/dist"` attribute on the script tag or by calling `setBasePath()`. Without it, components and icons are looked for in the wrong place.
- What to do: treat as unconfirmed until tried. It matters for any build that must not depend on outside hosts.

## What the skill's script understands

Checked on 2026-10-03 with a small Web Awesome page:

- `inventory` and coverage count `wa-button`, `wa-input`, `wa-select`, `wa-checkbox` and similar tags as interactive, so they need context like native controls.
- A field's `label` attribute counts as its label. A field with no label is reported.
- `type="password"` and names such as `email` on a `wa-input` are recognised as sensitive data.

## Questions it raises

- Will the real site load Web Awesome from the CDN, or host the files itself? (CDN means two outside hosts see every visitor.)
- Free version, or a Pro project with a kit code? (Pro changes the install tags and unlocks more icons.)
- Does the site need a dark mode?
- Which version is the build pinned to, and who checks the notes again when it is upgraded?
