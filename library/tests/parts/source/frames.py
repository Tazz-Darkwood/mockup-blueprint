"""Builds the frames swatch book (../frames.html) from frames-template.html beside this file.

It draws the shapes once (the torn outline of a sheet, the seams between sections, the corner pieces as masks whose only
job is their alpha), then writes one swatch for each option of each layer (the other layers at their defaults), then
one for each starting point, in the guide's order. Every swatch has the same things in it, so the frame is the only
thing that changes: a sheet with a short form (a field, a tick box, a button), a list of three items, and the next
section below on a band of colour. Run from this folder:
    python3 frames.py ../frames.html"""
import math, random, sys, urllib.parse
from pathlib import Path

HERE = Path(__file__).parent
R = random.Random(23)

DEFAULTS = {"border": "none", "edge": "straight", "section-edge": "straight", "ornament": "none", "dividers": "space", "controls": "fine"}
PREFIX = {"border": "bo", "edge": "ed", "section-edge": "se", "ornament": "or", "dividers": "dv", "controls": "co"}

# each layer's options, in the guide's order: (id, name, a line for the sheet)
LAYERS = {
    "border": [
        ("none", "None", "No line: space and the sheet's own colour do the grouping."),
        ("hairline", "Hairline", "One thin line in the line colour, all round."),
        ("rule", "Rule", "A heavy rule across the top, a hairline round the rest: a ledger."),
        ("double", "Double", "A heavy line and a thin one inside it, like a plate in a book."),
        ("inked", "Inked", "A thick, flat line in the ink colour, as if printed."),
        ("pen-line", "Pen line", "A line drawn round by hand, wobbling a little, gone over twice."),
        ("carved-band", "Carved band", "A band of carved beads between two fine rules."),
        ("metal-ring", "Metal ring", "A bevelled metal ring with a dark line round it."),
    ],
    "edge": [
        ("straight", "Straight", "A machine-cut sheet with straight sides."),
        ("cut", "Cut", "Cut by hand with scissors: not quite square, laid a little crooked."),
        ("torn", "Torn", "Torn from a pad: a ragged edge all round."),
        ("deckled", "Deckled", "Handmade paper: a soft, feathered edge."),
    ],
    "section-edge": [
        ("straight", "Straight", "One section simply stops where the next begins."),
        ("torn", "Torn", "The band below is torn across."),
        ("wavy", "Wavy", "A soft wave, like a hill in front of the next band."),
        ("contour", "Contour", "A skyline of land, traced along its top with a fine line."),
        ("valance", "Valance", "Scallops hang from the section above, like an awning."),
        ("band", "Band", "A strip of carved pattern between two fine rules."),
    ],
    "ornament": [
        ("none", "None", "Nothing on the border."),
        ("corners", "Corners", "A drawn piece in each corner."),
        ("studs", "Studs", "A round stud or rivet in each corner."),
        ("keystone", "Keystone", "One jewel set in the middle of the top edge."),
        ("crop-marks", "Crop marks", "Printer's marks just outside each corner."),
    ],
    "dividers": [
        ("space", "Space", "Space alone between items."),
        ("hairline", "Hairline", "A thin line between items."),
        ("dashed", "Dashed", "A dashed line, like a page to cut along."),
        ("double-rule", "Double rule", "A heavy rule over the list, thin ones between."),
        ("ornament", "Ornament", "A printer's mark between items."),
    ],
    "controls": [
        ("fine", "Fine", "Fields and tick boxes in a one-pixel line of the soft ink."),
        ("firm", "Firm", "Fields and tick boxes in a two-pixel line of the ink."),
    ],
}

