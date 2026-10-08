"""Builds the lettering swatch book (../lettering.html) from lettering-template.html beside this file.

It writes one swatch for each option of each layer, then one for each starting point, in the guide's order. Every
swatch holds the same things (a label, a heading in the display face, a sheet with a subheading, a paragraph in the
reading face, a figure and a button), so the layer is the only thing that changes. An option is shown with the
partners it is usually paired with (named in the swatch's top line), not with faces it fights. The three type scales
are worked out here, Utopia's way (a ratio at 320px and a larger one at 1240px, joined with clamp()), and written into
the page and printed so the guide can quote them. Run from this folder:
    python3 lettering.py ../lettering.html"""
import sys
from pathlib import Path

HERE = Path(__file__).parent
DEFAULTS = {"body": "humanist-sans", "display": "book-serif", "scale": "classic", "voice": "sentence-case", "marks": "none"}

BODY = {"humanist-sans": "Source Sans 3", "grotesque": "Karla", "geometric-sans": "Figtree", "book-serif": "Alegreya",
        "hyperlegible": "Atkinson Hyperlegible Next"}
DISPLAY = {"one-family": None, "book-serif": "Newsreader 600", "soft-serif": "Fraunces, SOFT 100", "quirky-grotesque": "Bricolage Grotesque 800",
           "fat-poster": "Caprasimo on cut blocks", "condensed-gothic": "League Gothic, capitals", "bladed": "Pirata One",
           "chiselled": "Cinzel Decorative, carved"}

# scale: (name, ratio on a phone at 320px, ratio at 1240px, which step each token is)
BODY_MIN, BODY_MAX, VW_MIN, VW_MAX = 17, 19, 320, 1240
SCALES = {
    "gentle": (1.2, 1.25, {"l": 2, "xl": 3, "xxl": 5}),
    "classic": (1.2, 1.333, {"l": 2, "xl": 3, "xxl": 5}),
    "dramatic": (1.2, 1.414, {"l": 2, "xl": 3, "xxl": 6}),
}


def fluid(a, b):
    """clamp() from a px at 320 to b px at 1240, with a rem part so the reader's text size still counts."""
    slope = (b - a) / (VW_MAX - VW_MIN)
    base = a - slope * VW_MIN
    r = lambda v: f"{v / 16:.4f}".rstrip("0").rstrip(".")
    return f"clamp({r(a)}rem, {r(base)}rem + {slope * 100:.3f}vw, {r(b)}rem)"


def scale_css():
    out, table = [], []
    for sid, (lo, hi, steps) in SCALES.items():
        toks = {"s": "0.875rem", "m": fluid(BODY_MIN, BODY_MAX)}
        row = {"s": (14, 14), "m": (BODY_MIN, BODY_MAX)}
        for name, n in steps.items():
            a, b = BODY_MIN * lo ** n, BODY_MAX * hi ** n
            toks[name] = fluid(round(a, 1), round(b, 1))
            row[name] = (round(a), round(b))
        out.append(f".scale-{sid} {{ " + " ".join(f"--text-{k}: {v};" for k, v in toks.items()) + " }")
        table.append((sid, row, toks))
    return "\n".join(out) + "\n.lt .r-xxl { font-size: var(--text-xxl); } .lt .r-xl { font-size: var(--text-xl); } .lt .r-l { font-size: var(--text-l); } .lt .r-m { font-size: var(--text-m); } .lt .r-s { font-size: var(--text-s); }", table


SCALE_CSS, SCALE_TABLE = scale_css()
SCALE_PX = {sid: row for sid, row, _ in SCALE_TABLE}

MARKET = dict(label="This Saturday", w1="Night", w2="market", sub="Forty stalls, <em>one car park</em>", wave="one car park",
              read="Stalls open at six under strings of lamps, and the hatch at the bakery van stays up till the bread is gone. "
                   "Bring a bag; <span class=\"hl\">most stalls take cards</span>, a few take only coins.",
              fig="£2", fact="a pitch, paid on the night", hand="bring a torch!", button="See the stalls")

