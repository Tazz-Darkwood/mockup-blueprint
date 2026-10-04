---
name: HTMX
summary: Library that lets ordinary HTML fetch pieces of a page from a server and swap them in, using hx- attributes instead of written JavaScript. Read when a mockup or build uses hx- attributes. Setup, how to stand in for the server in a mockup, and what catches people out.
detect: ["hx-get", "hx-post", "hx-put", "hx-delete", "hx-target", "htmx.org"]
version: 2.0.11
checked: 2026-10-03
source: https://htmx.org/docs/ and https://htmx.org/reference/
---

# HTMX

With HTMX an element says, in attributes, what to ask the server for and where to put the reply: `<button hx-post="/basket" hx-target="#msg">`. The server answers with a piece of HTML, not data. It suits sites built with a server framework such as Django, where the server already makes HTML.

That is also its difficulty for a mockup: **there is no server**. Every `hx-` attribute in a mockup is a promise that some address will answer with some HTML, and none of those answers can be seen in the mockup's files unless they are written down. So for HTMX the blueprint matters more than usual: each route is something to build.

## Use it properly

In the `<head>`, pinned to a version:

```html
<script src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.11/dist/htmx.min.js"></script>
```

In a mockup, a pretend server straight after it. Copy `htmx-mock.js` from this skill's `assets/` folder beside the page:

```html
<script src="htmx-mock.js"></script>
<script>
  htmxMock({
    'GET /search': (asked) => '<li>Results for ' + htmxMock.escape(asked.params.q) + '</li>',
    'POST /items': (asked) => asked.params.name
        ? '<li>' + htmxMock.escape(asked.params.name) + '</li>'
        : { status: 422, body: '<p class="error">Give it a name.</p>' },
  }, { delay: 300 });   // a little delay, so waiting states can be seen
</script>
```

Rules that save time, each explained in the notes below:

- Whatever a visitor typed goes through `htmxMock.escape()` before it is put into a reply, as in the example. The real server must do the same.
- Every route in the pretend server goes into the blueprint: its address, what it is sent, and each reply it can give. They are the server's to-do list.
- Decide what happens to error replies. As made, HTMX throws them away.
- Give any field that may be replaced while someone is typing in it an `id`.
- Buttons that buy, send or delete get `hx-disabled-elt="this"`.
- Scripts must wait for the page to finish loading before triggering anything.

## Notes

### One script tag is enough, and an element fetches into itself by default
- Status: approved
- Test: `tests/htmx/setup-loads.html` (passed 2026-10-03, version 2.0.11)
- What happens: with the one script tag, a button carrying only `hx-get` fetched when pressed and put the reply inside itself, replacing its own label.
- What to do: nearly always add `hx-target` to say where the reply goes, and `hx-swap` if it should replace the target or be added to it instead of filling it.
- In someone else's mockup: a button whose label turns into a chunk of page when pressed has no `hx-target`.

### Opened from a folder, HTMX cannot fetch a file beside the page
- Status: approved
- Test: `tests/htmx/from-a-folder.html` (passed 2026-10-03, version 2.0.11)
- What happens: `hx-get="piece.htm"` on a page opened straight from a folder fetched nothing. The target was unchanged and HTMX fired `htmx:sendError`. The browser refuses the request.
- What to do: do not build an HTMX mockup out of little files of HTML. Use the pretend server.
- In someone else's mockup: one that "works on my machine" was being run through a local server. Either run one too, or move its pieces into a pretend server.

### The pretend server answers gets and posts, with what was sent
- Status: approved
- Test: `tests/htmx/pretend-server.html` (passed 2026-10-03, version 2.0.11)
- What happens: with `htmx-mock.js` loaded, a get that included a field's value and a posted form were both answered by functions in the page, and the replies were swapped in as HTMX would swap a real server's. The request arrived carrying the header `HX-Request: true`, as real ones do.
- What to do: write one function per route. Give it a delay of a few tenths of a second so the waiting states can be seen. A request that no route matches gets a 404 saying so.
- Careful: the pretend server replaces the browser's way of making requests for the whole page. Do not use it alongside other code that fetches things.

### A reply that says something went wrong is not put on the page
- Status: approved
- Test: `tests/htmx/errors-not-shown.html` (passed 2026-10-03, version 2.0.11)
- What happens: the server replied 422 with a message for the visitor. HTMX left the page exactly as it was and fired `htmx:responseError`. After adding `{ code: '422', swap: true }` to `htmx.config.responseHandling`, the same reply was shown.
- What to do: decide, and write in the blueprint, how the server reports a problem with what was sent. Either it replies 200 with the form and its messages, or it replies 422 and the page sets `responseHandling` to show it. A server framework's form handling usually replies 200; an API-minded one replies 422. Mixing the two gives forms that fail in silence.
- In someone else's mockup: a form that does nothing when submitted wrongly.

### Typing is interrupted when a field is replaced, unless the field has an id
- Status: approved
- Test: `tests/htmx/focus-after-swap.html` (passed 2026-10-03, version 2.0.11)
- What happens: a field that had focus was replaced by the server's reply. Without an `id` the focus was lost to the page. With an `id` that the new field shared, focus and the position of the caret were kept.
- What to do: give every field inside something that gets swapped an `id`, and keep it the same in the reply. Better still, do not swap a field while it is being typed in: aim the reply at the results, not the form.
- In someone else's mockup: a search box that drops the cursor after every result.
- Careful with Web Awesome: this does not hold for `<wa-input>`. See the next note.

