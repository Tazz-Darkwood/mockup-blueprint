# Problems met while using this skill: the maintainer's history

Reports from before version 0.9.0, all dealt with. New reports are no longer written here: they go to each person's own folder for the skill (`blueprint.py doctor` prints where), so they survive updates and can be sent in.

Added by `blueprint.py feedback`, newest last. See "When the skill itself gets in the way" in SKILL.md.
An entry is a report, not a fix. Mark it `- Status: fixed` with what was changed once it has been dealt with.

## 1. The problem log cannot be used when the user says to change only one folder
- Status: fixed
- Done (2026-10-03): `feedback --beside <folder>` keeps the log beside the mockup; SKILL.md says the log is the one file outside the user's folder that may be written, and what to do when it cannot be.
- Kind: instructions
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

The problem log cannot be used when the user says to change only one folder

All three helpers were told to change files only inside their own folder. The log lives in the skill's folder, so none of them logged anything and all three reported their problems in their final message instead. The skill does not say which instruction wins. Reported by: all three.

## 2. Annotate: how much may be changed in someone else's mockup is contradictory, and nothing s
- Status: fixed
- Done (2026-10-03): SKILL.md now has one list of what may be changed in someone else's mockup, says to copy the originals into `original/` first, to leave a found secret in place and report it, and to list changes in `project.changes`.
- Kind: instructions
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Annotate: how much may be changed in someone else's mockup is contradictory, and nothing says to keep the original

Step 3 says adding attributes is the only change. Step 7 says fix what can be fixed without changing the look. The audit says to remove a secret. carry-storage needs a script tag and a changed redirect. The helper removed a key line, rewrote a redirect, added a keyboard handler and removed the zoom lock, and kept no copy of the original. Reported by: annotate helper (bike shop).

## 3. Create: says to ask the user and agree the brief, but not what to do when nobody is there
- Status: fixed
- Done (2026-10-03): SKILL.md has a rule for every job when nobody is there to ask: take the suggested default, mark it inferred, write the question.
- Kind: instructions
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Create: says to ask the user and agree the brief, but not what to do when nobody is there

Annotate step 6 covers an absent user; Create does not. The helper wrote the brief as a proposal and added a question asking whether it was right. Reported by: create helper (workshop).

## 4. carry-storage is described only under Create
- Status: fixed
- Done (2026-10-03): carry-storage is in the Annotate list of allowed changes.
- Kind: instructions
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

carry-storage is described only under Create

The Annotate section does not say whether to add it to a mockup someone sent. Reported by: annotate helper (bike shop).

## 5. Merge: several kinds of answer are not covered
- Status: fixed
- Done (2026-10-03): Merge section covers answers that do not fit (`heard`), answers from someone else (`answered_by`), questions made pointless (`closed`), comments on the look, the site style guide, and searching for everything an answer touches. Still not defined: exactly when a mockup counts as 'what ships'.
- Kind: instructions
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Merge: several kinds of answer are not covered

(a) An answer that does not fit its question ('continue' to 'who will photograph the soaps?'). (b) A question addressed to one person and answered by another. (c) A comment on how something looks: the library section says fix the mockup, the merge section says choose between a context change, a question or a comment to pass on. (d) The site's own style guide is not mentioned, though answers change what it says. (e) 'The mockup is itself what ships' and 'changes what the page does' are not defined. (f) One answer can touch ten places and nothing helps find them. Reported by: merge helper (Greenfire copy).

## 6. Small errors in SKILL.md
- Status: fixed
- Done (2026-10-03): Wording corrected; the project.style example says which names to list.
- Kind: instructions
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Small errors in SKILL.md

'Three kinds of file' sits above a table of five. The project.style example does not say whether guide names are short names or file names, or whether the general guides are listed. Reported by: annotate helper (bike shop), create helper (workshop).

## 7. Too much to read before starting
- Status: fixed
- Done (2026-10-03): The library section says what to read for each job, and to read note titles first.
- Kind: library
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Too much to read before starting

The annotate job was pointed at about 740 lines of library, including style guides it may not act on in someone else's mockup. The create job read about 2,000 lines before drawing. `library <mockup>` cannot run before the mockup exists, so entries were chosen from the file list. Reported by: annotate helper (bike shop), create helper (workshop).

