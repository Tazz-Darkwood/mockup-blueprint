---
name: Light (a part guide)
summary: Where the light on a page comes from and how much of it there is - what is brightest, what falls into shadow, what glows. Its options can be picked on their own and combined with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: the mockups made with the skill so far, and the guides named in each option
---

# Light

A part guide. It covers the light on a page: whether there is a source of light at all, where it is, how bright the page is round it, and what glows. A site picks one option in its own guide, and in the blueprint as `project.style.parts`: `{"light": "<option-id>"}`. The picked option wins over the feel guide for the light only; everything else still comes from the feel guides. The general guide's accessibility minimums (contrast, text size, tap size) still hold whatever is picked.

Light is the part that changes contrast most. A light source makes some of the page brighter and the rest darker, so text that passed on a flat page can fail in the shadow, or next to the glow. Every option below says what it does to contrast.

## Choosing

| Option | What it feels like | Suits best | Fights |
|---|---|---|---|
| Flat and even | No light at all: a page, not a picture. Calm and clear | professional, warm | a scene that is meant to be lit |
| Daylight | Bright, warm, open air; everything is lit and nothing hides | warm, a game-style or playful site | professional (too loud), anything meant to feel hushed |
| Moonlight | Night, cool and quiet; everything visible but dim and blue | artistic, a second look for a site | warm (the bright colours go grey), professional |
| Sky by the clock | The page keeps time: day, dusk, night, as the hours pass | a site that is a place people come back to | anything that must look the same in every picture of it |
| One light | A dark room with one lamp in it; what is near is lit in its colour, the rest falls into dark | artistic, a dark, painterly site | warm (it wants the whole page bright), professional |
| Spotlight on the main thing | The light picks out one thing, and follows the visitor's attention | one light, sales (the product) | a page with no single main thing |
| Glow on edges | Bright rims and haloes on small things, like a game screen | a game-style site, small marks only | professional, and any page that must look hand-made |

How to choose:

- Start from the lead feel guide: if it decides how bright the page is (warm's bold flat colour, a dark guide's dark room), pick the option that agrees with it, or say in the site's guide why not.
- Pick one light for a look. Two sources of light on one page (a bright sun and a lamp) fight over which is brightest; on one mockup the painted sun had to be dimmed so the light the figure held stayed the brightest thing.
- A site with two looks may pick a light for each, and a site may use two options on different pages when each page is a different place: the 3D game kept its pages for deciding in flat daylight and its game screen underground, lit by lamps.

## Options

### Flat and even
- Id: flat-and-even
- Status: draft
- Looks like: no light source at all. Grounds are one flat colour or a quiet texture, and anything raised has at most one small, soft shadow. The usual web page.
- Made with: the general guide's tokens and nothing more. One shadow token, used the same way everywhere, so every raised thing seems lit from the same side.

```css
:root {
  --ground: #f7f4ee; --surface: #fff; --ink: #1c1f23;
  --shadow: 0 1px 2px rgb(0 0 0 / 0.06), 0 8px 24px rgb(0 0 0 / 0.06);
}
.flat { background: var(--ground); color: var(--ink); }
.flat .card { background: var(--surface); box-shadow: var(--shadow); }
```

- Careful: contrast is the easiest of any option: every pair of text and ground is measured once and holds wherever it appears. The risk is the template look: flat light with a pale ground and one accent is tell 7 in the general guide. Pair it with a bold colour or a detailed ground, not with a pale one.
- Goes with: `density: balanced`, a bold flat colour from warm.
- Used on: 4 mockups: a home soap shop, a tutor's page, a poetry site, a volunteer page.

### Daylight
- Id: daylight
- Status: draft
- Looks like: a bright outdoor scene behind the page: a blue sky lightening to warm near the horizon, a sun with a soft glow and a few broad rays, clouds, saturated green ground. Everything is lit; the sun is the brightest point.
- Made with: a sky drawn as a vertical gradient, a sun as a disc with a radial glow round it, and rays as pale wedges at low opacity. Words never sit on the sky itself: they sit on a dark panel or a solid band.

```css
.daylight {
  --sky-top: #2a78d4; --sky-mid: #7cc4ff; --sky-low: #ffe6a6; --sun: #fff8d2;
  background:
    radial-gradient(circle at 75% 30%, var(--sun) 0 6%, rgb(255 240 168 / 0.8) 9%, transparent 30%),
    linear-gradient(var(--sky-top), var(--sky-mid) 45%, var(--sky-low) 75%);
}
.daylight .panel { background: rgb(22 18 14 / 0.88); color: #fff; }   /* words on a dark panel, never on the sky */
```