# each layer's options, in the guide's order: (id, name, picks for the other layers to show it well, a line saying what it is)
LAYERS = {
    "body": [
        ("humanist-sans", "Humanist sans", {}, "The reading face: a sans drawn from the pen, open and calm."),
        ("grotesque", "Grotesque", {"display": "soft-serif"}, "The reading face: a plain, slightly quirky grotesque."),
        ("geometric-sans", "Geometric sans", {"display": "quirky-grotesque"}, "The reading face: round, even and modern."),
        ("book-serif", "Book serif", {"display": "one-family"}, "The reading face: a serif with a hand in it, here carrying the headings too."),
        ("hyperlegible", "Hyperlegible", {}, "The reading face: drawn so that no two letters can be mistaken."),
    ],
    "display": [
        ("one-family", "One family", {}, "No second face: the reading face, heavy and tight, does the headings."),
        ("book-serif", "Book serif", {}, "A readable serif for headings and figures."),
        ("soft-serif", "Soft serif", {"body": "grotesque"}, "Round, warm, a little old-fashioned."),
        ("quirky-grotesque", "Quirky grotesque", {"body": "geometric-sans"}, "A heavy sans with ink traps and odd widths."),
        ("fat-poster", "Fat poster", {"body": "hyperlegible", "scale": "dramatic"}, "Fat, soft letters on blocks of cut paper."),
        ("condensed-gothic", "Condensed gothic", {"body": "grotesque", "scale": "dramatic"}, "Tall, narrow capitals, like wood type on a bill."),
        ("bladed", "Bladed", {"body": "book-serif"}, "A blackletter with blades: a few words only."),
        ("chiselled", "Chiselled", {"voice": "tracked-capitals"}, "Carved capitals with an edge and a drop."),
    ],
    "scale": [
        ("gentle", "Gentle", {}, "Ratio 1.2 on a phone, 1.25 on a wide screen."),
        ("classic", "Classic", {}, "Ratio 1.2 on a phone, 1.333 on a wide screen."),
        ("dramatic", "Dramatic", {}, "Ratio 1.2 on a phone, 1.414 on a wide screen; the top step is one further."),
    ],
    "voice": [
        ("sentence-case", "Sentence case", {}, "Headings, labels and buttons written as sentences."),
        ("tracked-capitals", "Tracked capitals", {}, "Short labels in capitals, spaced 10 per cent apart."),
        ("capital-headings", "Capital headings", {}, "Short headings in capitals, a little spaced."),
        ("italic-accents", "Italic accents", {"display": "soft-serif", "body": "grotesque"}, "One phrase of a heading in the display face's real italic."),
    ],
    "marks": [
        ("none", "None", {"display": "soft-serif", "body": "grotesque"}, "Nothing drawn on the words."),
        ("pencil", "Pencil", {"display": "soft-serif", "body": "grotesque"}, "A ring round a word and a wavy line under a phrase."),
        ("highlighter", "Highlighter", {"display": "soft-serif", "body": "grotesque"}, "One phrase in the paragraph marked with a highlighter."),
        ("stamp", "Stamp", {"display": "soft-serif", "body": "grotesque"}, "A rubber stamp, tilted, on the sheet's edge."),
        ("handwriting", "Handwriting", {"display": "soft-serif", "body": "grotesque"}, "A few words in a handwriting face, with a drawn arrow."),
    ],
}