## 8. A question cannot be closed as no longer needed, and an answer is all or nothing
- Status: fixed
- Done (2026-10-03): Questions may carry `closed`, `heard`, `answered_by` and `answered_on`; the check and viewer honour them.
- Kind: format
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

A question cannot be closed as no longer needed, and an answer is all or nothing

Choosing a shop service made 'which payment service?' moot; the helper wrote a pretend answer, which the check counts as answered. A question that asked two things and got one settled had to be answered and a new question added. There is no field for who answered or when. Reported by: merge helper (Greenfire copy).

## 9. One status for a whole section or element
- Status: fixed
- Done (2026-10-03): Any section or element may carry `decided`: the statements a person settled, while the item stays inferred.
- Kind: format
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

One status for a whole section or element

A section that is partly the user's decision and partly worked out has nowhere to say so. Helpers invented keys (decided_by_owner, answered_by) or left the whole thing inferred. Reported by: all three.

## 10. No place for routes, emails, or changes made to the mockup
- Status: fixed
- Done (2026-10-03): `project.routes` and `project.changes` are in the format; the check warns about hx- addresses no route describes. Emails belong in `project.background`.
- Kind: format
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

No place for routes, emails, or changes made to the mockup

SKILL.md and htmx.md say every pretend-server route must be in the blueprint, but the format has nowhere for routes; the helper invented project.routes and project.emails. Another invented project.changes_made_to_the_mockup. Reported by: create helper (workshop), annotate helper (bike shop).

## 11. An open section blocks the build whatever its question says
- Status: fixed
- Done (2026-10-03): A question about an open item now holds up whatever its own `blocks` says; documented.
- Kind: check
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

An open section blocks the build whatever its question says

A question about an open section blocks the build even when marked blocks: launch. This is not in context-format.md and clashes with the instruction that the host question blocks launch. Both helpers marked deployment as inferred to get round it. Reported by: annotate helper (bike shop), create helper (workshop).

## 12. The separate-storage check misses state saved on submit
- Status: fixed
- Done (2026-10-03): The storage check also reads the keys named in each page's code, so state saved on submit is seen. Confirmed on the bike shop with the helper removed.
- Kind: check
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

The separate-storage check misses state saved on submit

The bike shop saves bookings only when the form is sent and moves on with location.href; the staff page reads them on load. The check looks for a key both pages read as they load, so neither warning fired. The helper added carry-storage from the instructions anyway. Reported by: annotate helper (bike shop).

## 13. A stranger's desktop-only mockup can never pass
- Status: fixed
- Done (2026-10-03): Decided by the skill's owner: desktop only is acceptable. `project.phone` = "not designed" stops phone findings blocking the build and holds up the launch until decided; "desktop only" records the decision.
- Kind: check
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

A stranger's desktop-only mockup can never pass

mobile/sideways-scroll and mobile/tap-size stop the build; step 7 says a phone problem in someone else's mockup is the designer's decision; waiving to pass is forbidden. So it stays NOT READY until redrawn, and the skill does not say whether that is intended. Reported by: annotate helper (bike shop).

## 14. html/never-loaded appears and disappears
- Status: fixed
- Done (2026-10-03): The check waits and looks once more before reporting a tag that never loaded, and the message says to run again.
- Kind: check
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

html/never-loaded appears and disappears

One run reported three errors for wa-button, wa-input and wa-toast; two more runs on the same files reported none. Probably a slow CDN. The check does not retry or say that a load failed. Reported by: merge helper (Greenfire copy).

## 15. Library entries are matched by a word anywhere in the blueprint
- Status: fixed
- Done (2026-10-03): Sentences that rule a tool out are skipped when matching library entries.
- Kind: check
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Library entries are matched by a word anywhere in the blueprint

'uses Render' and 'uses GitHub Pages' appeared because the text mentioned them only to rule them out. Reported by: all three.

## 16. Two-questions warning fires on a quoted question mark
- Status: fixed
- Done (2026-10-03): Quoted text is ignored when looking for two questions in one.
- Kind: check
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Two-questions warning fires on a quoted question mark

"Should Delete ask 'Are you sure?' before removing a booking?" was flagged. Reported by: annotate helper (bike shop), merge helper (Greenfire copy).