# (id, name, picks, line, stand-ins for other parts)
STARTS = [
    ("none", "None", {"dividers": "ornament"}, "No frames: space, and a printer's mark between items.", ["flat"]),
    ("hairline", "Hairline", {"border": "hairline", "dividers": "hairline"}, "Thin lines round sheets and between items.", []),
    ("card", "Card", {}, "No line; the card is the light part's shadow and the corners part's radius.", ["rounded"]),
    ("torn-paper", "Torn paper", {"edge": "torn", "section-edge": "torn"}, "Torn sheets, and a torn edge between sections.", []),
    ("inked-panel", "Inked panel", {"border": "inked", "dividers": "hairline", "controls": "firm"}, "A thick printed line round each panel.", []),
    ("carved-plate", "Carved plate", {"border": "carved-band", "ornament": "corners", "section-edge": "band"}, "Framed like a plate: a carved band and corner pieces.", []),
    ("riveted-metal", "Riveted metal", {"border": "metal-ring", "ornament": "studs", "controls": "firm"}, "A metal ring with a rivet in each corner.", []),
    ("wavy-edge", "Wavy edge", {"section-edge": "wavy"}, "Plain sheets; a soft wave between sections.", []),
    ("warm", "Warm", {"edge": "cut", "section-edge": "torn", "dividers": "dashed"}, "Cut paper, a torn band, dashed lines between.", []),
    ("artistic", "Artistic", {"border": "pen-line", "section-edge": "torn", "dividers": "ornament"}, "A pen-drawn frame round the one thing that matters.", []),
    ("professional", "Professional", {"border": "rule", "dividers": "hairline"}, "Ruled like a ledger: a heavy rule over, thin ones under.", []),
    ("civic", "Civic", {"dividers": "hairline", "controls": "firm"}, "Almost no frames; fields with a firm, plain edge.", ["flat"]),
    ("sorcery", "Sorcery", {"border": "inked", "edge": "torn", "section-edge": "band", "ornament": "corners", "dividers": "ornament"}, "Torn parchment inked round, a carved band below.", []),
    ("gilded-dark", "Gilded dark", {"border": "metal-ring", "ornament": "keystone", "section-edge": "wavy", "controls": "firm"}, "A gilded ring with a jewel, over a rolling land.", []),
    ("lantern-fair", "Lantern fair", {"section-edge": "valance", "dividers": "dashed"}, "An awning's scallops over the stalls.", []),
    ("almanac-plate", "Almanac plate", {"border": "hairline", "ornament": "crop-marks", "section-edge": "contour", "dividers": "double-rule"}, "A printed plate: hairlines, a skyline traced in ink.", []),
    ("catalogue-of-glazes", "Catalogue of glazes", {}, "Nothing drawn at all: space does every job.", ["flat"]),
    ("field-journal", "Field journal", {"edge": "torn", "section-edge": "torn", "dividers": "hairline"}, "Torn-out pages, ruled lines in the log.", []),
    ("repair-cafe", "Repair cafe", {"edge": "cut", "section-edge": "band", "ornament": "studs", "dividers": "dashed", "controls": "firm"}, "Cut card pinned up, a strip of pattern, firm edges to write in.", []),
]

TITLES = {"border": "Border", "edge": "Edge of a sheet", "section-edge": "Edge between sections", "ornament": "Ornament",
          "dividers": "Dividers", "controls": "Controls"}
NOTES = {
    "border": "The line round a sheet or panel. Look at the sheet on the left; the list and the band are unchanged.",
    "edge": "The outline of the paper itself. On a shaped edge, the border is drawn as an outline that follows the shape.",
    "section-edge": "Where the section with the sheet meets the band of colour below it.",
    "ornament": "Pieces set on the border. Shown here on a hairline border, since an ornament needs a line to sit on.",
    "dividers": "What separates the items in the list on the right.",
    "controls": "The edge of the field and the tick box in the sheet. It must reach 3 to 1 against the sheet, so it is never the decorative line colour.",
}
ITEMS = [("Tue 14 Oct", "Bike and kettle repairs, from six"), ("Sat 18 Oct", "Mending clothes, with tea"), ("Thu 23 Oct", "Lamps and radios")]


def uri(svg):
    svg = " ".join(svg.split())
    return 'url("data:image/svg+xml,' + urllib.parse.quote(svg, safe=" =:/'(),.-;") + '")'