# starting points: (id, name, picks, words on the swatch)
ORDER = ['sober-pair', 'professional', 'civic', 'almanac-plate', 'soft-serif', 'catalogue-of-glazes', 'hand-marks', 'field-journal', 'lively-grotesque', 'artistic', 'poster-face', 'warm', 'lantern-fair', 'repair-cafe', 'bladed-letters', 'sorcery', 'chiselled-metal', 'gilded-dark']
STARTS = [
    ("sober-pair", "Sober pair", {}, dict(label="Biology tutoring, Leeds", w1="AP Biology,", w2="one to one", sub="Lessons in your kitchen or online", wave="or online",
        read="I taught biology for eleven years. Most students come to me eight weeks before the exam; the ones who come in September sleep better.", fig="£38", fact="an hour, first lesson free", button="Book a first lesson")),
    ("soft-serif", "Soft serif", {"body": "grotesque", "display": "soft-serif"}, dict(label="Made in small batches", w1="Soap from", w2="the garden", sub="Nettle, oat and marigold", wave="and marigold",
        read="Every bar is cut by hand and cured for six weeks on the shelf by the back door.", fig="£6", fact="a bar, or three for £16", button="See this week's soap")),
    ("lively-grotesque", "Lively grotesque", {"body": "geometric-sans", "display": "quirky-grotesque", "voice": "tracked-capitals"}, dict(label="Season two", w1="Grow a farm", w2="with friends", sub="Plant, trade, harvest", wave="harvest",
        read="Each player tends a few rows; the farm is shared, and so is the weather.", fig="12", fact="players on a farm", button="Start a farm")),
    ("poster-face", "Poster face", {"body": "hyperlegible", "display": "fat-poster", "scale": "dramatic"}, dict(label="Volunteers wanted", w1="Lend a", w2="hand", sub="Saturday mornings at the hall", wave="at the hall",
        read="Sort the donations, make the tea, chat to whoever comes in. No experience needed and you can leave at any time.", fig="3", fact="hours, once a month", button="Sign up for a shift")),
    ("bladed-letters", "Bladed letters", {"body": "book-serif", "display": "bladed"}, dict(label="The guild of small wands", w1="Wands &", w2="Curios", sub="Every wand tested", wave="tested",
        read="Results vary. Each piece is turned from fallen wood and comes with a note of what it has done so far.", fig="9", fact="wands left this season", button="See the stall")),
    ("chiselled-metal", "Chiselled metal", {"display": "chiselled", "voice": "tracked-capitals"}, dict(label="Choose your side", w1="Energy", w2="Eternal", sub="Your reward awaits", wave="awaits",
        read="Pick a side, claim a title, and come back tomorrow to see who is winning the argument.", fig="2", fact="sides, no truce", button="Accept quest")),
    ("hand-marks", "Hand marks", {"body": "grotesque", "display": "soft-serif", "marks": "pencil"}, dict(MARKET)),
    ("warm", "Warm", {"body": "hyperlegible", "display": "fat-poster", "scale": "dramatic", "marks": "pencil"}, dict(label="Everyone welcome", w1="Bring a", w2="dish", sub="The street supper, 14 June", wave="14 June",
        read="Tables down the middle of Clay Lane from four o'clock. Bring something to share and a chair if you have one.", fig="1", fact="long table, the whole street", button="Say you are coming")),
    ("artistic", "Artistic", {"body": "book-serif", "display": "one-family", "scale": "dramatic"}, dict(label="Spring exhibition", w1="Salt", w2="& ash", sub="Twenty-two prints by Mira Holt", wave="Mira Holt",
        read="Prints made with seawater and the ash of the old pier, shown together for the first time.", fig="22", fact="prints, until 30 May", button="Plan a visit")),
    ("professional", "Professional", {"scale": "gentle"}, dict(label="Accountants in Harrogate", w1="Your accounts,", w2="done on time", sub="For sole traders and small firms", wave="small firms",
        read="We file your return, answer your questions in plain words, and tell you what you owe a month before you owe it.", fig="£45", fact="a month, fixed", button="Book a call")),
    ("civic", "Civic", {"body": "hyperlegible", "display": "one-family", "scale": "gentle"}, dict(label="Bins and recycling", w1="Check your", w2="bin day", sub="Collections over the holidays", wave="holidays",
        read="Enter your postcode to see which bins are collected and when. Collections move by one day in the week after a bank holiday.", fig="1", fact="day later after a bank holiday", button="Check your bin day")),
    ("sorcery", "Sorcery", {"body": "book-serif", "display": "bladed", "scale": "dramatic"}, dict(label="Enrolment is open", w1="Quit tech", w2="for magic", sub="Leave your inbox at the door", wave="at the door",
        read="The tower takes twelve apprentices a year. You will lose your phone and gain a familiar; most think it a fair trade.", fig="12", fact="places, one cat each", button="Take the oath")),
    ("gilded-dark", "Gilded dark", {"display": "chiselled", "scale": "dramatic", "voice": "tracked-capitals"}, dict(label="New quest", w1="Choose", w2="your class", sub="The guild is recruiting", wave="recruiting",
        read="Tanks at the front, healers behind, and someone has to carry the snacks.", fig="40", fact="players in the guild", button="Join the guild")),
    ("lantern-fair", "Lantern fair", {"body": "hyperlegible", "display": "fat-poster", "scale": "dramatic", "voice": "tracked-capitals"}, dict(MARKET)),
    ("almanac-plate", "Almanac plate", {"voice": "tracked-capitals"}, dict(label="Tonight over Kielder", w1="Saturn rises", w2="at 21:40", sub="A clear night, little moon", wave="little moon",
        read="The dome opens at nine. Bring warm clothes; the telescope room is kept at the outside temperature so the mirror stays still.", fig="21:40", fact="Saturn above the trees", button="Book the telescope")),
    ("catalogue-of-glazes", "Catalogue of glazes", {"body": "grotesque", "display": "soft-serif", "voice": "italic-accents", "scale": "classic"}, dict(label="Autumn firing", w1="Glazes,", w2="<em>slowly</em>", sub="Nine pots from the <em>wood kiln</em>", wave="",
        read="Each pot sat three days in the kiln. The ash fell where it wanted; the glaze is what it left.", fig="9", fact="pots, one of each", button="See the pots")),
    ("field-journal", "Field journal", {"body": "hyperlegible", "marks": "pencil + stamp"}, dict(label="Walks this month", w1="The heron", w2="walk", sub="Round the reservoir, slowly", wave="slowly",
        read="Slow, free walks round Millbrook's reservoir, marsh and woods. The dawn walk is full; the evening one has room.", fig="6", fact="of 12 places left", button="Save a place")),
    ("repair-cafe", "Repair cafe", {"body": "hyperlegible", "display": "fat-poster", "scale": "dramatic", "voice": "tracked-capitals", "marks": "stamp"}, dict(label="Last Saturday of the month", w1="Toss it?", w2="No way!", sub="Bring it in broken", wave="broken",
        read="Kettles, lamps, jeans and bikes: our fixers show you how, and the tea is free. Saturday is full; Sunday still has room.", fig="31", fact="things fixed last time", button="Book a repair")),
]
STARTS.sort(key=lambda st: ORDER.index(st[0]))
NOTES = {
    "body": "The reading face. Each is shown under the heading face it is usually paired with, named in the top line.",
    "display": "The heading face and what is done to it. Each is shown over the reading face it is usually paired with.",
    "scale": "The sizes, as a ladder. The numbers are the size on a phone (320px) and on a wide window (1240px); between them they grow smoothly. Seen here at the window's width.",
    "voice": "Case and spacing on labels and headings.",
    "marks": "What is drawn on the words. All shown over the soft serif and a grotesque; each works with any faces.",
}
TITLES = {"body": "Body", "display": "Display", "scale": "Scale", "voice": "Voice", "marks": "Marks"}
RING = '<svg aria-hidden="true" focusable="false"><use href="#mk-ring"/></svg>'
WAVE = '<svg aria-hidden="true" focusable="false"><use href="#mk-wave"/></svg>'