## 17. Placeholder count is off
- Status: fixed
- Done (2026-10-03): Placeholders that only appear once the page's script has run are now counted, by reading the page's text in the browser.
- Done (2026-10-03): Partly fixed: dummy phone numbers in visible text are found and filler text is counted once. Placeholders held in a pretend server's data are still not seen.
- Kind: check
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Placeholder count is off

It missed the dummy phone number 555-0100 in visible text (that pattern only runs on links), counted one Lorem ipsum paragraph twice, and cannot see placeholders held in a pretend server's data. Reported by: annotate helper (bike shop), create helper (workshop).

## 18. Audit missed an insecure link and gives no guidance on a found secret
- Status: fixed
- Done (2026-10-03): http:// links are reported as `sec/insecure-link`; SKILL.md says how to handle a found secret.
- Kind: check
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Audit missed an insecure link and gives no guidance on a found secret

The http:// Facebook link was not flagged though the skill says insecure links are caught. The secret finding does not say what to do with an obviously dummy key in someone else's mockup, or how to refer to it without repeating it. Reported by: annotate helper (bike shop).

## 19. audit, inventory and check treat a path differently, and check cuts its list at 40
- Status: fixed
- Done (2026-10-03): audit says when it looked at one page of a blueprint that covers several; long lists are no longer cut at 40.
- Kind: script
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

audit, inventory and check treat a path differently, and check cuts its list at 40

audit on one page audits only that page; inventory and check given the same path cover every page. check truncates errors at 40 with no way to see the rest. Reported by: annotate helper (bike shop).

## 20. Only the page as loaded is checked
- Status: fixed
- Done (2026-10-03): `project.check_states` lists the presses that reach other states of a page; the check repeats contrast, placeholders and the phone measurements in each. The first-screen measurement is skipped there.
- Kind: check
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Only the page as loaded is checked

Anything swapped in by HTMX, and any form or dialog that opens on a press, is invisible to the scan and to the phone and contrast pass. The create helper put replies in template elements so the scan could see them and wrote a helper that re-runs the phone and contrast measurements after clicking. Run on a scrolled page, mobile/first-screen gives a false alarm. Reported by: create helper (workshop).

## 21. htmx-mock matches exact addresses only
- Status: fixed
- Done (2026-10-03): htmx-mock matches addresses with changing parts and gives the address as written; the check compares hx- addresses with project.routes.
- Kind: script
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

htmx-mock matches exact addresses only

No patterns such as /workshops/<id>/signup/, so routes were registered per session in a loop. asked.path keeps only the last segment (just '/' with a trailing slash). Nothing in blueprint.py knows about hx- attributes, so it cannot tell whether routes are described. Reported by: create helper (workshop).

## 22. htmx.md's advice to give swapped fields an id breaks with wa-input
- Status: fixed
- Done (2026-10-03): Tested: a focused wa-input with an id is swapped but loses focus; a plain input keeps it. htmx.md corrected. The reported htmx:swapError was not reproduced and is recorded in the note as reported only.
- Kind: library
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

htmx.md's advice to give swapped fields an id breaks with wa-input

With HTMX 2.0.11 and Web Awesome 3.14.0: when the focused wa-input has an id and the reply holds one with the same id, HTMX calls focus() on the new wa-input before it is ready; it throws, the swap stops (htmx:swapError) and focus is lost. Seen by pressing Enter in the email field with a mistake in it. The helper removed the ids and set focus from script. NOT YET CONFIRMED by a test page here. Django gives form fields ids by default, so this matters. Reported by: create helper (workshop).

## 23. Small gaps in the library notes
- Status: fixed
- Done (2026-10-03): web-awesome.md notes wa-cloak and leaking theme defaults (untested); the general guide explains that 66ch is not 66 characters.
- Kind: library
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Small gaps in the library notes

web-awesome.md says to add wa-cloak but not whether the audit, which waits 0.4s, still sees the page (it does; the helper tested). Only six Web Awesome theme variables have tests; about forty were mapped by eye and one default leaked. The general guide's 66ch measure gave 78-character lines in IBM Plex Sans; ch is not a character count. Reported by: create helper (workshop).

