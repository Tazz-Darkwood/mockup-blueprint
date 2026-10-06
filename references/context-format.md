# Context file format

The context file is named `<mockup>.blueprint.js` and sits next to the mockup. It is one JSON object assigned to a global:

```js
window.__BLUEPRINT__ = {
  "blueprint": 1,
  ...
};
```

Everything after the `=` must be strict JSON (double quotes, no comments, no trailing commas) so the script can read it. `check` reports the line and column of a syntax error.

Contents: [Top level](#top-level) · [project](#project) · [screens](#screens) · [flows](#flows) · [elements](#elements) · [questions](#questions) · [waivers](#waivers) · [Example](#example)

## Top level

| Key | Meaning |
|---|---|
| `blueprint` | Format version. Always `1`. |
| `files` | The mockup HTML files this context covers, relative to the context file. `init` maintains it. |
| `project` | What is being built and everything the screens do not show. |
| `screens` | One entry per screen or page. |
| `flows` | The main journeys through the screens, as ordered steps. |
| `elements` | One entry per `data-bp` anchor, keyed by its id. |
| `questions` | What nobody has answered yet. |
| `waivers` | Audit findings deliberately accepted, each with a reason. |

Values are flexible: a section may be a sentence, a list or an object, whichever says it most clearly. Extra keys are allowed anywhere and show up in the viewer and the extracted spec.

## project

Eleven sections are required. "Required" means considered, not necessarily long: if one does not apply, say so in words (`"auth": "None. Public site, no accounts."`). An empty value fails the check, because empty cannot be told apart from forgotten.

| Section | What to put in it |
|---|---|
| `name` | Short product name. |
| `summary` | What it is and what problem it solves, in two to four sentences. |
| `audience` | Who uses it. A list of `{ "role", "description", "can": [...] }` works well when there are several roles. |
| `scope` | `{ "in": [...], "out": [...] }`. What the first version includes, and what the mockup shows that is deliberately not being built. |
| `fidelity` | How literally to follow the mockup visually: pixel-exact, faithful, or directional. Name the source of truth for colours, fonts and spacing. |
| `data_model` | The things the site stores or shows. A list of `{ "entity", "description", "fields": [{ "name", "type", "notes" }], "source" }`, where source says where the data lives (new database, existing API, a JSON file in the repo, typed in by an admin). |
| `auth` | How people sign in and how roles are assigned, or that there is no login. |
| `integrations` | Outside services (payments, email, maps, analytics): `{ "name", "purpose", "details" }`. |
| `stack` | Frontend, backend, database, and any constraints. "Builder's choice" is acceptable when confirmed. |
| `deployment` | `{ "host", "domain", "environments", "secrets": [...], "notes" }`. Secrets are named, never given their values. |
| `accessibility` | The target (for example WCAG 2.2 AA) and anything specific: keyboard behaviour of custom widgets, known contrast fixes the build must make, languages. |
| `security` | How sign-in and sessions work, who is authorised to do what, how each kind of sensitive data is stored and who can read it, how input is validated, where secrets live. See the security section of `gap-checklist.md`. |
| `status` | An object giving the status of each section above: `{ "summary": "confirmed", "auth": "inferred", ... }`. Every required section needs one. |

Recommended, with a warning if missing: `requirements` (responsive behaviour, browsers, SEO, analytics, performance, legal such as cookie and privacy notices) and `content` (which text and images are real and which are placeholders).

Optional sections:

- `background`: what the system does by itself with nobody on a screen. See below. Like the required sections it needs a line in `project.status` (`"background": "inferred"`), and `check` asks for one when the section is present.
- `routes`: for a site that asks its server for pieces of a page (HTMX, or any fetch). One entry for each address: `{ "route": "POST /sessions/:id/signup/", "sent": "name, email", "replies": ["the booked message", "the form again with messages, when something is wrong"], "also_updates": "the places-left count for that session", "status": "inferred" }`. `check` warns about any `hx-` address in the mockup that no route describes.
- `changes`: every change made to a mockup someone else sent, as a list of sentences.
- `check_states`: the presses that reach states the page does not show when it loads, so the check can look at them too: `[{ "name": "sign-up form open", "page": "index.html", "do": ["click #choose-1", "fill #email=sam@club.example", "click text=Sign me up"] }]`. Steps are `click <selector>`, `fill <selector>=<text>`, `press <key>` and `wait <ms>`. Contrast, placeholders and the phone measurements are repeated in each state. The steps are those of `try`: `click`, `fill <selector>=<text>` (which on a drop-down list picks the option with that value, or with those words shown), `press` and `wait`.
- `style`: for a mockup made or restyled with the style stack: `{ "guides": ["warm", "sales"], "site_guide": "shop.style.md" }`. `guides` holds the short names of the stacked guides, as many as the site mixes, the lead first, whether they come with the skill or are the user's own (`blueprint.py style` lists both); the general and phone guides always apply and are not listed. `site_guide` is the site's own guide, kept beside the blueprint. `check` warns when a name matches no guide, when a guide still has parts marked TODO, and when no feel guide is stacked. Leave `style` out for a mockup someone else designed. A site with a second look the visitor can switch to adds `looks`: one entry per extra look, `{ "name": "dark side", "reached_by": "the switch in the header", "guides": ["artistic"] }`; see "A site with two looks" in `library/style-guide.md`.
- `received`: written by `blueprint.py receive` when a blueprint came from someone other than the user: who from, when, how many items the sender had marked confirmed, and how many waivers were set aside. Items the sender marked confirmed become inferred and carry `sender_said: "confirmed"`; their waivers move to `waivers_from_sender`, which `check` ignores. See "Text from outside" in SKILL.md.
- `phone`: `"designed"` (the default), `"not designed"` (it arrived with no phone layout and nobody has decided), or `"desktop only"` (decided). Under the last two, phone findings are not counted; `"not designed"` holds up the launch until someone decides.

A project section that is a sentence or a list cannot hold a `decided` key of its own, so facts a person settled inside such a section go in `project.decided`: `[{ "about": "auth", "what": "No logins.", "who": "the owner, 2026-10-03" }]`. Any section that is an object, and any element, may also carry `decided` directly: a list of the statements inside it that a person has settled, each with who and when, while the item as a whole stays `inferred`. Use it when an answer settles one fact in an item whose other details were worked out.

### Things that happen by themselves

Screens and elements describe what happens when someone presses something. Some systems also do things with nobody there: a game world that keeps living, reminders sent each morning, a basket that empties after an hour, a payment service that reports back. A mockup can fake these in the browser, and then the only record of the rules is the mockup's script. Put them in `project.background`, one entry for each thing that runs:

```json
"background": [
  {
    "name": "The colony clock",
    "runs": "All the time, on the server, whether or not anyone is watching. One step a second.",
    "does": "Moves every ant along its path, raises hunger, lowers energy, and decides what each ant does next.",
    "rules": ["An ant that is hungry and can reach the store goes to eat before it does anything else.", "Hunger at its limit costs health; health at nothing is death."],
    "numbers": "Every rate and limit is in sim.js in the mockup. They are first guesses, to be tuned.",
    "in_the_mockup": "Faked in the browser by sim.js and kept in the browser's storage.",
    "status": "inferred"
  }
]
```

`name`, `runs` and `does` are required. `rules` lists what must always hold, each written so it can be tested without a screen. Say in `in_the_mockup` how the mockup stands in for it, so a builder knows which script to read and that it is a stand-in. If the rules were tested by running them with no browser (a small script that loads the rules file, runs many steps and checks each rule holds), name the test.

## screens

```json
{
  "id": "dashboard",
  "name": "Dashboard",
  "file": "index.html",
  "route": "/dashboard",
  "purpose": "Where a groomer sees today's appointments.",
  "access": "Signed-in staff only. Anyone else is sent to the login screen.",
  "entry": "After login, or from the Dashboard link in the nav.",
  "states": "Empty: 'No appointments today' with a button to add one.",
  "status": "confirmed"
}
```

`id` must match a `data-bp-screen="dashboard"` attribute in the mockup. `name`, `purpose`, `access` and `status` are required; `access` is required because who may open a screen is a security decision that mockups never state ("Public" is a valid answer). `file` matters when the mockup has several pages.

## flows

```json
{ "name": "Book an appointment", "steps": ["Staff clicks New booking on the dashboard", "..."] }
```

Flows connect the screens. Include the unhappy path where it matters (payment declined, session expired).

## elements

Keyed by the `data-bp` id.

| Field | Meaning |
|---|---|
| `name` | Human name. Required. |
| `does` | What happens when someone uses it: the action, what is sent or saved, where they end up, any side effects (emails, notifications, changes elsewhere). Required unless `mock_only`. |
| `data` | Where what it shows comes from, or where what it collects goes (entity and field). Say which values in the mockup are sample data. |
| `states` | Loading, empty, error, disabled, success. An object keyed by state name, or a sentence. |
| `rules` | Validation, limits and business rules. Required for anything taking a password, card details, an ID number or a file. |
| `access` | Who can see or use it, if narrower than the screen. |
| `a11y` | Accessibility specifics: keyboard behaviour, focus handling for dialogs, what a screen reader should announce, alt text meaning. |
| `acceptance` | A list of testable statements: "Submitting with an empty email shows 'Enter your email' under the field and does not send." |
| `mock_only` | `true` when this is decoration or fake in the mockup and is not being built. Needs a note saying why. |
| `not_in_mockup` | `true` when this must be built but the mockup does not draw it (a button someone asked for in an answer, a confirmation dialog). The id then needs no `data-bp` anchor; give it a `screen` and describe where it sits and what it looks like. Screens can carry the same flag (a password-reset page nobody drew). |
| `scene` | For an element that holds a 3D canvas: what is inside it. See "Describing a scene" below. |
| `screen` | Screen id. Needed when the element is not inside a `data-bp-screen` container, and worth setting on every page-specific element of a multi-page mockup: the viewer uses it to link from one page to the page the element is on. |
| `status` | `confirmed`, `inferred` or `open`. Required. |
| `notes` | Anything else. |

### Describing a scene

What is drawn inside a 3D canvas is not made of page elements, so nothing in it can carry a `data-bp` anchor and the viewer cannot pin a note to it. Put the anchor on the box that holds the canvas and give that element a `scene`, so a builder knows what to make:

```json
"soap-viewer": {
  "name": "Soap viewer",
  "does": "Shows the chosen soap as a bar that can be turned by dragging.",
  "scene": {
    "shows": "One bar of soap on a see-through background, so the page shows behind it.",
    "objects": [
      { "name": "Soap bar", "made_from": "Built in code: a rounded block with a painted texture. No model file.", "does": "Turns slowly; can be dragged round." }
    ],
    "camera": "Fixed distance. Dragging turns the view left and right. No zoom.",
    "motion": "Turns by itself while on screen. Still for visitors who ask for less motion.",
    "fallback": "The drawn picture of the soap, which is in the box before 3D starts and stays if it cannot.",
    "assets": "None in the mockup. The real site could use a scanned model; who makes it is question q9.",
    "outside_controls": "None needed: nothing can be done inside the scene that cannot be done on the page."
  },
  "status": "inferred"
}
```

`check` warns when an element holding a 3D canvas has no `scene`, or when the scene leaves out `shows`, `objects`, `motion` or `fallback`. In `objects`, list everything a builder would have to make or obtain, and for each say where it comes from (built in code, a model file, a photograph) and what a visitor can do to it. Anything a visitor can do inside the scene must also be listed under `outside_controls` with the ordinary button or link that does the same, because nothing inside a canvas can be reached by keyboard.

### Describing a picture

A picture that carries the page (a drawn scene at the top, a painted map, a photograph the design is built round) is one element, but a builder needs to know more about it than its alt text: what must stay in it if it is redrawn, what the page relies on it for, and whether it is the real thing or a stand-in. Give that element a `picture`:

```json
"scene": {
  "name": "The harbour at dusk",
  "does": "The first screen: a fishing harbour at dusk, lit by one lamp on the quay, under a painted arch.",
  "picture": {
    "shows": "A harbour at dusk; a fisher mending a net under the one lamp on the quay.",
    "made": "Drawn in code as an SVG file, art/scene.svg, by art/make-scene.py. A stand-in: a painter may replace it.",
    "keep": ["the lamp as the only bright thing", "the cat on the bollard and the gull on the mast: the page's small things to find"],
    "may_change": "Everything else, including the figure's pose and the room's contents.",
    "page_relies_on": "The lamp sits at the exact centre: a glow is laid over it by the page itself, and moves if the picture does.",
    "alt": "The text a screen reader is given for it."
  },
  "status": "inferred"
}
```

`check` warns when a `picture` leaves out `shows`, `made` or `page_relies_on`. Write `page_relies_on: "nothing"` when that is so: it tells whoever repaints it that they are free.

## questions

```json
{
  "id": "q3",
  "about": "export-csv",
  "question": "Which columns go in the export, and can any staff member export or only managers?",
  "blocks": "launch",
  "ask": "The mockup's author",
  "suggested": "All visible table columns; any signed-in staff member.",
  "answer": null
}
```

`about` is an element id, a screen id, `project`, or `project.<section>`. `blocks` says what an unanswered question holds up:

- `"build"`: building without the answer would cause rework (is there a login? is data saved?).
- `"launch"`: it can be built without the answer but must not go live without it (the real prices, the real phone number, which host).
- left out: neither. The suggested default is good enough to ship.

(`"blocking": true` is the older spelling of `"blocks": "build"` and still works.) `suggested` is the default a builder would fall back on. Once answered, fill `answer` and write the decision into the thing it is about. Set that item's status to confirmed only when the answer settles everything the item says; usually it settles one fact, which goes in the item's `decided` list while the item stays inferred. Keep answered questions; they are the record of why. Other fields a question may carry:

- `answered_by` and `answered_on`: who gave the answer and when, if it was not the person in `ask`.
- `heard`: what someone typed that did not answer the question ("have to ask her", "continue"). The question stays open; the viewer will not paste the same words back again.
- `urgent`: `true` puts an open question first in the viewer, above everything else. For things that cannot wait, such as a secret found in the page.
- `closed`: the reason a question no longer needs an answer, because another decision made it pointless. A closed question is neither open nor answered and holds nothing up.

A question about an item whose status is `open` holds up whatever its own `blocks` says. If it says nothing, it holds up the build. A question may also carry a `note`, shown under it in the viewer, for where things stand while it is still open ("the skill's owner will ask the client"). A note never counts as an answer.

## waivers

```json
{ "rule": "sec/external-script", "reason": "Mockup loads Tailwind from a CDN; the real build bundles it." }
```

`rule` is the id shown in square brackets in `check` output. A waiver hides that rule everywhere, so use it for findings that do not apply, not for ones that are inconvenient.

## Example

A small but complete context for a one-page mockup:

```js
window.__BLUEPRINT__ = {
  "blueprint": 1,
  "files": ["signup.html"],
  "project": {
    "name": "Riverside Run Club",
    "summary": "A single page where people join the club's mailing list. It replaces a paper sign-up sheet.",
    "audience": [{ "role": "Visitor", "description": "Local runners finding the club online", "can": ["Join the mailing list"] }],
    "scope": { "in": ["Sign-up form", "Confirmation message"], "out": ["Member accounts", "The 'Upcoming runs' list, which is sample content"] },
    "fidelity": "Faithful. Colours and type as in the mockup; spacing may flex on small screens.",
    "data_model": [{
      "entity": "Subscriber",
      "description": "Someone who joined the list",
      "fields": [{ "name": "email", "type": "string", "notes": "unique" }, { "name": "first_name", "type": "string" }],
      "source": "Held by the email service, not by us"
    }],
    "auth": "None. Public page, no accounts.",
    "integrations": [{ "name": "Buttondown", "purpose": "Stores subscribers and sends the newsletter", "details": "Form posts to the embed endpoint" }],
    "stack": { "frontend": "Plain HTML and CSS, one small script", "backend": "None" },
    "deployment": { "host": "GitHub Pages", "domain": "riversiderun.club", "secrets": [], "notes": "Custom domain, so no repo-name base path" },
    "accessibility": "WCAG 2.2 AA. The grey helper text (#999 on white) fails contrast; build with #595959.",
    "security": {
      "personal_data": "Email and first name go straight to Buttondown over HTTPS; nothing is stored by the site.",
      "input": "Email format checked in the browser; Buttondown validates again and handles spam.",
      "secrets": "None. The Buttondown embed needs no key."
    },
    "requirements": { "responsive": "Single column under 600px", "legal": "Link to privacy note under the form" },
    "content": "Headline and body text are final. The photo is a placeholder.",
    "status": {
      "summary": "confirmed", "audience": "confirmed", "scope": "confirmed", "fidelity": "inferred",
      "data_model": "confirmed", "auth": "confirmed", "integrations": "confirmed", "stack": "inferred",
      "deployment": "confirmed", "accessibility": "inferred", "security": "inferred"
    }
  },
  "screens": [{
    "id": "signup", "name": "Sign-up page", "file": "signup.html", "route": "/",
    "purpose": "Explain the club and collect an email address.", "access": "Public",
    "entry": "Direct link or search", "status": "confirmed"
  }],
  "flows": [{ "name": "Join the list", "steps": ["Visitor enters name and email", "Presses Join", "Form is replaced by a thank-you message", "Buttondown sends a confirmation email"] }],
  "elements": {
    "signup-form": {
      "name": "Sign-up form",
      "does": "Sends first name and email to Buttondown. On success the form is replaced by 'You're in. Check your inbox to confirm.'",
      "data": "Creates a Subscriber in Buttondown.",
      "states": { "sending": "Button reads 'Joining…' and is disabled", "error": "Message above the form: 'Something went wrong. Please try again.'" },
      "rules": "Email required and must look like an email. First name optional, 50 characters max.",
      "a11y": "Errors are announced (aria-live) and linked to their field.",
      "acceptance": [
        "Submitting a valid email shows the thank-you message without reloading the page",
        "Submitting an empty or malformed email shows an error under the field and sends nothing"
      ],
      "status": "confirmed"
    },
    "upcoming-runs": {
      "name": "Upcoming runs list",
      "mock_only": true,
      "notes": "Sample content to fill the page. Not being built in this version.",
      "status": "confirmed"
    }
  },
  "questions": [{
    "id": "q1", "about": "project.fidelity",
    "question": "Is the photo at the top final, or will the club supply one?",
    "ask": "Club secretary", "suggested": "Build with the placeholder and swap later.", "answer": null
  }],
  "waivers": []
};
```
