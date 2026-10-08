"""Builds the picture-style swatch book (../pictures.html) from pictures-template.html beside this file.

One subject (a dipped jug and a cup on a table, a sprig in the jug, a sun behind) is drawn in every technique, so the
technique is the only thing that changes between those swatches. Every drawing is a <symbol> in one shared <defs>
outside the swatches (swatches.js copies each swatch for the dark page and strips ids inside it), coloured only by the
shared colour names through classes and custom properties, which reach into a <use> by inheritance. The treatments
are CSS over the photograph (pictures.jpg beside this file: "Making pottery" by Jared Sluyter, CC0, from Unsplash via
Wikimedia Commons) and over one of the drawings. Run from this folder:
    python3 pictures.py ../pictures.html"""
import math, random, re, sys
from pathlib import Path

HERE = Path(__file__).parent
R = random.Random(11)
W, H = 320, 220

# ---------------------------------------------------------------- the subject's geometry (viewBox 0 0 320 220)
JUG = ("M120 70H160C158 80 154 86 156 94C186 106 196 140 184 166C178 178 172 184 166 186H114C108 184 102 178 96 166"
       "C84 140 94 106 124 94C126 86 122 80 120 70Z")
SPOUT = "M122 70L105 61C109 70 115 77 123 81Z"
HANDLE = "M157 100C190 92 204 120 182 146"
CLAY = "M80 150C100 144 116 156 136 150S170 144 200 152V200H80Z"      # below the dip line, clipped by the jug
CUP = "M212 150H254C254 168 249 183 241 186H225C217 183 212 168 212 150Z"
CUP_HANDLE = "M253 156C268 155 268 175 250 176"
STEM = "M140 72C136 52 144 36 150 16"
LEAVES = [(138, 58, -150, 1.1), (143, 47, -25, 1.0), (141, 36, -145, 0.9), (147, 28, -30, 0.85), (149, 19, -100, 0.7)]
LEAF = "M0 0C5 -6 14 -6 19 0C14 6 5 6 0 0Z"
SUN = (252, 58, 26)
# the outline as open strokes, for the line techniques (each a separate mark of the pen)
LINES = [
    "M124 94C94 106 84 140 96 166C102 178 108 184 114 186",
    "M156 94C186 106 196 140 184 166C178 178 172 184 166 186",
    "M112 186L168 186", "M118 70L162 70", "M120 70C122 80 126 86 124 94", "M160 70C158 80 154 86 156 94",
    "M120 71L105 62C109 70 115 77 123 81", HANDLE,
    "M93 150C104 146 118 155 136 150C150 146 170 145 188 151",
    "M212 150L254 150", "M212 150C212 168 217 183 225 186L241 186C249 183 254 168 254 150", CUP_HANDLE,
    "M8 188C100 186 220 189 312 187", STEM,
]


def leaves(cls="", extra=""):
    return "".join(f'<path class="{cls}" d="{LEAF}" transform="translate({x} {y}) rotate({a}) scale({s})"{extra}/>' for x, y, a, s in LEAVES)


def leaf_lines(cls):
    out = []
    for x, y, a, s in LEAVES:
        out.append(f'<path class="{cls}" d="{LEAF}M2 0H17" transform="translate({x} {y}) rotate({a}) scale({s})"/>')
    return "".join(out)


# ---------------------------------------------------------------- a small path sampler, for brush strokes and hatching
def sample(d, n=10):
    """Points along a path written with absolute M, L, H, V and C only."""
    toks = re.findall(r"[MLHVCZ]|-?\d+\.?\d*", d)
    pts, i, cur, cmd = [], 0, (0, 0), None
    while i < len(toks):
        if toks[i] in "MLHVCZ":
            cmd = toks[i]; i += 1
            continue
        if cmd == "M":
            cur = (float(toks[i]), float(toks[i + 1])); i += 2; pts.append(cur); cmd = "L"
        elif cmd == "L":
            nxt = (float(toks[i]), float(toks[i + 1])); i += 2
            for k in range(1, 9):
                t = k / 8; pts.append((cur[0] + (nxt[0] - cur[0]) * t, cur[1] + (nxt[1] - cur[1]) * t))
            cur = nxt
        elif cmd in "HV":
            v = float(toks[i]); i += 1
            nxt = (v, cur[1]) if cmd == "H" else (cur[0], v)
            for k in range(1, 9):
                t = k / 8; pts.append((cur[0] + (nxt[0] - cur[0]) * t, cur[1] + (nxt[1] - cur[1]) * t))
            cur = nxt
        elif cmd == "C":
            c = [float(t) for t in toks[i:i + 6]]; i += 6
            p0, p1, p2, p3 = cur, (c[0], c[1]), (c[2], c[3]), (c[4], c[5])
            for k in range(1, n + 1):
                t = k / n; u = 1 - t
                pts.append((u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
                            u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1]))
            cur = p3
    return pts


