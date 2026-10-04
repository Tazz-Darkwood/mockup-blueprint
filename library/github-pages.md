---
name: GitHub Pages
summary: Free static hosting from a GitHub repository. Read when a blueprint names it as the host, for the path, routing and header limits that change how a site must be built.
detect: ["github pages", "github\\.io"]
checked: 2026-10-03
source: https://docs.github.com/en/pages
---

# GitHub Pages

Serves the files in a repository as a website. It suits anything that is only pages, styles, scripts and data that can be public. It cannot run code on a server, keep a secret, check a password or store what a form sends.

Every note here is a draft. They were written from general knowledge and have not been confirmed by a deployment made with this skill. The first real deployment should check each one and record what was seen.

## Use it properly

Confirm with the user which account and repository to use before publishing anything. Publishing is visible to the world.

## Notes

### Everything published is public
- Status: draft
- Test: none. Needs a real deployment.
- What happens: any file in the published folder can be read by anyone, and so can the repository if it is public.
- What to do: nothing secret goes in the repository or the built files. A site that needs login, saved data or secrets needs a backend elsewhere, and the blueprint must say which.

### A project site is served from a sub-folder, which breaks paths that start with a slash
- Status: draft
- Test: none. Needs a real deployment.
- What happens: a project site lives at `https://<user>.github.io/<repo>/`. A path such as `/styles.css` then points at the wrong place.
- What to do: use relative paths, or set the framework's base path (`base` in Vite, `basePath` in a Next static export). A custom domain or a `<user>.github.io` repository serves from `/` and does not have the problem. The blueprint's `deployment` should say which case applies.

### Single-page apps return "not found" on refresh or a direct link
- Status: draft
- Test: none. Needs a real deployment.
- What happens: with client-side routing, an address like `/settings` has no file behind it.
- What to do: use hash routing, or copy `index.html` to `404.html` as a fallback.

### Folders and files starting with an underscore are skipped
- Status: draft
- Test: none. Needs a real deployment.
- What happens: the default processing ignores them, so they are missing from the published site.
- What to do: add an empty `.nojekyll` file at the top of the published folder.

### Response headers cannot be set
- Status: draft
- Test: none. Needs a real deployment.
- What happens: there is no way to add headers such as `Content-Security-Policy` or `Strict-Transport-Security`.
- What to do: put a Content-Security-Policy in a `<meta http-equiv>` tag, and tell the user about the limit. HTTPS itself is automatic; tick "Enforce HTTPS" in the repository's Pages settings.

### A Pages frontend talking to a backend on another domain needs care with logins
- Status: draft
- Test: none. Needs a real deployment with a backend.
- What happens: the two are different origins. The backend must allow the Pages address explicitly, and cookie-based sessions across the two need `SameSite=None; Secure`, which some browsers block.
- What to do: put both under one custom domain, which is the simple and safe way. Token-based sign-in also works, but then the token has to be kept somewhere in the browser, and anything kept where scripts can read it (`localStorage`) is taken by any script injection on the site; keep it in memory and renew it, or use the one-domain route. Decide before building the login.

## Questions it raises

- Which account and repository will hold the site?
- A custom domain, or the `github.io` address?
- Does anything on the site need a secret, a login or saved data? If so, where does that part run?
