"""Builds the materials swatch book (../materials.html) from materials-template.html beside this file.

It draws the texture tiles as masks (black shapes whose only job is their alpha: the colour comes from the shared colour
names in CSS, so one tile works on a light page, a dark page and a lamplit one), and writes one swatch for each option of
each layer, then one for each starting point, in the guide's order. Every swatch has the same things in it, so the
material is the only thing that changes: a sheet with a heading, a line of text, a line of soft text and a button.
Run from this folder:
    python3 materials.py ../materials.html"""
import math, random, sys, urllib.parse
from pathlib import Path

HERE = Path(__file__).parent
R = random.Random(11)


def uri(svg):
    svg = " ".join(svg.split())
    return 'url("data:image/svg+xml,' + urllib.parse.quote(svg, safe=" =:/'(),.-;") + '")'


def noise(w, h, freq, alpha, octaves=2, seed=1, kind="fractalNoise", extra=""):
    """A noise tile turned into alpha only: alpha = a * red + b. Stitched, so it repeats without a seam."""
    a, b = alpha
    return uri(f"""<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'>
<filter id='n' x='0' y='0' width='100%' height='100%'><feTurbulence type='{kind}' baseFrequency='{freq}' numOctaves='{octaves}' seed='{seed}' stitchTiles='stitch'/>
<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  {a} 0 0 0 {b}'/></filter>
<rect width='{w}' height='{h}' filter='url(#n)'/>{extra}</svg>""")


def fibres(size=260, count=46):
    """Paper fibre: fine speckle and a few short, curled fibres lying every way, each drawn again a tile away where it crosses an edge."""
    paths = []
    for _ in range(count):
        x, y = R.uniform(0, size), R.uniform(0, size)
        ang, ln = R.uniform(0, math.tau), R.uniform(6, 18)
        bend = R.uniform(-5, 5)
        x2, y2 = x + math.cos(ang) * ln, y + math.sin(ang) * ln
        cx, cy = (x + x2) / 2 - math.sin(ang) * bend, (y + y2) / 2 + math.cos(ang) * bend
        d = f"M{x:.1f} {y:.1f}Q{cx:.1f} {cy:.1f} {x2:.1f} {y2:.1f}"
        op = R.choice([0.35, 0.5, 0.7])
        for ox in (-size, 0, size):
            for oy in (-size, 0, size):
                if (ox, oy) == (0, 0) or (min(x, x2) - 20 + ox < size and max(x, x2) + 20 + ox > 0 and min(y, y2) - 20 + oy < size and max(y, y2) + 20 + oy > 0):
                    paths.append(f"<path d='{d}' transform='translate({ox} {oy})' opacity='{op}'/>")
    strokes = f"<g fill='none' stroke='black' stroke-width='0.7' stroke-linecap='round'>{''.join(paths)}</g>"
    return noise(size, size, 0.85, (2.2, -1.0), extra=strokes)


def scratches(size=300, count=34):
    """Scuffs: short straight scratches, mostly one way, as a hand drags a thing across a table."""
    out = []
    for _ in range(count):
        x, y = R.uniform(0, size), R.uniform(0, size)
        ang = R.gauss(-0.35, 0.5)
        ln = R.uniform(8, 30)
        x2, y2 = x + math.cos(ang) * ln, y + math.sin(ang) * ln
        out.append(f"<path d='M{x:.1f} {y:.1f}L{x2:.1f} {y2:.1f}' opacity='{R.choice([0.4, 0.6, 0.9])}'/>")
    return uri(f"<svg xmlns='http://www.w3.org/2000/svg' width='{size}' height='{size}'><g stroke='black' stroke-width='0.8' stroke-linecap='round'>{''.join(out)}</g></svg>")


