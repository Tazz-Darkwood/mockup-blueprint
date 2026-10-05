---
name: Django with Postgres
summary: Server framework that makes HTML pages, handles forms and sign-in, and keeps data in a database. Read when a blueprint names Django or Postgres, above all when the site holds anything of value (coins, items, bookings, places) that two requests could fight over. What the server must do that a mockup cannot show, and the traps in forms, sign-in, settings and money moves.
detect: ["\\bdjango\\b", "csrfmiddlewaretoken", "csrf_token", "\\bpostgres", "X-CSRFToken"]
version: 6.1.1
needs: django psycopg[binary] pixeltable-pgserver
checked: 2026-10-03
source: https://docs.djangoproject.com/en/6.1/ and the tests named in each note, run against Django 6.1.1 and PostgreSQL 18.4
---

# Django with Postgres

Django runs on a server. It answers each request with HTML it builds from templates, checks forms, signs people in, and reads and writes a database through its own model classes. Postgres is the database to pair it with for anything that matters: unlike the small database Django starts with (SQLite), it can lock a row while one request works on it.

A mockup has no server, so nothing here can be seen in one. Every note below is something the blueprint has to say and the build has to do. With HTMX for the moving parts of a page (see `htmx.md`), the mockup's pretend server stands in for Django, and each route in it becomes a Django view.

The tests behind these notes are small Python scripts, not pages. They need Django, a database driver and a throwaway Postgres, all installed into the skill's own environment by `blueprint.py doctor --setup --for django` (no system install, no administrator rights).

## Use it properly

For the blueprint, when the stack is Django:

- List every route the pages call, with what it is sent and each reply it can give (`project.routes`). A form that can be wrong replies with the form again.
- For everything of value, write the rule that must always hold ("coins never go below zero", "an item has one owner") in `project.background` or the data model, and say that each move happens in one transaction.
- Name the settings that differ between a developer's machine and the live site, and the secrets, in `project.deployment`. Never their values.

For the build:

- One project setting file reading everything secret or host-specific from the environment. `DEBUG` off on the live site.
- Run `python manage.py check --deploy` before every launch and clear what it lists.
- Use Postgres from the first day of development, not SQLite, when the site moves anything of value. The code that protects a balance does nothing on SQLite and nobody is told.
- Wrap every move of value in `transaction.atomic()`, lock the rows it reads with `select_for_update()` or change them with `F()`, and give every action that must happen once a unique key.

## Notes

### A form sent without Django's token is refused, and HTMX can carry the token in a header
- Status: approved
- Test: `tests/django/csrf-refuses-post.py` (passed 2026-10-03, Django 6.1.1)
- What happens: a POST with no token got 403. With the token as a hidden form field it got 200. With the token in an `X-CSRFToken` header and no field it also got 200.
- What to do: this is Django's protection against forged requests and it is on by default; leave it on. In a plain form put `{% csrf_token %}` inside it. For HTMX put the token on the body once, `<body hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>`, and every HTMX request carries it.
- For the blueprint: nothing to decide. Say in `project.security` that forged-request protection is the framework's own.

### A form with a mistake comes back with status 200, which is what HTMX shows
- Status: approved
- Test: `tests/django/invalid-form-is-200.py` (passed 2026-10-03, Django 6.1.1)
- What happens: the usual form view, sent a bad email address, replied 200 with the form and the message "Enter a valid email address" in it.
- What to do: with HTMX, keep it that way. HTMX puts a 200 reply on the page and throws an error reply away (see "A reply that says something went wrong is not put on the page" in `htmx.md`), so Django's habit and HTMX's fit without any setting. If the build chooses to reply 422 for mistakes instead, it must also tell HTMX to show 422 replies.
- For the blueprint: each form route's replies are "the next thing, when it is right" and "the form again with messages, when it is wrong".

### One view can serve the whole page to a visitor and only the piece to HTMX
- Status: approved
- Test: `tests/django/hx-request-header.py` (passed 2026-10-03, Django 6.1.1)
- What happens: the same address returned a whole page when asked for plainly and only the list when the request carried the header `HX-Request: true`.
- What to do: check `request.headers.get("HX-Request")` in the view and render the partial template for HTMX, the full page otherwise. The address then works when typed, bookmarked or opened in a new tab, which a route that only ever returns a piece does not.

