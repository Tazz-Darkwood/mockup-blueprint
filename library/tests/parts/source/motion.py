"""Builds the motion swatch book (../motion.html) from motion-template.html beside this file.

Motion cannot be seen in a picture, so every swatch has two halves: a live demonstration (it plays once when the page
opens, and again from its Play button), and a strip of still frames drawn here, from the same timings and easing curves,
so a screenshot shows what the motion does. The pace swatches draw their easing curves and durations instead.
It writes one swatch for each option of each layer (the other layers at their defaults), then one for each starting
point, in the guide's order. Run from this folder:
    python3 motion.py ../motion.html"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).parent

DEFAULTS = {"pace": "brisk", "feedback": "fade", "entrance": "none", "ambient": "none", "clock": "none",
            "transitions": "none", "moments": "none"}
SHORT = {"pace": "pa", "feedback": "fe", "entrance": "en", "ambient": "am", "clock": "cl", "transitions": "tr", "moments": "mm"}

# the pace values, the same as the guide's: durations in ms and the three curves as cubic-bezier numbers
PACES = {
    "still":   {"dur": (0, 0, 0), "step": 0, "out": None, "in": None, "inout": None},
    "brisk":   {"dur": (100, 200, 300), "step": 30, "out": (0, 0, 0.38, 0.9), "in": (0.2, 0, 1, 0.9), "inout": (0.2, 0, 0.38, 0.9)},
    "gentle":  {"dur": (150, 300, 500), "step": 50, "out": (0.05, 0.7, 0.1, 1), "in": (0.3, 0, 0.8, 0.15), "inout": (0.2, 0, 0, 1)},
    "slow":    {"dur": (240, 400, 700), "step": 80, "out": (0, 0, 0.3, 1), "in": (0.4, 0.14, 1, 1), "inout": (0.4, 0.14, 0.3, 1)},
    "springy": {"dur": (150, 300, 500), "step": 50, "out": (0, 0, 0, 1), "in": (0.3, 0, 1, 1), "inout": (0.2, 0, 0, 1)},
}


def bezier(p, x):
    """y at x on a CSS cubic-bezier(p): solve for t by bisection, then evaluate y."""
    if p is None:
        return 1.0 if x > 0 else 0.0
    x1, y1, x2, y2 = p
    lo, hi = 0.0, 1.0
    for _ in range(40):
        t = (lo + hi) / 2
        bx = 3 * (1 - t) ** 2 * t * x1 + 3 * (1 - t) * t * t * x2 + t ** 3
        lo, hi = (t, hi) if bx < x else (lo, t)
    t = (lo + hi) / 2
    return 3 * (1 - t) ** 2 * t * y1 + 3 * (1 - t) * t * t * y2 + t ** 3


def spring(t, zeta=0.62, turns=2.2):
    """A damped spring from 0 to 1, overshooting about 8 per cent, settled by t = 1."""
    w = 2 * math.pi * turns
    wd = w * math.sqrt(1 - zeta * zeta)
    return 1 - math.exp(-zeta * w * t) * (math.cos(wd * t) + zeta * w / wd * math.sin(wd * t))


SPRING_POINTS = [round(spring(i / 32), 3) for i in range(33)]
SPRING_POINTS[-1] = 1
SPRING = "linear(" + ", ".join(f"{v:g}" for v in SPRING_POINTS) + ")"


def ease_of(pace, which="out"):
    if pace == "springy" and which == "spring":
        return lambda x: spring(x)
    p = PACES[pace][which if which != "spring" else "out"]
    return lambda x: bezier(p, x)


# ---------------------------------------------------------------- the options, in the guide's order
LAYERS = {
    "pace": [
        ("still", "Still", "Nothing travels: every change is instant. What reduced motion turns any pace into."),
        ("brisk", "Brisk", "Quick and plain, for getting things done: 100, 200 and 300 ms."),
        ("gentle", "Gentle", "A little slower, with a soft landing: 150, 300 and 500 ms."),
        ("slow", "Slow", "Unhurried, for a few big moments: 240, 400 and 700 ms."),
        ("springy", "Springy", "Quick, with a small overshoot that settles, like a spring."),
    ],
    "feedback": [
        ("none", "None", "The pointed-at and pressed states change at once."),
        ("fade", "Fade", "A light veil fades in when pointed at, and deepens when pressed."),
        ("press-in", "Press in", "Pressed, the button moves into its own shadow."),
        ("lift", "Lift", "Pointed at, the card rises a little and its shadow grows."),
        ("straighten", "Straighten", "Things pinned up at a slant straighten when pointed at."),
        ("squeeze", "Squeeze", "Pressed, it gives a little, and springs back when let go."),
    ],
    "entrance": [
        ("none", "None", "Everything is simply there when the page opens."),
        ("fade", "Fade", "The things on the page fade in together."),
        ("rise", "Rise", "They fade in while rising a short way into place."),
        ("stagger", "Stagger", "They rise one after another, a beat apart."),
        ("scroll-reveal", "Scroll reveal", "Each settles into place as it is scrolled into view, never fading from nothing."),
    ],
    "ambient": [
        ("none", "None", "Nothing moves by itself."),
        ("breathing", "Breathing", "A lamp's light swells and settles over seven seconds."),
        ("flicker", "Flicker", "A flame's light wavers a little, unevenly, about once a second."),
        ("twinkle", "Twinkle", "A few stars dim and brighten slowly, each in its own time."),
        ("drift", "Drift", "Motes of dust drift slowly across, behind the words."),
    ],
    "clock": [
        ("none", "None", "The page looks the same at every hour."),
        ("real-time", "Real time", "The sky follows the real hour, repainted once a minute with no transition."),
        ("game-time", "Game time", "A faster clock of its own: a game minute every real second, with a way to hold it."),
    ],
    "transitions": [
        ("none", "None", "One view replaces the other at once."),
        ("cross-fade", "Cross-fade", "The old view fades out as the new one fades in."),
        ("slide", "Slide", "The new view comes a short way in from the side it lies on."),
        ("grow", "Grow", "The thing chosen grows into its own view."),
    ],
    "moments": [
        ("none", "None", "Something done is shown in words, with no motion."),
        ("write-in", "Write in", "A name added to the sheet is written in, left to right."),
        ("celebrate", "Celebrate", "Once, on success, a handful of paper pieces burst and fall."),
        ("secret-swap", "Secret swap", "A secret code swaps the whole look, cross-fading."),
        ("nudge", "Nudge", "A ring pulses twice round the next thing to press, then stops."),
    ],
}

STARTS = [
    ("none", "None", {"pace": "still", "feedback": "none"}, "Nothing moves at all."),
    ("professional", "Professional", {"pace": "brisk", "feedback": "fade", "transitions": "cross-fade"}, "Quick, plain answers; nothing moves by itself."),
    ("warm", "Warm", {"pace": "gentle", "feedback": "lift", "entrance": "rise", "moments": "celebrate"}, "Cards lift to the hand; a small party when you sign up."),
    ("artistic", "Artistic", {"pace": "slow", "feedback": "fade", "entrance": "scroll-reveal", "transitions": "cross-fade"}, "Work arrives slowly as you scroll to it."),
    ("sorcery", "Sorcery", {"pace": "slow", "feedback": "fade", "entrance": "fade", "ambient": "breathing", "transitions": "cross-fade"}, "A lamp that breathes in a dark, slow room."),
    ("gilded-dark", "Gilded dark", {"pace": "brisk", "feedback": "squeeze", "ambient": "twinkle", "transitions": "cross-fade", "moments": "secret-swap"}, "Quick, solid controls; sparkles; a secret look."),
    ("lantern-fair", "Lantern fair", {"pace": "gentle", "feedback": "lift", "entrance": "stagger", "ambient": "breathing"}, "A breathing lantern over stalls that come in one by one."),
    ("almanac-plate", "Almanac plate", {"pace": "gentle", "feedback": "fade", "ambient": "twinkle", "clock": "real-time"}, "Charts under the visitor's own sky, a star or two twinkling."),
    ("repair-cafe", "Repair cafe", {"pace": "brisk", "feedback": "press-in", "entrance": "none", "moments": "write-in"}, "Buttons that press in; your name written on the sheet."),
]

TITLES = {"pace": "Pace", "feedback": "Feedback", "entrance": "Entrance", "ambient": "Ambient", "clock": "Clock",
          "transitions": "Transitions", "moments": "Moments"}
NOTES = {
    "pace": "The shared durations and easing curves every other layer uses. The faint dots are where each runner is every 50 ms on its way across. The curves show how far a thing has gone (up) against time (across): arriving (solid), leaving (dashed). The bars are the three durations to scale.",
    "feedback": "What a control does when it is pointed at and pressed. Try the button and the card; the frames show rest, pointed at, and pressed.",
    "entrance": "How things arrive when the page opens, or when they are scrolled to. Play shows it again; the frames are the same motion, stopped.",
    "ambient": "Motion that runs by itself. It is slow, small, never flashes, stops when the visitor asks for less motion, and the switch at the top of the page pauses it.",
    "clock": "Motion at the speed of a clock. The real clock is repainted once a minute with no transition, too slowly to be seen: it is not motion, and goes on under reduced motion.",
    "transitions": "How one view changes to another: a tab, a step, a page. Press the other tab; the frames show the change stopped at four moments.",
    "moments": "Motion that marks something done or something to notice. Press the button; the frames show the moment stopped.",
}


# ---------------------------------------------------------------- still frames
def frames_html(cells, labels):
    out = "".join(f'<div class="frame"><div>{c}</div><span>{l}</span></div>' for c, l in zip(cells, labels))
    return f'<div class="frames" aria-hidden="true">{out}</div>'


def block(op=1, tx=0, ty=0, sc=1, rot=0, cls="fb"):
    style = []
    if op != 1:
        style.append(f"opacity:{round(op, 2):g}")
    if round(tx, 1) or round(ty, 1):
        style.append(f"translate:{round(tx, 1):g}px {round(ty, 1):g}px")
    if round(sc, 2) != 1:
        style.append(f"scale:{round(sc, 2):g}")
    if round(rot):
        style.append(f"rotate:{round(rot)}deg")
    return f'<i class="{cls}"' + (f' style="{";".join(style)}"' if style else "") + "></i>"


def ms_labels(total, n=4):
    return [f"{round(total * i / (n - 1))} ms" for i in range(n)]


def entrance_frames(kind, pace="brisk"):
    d = PACES[pace]["dur"][2]
    step = PACES[pace]["step"]
    ease = ease_of(pace)
    total = d + (2 * step if kind in ("stagger",) else 0)
    if kind == "none":
        return frames_html(["".join(block() for _ in range(3))] * 4, ["0 ms", "", "", "at once"])
    cells = []
    for i in range(4):
        t = total * i / 3
        row = ""
        for k in range(3):
            start = k * step if kind == "stagger" else 0
            p = min(1, max(0, (t - start) / d))
            e = ease(p)
            if kind == "fade":
                row += block(op=e)
            elif kind == "scroll-reveal":   # it moves into place, never fading from nothing
                row += block(ty=(1 - e) * 22, sc=0.94 + 0.06 * e)
            else:
                row += block(op=e, ty=(1 - e) * 12)
        cells.append(row)
    labels = ms_labels(total) if kind != "scroll-reveal" else ["below", "entering", "half in", "in view"]
    return frames_html(cells, labels)


def feedback_frames(kind):
    if kind == "straighten":
        cells = ['<span class="fcard"></span>', '<span class="fcard is-hover"></span>', '<span class="fcard is-hover is-press"></span>']
    elif kind == "lift":
        cells = ['<span class="fcard"></span>', '<span class="fcard is-hover"></span>', '<span class="fcard is-hover is-press"></span>']
    else:
        cells = ['<span class="fbtn"></span>', '<span class="fbtn is-hover"></span>', '<span class="fbtn is-hover is-press"></span>']
    labels = ["at rest", "pointed at", "pressed"]
    if kind == "fade":    # the veil half-way, 50 ms in
        cells.insert(1, '<span class="fbtn is-half"></span>')
        labels.insert(1, "50 ms in")
    out = "".join(f'<div class="frame"><div>{c}</div><span>{l}</span></div>'
                  for c, l in zip(cells, labels))
    return f'<div class="frames{"" if len(cells) == 4 else " frames-3"}" aria-hidden="true">{out}</div>'


def ambient_frames(kind):
    if kind == "none":
        return frames_html(['<i class="f-lamp"></i>'] * 4, ["0 s", "", "", "always"])
    if kind == "breathing":     # opacity 1 to 0.78 and back, sine-like, over 7 s
        vals = [1 - 0.22 * (1 - math.cos(math.pi * t / 3.5)) / 2 for t in (0, 1.75, 3.5, 7)]
        cells = [f'<i class="f-lamp"><b style="opacity:{v:.2f}"></b></i>' for v in vals]
        return frames_html(cells, [f"{t} s, {v:.0%}" for t, v in zip(("0", "1.8", "3.5", "7"), vals)])
    if kind == "flicker":
        vals = [1, 0.9, 0.85, 0.96]
        cells = [f'<i class="f-lamp"><b style="opacity:{v:.2f}"></b></i>' for v in vals]
        return frames_html(cells, [f"{t} s, {v:.0%}" for t, v in zip(("0", "0.3", "1", "1.2"), vals)])
    if kind == "twinkle":
        sets = [(1, 0.6, 0.9), (0.7, 1, 0.5), (0.45, 0.8, 1), (0.8, 0.5, 0.7)]
        cells = ["".join(f'<i class="f-star" style="opacity:{o}"></i>' for o in s) for s in sets]
        return frames_html(cells, ["0 s", "2 s", "4 s", "6 s"])
    if kind == "drift":
        cells = ["".join(f'<i class="f-mote" style="translate:{(x + 8 * i) % 70 - 30}px {y + i}px"></i>' for x, y in ((0, -10), (25, 4), (50, 12))) for i in range(4)]
        return frames_html(cells, ["0 s", "10 s", "20 s", "30 s"])


def sun_xy(hour):
    """Where the disc sits on the arc at an hour: rises at 6, highest at 12, sets at 18; the moon takes the night."""
    day = 6 <= hour < 18
    a = ((hour - 6) / 12) if day else (((hour - 18) % 24) / 12)
    return 50 - 40 * math.cos(math.pi * a), 85 - 70 * math.sin(math.pi * a), day


def clock_frames(kind):
    if kind == "none":
        return frames_html(['<i class="f-sky"><b class="f-disc" style="left:50%;top:15%"></b></i>'] * 4, ["06:00", "12:00", "18:00", "23:00"])
    hours = (7, 12, 17, 23)
    cells = []
    for h in hours:
        x, y, day = sun_xy(h)
        cells.append(f'<i class="f-sky{" night" if not day else ""}"><b class="f-disc{" moon" if not day else ""}" style="left:{x:.0f}%;top:{y:.0f}%"></b></i>')
    labels = ["07:00", "12:00", "17:00", "23:00"] if kind == "real-time" else ["+1 min", "+6 min", "+11 min", "+17 min"]
    return frames_html(cells, labels)


def transition_frames(kind, pace="brisk"):
    d = PACES[pace]["dur"][2]
    ease = ease_of(pace, "inout")
    cells = []
    for i in range(4):
        p = i / 3
        e = ease(p)
        if kind == "none":
            o_old, o_new = (1, 0) if i == 0 else (0, 1)
            cells.append(block(op=o_old, cls="fp old") + block(op=o_new, cls="fp new"))
        elif kind == "cross-fade":
            cells.append(block(op=1 - e, cls="fp old") + block(op=e, cls="fp new"))
        elif kind == "slide":
            cells.append(block(op=1 - e, tx=-12 * e, cls="fp old") + block(op=e, tx=12 * (1 - e), cls="fp new"))
        elif kind == "grow":
            s = 0.35 + 0.65 * e
            cells.append(block(op=1, sc=s, tx=-14 * (1 - e), ty=-8 * (1 - e), cls="fp new"))
    return frames_html(cells, ["0 ms", "", "", "at once"] if kind == "none" else ms_labels(d))


def moment_frames(kind, pace="brisk"):
    if kind == "none":
        return frames_html(['<i class="f-line"></i><i class="f-line"></i>'] * 3 + ['<i class="f-line"></i><i class="f-line"></i><i class="f-line new"></i>'],
                           ["", "", "", "at once"])
    if kind == "write-in":
        cells = [f'<i class="f-line"></i><i class="f-line"></i><i class="f-line new" style="width:{w}%"></i>' for w in (4, 33, 66, 80)]
        return frames_html(cells, ms_labels(PACES[pace]["dur"][2] * 2.5))
    if kind == "celebrate":
        cells = []
        for i, p in enumerate((0, 0.35, 0.7, 1)):
            e = 1 - (1 - p) ** 3
            bits = "".join(block(op=1 - p ** 3, tx=math.cos(a) * 40 * e, ty=math.sin(a) * 22 * e + 16 * p * p, rot=200 * p * (1 if k % 2 else -1), cls="f-bit")
                           for k, a in enumerate(i * 0 + math.radians(d) for d in (200, 240, 290, 330, 20, 160)))
            cells.append(bits + '<i class="f-dot"></i>')
        return frames_html(cells, ms_labels(700))
    if kind == "secret-swap":
        e = ease_of(pace, "inout")
        cells = [f'<i class="f-look a" style="opacity:{1 - e(p):.2f}"></i><i class="f-look b" style="opacity:{e(p):.2f}"></i>' for p in (0, 1 / 3, 2 / 3, 1)]
        return frames_html(cells, ms_labels(round(PACES[pace]["dur"][2] * 1.6)))
    if kind == "nudge":
        cells = []
        for p in (0, 0.33, 0.66, 1):
            cells.append(f'<i class="f-ring" style="scale:{1 + 0.35 * p:.2f};opacity:{0.9 * (1 - p):.2f}"></i><i class="f-dot"></i>')
        return frames_html(cells, ["0 s", "0.4 s", "0.8 s", "1.2 s"])


def pace_figure(pace):
    p = PACES[pace]
    w, h = 120, 80

    def path(which):
        if pace == "still":
            return f"M0 {h} L0 0 L{w} 0"
        if pace == "springy" and which == "out":
            pts = [(i / 32, spring(i / 32)) for i in range(33)]
        else:
            pts = [(i / 40, bezier(p[which], i / 40)) for i in range(41)]
        return "M" + " L".join(f"{x * w:.1f} {h - y * h:.1f}" for x, y in pts)
    svg = (f'<svg class="curve" viewBox="-4 -14 {w + 8} {h + 22}" aria-hidden="true" focusable="false">'
           f'<path class="axis" d="M0 0 V{h} H{w}"/><path class="over" d="M0 0 H{w}"/>'
           f'<path class="c-in" d="{path("in")}"/><path class="c-out" d="{path("out")}"/></svg>')
    bars = "".join(f'<div class="bar"><i style="width:{max(2, d / 7):.0f}%"></i><span>{name} {d} ms</span></div>'
                   for name, d in zip(("short", "medium", "long"), p["dur"]))
    return f'<div class="pace-fig" aria-hidden="true">{svg}<div class="bars">{bars}</div></div>'


# ---------------------------------------------------------------- the live parts
def cards(n=3):
    words = ["Lamps", "Kettles", "Bicycles", "Radios", "Coats", "Clocks"]
    return '<div class="cards">' + "".join(f'<div class="card enter" style="--i:{i}"><b>{words[i]}</b><span>Bring it in</span></div>' for i in range(n)) + "</div>"


def ambient_fx(kind):
    if kind in ("breathing", "flicker"):
        return '<div class="amb" aria-hidden="true"><i class="glow"></i><i class="src"></i></div>'
    if kind == "twinkle":
        stars = "".join(f'<i class="star" style="left:{x}%;top:{y}%;--d:{d}s;--o:{o}s"></i>'
                        for x, y, d, o in ((12, 20, 5, 0), (30, 60, 7, -2), (48, 28, 5, -3.5), (66, 70, 7, -1), (82, 34, 5, -4.2), (90, 78, 5, -1.6)))
        return f'<div class="amb amb-sky" aria-hidden="true">{stars}</div>'
    if kind == "drift":
        motes = "".join(f'<i class="mote" style="left:{x}%;top:{y}%;--d:{d}s;--o:{o}s"></i>'
                        for x, y, d, o in ((5, 25, 30, 0), (20, 70, 38, -9), (40, 40, 34, -20), (55, 15, 42, -5), (70, 60, 30, -14), (85, 35, 36, -25)))
        return f'<div class="amb amb-motes" aria-hidden="true">{motes}</div>'
    return ""


def clock_live(kind):
    if kind == "none":
        return ""
    hold = '<button class="sbtn hold" type="button" aria-pressed="false">Hold it still</button>' if kind == "game-time" else ""
    label = "Now" if kind == "real-time" else "Colony time"
    return (f'<div class="clock" data-kind="{kind}"><div class="sky" aria-hidden="true"><i class="arc"></i><b class="disc"></b></div>'
            f'<p class="time"><span>{label}:</span> <output class="t">--:--</output></p>{hold}</div>')


def toggle(kind):
    if kind == "grow":
        panels = ('<div class="panel" data-p="0"><div class="minis"><div class="mini pick">Lamp</div><div class="mini">Kettle</div><div class="mini">Radio</div></div></div>'
                  '<div class="panel detail" data-p="1" hidden><b>Lamp</b><span>Brass, 1930s. The switch sticks; the cord is worn.</span></div>')
        names = ("All items", "The lamp")
    else:
        panels = ('<div class="panel" data-p="0"><b>Stalls</b><span>Forty stalls along the river, open from six.</span></div>'
                  '<div class="panel" data-p="1" hidden><b>Map</b><span>Start at the bridge; the food is at the far end.</span></div>')
        names = ("Stalls", "Map")
    tabs = "".join(f'<button class="sbtn tab" type="button" data-tab="{i}" aria-pressed="{"true" if i == 0 else "false"}">{n}</button>' for i, n in enumerate(names))
    return f'<div class="views"><div class="tabs" role="group" aria-label="Views">{tabs}</div><div class="panels">{panels}</div></div>'


def moment_live(kind):
    if kind in ("none", "write-in"):
        return ('<div class="signup"><ol class="names"><li><span class="who">Ade Okafor</span></li><li><span class="who">Mei Lin</span></li></ol>'
                '<button class="btn" type="button" data-moment>Add my name</button><p class="said" role="status"></p></div>')
    if kind == "celebrate":
        return '<div class="signup"><button class="btn" type="button" data-moment>Sign me up</button><p class="said" role="status"></p></div>'
    if kind == "secret-swap":
        return ('<div class="look"><b class="emblem" aria-hidden="true"></b><span>The everyday look.</span>'
                '<button class="sbtn" type="button" data-moment>Say the secret word</button></div>')
    if kind == "nudge":
        return '<div class="signup"><p class="hint">Your basket is ready.</p><button class="btn nudge-me" type="button">Go to checkout</button><button class="sbtn" type="button" data-moment>Nudge</button></div>'
    return ""


def stage(option, picks, name, idline, line, demo, frames):
    p = dict(DEFAULTS, **picks)
    classes = ["stage", "mo"] + [f"{SHORT[k]}-{v}" for k, v in p.items()]
    data = f' data-tr="{p["transitions"]}" data-mm="{p["moments"]}"'
    return (f'<section class="swatch" data-option="{option}">\n<div class="{" ".join(classes)}"{data}>\n'
            f'<div class="sw-head"><div><h3>{name}</h3><p class="id">{idline}</p></div>'
            f'<button class="sbtn play" type="button">Play</button></div>\n'
            f'<p class="line">{line}</p>\n<div class="demo">{demo}</div>\n{frames}\n</div>\n</section>\n')


def ghosts(pace, d):
    """Where a runner is every 50 ms on its way across, as faint dots: a still picture of the curve and the duration."""
    if not d:
        return ""
    ease = (lambda x: spring(x)) if pace == "springy" else ease_of(pace, "inout")
    return "".join(f'<i class="gh" style="--p:{round(ease(k * 50 / d), 2):g}"></i>' for k in range(1, int(d / 50)) )


def option_swatch(layer, oid, name, line):
    opt = f"{layer}:{oid}"
    if layer == "pace":
        demo = '<div class="tracks">' + "".join(f'<div class="track"><span>{k}</span><i class="lane">{ghosts(oid, d)}<i class="runner {k}"></i></i></div>'
                                                for k, d in zip(("short", "medium", "long"), PACES[oid]["dur"])) + "</div>"
        demo += '<button class="btn" type="button">Press me</button>'
        frames = pace_figure(oid)
    elif layer == "feedback":
        demo = ('<div class="fb-row"><button class="btn" type="button">Press me</button>'
                '<a class="card link-card" href="#feedback"><b>Kettles</b><span>Point at this card</span></a></div>')
        frames = feedback_frames(oid)
    elif layer == "entrance":
        if oid == "scroll-reveal":
            demo = ('<div class="scroller" tabindex="0" role="region" aria-label="Scroll this box">'
                    + "".join(f'<p class="blockrow enter">Plate {i + 1}: {w}</p>' for i, w in enumerate(("a celadon bowl", "a tea bowl, ash glaze", "a jug in tenmoku", "two cups, shino", "a dish, copper red", "a lidded jar"))) + "</div>")
        else:
            demo = cards()
        frames = entrance_frames(oid)
    elif layer == "ambient":
        demo = ambient_fx(oid) + '<p class="over">Open every Saturday, ten till four.</p>'
        frames = ambient_frames(oid)
    elif layer == "clock":
        demo = clock_live(oid) or '<p class="over">Open every Saturday, ten till four.</p>'
        frames = clock_frames(oid)
    elif layer == "transitions":
        demo = toggle(oid)
        frames = transition_frames(oid)
    else:
        demo = moment_live(oid)
        frames = moment_frames(oid)
    return stage(opt, {layer: oid}, name, f"{layer}: {oid}", line, demo, frames)


def start_swatch(sid, name, picks, line):
    p = dict(DEFAULTS, **picks)
    idline = "; ".join(f"{k}: {v}" for k, v in picks.items())
    demo = ambient_fx(p["ambient"])
    demo += '<div class="start-grid">' + cards(3) + '<div class="start-side">' + clock_live(p["clock"])
    if p["transitions"] != "none":
        demo += toggle(p["transitions"])
    if p["moments"] != "none":
        demo += moment_live(p["moments"])
    else:
        demo += '<button class="btn" type="button">Press me</button>'
    demo += "</div></div>"
    return stage(f"start:{sid}", picks, name, idline, line, demo, "")


out = []
for layer, options in LAYERS.items():
    out.append(f'<h2 class="layer">{TITLES[layer]}</h2>\n<p class="layer-note">{NOTES[layer]}</p>\n')
    for oid, name, line in options:
        out.append(option_swatch(layer, oid, name, line))
out.append('<h2 class="layer">Starting points</h2>\n<p class="layer-note">Saved sets of picks; any layer not named is at its default (brisk, fade, nothing else). Play shows each one again.</p>\n')
for sid, name, picks, line in STARTS:
    out.append(start_swatch(sid, name, picks, line))

page = (HERE / "motion-template.html").read_text(encoding="utf-8")
page = page.replace("{{SPRING}}", SPRING).replace("{{SWATCHES}}", "".join(out))
Path(sys.argv[1]).write_text(page, encoding="utf-8")
print("wrote", sys.argv[1], len(page), "bytes")
