---
name: Motion (a part guide)
summary: What moves on a page and how, in layers that switch on their own - pace, feedback, entrance, ambient, clock, transitions and moments - from a page where nothing moves to a lamp that breathes, a sky that keeps the hour and a secret look that cross-fades in. It owns every duration and easing curve, handed to the other parts as shared values, and the rules every moving thing keeps - it stops when the visitor asks for less motion, never flashes, never hides content, and moves only opacity and transforms. Each layer works on a light page and a dark one, and can be picked with any feel guide.
kind: part
detect: []
checked: 2026-10-07
source: research online (six kinds of source, listed under Sources), the motion in 15 mockups made with the skill and in the feel guides, as named in each option
---

# Motion

A part guide. It covers what moves on a page and how: how fast and with what curve, what a control does when pointed at and pressed, how things arrive, what moves by itself, what follows a clock, how one view changes to another, and the few moments that mark something done. It is made of seven layers, each one decision that switches on its own: **pace**, **feedback**, **entrance**, **ambient**, **clock**, **transitions** and **moments**. A site picks a starting point whole, or a starting point with one layer changed, in its own guide and in the blueprint as `project.style.parts`: `{"motion": "professional"}`, or `{"motion": {"start": "lantern-fair", "entrance": "none"}}`. The pick wins over the feel guide for motion only. The general guide's accessibility minimums still hold whatever is picked, and so do the rules under "How it is built", which no option and no site guide overrides.

**This part owns how things move, never what is drawn.** The light part draws the lamp and its pool of light; this part decides whether it breathes. The frames part draws an inked button; this part decides that it moves into its shadow when pressed. The colour part decides what a pressed button looks like; this part decides how fast it gets there. Where another part's guide says how something moves (the light part's breathing lamp and spotlight, the frames part's pressed button), this part's layer is the one used, with its values.

**Most of the evidence is small.** Fifteen mockups were made before this part existed. None hid content behind an animation, none used scroll reveals or view transitions, and none flashed. Their motion was a lamp breathing over seven seconds (three mockups), stars twinkling, cards lifting or straightening under the pointer, buttons pressing in, a hand waving once on a done screen, a secret look cross-fading in, and two clocks. The options that no mockup used yet say so on their `Used on` line, and lean on the research instead.

## How it is built

**The shared values.** The pace layer sets eight custom properties on the element that carries the look (the `<body>`, or a wrapper round the sections). Every transition and animation on the page, in any part, is written with them, never with its own numbers, so one pick changes the whole page's speed, and reduced motion turns every one of them to zero at once.

| Property | What it is for |
|---|---|
| `--dur-short` | a control answering: a colour or veil on hover and press, a tick appearing. About 100 ms: "simple feedback" in NN/g's measure (R22) |
| `--dur-medium` | something small arriving or leaving: a card lifting, a menu, a tooltip. NN/g puts modals and small moves at 200 to 300 ms (R22) |
| `--dur-long` | something large changing: a panel, a view, a page, an entrance. Never over 700 ms; over 500 ms starts to feel like waiting (R22) |
| `--dur-step` | the gap between items in a stagger |
| `--ease-out` | for things arriving: fast at first, landing softly ("decelerate" in Material, "entrance" in Carbon; R16, R17) |
| `--ease-in` | for things leaving: slow at first, then gone ("accelerate", "exit") |
| `--ease-in-out` | for things moving from one place on the screen to another ("standard") |
| `--ease-spring` | a small overshoot that settles, for things that give and spring back. It is `--ease-out` in every pace but springy |

Leaving is quicker than arriving: an exit takes the next duration down (`--dur-medium` where the entrance took `--dur-long`) with `--ease-in` (R22).

**No motion first.** The values are zero by default, and only a visitor whose device has not asked for less motion gets them (R5, R21). Every animation that loops is declared inside the same media query. A browser too old to know the query gets the still page, which is the safe way round.

The zeros are under "Base" below; each pace sets its values on the page root inside `@media (prefers-reduced-motion: no-preference)`, and every transition is written with them (`.btn { transition: translate var(--dur-short) var(--ease-out); }`), so under reduced motion it is an instant change.

**The rules every option keeps.** They are what the swatch book's test proves in the page (see "Swatch book").

1. **Reduced motion means still.** Under `prefers-reduced-motion: reduce` every duration is zero, nothing loops, no view transition runs, and anything run from a script checks `matchMedia('(prefers-reduced-motion: reduce)')` first. WCAG asks that motion from interaction can be turned off (2.3.3, R1); the platform's own advice is to remove decorative motion and keep what does a job (R4, R5). This part goes further than "reduce" for a simple reason: a page of parts cannot tell which motion is decoration, so all of it becomes an instant change, and the change itself (the new view, the tick, the name on the sheet) still happens. The one exception is the clock, below.
2. **Anything that moves by itself for more than five seconds can be paused** (WCAG 2.2.2, R2). Reduced motion is not enough: the visitor may not know the setting. A page with an ambient layer or a running game clock has one switch, "Pause moving things", that sets `data-motion="paused"` on `<html>`; every looping animation reads it, and a game clock holds.
3. **Nothing flashes.** No more than three dips in brightness in any second (WCAG 2.3.1, R3); in this part's loops it is about one a second at most, and each change is small (a quarter of a glow's brightness, not on and off).
4. **Content is there before and without motion.** An entrance is a CSS animation that fills `backwards`, so the thing's own style is fully visible and the animation only plays over it. Never write `opacity: 0` in a stylesheet and wait for a script to add a class: if the script fails, is slow or is blocked, the page is empty. A scroll reveal moves things only, never fades them from nothing, so a page printed, photographed whole or searched with find-in-page is complete.
5. **Only opacity and transforms move.** `translate`, `scale`, `rotate`, `transform` and `opacity` run on the compositor and do not move anything else on the page, so they neither drop frames nor shift the layout (R6, R7). Never animate `width`, `height`, `top`, `left`, `margin` or `box-shadow`. The one exception is a control's own colour easing between its states (feedback `fade`): a button, over a tenth of a second. A shadow that grows is a second shadow on a `::after` whose opacity fades in (R25). A bar that fills is `scale` on the x axis from the left edge. One mockup animated a resource bar's `width` every 1.2 seconds, forever: it is the thing this rule is for.
6. **Nothing large travels.** The motions that make people with vestibular disorders dizzy or sick are large: big areas moving, parallax (layers at different speeds), zooming, spinning, things crossing the screen, motion that goes against the scroll, and scroll-jacking (R15, R24). In this part nothing larger than a card moves more than about 1.5rem, and nothing spins, zooms or moves against the scroll.
7. **Hover is extra.** Anything that answers the pointer is inside `@media (hover: hover)`, so a phone does not keep a card lifted after a tap, and nothing is reachable only by hovering (the mobile guide).

**When two parts meet.** The light part draws glows and shadows, and this part may fade them: a lift fades in the light part's `--shadow-mid`, and a breathing lamp changes the opacity of the light part's glow layer, never its gradient or blur (light R7, R12). The density part decides how far apart things are, and this part never animates a gap. The lettering part's text never moves by itself.

## Choosing

Start from a starting point (below), then change a layer if the brief asks for it.

| Starting point | What it feels like | Suits best | Fights |
|---|---|---|---|
| None | Nothing moves; every change is instant | Pages of reading; a tool used daily; a site for people who find motion hard | A game or a party |
| Professional | Quick, plain answers; nothing moves by itself | Professional; civic; anything with forms | Artistic, sorcery |
| Warm | Cards lift to the hand; a small party when you sign up | Warm; community groups; volunteering | Professional (too playful) |
| Artistic | Work settles into place as you scroll; slow fades | Artistic; a portfolio or gallery | Shops and forms (it slows the task) |
| Sorcery | A lamp that breathes in a dark, slow room | The dark, painterly guide | Anything bright and quick |
| Gilded dark | Quick, solid controls, sparkles, a secret second look | The game-interface guide; a game | Calm or official sites |
| Lantern fair | A breathing lantern over stalls that come in one by one | A night market; a shop with a dark lead | Daytime services |
| Almanac plate | Charts under the visitor's own sky, a star or two twinkling | A society, an observatory, a garden | Shops (the product must look the same at every hour) |
| Repair cafe | Buttons that press in; your name written on the sheet | A bright community page, busy and hand-made | Anything hushed |

