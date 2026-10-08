"""Builds the density swatch book (../density.html) from density-template.html beside this file.

One swatch for each option of each layer (the other layers at their defaults), then one for each starting point, in
the guide's order. The spacing options are shown in words at real size, with a key of the four gaps. The other layers
are shown as a page in miniature: the same page laid out at full size in a window 1600 wide and a phone 390 wide, then
scaled down; the page itself is filled in from the template's <template id="mini"> when the book loads, so the file
stays small. Run from this folder:
    python3 density.py ../density.html"""
import sys
from pathlib import Path

HERE = Path(__file__).parent

DEFAULTS = {"spacing": "standard", "fill": "balanced", "layout": "single-column", "width": "standard", "rhythm": "even"}
# the fill and rhythm swatches show the page as a grid, so that a screen holds more than one section; fill also runs
# wide, so the empty margins of a standard page do not hide what the fill itself changes
SHOWN = {"fill": {"layout": "grid", "width": "wide"}, "rhythm": {"layout": "grid"}}
SHORT = {"spacing": "sp", "fill": "fi", "layout": "la", "width": "wi", "rhythm": "rh"}

# each layer's options, in the guide's order: (id, name, one sentence)
LAYERS = {
    "spacing": [
        ("airy", "Airy", "Large gaps, growing most on a wide screen: one thing at a time, read slowly."),
        ("standard", "Standard", "The general guide's scale: generous between sections, close inside them."),
        ("snug", "Snug", "Small gaps, nothing over 48 pixels: a full page that still groups clearly."),
        ("compact", "Compact", "The smallest gaps, for tools, tables and readouts used for a long sitting."),
    ],
    "fill": [
        ("open", "Open", "Most of each screen is left open; no decoration in the gaps."),
        ("balanced", "Balanced", "Room round each thing, and two or three drawn marks per screen."),
        ("full", "Full", "Every region of the screen holds content on plain panels; the gaps stay plain."),
        ("packed", "Packed", "Full, and every gap holds detail: drawn bands, signs in the margins."),
    ],
    "layout": [
        ("single-column", "Single column", "One column, things in the order they are needed."),
        ("margin-column", "Margin column", "Headings and particulars in a narrow column beside the main one."),
        ("two-columns", "Two columns", "The main thing and what goes with it, side by side."),
        ("grid", "Grid", "Many like things in tiles that wrap, as many across as fit."),
        ("staggered", "Staggered", "Things of different sizes, set off the straight lines."),
        ("panels", "Panels", "A screen laid out to the window: plain panels in the regions of a grid."),
    ],
    "width": [
        ("narrow", "Narrow", "The page is one reading column: the measure and its margins."),
        ("standard", "Standard", "The page stops at 72rem and centres; the ground shows at the sides."),
        ("wide", "Wide", "The page runs to 92rem, for galleries and catalogues; text keeps its measure."),
        ("full-bleed", "Full bleed", "Bands and pictures run to the window's edges; the content inside keeps to 72rem."),
    ],
    "rhythm": [
        ("even", "Even", "Every section the same gap, width and alignment: calm and orderly."),
        ("alternating", "Alternating", "Every other section on a band, and sides swapped: a beat down the page."),
        ("one-big-moment", "One big moment", "Sections are even, and one thing per screen is set large with space round it."),
    ],
}

STARTS = [
    ("minimal", "Minimal", {"spacing": "airy", "fill": "open", "layout": "margin-column", "width": "standard", "rhythm": "one-big-moment"}, "One thing at a time on an open page."),
    ("clean", "Clean", {"spacing": "standard", "fill": "open", "layout": "two-columns", "width": "standard", "rhythm": "even"}, "A normal amount on each screen, all of it lined up."),
    ("balanced", "Balanced", {"spacing": "standard", "fill": "balanced", "layout": "grid", "width": "full-bleed", "rhythm": "alternating"}, "Lively, with room to breathe."),
    ("full-but-quiet", "Full but quiet", {"spacing": "compact", "fill": "full", "layout": "panels", "width": "full-bleed", "rhythm": "even"}, "The whole window used, every panel calm inside."),
    ("busy", "Busy", {"spacing": "snug", "fill": "packed", "layout": "grid", "width": "standard", "rhythm": "even"}, "Fill the frame: narrow gaps, every one filled."),
    ("warm", "Warm", {"spacing": "standard", "fill": "balanced", "layout": "two-columns", "width": "full-bleed", "rhythm": "alternating"}, "Bands edge to edge, people at the top, a few marks."),
    ("artistic", "Artistic", {"spacing": "airy", "fill": "open", "layout": "staggered", "width": "wide", "rhythm": "one-big-moment"}, "The work large, off the centred column."),
    ("professional", "Professional", {"spacing": "airy", "fill": "open", "layout": "grid", "width": "standard", "rhythm": "even"}, "An orderly grid with generous space."),
    ("civic", "Civic", {"spacing": "standard", "fill": "open", "layout": "single-column", "width": "narrow", "rhythm": "even"}, "One readable column, nothing extra."),
    ("sorcery", "Sorcery", {"spacing": "snug", "fill": "packed", "layout": "single-column", "width": "full-bleed", "rhythm": "one-big-moment"}, "A scene at the top, then every gap filled."),
    ("gilded-dark", "Gilded dark", {"spacing": "snug", "fill": "full", "layout": "panels", "width": "full-bleed", "rhythm": "one-big-moment"}, "Heavy panels over one big painted world."),
    ("lantern-fair", "Lantern fair", {"spacing": "snug", "fill": "packed", "layout": "grid", "width": "full-bleed", "rhythm": "alternating"}, "Bands of stalls, bunting in every gap."),
    ("almanac-plate", "Almanac plate", {"spacing": "airy", "fill": "balanced", "layout": "two-columns", "width": "full-bleed", "rhythm": "alternating"}, "Sheets on one half, the scene on the other, turn about."),
    ("catalogue-of-glazes", "Catalogue of glazes", {"spacing": "airy", "fill": "open", "layout": "margin-column", "width": "standard", "rhythm": "alternating"}, "One piece to a screen, particulars in the margin."),
    ("field-journal", "Field journal", {"spacing": "standard", "fill": "balanced", "layout": "staggered", "width": "standard", "rhythm": "alternating"}, "Pages laid down a little out of line."),
    ("repair-cafe", "Repair cafe", {"spacing": "snug", "fill": "packed", "layout": "grid", "width": "standard", "rhythm": "alternating"}, "A full board: tags four across, a band at every break."),
]

