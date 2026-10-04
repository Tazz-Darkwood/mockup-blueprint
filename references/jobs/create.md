# Create a new mockup with context

The job when the user wants a new mockup. Read `SKILL.md` first.

**What to read, and when.** There is a lot, and not all of it is needed before the first line is drawn.

| Before | Read |
|---|---|
| the brief (step 4) | `library/style-guide.md`: how the stack works, "Write a design brief", "Decide where the detail goes", "It must not look like a template". Then the feel guide chosen, all of it. |
| writing HTML (step 5) | `library/style-mobile.md` from "Use it properly" to the end of "Before showing a mockup". "Use it properly" and the note titles of each tool's entry, `library/web-platform.md` and `library/css-layout.md`; open a note when its title matches what you are about to write. |
| writing the context (step 9) | `references/context-format.md`, then `references/gap-checklist.md`. |

The rest of the general style guide's notes are a reference for the "Before showing a mockup" list in step 6: read them there.

1. **Get the intent first.** Before drawing anything, find out: what it is for, who uses it, the handful of things they must be able to do, what data is involved, whether there are existing brand colours or references, and which tools it should be built with. Ask; do not invent a product.

2. **Read what applies.** The library entry for each tool named; `library/web-platform.md` and `library/css-layout.md`; `library/style-mobile.md`; and `library/style-guide.md`, which explains the style stack: the general guide, the purpose, feel and field guides a site stacks on it, and the site's own guide. If a tool the user named has no library entry, say so: its behaviour is unverified, so try what matters with `try` as you go, and propose notes for what surprises you.

3. **Choose the style guides with the user.** Run `style` to list the guides there are, the skill's and the ones the user has made.
   - Guides are there to be mixed. A site may take several, two of the same kind included (warm with artistic, say), and an unusual mix is how a site ends up looking like nothing else. Name the lead first, and say in the brief which parts of the site each one governs.
   - If no feel guide fits the site, stop and ask. Do not quietly take the nearest one and do not go without, because a page with no feel guide comes out plain and nobody chose that. Offer the two ways on, as `references/jobs/style-guide.md` describes: make a guide for this kind of site now, or use the nearest and say what it lacks.
   - Read the guides chosen and record the choice in the blueprint as `project.style` (`{"guides": ["artistic", "sales"], "site_guide": "name.style.md"}`: the short names of the stacked guides only; the general and phone guides always apply and are not listed).

4. **Write the design brief and show it before drawing.** It is the eight lines the general style guide asks for. Agreeing it first is far cheaper than redrawing a mockup whose tone was wrong. The brief is the first section of the site's own guide, `<name>.style.md`, kept beside the mockup; `references/site-guide.md` lists that file's sections. Start the file now and fill the rest in as the page is drawn.

5. **Build the mockup with anchors from the start, phone first.** Run `init` as soon as the first page exists, so `audit`, `check` and `try` work from then on; the context file starts empty and is filled in at step 9.
   - Choose this site's typefaces and colours for its own subject. Do not copy the fonts or tokens of another mockup that happens to be in the next folder.
   - Set the style guide's tokens first (type scale, spacing scale, colours, radius) and use only those.
   - Lay the page out at phone width before anything else: one column, in the order a visitor needs things, with the first screen decided on purpose, as `library/style-mobile.md` describes. Widen it afterwards and add columns only where the content gains from them. A page drawn wide and squeezed later puts the wrong things first on a phone, and most visitors to most sites are on one.
   - Put `data-bp-screen` and `data-bp` on elements as you write them.
   - Make it accessible by construction: real `<button>`, `<a>`, `<label>` and heading elements, a `lang` attribute, a title, alt text, visible focus, text contrast of at least 4.5:1. It is far cheaper than retrofitting.

6. **Before the user sees anything**, run the "Before showing a mockup" lists in both guides, and `audit`. The last item on the general list is the template test: count the template tells and name three things on the page that were made for this site alone. It is the one check no script can do for you and the one users notice first, so do not skip it because everything else passed.

7. **Click through it as each kind of user.** Before writing any context, open the mockup and use it as a visitor, as a signed-in member, and as any other role, at desktop and phone width. The audit checks the markup; only using the page shows that something a role should see is missing or that a button leads nowhere. `try page.html "click #x" "fill #y=text"` carries out a few presses and reports errors, messages and where the focus went.

8. **Show the states that matter.** Where it is cheap, mock the empty, loading and error states too, or describe them in the element's `states`. The check only sees a page as it loads, so list the presses that reach each other state (a form that opens, a message after sending, a full list) in `project.check_states`; the check then looks at those as well.

9. **Write the context**, the same way as steps 4 to 9 of `references/jobs/annotate.md`.
   - For a mockup of several pages, pass every page to one `init` command so they share one context file (run it again when a page is added), and give the shared parts (header, footer) the same `data-bp` id on every page so they are described once.
   - If the pages share anything that changes (who is signed in, a basket, a game), the browser's storage alone will not carry it from page to page: opened from a folder, some browsers keep separate storage for every file, so one page cannot read what another saved and the mockup seems to forget things. Copy `assets/carry-storage.js` beside the pages and load it first on every one; the pages then use `localStorage` as usual. Where a script sends the visitor to another page, use `carryStorage.go('page.html')`, not `location.href`. `audit` and `check` try this for every mockup of more than one page and report `mockup/storage-not-shared` or `mockup/script-leaves-storage`.
   - If the mockup needs a control that only exists to show different states, such as a "view as visitor or member" switch, mark it `mock_only`.
   - Everything the user told you is confirmed. Everything you chose to make the mockup look complete (sample names, numbers, extra menu items) is inferred or `mock_only`. Say which is which, because invented filler is the most common thing to get built by accident.
