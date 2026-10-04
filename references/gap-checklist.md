# Gap checklist: what mockups do not show

Walk this against the mockup after the first pass of context. Each line is something a builder will have to decide; the goal is that a person decides it instead. Skip what plainly does not apply, and turn anything unanswered into a question.

Contents: [By element type](#by-element-type) · [Screens nobody drew](#screens-nobody-drew) · [Behind the screens](#behind-the-screens) · [Real or placeholder](#real-or-placeholder) · [Accessibility](#accessibility) · [Security](#security)

## By element type

**Forms**
- Which fields are required? What format, length and range does each accept?
- What does each error say, and where does it appear?
- What happens on success: a message, a redirect, a cleared form?
- Where does the data go? Does submitting trigger anything else (an email, a notification, a record somewhere)?
- Can it be submitted twice by a double-click? Is an unfinished form saved?

**Buttons and links**
- What exactly happens? Where does the person end up?
- Is it reversible? Does it ask for confirmation?
- Is it ever disabled or hidden, and for whom?
- For links: internal route or external site? Same tab or new tab?

**Tables and lists**
- Where do the rows come from? Which are sample rows?
- What order? Can it be sorted, filtered or searched, and by what?
- How many at once: pages, "load more", or everything?
- What does it look like with zero rows? With one very long value?
- What can be done to a row, and by whom?

**Navigation**
- Where does each item go? Which items appear for which roles?
- What does it become on a phone?
- How is the current page marked?

**Search and filters**
- What is searched (which fields)? As you type or on submit?
- What shows when nothing matches?
- Do filters survive a page reload or a shared link?

**Charts and numbers**
- What precisely is each number: the formula, the time period, the units?
- How fresh is it: live, daily, at page load?
- Real metric or decoration?

**Dialogs, drawers and menus**
- What opens it, and what closes it (button, Escape, clicking outside)?
- Does unsaved input survive closing it?

**File uploads**
- Which types and what size limit? One file or several?
- Where are files stored, and who can see them afterwards?

**Login, sign-up and account**
- Email and password, a provider such as Google, a magic link?
- Can anyone sign up, or are accounts created by an admin?
- Password reset, email verification, sign out, session length?
- What does a signed-out person see when they open a private page?

**Payments**
- Which provider? One-off or subscription? Which currencies?
- What happens on a declined payment, a refund, a cancellation?
- Are receipts or invoices sent?

## Screens nobody drew

Mockups show the happy path. Ask whether each of these exists and what it looks like:

- Empty states: a brand-new account with no data yet
- Loading states: what shows while data arrives
- Error states: the server is down, the connection drops, a save fails
- Not found (404) and not allowed (signed in, but no permission)
- Password reset, email verification, sign-out confirmation
- Confirmation and success pages or messages
- Settings and profile, if there are accounts
- An admin view for whoever manages the content or users
- Emails and notifications the site sends: who gets them, when, and what they say
- Phone and tablet layouts, if only desktop was drawn

## Behind the screens

- **Data**: what is stored, for how long, and who can change or delete it. Is there existing data to import? What starter data does a fresh install need?
- **Roles**: what each role can see and do. Mockups usually show one role's view.
- **Timing**: anything scheduled or delayed (reminders, expiry, reports).
- **Scale**: roughly how many users and records. Ten or ten million changes the build.
- **Hosting**: static files only, or a server and database? Which domain? Who owns the accounts and pays?
- **Handover**: who updates content after launch, and how. Editing code, a spreadsheet, an admin screen?
- **Legal**: privacy policy, cookie notice, terms, age limits, anything specific to the country or industry.

## Real or placeholder

For everything visible, know which it is:

- Text: final copy, or filler?
- Images, logos and icons: final and licensed, or stand-ins?
- Names, numbers and dates in tables and charts: sample data?
- Menu items and buttons added to make the page look complete: real features, or decoration? Mark decoration `mock_only`.

## Accessibility

Fill `project.accessibility` with the target and the specifics. The usual target is WCAG 2.2 AA; confirm it with the user in plain words ("usable by people who rely on a keyboard or a screen reader, and readable for people with low vision").

Run `audit` first; it finds the mechanical problems. Then go through what it cannot judge and record the answers in `project.accessibility` or the element's `a11y` field:

- **Keyboard**: can everything be reached and used with Tab, Enter, Space and arrow keys? Is the tab order the visual order? Is focus always visible?
- **Custom widgets** (dropdowns, tabs, dialogs, date pickers, drag and drop): what are the keys? Where does focus go when a dialog opens, and where does it return when it closes?
- **Screen readers**: do icon-only buttons have names? Are errors and status changes ("Saved", "3 results") announced? Do images that carry meaning have alt text that says what they mean?
- **Colour**: contrast of at least 4.5:1 for text (3:1 for large text and for the edges of inputs and buttons). Is anything conveyed by colour alone, such as red for error with no icon or text?
- **Text and zoom**: does the layout hold at 200% zoom and at 320px wide?
- **Motion**: does anything animate or autoplay? Can it be paused, and does it respect the reduced-motion setting?
- **Things that happen by themselves**: does anything change with nobody on a screen (a clock, a simulation, reminders, things that expire, another service reporting back)? When does each run, where, and what must always be true afterwards? In the mockup these are usually faked by a script; say which, and put the rules in `project.background`.
- **3D and other canvases**: what is in the scene and where each object comes from (built in code, a model file; who makes it, and may it be used)? What shows if 3D cannot run on a device? Does it stop when out of sight? Can a visitor turn or zoom it, and does that get in the way of scrolling, with a mouse wheel and with a finger? Is it on every page or only one? What is its name for a screen reader, and can everything done inside it also be done with ordinary buttons?
- **Forms**: visible labels (not just placeholders), clear error text next to the field, and `autocomplete` values on personal-data fields.
- **Time limits**: does anything expire while someone is filling it in?

When the mockup itself fails (low-contrast brand colours, tiny tap targets), do not quietly redesign it. Record the fix the build should make and raise a question for the designer.

## Security

Fill `project.security`. It should let a builder answer each of these without guessing. Write "not applicable" with the reason where it does not apply.

- **Sign-in**: how people prove who they are. If passwords: who stores them (prefer an auth provider or a well-known library; never plain text), minimum rules, reset flow, lockout or rate limiting after failed attempts.
- **Sessions**: how a signed-in state is kept (secure, http-only cookies preferred) and when it ends.
- **Authorisation**: for every screen and every action that changes or reveals data, who is allowed. The check must happen on the server; hiding a button is not a permission.
- **Sensitive data**: list each kind the mockup collects (the `check` output names them). For each: where it is stored, who can read it, whether it is encrypted, how long it is kept, how it is deleted.
- **Payments**: card details go directly to the payment provider's hosted fields or checkout. They never touch the site's own server or database.
- **Forged requests**: a request that changes something must come from the site's own pages, not from a link or form on another site that borrows the visitor's signed-in state (CSRF). Use the framework's own protection, usually a hidden token in each form; with HTMX, send the token as a header on every request. Sign-in cookies get `SameSite=Lax` or stricter.
- **Input**: everything from a user is validated on the server as well as in the browser, and escaped when displayed (protection against script injection). Database queries use parameters, never pasted-together strings.
- **File uploads**: allowed types, size limit, stored outside the web root or in object storage, never executed, served with a safe content type.
- **Secrets**: API keys and passwords live in environment variables on the host, never in the repository or in anything sent to the browser. Name each secret in `deployment.secrets`; never write its value into the blueprint.
- **Transport**: HTTPS everywhere. If the frontend and backend are on different domains, state the allowed origins (CORS) rather than allowing all.
- **Abuse**: rate limits on sign-in, sign-up, contact forms and anything that sends email or costs money. Spam protection on public forms.
- **Third-party scripts**: which outside scripts the real site loads and why. Each one can read everything on the page.
- **After launch**: who gets told when something breaks, who updates dependencies, and whether there are backups.

Two hosting facts that change the answers:

- **GitHub Pages** serves static files that anyone can read. It cannot keep a secret, check a password, or store submitted data. A site on Pages that needs any of those must use a backend elsewhere (such as Render) or a third-party service, and the blueprint must say which.
- **Render** runs servers and databases. Secrets go in its environment settings. Free services sleep when idle, so the first request after a pause is slow; say whether that is acceptable.
