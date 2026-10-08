"""Builds the light swatch book (../light.html) from light-template.html beside this file.

It writes one swatch for each option of each layer (the other layers at their defaults), then one for each starting
point, in the guide's order. Every swatch has the same things in it, so the light is the only thing that changes: a
raised sheet with a heading and a button, a stack of three cards (the top one torn and taped, to show paper on paper),
a ball that shows the bright side, and the light's own effect. Run from this folder:
    python3 light.py ../light.html"""
import sys
from pathlib import Path

HERE = Path(__file__).parent

DEFAULTS = {"direction": "overhead", "shadows": "soft", "glow": "none", "sky": "none", "focus": "none"}

# each layer's options, in the guide's order: (id, name, a line for the sheet, the button's words)
LAYERS = {
    "direction": [
        ("none", "None", "No source: shadows sit evenly all round, and nothing has a bright side.", "Read on"),
        ("overhead", "Overhead", "Light from straight above: every shadow falls just below.", "Continue"),
        ("top-left", "Top left", "Light from above and to the left, the long habit of screens.", "Open"),
        ("top-right", "Top right", "Light from above and to the right: a window on the other side.", "Open"),
        ("low-side", "Low side", "A low light from one side: long shadows, late in the day.", "Go on"),
    ],
    "shadows": [
        ("none", "None", "Nothing is raised: sheets are told apart by colour and line.", "Read on"),
        ("soft", "Soft", "Layered, tinted shadows that grow softer as things rise.", "Continue"),
        ("paper-lift", "Paper lift", "A tight contact line and a soft lift: paper lying on paper.", "Pin it up"),
        ("crisp", "Crisp", "A hard, flat offset with no blur, like a print or a cut-out.", "Join in"),
        ("deep", "Deep", "Heavy, dark shadows: panels standing well off a dark world.", "Enter"),
    ],
    "glow": [
        ("none", "None", "Nothing gives off light.", "Read on"),
        ("lamp", "Lamp", "One warm pool of light; the far side falls into shade.", "Come in"),
        ("edges", "Edges", "Thin rims of light round frames and controls.", "Claim"),
        ("bloom", "Bloom", "A soft haze round the brightest thing only: the main button.", "Begin"),
    ],
    "sky": [
        ("none", "None", "White light: the page keeps its own colours.", "Read on"),
        ("day", "Day", "A clear sky and a warm sun: shadows turn a little blue.", "Set out"),
        ("dusk", "Dusk", "Low, warm light from one side, violet overhead.", "Stay late"),
        ("night", "Night", "Moonlight: the scene goes blue and dim; sheets stay readable.", "Look up"),
        ("by-the-clock", "By the clock", "The light follows a clock. Four hours of it:", "See tonight"),
    ],
    "focus": [
        ("none", "None", "The light is even across the page.", "Read on"),
        ("spotlight", "Spotlight", "A pool of light on the main thing; it grows when you reach the button.", "Buy this"),
        ("vignette", "Vignette", "The corners fall into shade, so the eye stays in the middle.", "Look closer"),
    ],
}

STARTS = [
    ("flat-and-even", "Flat and even", {"direction": "none", "shadows": "none"}, "No light at all: a page, not a picture.", "Read on"),
    ("professional", "Professional", {"direction": "overhead", "shadows": "soft"}, "Soft, tinted elevation from above, used sparingly.", "Book a call"),
    ("warm", "Warm", {"direction": "top-left", "shadows": "paper-lift"}, "A kitchen table by a window: paper on paper.", "Order"),
    ("daylight", "Daylight", {"direction": "top-right", "shadows": "crisp", "sky": "day"}, "Bright open air: a high sun and hard little shadows.", "Set out"),
    ("moonlight", "Moonlight", {"direction": "top-left", "shadows": "soft", "sky": "night", "focus": "vignette"}, "Night, cool and quiet: everything visible but blue.", "Look up"),
    ("sky-by-the-clock", "Sky by the clock", {"direction": "overhead", "shadows": "soft", "sky": "by-the-clock"}, "The page keeps time. Four hours of it:", "See tonight"),
    ("almanac-plate", "Almanac plate", {"direction": "overhead", "shadows": "paper-lift", "sky": "by-the-clock", "glow": "bloom"}, "Printed charts under the visitor's own sky:", "Come and look"),
    ("one-light", "One light", {"direction": "top-left", "shadows": "soft", "glow": "lamp"}, "A room with one lamp in it; the rest falls away.", "Come in"),
    ("spotlight-on-the-main-thing", "Spotlight on the main thing", {"shadows": "soft", "focus": "spotlight"}, "The light picks out the one thing that matters.", "Buy this"),
    ("glow-on-edges", "Glow on edges", {"shadows": "deep", "glow": "edges"}, "Bright rims on small things, like a game screen.", "Claim"),
    ("sorcery", "Sorcery", {"direction": "low-side", "shadows": "deep", "glow": "lamp", "focus": "vignette"}, "A low lamp in a dark room; the corners are lost.", "Enter"),
    ("gilded-dark", "Gilded dark", {"direction": "overhead", "shadows": "deep", "glow": "edges", "sky": "day"}, "Panels over a bright painted world, rimmed in light.", "Play"),
    ("lantern-fair", "Lantern fair", {"direction": "top-right", "shadows": "paper-lift", "glow": "lamp", "sky": "night"}, "One paper lantern over a market at night.", "Book a stall"),
    ("field-journal", "Field journal", {"direction": "top-right", "shadows": "paper-lift", "sky": "day"}, "Taped-in pages in morning sun.", "Join a walk"),
    ("repair-cafe", "Repair cafe", {"direction": "top-left", "shadows": "crisp"}, "Cut card and pegboard: flat light, hard shadows.", "Bring it in"),
]

