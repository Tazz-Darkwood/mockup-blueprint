"""Builds the background swatch page (../background.html): draws the repeating tiles, encodes them as data URIs and
fills them into background-template.html beside this file. Run from this folder: python3 background.py ../background.html"""
import math, random, sys, urllib.parse
from pathlib import Path

HERE = Path(__file__).parent
R = random.Random(7)


def uri(svg):
    svg = " ".join(svg.split())
    return 'url("data:image/svg+xml,' + urllib.parse.quote(svg, safe=" =:/'(),.-;") + '")'


def grain(alpha, rgb="0 0 0", size=240, freq=0.85):
    r, g, b = rgb.split()
    return uri(f"""<svg xmlns='http://www.w3.org/2000/svg' width='{size}' height='{size}'>
<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='{freq}' numOctaves='2' stitchTiles='stitch'/>
<feColorMatrix values='0 0 0 0 {r}  0 0 0 0 {g}  0 0 0 0 {b}  0 0 0 {alpha} 0'/></filter>
<rect width='{size}' height='{size}' filter='url(#n)'/></svg>""")


# paper grain as on the soap maker's shop: a brown speckle that only darkens
PAPER = uri("""<svg xmlns='http://www.w3.org/2000/svg' width='260' height='260'>
<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.7' numOctaves='3' stitchTiles='stitch'/>
<feColorMatrix values='0 0 0 0 0.45  0 0 0 0 0.36  0 0 0 0 0.22  0 0 0 0.5 -0.13'/></filter>
<rect width='260' height='260' filter='url(#n)' opacity='0.55'/></svg>""")


def stroke(x, y, length, width, angle, colour, op):
    """One painted stroke: a long rounded dab, a little curved."""
    a = math.radians(angle)
    dx, dy = math.cos(a) * length, math.sin(a) * length
    bend = R.uniform(-0.15, 0.15) * length
    mx, my = x + dx / 2 - math.sin(a) * bend, y + dy / 2 + math.cos(a) * bend
    return (f"<path d='M{x:.0f} {y:.0f}Q{mx:.0f} {my:.0f} {x + dx:.0f} {y + dy:.0f}' stroke='{colour}' "
            f"stroke-width='{width:.0f}' stroke-linecap='round' fill='none' opacity='{op:.2f}'/>")


def painted_tile():
    w, h = 480, 480
    o = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'>"]
    body = []
    for _ in range(70):
        body.append(stroke(R.uniform(-60, w), R.uniform(0, h), R.uniform(60, 200), R.uniform(8, 22),
                           R.uniform(-8, 8), R.choice(["#5a2418", "#4a1d14", "#6b2c1c", "#32120d"]), R.uniform(0.35, 0.7)))
    for _ in range(26):   # lit edges on the rock
        body.append(stroke(R.uniform(-30, w), R.uniform(0, h), R.uniform(20, 60), R.uniform(2, 5),
                           R.uniform(-10, 10), R.choice(["#b2602f", "#c9773a"]), R.uniform(0.15, 0.32)))
    for _ in range(140):  # stipple in shadow
        body.append(f"<circle cx='{R.uniform(0, w):.0f}' cy='{R.uniform(0, h):.0f}' r='{R.uniform(0.8, 1.8):.1f}' fill='#1a0806' opacity='0.4'/>")
    g = "".join(body)
    # draw it three times across and down so strokes that cross an edge wrap round
    for ox in (-w, 0, w):
        for oy in (-h, 0, h):
            o.append(f"<g transform='translate({ox} {oy})'>{g}</g>")
    o.append("</svg>")
    return uri("".join(o))