### A Web Awesome field loses the focus when replaced, id or no id
- Status: approved
- Test: `tests/htmx/wa-input-focus.html` (passed 2026-10-03, HTMX 2.0.11 with Web Awesome 3.14.0)
- What happens: a focused `<wa-input>` with an `id` was replaced by one with the same id. The swap happened, but focus was lost; a plain `<input>` in the same test kept it. With no id the swap also happened and focus was lost.
- What to do: do not swap a Web Awesome field while it is being used. Aim the reply at a message beside the field, or at the results. If the whole form must come back, put the focus where it belongs from script after the swap (`htmx:afterSwap`).
- Reported but not reproduced here: in the cold test of 2026-10-03, a form reply that replaced a focused `<wa-input>` carrying an id stopped with `htmx:swapError`. This test saw no error. Django gives every form field an id, so if a swapped Web Awesome form misbehaves, try removing the ids first.

### The pretend server matches addresses with changing parts
- Status: approved
- Test: `tests/htmx/changing-addresses.html` (passed 2026-10-03, version 2.0.11)
- What happens: a route written as `'POST /sessions/:id/signup/'` answered a request to `/sessions/7/signup/` and was given `7` as `params.id`. A relative address with a query was matched by its path.
- What to do: write one route per kind of address, as the real server will, not one per item.

### A script inside a reply is run
- Status: approved
- Test: `tests/htmx/scripts-run.html` (passed 2026-10-03, version 2.0.11)
- What happens: a reply containing a `<script>` tag had its script run when swapped in. With `htmx.config.allowScriptTags = false` it did not.
- What to do: this is a security matter. Anything the server puts into a reply that came from a visitor (a name, a comment) must be escaped, or it can run as script in other visitors' browsers. Say so in the blueprint's security section. If the site never needs scripts in replies, switch them off.

### Listeners on replaced content are gone; htmx.onLoad sets up what arrives
- Status: approved
- Test: `tests/htmx/new-content-setup.html` (passed 2026-10-03, version 2.0.11)
- What happens: a click listener added to a button stopped working once the button was replaced by a reply. A listener added through `htmx.onLoad` worked on the new button, and so did one listening on the body for clicks on that kind of button. `htmx.onLoad` was handed the new button itself, not something containing it.
- What to do: set things up inside `htmx.onLoad`, and check both the element handed over and what is inside it: `(el.matches(sel) ? [el] : el.querySelectorAll(sel))`. Or listen once, higher up the page.
- In someone else's mockup: things that work until the first time part of the page refreshes.

### A search box asks once after a pause, not on every key
- Status: approved
- Test: `tests/htmx/typing-delay.html` (passed 2026-10-03, version 2.0.11)
- What happens: four letters typed into a field with `hx-trigger="keyup"` sent three requests. With `hx-trigger="keyup changed delay:300ms"` they sent one, asking for the whole word.
- What to do: use `keyup changed delay:300ms` (or `input changed delay:300ms`) on anything that searches as you type.

### Two quick presses send two requests unless the button is switched off meanwhile
- Status: approved
- Test: `tests/htmx/double-press.html` (passed 2026-10-03, version 2.0.11)
- What happens: pressing a button twice while the server took 0.3 seconds sent two requests. With `hx-disabled-elt="this"` it sent one: the button was disabled while waiting and enabled again afterwards.
- What to do: put `hx-disabled-elt="this"` on any button that buys, sends, saves or deletes. The server must still cope with a repeat, because not every repeat comes from a double press.

### The class htmx-request is on the element while it waits
- Status: approved
- Test: `tests/htmx/waiting-sign.html` (passed 2026-10-03, version 2.0.11)
- What happens: while a request was in flight the element that made it had the class `htmx-request`, and a spinner styled to show under that class was visible. Afterwards the class was gone.
- What to do: style the waiting state from `.htmx-request`. Give the pretend server a delay or the state will never be seen in the mockup.

### One reply can update a second place on the page
- Status: approved
- Test: `tests/htmx/second-place.html` (passed 2026-10-03, version 2.0.11)
- What happens: a reply contained a message and, beside it, a `<span id="count" hx-swap-oob="true">`. The message went to the target; the span replaced the element with that id elsewhere on the page.
- What to do: use it for things like a basket count in the header. In the blueprint, say which routes update which other places, since it cannot be seen from the element that was pressed.

### HTMX attributes work on Web Awesome buttons and fields
- Status: approved
- Test: `tests/htmx/with-web-awesome.html` (passed 2026-10-03, HTMX 2.0.11 with Web Awesome 3.14.0)
- What happens: a `<wa-button hx-get>` fetched when pressed. A form posted with `hx-post` included the value of a `<wa-input>` inside it. A `<wa-input>` carrying `hx-get` itself sent its own name and value.
- What to do: the two can be used together as they are.

### Announcing a swap to screen readers
- Status: draft
- Source: none; not tested. HTMX does not announce what it swaps in.
- What would confirm it: a test that reads what a screen reader is given after a swap into a region with and without `aria-live`.
- Until then: make the target of anything a visitor needs to hear about (a message, an error, a count of results) a live region.

## What the skill cannot check

- Whether the pretend server's replies match what the real server will send. The blueprint is the only link between them.
- Anything about the real server: speed, sign-in, protection against forged requests.

## Questions it raises

- For each hx- attribute: what address, what is sent, and what does each possible reply contain?
- How does the server report a mistake in what was sent: a normal reply with messages, or an error code?
- Which replies also update another part of the page?
- Does any reply include something a visitor typed?