## 24. Typed non-answers are pasted again, and two layout faults
- Status: fixed
- Done (2026-10-03): Questions marked `urgent` are listed first; the Blueprint button is smaller and slightly see-through on a phone-sized screen, and re-checks for fixed bars.
- Done (2026-10-03): Partly fixed: words recorded in `heard`, and closed questions, are no longer pasted again. Still open: the Blueprint button sits over content at phone width, and urgent questions are not listed first.
- Kind: viewer
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Typed non-answers are pasted again, and two layout faults

Answers typed in the panel stay in the browser until the question is answered, so 'have to ask her' will be copied again next time. At phone width the Blueprint button sits over the bottom-right of the content. Questions are sorted by what they block, so an urgent one (a possible live key) is not first. Reported by: merge helper (Greenfire copy), create helper (workshop), annotate helper (bike shop).

## 25. Helpers each job had to write for itself
- Status: fixed
- Done (2026-10-03): `blueprint.py try` clicks through a page and reports what happened; `add-question` appends a numbered question; SKILL.md says where to anchor rows that come from one template.
- Done (2026-10-03): Partly fixed: `blueprint.py ask <folder> [--who name]` prints open questions as a list to send. Still open: a click-through helper, a generator for long question lists, and anchors on rows that all come from one template.
- Kind: other
- When: 2026-10-03 20:36
- Working on: cold test round 1, 2026-10-03
- Folder: ClaudeStuff

Helpers each job had to write for itself

A click-through script (about 60 lines); a generator that wrote the JSON for 49 questions, renumbered them and checked cross-references; a script to strip duplicate anchors because 'anchor one repeated item' does not work when every row comes from one template; 'offer to put those questions in a form the user can send on' has no script behind it. Reported by: annotate helper (bike shop), create helper (workshop), merge helper (Greenfire copy).

## 26. The viewer's dock() only runs on load and on resize, so a bottom bar that the mockup shows
- Status: fixed
- Done (2026-10-03): The viewer now re-checks for fixed bars every half second, not only on load and resize.
- Kind: viewer
- When: 2026-10-03 21:07
- Working on: volunteer sign-up page
- Folder: ClaudeStuff

The viewer's dock() only runs on load and on resize, so a bottom bar that the mockup shows later (here, a bar that appears on a phone once an event is chosen) is not noticed and the Blueprint button covers the bar's button. Seen in a Playwright click-through at 390 wide: the click on the bar's link was intercepted by #blueprint-viewer-root. Worked around in the mockup by dispatching a resize event when the bar shows or hides. dock() could also run from the 500ms sync.

## 27. The placeholder count reported 0 for a page that uses volunteers@willowmere.example five t
- Status: fixed
- Done (2026-10-03): Addresses ending in .example, .test and .invalid are now counted as placeholders, in text and in links.
- Kind: check
- When: 2026-10-03 21:12
- Working on: volunteer sign-up page
- Folder: ClaudeStuff

The placeholder count reported 0 for a page that uses volunteers@willowmere.example five times. It seems to know example.com but not the reserved .example ending (nor .test or .invalid), which is the safer way to write a made-up address. I listed the stand-ins in project.content and made them a launch question by hand.

## 28. The contrast check did not see a background drawn behind text by ::before or ::after (cut 
- Status: fixed
- Done (2026-10-03): The viewer's contrast check now reads a shape that ::before or ::after paints behind an element (positioned, covering it, negative z-index). The phone check skips anything not rendered, such as the inside of a closed details.
- Kind: check
- When: 2026-10-03 21:49
- Working on: not said
- Folder: mockup-blueprint

The contrast check did not see a background drawn behind text by ::before or ::after (cut paper, a tilted block), so it compared the text with the colour further back and gave a false warning; and the bar-covers-end check measured labels inside a closed details element. Both found while redoing the volunteer page with the warm guide.

## 29. Ran: study tartinebakery.com ... bigsurbakery.com --out study. For bigsurbakery-com the su
- Status: fixed
- Done (2026-10-03): study now measures only text a visitor can see (not labels hidden for screen readers), prints 'no text could be measured' instead of None, and never reports markup as a headline.
- Kind: script
- When: 2026-10-03 21:58
- Working on: Bakery style guide
- Folder: volunteer-signup-before