- Careful: daylight is where pale text fails. White on a mid-blue sky is about 2.5:1 or less, and an outline drawn with four text shadows does not count: the check measures the letters against the ground, not their outline. Put every line of text on a panel dark enough to pass against the brightest part of the sky behind it, or on the solid ground lower down with dark ink. Keep one area brightest (the sun) and push the rest of the picture back where panels sit.
- Goes with: `glow-on-edges` for small marks, `density: busy`, `frames: riveted-metal`.
- Used on: 2 mockups: a game-style joke site (its main look: a summer day on a road to a castle) and a 3D game in the browser (its pages above ground are in daylight, a sand page with dark ink).

### Moonlight
- Id: moonlight
- Status: draft
- Looks like: the same outdoor scene at night. A deep blue sky, a pale moon with a cool halo, everything still visible but dim and blue, a few stars. Calm where daylight is loud.
- Made with: the daylight recipe with the colours turned: a dark-to-mid blue sky, a moon disc with a cool radial glow, and the scene's own colours pulled towards blue. Pale text with a cool tint reads well on it.

```css
.moonlight {
  --sky-top: #050f2a; --sky-mid: #12306b; --sky-low: #2f6aaf; --moon: #eaf8ff;
  background:
    radial-gradient(circle at 25% 28%, var(--moon) 0 6%, rgb(191 230 255 / 0.5) 9%, transparent 26%),
    linear-gradient(var(--sky-top), var(--sky-mid) 50%, var(--sky-low));
  color: #e8efff;
}
```

- Careful: pale text passes easily on the top of the sky and fails near the horizon and the moon, where the blue is lighter: measure it there. Mid-tone colours (a green, a purple) go dull and close in brightness at night; a meaning carried by colour needs a word beside it. A main button in a pale cool colour with dark text stays the brightest thing after the moon.
- Goes with: `sky-by-the-clock` (it is the clock's night), `glow-on-edges` on small marks.
- Used on: 2 mockups: the second look of a game-style joke site (a moonlit lake), and the night hours of a 3D game in the browser.

### Sky by the clock
- Id: sky-by-the-clock
- Status: draft
- Looks like: a sky that follows a clock: day, a warm glow at sunrise and sunset, then night with a moon. The page looks different at different times, which makes it feel like a place that goes on when nobody is looking.
- Made with: work out how high the sun is from the hour, and blend the sky's colours and the light's strength from that: night at 0, day at 1, and a warm glow near the horizon in between. Repaint only when the light has changed enough to see. In a flat page, the same thing can be done by setting the sky colours as custom properties from the hour.

```css
.sky-clock {
  /* set from the hour by the script below; these are noon */
  --sky-top: #2a78d4; --sky-low: #ffe6a6;
  background: linear-gradient(var(--sky-top), var(--sky-low));
}
```

```js
// sun height from the hour: above the horizon from 6 to 18
const hour = new Date().getHours() + new Date().getMinutes() / 60;
const sunUp = Math.sin(((hour - 6) / 12) * Math.PI);           // -1 at midnight, 1 at noon
const day = Math.min(1, Math.max(0, (sunUp + 0.12) / 0.37));     // 0 night, 1 day
const glow = Math.max(0, 1 - Math.abs(sunUp) / 0.3);             // near sunrise and sunset
```

- Careful: contrast changes with the hour, so it must pass at the worst one. Check it at noon and at midnight at least, and at dusk if text sits on the sky; list those states in `project.check_states`. Change the sky gradually, never in a jump that flashes; under reduced motion it may still follow the clock, since one hour's change is not motion, but nothing in it animates. Say in the blueprint whose clock it is (the visitor's, the server's, a game's): on the 3D game it was the game's own clock, one day every 24 real minutes.
- Goes with: `daylight` and `moonlight` (its two ends), `spotlight-on-the-main-thing` for a light that matters only at night.
- Used on: 1 mockup: a 3D game in the browser, whose sky, sun and moon follow the game's clock.

### One light
- Id: one-light
- Status: draft
- Looks like: a dark room with one source of light inside the picture, a lamp, a lantern or a glowing ball. Things near it are lit in its colour; things further away fall into shadow and dark. It is the brightest point on the page, and the main button takes its colour.
- Made with: a dark ground with a colour of its own (wine, night blue), never black. In the picture, a radial gradient in the light's colour laid over the scene with `mix-blend-mode: screen`, a dark radial gradient centred on the same point laid over that, and hatching or stipple that gets heavier the further it is from the light. On the page, one glow colour kept for the light and the main action only.

```css
.one-light {
  --room: #1e0e11; --glow: #f2a541; --on-glow: #1e0e11; --pale: #efe6d6;
  background: var(--room); color: var(--pale);
}
.one-light .scene { position: relative; background: #0b0a16; overflow: clip; }
.one-light .scene::after {                 /* the light, laid over the picture */
  content: ""; position: absolute; left: 50%; top: 55%; width: 26rem; aspect-ratio: 1; translate: -50% -50%;
  background: radial-gradient(circle, rgb(255 190 100 / 0.32), rgb(255 160 70 / 0.08) 40%, transparent 68%);
  mix-blend-mode: screen; pointer-events: none;
}
.one-light .btn-main { background: var(--glow); color: var(--on-glow); }   /* the brightest thing after the light */
```

