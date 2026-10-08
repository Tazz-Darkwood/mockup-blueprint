"""Builds the corners-and-shapes swatch book (../shapes.html) from shapes-template.html beside this file.

It writes one swatch for each option of each layer (the other layers at their defaults), then one for each starting
point, in the guide's order. Every swatch holds the same things, so the shapes are the only thing that changes: a sheet,
a picture, two labels, a field shown with its focus ring, the main button, a tick box and a round choice. Run from this
folder:
    python3 shapes.py ../shapes.html"""
import sys
from pathlib import Path

HERE = Path(__file__).parent

DEFAULTS = {"corners": "slight", "controls": "plain", "labels": "plain", "pictures": "plain"}
SHORT = {"corners": "co", "controls": "ct", "labels": "la", "pictures": "pi"}

# each layer's options, in the guide's order: (id, name, a line for the sheet, the button's words)
LAYERS = {
    "corners": [
        ("sharp", "Sharp", "Square corners on every box: exact, official, printed.", "Apply"),
        ("slight", "Slight", "Two or three pixels: square at a glance, but not raw.", "Continue"),
        ("soft", "Soft", "Six pixels on buttons and cards: the usual calm interface.", "Book a call"),
        ("round", "Round", "Twelve pixels and up: soft, friendly, easy to like.", "Join in"),
        ("hand-cut", "Hand-cut", "Every corner a little different, as if cut with scissors.", "Sign up"),
        ("cut", "Cut", "Corners cut straight across, like a metal plate or a game panel.", "Enter"),
    ],
    "controls": [
        ("plain", "Plain", "Buttons and fields take the corners of every other box.", "Continue"),
        ("pill", "Pill", "The button is fully round at the ends; the field stays a box.", "Get started"),
        ("ticket", "Ticket", "The button has a bite out of each end, like a ticket.", "Get tickets"),
        ("tag", "Tag", "The button is a luggage tag: a pointed end with a hole in it.", "Way in"),
    ],
    "labels": [
        ("plain", "Plain", "Small boxes in the corners of every other box.", "Continue"),
        ("pill", "Pill", "Fully round ends: the usual chip and status badge.", "Continue"),
        ("luggage-tag", "Luggage tag", "Two corners cut off and a hole punched at one end.", "Continue"),
        ("hanging-tag", "Hanging tag", "Upright, shoulders cut, a hole at the top for the string.", "Continue"),
        ("ticket", "Ticket", "A half-circle bitten out of each end.", "Continue"),
        ("ribbon", "Ribbon", "A strip with a V cut into each end.", "Continue"),
        ("seal", "Seal", "A round stamp, a little uneven, pressed on slightly turned.", "Continue"),
    ],
    "pictures": [
        ("plain", "Plain", "A rectangle, in the small corners of the boxes round it.", "Continue"),
        ("rounded", "Rounded", "A clearly rounded rectangle, like a photo on a phone.", "Continue"),
        ("circle", "Circle", "A circle: for people, and for one thing seen up close.", "Continue"),
        ("arch", "Arch", "Round at the top and flat at the foot, like a window.", "Continue"),
        ("cut-corner", "Cut corner", "Two opposite corners cut straight across.", "Continue"),
        ("pebble", "Pebble", "A round shape that no compass drew.", "Continue"),
    ],
}

STARTS = [
    ("professional", "Professional", {"corners": "soft", "pictures": "rounded"}, "Small, even rounding; nothing cut or tied on.", "Book a call"),
    ("civic", "Civic", {"corners": "sharp"}, "Square everything: plain, exact, the same for everyone.", "Apply now"),
    ("warm", "Warm", {"corners": "hand-cut", "pictures": "pebble"}, "Scissor-cut corners and a pebble of a picture.", "Sign up"),
    ("soft-and-round", "Soft and round", {"corners": "round", "controls": "pill", "labels": "pill", "pictures": "circle"}, "Round all through: an app that wants to be liked.", "Get started"),
    ("artistic", "Artistic", {"labels": "seal"}, "Near-square boxes and the maker's seal.", "View the work"),
    ("sorcery", "Sorcery", {"labels": "seal", "pictures": "arch"}, "A scene in an arch, a wax seal, plain controls.", "Enter"),
    ("gilded-dark", "Gilded dark", {"corners": "cut", "labels": "ribbon", "pictures": "circle"}, "Cut-cornered panels, a round portrait, a ribbon.", "Play"),
    ("lantern-fair", "Lantern fair", {"controls": "tag", "labels": "hanging-tag"}, "Stall tags on string; links cut like tags.", "Book a stall"),
    ("field-journal", "Field journal", {"labels": "luggage-tag"}, "Plain pages with luggage tags on the walks.", "Join a walk"),
    ("repair-cafe", "Repair cafe", {"labels": "hanging-tag", "controls": "plain", "corners": "slight"}, "Brown repair tags tied on, square notices.", "Bring it in"),
]

TITLES = {"corners": "Corners", "controls": "Controls", "labels": "Labels", "pictures": "Pictures"}
NOTES = {
    "corners": "The radius of every box: the sheet, the field, the button and the tick box. Look at the sheet's corners and the field's focus ring, which follows them.",
    "controls": "The outline of the main button, and of the field. The button is pressed anywhere in its box, whatever its outline.",
    "labels": "The two small labels at the top of the sheet: a date and a mark that something is new.",
    "pictures": "The shape the picture on the left is cut to.",
}


def swatch(option, picks, name, idline, line, button):
    p = dict(DEFAULTS, **picks)
    classes = ["ground"] + [f"{SHORT[layer]}-{opt}" for layer, opt in p.items()]
    pic = ('<div class="pic"><svg viewBox="0 0 120 150" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
           '<use href="#view"/></svg></div>')
    labels = '<p class="labels"><span class="label l1">14 June</span><span class="label l2">New</span></p>'
    form = ('<div class="form"><label class="fld">Your name<input type="text" class="shown-focus" value="Ada Okafor" autocomplete="off"></label>'
            f'<button class="btn" type="button">{button}</button></div>'
            '<p class="ticks"><label><input type="checkbox" checked> Remind me</label>'
            '<label><input type="radio" checked> By email</label></p>')
    return (f'<section class="swatch" data-option="{option}">\n<div class="{" ".join(classes)}">\n'
            f'<div class="sheet">{pic}<div class="words">{labels}<h3>{name}</h3><p class="id">{idline}</p><p>{line}</p>{form}</div></div>\n'
            '</div>\n</section>\n')


out = []
for layer, options in LAYERS.items():
    out.append(f'<h2 class="layer">{TITLES[layer]}</h2>\n<p class="layer-note">{NOTES[layer]}</p>\n')
    for oid, name, line, button in options:
        out.append(swatch(f"{layer}:{oid}", {layer: oid}, name, f"{layer}: {oid}", line, button))
out.append('<h2 class="layer">Starting points</h2>\n<p class="layer-note">Saved sets of picks; any layer not named is at its default '
           '(corners: slight; controls: plain; labels: plain; pictures: plain).</p>\n')
for sid, name, picks, line, button in STARTS:
    idline = "; ".join(f"{k}: {v}" for k, v in picks.items())
    out.append(swatch(f"start:{sid}", picks, name, idline, line, button))

page = (HERE / "shapes-template.html").read_text(encoding="utf-8").replace("{{SWATCHES}}", "".join(out))
Path(sys.argv[1]).write_text(page, encoding="utf-8")
print("wrote", sys.argv[1], len(page), "bytes")