def tear(points=30, depth=1.7):
    """A torn outline as a clip-path polygon in percent: small ragged steps along each side, deeper in a few places."""
    pts = []
    def jag():
        return R.uniform(0, depth) * (2.2 if R.random() < 0.15 else 1)
    for i in range(points + 1):
        pts.append((i * 100 / points, jag() if 0 < i < points else 0.3))
    for i in range(1, points // 2):
        pts.append((100 - jag() * 0.8, i * 200 / points))
    for i in range(points, -1, -1):
        pts.append((i * 100 / points, 100 - (jag() if 0 < i < points else 0.3)))
    for i in range(points // 2 - 1, 0, -1):
        pts.append((jag() * 0.8, i * 200 / points))
    return "polygon(" + ", ".join(f"{x:.1f}% {y:.1f}%" for x, y in pts) + ")"


def torn_path(w=1200, h=24):
    x, d = 0, [f"M0 {h}V{R.uniform(8, 14):.0f}"]
    while x < w:
        x = min(w, x + R.uniform(14, 46))
        d.append(f"L{x:.0f} {R.uniform(2, 18):.0f}")
    return "".join(d) + f"V{h}Z"


def corner():
    """One corner piece, top left: an L of two strokes that curl at their ends, and a small leaf in the angle."""
    return ("<g fill='none' stroke='black' stroke-width='2.2' stroke-linecap='round'>"
            "<path d='M3 27V9Q3 3 9 3H27'/><path d='M27 3q2 4 -2 6'/><path d='M3 27q4 2 6 -2'/>"
            "<path d='M8 20V12Q8 8 12 8H20' stroke-width='1.2'/></g><path d='M10 10q7 0 8 8q-8 -1 -8 -8z'/>")


def corners():
    out = {}
    for name, t in (("tl", ""), ("tr", "translate(30 0) scale(-1 1)"), ("bl", "translate(0 30) scale(1 -1)"), ("br", "translate(30 30) scale(-1 -1)")):
        out[name] = uri(f"<svg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'><g transform='{t}'>{corner()}</g></svg>")
    return out


SEAMS = {
    "torn": f'<path fill="currentColor" d="{torn_path()}"/>',
    "wavy": '<path fill="currentColor" d="M0 24V12Q150 0 300 10T600 12T900 8T1200 12V24Z"/>',
    "contour": ('<path fill="currentColor" d="M0 24V16L90 9L170 13L260 4L330 10L420 7L520 15L610 6L700 11L790 2L880 12L960 9L1060 14L1130 6L1200 11V24Z"/>'
                '<path class="trace" d="M0 16L90 9L170 13L260 4L330 10L420 7L520 15L610 6L700 11L790 2L880 12L960 9L1060 14L1130 6L1200 11"/>'),
}


def swatch(option, picks, name, idline, line, standins=()):
    p = dict(DEFAULTS, **picks)
    if option.startswith("ornament:"):
        p["border"] = "hairline"
    classes = ["scene"] + [f"{PREFIX[layer]}-{opt}" for layer, opt in p.items()] + list(standins)
    if p["edge"] != "straight":
        classes.append("shaped")
    seam = ""
    se = p["section-edge"]
    if se in SEAMS:
        seam = f'<svg class="seam" viewBox="0 0 1200 24" preserveAspectRatio="none" aria-hidden="true" focusable="false">{SEAMS[se]}</svg>'
    elif se in ("valance", "band"):
        seam = '<div class="seam" aria-hidden="true"></div>'
    orn = '<span class="orn" aria-hidden="true"></span>' if p["ornament"] != "none" else ""
    items = "".join(f"<li><b>{d}</b>{t}</li>" for d, t in ITEMS)
    return (f'<section class="swatch" data-option="{option}">\n<div class="{" ".join(classes)}">\n<div class="top">'
            f'<div class="sheet">{orn}<h3>{name}</h3><p class="id">{idline}</p><p>{line}</p>'
            f'<p class="field"><label>Your name <input type="text" autocomplete="off"></label></p>'
            f'<p class="tick"><label><input type="checkbox" checked> Remind me the day before</label></p>'
            f'<button class="btn" type="button">Save a place</button></div>'
            f'<div class="list"><h4>Coming up</h4><ul class="items">{items}</ul></div></div>\n'
            f'<div class="low">{seam}<p>The next section starts here, on a band of colour.</p></div>\n</div>\n</section>\n')


out = []
for layer, options in LAYERS.items():
    out.append(f'<h2 class="layer">{TITLES[layer]}</h2>\n<p class="layer-note">{NOTES[layer]}</p>\n')
    for oid, name, line in options:
        out.append(swatch(f"{layer}:{oid}", {layer: oid}, name, f"{layer}: {oid}", line))
out.append('<h2 class="layer">Starting points</h2>\n<p class="layer-note">Saved sets of picks; any layer not named is at its default. '
           'A few also show stand-ins for other parts, since their look is mostly theirs: card has rounded corners; none, civic and catalogue of glazes have no shadow.</p>\n')
for sid, name, picks, line, standins in STARTS:
    idline = "; ".join(f"{k}: {v}" for k, v in picks.items()) or "every layer at its default"
    out.append(swatch(f"start:{sid}", picks, name, idline, line, standins))

c = corners()
style = (f'<style>:root {{ --tear: {tear()}; --corner-tl: {c["tl"]}; --corner-tr: {c["tr"]}; '
         f'--corner-bl: {c["bl"]}; --corner-br: {c["br"]}; }}</style>')
page = (HERE / "frames-template.html").read_text(encoding="utf-8")
page = page.replace("{{SWATCHES}}", "".join(out)).replace("{{SYMBOLS}}", "").replace("</head>", style + "\n</head>", 1)
Path(sys.argv[1]).write_text(page, encoding="utf-8")
print("wrote", sys.argv[1], len(page), "bytes")
