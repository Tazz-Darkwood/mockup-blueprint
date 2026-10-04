# The library

Notes about the tools mockups are built with: what each one needs, the odd things it does, and how to spot and fix its usual flaws in a mockup someone else made. One file per tool.

The point of the library is that its notes can be trusted. A note that is wrong is worse than no note, because it gets applied to every mockup after it. So every note has a status, and the only way to become approved is to pass a test.

## How a note gets in

1. **Claude proposes.** When a session hits something surprising about a tool (it cost time, it broke a mockup, the documentation did not say), Claude describes the note in plain words and says how it would be tested. Claude does not add notes on its own.
2. **The person agrees**, or says no, or changes it.
3. **It is written and tested.** The note goes into the tool's file as `draft`, with a small test page under `tests/<tool>/` that demonstrates the behaviour.
4. **Passing the test is the approval.** Run `blueprint.py library --test <tool>`. When the note's test passes, change its status to `approved`. If it fails, the note was wrong: correct it or delete it. Do not keep a note whose test disproved it.

A note that cannot be tested with a page in a browser (it needs a real deployment, an account, a payment) stays `draft` and says what would confirm it. When that thing actually happens in a real project, record what was seen and the date, and it can be approved by the person.

Rules about how something should look are a second case that no test page can settle. Those live in the style guides and are approved by critique. The style guides are a stack: `style-guide.md` (general) with `style-mobile.md` (phones) beside it, then `style-purpose-<name>.md`, `style-feel-<name>.md` and `style-field-<name>.md` guides chosen per site, then the site's own `<name>.style.md` in its folder; `style-guide.md` explains the order. A stacked guide records which parts of a page need detailed styling and how much, with evidence from real sites, and leaves the specifics to each site. A new stacked guide starts from research: open a set of well-regarded sites of that kind, record for each part of the page how much detail it got, and keep what most of them share. `references/jobs/style-guide.md` in the skill folder is that method as a job, with `blueprint.py study` to photograph and measure the sites; guides a user makes that way live in their own folder outside the skill, not here. For the general guide and the stacked guides, approval works like this: the rule is applied in a real mockup, the person looks at the result, and if they agree the note gets `- Status: approved` and a line `- Approved by: <name>, <date>, on <which mockup>`. If they disagree, the rule is rewritten to say what they wanted and stays draft until the next mockup shows it working.

## How to use the notes

- **approved**: rely on it.
- **draft**: a lead, not a fact. Check it before relying on it, and tell the user it is unconfirmed.

Run `blueprint.py library <mockup>` to see which entries a mockup needs, and read only those. `check` lists them too.

Tools change. Each entry records the version its tests last passed against. When a tool releases a new version, run `blueprint.py library --test <tool> --as-version X.Y.Z`: any approved note whose test now fails is reported, and goes back to draft until it is re-checked.

## File format

`library/<tool>.md`:

```markdown
---
name: Tool Name
summary: One line: what it is and when the entry matters.
detect: ["<wa-", "webawesome"]
version: 3.14.0
checked: 2026-10-03
source: https://example.com/docs
---

# Tool Name

What it is and when we use it, in a few sentences.

## Use it properly

The starting point for a new mockup: the tags or setup that are known to work.

## Notes

### Short title that states the behaviour
- Status: approved
- Test: `tests/tool-name/short-title.html` (passed 2026-10-03, version 3.14.0)
- What happens: ...
- What to do: ...
- In someone else's mockup: how to spot it, and the fix.

## Questions it raises

Decisions this tool forces, worded the way they would be asked in a blueprint.
```

Rules the script depends on:

- `detect` is a JSON list of patterns on one line, matched against the mockup's source and its context file, ignoring case.
  Keep each pattern specific to the tool (a tag prefix, a package name, a host). A pattern shorter than three characters, or one that matches anything, is ignored, and so is one that is not a valid pattern.
- `always: creating` marks an entry that is advice for making any page (the browser's own building blocks, CSS layout), not notes on one tool. It is listed for the Create and Restyle jobs and left out when annotating someone else's mockup.
- Each note is a `### ` heading. Use `### ` for nothing else.
- `- Status:` is `approved` or `draft`.
- `- Test:` names the test page in backticks, relative to the library folder. A draft that cannot be tested in a browser says `- Test: none` and why.
- Anything outside a note that is not backed by a test should say where it came from (the tool's documentation, with the date read).

## A person's own notes

The entries in this folder come with the skill and are replaced when the skill is updated. Notes a user adds for a tool the skill does not cover go in their own folder for the skill, outside it: `library/<tool>.md` under the folder `blueprint.py doctor` prints, with test pages in `library/tests/<tool>/` beside it. Same file format, same rule that a test approves a note. `library`, `check` and `library --test` pick them up with the built-in ones, and the runner keeps a copy of `harness.js` in that `tests` folder.

An entry of the user's own can add a tool. It cannot take the name of an entry that comes with the skill. Sending the folder to whoever looks after the skill is how a note becomes part of it.

## Test pages

A test page is a small, complete HTML file that loads the real tool and checks one behaviour. It includes `../harness.js` and calls `run(async () => ({ pass, detail }))`:

- `pass` is true when the behaviour the note describes was observed. A note about a flaw passes when the flaw shows up.
- `detail` says in words what was seen, including the actual values. It is printed by the runner and shown on the page, so a person can open the file in a browser and read PASS or FAIL.

Keep one behaviour per page so a failure points at one note. Tests need an internet connection when the tool loads from a CDN.

Events faked by script do not behave like a person's: in testing, a select option clicked from script did not select, though a real click did. When a behaviour depends on a person, ask the runner for real input from inside the test:

- `await real('click', '#save')`, `await real('hover', '#help')`, `await real('mouse', '5,5')` (a click at that point on the page)
- `await real('type', 'hello')`, `await real('press', 'Enter')`
- `await real('drag', '10,10,90,40')` presses at the first point, moves to the second and lets go. `await real('wheel', '50,50,300')` turns the mouse wheel with the pointer at that point. `await real('swipe', '50,50,-200')` is a finger put down there and moved 200 pixels up.
- `await real('motion', 'reduce')` makes the browser report that the visitor asked for less motion; `'no-preference'` undoes it.
- `await real('aria', '#field')` returns how that element is announced to assistive technology, as text such as `- textbox "Email"`. Use it for every accessibility claim instead of reading attributes.

A page that uses `real()` only passes under the runner; opened by hand it says so.

Explore before asserting. Write a scratch page that prints what the tool does, read the output, and only then write the test and the note. Expect to be wrong: among the first behaviours written down for Web Awesome, one was disproved by its own test, and another test turned out to be measuring the wrong thing.