### A signed-out HTMX request is handed the sign-in page as if it were the piece it asked for
- Status: approved
- Test: `tests/django/login-required-redirects.py` (passed 2026-10-03, Django 6.1.1)
- What happens: `login_required` answered a signed-out request with a 302 redirect to `/accounts/login/?next=/tank/`, the same for an HTMX request as for a plain one. A browser follows a redirect by itself, so HTMX never sees it: it receives the sign-in page and swaps it into the target.
- What to do: for HTMX requests from someone signed out (their session ran out while the page was open), reply 200 with an `HX-Redirect` header naming the sign-in page, which HTMX documents as taking the whole browser there (not tested here). A small piece of middleware can do it for every view.
- For the blueprint: say what a signed-in page does when the visitor's session has ended.

### Without a transaction, a failure halfway through a payment leaves the money gone
- Status: approved
- Test: `tests/django/atomic-rolls-back.py` (passed 2026-10-04, Django 6.1.1 on PostgreSQL 18.4)
- What happens: a payment took 30 coins from one wallet and failed before paying the other. Run plainly, the 30 coins were gone. Run inside `transaction.atomic()`, the first wallet was back at 100.
- What to do: every move of value, with all its parts (take, give, write the ledger line, mark the item's new owner), goes inside one `with transaction.atomic():` block. Django does not do this for a view unless told to.

### Two requests at the same moment lose one change, unless the row is locked
- Status: approved
- Test: `tests/django/lost-update-without-lock.py` (passed 2026-10-04, Django 6.1.1 on PostgreSQL 18.4)
- What happens: two purchases of 10 coins arrived together. Each read the balance as 100, each saved 90. The result was 90: one purchase was free. With `select_for_update()` on the read, the second waited for the first and the result was 80.
- What to do: when a request reads something, decides, and writes it back, read it with `select_for_update()` inside the transaction. This is how items and coins get duplicated on pet sites: not by clever attacks, by pressing a button twice quickly.
- In someone else's code: `obj = Model.objects.get(...)`, some checks, `obj.save()`, with no lock, on anything of value.

### On SQLite the same lock is accepted and does nothing
- Status: approved
- Test: `tests/django/sqlite-ignores-row-locks.py` (passed 2026-10-03, Django 6.1.1)
- What happens: on SQLite, `select_for_update()` raised no error and the query was sent without any lock. The database reports that it does not support row locks.
- What to do: develop and test on Postgres. Code that is safe on Postgres and silently unsafe on SQLite will pass every test run on SQLite.
- For the blueprint: `project.stack` names the database for development as well as for the live site.

### Asking for a lock outside a transaction is an error
- Status: approved
- Test: `tests/django/select-for-update-needs-atomic.py` (passed 2026-10-04, Django 6.1.1 on PostgreSQL 18.4)
- What happens: on Postgres, `select_for_update()` with no transaction raised `TransactionManagementError: select_for_update cannot be used outside of a transaction`. Inside `transaction.atomic()` it read the row.
- What to do: nothing more than the note above asks. Worth knowing because it is the one mistake here that announces itself.

### A change written with F() needs no lock, and a database rule refuses a balance below zero
- Status: approved
- Test: `tests/django/f-expression-and-check.py` (passed 2026-10-04, Django 6.1.1 on PostgreSQL 18.4)
- What happens: two purchases at the same moment, each written as `update(coins=F("coins") - 10)`, left 80 of 100. With a `CheckConstraint` saying coins are zero or more, spending 500 raised `IntegrityError` naming the constraint and the balance stayed at 80.
- What to do: for a plain add or subtract, use `F()`: the database does the sum, so there is nothing to lose. Put every rule that must always hold into the database as a constraint as well as into the code; the constraint is the one that cannot be forgotten by a new view.

### A unique key on each action makes a repeated request count once
- Status: approved
- Test: `tests/django/idempotency-key.py` (passed 2026-10-04, Django 6.1.1 on PostgreSQL 18.4)
- What happens: the same payment notice was delivered three times at the same moment. Each attempt first created a row with the notice's id in a column marked unique, inside the transaction that granted the coins. One attempt granted 50 coins; the other two hit `IntegrityError` and granted nothing.
- What to do: give every action that must happen once an id of its own (made in the browser for a button press, taken from the payment service for a payment) and record it in a unique column in the same transaction as the action. Payment services deliver notices more than once and out of order as a matter of course.
- For the blueprint: for each such action say what the key is and where it comes from.

### Two trades locking the same rows in opposite orders deadlock
- Status: approved
- Test: `tests/django/deadlock-opposite-order.py` (passed 2026-10-04, Django 6.1.1 on PostgreSQL 18.4)
- What happens: Ada paid Bo while Bo paid Ada, each transaction locking the payer's wallet first. One finished and the other was stopped by Postgres with a deadlock error. When each locked both wallets in one query ordered by id, both finished.
- What to do: whenever one transaction locks more than one row, lock them all at the start, in one agreed order (by id). And treat a deadlock error as "try again", not as a failure to show the player.

### Templates escape what a visitor typed unless told it is safe
- Status: approved
- Test: `tests/django/templates-escape.py` (passed 2026-10-03, Django 6.1.1)
- What happens: a pet named `<script>alert(1)</script>` came out of `{{ name }}` with its angle brackets turned into harmless text. Out of `{{ name|safe }}` it came out as a working script tag. `format_html("<b>{}</b>", name)` escaped the name and kept the bold tags.
- What to do: never use `|safe` or `mark_safe` on anything a player typed (names, messages, shop descriptions). Build HTML in Python with `format_html`. This matters twice over with HTMX, which runs scripts in what it swaps in (see `htmx.md`).

### A host name that is not listed is refused once DEBUG is off
- Status: approved
- Test: `tests/django/debug-off-needs-allowed-hosts.py` (passed 2026-10-03, Django 6.1.1)
- What happens: with `DEBUG` off and `ALLOWED_HOSTS = ["kiln.example"]`, a request for `kiln.example` got 200 and one for `kiln-clay.onrender.com` got 400. The refusal comes from middleware every new project has; with that middleware removed, the first version of this test got 200 for both.
- What to do: put every address the site answers at into `ALLOWED_HOSTS`, read from the environment: the custom domain and the host's own address (on Render, the `.onrender.com` name). A site that works on the developer's machine and answers 400 to everything once deployed has this wrong.

### The deploy check finds unsafe settings in a new project
- Status: approved
- Test: `tests/django/check-deploy.py` (passed 2026-10-03, Django 6.1.1)
- What happens: `check --deploy` on settings as `startproject` writes them gave six security warnings, among them: no HSTS (`security.W004`), no redirect to HTTPS (`W008`), a weak secret key (`W009`), the sign-in cookie not marked Secure (`W012`), the CSRF cookie not marked Secure (`W016`), and `DEBUG` on (`W018`).
- What to do: run it before every launch; it is the cheapest security check there is. On the live site set `DEBUG=False`, a long random `SECRET_KEY` from the environment, `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE` and `SECURE_HSTS_SECONDS`. Behind a host's proxy also set `SECURE_PROXY_SSL_HEADER`, or the HTTPS redirect loops (not tested here; see `render.md`).

### Cookies are not marked Secure until the settings say so
- Status: approved
- Test: `tests/django/cookies-not-secure-by-default.py` (passed 2026-10-03, Django 6.1.1)
- What happens: the defaults were `SESSION_COOKIE_SECURE = False`, `CSRF_COOKIE_SECURE = False`, `SESSION_COOKIE_HTTPONLY = True`, `CSRF_COOKIE_HTTPONLY = False`, and `SameSite=Lax` for both.
- What to do: turn both `SECURE` settings on for the live site. Leave `CSRF_COOKIE_HTTPONLY` off only if a script needs to read the token from the cookie; with the token put on the body by the template, as above, nothing does, and it can be turned on.

### create_user stores a hash; create() stores the password itself
- Status: approved
- Test: `tests/django/passwords-hashed.py` (passed 2026-10-03, Django 6.1.1)
- What happens: `User.objects.create_user("ada", password=...)` stored a salted `pbkdf2_sha256` hash 89 characters long, and the real password was accepted at sign-in. `User.objects.create(username="bo", password=...)` stored the password itself, readable in the table, and that account could not sign in.
- What to do: make accounts only with `create_user`, Django's sign-up forms, or `set_password`. In seed data and test accounts too: a script that fills the development database with `create(password=...)` puts readable passwords in it.

### A JSON column holds structured data and can be searched by what is in it
- Status: approved
- Test: `tests/django/jsonfield-query.py` (passed 2026-10-04, Django 6.1.1 on PostgreSQL 18.4)
- What happens: a pet's genome was stored in a `JSONField` as a dictionary with a version number. `filter(genome__glow=True)` and `filter(genome__body__contains="A1")` each found the right pet, and the genome read back as a dictionary.
- What to do: use a JSON column for data whose shape belongs to the game's rules and will change (a genome, a dungeon layout), with a version number inside it. Keep anything of value, and anything used to decide who owns what, in ordinary columns with constraints.

### A timer kept as a timestamp needs nothing running on the server
- Status: approved
- Test: `tests/django/timers-from-timestamps.py` (passed 2026-10-03, Django 6.1.1)
- What happens: an egg stored only the moment it was laid. Its state ("incubating", then "hatched") was worked out from that moment and the present whenever someone looked, and one query found every egg due by a given time. `timezone.now()` carries its time zone.
- What to do: store when things started, not how long is left, and work out the rest on reading. Nothing has to tick. A scheduled job is then only needed for things that must happen with nobody looking (a daily reset that other players can see).
- For the blueprint: this is a `project.background` entry: what runs by itself, on what clock, and what must hold.

### Serving the site's own files in production
- Status: draft
- Test: none. Needs a real deployment.
- What happens: Django's development server serves CSS, scripts and images by itself. With `DEBUG` off it does not, by design.
- What would confirm it: a deployed site whose styles load. The usual answer is the WhiteNoise package plus `collectstatic` in the build step.
- Seen once, at home and not on a host: the Meridian build (2026-10-04) ran with `DEBUG` off behind the waitress server, with WhiteNoise's middleware and `collectstatic` run at each start; its styles, scripts and fonts loaded.
- Until then: plan for it in `project.deployment`; a deployed Django site with no styling has this wrong.

### A Postgres that comes with the project, for a site run at home
- Status: draft
- Test: none. Seen on one build (the Meridian ant colony, 2026-10-04, Django 6.1.1, `pixeltable-pgserver` 0.6.0 carrying PostgreSQL 18.4, on Linux).
- What happens: the `pixeltable-pgserver` package installs a whole Postgres with `pip` and starts it from Python (`get_server(folder, cleanup_mode="stop")`), so a site that runs on somebody's own computer needs no database installed and no administrator rights. It is the package these tests use. The older `pgserver` package it grew out of has no build for Python 3.13 on Windows.
- The trap: it would not start when the folder for its data had a space anywhere in its path (`postgres: invalid argument`), because the path is handed to Postgres unquoted. Project folders often have spaces; a temporary folder does not, which is why a test suite never meets this.
- What to do: keep the database's folder in the usual place for a program's own data (`%LOCALAPPDATA%` on Windows, `~/.local/share` on Linux), not beside the code, and stop with a plain message if that path has a space. This also means moving or replacing the code folder does not lose the data.
- What would confirm it: the same build started on Windows.
- Not for a public site: on a host such as Render, use the host's own Postgres.

## What the skill cannot check

- Anything about a real Django project. The skill's `check` and `audit` look at mockups and at built pages, not at Python code.
- Whether every move of value in a codebase is inside a transaction with the right locks. That needs reading the code, and a test like the ones here for each kind of move.
- Load. These tests show what happens with two or three requests at once, not two hundred.

## Questions it raises

- What on this site has value, and which rule about it must never be broken?
- Which actions must happen exactly once, and what identifies each one?
- What does a signed-in page do when the visitor's session has ended?
- Which database is used during development?
- Which settings and secrets differ between a developer's machine and the live site?