CHIPS = [("rise", "dawn"), ("noon", "noon"), ("set", "dusk"), ("night", "night")]
SKY = '<span class="fx fx-sky-mul" aria-hidden="true"></span><span class="fx fx-sky-scr" aria-hidden="true"></span>'
TITLES = {"direction": "Direction", "shadows": "Shadows", "glow": "Glow", "sky": "Sky", "focus": "Focus"}
NOTES = {
    "direction": "Where the light comes from. The sun mark shows it; every shadow and the ball's bright side follow it.",
    "shadows": "What raised things cast. The sheet stands highest, the button and the cards lie low. On the dark page, raised things are lighter instead, with a faint lit edge.",
    "glow": "Light given off by things. On a dark page it glows; on a light page it can only show as colour and as the shade round it.",
    "sky": "The colour of the light over the page. It tints the ground and the things on it, never the sheet with the words.",
    "focus": "Where the light leads the eye.",
}


def swatch(option, picks, name, idline, line, button):
    p = dict(DEFAULTS, **picks)
    classes = ["ground"] + [f"{layer[:2]}-{opt}" for layer, opt in p.items()]
    fx = []
    if p["direction"] != "none" and option.startswith("direction:"):
        fx.append('<svg class="sun-mark" viewBox="0 0 28 28" aria-hidden="true" focusable="false"><use href="#sun"/></svg>')
    if p["sky"] != "none":            # the sky first: a lamp at night is lit over the night, not dimmed by it
        fx.append(SKY)
    if p["glow"] == "lamp":
        fx.append('<div class="fx fx-lamp-shade" aria-hidden="true"></div><div class="fx fx-lamp-light" aria-hidden="true"></div><i class="lamp-src" aria-hidden="true"></i>')
    if p["focus"] == "vignette":
        fx.append('<div class="fx fx-vignette" aria-hidden="true"></div>')
    chips = ""
    if p["sky"] == "by-the-clock":
        chips = ('<ul class="chips" aria-label="The same light at four hours">' + "".join(
            f'<li><span class="chip" data-t="{t}" aria-hidden="true">{SKY}</span>{name} <span class="chip-time"></span></li>' for t, name in CHIPS) + "</ul>")
    sheet = (f'<div class="main"><div class="sheet"><h3>{name}</h3><p class="id">{idline}</p><p>{line}</p>{chips}'
             f'<button class="btn" type="button">{button}</button></div></div>')
    side = '<div class="side" aria-hidden="true"><div class="stack"><i></i><i></i><i class="torn"></i></div><div class="ball"></div></div>'
    return (f'<section class="swatch" data-option="{option}">\n<div class="{" ".join(classes)}">\n'
            f'{"".join(fx)}{sheet}{side}\n</div>\n</section>\n')


out = []
for layer, options in LAYERS.items():
    out.append(f'<h2 class="layer">{TITLES[layer]}</h2>\n<p class="layer-note">{NOTES[layer]}</p>\n')
    for oid, name, line, button in options:
        out.append(swatch(f"{layer}:{oid}", {layer: oid}, name, f"{layer}: {oid}", line, button))
out.append('<h2 class="layer">Starting points</h2>\n<p class="layer-note">Saved sets of picks; any layer not named is at its default.</p>\n')
for sid, name, picks, line, button in STARTS:
    idline = "; ".join(f"{k}: {v}" for k, v in picks.items())
    out.append(swatch(f"start:{sid}", picks, name, idline, line, button))

page = (HERE / "light-template.html").read_text(encoding="utf-8").replace("{{SWATCHES}}", "".join(out))
Path(sys.argv[1]).write_text(page, encoding="utf-8")
print("wrote", sys.argv[1], len(page), "bytes")