Ran: study tartinebakery.com ... bigsurbakery.com --out study. For bigsurbakery-com the summary line printed 'largest text Nonepx ("None", None) ... faces ; main colours' (empty), yet counted the site as seen. In metrics.json its 'headline' is raw HTML ('<img width="202" height="30" src=...'). For e5bakehouse-com the largest text was reported as 'USER ACCOUNT MENU' (24px), which looks like a hidden or off-screen menu label, not anything a visitor sees. For breadahead-com the largest text was 14px 'BAKERY' while reading text was 18px. I carried on and relied on the pictures, not these numbers; the summary should print 'no text measured' instead of None and skip text that is not visible.

## 30. Make a style guide, step 1 is headed 'Ask first, every time' but its body only covers the 
- Status: fixed
- Done (2026-10-03): Step 1 rewritten as 'Say what is about to happen, every time', with one case for 'nothing fits' and one for 'the user asked outright' (name the nearest guide and how theirs would differ).
- Kind: instructions
- When: 2026-10-03 21:58
- Working on: Bakery style guide
- Folder: volunteer-signup-before

Make a style guide, step 1 is headed 'Ask first, every time' but its body only covers the case 'when you got here because nothing fits'. The user here asked outright for a reusable guide. It is unclear whether anything must be asked or said in step 1 in that case (for example, showing which guides exist and that 'warm' is the nearest). I took it that step 1 is satisfied by the user's request and went on to the interview.

## 31. Step 2 collects 'one site they would hate theirs to resemble' but step 3 does not say whet
- Status: fixed
- Done (2026-10-03): Step 3 now says to study the disliked site into a folder of its own and keep it out of the counts.
- Kind: instructions
- When: 2026-10-03 21:58
- Working on: Bakery style guide
- Folder: volunteer-signup-before

Step 2 collects 'one site they would hate theirs to resemble' but step 3 does not say whether to run study on it. Studying it would give evidence for 'must never look like'; leaving it out keeps the counts clean. I guessed: study it in a separate folder (study/avoid) so its pictures and numbers do not mix into the counts.

## 32. pophams.com failed with net::ERR_CONNECTION_CLOSED. The skill does not say whether to retr
- Status: fixed
- Done (2026-10-03): study treats an error status or an error or block page as not seen, says to try once more by itself, and a second run into the same folder now adds to the first.
- Kind: script
- When: 2026-10-03 21:59
- Working on: Bakery style guide
- Folder: volunteer-signup-before

pophams.com failed with net::ERR_CONNECTION_CLOSED. The skill does not say whether to retry, so I ran 'study www.pophams.com --out study/retry'. That returned a hosting error page ('Error 410', Montserrat, 53px) and the script reported '1 of 1 site(s) seen' and measured the error page as if it were the site. study should notice an error status or an error-page title and report COULD NOT BE SEEN. I left Pophams out of the counts. Also: study gives no advice on retrying, and a second run into the same --out folder would overwrite metrics.json and the sheets, so a retry has to go in another folder.

## 33. breadahead.com: the first screen is one very large headline ('Early Bird Sale', roughly 15
- Status: fixed
- Done (2026-10-03): study reports when one picture fills most of the first screen and says the type sizes mean little there; the job's steps say numbers cannot see lettering in pictures.
- Kind: script
- When: 2026-10-03 21:59
- Working on: Bakery style guide
- Folder: volunteer-signup-before

breadahead.com: the first screen is one very large headline ('Early Bird Sale', roughly 150px tall letters) that is part of a picture, so study reported 'largest text 14px (BAKERY)' and headline null. Lettering inside pictures is common on food sites (flourbakery.com 'BUTTERY' is the same). The numbers under-report headline size on exactly the sites that make the most of it; the summary line could say 'the first screen is mostly one picture; look for lettering in it'.

## 34. study's 'SOMETHING COVERS THE PAGE' flag did not match the pictures. Flagged: tartinebaker
- Status: fixed
- Done (2026-10-03): The 'something covers the page' guess was replaced: study now reports a fixed box that talks about cookies, newsletters or offers, with its words, tries more ways of closing one, and reports a blocked phone page. The steps say to judge 'partly seen' from the pictures.
- Kind: script
- When: 2026-10-03 22:00
- Working on: Bakery style guide
- Folder: volunteer-signup-before

