# Restyle an existing mockup

Read `SKILL.md` first.

When a mockup already exists and the job is to make it look better with the style stack, not to change what it does.

1. **Work on a copy** in its own folder and keep the original where it is. The user needs both to compare, and the original is somebody's work.
2. **Write the brief and choose the guides**, as in steps 2 to 4 of `references/jobs/create.md`. Then look at the existing page next to the guides and list what they would change and why. Expect to find that a competent mockup already has most of the right content; what the guides usually move is where the emphasis sits, how many typefaces and boxes there are, and what the first screen says.
3. **Keep every anchor, every word and every behaviour** unless a guide gives a reason to change one. Carry the page's own build comments across and correct the ones the restyle makes untrue. Where a guide does change words or the order of sections, that is a decision for the owner: mark those elements `inferred` and ask about each as its own question.
4. **Update the context.** Element notes often describe the look ("the chosen button turns dark"). Reword the ones that are no longer true, set `project.style`, and add one question that blocks the build: which version is to be built. Until the user has seen both, the restyle is a proposal.
5. **Write the site's own guide** (`references/site-guide.md` lists its sections): the brief, what changed with the guide that asked for it, the tokens, what the first screen holds on a phone, and what the guides did not settle. Then run `check` and report as usual, with the before and after side by side.