def faces(p):
    body = BODY[p["body"]]
    disp = DISPLAY[p["display"]] or f"{body}, heavy"
    return f"{disp} over {body}"


def swatch(option, picks, idline, words):
    p = dict(DEFAULTS, **picks)
    classes = ["lt", "ground"] + [f"{layer}-{o}" for layer, opt in p.items() for o in opt.split(" + ")]   # a layer may take two: "pencil + stamp"
    w = dict(MARKET, **words)
    tag = f'<p class="tag">{idline} · {faces(p)}</p>'
    if option.startswith("scale:"):
        px = SCALE_PX[p["scale"]]
        rung = lambda cls, text, key: f'<p class="{cls}">{text} <small>{px[key][0]} to {px[key][1]}px</small></p>'
        title = ('<div class="ladder">' + rung("title r-xxl", "Plums", "xxl") + rung("sub r-xl", "Section", "xl")
                 + rung("sub r-l", "Subheading", "l") + rung("r-m", "Reading text", "m") + rung("label r-s", "A label", "s") + "</div>")
        sheet = (f'<div class="sheet"><p class="read r-m">The biggest words on the first screen take the top step; section headings the next; '
                 f'reading text never goes under 16 pixels.</p><button class="btn" type="button">{w["button"]}</button></div>')
        return f'<section class="swatch" data-option="{option}">\n<div class="{" ".join(classes)}">\n{tag}{title}{sheet}\n</div>\n</section>\n'
    w2 = w["w2"] if "<" in w["w2"] else f'<span class="ring">{w["w2"]}{RING}</span>'
    sub = w["sub"]
    if w["wave"] and w["wave"] in sub:
        sub = sub.replace(w["wave"], f'<span class="wave">{w["wave"]}{WAVE}</span>', 1)
    read = w["read"]
    if "hl" not in read:
        cut = read.find(". ") + 1 or len(read)
        read = f'<span class="hl">{read[:cut]}</span>{read[cut:]}'
    stamp = '<span class="stamp" aria-hidden="true">Full</span>' if "full" in read.lower() or option.startswith("marks:") else ""
    if option.startswith("marks:") and "full" not in read.lower():
        read += " Saturday is full; Sunday still has room."
    body = (f'<p class="label">{w["label"]}</p>\n<h3 class="title"><span class="w">{w["w1"]}</span> <span class="w">{w2}</span></h3>\n'
            f'<div class="sheet">{stamp}<p class="sub">{sub}</p><p class="read">{read}</p>'
            f'<p class="fact"><b class="fig">{w["fig"]}</b> {w["fact"]}</p>'
            f'<p class="hand"><svg class="arrow" aria-hidden="true" focusable="false"><use href="#mk-arrow"/></svg>{w["hand"]}</p>'
            f'<button class="btn" type="button">{w["button"]}</button></div>')
    return f'<section class="swatch" data-option="{option}">\n<div class="{" ".join(classes)}">\n{tag}{body}\n</div>\n</section>\n'