TITLES = {"spacing": "Spacing", "fill": "Fill", "layout": "Layout", "width": "Width", "rhythm": "Rhythm"}
NOTES = {
    "spacing": "The gaps: inside an item, between items, between groups and between sections, and the page's side margin. Shown in words at real size, at this swatch's width; the key under each gives the four gaps measured here. Steps 1 to 6 of the scale never change, so controls and tap spacing are the same in every option.",
    "fill": "Shown with layout: grid and width: wide. How much of each screen is left open, and what fills the rest. Drawn signs stand for whatever decoration the other parts bring. The tinted boxes are the box count: the first screen cut into 10 by 6, a check anyone can make by eye.",
    "layout": "How things are arranged on a wide screen. On the phone every layout comes down to one column, except small tiles, two across.",
    "width": "How wide the page runs in a window 1600 pixels wide. The dashed blue lines mark the edges of the page's content.",
    "rhythm": "Shown with layout: grid, three screens deep. How one section follows the next; the dashed lines are the bottoms of the screens.",
}

REAL = """<div class="real {cls}">
<div class="group"><div class="head"><h4>Programme</h4><p>Three sessions this month, each about an hour.</p></div>
<ul><li><b>Morning session</b><span>Saturday, 10:00</span></li><li><b>Afternoon talk</b><span>Saturday, 14:30</span></li><li><b>Evening meeting</b><span>Tuesday, 19:00</span></li></ul></div>
<div class="group"><div class="head"><h4>Hold a place</h4><p>We will write back within a day.</p></div>
<form><label>Your name <input name="n" autocomplete="name"></label><button class="btn" type="submit">Hold a place</button></form></div>
<div class="key" aria-label="The four gaps, measured at this width">
<div>Inside an item <i style="width: var(--gap-inside)"></i><output></output></div>
<div>Between items <i style="width: var(--gap-items)"></i><output></output></div>
<div>Between groups <i style="width: var(--gap-groups)"></i><output></output></div>
<div>Between sections <i style="width: var(--gap-sections)"></i><output></output></div></div>
</div>"""


def classes(picks):
    p = dict(DEFAULTS, **picks)
    return " ".join(f"{SHORT[k]}-{v}" for k, v in p.items())


def mini(picks, screens=1, counted=False, guides=False):
    cls = classes(picks)
    extra = (" counted" if counted else "") + (" with-guides" if guides else "")
    return (f'<div class="stage{extra}" data-screens="{screens}" style="--screens:{screens}">'
            f'<div class="win desk" aria-hidden="true"><div class="vp"><div class="pg {cls}"></div></div></div>'
            f'<div class="win phone" aria-hidden="true"><div class="vp"><div class="pg {cls}"></div></div></div></div>'
            f'<p class="caption">Left, a window 1600 pixels wide; right, a phone 390 wide, at the same scale.'
            f'{" <span class=count></span>" if counted else ""}</p>')


def swatch(option, picks, name, idline, line, layer):
    if layer == "spacing":
        body = REAL.format(cls=classes(picks))
    else:
        shown = dict(SHOWN.get(layer, {}), **picks)
        body = mini(shown, screens={"rhythm": 3, "width": 1}.get(layer, 2),
                    counted=layer in ("fill", "start"), guides=layer == "width")
    stack = "" if layer == "spacing" else " data-stack"   # whole-page miniatures: light above dark, full width
    return (f'<section class="swatch" data-option="{option}"{stack}>\n<h3>{name}</h3><p class="id">{idline}</p>'
            f'<p class="what">{line}</p>\n{body}\n</section>\n')


out = []
for layer, options in LAYERS.items():
    out.append(f'<h2 class="layer">{TITLES[layer]}</h2>\n<p class="layer-note">{NOTES[layer]}</p>\n')
    for oid, name, line in options:
        out.append(swatch(f"{layer}:{oid}", {layer: oid}, name, f"{layer}: {oid}", line, layer))
out.append('<h2 class="layer">Starting points</h2>\n<p class="layer-note">Saved sets of picks, two screens deep, with the box count for the first screen.</p>\n')
for sid, name, picks, line in STARTS:
    idline = "; ".join(f"{k}: {v}" for k, v in picks.items())
    out.append(swatch(f"start:{sid}", picks, name, idline, line, "start"))

page = (HERE / "density-template.html").read_text(encoding="utf-8").replace("{{SWATCHES}}", "".join(out))
Path(sys.argv[1]).write_text(page, encoding="utf-8")
print("wrote", sys.argv[1], len(page), "bytes")