study's 'SOMETHING COVERS THE PAGE' flag did not match the pictures. Flagged: tartinebakery.com (a thin cookie bar at the bottom). Not flagged at wide width: e5bakehouse.com and dominiqueansel.com, which have the same kind of cookie bar, and dominiqueansel.com's second screen, which is wholly covered by a '10% off' pop-up. levainbakery.com phone was flagged but its phone picture is clean. flourbakery.com on a phone showed 'We couldn't verify the security of your connection. Access to this content has been restricted' where the top picture should be, and bigsurbakery.com's second screen had a large blank area (pictures not loaded); neither was reported. I decided 'partly seen' from the pictures, not from the flag.

## 35. Step 2 says 'work out for yourself which kind of guide it is' with one clause per kind. A 
- Status: fixed
- Done (2026-10-03): Step 2 now gives a test for feel, field or purpose, names a model guide for each, and asks the guide to say which was chosen and why.
- Kind: instructions
- When: 2026-10-03 22:00
- Working on: Bakery style guide
- Folder: volunteer-signup-before

Step 2 says 'work out for yourself which kind of guide it is' with one clause per kind. A guide for 'small independent bakeries and cafes' is plainly about one trade (field) yet the interview (three words, admired sites) and the detail map are about feel, and step 4's example uses --kind feel. The choice matters: a site stacks at most one per shelf and a field guide beats a feel guide. No test is given for telling them apart, and SKILL.md does not point to a field or purpose guide to read as a model (only style-feel-warm.md). I read the top of style-field-education.md and the stack section of style-guide.md to decide, chose feel because what I gathered is where the detail goes, not what visitors come to do, and said so in the guide.

## 36. Step 4 and the output of 'style new' both say "'check' warns while any TODO are left". Wit
- Status: fixed
- Done (2026-10-03): New command 'style check <name>' checks one guide by itself: TODO left, missing sections, notes without Status, Source or Rule, sources that do not say where they come from.
- Kind: check
- When: 2026-10-03 22:03
- Working on: Bakery style guide
- Folder: volunteer-signup-before

Step 4 and the output of 'style new' both say "'check' warns while any TODO are left". With only a guide and no mockup there is nothing to run check on: 'check shelf/style-feel-bakery.md' answers 'is not wired to a context file; run init on it first'. So a guide cannot be checked by itself when the job is only 'make me a guide'. I counted TODO with grep (0) and confirmed 'style' lists it as 'bakery, yours, 0 approved, 10 draft'. A 'style check <name>' would fit: TODO left, notes without Status or Source, counts without site names.

## 37. Step 4 passes --by '<whose it is>' to 'style new', but the interview in step 2 never asks 
- Status: fixed
- Done (2026-10-03): The interview now asks whose name goes on the guide.
- Kind: instructions
- When: 2026-10-03 22:03
- Working on: Bakery style guide
- Folder: volunteer-signup-before

Step 4 passes --by '<whose it is>' to 'style new', but the interview in step 2 never asks whose guide it is. In a real session I would have had to guess or go back to the user. Add it to the interview or say what the default is.

## 38. Step 3 says to go down nine parts of the page for every site, 'note which level each got',
- Status: fixed
- Done (2026-10-03): study writes tally.md (sites down, parts across) into the study folder, and 'study --guide <name>' keeps the study with the user's own guides so counts can be traced.
- Kind: instructions
- When: 2026-10-03 22:03
- Working on: Bakery style guide
- Folder: volunteer-signup-before

Step 3 says to go down nine parts of the page for every site, 'note which level each got', 'then count', but gives nowhere to put that table (63 cells for seven sites). study writes metrics.json and the sheets only. I kept the tally in my working notes and it is not saved anywhere, so nobody can audit the guide's '5 of 7' counts later. study could write a blank tally sheet (sites down, parts across) into the --out folder. Related: nothing says where the study folder should live afterwards or whether the guide's Sources should point to it; I wrote its path into Sources.

## 39. The contact sheets show each picture about 600 pixels wide, enough to see layout but not t
- Status: fixed
- Done (2026-10-03): The steps and the script's own output now say when to open a site's single pictures; study tries harder to close boxes.
- Kind: script
- When: 2026-10-03 22:03
- Working on: Bakery style guide
- Folder: volunteer-signup-before

The contact sheets show each picture about 600 pixels wide, enough to see layout but not to read small type, judge a menu, or tell a cookie bar from a footer. I opened seven of the single pictures as well. Step 3 says 'look at every contact sheet it names' and does not mention the single pictures; say when to open them. Also study does not try to dismiss cookie or newsletter boxes, so 5 of 7 sites were partly hidden; with a list this short that weakens every count.

