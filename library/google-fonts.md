---
name: Google Fonts
summary: Web fonts loaded with a link to fonts.googleapis.com. Read when a mockup uses that link, for the privacy question it raises and how to host the fonts yourself.
detect: ["fonts\\.googleapis\\.com", "fonts\\.gstatic\\.com"]
checked: 2026-10-03
source: https://fonts.google.com/
---

# Google Fonts

The quickest way to use a custom typeface in a mockup: one `<link>` tag in the head. The cost is that every visitor's browser contacts Google.

## Use it properly

Fine for mockups. For a real site, decide deliberately between keeping the link and hosting the font files yourself, and record the decision in the blueprint's `integrations` and `security` sections.

## Notes

### One link tag makes the visitor's browser contact two Google hosts
- Status: approved
- Test: `tests/google-fonts/two-outside-hosts.html` (passed 2026-10-03)
- What happens: the stylesheet comes from `fonts.googleapis.com`, and it points the browser at `fonts.gstatic.com` for the font files themselves. Both see the visitor's IP address on every visit.
- What to do: list both hosts in the blueprint's security section, and in any Content-Security-Policy (`style-src` for the first, `font-src` for the second).
- In someone else's mockup: the skill's audit reports `fonts.googleapis.com` as a third party. The second host is not written in the HTML, so add it by hand.

### Hosting the font files yourself removes both requests
- Status: draft
- Test: none. Needs the font files downloaded into a real project and the page checked for outside requests.
- What happens: downloading the font files into a `fonts/` folder and declaring them with `@font-face` in the site's own CSS should give the same look with no contact with Google.
- What to do: unconfirmed until done once in a real build. When it is, record the steps that worked and which file formats were needed.

## Questions it raises

- Keep loading the fonts from Google, or put the font files on the site itself?