- Careful: the light is small. A page that glows all over has no light at all; nothing very bright covers more than a small part of the page. Nothing glows behind words meant to be read: put reading text on a calm dark patch, or on a sheet that is dimmer than the light (one mockup kept its paper at about two-thirds of the light's brightness, so the light stayed the brightest thing). The text in the shadowed parts still passes 4.5:1; darkness is not a way to make words quieter. If the glow moves (it breathes slowly, on two mockups over seven seconds), it stops under reduced motion and never flashes. Decide where the light sits in the picture before drawing, since a glow laid over it depends on that point.
- Goes with: `spotlight-on-the-main-thing`, `density: busy`, a detailed dark ground.
- Used on: 5 mockups: a dark, painterly joke site, two versions of a small shop, and the first two versions of a game-style joke site.

### Spotlight on the main thing
- Id: spotlight-on-the-main-thing
- Status: draft
- Looks like: a pool of light on the one thing that matters on the screen, the main action or the product, with the rest a step darker. The light answers the visitor: it grows when they reach for the main action, or follows what is theirs.
- Made with: a radial glow placed behind the main thing, at rest a little dim, brighter and wider when the main button is pointed at or has keyboard focus (`:has()` lets the glow react to the button). A slow, small change.

```css
.spot { --glow: #ffb030; position: relative; isolation: isolate; }
.spot::before {
  content: ""; position: absolute; inset: -20%; z-index: -1; pointer-events: none;
  background: radial-gradient(closest-side, rgb(255 196 90 / 0.5), rgb(255 160 40 / 0.18) 50%, transparent);
  opacity: 0.6; transition: opacity 0.6s ease, scale 0.6s ease;
}
.spot:has(.btn-main:hover, .btn-main:focus-visible)::before { opacity: 1; scale: 1.2; }
@media (prefers-reduced-motion: reduce) { .spot::before { transition: none; } }
```

- Careful: it reacts to focus as well as to the pointer, so a keyboard visitor gets it too, and it is never the only sign of focus: the focus ring is still drawn. The darker parts round the spot still pass the contrast minimum. Under reduced motion the change happens without the slow fade. Measure the main button's text against the brightest state of the glow behind it.
- Goes with: `one-light`, a product shown alone.
- Used on: 2 mockups, in part: a dark, painterly joke site (the light in its picture grows when the main button is pointed at), and a 3D game in the browser (a small light travels with the player's own piece, and matters only at night and underground).

### Glow on edges
- Id: glow-on-edges
- Status: draft
- Looks like: bright rims and haloes on small things: a slot whose rim glows in its rarity colour, a verdict word with a soft halo, trim on a figure that glows. Neon-like, and very much a game screen.
- Made with: a blurred shadow in the thing's own colour: `box-shadow` with a blur for a box, `text-shadow` with `currentColor` for a word, `filter: drop-shadow()` for a shape. Small things only, on a dark ground, where it shows.

```css
.glow-edge { --rim: #5aa2ff; background: #120c07; color: #fff; }
.glow-edge .slot { box-shadow: 0 0 0 2px #000, 0 0 0 4px var(--rim), 0 0 10px 2px var(--rim); }
.glow-edge .verdict { color: var(--rim); text-shadow: 0 0 12px currentColor; }
```

- Careful: a glow does not count towards contrast: the check measures the letters' own colour against the ground, so the colour has to pass on its own, and a halo round small text blurs its edges. Keep it for large words and for rims, not for reading text. A focus ring is a solid outline, not a glow, so that it reaches 3:1. A glow that moves (a pulse, a shimmer) is slow, stops under reduced motion and never flashes: nothing changes brightness more than three times a second. Two briefs named "glowing panels" as what a hand-made page must not look like; on such a site, leave it out.
- Goes with: `daylight` or `moonlight` behind it, `frames: riveted-metal`.
- Used on: 1 mockup: the latest version of a game-style joke site (rarity rims on reward slots, a halo on the verdict row, a glow round the message that announces the second look).

## Swatch book

`tests/parts/light.html` shows every option live; open it in a browser to choose by eye.

## Not covered yet

- A light that moves across the page as the visitor scrolls (the sun setting as they read down). Not tried.
- Photographs. Every lit page so far was drawn in code; how a real photograph's own light sits with these options is untried.
- Light in the dark for a whole site's theme: a dark mode that is only the flat option darkened is not covered here.
- How the check measures text laid over a glow that moves: it measures one moment. Nothing yet checks the brightest moment.
- A light source that is the page's own interface (a screen glowing in a dark room, light coming through a window frame). Named as ideas in briefs, not drawn.
