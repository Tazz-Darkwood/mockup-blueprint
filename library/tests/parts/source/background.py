"""Builds the background swatch book (../background.html) from background-template.html beside this file.

It draws the repeating tiles as masks (black shapes whose only job is their alpha: the colour comes from the shared
colour names in CSS, so the same tile works on a light page and a dark one), and writes one swatch for each option of
each layer, then one for each starting point, in the guide's order. Run from this folder:
    python3 background.py ../background.html
It also redraws the tiles in the part guide's assembly code (the lines "& { --background-<tile>: url(...); }" in
library/style-part-background.md), so the code 'style css' lifts is the same as the swatch book's."""
import math, random, re, sys, urllib.parse
from pathlib import Path

HERE = Path(__file__).parent
R = random.Random(7)


def uri(svg):
    svg = " ".join(svg.split())
    return 'url("data:image/svg+xml,' + urllib.parse.quote(svg, safe=" =:/'(),.-;") + '")'


# ---------- mask tiles ----------

def grain_mask(size=240, freq=0.8, alpha=1):
    """Speckle: the noise's red channel turned into alpha, so only the specks are opaque. alpha below 1 scales it
    (the soft grain the guide's mottled texture lays in the same mask as its mottling)."""
    soft = f"<feComponentTransfer><feFuncA type='linear' slope='{alpha}'/></feComponentTransfer>" if alpha != 1 else ""
    return uri(f"""<svg xmlns='http://www.w3.org/2000/svg' width='{size}' height='{size}'>
<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='{freq}' numOctaves='2' stitchTiles='stitch'/>
<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  2.4 0 0 0 -0.95'/>{soft}</filter>
<rect width='{size}' height='{size}' filter='url(#n)'/></svg>""")


def mottle_mask():
    """A slow, stretched mottling: large soft patches."""
    return uri("""<svg xmlns='http://www.w3.org/2000/svg' width='640' height='720'>
<filter id='m' x='0' y='0' width='100%' height='100%'><feTurbulence type='fractalNoise' baseFrequency='0.006 0.02' numOctaves='4' seed='6' stitchTiles='stitch'/>
<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1.8 0 0 0 -0.55'/></filter>
<rect width='640' height='720' filter='url(#m)'/></svg>""")


def wrap(w, h, x0, y0, x1, y1, pad, body):
    """Copies of one shape moved a tile's width or height, for each side it crosses, so the tile repeats without a seam."""
    out = []
    for ox in (-w, 0, w):
        for oy in (-h, 0, h):
            if min(x0, x1) - pad + ox < w and max(x0, x1) + pad + ox > 0 and min(y0, y1) - pad + oy < h and max(y0, y1) + pad + oy > 0:
                out.append(body if (ox, oy) == (0, 0) else f"<g transform='translate({ox} {oy})'>{body}</g>")
    return "".join(out)


