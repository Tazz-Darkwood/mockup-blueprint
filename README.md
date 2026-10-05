# mockup-blueprint

A skill for Claude Code. It turns an HTML mockup into a blueprint: the mockup, plus everything a builder needs that a mockup never shows (what each button does, where data comes from, who is allowed in, where it will be hosted), plus a check that says whether enough is in place to build and to launch.

You do not run anything in this folder yourself. Claude does, when you ask it for something the skill covers.

## Installing

The easy way: tell Claude Code "install the skill from https://github.com/Tazz-Darkwood/mockup-blueprint". What it should do is put a copy of this repository in your skills folder:

```bash
git clone https://github.com/Tazz-Darkwood/mockup-blueprint ~/.claude/skills/mockup-blueprint
```

On Windows the folder is `%USERPROFILE%\.claude\skills\mockup-blueprint`. To have the skill in one project only, clone it into that project's `.claude/skills/` instead. The folder must be called `mockup-blueprint`.

Then start a new Claude Code session in your project.

## Using it

Ask in your own words. For example:

- "I want a mockup for a page where people can book a place at my open evening."
- "Here is a mockup someone sent me. What is it missing before it can be built?"
- "Make this mockup look better."
- "Make me a style guide for bakery sites that I can reuse."
- "Build the real site from this mockup."

The first time, Claude will check what is set up on your computer. Some of the checks need a browser it can drive, and it will ask before downloading one (about 300 MB, kept in a folder of the skill's own; nothing else on your computer changes).

Claude asks questions as it goes. Short answers are fine, and "I don't know, ask the client" is a real answer: it gets written down as an open question for that person.

Open any mockup it makes in your browser and press the "Blueprint" button to see the notes and the open questions. Anyone you send the folder to can type answers there and send them back to you. To change wording, select any words on the page and press "Note on these words": say what is wrong, or type the exact words you want instead.

## Your own folder

Things that are yours are kept outside the skill, in `~/.claude/mockup-blueprint/`, so updating the skill never touches them:

- `styles/`: style guides you made
- `library/`: notes on tools the skill did not know about
- `feedback.md`: problems Claude met while using the skill

The skill is still being tested. If something went wrong or seemed odd, send that folder (or just `feedback.md`) to whoever gave you the skill. It records the names of the folders you worked in, not their full paths, and nothing is ever sent anywhere by itself.

## Updating

Ask Claude to update the skill, or run `git pull` inside the skill's folder. Your own folder stays as it is.