How to choose:

- **Motion has a job or it goes.** NN/g names four: feedback on what the visitor did, showing that something changed, showing where things are, and hinting at what can be done (R23). Apple's guidance is the same: "Don't add motion for the sake of adding motion" (R18). A brief that cannot say what an animation is for picks `none` for that layer.
- **The pace follows the personality.** Serious and calm pages are brisk or gentle; dramatic ones slow; playful ones springy. Carbon keeps quick "productive" motion for tasks and slow "expressive" motion for a few significant moments (R17): a slow page still uses brisk feedback on its form.
- **One ambient thing per screen.** A lamp that breathes and stars that twinkle and dust that drifts is a screensaver. The light part's rule, one light per look, is this part's rule too.
- **A site with two looks** picks motion for each (the general guide's "A site with two looks"), and the swap between them is the moments layer's secret swap.
- **Say what reduced motion and the pause switch do** in the site's own guide, and list the reduced-motion state in `project.check_states` so `check` sees the still page.

## Base

The code every pick needs, lifted into a site's stylesheet whatever the layers say (`blueprint.py style css`): no motion first (every duration zero until a pace sets it, and only inside `no-preference`), the moves the layers share, the page's pause switch, and the view-transition timing. It styles only the page root and a few of the part's own classes; what arrives (`entrance`) is the sheets, panels and pictures of the bands, not one inside another, or anything marked .motion-enter. The part's own classes, each added by the page's markup or its script: `.motion-enter`, `.motion-lift`, `.motion-tilt`, `.motion-glow`, `.motion-star`, `.motion-mote`, `.motion-sun`, `.motion-changing`, `.motion-chosen`, `.motion-look`, `.motion-writing`, `.motion-bit` and `.motion-ring`. The values a script sets are `--motion-i` (a place in a stagger), `--motion-x` and `--motion-y` (a sun's place), and `--motion-dir` (which way a slide goes).

```css assemble
/* motion's base: no motion first. Every duration is zero and every curve linear; a pace sets them only inside
   prefers-reduced-motion: no-preference, so a visitor who asks for less motion gets an instant change everywhere. */
& { --dur-short: 0s; --dur-medium: 0s; --dur-long: 0s; --dur-step: 0s;
  --ease-out: linear; --ease-in: linear; --ease-in-out: linear; --ease-spring: linear;
  view-transition-name: none; }   /* only the thing that changes takes part in a view transition, not the whole page */
@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior: smooth; }
  ::view-transition-group(*), ::view-transition-old(*), ::view-transition-new(*) {
    animation-duration: var(--dur-long); animation-timing-function: var(--ease-in-out); }
}
@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*), ::view-transition-old(*), ::view-transition-new(*) { animation: none !important; }
}
/* the moves the layers share: opacity and transforms only */
@keyframes motion-fade { from { opacity: 0; } }
@keyframes motion-rise { from { opacity: 0; translate: 0 0.75rem; } }
@keyframes motion-settle { from { translate: 0 2rem; scale: 0.94; } }
/* the page's own switch, "Pause moving things", sets data-motion="paused" on <html> (WCAG 2.2.2) */
html[data-motion="paused"] body::before, html[data-motion="paused"] body::after,
html[data-motion="paused"] :is(.deco, .motion-glow, .motion-star, .motion-mote) { animation-play-state: paused; }
```

## Layers

### Pace
- Layer: pace
- Owns: the shared durations and easing curves (`--dur-short`, `--dur-medium`, `--dur-long`, `--dur-step`, `--ease-out`, `--ease-in`, `--ease-in-out`, `--ease-spring`) every other layer and every other part uses. It moves nothing itself.
- Default: brisk

#### Still
- Id: still
- Status: draft
- Looks like: nothing travels. Every hover, press, view and moment happens at once. It is what every other pace becomes when the visitor asks for less motion.
- Made with: every duration zero, every curve `linear`: the defaults above, with no pace class.

```css assemble
/* pace still: no values set, so the base's zeros stand and every change is instant */
```

- Careful: still is not broken. The states must still be drawn (a hovered button looks hovered, a chosen tab looks chosen), only without the time between. The colour part draws them.
- Light and dark: the same on both.
- Personality: serious, calm
- Goes with: `motion: feedback none`; every other layer at `none`.
- Used on: 4 mockups that move nothing but a smooth scroll to an anchor: a poetry site, a tutoring site, a quiet gallery of pots, and a repair café (whose stylesheet also turns every transition and animation off under reduced motion).

#### Brisk
- Id: brisk
- Status: draft
- Looks like: quick and plain, for getting things done. A control answers in a tenth of a second; a panel opens in under a third.
- Made with: 100, 200 and 300 ms, and Carbon's "productive" curves, which start and stop quickly (R17). NN/g's "about 100 ms" for feedback (R22).

```css assemble
@media (prefers-reduced-motion: no-preference) {
  & { --dur-short: 100ms; --dur-medium: 200ms; --dur-long: 300ms; --dur-step: 30ms;
    --ease-out: cubic-bezier(0, 0, 0.38, 0.9); --ease-in: cubic-bezier(0.2, 0, 1, 0.9);
    --ease-in-out: cubic-bezier(0.2, 0, 0.38, 0.9); --ease-spring: var(--ease-out); }
}
```

- Careful: the right pace for forms, shops and tools, and for feedback on any page. Below about 100 ms a change is not seen as motion at all, so nothing goes quicker than `--dur-short`.
- Light and dark: the same on both.
- Personality: serious, calm, friendly
- Goes with: `motion: feedback fade` or `press-in`; `motion: transitions cross-fade`.
- Used on: most mockups' feedback, without naming it: a field notebook's buttons (0.15 s), a volunteer page's cards and a soap shop's tiles (0.15 s), and a game-style joke site's emblem (0.12 s).