def stone_masks():
    """Courses of dressed stone: block faces at a few strengths, and the joints between them."""
    w, h, course = 420, 208, 52
    faces, joints = [], []
    for row in range(h // course):
        y = row * course
        x = -R.uniform(0, 90) if row % 2 else 0
        joints.append(f"<path d='M0 {y}H{w}'/>")
        while x < w:
            bw = R.uniform(90, 150)
            faces.append(wrap(w, h, x, y, x + bw, y + course, 0,
                              f"<rect x='{x:.0f}' y='{y}' width='{bw:.0f}' height='{course}' opacity='{R.choice([0.15, 0.35, 0.55, 0.8]):.2f}'/>"))
            if x > 0:
                joints.append(f"<path d='M{x:.0f} {y}V{y + course}'/>")
            x += bw
    joints.append("<path d='M200 60l14 18l-6 14l12 18' stroke-width='1.5'/>")   # a crack
    head = f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'>"
    return (uri(head + "".join(faces) + "</svg>"),
            uri(head + "<g fill='none' stroke='black' stroke-width='3'>" + "".join(joints) + "</g></svg>"))


def painted_masks():
    """The painted ground: a cliff of rock ledges, painted in big shapes of three or four values with the light from the
    upper left, as a backdrop painter would block it in. Five masks, one per value, so each takes its own colour in CSS:
      face  - the rock faces under each ledge, with upright strokes that follow the fall of the stone
      shade - the facets turned away from the light, and the cast shadow under each lip
      lit   - the top of each ledge, the rims of the lit facets, and dabs on the bushes
      leaf  - bushes and tufts on the ledges
    The earth between the ledges is the layer's own background. Every ledge line is periodic across the tile, and shapes
    that cross the top or bottom are drawn again one tile away, so it repeats without a seam. One displacement filter, the
    same in all five, roughens every edge like a loaded brush, and keeps the masks lined up with each other."""
    rnd = random.Random(21)
    W, H, N = 960, 600, 4                      # four ledges, 150 px apart
    step = W // 20                             # one crag every 48 px
    def ledge(base, amp):
        p1, p2 = rnd.uniform(0, 6.3), rnd.uniform(0, 6.3)
        jag = [rnd.uniform(-1, 1) * amp * 0.45 for _ in range(W // step)]
        return [(x, base + amp * math.sin(2 * math.pi * x / W + p1) + amp * 0.5 * math.sin(4 * math.pi * x / W + p2) + jag[(x // step) % len(jag)])
                for x in range(0, W + step, step)]
    def d(pts):
        return "M" + "L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    def poly(pts, op):                         # a filled shape (kept apart from the strokes: they need no fill)
        return ("P", f"<path d='{d(pts)}Z' opacity='{str(round(op, 1)).lstrip("0")}'/>")
    def line(pts, w, op):
        return ("L", f"<path d='{d(pts)}' stroke-width='{w:.0f}' opacity='{str(round(op, 1)).lstrip("0")}'/>")
    def dab(x, y, length, w, ang, op):
        a = math.radians(ang)
        return line([(x, y), (x + math.cos(a) * length, y + math.sin(a) * length)], w, op)
    face, shade, lit, leaf = [], [], [], []
    for i in range(N):
        lip = ledge(70 + i * 150 + rnd.uniform(-12, 12), rnd.uniform(18, 30))
        depth = [rnd.uniform(60, 96) for _ in lip]
        depth[-1] = depth[0]
        foot = [(x, y + d) for (x, y), d in zip(lip, depth)]
        top = [(x, y - rnd.uniform(9, 22)) for x, y in lip]
        top[-1] = (top[-1][0], top[0][1] + (lip[-1][1] - lip[0][1]))
        f, sh, li, le = [poly(lip + foot[::-1], 0.92)], [], [poly(top + lip[::-1], 0.85)], []
        for k in range(len(lip) - 1):
            (x0, y0), (x1, y1) = lip[k], lip[k + 1]
            if y1 < y0 - 4:                     # the crag turns away from the light: its facet is in shade
                sh.append(poly([lip[k], lip[k + 1], foot[k + 1], (foot[k][0] + 6, foot[k][1])], rnd.uniform(0.55, 0.8)))
            else:                               # turned to the light: a lit rim along its lip
                li.append(line([(x0, y0 + 1), (x1, y1 + 1)], rnd.uniform(2, 4), rnd.uniform(0.7, 1)))
            for _ in range(rnd.randint(1, 2)):  # upright strokes down the face, each its own width
                sx = rnd.uniform(x0, x1); sy = y0 + (y1 - y0) * (sx - x0) / (x1 - x0) + rnd.uniform(6, 20)
                (sh if rnd.random() < 0.5 else f).append(dab(sx, sy, rnd.uniform(25, 70), rnd.uniform(3, 11), rnd.uniform(78, 98), rnd.uniform(0.25, 0.6)))
        sh.append(line([(x, y + 7) for x, y in lip], 9, 0.5))                  # the cast shadow under the lip
        sh.append(line([(x, y + 3) for x, y in foot], 14, 0.28))               # the foot of the face, in the earth
        for x, y in lip[::3]:                                                   # strokes along the top, following it
            li.append(dab(x + rnd.uniform(-10, 10), y - rnd.uniform(5, 12), rnd.uniform(18, 46), rnd.uniform(3, 7), rnd.uniform(-12, 12), rnd.uniform(0.4, 0.8)))
        for x, y in foot[1::2]:                                                 # the earth slope: long, slanting strokes
            g = sh if rnd.random() < 0.5 else li
            g.append(dab(x + rnd.uniform(-20, 20), y + rnd.uniform(12, 40), rnd.uniform(40, 110), rnd.uniform(4, 12), rnd.uniform(8, 24), rnd.uniform(0.15, 0.35)))
        for x, y in rnd.sample(top[1:-1], 2):                                    # bushes on the ledge, lit on the upper left
            r = rnd.uniform(9, 16)
            for _ in range(rnd.randint(6, 9)):
                cx, cy, cr = x + rnd.uniform(-2.2, 2.2) * r, y - rnd.uniform(0, 1.3) * r, rnd.uniform(0.45, 0.9) * r
                le.append(("P", f"<circle cx='{cx:.0f}' cy='{cy:.0f}' r='{cr:.0f}'/>"))
                if cx < x and cy < y - r * 0.4:
                    li.append(("P", f"<circle cx='{cx - cr * 0.3:.0f}' cy='{cy - cr * 0.3:.0f}' r='{cr * 0.5:.0f}' opacity='.8'/>"))
        for group, items in ((face, f), (shade, sh), (lit, li), (leaf, le)):
            body = "".join(b for k, b in items if k == "P") + "<g fill='none'>" + "".join(b for k, b in items if k == "L") + "</g>"
            ys = [y for _, y in top] + [y for _, y in foot]
            lo, hi = min(ys) - 40, max(ys) + 60
            copies = "".join(f"<use href='#g{i}' y='{oy}'/>" for oy in (-H, H) if lo + oy < H and hi + oy > 0)
            group.append(f"<g id='g{i}'>{body}</g>{copies}" if copies else body)   # drawn again a tile away where it crosses
    head = (f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}'><filter id='b' filterUnits='userSpaceOnUse' x='-20' y='-20' "
            f"width='{W + 40}' height='{H + 40}'><feTurbulence type='fractalNoise' baseFrequency='0.045' numOctaves='3' seed='3'/>"
            "<feDisplacementMap in='SourceGraphic' scale='9'/></filter>"
            "<g filter='url(#b)' stroke='black' stroke-linecap='round' stroke-linejoin='round'>")
    return tuple(uri(head + "".join(g) + "</g></svg>") for g in (face, shade, lit, leaf))


def ridge_mask():
    """Two far ridges for the top of the painted ground, in one mask: the farther at a low alpha, so over the sky it is
    paler and closer to the air's colour (atmospheric perspective), the nearer at a higher one. Periodic across the tile."""
    rnd = random.Random(5)
    W, H = 1200, 120
    out = []
    for base, amp, op in ((50, 26, 0.45), (84, 18, 0.8)):
        p = [rnd.uniform(0, 6.3) for _ in range(3)]
        pts = [(x, base + amp * (math.sin(2 * math.pi * x / W + p[0]) + 0.6 * math.sin(6 * math.pi * x / W + p[1]) + 0.25 * math.sin(14 * math.pi * x / W + p[2])))
               for x in range(0, W + 30, 30)]
        out.append(f"<path d='M0 {H}L" + "L".join(f"{x:.0f} {y:.0f}" for x, y in pts) + f"L{W} {H}Z' opacity='{op}'/>")
    return uri(f"""<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}'><filter id='b' x='-5%' y='-20%' width='110%' height='140%'>
<feTurbulence type='fractalNoise' baseFrequency='0.04' numOctaves='3' seed='3'/><feDisplacementMap in='SourceGraphic' scale='7'/></filter>
<g filter='url(#b)'>{"".join(out)}</g></svg>""")


def sign(cx, cy, s, rot, kind, op):
    st = f"stroke-width='{max(1.2, s / 20):.1f}' opacity='{op:.2f}'"
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


def signs_mask():
    """Small signs scattered over a large tile, no two closer than about 150 pixels, all roughened by one filter."""
    w, h = 640, 720
    placed, signs = [], []
    tries = 0
    while len(placed) < 10 and tries < 5000:
        tries += 1
        x, y = R.uniform(60, w - 60), R.uniform(60, h - 60)
        if any(math.hypot(x - a, y - b) < 150 for a, b in placed):
            continue
        placed.append((x, y))
        signs.append(sign(x, y, R.uniform(14, 40), R.uniform(0, 360), len(placed) % 5, R.uniform(0.55, 1)))
    specks = "".join(f"<circle cx='{R.uniform(0, w):.0f}' cy='{R.uniform(0, h):.0f}' r='{R.uniform(0.6, 1.6):.1f}'/>" for _ in range(120))
    return uri(f"""<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'>
<filter id='r'><feTurbulence type='fractalNoise' baseFrequency='0.05' numOctaves='2' seed='12'/><feDisplacementMap in='SourceGraphic' scale='3'/></filter>
<g opacity='0.5'>{specks}</g>
<g filter='url(#r)' fill='none' stroke='black' stroke-linecap='round'>{"".join(signs)}</g></svg>""")


# ---------- the swatches ----------

DEFAULTS = {"texture": "none", "pattern": "none", "drawings": "none", "finds": "off", "scene": "none"}

# each layer's options, in the guide's order: (id, name, a line for the sheet, the button's words)
LAYERS = {
    "texture": [
        ("none", "None", "One flat colour; nothing between the reader and the words.", "Read on"),
        ("grain", "Grain", "A fine speckle, like paper or plaster. From across the room, still one colour.", "Order"),
        ("felt-weave", "Felt weave", "A faint dot weave: the page is a noticeboard's felt.", "Pin a note"),
        ("mottled-and-hatched", "Mottled and hatched", "Slow patches, fine hatching and grain: an old, worked surface.", "Enter"),
    ],
    "pattern": [
        ("none", "None", "No large shapes behind the sections.", "Read on"),
        ("coloured-bands", "Coloured bands", "Each section on a whole band of a deep colour, edge to edge.", "See the stall"),
        ("stone-courses", "Stone courses", "Courses of dressed stone, with a crack or two.", "Go in"),
    ],
    "drawings": [
        ("none", "None", "No signs drawn on the ground.", "Read on"),
        ("a-few", "A few", "Three large signs, set by hand, one running off the edge.", "Look closer"),
        ("lots", "Lots", "Small signs all over, and larger ones set by hand: something in every corner.", "Enter"),
    ],
    "finds": [
        ("off", "Off", "Nothing hidden in the gaps.", "Read on"),
        ("on", "On", "Small things drawn for the site, sitting in the gaps beside the sheet.", "Look around"),
    ],
    "scene": [
        ("none", "None", "No picture behind the sections.", "Read on"),
        ("painted-ground", "Painted ground", "The picture's world in broad strokes, carried on behind the panels.", "Play"),
        ("one-long-scene", "One long scene", "The picture goes on down the page, band by band.", "Set out"),
    ],
}

STARTS = [
    ("plain", "Plain", {}, "Clean and quiet: one flat colour.", "Read on"),
    ("coloured-bands", "Coloured bands", {"pattern": "coloured-bands", "texture": "grain"}, "Bold blocks of colour, with grain on every band.", "See the stall"),
    ("grain", "Grain", {"texture": "grain"}, "Made, not printed: the safest step up from plain.", "Order"),
    ("material-ground", "Material ground", {"texture": "felt-weave"}, "The page is made of the site's material: here, felt.", "Pin a note"),
    ("painted-ground", "Painted ground", {"scene": "painted-ground"}, "The picture's world behind the panels.", "Play"),
    ("detailed-ground", "Detailed ground", {"texture": "mottled-and-hatched", "drawings": "lots", "finds": "on"}, "A full, lived-in room with something in every corner.", "Enter"),
    ("one-long-scene", "One long scene", {"scene": "one-long-scene"}, "A journey: the world changes as you scroll.", "Set out"),
]

# hand-set signs: (symbol, width in px, left, top, turn); left and top are of the ground
FEW = [("sg-ring", 150, "-6%", "52%", 14), ("sg-moon", 110, "78%", "8%", -18), ("sg-tree", 120, "60%", "62%", 8)]
LOTS = FEW + [("sg-diamond", 90, "70%", "-6%", 30), ("sg-rose", 70, "88%", "48%", -10), ("sg-ring", 60, "52%", "2%", 40),
              ("sg-tree", 80, "-3%", "-4%", -24), ("sg-diamond", 130, "84%", "70%", 6)]


def signs_html(placed):
    return "".join(f'<svg class="sign" style="width:{w}px;left:{x};top:{y};rotate:{r}deg" viewBox="0 0 100 100"><use href="#{sym}"/></svg>'
                   for sym, w, x, y, r in placed)


FINDS = """<div class="finds" aria-hidden="true">
<svg class="find find-keys" viewBox="0 0 110 170" focusable="false"><g filter="url(#pen)"><circle class="solid" cx="55" cy="10" r="5"/><circle cx="55" cy="36" r="22"/><path d="M44 56L24 140M24 140L36 143M27 128L39 131M57 58L60 156M60 156L72 155M60 142L72 141M68 55L92 132M92 132L102 126M88 120L98 114"/></g></svg>
<svg class="find find-pot" viewBox="0 0 120 116" focusable="false"><g filter="url(#pen)"><path class="f1" d="M28 70H78L90 110H16Z"/><path class="f1" d="M38 56H68V70H38Z"/><path class="f3" d="M54 62C66 32 86 14 114 4C106 30 92 48 62 66Z"/><path d="M56 64C72 42 92 22 112 6"/></g></svg>
<svg class="find find-jars" viewBox="0 0 150 84" focusable="false"><g filter="url(#pen)"><path class="f2" d="M4 78V42C4 32 12 32 12 22V10H24V22C24 32 32 32 32 42V78Z"/><path class="f1" d="M48 78C36 62 50 46 53 42V24H65V42C68 46 82 62 70 78Z"/><path class="f3" d="M96 78V42C96 32 104 32 104 22V10H116V22C116 32 124 32 124 42V78Z"/><path d="M0 81H150"/></g></svg>
</div>"""

SCENE = """<div class="band b1">
<svg class="paint" viewBox="0 0 1600 700" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false"><g filter="url(#pen)">
<rect class="sky" width="1600" height="700"/><path class="far" d="M0 430Q200 300 420 380T860 330T1300 370T1600 320V700H0Z"/>
<path class="castle" d="M1180 360V250H1205V230H1225V250H1255V200H1280V180H1300V200H1325V360Z"/>
<path class="near" d="M0 540Q260 450 560 520T1100 480T1600 520V700H0Z"/><path class="road" d="M720 700Q800 600 1000 560T1250 500L1268 506Q1080 590 900 700Z"/></g></svg>
<svg class="edge" viewBox="0 0 1600 80" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path class="next" d="M0 80V52Q50 66 120 50Q250 18 400 52Q560 90 720 54Q880 16 1020 48Q1180 86 1330 52Q1470 20 1600 46V80Z"/></svg>
{sheet}</div>
<div class="band b2">
<svg class="paint" viewBox="0 0 1600 400" preserveAspectRatio="xMidYMin slice" aria-hidden="true" focusable="false"><g filter="url(#pen)">
<rect class="meadow" width="1600" height="400"/><path class="stream" d="M300 0Q420 120 360 200T520 400H600Q460 300 470 210T380 0Z"/>
<path class="tuft" d="M900 160l10 -30l8 30M940 220l12 -34l8 34M1200 120l10 -26l8 26M180 260l10 -30l8 30M1320 300l12 -34l8 34"/></g></svg>
</div>"""


def swatch(option, picks, name, idline, line, button):
    p = dict(DEFAULTS, **picks)
    classes = ["ground"] + [f"{layer[:2]}-{opt}" for layer, opt in p.items() if opt not in ("none", "off")]
    bg = []
    if p["scene"] == "painted-ground":
        bg.append('<div class="bg-scene"><i class="p-face"></i><i class="p-shade"></i><i class="p-lit"></i><i class="p-leaf"></i></div>')
    if p["pattern"] != "none":
        bg.append('<div class="bg-pattern"></div>')
    if p["texture"] != "none":
        bg.append('<div class="bg-texture"></div>')
    if p["drawings"] == "lots":
        bg.append('<div class="bg-drawings"></div>')
    if p["drawings"] != "none":
        bg.append(signs_html(LOTS if p["drawings"] == "lots" else FEW))
    corner = ('<svg class="sign ink" viewBox="0 0 100 100" aria-hidden="true" focusable="false"><use href="#sg-rose"/></svg>'
              if p["drawings"] == "lots" else "")
    sheet = (f'<div class="sheet">{corner}<h3>{name}</h3><p class="id">{idline}</p><p>{line}</p>'
             f'<button class="btn" type="button">{button}</button></div>')
    inner = (f'<div class="bg" aria-hidden="true">{"".join(bg)}</div>' if bg else "")
    inner += FINDS if p["finds"] == "on" else ""
    inner += SCENE.format(sheet=sheet) if p["scene"] == "one-long-scene" else sheet
    if p["pattern"] == "coloured-bands":
        inner += '<p class="on-band">Pale words can sit straight on a deep band.</p>'
    return f'<section class="swatch" data-option="{option}">\n<div class="{" ".join(classes)}">\n{inner}\n</div>\n</section>\n'


TITLES = {"texture": "Texture", "pattern": "Pattern", "drawings": "Drawings", "finds": "Things to find", "scene": "Scene"}

out = []
for layer, options in LAYERS.items():
    out.append(f'<h2 class="layer">{TITLES[layer]}</h2>\n')
    for oid, name, line, button in options:
        out.append(swatch(f"{layer}:{oid}", {layer: oid}, name, f"{layer}: {oid}", line, button))
out.append('<h2 class="layer">Starting points</h2>\n')
for sid, name, picks, line, button in STARTS:
    idline = "; ".join(f"{k}: {v}" for k, v in picks.items()) or "every layer at its default"
    out.append(swatch(f"start:{sid}", picks, name, idline, line, button))

faces, joints = stone_masks()
p_face, p_shade, p_lit, p_leaf = painted_masks()
tiles = {"GRAIN": grain_mask(), "GRAIN_SOFT": grain_mask(alpha=0.67), "MOTTLE": mottle_mask(), "STONE_FACES": faces, "STONE_JOINTS": joints,
         "P_FACE": p_face, "P_SHADE": p_shade, "P_LIT": p_lit, "P_LEAF": p_leaf, "P_RIDGE": ridge_mask(), "SIGNS": signs_mask()}
page = (HERE / "background-template.html").read_text(encoding="utf-8")
for k, v in tiles.items():
    page = page.replace("{{" + k + "}}", v)
page = page.replace("{{SWATCHES}}", "".join(out))
Path(sys.argv[1]).write_text(page, encoding="utf-8")
print("wrote", sys.argv[1], len(page), "bytes")

# the same tiles in the part guide's assembly blocks, so 'style css' lifts exactly what the swatch book shows
GUIDE = HERE.parents[2] / "style-part-background.md"
IN_GUIDE = {"grain": "GRAIN", "grain-soft": "GRAIN_SOFT", "mottle": "MOTTLE", "stone-faces": "STONE_FACES", "stone-joints": "STONE_JOINTS", "face": "P_FACE",
            "shade": "P_SHADE", "lit": "P_LIT", "leaf": "P_LEAF", "ridge": "P_RIDGE", "signs": "SIGNS"}
if GUIDE.is_file():
    text = GUIDE.read_text(encoding="utf-8")
    new, n = re.subn(r'(--background-(' + "|".join(IN_GUIDE) + r'): )url\("data:[^"]*"\)',
                     lambda m: m.group(1) + tiles[IN_GUIDE[m.group(2)]], text)
    if new != text:
        GUIDE.write_text(new, encoding="utf-8")
    print(f"redrew {n} tile(s) in {GUIDE.name}" + ("" if new != text else " (no change)"))