def wood(w=480, h=160, rings=26):
    """Wood grain: long, gently wavy lines along the board, closer in places, and one knot the lines bend round.
    Every wave has a whole number of periods across the tile, and lines near the top or bottom are drawn again a tile
    away, so it repeats without a seam."""
    out = []
    y = 0.0
    kx, ky = R.uniform(120, 360), R.uniform(50, 110)
    while y < h:
        y += R.choice([3, 4, 5, 6, 8, 11])
        a1, a2, p1, p2 = R.uniform(0.6, 2.2), R.uniform(0.3, 1.2), R.uniform(0, 6), R.uniform(0, 6)
        pts = []
        for i in range(0, w + 1, 16):
            dy = a1 * math.sin(i / w * 2 * math.pi + p1) + a2 * math.sin(i / w * 6 * math.pi + p2)
            d = math.hypot(i - kx, (y - ky) * 2.2)
            dy += 9 * math.exp(-(d / 34) ** 2) * (1 if y < ky else -1)         # the lines part round the knot
            pts.append(f"{i} {y + dy:.0f}")
        d = "M" + "L".join(pts)
        sw, op = R.choice([0.6, 0.8, 1.1, 1.6]), R.choice([0.35, 0.55, 0.8])
        for oy in (-h, 0, h):
            if oy == 0 or (oy < 0 and y > h - 14) or (oy > 0 and y < 14):
                out.append(f"<path d='{d}'" + (f" transform='translate(0 {oy})'" if oy else "") + f" stroke-width='{sw}' opacity='{op}'/>")
    knot = f"<ellipse cx='{kx:.0f}' cy='{ky:.0f}' rx='9' ry='4' fill='black' opacity='0.5'/><ellipse cx='{kx:.0f}' cy='{ky:.0f}' rx='15' ry='7' fill='none' stroke='black' opacity='0.4'/>"
    return uri(f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'><g fill='none' stroke='black' stroke-linecap='round'>{''.join(out)}</g>{knot}</svg>")


TILES = {
    "FIBRE": fibres(),
    "FORMATION": noise(300, 300, 0.03, (0.6, -0.31), octaves=3, seed=4),          # paper held to the light: soft clouds
    "MOTTLE": noise(520, 520, 0.009, (1.3, -0.48), octaves=4, seed=7),             # parchment's slow stains
    "WOOD": wood(),
    "BRUSHED": noise(480, 240, "0.002 0.75", (2.6, -1.05), octaves=2, seed=9),     # fine streaks one way
    "SPECKLE": noise(220, 220, 0.42, (9.0, -6.2), octaves=2, seed=5),              # sparse mineral flecks, or frost
    "SCUFF": scratches(),
    # stone: thin veins where turbulence crosses zero, and a slow cloud, both faint (the speckle grain's second layer)
    "VEIN": uri("""<svg xmlns='http://www.w3.org/2000/svg' width='560' height='380'>
<filter id='v' x='0' y='0' width='100%' height='100%'><feTurbulence type='turbulence' baseFrequency='0.006 0.011' numOctaves='4' seed='12' stitchTiles='stitch'/>
<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -5 0 0 0 0.5'/></filter>
<filter id='c' x='0' y='0' width='100%' height='100%'><feTurbulence type='fractalNoise' baseFrequency='0.008' numOctaves='3' seed='3' stitchTiles='stitch'/>
<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0.8 0 0 0 -0.36'/></filter>
<rect width='560' height='380' filter='url(#c)'/><rect width='560' height='380' filter='url(#v)'/></svg>"""),
    "KNOCK": noise(200, 200, 0.6, (-7.0, 4.9), octaves=3, seed=8),                 # mostly opaque, with holes: ink that did not take
    "PENCIL": noise(120, 120, 1.4, (-3.2, 2.75), octaves=1, seed=6),                # graphite: fine, even, a little broken
    "CHALK": noise(160, 160, "0.8 0.3", (-4.5, 3.25), octaves=2, seed=2),                 # finer, more holes: chalk on a rough face
}

DEFAULTS = {"sheet": "plain", "grain": "none", "fixing": "none", "wear": "none", "ink": "printed"}

# what each sheet is usually seen with: its swatch shows it so, so the sheet reads as itself at a glance
USUAL_GRAIN = {"plain": "none", "fine-paper": "fibre", "card": "fibre", "kraft": "fibre", "parchment": "fibre",
               "canvas": "weave", "glass": "none", "metal": "brushed"}

LAYERS = {
    "sheet": [
        ("plain", "Plain", "No material: one flat colour, the surface and nothing else.", "Read on"),
        ("fine-paper", "Fine paper", "A good sheet: bright, even, a faint cloud in it held to the light.", "Read the issue"),
        ("card", "Card", "Thick, matte card with a little colour in it: a label, a tag, a notice.", "Pin it up"),
        ("kraft", "Kraft", "Brown paper: a parcel, a bag, a price tag. Words on it are heavier.", "Add to bag"),
        ("parchment", "Parchment", "Old skin-paper, warm and uneven, with slow stains in it.", "Unroll it"),
        ("canvas", "Canvas", "Unbleached cloth: an awning, a banner, a stall's cover.", "Book a stall"),
        ("glass", "Glass", "Smoked glass over the world behind: it blurs what shows through.", "Enter"),
        ("metal", "Metal", "A brushed plate: a sheen across it and fine streaks one way.", "Engage"),
    ],
    "grain": [
        ("none", "None", "No fine texture: the sheet is smooth.", "Read on"),
        ("fibre", "Fibre", "Specks and short fibres, as in any paper made from pulp.", "Read on"),
        ("laid", "Laid", "Fine lines close together and a few far apart, as in hand-made paper.", "Read on"),
        ("weave", "Weave", "Threads crossing: linen, canvas, book cloth.", "Read on"),
        ("wood", "Wood", "Long streaks along the board, closer in places.", "Read on"),
        ("brushed", "Brushed", "Fine straight streaks one way: brushed steel or tin.", "Read on"),
        ("speckle", "Speckle", "Sparse flecks: stone, slate, terrazzo, or frost on glass.", "Read on"),
        ("graph", "Graph", "A printed grid in the line colour: a notebook or a chart.", "Read on"),
    ],
    "fixing": [
        ("none", "None", "The sheet lies flat and square: nothing holds it.", "Read on"),
        ("tape", "Tape", "Two strips of tape across the corners; the paper a little crooked.", "Stick it in"),
        ("pins", "Pins", "Two pushpins at the top: a notice on a board.", "Pin it up"),
        ("clips", "Clips", "A bulldog clip at the top: a list on a clipboard.", "Sign the list"),
        ("rivets", "Rivets", "A rivet in each corner: a plate fixed to a wall or a machine.", "Engage"),
        ("string", "String", "A tag on a string from a rail, through a punched, ringed hole.", "Take a tag"),
    ],
    "wear": [
        ("none", "None", "New: nothing has happened to it yet.", "Read on"),
        ("soft-edges", "Soft edges", "Edges gone darker with age and hands, the middle still clean.", "Read on"),
        ("creased", "Creased", "Folded once each way and opened out again.", "Read on"),
        ("stained", "Stained", "A cup ring in one corner and a blot in another.", "Read on"),
        ("scuffed", "Scuffed", "Fine scratches, worst near the corners.", "Read on"),
    ],
    "ink": [
        ("printed", "Printed", "Clean, even ink: the words as set.", "Read on"),
        ("stamped", "Stamped", "Headings rubber-stamped: a little tilted, ink that missed in places.", "Read on"),
        ("letterpress", "Letterpress", "Words pressed into the sheet: a lit edge inside every letter.", "Read on"),
        ("chalk", "Chalk", "Headings in chalk: rough, broken strokes.", "Read on"),
        ("pencil", "Pencil", "Headings in soft pencil, underlined by hand.", "Read on"),
    ],
}

STARTS = [
    ("fine-paper", "Fine paper", {"sheet": "fine-paper", "grain": "fibre"}, "Quiet, printed, careful: a good sheet on a desk.", "Read the issue"),
    ("paper-and-tape", "Paper and tape", {"sheet": "fine-paper", "grain": "fibre", "fixing": "tape", "ink": "pencil"}, "Made at a kitchen table by one person.", "Order one"),
    ("cut-paper-on-felt", "Cut paper on felt", {"sheet": "card", "fixing": "pins"}, "A club's notice board: card pinned up a little crooked.", "Sign up"),
    ("parchment-and-ink", "Parchment and ink", {"sheet": "parchment", "grain": "fibre", "wear": "soft-edges"}, "Old, hand-written, a little worn at the edges.", "Read the scroll"),
    ("stone-and-chalk", "Stone and chalk", {"sheet": "plain", "grain": "speckle", "wear": "scuffed", "ink": "chalk"}, "A slate someone has written on.", "Enter"),
    ("wood-and-canvas", "Wood and canvas", {"sheet": "canvas", "grain": "weave", "fixing": "string"}, "A market stall: canvas tags hung from an oak rail.", "Visit the stall"),
    ("metal-and-dark-glass", "Metal and dark glass", {"sheet": "glass", "fixing": "rivets"}, "A game's interface: smoked glass in riveted metal.", "Claim"),
    ("warm", "Warm", {"sheet": "card", "grain": "fibre", "fixing": "tape", "ink": "stamped"}, "Somebody's hand is visible: card, tape, a stamp.", "Join in"),
    ("sorcery", "Sorcery", {"sheet": "parchment", "grain": "fibre", "fixing": "pins", "wear": "stained"}, "Stained parchment nailed up in a dark room.", "Enter"),
    ("gilded-dark", "Gilded dark", {"sheet": "glass", "grain": "speckle", "fixing": "rivets", "wear": "scuffed"}, "Battered glass panes in riveted frames.", "Play"),
    ("lantern-fair", "Lantern fair", {"sheet": "kraft", "grain": "fibre", "fixing": "string", "ink": "stamped"}, "Brown paper tags on string at a night market.", "Book a stall"),
    ("almanac-plate", "Almanac plate", {"sheet": "fine-paper", "grain": "laid", "ink": "letterpress"}, "A printed plate from an old almanac, pressed into laid paper.", "Come and look"),
    ("catalogue-of-glazes", "Catalogue of glazes", {"sheet": "card"}, "A museum label: plain matte card, nothing else.", "See the pots"),
    ("field-journal", "Field journal", {"sheet": "fine-paper", "grain": "graph", "fixing": "clips", "wear": "creased", "ink": "pencil"}, "A notebook page clipped to a board, folded in a pocket.", "Join a walk"),
    ("repair-cafe", "Repair cafe", {"sheet": "card", "grain": "fibre", "fixing": "string", "wear": "scuffed", "ink": "stamped"}, "Manila repair tags, handled and stamped.", "Bring it in"),
]

TITLES = {"sheet": "Sheet", "grain": "Grain", "fixing": "Fixing", "wear": "Wear", "ink": "Ink"}
NOTES = {
    "sheet": "What the surfaces with words are made of. Each is shown with the grain it is usually seen with (named under its title), so it reads as itself.",
    "grain": "The fine texture on the sheet, seen close up. Shown on fine paper, except weave (on canvas), wood (on kraft), brushed (on metal) and speckle (on plain).",
    "fixing": "How a sheet is laid on. The paper may turn a little; the words never do.",
    "wear": "Age and handling. Shown on fine paper with fibre. Wear stays at the edges and corners, away from the words.",
    "ink": "How the marks sit on the sheet. Only headings and short labels change; reading text stays printed. Shown on fine paper with fibre, except chalk (on plain with speckle: a slate).",
}
SHOWN_ON = {"grain": {"sheet": "fine-paper"}, "wear": {"sheet": "fine-paper", "grain": "fibre"}, "ink": {"sheet": "fine-paper", "grain": "fibre"}}
INK_ON = {"chalk": {"sheet": "plain", "grain": "speckle"}}
GRAIN_ON = {"brushed": "metal", "speckle": "plain", "wood": "kraft", "weave": "canvas"}

PIN = '<svg class="pin" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><use href="#pin"/></svg>'
FIX = {
    "none": "",
    "tape": '<span class="fix" aria-hidden="true"><i class="tape tape-l"></i><i class="tape tape-r"></i></span>',
    "pins": f'<span class="fix" aria-hidden="true">{PIN}{PIN}</span>',
    "clips": '<span class="fix" aria-hidden="true"><svg class="clip" viewBox="0 0 64 44" aria-hidden="true" focusable="false"><use href="#clip"/></svg></span>',
    "rivets": '<span class="fix" aria-hidden="true"></span>',
    "string": '<span class="fix" aria-hidden="true"><i class="rail"></i><i class="string"></i><i class="hole"></i></span>',
}


def swatch(option, picks, name, idline, line, button, shown=""):
    p = dict(DEFAULTS, **picks)
    classes = ["ground"] + [f"{layer[0]}-{opt}" for layer, opt in p.items()]
    sheet = (f'<article class="sheet">\n<span class="mat" aria-hidden="true"></span>{FIX[p["fixing"]]}\n'
             f'<h3>{name}</h3><p class="id">{idline}</p>{shown}<p>{line}</p>'
             f'<p class="soft">Soft text sits here too, at 4.5 to 1.</p>'
             f'<button class="btn" type="button">{button}</button>\n</article>')
    return (f'<section class="swatch" data-option="{option}">\n<div class="{" ".join(classes)}">\n'
            f'<span class="behind" aria-hidden="true"></span>\n{sheet}\n</div>\n</section>\n')


out = []
for layer, options in LAYERS.items():
    out.append(f'<h2 class="layer">{TITLES[layer]}</h2>\n<p class="layer-note">{NOTES[layer]}</p>\n')
    for oid, name, line, button in options:
        picks = {layer: oid}
        shown = ""
        if layer == "sheet" and USUAL_GRAIN[oid] != "none":
            picks["grain"] = USUAL_GRAIN[oid]
            shown = f'<p class="shown">shown with grain: {USUAL_GRAIN[oid]}</p>'
        elif layer in SHOWN_ON:
            base = dict(SHOWN_ON[layer])
            if layer == "grain" and oid in GRAIN_ON:
                base["sheet"] = GRAIN_ON[oid]
            if layer == "ink" and oid in INK_ON:
                base = dict(INK_ON[oid])
            picks = dict(base, **picks)
            shown = '<p class="shown">shown on ' + "; ".join(f"{k}: {v}" for k, v in base.items()) + "</p>"
        out.append(swatch(f"{layer}:{oid}", picks, name, f"{layer}: {oid}", line, button, shown))
out.append('<h2 class="layer">Starting points</h2>\n<p class="layer-note">Saved sets of picks; any layer not named is at its default (plain, no grain, no fixing, no wear, printed).</p>\n')
for sid, name, picks, line, button in STARTS:
    idline = "; ".join(f"{k}: {v}" for k, v in picks.items())
    out.append(swatch(f"start:{sid}", picks, name, idline, line, button))

page = (HERE / "materials-template.html").read_text(encoding="utf-8").replace("{{SWATCHES}}", "".join(out))
for k, v in TILES.items():
    page = page.replace("{{" + k + "}}", v)
Path(sys.argv[1]).write_text(page, encoding="utf-8")
print("wrote", sys.argv[1], len(page), "bytes")