def sign(cx, cy, s, rot, kind, colour, op):
    st = f"stroke='{colour}' stroke-width='{max(1.2, s / 20):.1f}' fill='none' opacity='{op:.2f}' stroke-linecap='round'"
    g = [f"<g transform='translate({cx:.0f} {cy:.0f}) rotate({rot:.0f})' {st}>"]
    if kind == 0:     # a circle with a seven-point line star
        pts = [(s * math.cos(2 * math.pi * k * 3 / 7 - math.pi / 2), s * math.sin(2 * math.pi * k * 3 / 7 - math.pi / 2)) for k in range(7)]
        g.append(f"<circle r='{s:.0f}'/><path d='M" + "L".join(f"{x:.0f} {y:.0f}" for x, y in pts) + "Z'/>")
    elif kind == 1:   # a ring with ticks and a triangle
        g.append(f"<circle r='{s:.0f}'/><circle r='{s * .78:.0f}'/>")
        for k in range(12):
            a = 2 * math.pi * k / 12
            g.append(f"<path d='M{s * .78 * math.cos(a):.0f} {s * .78 * math.sin(a):.0f}L{s * math.cos(a):.0f} {s * math.sin(a):.0f}'/>")
        g.append(f"<path d='M0 {-s * .6:.0f}L{s * .5:.0f} {s * .4:.0f}L{-s * .5:.0f} {s * .4:.0f}Z'/>")
    elif kind == 2:   # a branching mark
        g.append(f"<path d='M0 {-s:.0f}V{s:.0f}M0 {-s * .4:.0f}L{s * .55:.0f} {-s:.0f}M0 0L{-s * .5:.0f} {s * .45:.0f}'/>")
    elif kind == 3:   # a moon and an orbit
        g.append(f"<path d='M{s * .3:.0f} {-s:.0f}a{s:.0f} {s:.0f} 0 1 0 0 {2 * s:.0f}a{s * .75:.0f} {s * .75:.0f} 0 1 1 0 {-2 * s:.0f}'/>")
        g.append(f"<ellipse rx='{s * 1.6:.0f}' ry='{s * .5:.0f}'/>")
    else:             # a written line of made-up letters
        x = -s * 1.6
        while x < s * 1.6:
            g.append(R.choice([f"<path d='M{x:.0f} -8v16M{x:.0f} -4l7 -4'/>", f"<path d='M{x:.0f} 8l5 -16l5 16'/>",
                               f"<path d='M{x:.0f} -8v16l8 -8l-8 -8'/>", f"<path d='M{x:.0f} -8l9 16M{x + 9:.0f} -8l-9 16'/>"]))
            x += 15
    g.append("</g>")
    return "".join(g)


def detail_tile():
    """The detailed ground's repeating layer: mottling, hatching, specks and small signs.
    Transparent, so the ground colour underneath comes from CSS and can be changed there."""
    w, h = 640, 720
    placed, signs = [], []
    tries = 0
    while len(placed) < 9 and tries < 5000:
        tries += 1
        x, y = R.uniform(60, w - 60), R.uniform(60, h - 60)
        if any(math.hypot(x - a, y - b) < 150 for a, b in placed):
            continue
        placed.append((x, y))
        signs.append(sign(x, y, R.uniform(14, 40), R.uniform(0, 360), len(placed) % 5,
                          R.choice(["#d9c38f", "#b9c3dd", "#d39a78"]), R.uniform(0.16, 0.28)))
    specks = "".join(f"<circle cx='{R.uniform(0, w):.0f}' cy='{R.uniform(0, h):.0f}' r='{R.uniform(0.6, 1.8):.1f}'/>" for _ in range(260))
    return uri(f"""<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'>
<defs>
<filter id='m' x='0' y='0' width='100%' height='100%'><feTurbulence type='fractalNoise' baseFrequency='0.006 0.02' numOctaves='4' seed='6' stitchTiles='stitch'/>
<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.6 0'/></filter>
<filter id='r'><feTurbulence type='fractalNoise' baseFrequency='0.05' numOctaves='2' seed='12'/><feDisplacementMap in='SourceGraphic' scale='3'/></filter>
<pattern id='h' width='7' height='7' patternUnits='userSpaceOnUse' patternTransform='rotate(38)'><path d='M0 0V7' stroke='#000' stroke-width='1.4' opacity='0.5'/></pattern>
</defs>
<rect width='{w}' height='{h}' filter='url(#m)'/>
<rect width='{w}' height='{h}' fill='url(#h)' opacity='0.3'/>
<g fill='#000' opacity='0.45'>{specks}</g>
<g filter='url(#r)'>{"".join(signs)}</g>
</svg>""")


tpl = (HERE / "background-template.html").read_text()
fills = {
    "GRAIN_DARK": grain(0.55),
    "GRAIN_LIGHT": grain(0.22),
    "GRAIN_WHITE": grain(0.1, "1 1 1", 220, 0.9),
    "PAPER": PAPER,
    "PAINTED": painted_tile(),
    "DETAIL": detail_tile(),
}
for k, v in fills.items():
    tpl = tpl.replace("{{" + k + "}}", v)
Path(sys.argv[1]).write_text(tpl)
print("wrote", sys.argv[1], len(tpl), "bytes")
