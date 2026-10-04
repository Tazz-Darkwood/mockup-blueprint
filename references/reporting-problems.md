# When the skill itself gets in the way

This skill is still being tested, and the person who looks after it can only fix what they hear about. Whenever the skill, not the mockup, is the problem, note it at once with the script, then carry on:

```
python3 "<skill-dir>/scripts/blueprint.py" feedback --kind instructions --task "tutor site" "Step 6 says to ask the user, but does not say what to do when there is nobody to ask. I marked the questions open and carried on."
```

Kinds: `instructions` (unclear, missing, contradictory, or in the wrong order), `script` (an error, a wrong or confusing result), `check` (a false alarm, or something it should have caught), `library` (a note that was wrong, missing or hard to find), `format` (something the blueprint could not express), `viewer`, `other`.

Note it when any of these happens:

- You had to guess what an instruction meant, or two instructions disagreed.
- You did something the instructions did not cover, or chose not to follow one. Say why.
- The script failed, or its output misled you. A crash is noted for you; add what you were trying to do.
- A check complained about something that was fine, or stayed quiet about something that was wrong.
- The user had to explain something the skill should have told you, or was surprised by what you did.
- A library note did not match what the tool actually did.
- You wrote a helper, a workaround, or the same few commands several times. That is something the skill should carry.

Say what you were doing, what happened (the exact command and output if there was one), and what you did instead. Write it when it happens, not from memory at the end. Do not edit the skill's own files to fix it unless the user asks: the point is that the problem is seen. The log is kept in the user's own folder for this skill, outside the skill itself (`doctor` prints where), so it survives updates and can be sent to whoever looks after the skill. It records the name of the folder you were working in, not its full path. If you have been told to change nothing outside a project folder, keep the log beside the mockup with `feedback --beside <folder>` and tell the user where it is. A note about the skill is not a substitute for the library's own route for tool notes; if the problem is a wrong library note, do both.

At the end of the job, run `feedback --list` and tell the user how many notes were added, what they were about, and where the file is, so they can send it to whoever looks after the skill.