#### Gentle
- Id: gentle
- Status: draft
- Looks like: a little slower, with a soft landing: things arrive quickly and settle slowly into place.
- Made with: 150, 300 and 500 ms (Material 3's short3, medium2 and long2), and Material's "emphasized decelerate" curve for arriving (R16).

```css assemble
@media (prefers-reduced-motion: no-preference) {
  & { --dur-short: 150ms; --dur-medium: 300ms; --dur-long: 500ms; --dur-step: 50ms;
    --ease-out: cubic-bezier(0.05, 0.7, 0.1, 1); --ease-in: cubic-bezier(0.3, 0, 0.8, 0.15);
    --ease-in-out: cubic-bezier(0.2, 0, 0, 1); --ease-spring: var(--ease-out); }
}
```

- Careful: the decelerating curve is fast at the start, so a 500 ms entrance looks done in half that; it is the long tail that feels soft. Keep the visitor's own actions on `--dur-short`.
- Light and dark: the same on both.
- Personality: calm, friendly
- Goes with: `motion: feedback lift`; `motion: entrance rise` or `stagger`.
- Used on: a game-style joke site's swap between its two looks (a 0.5 s cross-fade).

#### Slow
- Id: slow
- Status: draft
- Looks like: unhurried. Views fade into one another, a glow grows when the main button is reached. For a few large moments, not for every press.
- Made with: 240, 400 and 700 ms, and Carbon's "expressive" curves, which it keeps for "significant moments" (R17).

```css assemble
@media (prefers-reduced-motion: no-preference) {
  & { --dur-short: 240ms; --dur-medium: 400ms; --dur-long: 700ms; --dur-step: 80ms;
    --ease-out: cubic-bezier(0, 0, 0.3, 1); --ease-in: cubic-bezier(0.4, 0.14, 1, 1);
    --ease-in-out: cubic-bezier(0.4, 0.14, 0.3, 1); --ease-spring: var(--ease-out); }
}
```

- Careful: 700 ms is the most any change of view takes; NN/g finds anything over 500 ms starts to feel like a delay (R22). A form on a slow page still answers at brisk speed: write its feedback with a brisk value in the site's guide, and say so.
- Light and dark: the same on both.
- Personality: dramatic, calm
- Goes with: `motion: entrance fade`; `motion: ambient breathing`; `motion: transitions cross-fade`.
- Used on: a dark, painterly joke site, whose glow grows over 0.6 s when the main button is reached.

#### Springy
- Id: springy
- Status: draft
- Looks like: quick, with a little bounce: a pressed thing gives and springs back past where it was, then settles. Playful without being silly.
- Made with: gentle's durations, and `--ease-spring` written as a `linear()` curve sampled from a damped spring that overshoots by about 8 per cent. `linear()` joins its points with straight lines, so a spring needs thirty or more of them; the swatch book's builder works them out (R8, R9, R20).

```css assemble
@media (prefers-reduced-motion: no-preference) {
  & { --dur-short: 150ms; --dur-medium: 300ms; --dur-long: 500ms; --dur-step: 50ms;
    --ease-out: cubic-bezier(0, 0, 0, 1); --ease-in: cubic-bezier(0.3, 0, 1, 1); --ease-in-out: cubic-bezier(0.2, 0, 0, 1);
    --ease-spring: linear(0, 0.077, 0.254, 0.464, 0.662, 0.827, 0.948, 1.026, 1.068, 1.083, 1.08, 1.067, 1.05, 1.032, 1.018, 1.007, 0.999, 0.995, 0.993, 0.993, 0.994, 0.995, 0.997, 0.998, 0.999, 1, 1, 1.001, 1.001, 1.001, 1, 1, 1); }
}
```

- Careful: overshoot only on small things the visitor touched (a button, a toggle), never on a panel or a view, where it reads as wobbling. A spring in CSS is still bound to its duration, and one that is interrupted half-way restarts rather than carrying its speed (R20). `linear()` is in every current browser (R8); an older one ignores the line and keeps `--ease-out`.
- Light and dark: the same on both.
- Personality: playful, friendly
- Goes with: `motion: feedback squeeze`; `motion: moments celebrate`.
- Used on: none yet.

### Feedback
- Layer: feedback
- Owns: what a control or a card that is a link does when it is pointed at, pressed and let go: a colour easing, a press into its shadow, a lift, a straightening, a squeeze. The colour part decides the colours of those states; this layer decides how they move.
- Default: fade

The colour part draws every state of a control (`--accent-hover` and `--accent-pressed` on the main button, and the shapes part's fill and edge when a button is cut to a shape); the options below decide how the control gets there and how it moves. The swatch book draws its states with a **veil** (a "state layer"): a `::before` in the control's own text colour, at 12 per cent when pointed at and 22 per cent when pressed, whose opacity alone changes. A site's stylesheet does not: the shapes part draws a shaped button on its `::before` and `::after`, so a veil there would paint over it. A site that wants the veil, on buttons that are plain boxes, takes it from the swatch book and says so.


#### None
- Id: none
- Status: draft
- Looks like: the pointed-at and pressed states appear at once, with nothing moving.
- Made with: the colour part's states, with no transition.

```css assemble
/* feedback none: the colour part's pointed-at and pressed colours change at once */
```

- Careful: still clear: every state is drawn. It suits pages where a press leads straight to a new page.
- Light and dark: the same on both.
- Personality: serious, calm
- Goes with: `motion: pace still`.
- Used on: a poetry site and a tutoring site (their links change colour at once).

#### Fade
- Id: fade
- Status: draft
- Looks like: a control's colour eases to its pointed-at shade, and deeper when it is pressed. The quietest feedback that still feels alive.
- Made with: the colour part's state colours (and the shapes part's fill and edge on a shaped button), over `--dur-short`. The swatch book fades a veil's opacity instead.

```css assemble
/* the colour part's state colours (and shapes' fill and edge, when a button is cut to a shape) fade over --dur-short */
.btn, .btn::before, .btn::after { transition: background-color var(--dur-short) var(--ease-out),
  border-color var(--dur-short) var(--ease-out), color var(--dur-short) var(--ease-out); }
```

- Careful: a colour transition repaints the button on every frame, where a veil's opacity would not (R6); on a button, over a tenth of a second, that is cheap. Never fade the colour of anything large, a sheet or a band.
- Light and dark: the same on both; the colour part's hover and pressed shades are worked out for each tone.
- Personality: any
- Goes with: every pace.
- Used on: a field notebook (its buttons' background over 0.15 s, which this does more cheaply).

#### Press in
- Id: press-in
- Status: draft
- Looks like: pressed, a button moves down into its own shadow and the shadow goes, like a key or a card pushed onto the board. Let go, it comes back up.
- Made with: `translate` by the light part's direction (`--lx`, `--ly`) times the low shadow's offset, over half of `--dur-short`; the shadow goes at once.

```css assemble
/* pressed, a button moves into its own shadow by the light's direction, and the shadow goes */
.btn { transition: translate calc(var(--dur-short) / 2) var(--ease-out); }
.btn:active { translate: calc(var(--lx, 0.5) * 2px) calc(var(--ly, 1) * 2px); box-shadow: none; filter: none; }
```

- Careful: it needs a shadow with an offset to press into (the light part's `shadows: crisp` or `paper-lift`). The distance is the shadow's offset, no more, or the button slides rather than presses. A pressed button in an inked frame does the same.
- Light and dark: on a dark page the shadow hardly shows, so the press reads as the button moving: still clear.
- Personality: friendly, playful
- Goes with: `light: shadows crisp`; `frames: border inked`; `motion: pace brisk`.
- Used on: 3 mockups, all at once with no duration: a repair café (`translate: 1px 2px` and a smaller shadow), a small shop with a dark lead (2px), and a game-style joke site's buttons (2px down and an inset shadow).

#### Lift
- Id: lift
- Status: draft
- Looks like: pointed at, a card or a button rises a little towards the pointer and its shadow grows; pressed, it settles back down.
- Made with: `translate` up by 3px. The swatch book also fades the light part's `--shadow-mid` in on a `::after` (R25); a site's stylesheet does not, because the frames part draws a sheet's ring on its `::after`, so the light part's own shadow stays as it is.

```css assemble
/* a card that is a link (<a class="sheet">), a button, or anything marked .motion-lift rises to the pointer */
:is(a.sheet, .btn, .motion-lift) { transition: translate var(--dur-medium) var(--ease-out); }
@media (hover: hover) { :is(a.sheet, .btn, .motion-lift):hover { translate: 0 -3px; } }
:is(a.sheet, .btn, .motion-lift):active { translate: 0 -1px; transition-duration: var(--dur-short); }
```

- Careful: only on things that are links or buttons: a card that lifts promises it can be pressed. A site that wants the shadow to grow too fades it in on an element of its own inside the card, never by animating `box-shadow`; a soap shop eased the rise but let the shadow snap, which looked uneven.
- Light and dark: on a dark page the shadow hardly shows, so the rise does the work; the light part's lighter `--surface-raised` may stand in.
- Personality: friendly, calm
- Goes with: `light: shadows soft` or `paper-lift`; `motion: pace gentle`.
- Used on: a volunteer page (event cards rise 3px over 0.15 s) and a soap shop (tiles rise 3px).

#### Straighten
- Id: straighten
- Status: draft
- Looks like: things pinned up at a slant (notes, tags, tiles) straighten when pointed at, as if a hand had set them right.
- Made with: `rotate` from the item's own slant to none, over `--dur-medium` with `--ease-spring`, so on a springy pace it settles with a wobble. In a site's stylesheet the labels (`.tag`) and anything marked `.motion-tilt` take the slant, three different ones in turn; paper the materials part already turns keeps its own slant.

```css assemble
/* labels, and anything marked .motion-tilt, hang at a small slant, each its own, and straighten when pointed at */
:is(.tag, .motion-tilt) { display: inline-block; rotate: var(--motion-tilt, -2.5deg); transition: rotate var(--dur-medium) var(--ease-spring); }
:is(.tag, .motion-tilt):nth-child(3n+2) { --motion-tilt: 1.5deg; }
:is(.tag, .motion-tilt):nth-child(3n) { --motion-tilt: -1deg; }
@media (hover: hover) { :is(.tag, .motion-tilt):hover { rotate: 0deg; } }
```

- Careful: the slant is small (one to three degrees) and differs from item to item, or they look like a mistake. Text that is read at a slant is harder to read: the slant is for short labels and pictures.
- Light and dark: the same on both.
- Personality: playful, friendly
- Goes with: the materials part's paper and tape; `motion: pace springy` or `gentle`.
- Used on: a soap shop (tiles at −1.3, 0.9 and −0.6 degrees straighten over 0.15 s).

#### Squeeze
- Id: squeeze
- Status: draft
- Looks like: pressed, a control gives a little, like a rubber key; let go, it springs back.
- Made with: `scale` to 0.94 over `--dur-short`, and back over `--dur-medium` with `--ease-spring`.

```css assemble
.btn { transition: scale var(--dur-medium) var(--ease-spring); }
.btn:active { scale: 0.94; transition-duration: var(--dur-short); transition-timing-function: var(--ease-out); }
```

- Careful: not below 0.92, or the label jumps. Good for a big round emblem or a game button; on a row of form buttons it is too much.
- Light and dark: the same on both.
- Personality: playful
- Goes with: `motion: pace springy`; the game-interface look's emblem.
- Used on: a game-style joke site in both its versions (its emblem shrinks to 0.94 and 0.92 for about a tenth of a second when tapped).

### Entrance
- Layer: entrance
- Owns: how the things on a page arrive when it opens, or when they are scrolled to.
- Default: none

Every entrance is a CSS animation that fills `backwards` and is declared inside `no-preference`, so the thing's own style is fully visible, and without the animation (reduced motion, a browser that does not run it, a picture taken later) nothing is missing. Entrances play once. They are for the first screen and for the things a page is about (the cards, the work), never for words in running text.


#### None
- Id: none
- Status: draft
- Looks like: everything is simply there when the page opens.
- Made with: nothing.

```css assemble
/* entrance none: everything is simply there when the page opens */
```

- Careful: the right choice for most pages: a page that is quick to use is quick to appear.
- Light and dark: the same on both.
- Personality: any
- Goes with: every other option.
- Used on: all 15 mockups so far.

#### Fade
- Id: fade
- Status: draft
- Looks like: the things on the page fade in together as it opens, like a slide in a darkened room.
- Made with: opacity from none, over `--dur-long`.

```css assemble
/* the sheets, panels and pictures of the bands, not one inside another, or anything marked .motion-enter, fade in together as the page opens */
@media (prefers-reduced-motion: no-preference) {
  .band :is(.sheet, .panel, .picture):not(:is(.sheet, .panel) *), .motion-enter { animation: motion-fade var(--dur-long) var(--ease-out) backwards; }
}
```

- Careful: never on text that has to be read at once (a heading, an error, a price): the first moment is when people read it. A cross-fade is the gentlest motion there is; MDN suggests it in place of larger moves (R4), but under this part's rule it still becomes instant under reduced motion.
- Light and dark: the same on both.
- Personality: calm, dramatic
- Goes with: `motion: pace slow`; `motion: ambient breathing`.
- Used on: none yet. The artistic guide notes that a published review credited several artistic sites' effect to animation on load and on scroll, which a screenshot cannot show.

#### Rise
- Id: rise
- Status: draft
- Looks like: they fade in while rising a short way into place, as if set down.
- Made with: opacity and a 0.75rem `translate`, over `--dur-long` with `--ease-out`.

```css assemble
/* the sheets, panels and pictures of the bands, not one inside another, or anything marked .motion-enter, rise a short way into place as the page opens */
@media (prefers-reduced-motion: no-preference) {
  .band :is(.sheet, .panel, .picture):not(:is(.sheet, .panel) *), .motion-enter { animation: motion-rise var(--dur-long) var(--ease-out) backwards; }
}
```

- Careful: 0.75rem, no more: things that travel far are a vestibular trigger (R24) and look like they are falling.
- Light and dark: the same on both.
- Personality: friendly, calm
- Goes with: `motion: pace gentle`; `motion: feedback lift`.
- Used on: none yet.

#### Stagger
- Id: stagger
- Status: draft
- Looks like: they rise one after another, a beat apart, like cards dealt onto a table.
- Made with: rise, with each item delayed by its place in the row times `--dur-step`. The index is the item's place among its neighbours, or set in the markup (`style="--motion-i: 2"`), and capped at six, so a long list does not keep the last item waiting.

```css assemble
/* the sheets, panels and pictures of the bands, not one inside another, or anything marked .motion-enter, rise one after another by their place among their neighbours (capped at six);
   style="--motion-i: 2" in the markup sets a place by hand */
@media (prefers-reduced-motion: no-preference) {
  .band :is(.sheet, .panel, .picture):not(:is(.sheet, .panel) *), .motion-enter { animation: motion-rise var(--dur-long) var(--ease-out) backwards;
    animation-delay: calc(min(var(--motion-i, 0), 6) * var(--dur-step)); }
}
:is(.sheet, .panel, .picture, .motion-enter):nth-child(2) { --motion-i: 1; }
:is(.sheet, .panel, .picture, .motion-enter):nth-child(3) { --motion-i: 2; }
:is(.sheet, .panel, .picture, .motion-enter):nth-child(4) { --motion-i: 3; }
:is(.sheet, .panel, .picture, .motion-enter):nth-child(5) { --motion-i: 4; }
:is(.sheet, .panel, .picture, .motion-enter):nth-child(6) { --motion-i: 5; }
:is(.sheet, .panel, .picture, .motion-enter):nth-child(n+7) { --motion-i: 6; }
```

- Careful: the last item arrives within about 0.8 s of the first, or the page feels slow. Only the first screen staggers; things further down are already in place.
- Light and dark: the same on both.
- Personality: friendly, playful
- Goes with: `motion: pace gentle` or `springy`.
- Used on: none yet.

#### Scroll reveal
- Id: scroll-reveal
- Status: draft
- Looks like: each thing settles into place as it is scrolled into view: it comes up from a little below and grows to its size. It never fades from nothing.
- Made with: a scroll-driven animation (`animation-timeline: view()`), which follows the scroll itself rather than a clock and needs no script, inside `@supports`, so a browser without it simply shows the page (R13, R14).

```css assemble
/* the sheets, panels and pictures of the bands, not one inside another, or anything marked .motion-enter, settle into place as they are scrolled into view; they move only, never fade from nothing */
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .band :is(.sheet, .panel, .picture):not(:is(.sheet, .panel) *), .motion-enter { animation: motion-settle linear both; animation-timeline: view(); animation-range: entry 0% entry 100%; }
  }
}
```

- Careful: it moves only, because a reveal that fades from nothing hides everything below the fold. The swatch book's own test caught it: with opacity in it, the cards below the first screen were invisible in a whole-page picture. Scroll-driven animations are in Chrome, Edge and Safari but not yet in Firefox (R13), so it is a finish, never something the page needs. web.dev lists scroll reveals among what reduced motion removes (R5), and it is never on a page that also moves things in the background as it scrolls (parallax, R24).
- Light and dark: the same on both.
- Personality: calm, dramatic
- Goes with: `motion: pace slow`; a gallery or a long single page of work.
- Used on: none yet; the artistic guide's review (see Fade) is the reason it is here.

### Ambient
- Layer: ambient
- Owns: motion that runs by itself, with nobody touching anything: a lamp that breathes, a flame that wavers, stars that twinkle, dust that drifts. The light part draws the lamp and the stars; this layer moves them.
- Default: none

Every ambient option is slow, small and behind the words; changes opacity or a short translate only; is declared inside `no-preference`; stops under the page's pause switch; and dips in brightness about once a second at most (rules 1 to 3).


#### None
- Id: none
- Status: draft
- Looks like: nothing moves by itself.
- Made with: nothing.

```css assemble
/* ambient none: nothing moves by itself */
```

- Careful: the professional guide's own rule: "nothing that moves by itself". Most pages.
- Light and dark: the same on both.
- Personality: any
- Goes with: every other option.
- Used on: 11 mockups.

#### Breathing
- Id: breathing
- Status: draft
- Looks like: a lamp's light slowly swells and settles, over seven seconds, like a flame in still air. The lamp itself stays; only its pool of light changes.
- Made with: the opacity of the light part's glow layer, from full to 78 per cent and back, `ease-in-out`, every 7 s. In a site's stylesheet that layer is `body::after`, where the light part screens its lamp's pool, or an element of the site's own marked `.motion-glow`.

```css assemble
/* the light part's screen layer (body::after, where its lamp's pool is drawn), or a site's own .motion-glow, swells and settles */
@keyframes motion-breathe { 50% { opacity: 0.78; } }
@media (prefers-reduced-motion: no-preference) {
  body::after, .motion-glow { animation: motion-breathe 7s ease-in-out infinite; }
}
@media (prefers-contrast: more) { body::after, .motion-glow { animation: none; } }   /* the light part turns its glows down there */
```

- Careful: animate the glow layer's opacity, never its gradient, its size or a blur: one mockup also scaled a 26rem glow, which repaints a large area for no visible gain (light R7, R12). Words never sit in the part that breathes, so their contrast does not change. It needs the pause switch: it runs for ever.
- Light and dark: on a dark page a lamp that clearly breathes; on a light page a faint warm pulse, barely seen. A light page that wants a lamp people notice needs the colour part's dark or lamplit tone first.
- Personality: calm, dramatic
- Goes with: `light: glow lamp`; `motion: pace slow` or `gentle`.
- Used on: 3 mockups, all at 7 s: a night market (the lantern's glow to 78 per cent), a small shop with a dark lead (its lantern to 55 per cent, also scaled), and a dark, painterly joke site (its glow from 45 to 80 per cent).

#### Flicker
- Id: flicker
- Status: draft
- Looks like: a flame's light wavers a little, unevenly, about once a second, as a candle does in a draught.
- Made with: the glow layer's opacity, through uneven steps between 85 and 100 per cent over 3.2 s, `linear`, so it never settles into a rhythm. Four small dips in 3.2 s.

```css assemble
/* the light part's screen layer (body::after), or a site's own .motion-glow, wavers unevenly: never below 85 per cent */
@keyframes motion-flicker { 0%, 100% { opacity: 1; } 8% { opacity: 0.9; } 14% { opacity: 1; } 30% { opacity: 0.85; } 37% { opacity: 0.96; }
  55% { opacity: 0.9; } 62% { opacity: 1; } 80% { opacity: 0.87; } 88% { opacity: 0.97; } }
@media (prefers-reduced-motion: no-preference) {
  body::after, .motion-glow { animation: motion-flicker 3.2s linear infinite; }
}
@media (prefers-contrast: more) { body::after, .motion-glow { animation: none; } }
```

- Careful: the most dangerous option. A flicker that dips deep or fast becomes a flash: never below 85 per cent, never more than about one dip a second, and only on a small light, never on the page or a large area (WCAG 2.3.1, R3). The swatch book's test counts the dips.
- Light and dark: on a dark page a living flame; on a light page hardly visible, which is right.
- Personality: dramatic
- Goes with: `light: glow lamp`; `motion: pace slow`.
- Used on: none yet; the sorcery guide names it ("a glow that breathes, a flicker ... slow, small, and stops under the reduced-motion setting. Nothing flashes"), and its one mockup breathed instead.

#### Twinkle
- Id: twinkle
- Status: draft
- Looks like: a few stars, or sparkles on gold, dim and brighten slowly, each in its own time, so the sky never pulses as one.
- Made with: each star's opacity from full to 40 per cent and back, over 5 s or 7 s, `ease-in-out`, with its own negative delay, so they start part-way through. The stars are the page's own small elements marked `.motion-star`; this part moves them and does not draw them.

- Needs markup: the stars or sparkles themselves, the page's own small drawn elements (`aria-hidden="true"`), each with `class="motion-star"`; this part moves them and draws none.

```css assemble
/* each star or sparkle the page draws as a .motion-star dims and brightens in its own time */
@keyframes motion-twinkle { to { opacity: 0.4; } }
@media (prefers-reduced-motion: no-preference) {
  .motion-star { animation: motion-twinkle var(--motion-d, 5s) ease-in-out var(--motion-o, 0s) infinite alternate; }
}
.motion-star:nth-child(3n) { --motion-d: 7s; }
.motion-star:nth-child(2n) { --motion-o: -2.5s; }
.motion-star:nth-child(5n+1) { --motion-o: -4s; }
```

- Careful: a handful of stars, not hundreds; small ones; and never all in step, or the sky blinks.
- Light and dark: on a dark page stars; on a light page small warm specks that come and go, quieter.
- Personality: calm, playful
- Goes with: `light: sky night` or `by-the-clock`; `motion: clock real-time`.
- Used on: an observatory (its stars from 1 to 0.45 over 5 s, every third one over 7 s, all inside `no-preference`).

#### Drift
- Id: drift
- Status: draft
- Looks like: motes of dust drift slowly across the light, behind the words, as in a beam through a window.
- Made with: each mote's `translate` by about 2.5rem and back over 30 to 42 seconds, each with its own delay. The motes are the page's own small elements marked `.motion-mote`.

- Needs markup: the motes themselves, the page's own small drawn elements (`aria-hidden="true"`), each with `class="motion-mote"`, behind the words.

```css assemble
/* each mote the page draws as a .motion-mote drifts about 2.5rem and back, slowly, behind the words */
@keyframes motion-drift { to { translate: 2.5rem -0.75rem; } }
@media (prefers-reduced-motion: no-preference) {
  .motion-mote { animation: motion-drift var(--motion-d, 34s) ease-in-out var(--motion-o, 0s) infinite alternate; }
}
.motion-mote:nth-child(3n) { --motion-d: 42s; }
.motion-mote:nth-child(3n+1) { --motion-d: 30s; --motion-o: -11s; }
```

- Careful: tiny and few. Large things drifting, or layers drifting at different speeds, are the parallax that makes people sick (R15, R24). Nothing drifts across words.
- Light and dark: on a dark page specks in the light; on a light page darker specks from the shared texture colour, faint.
- Personality: calm, dramatic
- Goes with: `light: glow lamp` or `focus spotlight`; the background part's texture.
- Used on: none yet.

### Clock
- Layer: clock
- Owns: change at the speed of a clock: a sky that follows the real hour, a game's own day. The light part decides what each hour looks like; this layer decides how the page gets from one to the next.
- Default: none

#### None
- Id: none
- Status: draft
- Looks like: the page looks the same at every hour.
- Made with: nothing.

```css assemble
/* clock none: the page looks the same at every hour */
```

- Careful: anything that must look the same in every picture (a shop's products) has no clock.
- Light and dark: the same on both.
- Personality: any
- Goes with: every other option.
- Used on: 13 mockups.

#### Real time
- Id: real-time
- Status: draft
- Looks like: the sky follows the real hour: the sun climbs and sets, the moon comes up, and the visitor never sees it move.
- Made with: a script that repaints once a minute, with no transition, and places the sun or moon with `translate` (never `left` and `top`, which move the layout). Each repaint changes the page by less than a hundredth, so it is not motion and goes on under reduced motion (light R11). The light part's "by the clock" holds the sky's colours, sunrise and sunset, and the `?t=21:40` way to set the hour for pictures.

- Needs markup: the drawn sun or moon with `class="motion-sun"` in its sky, and the site's own clock script setting `--motion-x` and `--motion-y` on it once a minute (the light part's "by the clock" sets the sky's colours).

```css assemble
/* the sun or moon (.motion-sun) is placed by the clock's script once a minute through --motion-x and --motion-y
   (per cent of its sky), with no transition: it is not motion, so it goes on under reduced motion */
.motion-sun { translate: calc(var(--motion-x, 50) * 1%) calc(var(--motion-y, 20) * 1%); }
```

- Careful: never animate the change between two repaints: a sky that visibly slides is motion, and stops under reduced motion. A "show me the day" button that runs the hours quickly is motion too: it is checked against reduced motion and is over in a few seconds.
- Light and dark: the light part's: the sky changes, the sheets with words never.
- Personality: calm, playful
- Goes with: `light: sky by-the-clock`; `motion: ambient twinkle`.
- Used on: an observatory (the visitor's own sky, a time field and `?t=`; its sun and moon placed with `left` and `top`, which this option replaces with `translate`).

#### Game time
- Id: game-time
- Status: draft
- Looks like: a clock of the page's own, faster than the real one: a game minute every real second, so a game day passes in 24 minutes, with its time shown in words.
- Made with: one `requestAnimationFrame` or one-second loop that counts game time from the real time passed, capped so a tab left in the background does not jump a week, and repaints the words and the sky. A "Hold it still" button stops it (WCAG 2.2.2, R2), and the page's pause switch holds it too.

- Needs markup: the drawn sun or moon with `class="motion-sun"`, the site's own game-clock script that sets `--motion-x` and `--motion-y`, and a "Hold it still" button.

```css assemble
/* as real time, set each game minute by the game clock's script; no transition */
.motion-sun { translate: calc(var(--motion-x, 50) * 1%) calc(var(--motion-y, 20) * 1%); }
```

- Careful: the time and the things it changes are information, not decoration, so the clock goes on under reduced motion; what stops is everything drawn moving in it (the creatures, the 3D scene), which shows one still picture with a "Watch it move" button. Pause it when the page is hidden or off screen.
- Light and dark: as real time.
- Personality: playful
- Goes with: `light: sky by-the-clock`; a game.
- Used on: a 3D ant-farm game (one real second is one colony minute; under reduced motion one still picture, with "Watch it move" and "Hold it still").

### Transitions
- Layer: transitions
- Owns: how one view changes to another: a tab, a step in a form, a filter, a whole page.
- Default: none

Every option but none uses the browser's View Transitions: `document.startViewTransition(update)` for a change inside the page, which every current browser has (R10), and `@view-transition { navigation: auto; }` between pages of the same site, which Chrome, Edge and Safari have and Firefox does not yet (R11, R12). Without them the change happens at once, which is always acceptable. Only the thing that changes takes part: give it a `view-transition-name` for the moment of the change, and the page root none, so the rest of the page is not photographed and faded with it.


#### None
- Id: none
- Status: draft
- Looks like: one view replaces the other at once.
- Made with: the update, with no view transition.

```css assemble
/* transitions none: the script makes the change with no view transition */
```

- Careful: never "fade out, then swap, then fade in": one mockup took its whole page to nothing for 0.3 s each way when changing looks, so the screen went blank. A change is either instant or a cross-fade, where something is always there.
- Light and dark: the same on both.
- Personality: any
- Goes with: every other option.
- Used on: 13 mockups.

#### Cross-fade
- Id: cross-fade
- Status: draft
- Looks like: the old view fades out as the new one fades in, in the same place; if they differ in size, the box eases between them.
- Made with: the view transition's own default, timed by the pace.

- Needs markup: none in the page; the site's script puts `class="motion-changing"` on the one view that changes, for the moment of the change, inside `document.startViewTransition()`.

```css assemble
/* the script puts .motion-changing on the one view that changes, for the moment of the change; the browser cross-fades it */
.motion-changing { view-transition-name: motion-view; }
```

- Careful: the gentlest change of view, and the one MDN suggests in place of sliding (R4). Keep text in both views on solid ground, so it is never two layers of half-faded words for long.
- Light and dark: the same on both.
- Personality: any
- Goes with: every pace.
- Used on: a game-style joke site (its two looks, stacked in one grid cell, cross-fade over 0.5 s).

#### Slide
- Id: slide
- Status: draft
- Looks like: the new view comes in a short way from the side it lies on (the next tab from the right, the last one from the left) while the old one leaves the other way, both fading.
- Made with: the old and new pictures of the view transition, each moving 1.5rem and fading; the direction is `--motion-dir` on `<html>`, set by the script from the order of the views.

- Needs markup: none in the page; the site's script puts `class="motion-changing"` on the view that changes and sets `--motion-dir` (1 or -1) on `<html>`.

```css assemble
/* as cross-fade, and the old and new views move 1.5rem each way; the script sets --motion-dir (1 or -1) on <html>
   from the order of the views */
@keyframes motion-out { to { opacity: 0; translate: calc(var(--motion-dir, 1) * -1.5rem) 0; } }
@keyframes motion-in { from { opacity: 0; translate: calc(var(--motion-dir, 1) * 1.5rem) 0; } }
.motion-changing { view-transition-name: motion-view; }
@media (prefers-reduced-motion: no-preference) {
  ::view-transition-old(motion-view) { animation-name: motion-out; }
  ::view-transition-new(motion-view) { animation-name: motion-in; }
}
```

- Careful: 1.5rem, not the width of the screen: a whole view crossing the screen sideways is the peripheral motion that triggers vestibular symptoms (R15). It shows where the new view is, so use it only where the views have an order (tabs, steps), never for a dialog.
- Light and dark: the same on both.
- Personality: friendly, calm
- Goes with: a form in steps; tabs.
- Used on: none yet.

#### Grow
- Id: grow
- Status: draft
- Looks like: the thing chosen (a card in a list) grows into its own view, and shrinks back into its place on the way back, so the visitor sees where it came from.
- Made with: the same `view-transition-name` on the small card before the change and on the large view after it; the browser moves and sizes one into the other.

- Needs markup: none in the page; the site's script puts `class="motion-chosen"` on the card before the change and on the detail view after it.

```css assemble
/* the script puts .motion-chosen on the card before the change and moves it to the detail view after:
   one element at a time, or the transition is skipped */
.motion-chosen { view-transition-name: motion-item; }
```

- Careful: the name must be on exactly one element at a time, or the transition is skipped. The growing box is the group's own animation, which changes its size; keep it to a card into a panel on the same screen, not a card into a whole page, which is a zoom (R15).
- Light and dark: the same on both.
- Personality: calm, playful
- Goes with: a gallery; a list of items.
- Used on: none yet.

### Moments
- Layer: moments
- Owns: the motion that marks something done or something to notice: a name written onto a sheet, a small party on success, a secret look arriving, a nudge towards the next step.
- Default: none

A moment always comes with words that say the same thing (a status message in a live region), so a visitor who sees no motion, or no screen, misses nothing. It plays once, when it happens, and never loops.

#### None
- Id: none
- Status: draft
- Looks like: something done is shown in words, with no motion: the name is on the sheet, the message says thank you.
- Made with: the change and a `role="status"` message.

```css assemble
/* moments none: a role="status" message says it, with no motion */
```

- Careful: the words carry it; on most pages that is enough.
- Light and dark: the same on both.
- Personality: any
- Goes with: every other option.
- Used on: most mockups' forms.

#### Write in
- Id: write-in
- Status: draft
- Looks like: a name added to the sign-up sheet is written in from left to right, as if by a pen, then stays.
- Made with: a cover over the new name in the sheet's own colour (`--surface`), shrinking towards the right with `scale` over two and a half times `--dur-long`. The cover is only added by the script that adds the name, and only when motion is allowed, so the name is never hidden otherwise.

- Needs markup: none in the page; the script that adds a name gives it `class="motion-writing"` when motion is allowed and removes it on `animationend`.

```css assemble
/* the script that adds a name gives it .motion-writing (only when motion is allowed) and takes it off on animationend */
@keyframes motion-unwrite { to { scale: 0 1; } }
.motion-writing { position: relative; display: inline-block; }
@media (prefers-reduced-motion: no-preference) {
  .motion-writing::after { content: ""; position: absolute; inset: -2px -3px; background: var(--surface); transform-origin: 100% 50%;
    animation: motion-unwrite calc(var(--dur-long) * 2.5) var(--ease-in-out) forwards; }
}
```

- Careful: the cover must be the colour of what is behind the name exactly, or a box shows; on a textured sheet, a `mask-image` gradient moved with `translate` does the same. Remove the class when it ends (`animationend`).
- Light and dark: the same on both: the cover takes the sheet's colour in either tone.
- Personality: friendly, playful
- Goes with: the lettering part's handwriting; the materials part's paper.
- Used on: a repair café (the new name is added in red and focus moves to the thanks; it is not yet written in).

#### Celebrate
- Id: celebrate
- Status: draft
- Looks like: once, on success, a handful of paper pieces burst from the button and fall away, in the site's colours.
- Made with: about a dozen small elements, made by the script, each moved with the Web Animations API (`translate`, `rotate`, `opacity`) over 0.9 s, then removed. Colours from the shared names (`--accent`, `--band-1`, `--band-2`, `--mark`).

- Needs markup: a positioned container for the pieces (the done message's sheet); the site's script adds a dozen `<i class="motion-bit" aria-hidden="true">` to it, moves them and removes them.

```css assemble
/* a dozen .motion-bit pieces, made, placed and moved by the script with the Web Animations API, only when motion is allowed;
   each takes a colour from --accent, --band-1, --band-2 and --mark, and is removed at the end */
.motion-bit { position: absolute; width: 0.5rem; height: 0.75rem; pointer-events: none; }
.motion-bit:nth-child(4n) { background: var(--accent); } .motion-bit:nth-child(4n+1) { background: var(--band-1); }
.motion-bit:nth-child(4n+2) { background: var(--band-2); } .motion-bit:nth-child(4n+3) { background: var(--mark); }
```

- Careful: once, small, from the button, over in under a second; never full-screen confetti, never on a page that is about something sad (a donation after a death, a complaint). The words "You are signed up" carry it.
- Light and dark: the pieces take the band colours, which show on both.
- Personality: playful, friendly
- Goes with: `motion: pace springy`; a sign-up, a booking, an order.
- Used on: a volunteer page (a hand waves four times over 2 s on the done screen, then stops).

#### Secret swap
- Id: secret-swap
- Status: draft
- Looks like: a secret code (or ten taps on the emblem) swaps the whole look, the old cross-fading into the new.
- Made with: a view transition on the part that changes, over 1.6 times `--dur-long`; the rest of the general guide's "A site with two looks".

- Needs markup: none in the page; the site's script puts `class="motion-look"` on the part that changes for the moment of the swap.

```css assemble
/* the script puts .motion-look on the part that changes for the moment of the swap, then toggles the second look */
.motion-look { view-transition-name: motion-look; }
@media (prefers-reduced-motion: no-preference) {
  ::view-transition-group(motion-look), ::view-transition-old(motion-look), ::view-transition-new(motion-look) { animation-duration: calc(var(--dur-long) * 1.6); }
}
```

- Careful: a cross-fade, never a fade to nothing and back (see transitions none). Say it in a live region on the way in. Keep the visitor's place on the page: one mockup scrolled to the top on swap, which loses them.
- Light and dark: the two looks may differ in tone; the cross-fade is the same.
- Personality: playful, dramatic
- Goes with: the game-interface look; `motion: transitions cross-fade`.
- Used on: 2 versions of a game-style joke site (the Konami code or ten taps; one cross-faded over 0.5 s, the other faded the page out and in over 0.3 s each way).

#### Nudge
- Id: nudge
- Status: draft
- Looks like: a ring pulses out twice round the next thing to press, then stops: a tap on the shoulder, once.
- Made with: a `::after` ring that grows to 1.3 times and fades, twice, over 1.2 s each. Under reduced motion the ring is shown still for three seconds instead.

- Needs markup: none in the page; the site's script adds `<span class="motion-ring" aria-hidden="true"></span>` inside the next thing to press and removes it after 2.4 s.

```css assemble
/* the script adds an empty <span class="motion-ring"> inside the next thing to press (a button is already
   position: relative) and removes it after 2.4 s, or after 3 s under reduced motion, where it stands still */
@keyframes motion-ring { from { opacity: 0.9; scale: 1; } to { opacity: 0; scale: 1.3; } }
.motion-ring { position: absolute; inset: -7px; border: 3px solid var(--accent-edge); pointer-events: none;
  border-radius: calc(var(--radius-control, var(--radius, 6px)) + 7px); }
@media (prefers-reduced-motion: no-preference) {
  .motion-ring { animation: motion-ring 1.2s var(--ease-out) 2 forwards; }
}
```

- Careful: twice and stop. A pulse that never stops is a nag, and must be pausable (2.2.2). One thing at a time. It is not the focus ring and never replaces it.
- Light and dark: the ring is `--accent-edge`, which stands off both.
- Personality: friendly, playful
- Goes with: a basket ready to check out; the next step in a form.
- Used on: none yet.

## What the visitor's settings switch off

Every option keeps these, and the swatch book has them:

All of it is under "Base": every duration zero unless the visitor's device allows motion, no view transition under reduced motion, and the page's own switch (`data-motion="paused"` on `<html>`) pausing everything that moves by itself.

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
if (!reduce.matches && document.startViewTransition) document.startViewTransition(update); else update();
```

Under reduced motion nothing in this part moves except the clocks, whose steps are too small to see (real time) or are information (game time). Smooth scrolling to an anchor (`scroll-behavior: smooth`) is set inside `no-preference` too; seven mockups did, and the skill's own viewer is the one place found that scrolls smoothly whatever the setting.

## Starting points

### None
- Id: none
- Picks: pace: still; feedback: none
- Personality: serious, calm
- Looks like: nothing moves. Every hover, press and change is instant; every state is still drawn. A page that feels like paper.
- Used on: a poetry site, a tutoring site and a quiet gallery of pots, whose only motion is a smooth scroll to an anchor.

### Professional
- Id: professional
- Picks: pace: brisk; feedback: fade; transitions: cross-fade
- Personality: serious, calm
- Looks like: quick, plain answers: a colour that eases on what is pointed at, views that cross-fade in a third of a second, nothing that moves by itself.
- Used on: the professional guide ("nothing that moves by itself, no pop-ups, no countdowns") and a field notebook's 0.15 s buttons.

### Warm
- Id: warm
- Picks: pace: gentle; feedback: lift; entrance: rise; moments: celebrate
- Personality: friendly, calm
- Looks like: cards lift towards the hand, the first screen settles into place, and a small party, once, when you sign up.
- Used on: a volunteer page (cards that rise 3px, a hand that waves on the done screen) and the warm guide ("movement, if any, stops under the reduced-motion setting").

### Artistic
- Id: artistic
- Picks: pace: slow; feedback: fade; entrance: scroll-reveal; transitions: cross-fade
- Personality: calm, dramatic
- Looks like: unhurried: work settles into place as you scroll to it, and views fade slowly into one another.
- Used on: the artistic guide, whose review credited artistic sites' effect to motion on load and on scroll; no mockup yet.

### Sorcery
- Id: sorcery
- Picks: pace: slow; feedback: fade; entrance: fade; ambient: breathing; transitions: cross-fade
- Personality: dramatic
- Looks like: a dark, slow room with one lamp that breathes; things fade in out of the dark.
- Used on: the sorcery guide (light that moves is "slow, small, and stops under the reduced-motion setting") and a dark, painterly joke site (a glow that breathes over 7 s and grows when the main button is reached).

### Gilded dark
- Id: gilded-dark
- Picks: pace: brisk; feedback: squeeze; ambient: twinkle; transitions: cross-fade; moments: secret-swap
- Personality: playful, dramatic
- Looks like: quick, solid game controls that give when pressed, a few sparkles, and a secret second look behind a code.
- Used on: the game-interface guide ("moving glows and sparkles are small, slow, and stop under the reduced-motion setting") and a game-style joke site in both its versions.

### Lantern fair
- Id: lantern-fair
- Picks: pace: gentle; feedback: lift; entrance: stagger; ambient: breathing
- Personality: dramatic, friendly
- Looks like: one paper lantern breathing over a market at night, the stalls coming in one by one.
- Used on: a night market (the lantern's glow breathing over 7 s) and a small shop with a dark lead (its lantern the same).

### Almanac plate
- Id: almanac-plate
- Picks: pace: gentle; feedback: fade; ambient: twinkle; clock: real-time
- Personality: calm, serious
- Looks like: printed charts under the visitor's own sky, the sun and moon in their real places, a few stars twinkling at night.
- Used on: an observatory (twinkling stars, a sky repainted once a minute, `?t=` to set the hour).

### Repair cafe
- Id: repair-cafe
- Picks: pace: brisk; feedback: press-in; entrance: none; moments: write-in
- Personality: playful, friendly
- Looks like: cut-card buttons that press into their hard shadows, and your name written onto the sign-up sheet.
- Used on: a repair café (buttons that press 1px 2px into their shadow; a new name added to the sheet).

## Swatch book

`tests/parts/motion.html` shows every option of every layer, then every starting point, each on a light page and on a dark one side by side. Motion cannot be seen in a picture, so each swatch has two halves: a live demonstration, which plays from its **Play** button (loops are already running), and under it the same motion **drawn stopped** at three or four moments, worked out by the builder from the same durations and curves, so a screenshot shows what the option does. The pace swatches draw their curves (arriving solid, leaving dashed), their three durations to scale, and faint dots where each runner is every 50 ms. Nothing plays on its own as the page opens: `audit` measures a page 0.4 s after it opens, and text still fading in then cannot be measured (the first version of this book had 232 such pieces of text). A switch at the top, "Pause moving things", is the pause every page with an ambient layer needs.

Its test proves the rules in the page, after `swatchTest()`:

1. no rule in the page hides content with `opacity: 0`, and with every motion class off, every word in every swatch is fully drawn;
2. every animation and transition moves only opacity, translate, scale, rotate or transform;
3. every loop dips in brightness three times a second or less, and stops when the switch is pressed;
4. then, with reduced motion switched on (`real('motion', 'reduce')`), every swatch's Play is pressed, and nothing is running with a duration, no transition has a duration, no view transition runs, and every word is fully drawn at once. It switches back afterwards.

The swatch book's classes stand in for a site's: `.card` for a sheet that is a link, `.enter` for what arrives, `.glow` for the light's screen layer, `.star`, `.mote`, `.sun`, `.who.writing` and `.bit` for the part's own `.motion-…` classes; the code lifted into a site is each option's ` ```css assemble ` block and "Base". It is built by `tests/parts/source/motion.py` from `motion-template.html` beside it; run `python3 motion.py ../motion.html` there to rebuild it. The page writes the layer classes short (`pa-brisk` for `motion-pace-brisk`, and `fe-`, `en-`, `am-`, `cl-`, `tr-`, `mm-` for the others), and stands in for the light part's values (`--lx`, `--ly`, `--shadow-low`, `--shadow-mid`, `--lamp`) with its defaults.

## Not covered yet

- **Loading.** Spinners, skeletons and progress bars are motion that does a job (web.dev keeps them under reduced motion, R5); no mockup has had to wait for anything real.
- **Motion in canvas and 3D.** The three and pixi library pages cover a scene that moves; the ant game's still picture and "Watch it move" button is the pattern. This part covers the page around them.
- **Cross-document view transitions between real pages.** The mockups are single pages; the rule (`@view-transition { navigation: auto; }`, root cross-fade, in Chrome and Safari only) is untried.
- **Gestures.** Swiping, dragging and pull to refresh, and the motion that follows the finger.
- **Sound.** A moment with a sound is a different kind of thing, and off by default.
- **Entrances and `audit`.** `audit` measures contrast 0.4 s after a page opens, while a `slow` or staggered entrance is still fading in, so the words are listed as unmeasured. Until `audit` waits for finite animations to finish, a site with an entrance checks its first screen by eye, or with the viewer's Checks tab.
- **Picturing motion in checks.** `check` and `audit` see one moment; the swatch book proves its rules with its own test, but a site's pages do not have one. An audit step that switches on reduced motion and looks for running animations, and one that flags animated layout properties, would carry the rules to every page.

## Sources

Read on 2026-10-07. Six kinds of source: the standard (R1 to R3), the web platform's own references (R4 to R14), design systems (R16 to R19), craft writing by people who make interfaces (R20, R21, R25), research (R22, R23), and the accessibility community on motion sensitivity (R15, R24). The mockups made with the skill are the seventh: their CSS and scripts are quoted in each option's "Used on". Pages that would not open: Material 3's token page (its values are from Material's own token file, R16) and Apple's guidelines page (quoted from a mirror of it, R18); Apple gives no durations in milliseconds.

- R1 WCAG 2.2, Understanding 2.3.3 Animation from Interactions (motion from interaction can be disabled unless essential; vestibular disorders; `prefers-reduced-motion` an accepted technique): w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
- R2 WCAG 2.2, Understanding 2.2.2 Pause, Stop, Hide (moving, blinking or scrolling that starts by itself, lasts more than five seconds and sits beside other content needs a way to pause, stop or hide it): w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html
- R3 WCAG 2.2, Understanding 2.3.1 Three Flashes or Below Threshold: w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html
- R4 MDN, prefers-reduced-motion (scaling and panning large objects are vestibular triggers; a dissolve in place of scaling, a cross-fade in place of panning): developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
- R5 web.dev, prefers-reduced-motion (remove decorative motion, or animate only inside no-preference; keep motion that does a job, such as a sent form or a loading indicator; drop parallax and scroll reveals): web.dev/articles/prefers-reduced-motion
- R6 web.dev, how to create high-performance CSS animations (animate transform and opacity; `top` and `left` dropped 50% of frames in its test against 1% for `translate`): web.dev/articles/animations-guide
- R7 web.dev, optimize Cumulative Layout Shift ("composited animations using translate can't impact other elements, and so don't count toward CLS"): web.dev/articles/optimize-cls
- R8 MDN, the `linear()` easing function (Baseline since December 2023): developer.mozilla.org/en-US/docs/Web/CSS/easing-function/linear
- R9 Chrome for Developers, creating complex animation curves with `linear()` (springs and bounces as points; the Linear Easing Generator): developer.chrome.com/docs/css-ui/css-linear-easing-function
- R10 web.dev, same-document view transitions are Baseline Newly available (Firefox 144, October 2025): web.dev/blog/same-document-view-transitions-are-now-baseline-newly-available
- R11 caniuse, cross-document view transitions (Chrome and Edge 126, Safari 18.2; Firefox not yet): caniuse.com/cross-document-view-transitions
- R12 Chrome for Developers, cross-document view transitions (`@view-transition { navigation: auto; }`): developer.chrome.com/docs/web-platform/view-transitions/cross-document
- R13 MDN, animation-timeline (limited availability: Chrome and Edge 115, Safari 26; not in stable Firefox): developer.mozilla.org/en-US/docs/Web/CSS/animation-timeline
- R14 Chrome for Developers, scroll-driven animations (`view()` and `animation-range`): developer.chrome.com/docs/css-ui/scroll-driven-animations
- R15 WebKit, responsive design for motion (triggers: scaling and zooming, spinning, multi-speed or multi-direction motion such as parallax, planes moving in 3D, peripheral motion, animated blur): webkit.org/blog/7551/responsive-design-for-motion/
- R16 Material Design 3 motion tokens (durations short1 to extra-long4, 50 to 1000 ms; standard `cubic-bezier(0.2, 0, 0, 1)`, emphasized decelerate `(0.05, 0.7, 0.1, 1)`, emphasized accelerate `(0.3, 0, 0.8, 0.15)`), from Material's token file: raw.githubusercontent.com/material-components/material-web/main/tokens/versions/v0_192/_md-sys-motion.scss and m3.material.io/styles/motion/easing-and-duration/tokens-specs
- R17 IBM Carbon, motion (productive motion for tasks, expressive for significant moments; standard, entrance and exit curves for each; durations 70 to 700 ms): carbondesignsystem.com/elements/motion/overview/
- R18 Apple Human Interface Guidelines, motion ("Add motion purposefully ... Don't add motion for the sake of adding motion"; never the only way to convey information; with Reduce Motion on, "minimize or eliminate animations"): developer.apple.com/design/human-interface-guidelines/motion
- R19 Apple, reduced motion evaluation criteria (scaling, spinning and peripheral motion as triggers): developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria
- R20 Josh Comeau, springs and bounces in native CSS (`linear()` needs 40 or so points for a convincing spring; still bound to a duration; an interrupted spring does not carry its speed): joshwcomeau.com/animation/linear-timing-function/
- R21 Tatiana Mac, "no-motion-first" (`animation: none` by default, motion added only inside `no-preference`): tatianamac.com/posts/prefers-reduced-motion
- R22 Nielsen Norman Group, executing UX animations: duration and motion characteristics ("most animations should be in the range of 100-500 ms"; about 100 ms for simple feedback; exits shorter than entrances): nngroup.com/articles/animation-duration/
- R23 Nielsen Norman Group, the role of animation and motion in UX (feedback, state change, navigation, signifiers; "subtle, unobtrusive, and brief"): nngroup.com/articles/animation-purpose-ux/
- R24 Val Head, A List Apart, designing safer web animation for motion sensitivity (large areas of motion, parallax, scroll-jacking, zooms over a large space, things travelling far, motion against the scroll): alistapart.com/article/designing-safer-web-animation-for-motion-sensitivity/
- R25 Tobias Ahlin, how to animate box-shadow (fade a pseudo-element's shadow in with opacity, rather than animating the shadow): tobiasahlin.com/blog/how-to-animate-box-shadow/
