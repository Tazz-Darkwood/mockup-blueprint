---
name: Sorcery (a recipe)
summary: A site that feels like a painted wizard picture from a 1970s or 80s book cover, poster or record sleeve. A dark room with one low lamp, stained parchment in ink, a scene at the top, magic signs scattered in every gap, and as little clear space as possible.
kind: recipe
personality: dramatic
checked: 2026-10-07
source: the sorcery feel guide (made by Steven, from six painted pictures and one band's website), and the two mockups made with it
---

# Sorcery

For a site whose owner wants the look of old painted wizard art: "wizardy, hand-painted, old". The one idea: the page is a picture with a light inside it, and everything on the page is lit by that light. The page is full from edge to edge, and only the words get calm patches.

## Picks

```json
{
  "colour": {"start": "sorcery"},
  "background": {"start": "detailed-ground"},
  "light": {"start": "sorcery"},
  "materials": {"start": "sorcery"},
  "frames": {"start": "sorcery"},
  "shapes": {"start": "sorcery"},
  "lettering": {"start": "sorcery"},
  "density": {"start": "sorcery"},
  "pictures": {"start": "sorcery"},
  "motion": {"start": "sorcery"},
  "values": {
    "text-xxl": "clamp(2.75rem, 1.6rem + 3.6vw, 4.75rem)",
    "texture-strength": "0.05",
    "measure": "54ch",
    "pictures-age": "0.5"
  }
}
```

The values were found on a rebuild of the joke wizard site from this recipe, which Steven liked better than the original: at full size the name (up to 152px) covered the whole scene, so the biggest heading stops at about 76px; the lamplit texture at full strength read as blue denim, a machine pattern, so it is a third as strong; Alegreya is a wide face, so lines stop at 54 characters wide; and the aged picture treatment at full strength turned the scene to grey fog, so it is at half.

## What makes it

- The top is a scene, not a heading: a place with a robed figure or a thing of power at its middle, one source of light inside the picture (an orb, a lamp, a sword), and the site's name inside the picture's frame like a title on a book cover. Ask in the brief: what is the light, who stands in it, what frames it?
- Magic signs drawn by hand (circles, stars, runes, small diagrams) scattered between and around the sheets, at different sizes and angles, some half under a sheet or off an edge; never in a row or a pattern, never over words or controls.
- In earnest, with a wink: the picture is painted as if all of it were true, and one thing in it is funny; the words are plain and useful, with one phrase that belongs to this world.
- Made by a hand, never by a machine: every picture and ornament shows a brush mark, a pen line or an uneven edge. Test: could this be the menu screen of a modern fantasy video game? If so, it has gone wrong. Never use the reference pictures, and never a smooth machine-made picture.

## Notes from the owner

- On the feel: "wizardy, hand-painted, old".
- On a flat drawing for the scene: "that would be too plain. I think it would be better to make the site noisy like all the pics I showed you and try to have as little clear space as we can".
- On the first site made with it: "this looks really good, I like pretty much everything about it. I think the only thing is there doesn't feel like enough aged parchment and ink, and enough magic sigils drawn in random places." After the fix: "it looks good to me".
- On a shop it led: "A looks the best of the two". Then: "I think sorcery is an approved style guide for sure."
- On stacking: a warm-led site should be "a warm site with a hint of the sorcery", where the guides "flavor each other so it fills everything but with warm things". When sorcery came second and kept its figure and light: "the sorcery one seems to be leading it most of all".

## Used on

A joke site for people leaving tech for magic; the lead look of a shop for a fair-stall group; the second half of a game-style joke site, before it was taken out.

## Not covered yet

- On a small site the scene can be the menu: four or five parts of the picture, each a real link with its label written on it, and the same places listed plainly once on the page. No part gives this.
- The repeated item as a framed plate with a colour of its own: the frames pick gives the plate, not its own colour.
- Forms, fields and the foot of the page stay plain and dark, off the parchment, with the metal colour only for small marks.
- When sorcery is not the lead: keep the signs, two or three things to find and one wink, drawn in the lead's material; give up the figure, the light, the dark ground and parchment.
- A daylight version (one of the six pictures is sunny); phones beyond one look; inner pages, shops and long reading; how much of it survives without a commissioned painting; who paints the scene for a real site.