out = []
for layer, options in LAYERS.items():
    out.append(f'<h2 class="layer">{TITLES[layer]}</h2>\n<p class="layer-note">{NOTES[layer]}</p>\n')
    for oid, name, others, line in options:
        out.append(swatch(f"{layer}:{oid}", dict(others, **{layer: oid}), f"{layer}: {oid}", {}))
out.append('<h2 class="layer">Starting points</h2>\n<p class="layer-note">Saved sets of picks; any layer not named is at its default '
           '(humanist sans under a book serif, classic scale, sentence case, no marks).</p>\n')
for sid, name, picks, words in STARTS:
    out.append(swatch(f"start:{sid}", picks, f"start: {sid}", words))

page = (HERE / "lettering-template.html").read_text(encoding="utf-8").replace("{{SCALES}}", SCALE_CSS).replace("{{SWATCHES}}", "".join(out))
Path(sys.argv[1]).write_text(page, encoding="utf-8")
print("wrote", sys.argv[1], len(page), "bytes")
for sid, row, toks in SCALE_TABLE:
    print(sid, {k: v for k, v in row.items()}, round(row["xxl"][1] / BODY_MAX, 2), "x at wide;", round(row["xl"][1] / BODY_MAX, 2), "x section")
    for k, v in toks.items():
        print("   ", k, v)