## 40. The scaffold's detail map has nine fixed rows. For a trade the thing that mattered most be
- Status: fixed
- Done (2026-10-03): The skeleton and the steps say rows of the detail map may be added or dropped, and that the finished rules are read against the template tells, with a 'Careful' line where a rule asks for one of them.
- Kind: instructions
- When: 2026-10-03 22:03
- Working on: Bakery style guide
- Folder: volunteer-signup-before

The scaffold's detail map has nine fixed rows. For a trade the thing that mattered most beyond those (opening hours and address) had no row, and nothing says whether rows may be added or removed. I added one. Also the guide's main finding conflicts with the general guide's template tell 7 (pale ground, one accent) and with the warm guide's advice (bold colour, huge headline); nothing tells the writer of a new guide to compare it with the general guide's tells or say how to resolve a clash. I wrote a 'Careful' line in the colour note.

## 41. The 'In a mockup' question: a guide whose signature is a real photograph cannot be shown i
- Status: fixed
- Done (2026-10-03): The skeleton has an 'In a mockup' line on the signature note, and the steps say it is judgement until a mockup has been made.
- Kind: instructions
- When: 2026-10-03 22:03
- Working on: Bakery style guide
- Folder: volunteer-signup-before

The 'In a mockup' question: a guide whose signature is a real photograph cannot be shown in a mockup. style-feel-warm.md answers it for itself (draw artwork in the site's material) but step 4 does not ask a new guide to say what to do when the signature cannot exist yet. I wrote untested advice and marked it as judgement.

## Cold test of version 0.9.0 by a new user on a computer with nothing set up (2026-10-03)
- Status: fixed
- Kind: other

A fresh session made a booking page with Alpine.js and Tailwind, tools the library has no notes on, starting from a Python with no browser library. Setup worked in one command and the whole job ran. It reported thirteen problems, all fixed in 0.9.1:

1. Too much to read before drawing: the Create job now says what to read before each step.
2. No list of what the site's own guide holds: `references/site-guide.md`.
3. The warm guide pointed at a file that is not in the skill: reworded.
4. `init` came after steps that need the context file: moved to when the first page exists.
5. `try` refused options placed between its steps: options may now come anywhere.
6. `try` said "messages showing: none" with an error on screen: it now finds messages tied to a field and lists fields marked as wrong; `--full` photographs the whole page; a press on a switched-off control says so.
7. Contrast false alarm for words over a shape drawn as an empty element: the check now reads such a shape.
8. `check` asked for `project.status.background` and the format reference never mentioned it: documented.
9. A fact settled inside a section that is a sentence had nowhere to go: `project.decided`.
10. "No acceptance criteria" fired for plain text and decoration: now only for things that can be pressed or typed into, or that are still to be built.
11. "Two questions in one" fired on "or who have low vision": relative clauses no longer trip it; `add-question --replace` rewords a question.
12. "Take the default" and "do not answer blocking questions yourself" pulled apart: the core now says a default is worked to, the question stays open, and the verdict stays NOT READY.
13. Tailwind was not named as a tool without notes because its address has no file ending: any outside script or stylesheet now counts.

## Version 0.10.1: Windows, found by reading the code before the first Windows user's notes arrived (2026-10-04)
- Status: fixed
- Kind: script

The skill had only ever run on Linux. Reading the script for things that differ on Windows found these, all fixed without a Windows machine to try them on, so each still needs confirming there:

1. The Django tests reached their throwaway Postgres through a socket folder, which Windows does not have: they now connect the way the server itself says (an address and a port on Windows).
2. Output from the test scripts and from the set-up probe was read in the console's own encoding: now always UTF-8.
3. The console was made UTF-8-safe only after the command line was read, so help text could still fail: now first thing.
4. A copy of the skill checked out with Windows line endings made every mockup's viewer look out of date: files are now compared ignoring line endings, and `.gitattributes` keeps the skill's files the same bytes everywhere.
5. The set-up failure message gave Linux advice on Windows.

Also in 0.10.1: `try` no longer reports a live region that was on the page before anything was pressed as a message (reported while working on a tutoring site, 2026-10-04).