def taper(d, width, rnd, swell=0.6):
    """A brush mark: the path as a filled shape that swells in the middle and comes to a point at both ends."""
    pts = sample(d)
    left, right = [], []
    for k, (x, y) in enumerate(pts):
        a, b = pts[max(0, k - 1)], pts[min(len(pts) - 1, k + 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(dx, dy) or 1
        nx, ny = -dy / ln, dx / ln
        t = k / (len(pts) - 1)
        w = width * (0.12 + 0.88 * math.sin(math.pi * t) ** swell) * rnd.uniform(0.85, 1.12) / 2
        left.append((x + nx * w, y + ny * w)); right.append((x - nx * w, y - ny * w))
    ring = left + right[::-1]
    return "M" + "L".join(f"{x:.0f} {y:.0f}" for x, y in ring) + "Z"


# ---------------------------------------------------------------- filters and clips, shared by every swatch
FILTERS = """
<filter id="pen" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.09" numOctaves="2" seed="4" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="torn" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.045" numOctaves="2" seed="9" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3.5" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="pencil" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="1" seed="3" result="g"/>
  <feColorMatrix in="g" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.9" result="gaps"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="5" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="2.5" xChannelSelector="R" yChannelSelector="G" result="d"/>
  <feComposite in="d" in2="gaps" operator="in"/></filter>
<filter id="pencil-b" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="1" seed="8" result="g"/>
  <feColorMatrix in="g" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.9" result="gaps"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="12" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3.5" xChannelSelector="R" yChannelSelector="G" result="d"/>
  <feComposite in="d" in2="gaps" operator="in"/></filter>
<filter id="wash" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="1.6" result="b"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" seed="2" result="n"/>
  <feDisplacementMap in="b" in2="n" scale="9" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="mist" x="-20%" y="-30%" width="140%" height="160%"><feGaussianBlur stdDeviation="5"/></filter>
<filter id="brush" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.06 0.12" numOctaves="3" seed="13" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="4" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="pen-ic" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.2" numOctaves="2" seed="21" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="2.8" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="core" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.09" numOctaves="2" seed="31" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="4" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="grainf"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch" result="n"/>
  <feColorMatrix in="n" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  2.4 0 0 0 -0.95" result="a"/><feComposite in="SourceGraphic" in2="a" operator="in"/></filter>
<filter id="gran" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="1" seed="4" result="n"/>
  <feColorMatrix in="n" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -1.6 0 0 0 1.55" result="a"/><feComposite in="SourceGraphic" in2="a" operator="in"/></filter>
<filter id="soft" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="2.2"/></filter>
<filter id="dry" x="-5%" y="-20%" width="110%" height="140%"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.55" numOctaves="2" seed="6" result="s"/>
  <feColorMatrix in="s" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -3.2 2.2" result="streaks"/>
  <feComposite in="SourceGraphic" in2="streaks" operator="in"/></filter>
<clipPath id="cl-jug"><path d="JUG"/></clipPath>
<clipPath id="cl-cup"><path d="CUP"/></clipPath>
<clipPath id="cl-clay"><path d="CLAYP"/></clipPath>
<clipPath id="cl-pic"><rect width="320" height="220"/></clipPath>
""".replace("JUG", JUG).replace("CUP", CUP).replace("CLAYP", CLAY)


def sym(id_, body, vb="0 0 320 220"):
    return f'<symbol id="{id_}" viewBox="{vb}">{body}</symbol>\n'


# ---------------------------------------------------------------- the eight techniques
def t_flat():
    return sym("t-flat-shapes", f"""
<rect class="c-sky" width="320" height="188"/><circle class="c-sun" cx="{SUN[0]}" cy="{SUN[1]}" r="{SUN[2]}"/>
<rect class="c-table" y="186" width="320" height="34"/>
<path class="c-stem" d="{STEM}"/>{leaves("c-leaf")}
<path class="c-glaze-line" d="{HANDLE}"/><path class="c-glaze" d="{SPOUT}"/><path class="c-glaze" d="{JUG}"/>
<path class="c-clay" d="{CLAY}" clip-path="url(#cl-jug)"/>
<path class="c-cup-line" d="{CUP_HANDLE}"/><path class="c-cup" d="{CUP}"/>""")


def t_cut():
    """Layered paper: every shape its own sheet, with a pale torn core showing at its edge and the light part's shadow,
    five layers deep (backdrop, sun and far hill, near hill and table, jug and cup, clay, handle and leaves), grained."""
    def piece(d, cls, tr=""):
        t = f' transform="{tr}"' if tr else ""
        return f'<g class="cut"{t}><path class="core" d="{d}"/><path class="{cls}" d="{d}"/></g>'
    leaf_d = "".join(f'<path d="{LEAF}" transform="translate({x} {y}) rotate({a}) scale({s})"/>' for x, y, a, s in LEAVES)
    jug_handle = "M157 98C194 86 210 122 184 152L176 146C196 122 186 102 158 108Z"
    cup_handle = "M252 154C272 152 273 179 249 179L250 172C263 172 263 160 252 160Z"
    stem = "M138 76C134 52 142 34 148 14L152 15C146 36 140 54 143 76Z"
    return sym("t-cut-paper", f"""
<rect class="c-sky" width="320" height="220"/>
{piece(f"M{SUN[0] - SUN[2]} {SUN[1]}a{SUN[2]} {SUN[2]} 0 1 0 {2 * SUN[2]} 0a{SUN[2]} {SUN[2]} 0 1 0 {-2 * SUN[2]} 0Z", "c-sun")}
{piece("M-10 150C40 120 80 136 120 126S200 112 240 124S300 130 330 120V200H-10Z", "c-hill-far")}
{piece("M-10 188C40 152 90 168 130 160S230 142 330 170V200H-10Z", "c-hill")}
{piece("M-8 183L328 189V228H-8Z", "c-table")}
{piece(stem, "c-stem-fill")}<g class="cut"><g class="core">{leaf_d}</g><g class="c-leaf">{leaf_d}</g></g>
{piece(jug_handle, "c-glaze", "rotate(-2 140 130)")}{piece(JUG + SPOUT, "c-glaze", "rotate(-2 140 130)")}
<g transform="rotate(-2 140 130)"><g clip-path="url(#cl-jug)">{piece("M70 152C100 142 116 158 136 151S172 143 210 154V210H70Z", "c-clay")}</g></g>
{piece(cup_handle, "c-cup", "rotate(3 232 168)")}{piece(CUP, "c-cup", "rotate(3 232 168)")}
<rect class="paper-grain" width="320" height="220" filter="url(#grainf)"/>""")


def t_ink_line():
    rnd = random.Random(3)
    lines = "".join(f'<path d="{d}"/>' for d in LINES)
    return sym("t-ink-line", f"""
<rect class="c-paper" width="320" height="220"/>
<g transform="translate(5 4)"><circle class="c-sun-wash" cx="{SUN[0]}" cy="{SUN[1]}" r="{SUN[2] - 3}"/>
  <path class="c-glaze-wash" d="{JUG}"/><path class="c-cup-wash" d="{CUP}"/>{leaves("c-leaf-wash")}</g>
<path class="c-clay-wash" d="{CLAY}" clip-path="url(#cl-jug)"/>
<g class="ink" filter="url(#pen)">{lines}<circle cx="{SUN[0]}" cy="{SUN[1]}" r="{SUN[2]}"/>{leaf_lines("")}
  <path d="M100 120l6 -3M98 132l7 -2M176 128l5 4M178 140l5 3"/></g>""")


def hatch(x0, x1, y0, y1, step, angle, cls, rnd, jitter=0.6):
    """Straight hatching lines across a box at an angle, each a little uneven."""
    out = []
    a = math.radians(angle)
    dx, dy = math.cos(a), math.sin(a)
    span = math.hypot(x1 - x0, y1 - y0) / 2          # half the diagonal: every line that can cross the box, and no more
    k = -span
    while k < span:
        cx, cy = (x0 + x1) / 2 + k * -dy, (y0 + y1) / 2 + k * dx
        L = span
        out.append(f"M{cx - dx * L:.0f} {cy - dy * L + rnd.uniform(-jitter, jitter):.1f}L{cx + dx * L:.0f} {cy + dy * L:.0f}")
        k += step
    return f'<path class="{cls}" d="{"".join(out)}"/>'


def t_pencil():
    rnd = random.Random(5)
    lines = "".join(f'<path d="{d}"/>' for d in LINES)
    shade = hatch(150, 200, 96, 186, 4.2, 62, "", rnd)
    return sym("t-pencil", f"""
<rect class="c-paper" width="320" height="220"/>
<g class="wash" filter="url(#wash)"><circle class="c-sun-wash" cx="{SUN[0]}" cy="{SUN[1]}" r="{SUN[2] + 2}"/>
  <path class="c-glaze-wash" d="{JUG}"/><path class="c-cup-wash" d="{CUP}"/><path class="c-table-wash" d="M0 188H320V220H0Z"/></g>
<g class="graphite" filter="url(#pencil)">{lines}<circle cx="{SUN[0]}" cy="{SUN[1]}" r="{SUN[2]}"/>{leaf_lines("")}</g>
<g class="graphite again" filter="url(#pencil-b)" transform="translate(0.8 -0.6)">{"".join(f'<path d="{d}"/>' for d in LINES[:4])}</g>
<g class="graphite light" filter="url(#pencil)"><g clip-path="url(#cl-jug)">{shade}</g>
  <g clip-path="url(#cl-cup)">{hatch(238, 256, 150, 186, 3.6, 62, "", rnd)}</g>
  <path d="M168 194l30 2M176 199l34 1M186 204l26 1"/></g>
<path class="ring" filter="url(#pen)" d="M262 160C270 140 236 132 214 138C192 146 198 184 222 192C248 199 276 186 268 158C265 150 256 144 246 142"/>""")


def t_ink_wash():
    """Brush and ink: a pale first wash and a darker second, wet edges darker than the middle, ink pooled at the foot,
    pigment granulating, then the brush lines, and dry-brush strokes for the ground."""
    rnd = random.Random(8)
    strokes = [taper("M124 94C94 106 84 140 96 166C102 178 108 184 114 186", 9, rnd),
               taper("M156 94C186 106 196 140 184 166C178 178 172 184 166 186", 5, rnd),
               taper("M117 70L163 71", 5, rnd), taper("M111 187L169 185", 3.5, rnd),
               taper("M121 72C123 81 126 87 124 94", 3, rnd), taper("M159 72C157 81 154 87 156 94", 3, rnd),
               taper(HANDLE, 6, rnd), taper("M212 150C212 168 217 183 225 186L241 186C249 183 254 168 254 150", 4, rnd),
               taper(CUP_HANDLE, 3, rnd), taper(STEM, 3.5, rnd)]
    leafs = "".join(taper(f"M{x} {y}L{x + 18 * math.cos(math.radians(a)) * s:.1f} {y + 18 * math.sin(math.radians(a)) * s:.1f}", 7 * s, rnd, 0.9)
                    for x, y, a, s in LEAVES)
    dry = taper("M18 195C90 190 200 194 300 190", 9, rnd, 0.3) + taper("M60 203C120 200 170 203 230 201", 6, rnd, 0.3)
    marks = "".join(strokes)
    return f'<path id="iw-marks" d="{marks}"/>' + sym("t-ink-wash", f"""
<rect class="c-paper" width="320" height="220"/>
<g filter="url(#gran)"><path class="mist far" filter="url(#mist)" d="M-20 128C30 96 64 104 96 92C130 80 150 104 180 100C210 96 250 112 340 104V146C250 150 120 150 -20 146Z"/>
<path class="mist" filter="url(#mist)" d="M180 150C220 126 252 134 280 124C300 118 320 124 340 122V166C290 170 230 170 180 166Z"/></g>
<circle class="seal" filter="url(#pen)" cx="{SUN[0]}" cy="{SUN[1]}" r="{SUN[2] - 8}"/>
<g filter="url(#gran)"><path class="wash-1" filter="url(#wash)" d="{JUG}" transform="translate(-4 3)"/>
 <g clip-path="url(#cl-jug)"><path class="wash-2" filter="url(#wash)" d="M146 80C186 100 200 150 186 200H230V80Z"/>
  <path class="wet-edge" filter="url(#soft)" d="{JUG}"/><ellipse class="pool" filter="url(#soft)" cx="146" cy="184" rx="44" ry="11"/></g>
 <path class="wash-1" filter="url(#wash)" d="{CUP}" transform="translate(-2 2)"/>
 <g clip-path="url(#cl-cup)"><path class="wet-edge" filter="url(#soft)" d="{CUP}"/><ellipse class="pool" filter="url(#soft)" cx="234" cy="186" rx="20" ry="6"/></g></g>
<use href="#iw-marks" class="sumi-bleed" filter="url(#wash)"/>
<use href="#iw-marks" class="sumi" filter="url(#pen)"/><path class="sumi" filter="url(#pen)" d="{leafs}"/>
<path class="sumi dry" filter="url(#dry)" d="{dry}"/>""")


def t_painted():
    rnd = random.Random(13)
    def dabs(n, cls, box, w=(4, 9), ln=(20, 60), tilt=(-4, 4)):
        x0, y0, x1, y1 = box
        out = []
        for _ in range(n):
            x, y = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
            L = rnd.uniform(*ln)
            out.append(f'<path class="{cls}" d="M{x:.0f} {y:.0f}q{L / 2:.0f} {rnd.uniform(*tilt):.0f} {L:.0f} {rnd.uniform(-2, 2):.0f}" stroke-width="{rnd.uniform(*w):.1f}"/>')
        return "".join(out)
    body_lit = "".join(f'<path class="p-lit" d="M{102 + i * 5} {104 + i * 2}C{94 + i * 5} {124 + i} {96 + i * 5} {146 - i} {106 + i * 5} {164 - i * 2}" stroke-width="{rnd.uniform(4, 7):.1f}"/>' for i in range(4))
    body_dark = "".join(f'<path class="p-dark" d="M{170 + i * 4} {106 + i * 3}C{184 + i * 3} {124} {184 + i * 2} {146} {172 + i * 3} {172 - i * 3}" stroke-width="{rnd.uniform(4, 8):.1f}"/>' for i in range(4))
    return sym("t-painted", f"""
<rect class="c-sky" width="320" height="188"/>
<g filter="url(#brush)"><path class="p-sky-low" d="M-10 96H330V190H-10Z"/>{dabs(12, "p-sky-light", (-30, 6, 280, 90))}{dabs(10, "p-sky-warm", (-30, 96, 300, 150))}
<circle class="p-halo" cx="{SUN[0]}" cy="{SUN[1]}" r="{SUN[2] + 10}"/><circle class="p-sun" cx="{SUN[0]}" cy="{SUN[1]}" r="{SUN[2]}"/>
<path class="c-hill" d="M-10 190C40 152 90 170 130 162S230 146 330 172V200H-10Z"/>{dabs(8, "p-hill-dab", (-10, 160, 320, 182), (3, 6), (14, 36))}
<rect class="c-table" y="186" width="320" height="34"/>{dabs(12, "p-table-stroke", (-20, 190, 300, 216), (2, 5), (40, 100), (-1, 1))}
<path class="p-cast" d="M168 186C204 178 244 180 270 189L168 190Z"/><path class="p-cast" d="M252 186C266 182 284 184 294 189L252 190Z"/>
<path class="c-stem" d="{STEM}"/>{leaves("c-leaf")}{leaves("p-leaf-lit", ' style="translate: -1.5px -1px; scale: 0.8"')}
<path class="c-glaze-line" d="{HANDLE}"/><path class="p-dark" d="M176 100C196 106 200 124 186 144" stroke-width="3"/><path class="c-glaze" d="{SPOUT}"/><path class="c-glaze" d="{JUG}"/>
<g clip-path="url(#cl-jug)"><path class="p-shade" d="M156 60C196 92 206 150 180 200H230V60Z"/>{body_dark}{body_lit}<path class="c-clay" d="{CLAY}"/>
  <path class="p-clay-dark" d="M150 146C194 150 194 182 172 200H230V140Z"/><path class="p-lit" d="M100 158C104 172 110 180 118 184" stroke-width="5"/>
  <path class="p-glint" d="M112 112C108 120 108 128 110 134" stroke-width="4"/><path class="p-lit" d="M126 74L126 90" stroke-width="3"/></g>
<path class="c-cup-line" d="{CUP_HANDLE}"/><path class="c-cup" d="{CUP}"/>
<g clip-path="url(#cl-cup)"><path class="p-shade" d="M236 140C254 160 252 176 244 200H270V140Z"/><path class="p-lit" d="M218 156C218 166 220 174 224 180" stroke-width="4"/></g></g>""")


def t_engraved():
    rnd = random.Random(17)
    sky = []
    for y in range(4, 186, 4):
        sky.append(f"M0 {y}H320")
    body = "".join(f"M80 {y}Q140 {y + 9} 200 {y}" for y in range(98, 190, 4))
    cross = hatch(150, 200, 92, 190, 3.2, -35, "", rnd, 0.3)
    cup = "".join(f"M206 {y}Q233 {y + 6} 260 {y}" for y in [152 + i * 3.5 for i in range(11)])
    table = "".join(f"M0 {y:.1f}H320" for y in [188 + i * 2.6 for i in range(12)])
    lines = "".join(f'<path d="{d}"/>' for d in LINES)
    return sym("t-engraved", f"""
<rect class="c-paper" width="320" height="220"/>
<path class="e-fine" d="{''.join(sky)}"/>
<circle class="c-paper" cx="{SUN[0]}" cy="{SUN[1]}" r="{SUN[2] + 5}"/>
<path class="e-fine" d="{''.join(f'M{SUN[0] + (SUN[2] + 9) * math.cos(a * math.pi / 12):.1f} {SUN[1] + (SUN[2] + 9) * math.sin(a * math.pi / 12):.1f}L{SUN[0] + (SUN[2] + 17) * math.cos(a * math.pi / 12):.1f} {SUN[1] + (SUN[2] + 17) * math.sin(a * math.pi / 12):.1f}' for a in range(24))}"/>
<path class="c-paper" d="{JUG}"/><path class="c-paper" d="{CUP}"/><path class="c-paper" d="M0 186H320V220H0Z"/>
<path class="e-line" d="{table}"/>
<g clip-path="url(#cl-jug)"><path class="e-line" d="{body}"/><g class="e-line">{cross}</g>
  <g clip-path="url(#cl-clay)" class="e-line">{hatch(80, 200, 140, 190, 2.6, 35, "", rnd, 0.3)}</g></g>
<g clip-path="url(#cl-cup)"><path class="e-line" d="{cup}"/><g class="e-line">{hatch(234, 260, 150, 188, 3, -35, "", rnd, 0.3)}</g></g>
<g class="e-out">{lines}<circle cx="{SUN[0]}" cy="{SUN[1]}" r="{SUN[2]}"/>{leaf_lines("")}</g>""")


# ---------------------------------------------------------------- the jug as a line drawing, for the stroke layer
def jug_lines():
    return sym("jug-lines", "".join(f'<path d="{d}"/>' for d in LINES)
               + f'<circle cx="{SUN[0]}" cy="{SUN[1]}" r="{SUN[2]}"/>' + leaf_lines(""))


def jug_brush():
    rnd = random.Random(23)
    marks = [taper(d, 6 if i < 2 else 4.5, rnd) for i, d in enumerate(LINES)]
    marks.append(taper(f"M{SUN[0] - 26} {SUN[1]}C{SUN[0] - 26} {SUN[1] - 36} {SUN[0] + 26} {SUN[1] - 36} {SUN[0] + 26} {SUN[1]}"
                       f"C{SUN[0] + 26} {SUN[1] + 30} {SUN[0] - 18} {SUN[1] + 34} {SUN[0] - 24} {SUN[1] + 8}", 5, rnd))
    marks += [taper(f"M{x} {y}L{x + 18 * math.cos(math.radians(a)) * s:.1f} {y + 18 * math.sin(math.radians(a)) * s:.1f}", 7 * s, rnd, 0.9)
              for x, y, a, s in LEAVES]
    return sym("jug-brush", f'<path d="{"".join(marks)}"/>')


# ---------------------------------------------------------------- people, for the figures layer
def person_simple(x, skin, hair, shirt, hair_d, glasses=False):
    g = (f'<circle class="{skin}" cx="{x}" cy="96" r="21"/><path class="{hair}" d="{hair_d}"/>'
         f'<circle class="f-feature" cx="{x - 7}" cy="97" r="2.4"/><circle class="f-feature" cx="{x + 7}" cy="97" r="2.4"/>'
         f'<path class="f-smile" d="M{x - 6} 106q6 5 12 0"/>'
         f'<path class="{shirt}" d="M{x - 32} 186C{x - 33} 142 {x - 22} 124 {x} 124C{x + 22} 124 {x + 33} 142 {x + 32} 186Z"/>')
    if glasses:
        g += f'<g class="f-smile"><circle cx="{x - 7}" cy="97" r="5.5"/><circle cx="{x + 7}" cy="97" r="5.5"/><path d="M{x - 1.5} 97h3"/></g>'
    return g


def table_front():
    return ('<rect class="c-table" x="20" y="158" width="280" height="12" rx="2"/>'
            '<path class="c-table-line" d="M44 170L34 218M276 170L286 218M60 170L66 218M260 170L254 218"/>')


def people_simple():
    return sym("f-simple", '<rect class="c-sky" width="320" height="220"/>'
               + person_simple(92, "f-skin-3", "f-hair-1", "c-band-2", "M71 94C68 70 112 66 113 92C104 80 82 80 71 94Z")
               + person_simple(160, "f-skin-1", "f-hair-2", "c-band-1", "M139 98C134 66 186 66 181 98C178 84 166 78 160 79C152 78 142 84 139 98ZM150 74a10 10 0 1 1 20 0z", True)
               + person_simple(228, "f-skin-2", "f-hair-1", "c-band-3", "M207 92C206 74 222 70 236 74L250 70L248 90C236 82 220 82 207 92Z")
               + table_front()
               + '<path class="c-glaze" d="M150 158C148 146 154 138 160 136C166 138 172 146 170 158Z"/>')


def person_detail(x, skin, hair, shirt, look=0, long_hair=False):
    s = f"""
<path class="{skin}" d="M{x - 7} 112h14v16h-14z"/>
<path class="{shirt}" d="M{x - 37} 216L{x - 36} 188C{x - 38} 146 {x - 26} 126 {x} 125C{x + 26} 126 {x + 38} 146 {x + 36} 188L{x + 37} 216Z"/>
<path class="f-fold" d="M{x - 6} 126L{x} 140L{x + 6} 126M{x - 20} 150C{x - 22} 162 {x - 20} 174 {x - 16} 186M{x + 20} 150C{x + 22} 162 {x + 20} 174 {x + 16} 186"/>
<path class="f-shade" d="M{x + 12} 128C{x + 30} 134 {x + 38} 150 {x + 36} 188H{x + 20}C{x + 24} 160 {x + 20} 140 {x + 12} 128Z"/>
<ellipse class="{skin}" cx="{x}" cy="94" rx="17" ry="21"/>
<path class="f-shade" d="M{x + 8} 76C{x + 20} 84 {x + 20} 104 {x + 8} 114C{x + 14} 102 {x + 15} 88 {x + 8} 76Z"/>
<ellipse class="{skin}" cx="{x + 17}" cy="96" rx="3.5" ry="5.5"/>
<path class="f-line" d="M{x - 9 + look} 89q4 -2 7 0M{x + 3 + look} 89q4 -2 7 0M{x + look} 96l-2 7h4M{x - 5 + look} 108q5 3 10 0"/>
<circle class="f-feature" cx="{x - 5 + look}" cy="94" r="1.8"/><circle class="f-feature" cx="{x + 6 + look}" cy="94" r="1.8"/>"""
    if long_hair:
        s += f'<path class="{hair}" d="M{x - 19} 94C{x - 22} 66 {x + 22} 62 {x + 19} 92C{x + 22} 110 {x + 24} 126 {x + 16} 136C{x + 16} 118 {x + 14} 100 {x + 12} 84C{x + 2} 80 {x - 8} 82 {x - 14} 90C{x - 15} 110 {x - 12} 124 {x - 18} 134C{x - 26} 120 {x - 22} 104 {x - 19} 94Z"/>'
        s += f'<path class="f-strand" d="M{x - 10} 74C{x - 4} 70 {x + 6} 70 {x + 12} 76M{x - 14} 80C{x - 6} 74 {x + 6} 74 {x + 14} 82"/>'
    else:
        s += f'<path class="{hair}" d="M{x - 18} 90C{x - 20} 70 {x - 4} 66 {x + 4} 70C{x + 16} 68 {x + 22} 80 {x + 17} 90C{x + 12} 80 {x + 2} 78 {x - 6} 80C{x - 12} 82 {x - 15} 86 {x - 18} 90Z"/>'
        s += f'<path class="f-strand" d="M{x - 12} 76c6 -3 12 -3 18 0M{x - 8} 72c6 -2 12 -1 16 2"/>'
    s += (f'<path class="{shirt}" d="M{x - 30} 150C{x - 34} 156 {x - 26} 164 {x - 10} 160L{x + 4} 158L{x + 2} 150Z"/>'
          f'<ellipse class="{skin}" cx="{x + 8}" cy="155" rx="8" ry="5"/>')
    return s


def people_detailed():
    return sym("f-detailed", '<rect class="c-sky" width="320" height="220"/>'
               + person_detail(106, "f-skin-2", "f-hair-1", "c-band-3", 2, True)
               + person_detail(214, "f-skin-3", "f-hair-3", "c-band-2", -2)
               + table_front()
               + '<path class="c-glaze" d="M150 158C148 146 154 138 160 136C166 138 172 146 170 158Z"/>'
               + '<path class="f-line" d="M152 140h16"/>', "48 54 232 160")


def people_silhouettes():
    def body(x, top, extra):
        return (f'<circle cx="{x}" cy="{top}" r="15"/><path d="M{x - 6} {top + 10}h12v12h-12z"/>'
                f'<path d="M{x - 34} 170C{x - 34} {top + 32} {x - 24} {top + 22} {x} {top + 22}C{x + 24} {top + 22} {x + 34} {top + 32} {x + 34} 170Z"/>{extra}')
    a = body(108, 96, '<circle cx="96" cy="86" r="8"/>')                                            # hair in a bun
    b = body(214, 92, '<path d="M196 90C196 72 232 72 232 90ZM228 88h14v4h-14z"/>')                # a cap
    return sym("f-silhouettes", f"""<rect class="c-sky" width="320" height="220"/>
<circle class="c-sun" cx="162" cy="112" r="62"/><path class="c-hill" d="M-10 150C60 136 120 144 170 138S260 132 330 142V220H-10Z"/>
<g class="f-sil">{a}{b}<path d="{JUG}" transform="translate(119 100) scale(0.3)"/>
<rect x="20" y="156" width="280" height="12" rx="2"/><path d="M44 166L34 218M276 166L286 218" stroke-width="5"/></g>""")


def people_none():
    return sym("f-none", f"""<rect class="c-sky" width="320" height="220"/>
<rect class="c-table" x="20" y="158" width="280" height="12" rx="2"/><path class="c-table-line" d="M44 170L34 218M276 170L286 218M60 170L66 218M260 170L254 218"/>
<path class="c-glaze" d="M98 158C94 132 104 118 116 114C128 118 138 132 134 158Z"/><path class="c-clay" d="M96 146C108 142 120 150 136 146L134 158H98Z"/>
<path class="c-cup" d="M170 140H200C200 150 196 157 190 158H180C174 157 170 150 170 140Z"/>
<path class="c-cup" d="M224 158L230 118H268L274 158Z"/><path class="c-sun" d="M232 128H266L264 138H234Z"/>
<path class="c-stem" d="M116 114C114 98 120 88 124 76"/>""")


# ---------------------------------------------------------------- icons: one geometry, drawn four ways
# .b the body (a closed shape), .k a detail inside it (knocked out when filled), .o a detail outside it (always a line)
ICONS = {
    "home": ('<path class="b" d="M4 11L12 4L20 11V20H4Z"/><path class="k" d="M10 20V14H14V20"/>', "Home"),
    "find": ('<circle class="b" cx="10.5" cy="10.5" r="6.5"/><path class="o" d="M15.5 15.5L20.5 20.5"/><path class="k" d="M7.5 9a3.5 3.5 0 0 1 3 -2.5"/>', "Find"),
    "basket": ('<path class="b" d="M3.5 9.5H20.5L18.5 20H5.5Z"/><path class="o" d="M8 9.5L11 4M16 9.5L13 4"/><path class="k" d="M9 13V17M12 13V17M15 13V17"/>', "Basket"),
    "dates": ('<path class="b" d="M4 6H20V20H4Z"/><path class="k" d="M4 10.5H20M8 14H10M14 14H16M8 17H10"/><path class="o" d="M8 3V7.5M16 3V7.5"/>', "Dates"),
    "write": ('<path class="b" d="M5 19L5.8 15L15.5 5.3L18.7 8.5L9 18.2Z"/><path class="k" d="M13.6 7.2L16.8 10.4"/><path class="o" d="M13 19.5H20"/>', "Write"),
}


def icon_syms():
    return "".join(sym(f"i-{k}", v[0], "0 0 24 24") for k, v in ICONS.items())


def icon_row(sizes=False):
    items = "".join(f'<li><svg class="ic" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><use href="#i-{k}"/></svg><span>{v[1]}</span></li>'
                    for k, v in ICONS.items())
    return f'<ul class="icons">{items}</ul>'


# ---------------------------------------------------------------- swatches
PHOTO_ALT = "Clay-covered hands shaping a pot on a wheel, from above"


def photo(extra=""):
    return f'<img src="source/pictures.jpg" width="600" height="400" alt="{PHOTO_ALT}" loading="lazy" decoding="async"{extra}>'


def drawn(symbol, label, small=False):
    role = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg class="art" viewBox="0 0 320 220" {role} focusable="false"><use href="#{symbol}"/></svg>'


def treated(treatment, inner_html):
    """A picture wrapped for a treatment. Riso needs two copies of the picture, one per ink."""
    if treatment == "halftone":
        return f'<div class="pic tr-halftone"><div class="ht">{inner_html}</div></div>'
    if treatment == "riso":
        hidden = inner_html.replace('role="img"', 'aria-hidden="true" data-r="img"').replace(f'alt="{PHOTO_ALT}"', 'alt=""')
        return f'<div class="pic tr-riso"><div class="ink ink-a">{inner_html}</div><div class="ink ink-b" aria-hidden="true">{hidden}</div></div>'
    return f'<div class="pic tr-{treatment}">{inner_html}</div>'


TECH = {
    "flat-shapes": ("t-flat-shapes", "Drawing of a jug dipped in green glaze and a red cup on a table, a sprig in the jug and the sun behind, in flat shapes"),
    "cut-paper": ("t-cut-paper", "Cut-paper picture of a dipped jug and a red cup on a table, a sprig in the jug and the sun behind"),
    "ink-line": ("t-ink-line", "Ink drawing of a jug and a cup on a table, a sprig in the jug and the sun behind, with loose colour under the lines"),
    "pencil": ("t-pencil", "Pencil sketch of a jug and a cup on a table, washed with colour, the cup ringed in pencil"),
    "ink-wash": ("t-ink-wash", "Brush-and-ink painting of a jug with a sprig, a cup, misty hills and a red sun"),
    "painted": ("t-painted", "Painting of a green jug and a red cup on a table in the light from the left, the sun behind"),
    "engraved": ("t-engraved", "Engraving of a jug and a cup on a table under a ruled sky, shaded in fine lines"),
    "photograph": (None, PHOTO_ALT),
}


def tech_picture(t, label=True):
    s, alt = TECH[t]
    return photo() if s is None else drawn(s, alt if label else None)


def sheet(name, idline, line, extra=""):
    return f'<div class="sheet"><h3>{name}</h3><p class="id">{idline}</p><p>{line}</p>{extra}</div>'


def swatch(option, body, classes=""):
    return f'<section class="swatch" data-option="{option}">\n<div class="ground {classes}">\n{body}\n</div>\n</section>\n'


LAYERS = {
    "technique": [
        ("flat-shapes", "Flat shapes", "Clean flat shapes in a few colours, no outlines and no shading."),
        ("cut-paper", "Cut paper", "Shapes cut from coloured paper and laid on each other; uneven edges, a little shadow."),
        ("ink-line", "Ink line", "A pen outline with loose flat colour under it, slightly off the line."),
        ("pencil", "Pencil", "A graphite sketch with a light wash: drawn on the spot. One thing ringed."),
        ("ink-wash", "Ink wash", "Brush and ink: dry strokes, soft grey washes, a lot left empty."),
        ("painted", "Painted", "Opaque paint in big shapes: light from one side, shade on the other, brush marks."),
        ("engraved", "Engraved", "Black lines only: tone made by ruled hatching, as on an old printed plate."),
        ("photograph", "Photograph", "A real photograph of the real thing. Here: free to use, credited below."),
    ],
    "treatment": [
        ("none", "None", "The picture as it is."),
        ("duotone", "Duotone", "Two colours from the page: the darks in a band colour, the lights in the pale on it."),
        ("grain", "Grain", "A fine speckle over the picture, so it sits in a made page."),
        ("halftone", "Halftone", "Printed in dots: big dots in the shadows, none in the lights."),
        ("riso", "Riso", "Two inks printed one over the other, slightly out of register."),
        ("aged", "Aged", "Faded and warmed, softer at the edges, with grain: an old print."),
    ],
    "icons": [
        ("outline", "Outline", "Open shapes drawn in one even line."),
        ("filled", "Filled", "Solid shapes; details cut out of them."),
        ("duotone", "Duotone", "An outline with a pale fill of the same colour."),
        ("hand-drawn", "Hand-drawn", "The same shapes drawn by a hand: the line wavers."),
        ("none", "None", "No icons: words carry the menu."),
    ],
    "stroke": [
        ("hairline", "Hairline", "One pixel at every size: fine and exact."),
        ("regular", "Regular", "Two pixels at 24: the common weight."),
        ("bold", "Bold", "Three pixels at 24: chunky, reads from across a room."),
        ("brush", "Brush", "Lines that swell and taper, as a brush makes them."),
    ],
    "figures": [
        ("none", "None", "No people in the pictures: things and places only."),
        ("silhouettes", "Silhouettes", "People as dark shapes against the light: no faces."),
        ("simple", "Simple", "Round heads, dot eyes, a few shapes: friendly, and anyone."),
        ("detailed", "Detailed", "Faces, hair, folds and shade: particular people."),
        ("photographed", "Photographed", "Real people, photographed, named, and asked first."),
    ],
    "stand-in": [
        ("none", "None", "Nothing stands in: the drawing is the real picture of the site."),
        ("brief-box", "Brief box", "A box the size of the photograph, saying what it must show."),
        ("captioned", "Captioned", "A drawing in the site's own style, with a caption that says a photograph goes here."),
        ("quiet", "Quiet", "A drawing with an ordinary caption; the alt text and the blueprint say it stands in."),
    ],
}
DEFAULTS = {"technique": "flat-shapes", "treatment": "none", "icons": "outline", "stroke": "regular", "figures": "none", "stand-in": "captioned"}

STARTS = [
    ("warm", "Warm", {"technique": "cut-paper", "treatment": "grain", "icons": "hand-drawn", "stroke": "bold", "figures": "simple", "stand-in": "captioned"},
     "Cut paper with grain, simple friendly people, drawn icons; a caption says the real photograph is coming."),
    ("artistic", "Artistic", {"technique": "ink-wash", "icons": "none", "stroke": "brush", "stand-in": "quiet"},
     "One made picture in brush and ink, a lot left empty; words, not icons."),
    ("professional", "Professional", {"technique": "photograph", "stroke": "regular", "figures": "photographed", "stand-in": "brief-box"},
     "Real, named people, photographed; until then, a box saying what to shoot. Plain outline icons."),
    ("civic", "Civic", {"technique": "flat-shapes", "icons": "filled", "stroke": "bold", "stand-in": "brief-box"},
     "Few pictures, each carrying information; boxes for photographs; solid icons with words."),
    ("sorcery", "Sorcery", {"technique": "painted", "treatment": "aged", "icons": "hand-drawn", "stroke": "brush", "figures": "detailed", "stand-in": "quiet"},
     "Painted, then aged; particular people; brush lines and drawn icons."),
    ("gilded-dark", "Gilded dark", {"technique": "painted", "icons": "filled", "stroke": "bold", "figures": "silhouettes", "stand-in": "quiet"},
     "Painted; people as dark shapes against the light; chunky solid icons."),
    ("lantern-fair", "Lantern fair", {"technique": "cut-paper", "treatment": "grain", "icons": "hand-drawn", "stand-in": "none"},
     "Cut paper with grain and drawn icons, no people: how its lantern and dishes are drawn."),
    ("almanac-plate", "Almanac plate", {"technique": "engraved", "stroke": "hairline", "stand-in": "none"},
     "Fine ruled lines, like a printed star chart; hairline icons."),
    ("catalogue-of-glazes", "Catalogue of glazes", {"technique": "flat-shapes", "icons": "none", "stroke": "hairline", "stand-in": "quiet"},
     "Each piece drawn flat in its own glaze; no icons; the drawing quietly stands in."),
    ("field-journal", "Field journal", {"technique": "pencil", "icons": "hand-drawn", "stand-in": "none"},
     "A pencil sketch with a wash, one thing ringed; drawn icons."),
    ("repair-cafe", "Repair cafe", {"technique": "ink-line", "icons": "hand-drawn", "stroke": "bold", "figures": "simple", "stand-in": "captioned"},
     "Marker drawings with flat colour, friendly people, bold drawn icons."),
]

TITLES = {"technique": "Technique", "treatment": "Treatment", "icons": "Icons", "stroke": "Stroke", "figures": "Figures", "stand-in": "Stand-in"}
NOTES = {
    "technique": "How the pictures are made. The same jug, cup, sprig and sun in each, so only the technique changes. Drawings made from the band colours stay the same picture on a dark page; drawings made in the page's own ink and paper turn over, like chalk on a board.",
    "treatment": "What is done to a picture after it is made: the photograph and one drawing, each with the same treatment. All of it is CSS over the picture, in the shared colours.",
    "icons": "How small signs are drawn. The same five icons in each, always with their words. The weight is the stroke layer's.",
    "stroke": "The weight of every drawn line: the icons, and the jug drawn as a line drawing.",
    "figures": "How people are shown in the pictures. The same scene: people at a table with a jug.",
    "stand-in": "What fills a photograph's place in a mockup until the real one exists.",
}


def caption_for(stand, tech):
    if stand == "brief-box":
        return ""
    if stand == "captioned":
        return '<figcaption>Drawn for now: a photograph of the studio table goes here.</figcaption>'
    if stand == "quiet":
        return '<figcaption>Jug and cup, ash glaze.</figcaption>'
    return '<figcaption>The studio table in the morning.</figcaption>'


def brief_box():
    return ('<div class="brief" role="img" aria-label="Space for a photograph, not taken yet: hands at the wheel, from above">'
            '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>'
            '<b>Photo: hands at the wheel, from above</b><span>Daylight from the left. Clay on the hands; no faces needed. 3:2, 1800 by 1200 or larger.</span></div>')


def classes_for(p):
    return " ".join([f"ic-{p['icons']}", f"st-{p['stroke']}"])


def figure_symbol(f):
    return {"none": "f-none", "silhouettes": "f-silhouettes", "simple": "f-simple", "detailed": "f-detailed"}.get(f)


FIG_ALT = {
    "f-none": "Drawing of a table with a jug, a cup and a jar on it; nobody there",
    "f-silhouettes": "Two people against a low sun, drawn as dark shapes with no faces",
    "f-simple": "Drawing of three people at a table with a jug, each with a round face, dot eyes and a smile",
    "f-detailed": "Drawing of two people at a table, one with long hair looking down, the other with short grey hair, a jug between them",
}

out = []
for layer, options in LAYERS.items():
    out.append(f'<h2 class="layer">{TITLES[layer]}</h2>\n<p class="layer-note">{NOTES[layer]}</p>\n')
    for oid, name, line in options:
        idline = f"{layer}: {oid}"
        if layer == "technique":
            body = f'<figure class="pic tr-none">{tech_picture(oid)}</figure>' + sheet(name, idline, line)
            out.append(swatch(f"{layer}:{oid}", body, "pics-1"))
        elif layer == "treatment":
            body = (treated(oid, photo()) + treated(oid, drawn("t-flat-shapes", TECH["flat-shapes"][1]))
                    + sheet(name, idline, line))
            out.append(swatch(f"{layer}:{oid}", body, "pics-2"))
        elif layer == "icons":
            body = sheet(name, idline, line, icon_row() + '<button class="btn" type="button"><svg class="ic" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><use href="#i-basket"/></svg>Add to basket</button>')
            out.append(swatch(f"{layer}:{oid}", body, f"ic-{oid} st-regular one"))
        elif layer == "stroke":
            art = (f'<svg class="art line-art" viewBox="0 0 320 220" role="img" aria-label="Line drawing of a jug and a cup, a sprig and the sun" focusable="false"><use href="#{"jug-brush" if oid == "brush" else "jug-lines"}"/></svg>')
            body = f'<figure class="pic plain">{art}</figure>' + sheet(name, idline, line, icon_row())
            out.append(swatch(f"{layer}:{oid}", body, f"ic-outline st-{oid} pics-1"))
        elif layer == "figures":
            s = figure_symbol(oid)
            pic = photo() if s is None else drawn(s, FIG_ALT[s])
            body = f'<figure class="pic tr-none">{pic}</figure>' + sheet(name, idline, line)
            out.append(swatch(f"{layer}:{oid}", body, "pics-1"))
        elif layer == "stand-in":
            pic = brief_box() if oid == "brief-box" else f'<div class="pic tr-none">{drawn("t-flat-shapes", "Drawing of a dipped jug and a cup on a table" + (", standing in for a photograph of the studio table" if oid in ("captioned", "quiet") else ""))}</div>'
            body = f'<figure class="pic-fig">{pic}{caption_for(oid, "flat-shapes")}</figure>' + sheet(name, idline, line)
            out.append(swatch(f"{layer}:{oid}", body, "pics-1"))

out.append('<h2 class="layer">Starting points</h2>\n<p class="layer-note">Saved sets of picks, any layer not named at its default. Each shows its picture in its technique and treatment, its people, its icons at its line weight, and how a missing photograph is shown.</p>\n')
for sid, name, picks, line in STARTS:
    p = dict(DEFAULTS, **picks)
    idline = "; ".join(f"{k}: {v}" for k, v in picks.items())
    if p["stand-in"] == "brief-box" and p["technique"] == "photograph":
        main = f'<figure class="pic-fig">{treated(p["treatment"], photo())}<figcaption>Ruth at the wheel, Tuesday class.</figcaption></figure>'
    elif p["stand-in"] == "brief-box":
        main = f'<figure class="pic-fig">{brief_box()}</figure>'
    else:
        main = f'<figure class="pic-fig">{treated(p["treatment"], tech_picture(p["technique"]))}{caption_for(p["stand-in"], p["technique"])}</figure>'
    s = figure_symbol(p["figures"])
    if p["figures"] == "photographed":
        fig = f'<div class="pic tr-none small">{photo()}</div>' if p["stand-in"] != "brief-box" or p["technique"] != "photograph" else ""
    elif s and p["figures"] != "none":
        fig = f'<div class="pic tr-none small">{drawn(s, FIG_ALT[s])}</div>'
    else:
        fig = ""
    extra = fig + (icon_row() if p["icons"] != "none" else '<p class="words-only">Home · Find · Basket · Dates · Write</p>')
    if p["technique"] == "photograph" and p["stand-in"] == "brief-box":
        extra = f'<figure class="pic-fig small">{brief_box()}</figure>' + extra
    body = main + sheet(name, idline, line, extra)
    out.append(swatch(f"start:{sid}", body, f"{classes_for(p)} pics-1 start"))

defs = (FILTERS + t_flat() + t_cut() + t_ink_line() + t_pencil() + t_ink_wash() + t_painted() + t_engraved()
        + jug_lines() + jug_brush() + people_none() + people_silhouettes() + people_simple() + people_detailed() + icon_syms())
page = (HERE / "pictures-template.html").read_text(encoding="utf-8").replace("{{DEFS}}", defs).replace("{{SWATCHES}}", "".join(out))
Path(sys.argv[1]).write_text(page, encoding="utf-8")
print("wrote", sys.argv[1], len(page), "bytes")
