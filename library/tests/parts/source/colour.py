"""Builds the colour swatch book (../colour.html) from colour-template.html beside this file, and checks every
combination of the colour part's layers in Python before the page checks them again in a browser.

The colour part is the one part that writes raw colours. It writes them as oklch(): lightness comes from the tone,
chroma from the strength times a number the option carries, and hue from the neutrals or the accent. The numbers each
option carries are worked out here, so that no colour falls outside what an ordinary (sRGB) screen can show, at any
tone: outside it, a browser cuts the colour back in its own way and the contrast is no longer the one computed.
Run from this folder:
    python3 colour.py ../colour.html"""
import itertools, math, sys
from pathlib import Path

HERE = Path(__file__).parent

# ---------- OKLCH to sRGB, gamut and WCAG contrast ----------

def linear(L, C, h):
    a, b = C * math.cos(math.radians(h)), C * math.sin(math.radians(h))
    l_, m_, s_ = L + 0.3963377774 * a + 0.2158037573 * b, L - 0.1055613458 * a - 0.0638541728 * b, L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
            -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)


def in_gamut(L, C, h, eps=0.0008):
    return all(-eps <= x <= 1 + eps for x in linear(L, C, h))


def max_chroma(L, h):
    lo, hi = 0.0, 0.4
    for _ in range(30):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if in_gamut(L, mid, h, 0) else (lo, mid)
    return lo


def luminance(c):
    r, g, b = (min(1, max(0, x)) for x in linear(*c))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    ya, yb = luminance(a), luminance(b)
    return (max(ya, yb) + 0.05) / (min(ya, yb) + 0.05)


def safe(lightnesses, h, ceiling):
    """The most chroma a hue can take at every one of these lightnesses, kept a little inside the edge, and no more than the ceiling."""
    return round(min(ceiling, min(max_chroma(L, h) for L in lightnesses) * 0.96), 3)


# ---------- the layers ----------
# Each tone gives the lightness of every role (0 is black, 1 is white), and how much of the neutral's chroma each role takes.
TONES = {
    #          ground surface raised ink   soft  line  accent focus on-acc mark  band  on-band status texture shadow  k-ground k-sheet scrim tex-str shadow-str
    "light":   (0.965, 0.990, 0.997, 0.23, 0.46, 0.86, 0.50, 0.42, 0.98,  0.52, 0.42, 0.965, 0.50, 0.30, 0.25,    1.0,     0.3,   0.45, 0.10, 0.18),
    "toned":   (0.890, 0.972, 0.990, 0.22, 0.44, 0.79, 0.47, 0.36, 0.98,  0.48, 0.40, 0.965, 0.47, 0.30, 0.25,    1.8,     0.8,   0.45, 0.11, 0.18),
    "mid":     (0.750, 0.960, 0.980, 0.20, 0.42, 0.70, 0.37, 0.25, 0.98,  0.36, 0.36, 0.965, 0.46, 0.25, 0.22,    5.0,     1.0,   0.50, 0.12, 0.22),
    "dark":    (0.190, 0.235, 0.290, 0.93, 0.79, 0.40, 0.72, 0.88, 0.20,  0.76, 0.31, 0.950, 0.80, 0.92, 0.08,    1.6,     1.4,   0.60, 0.16, 0.45),
    "lamplit": (0.190, 0.800, 0.860, 0.20, 0.37, 0.56, 0.30, 0.88, 0.85,  0.76, 0.31, 0.950, 0.40, 0.92, 0.08,    1.8,     3.2,   0.60, 0.16, 0.45),
}
ROLE = ("ground", "surface", "raised", "ink", "soft", "line", "acc", "focus", "onacc", "mark", "band", "onband", "status", "tex", "shadow",
        "kground", "ksheet", "scrim", "texstr", "shadowstr")
T = {t: dict(zip(ROLE, v)) for t, v in TONES.items()}
LAMP_HUE, LAMP_CHROMA, LAMP_TEXT = 75, 0.022, 0.91      # lamplit sheets are warm paper whatever the ground; words on its ground are pale

NEUTRALS = {"paper": (80, 0.012), "stone": (250, 0.007), "sage": (150, 0.011), "clay": (55, 0.016), "night": (275, 0.014), "wine": (15, 0.015),
            "marigold": (85, 0.016)}
# A neutral may carry its own mid ground: (lightness, how many times its chroma, hue). Night and wine at the usual mid
# (0.75, five times) turn periwinkle and dusty rose, so they go greyer and a little deeper: a slate-blue board, a rosewood
# board. Marigold's board is lighter and yellower than any other, a sunflower board: a mid ground can be light, since
# everything that must be seen on it is dark.
NEUTRAL_MID = {"night": (0.72, 2.6, 252), "wine": (0.66, 2.7, 22), "marigold": (0.81, 6.5, 80)}
ACCENTS = {"brick": 35, "amber": 72, "forest": 155, "kingfisher": 220, "cobalt": 262, "plum": 330, "ink": None}
INK_ACCENT_L = {"light": 0.27, "toned": 0.26, "mid": 0.24, "dark": 0.93, "lamplit": 0.27}
INK_FOCUS_HUE = 262
# Accents that change with the tone. Amber is gold at every tone (0.81 on light pages, with dark words on it); a darker
# gold is brown. Brick and forest at night are set lower and less coloured, and turned warmer (rust, moss), because the
# usual lift makes them coral and mint.
ACCENT_L = {"amber": {"light": 0.81, "toned": 0.81, "mid": 0.81, "dark": 0.80},
            "brick": {"dark": 0.64}, "forest": {"dark": 0.66}}
ACCENT_HUE = {"amber": {"light": 80, "toned": 80, "mid": 80}, "brick": {"dark": 44, "lamplit": 44}, "forest": {"dark": 135, "lamplit": 135}}
ACCENT_CEIL = {"brick": {"dark": 0.15}, "forest": {"dark": 0.13}}
ON_ACCENT_L = {"amber": {"light": 0.22, "toned": 0.22, "mid": 0.22}}   # dark words on bright gold
# Where the accent cannot stand 3 to 1 off the ground or off a sheet by itself (gold on a pale page), its controls get a
# dark edge: this lightness, in the accent's hue. Elsewhere the edge is the accent itself.
EDGE_L = {"light": 0.42, "toned": 0.38, "mid": 0.3, "dark": 0.3}
EDGE_MAX = 0.1
# Lamplit turns the button round: a lamp colour (the dark tone's accent) is too near the parchment in lightness to stand
# off a sheet, so the button is dark (0.30, in the accent's hue) with words and an edge in the lamp colour. On a sheet the
# dark fill stands out; on the dark ground the lamp-coloured edge and words do.
LAMP_ON_MAX = 0.15
STRENGTH = {"muted": (0.45, 0.7), "natural": (0.7, 1.0), "vivid": (1.0, 1.5)}   # (accent, mark and band chroma; a mid page's ground chroma)
BANDS = {"none": None, "poster": (20, 150, 268), "earth": (45, 110, 62), "jewel": (330, 200, 262), "pale": (230, 95, 160)}
PALE = {"light": (0.93, 0.23), "toned": (0.955, 0.22), "mid": (0.93, 0.20), "dark": (0.30, 0.95), "lamplit": (0.30, 0.95)}
STATUS = {"danger": 27, "success": 150, "warning": 70}
# Materials the neutrals cannot give. Metal (rings, studs, plates) takes its own small layer; its middle lightness comes
# from the tone, its shade is 0.24 darker and its highlight 0.2 lighter (no more than 0.95). Each option is (hue, the most
# chroma it may have, a shift in lightness): gold is warm and strong, brass greener and quieter, silver near grey and a
# step lighter, iron a dark blue-grey.
METALS = {"gold": (80, 0.15, 0.0), "brass": (90, 0.10, -0.03), "silver": (250, 0.012, 0.05), "iron": (245, 0.018, -0.22)}
METAL_L = {"light": 0.70, "toned": 0.68, "mid": 0.63, "dark": 0.74, "lamplit": 0.74}
METAL_DEEP, METAL_LIT, METAL_LIT_MAX = 0.24, 0.20, 0.95
# Earth: kraft, card, cork, wood and leather, one warm brown whatever the neutrals. Pale kraft on light pages and under a
# lamp, a darker card on a mid board, dark wood at night. Words on it are dark, except at night.
EARTH_H = 68
EARTH = {"light": (0.70, 0.08), "toned": (0.67, 0.08), "mid": (0.60, 0.08), "dark": (0.36, 0.05), "lamplit": (0.68, 0.08)}   # (lightness, most chroma)
DARK_WORDS, PALE_WORDS = 0.18, 0.96
# With no bands, the band names still hold a quiet trio, so a part that needs three colours (a duotone, a riso print)
# has them: the accent's hue, the neutral's hue and the hue opposite the accent, at the tone's band lightness and a
# chroma any hue holds there (worked out below, the lowest over every hue).
QUIET_MAX = 0.05
# Hover and pressed: a step in lightness, away from the words on the fill so they only gain contrast. Light, toned and
# mid fills are darkened; dark and lamplit fills lightened (a darker step on a near-black fill would not show).
STEP = {"light": -0.05, "toned": -0.05, "mid": -0.05, "dark": 0.05, "lamplit": 0.06}
STEP_ACCENT = {"ink": {"dark": -0.05}}   # the ink button at night is near white: its step goes darker
DARK_TONES = ("dark", "lamplit")
def step(a, t): return STEP_ACCENT.get(a, {}).get(t, STEP[t])
ACCENT_MAX, FOCUS_MAX, BAND_MAX, PALE_MAX, MARK_MAX, STATUS_MAX = 0.19, 0.15, 0.13, 0.065, 0.11, 0.16

# the numbers each option carries, kept inside the sRGB gamut at every tone
def acc_l(a, t): return ACCENT_L.get(a, {}).get(t, T[t]["acc"])
def acc_h(a, t): return ACCENT_HUE.get(a, {}).get(t, ACCENTS[a])
acc_c = {a: {t: safe([acc_l(a, t)], acc_h(a, t), ACCENT_CEIL.get(a, {}).get(t, ACCENT_MAX)) for t in T} for a, h in ACCENTS.items() if h is not None}
foc_c = {a: {t: safe([T[t]["focus"]], acc_h(a, t), FOCUS_MAX) for t in T} for a, h in ACCENTS.items() if h is not None}
foc_c["ink"] = {t: safe([T[t]["focus"]], INK_FOCUS_HUE, FOCUS_MAX) for t in T}
band_c = {b: [safe([T[t]["band"] for t in T], h, BAND_MAX) for h in hs] for b, hs in BANDS.items() if hs and b != "pale"}
band_c["pale"] = [safe([L for L, _ in PALE.values()], h, PALE_MAX) for h in BANDS["pale"]]
edge = {}   # (accent, tone): (lightness, chroma before strength) of the edge, where it is not the accent; worked out below
for _a in ACCENTS:
    edge[(_a, "lamplit")] = (INK_ACCENT_L["dark"], None) if ACCENTS[_a] is None else (acc_l(_a, "dark"), acc_c[_a]["dark"])
quiet_c = round(min(QUIET_MAX, min(max_chroma(L, h) for L in [T[t]["band"] for t in T] for h in range(0, 360, 2)) * 0.96), 3)
hov_c = {a: {t: tuple(safe([acc_l(a, t) + step(a, t) * i], acc_h(a, t), acc_c[a][t]) for i in (1, 2)) for t in T} for a, h in ACCENTS.items() if h is not None}
lamp_on_c = {a: safe([T["lamplit"]["onacc"]], acc_h(a, "lamplit"), LAMP_ON_MAX) for a, h in ACCENTS.items() if h is not None}
mark_c = {n: safe([T[t]["mark"] for t in T], h, MARK_MAX) for n, (h, _) in NEUTRALS.items()}
status_c = {t: {s: safe([T[t]["status"]], h, STATUS_MAX) for s, h in STATUS.items()} for t in T}


def metal_ls(m, t):
    L = METAL_L[t] + METALS[m][2]
    return L, L - METAL_DEEP, min(METAL_LIT_MAX, L + METAL_LIT)


def words_on(L, C, h):
    """Dark or pale words, whichever stands further off this colour."""
    return DARK_WORDS if contrast((DARK_WORDS, 0.01, h), (L, C, h)) > contrast((PALE_WORDS, 0.01, h), (L, C, h)) else PALE_WORDS


metal_c = {m: {t: tuple(safe([L], h, c * f) for L, f in zip(metal_ls(m, t), (1, 0.85, 0.6))) for t in T} for m, (h, c, _) in METALS.items()}
on_metal_l = {m: {t: words_on(metal_ls(m, t)[0], metal_c[m][t][0], METALS[m][0]) for t in T} for m in METALS}
earth_c = {t: safe([L], EARTH_H, c) for t, (L, c) in EARTH.items()}
on_earth_l = {t: words_on(EARTH[t][0], earth_c[t], EARTH_H) for t in T}


def palette(t, n, a, s, b, m="gold"):
    """Every colour a set of picks gives, as (L, C, h): the same sums the CSS does."""
    R, (nh, nc), (k, gk) = T[t], NEUTRALS[n], STRENGTH[s]
    sh, sc = (LAMP_HUE, LAMP_CHROMA) if t == "lamplit" else (nh, nc)
    gl, gkk, gh = NEUTRAL_MID.get(n, (R["ground"], R["kground"], nh)) if t == "mid" else (R["ground"], R["kground"], nh)
    P = {"ground": (gl, nc * gkk * (gk if t == "mid" else 1), gh),
         "surface": (R["surface"], sc * R["ksheet"], sh), "surface-raised": (R["raised"], sc * R["ksheet"] * 0.3, sh),
         "ink": (R["ink"], sc * 1.5, sh), "ink-soft": (R["soft"], sc * 2, sh), "line": (R["line"], sc * 2.5, sh),
         "mark": (R["mark"], mark_c[n] * k, nh)}
    if a == "ink":
        P["accent"] = (INK_ACCENT_L[t], nc * 1.5, nh)
        P["on-accent"] = (R["onacc"], 0.008, nh)
        P["focus"] = (R["focus"], foc_c["ink"][t], INK_FOCUS_HUE)
    else:
        h = acc_h(a, t)
        P["accent"] = (acc_l(a, t), acc_c[a][t] * k, h)
        P["on-accent"] = (ON_ACCENT_L.get(a, {}).get(t, R["onacc"]), lamp_on_c[a] * k if t == "lamplit" else 0.008, h)
        P["focus"] = (R["focus"], foc_c[a][t], h)
    if (a, t) in edge:
        el, ec = edge[(a, t)]
        P["accent-edge"] = (el, nc * 1.5 if ec is None else ec * k, P["accent"][2])
    else:
        P["accent-edge"] = P["accent"]
    for name, h in STATUS.items():
        P[name] = (R["status"], status_c[t][name], h)
    mh = METALS[m][0]
    for name, L, C in zip(("metal", "metal-deep", "metal-lit"), metal_ls(m, t), metal_c[m][t]):
        P[name] = (L, C, mh)
    P["on-metal"] = (on_metal_l[m][t], 0.01, mh)
    P["earth"] = (EARTH[t][0], earth_c[t], EARTH_H)
    P["on-earth"] = (on_earth_l[t], 0.01, EARTH_H)
    P["on-ground"] = (LAMP_TEXT, 0.02, LAMP_HUE) if t == "lamplit" else P["ink"]
    ah = nh if a == "ink" else ACCENTS[a]
    for name, i in (("accent-hover", 1), ("accent-pressed", 2)):
        L, C, h = P["accent"]
        P[name] = (L + step(a, t) * i, C if a == "ink" else hov_c[a][t][i - 1] * k, h)
    if BANDS[b] is None:
        for i, h in enumerate((ah, nh, (ah + 180) % 360), 1):
            P[f"band-{i}"] = (R["band"], quiet_c * k, h)
        P["on-band"] = (R["onband"], 0.01, nh)
    else:
        bl, obl = PALE[t] if b == "pale" else (R["band"], R["onband"])
        for i, h in enumerate(BANDS[b], 1):
            P[f"band-{i}"] = (bl, band_c[b][i - 1] * k, h)
        P["on-band"] = (obl, 0.01, nh)
    return P


# Which accents need an edge: those that fall under 3 to 1 against the ground or a sheet at any neutral and strength.
for _a in ACCENTS:
    for _t in EDGE_L:
        if any(min(contrast(P["accent"], P["ground"]), contrast(P["accent"], P["surface"])) < 3
               for P in (palette(_t, n, _a, s, "none") for n in NEUTRALS for s in STRENGTH)):
            edge[(_a, _t)] = (EDGE_L[_t], 0.02 if _a == "ink" else safe([EDGE_L[_t]], acc_h(_a, _t), EDGE_MAX))

# A control stands off what it sits on by its fill or by its edge, so "accent" pairs take the better of the two.
PAIRS = [("on-ground", "ground", 4.5), ("ink", "surface", 4.5), ("ink-soft", "surface", 4.5), ("ink", "surface-raised", 4.5),
         ("on-accent", "accent", 4.5), ("on-accent", "accent-hover", 4.5), ("on-accent", "accent-pressed", 4.5), ("accent", "ground", 3), ("accent", "surface", 3), ("on-band", "band-1", 4.5), ("on-band", "band-2", 4.5),
         ("on-band", "band-3", 4.5), ("focus", "ground", 3), ("danger", "surface", 4.5), ("success", "surface", 4.5),
         ("warning", "surface", 4.5), ("on-metal", "metal", 4.5), ("on-earth", "earth", 4.5)]


def check():
    combos, misses, outside, worst = 0, [], [], {}
    for picks in itertools.product(T, NEUTRALS, ACCENTS, STRENGTH, BANDS, METALS):
        P = palette(*picks)
        combos += 1
        outside += [(picks, k) for k, v in P.items() if not in_gamut(*v)]
        for fg, bg, need in PAIRS:
            r = max(contrast(P[fg], P[bg]), contrast(P["accent-edge"], P[bg])) if fg == "accent" else contrast(P[fg], P[bg])
            if r < worst.get((fg, bg), (99,))[0]:
                worst[(fg, bg)] = (r, picks)
            if r < need:
                misses.append((picks, fg, bg, round(r, 2)))
    return combos, misses, outside, worst


# ---------- the CSS ----------

def n3(x):
    return f"{x:.3f}".rstrip("0").rstrip(".") if x else "0"


def css():
    out = ["/* ---- the sums: lightness from the tone, chroma from the strength and the option, hue from the neutrals or the accent ---- */",
           ".tone-light, .tone-toned, .tone-mid, .tone-dark, .tone-lamplit {",
           "  --ground: oklch(var(--l-ground) calc(var(--n-c) * var(--k-ground) * var(--k-ground-strength)) var(--g-h));",
           "  --surface: oklch(var(--l-surface) calc(var(--s-c) * var(--k-sheet)) var(--s-h));",
           "  --surface-raised: oklch(var(--l-raised) calc(var(--s-c) * var(--k-sheet) * 0.3) var(--s-h));",
           "  --ink: oklch(var(--l-ink) calc(var(--s-c) * 1.5) var(--s-h));",
           "  --ink-soft: oklch(var(--l-soft) calc(var(--s-c) * 2) var(--s-h));",
           "  --line: oklch(var(--l-line) calc(var(--s-c) * 2.5) var(--s-h));",
           "  --accent: oklch(var(--l-accent) calc(var(--c-accent) * var(--k)) var(--h-accent));",
           "  --on-accent: oklch(var(--l-on-accent) var(--c-on-accent) var(--h-accent));",
           "  --accent-hover: oklch(var(--l-hover) calc(var(--c-hover) * var(--k)) var(--h-accent));   /* a pointer over it */",
           "  --accent-pressed: oklch(var(--l-pressed) calc(var(--c-pressed) * var(--k)) var(--h-accent));   /* while pressed */",
           "  --accent-edge: oklch(var(--l-edge) calc(var(--c-edge) * var(--k)) var(--h-accent));   /* the edge of a control in the accent */",
           "  --focus: oklch(var(--l-focus) var(--c-focus) var(--focus-h, var(--h-accent)));",
           "  --mark: oklch(var(--l-mark) calc(var(--mark-c) * var(--k)) var(--n-h));",
           "  --band-1: oklch(var(--l-band) calc(var(--b1-c) * var(--k)) var(--b1-h));",
           "  --band-2: oklch(var(--l-band) calc(var(--b2-c) * var(--k)) var(--b2-h));",
           "  --band-3: oklch(var(--l-band) calc(var(--b3-c) * var(--k)) var(--b3-h));",
           "  --on-band: oklch(var(--l-on-band) 0.01 var(--n-h));",
           "  --metal: oklch(calc(var(--l-metal) + var(--metal-dl)) var(--c-metal) var(--m-h));   /* metal and gilt: rings, studs, plates */",
           f"  --metal-deep: oklch(calc(var(--l-metal) + var(--metal-dl) - {METAL_DEEP}) var(--c-metal-deep) var(--m-h));",
           f"  --metal-lit: oklch(min({METAL_LIT_MAX}, calc(var(--l-metal) + var(--metal-dl) + {METAL_LIT})) var(--c-metal-lit) var(--m-h));",
           "  --on-metal: oklch(var(--l-on-metal) 0.01 var(--m-h));",
           f"  --earth: oklch(var(--l-earth) var(--c-earth) {EARTH_H});   /* kraft, card, cork, wood, leather */",
           f"  --on-earth: oklch(var(--l-on-earth) 0.01 {EARTH_H});",
           "  --texture-rgb: from oklch(var(--l-texture) calc(var(--n-c) * 2) var(--n-h)) r g b;   /* three numbers, for rgb(var(--texture-rgb) / a) */",
           "  --shadow-rgb: from oklch(var(--l-shadow) calc(var(--n-c) * 2) var(--n-h)) r g b;",
           "  --scrim: rgb(var(--shadow-rgb) / var(--scrim-a));",
           "  background: var(--ground); color: var(--on-ground);",
           "}", "", "/* ---- tone: how light each role is ---- */"]
    for t, R in T.items():
        lamp = t == "lamplit"
        pale_l, pale_on = PALE[t]
        st = status_c[t]
        out.append(f".tone-{t} {{ color-scheme: {'dark' if R['ground'] < 0.5 else 'light'};\n"
                   + (f"  --l-ground: var(--mid-l, {n3(R['ground'])}); --g-h: var(--mid-h, var(--n-h)); --l-surface:" if t == "mid"
                      else f"  --l-ground: {n3(R['ground'])}; --g-h: var(--n-h); --l-surface:") + f" {n3(R['surface'])}; --l-raised: {n3(R['raised'])}; --l-ink: {n3(R['ink'])}; "
                   f"--l-soft: {n3(R['soft'])}; --l-line: {n3(R['line'])};\n"
                   f"  --l-accent: var(--accent-l-{t}, {n3(R['acc'])}); --c-accent: var(--accent-c-{t}); --h-accent: var(--accent-h-{t}, var(--a-h));\n"
                   f"  --l-on-accent: var(--on-accent-l-{t}, {n3(R['onacc'])}); "
                   + (f"--c-on-accent: calc(var(--on-accent-c-{t}, 0.008) * var(--k)); " if lamp else "--c-on-accent: 0.008; ")
                   + f"--l-edge: var(--edge-l-{t}, var(--l-accent)); --c-edge: var(--edge-c-{t}, var(--c-accent)); --l-focus: {n3(R['focus'])}; --c-focus: var(--focus-c-{t});\n"
                   f"  --l-mark: {n3(R['mark'])}; --l-band: var(--band-l-{t}, {n3(R['band'])}); --l-on-band: var(--on-band-l-{t}, {n3(R['onband'])}); "
                   f"--l-texture: {n3(R['tex'])}; --l-shadow: {n3(R['shadow'])};\n"
                   f"  --k-ground: {f"var(--mid-k, {n3(R['kground'])})" if t == 'mid' else n3(R['kground'])}; --k-ground-strength: {'var(--k-mid-ground)' if t == 'mid' else '1'}; --k-sheet: {n3(R['ksheet'])}; "
                   + (f"--s-h: {LAMP_HUE}; --s-c: {LAMP_CHROMA};\n" if lamp else "--s-h: var(--n-h); --s-c: var(--n-c);\n")
                   + f"  --on-ground: {f'oklch({LAMP_TEXT} 0.02 {LAMP_HUE})' if lamp else 'var(--ink)'};\n"
                   f"  --danger: oklch({n3(R['status'])} {n3(st['danger'])} 27); --success: oklch({n3(R['status'])} {n3(st['success'])} 150); "
                   f"--warning: oklch({n3(R['status'])} {n3(st['warning'])} 70);\n"
                   f"  --l-hover: calc(var(--l-accent) + var(--step-{t}, {STEP[t]})); --l-pressed: calc(var(--l-accent) + 2 * var(--step-{t}, {STEP[t]})); "
                   f"--c-hover: var(--hover-c-{t}, var(--c-accent)); --c-pressed: var(--pressed-c-{t}, var(--c-accent)); --dark: {1 if t in DARK_TONES else 0};\n"
                   f"  --l-metal: {n3(METAL_L[t])}; --c-metal: var(--metal-c-{t}); --c-metal-deep: var(--metal-deep-c-{t}); --c-metal-lit: var(--metal-lit-c-{t}); "
                   f"--l-on-metal: var(--on-metal-l-{t});\n"
                   f"  --l-earth: {n3(EARTH[t][0])}; --c-earth: {n3(earth_c[t])}; --l-on-earth: {n3(on_earth_l[t])};\n"
                   f"  --scrim-a: {n3(R['scrim'])}; --texture-strength: {n3(R['texstr'])}; --shadow-strength: {n3(R['shadowstr'])}; }}")
    out.append("\n/* ---- neutrals: the hue in the greys, and how much ---- */")
    for n, (h, c) in NEUTRALS.items():
        mid = NEUTRAL_MID.get(n)
        out.append(f".neutrals-{n} {{ --n-h: {h}; --n-c: {n3(c)}; --mark-c: {n3(mark_c[n])};"
                   + (f" --mid-l: {n3(mid[0])}; --mid-k: {n3(mid[1])}; --mid-h: {mid[2]};" if mid else "") + " }")
    out.append("\n/* ---- accent: a hue, and the most chroma it can hold at each tone's lightness ---- */")
    for a, h in ACCENTS.items():
        if h is None:
            out.append(".accent-ink { --a-h: var(--n-h); --focus-h: " + str(INK_FOCUS_HUE) + "; "
                       + " ".join(f"--accent-l-{t}: {n3(L)};" for t, L in INK_ACCENT_L.items()) + "\n  "
                       + " ".join(f"--accent-c-{t}: calc(var(--n-c) * 1.5 / var(--k));" for t in T) + "\n  "
                       + " ".join(f"--focus-c-{t}: {n3(foc_c['ink'][t])};" for t in T)
                       + "".join(f" --step-{t}: {v};" for t, v in STEP_ACCENT["ink"].items())
                       + "".join(f"\n  --edge-l-{t}: {n3(edge[('ink', t)][0])}; --edge-c-{t}: "
                                 + ("calc(var(--n-c) * 1.5 / var(--k))" if edge[('ink', t)][1] is None else n3(edge[('ink', t)][1])) + ";"
                                 for t in T if ('ink', t) in edge) + " }")
        else:
            extra = ("".join(f"--accent-l-{t}: {n3(L)}; " for t, L in ACCENT_L.get(a, {}).items())
                     + "".join(f"--accent-h-{t}: {H}; " for t, H in ACCENT_HUE.get(a, {}).items())
                     + "".join(f"--on-accent-l-{t}: {n3(L)}; " for t, L in ON_ACCENT_L.get(a, {}).items()))
            edges = " ".join(f"--edge-l-{t}: {n3(edge[(a, t)][0])}; --edge-c-{t}: {n3(edge[(a, t)][1])};" for t in T if (a, t) in edge)
            edges += f" --on-accent-c-lamplit: {n3(lamp_on_c[a])};"
            out.append(f".accent-{a} {{ --a-h: {h};" + (f"\n  {extra.strip()}" if extra else "") + "\n  "
                       + " ".join(f"--accent-c-{t}: {n3(acc_c[a][t])};" for t in T) + "\n  "
                       + " ".join(f"--focus-c-{t}: {n3(foc_c[a][t])};" for t in T) + "\n  "
                       + " ".join(f"--hover-c-{t}: {n3(hov_c[a][t][0])}; --pressed-c-{t}: {n3(hov_c[a][t][1])};" + ("\n  " if t == "mid" else "") for t in T).replace("\n   ", "\n  ")
                       + (f"\n  {edges}" if edges else "") + " }")
    out.append("\n/* ---- strength: how much of that chroma is used (and how coloured a mid page's ground is) ---- */")
    for s, (k, gk) in STRENGTH.items():
        out.append(f".strength-{s} {{ --k: {n3(k)}; --k-mid-ground: {n3(gk)}; }}")
    out.append("\n/* ---- bands: three strong grounds for whole bands, and the words on them ---- */")
    out.append(f".bands-none {{ --b1-h: var(--a-h); --b2-h: var(--n-h); --b3-h: calc(var(--a-h) + 180); --b1-c: {n3(quiet_c)}; --b2-c: {n3(quiet_c)}; --b3-c: {n3(quiet_c)}; }}"
               "   /* none drawn on the page, but a quiet trio for parts that need three colours */")
    for b, hs in BANDS.items():
        if not hs:
            continue
        line = f".bands-{b} {{ " + " ".join(f"--b{i}-h: {h}; --b{i}-c: {n3(band_c[b][i - 1])};" for i, h in enumerate(hs, 1))
        if b == "pale":
            line += "\n  " + " ".join(f"--band-l-{t}: {n3(L)}; --on-band-l-{t}: {n3(O)};" for t, (L, O) in PALE.items())
        out.append(line + " }")
    out.append("\n/* ---- metal: the colour of metal and gilt, its shade and its highlight ---- */")
    for m, (h, c, dl) in METALS.items():
        out.append(f".metal-{m} {{ --m-h: {h}; --metal-dl: {n3(dl)};\n  "
                   + " ".join(f"--metal-c-{t}: {n3(metal_c[m][t][0])}; --metal-deep-c-{t}: {n3(metal_c[m][t][1])}; --metal-lit-c-{t}: {n3(metal_c[m][t][2])};"
                              + ("\n  " if t == "mid" else "") for t in T).replace("\n   ", "\n  ") + "\n  "
                   + " ".join(f"--on-metal-l-{t}: {n3(on_metal_l[m][t])};" for t in T) + " }")
    return "\n".join(out)


# ---------- the swatches: one per option, in the guide's order, then one per starting point ----------
LAYERS = {
    "tone": [("light", "Light", "A pale paper page: the most common, and the easiest to read."),
             ("toned", "Toned", "Toned paper: cream, bisque or notebook, a step down from white."),
             ("mid", "Mid", "The ground is a colour: kraft, clay, a painted board."),
             ("dark", "Dark", "A dark room with a colour of its own; the sheets are dark too."),
             ("lamplit", "Lamplit", "A dark room, and the words on warm paper held up to a lamp.")],
    "neutrals": [("paper", "Paper", "Warm cream and brown-black ink."),
                 ("stone", "Stone", "Cool, nearly plain grey."),
                 ("sage", "Sage", "Grey-green, with green-black ink."),
                 ("clay", "Clay", "Bisque and terracotta; brown ink."),
                 ("night", "Night", "Blue-grey by day, night blue in the dark."),
                 ("wine", "Wine", "A blush of red; oxblood in the dark."),
                 ("marigold", "Marigold", "Butter paper; a sunflower board at mid.")],
    "accent": [("brick", "Brick", "Rust and seal red."), ("amber", "Amber", "Gold at every tone, with dark words on it."),
               ("forest", "Forest", "Deep green."), ("kingfisher", "Kingfisher", "Teal-blue."),
               ("cobalt", "Cobalt", "Printer's blue; ice blue in the dark."), ("plum", "Plum", "Red-violet."),
               ("ink", "Ink", "The ink itself: black buttons, white words.")],
    "strength": [("muted", "Muted", "Under half the colour there is room for."), ("natural", "Natural", "Most of it."),
                 ("vivid", "Vivid", "All of it, and a mid page's ground turns bold.")],
    "bands": [("none", "None", "No bands: a band is the ground."), ("poster", "Poster", "Madder red, forest and night."),
              ("earth", "Earth", "Terracotta, olive and umber."), ("jewel", "Jewel", "Plum, teal and sapphire."),
              ("pale", "Pale", "Sky, butter and mint, with dark words.")],
    "metal": [("gold", "Gold", "Warm, strong gilt."), ("brass", "Brass", "A greener, quieter gold."),
              ("silver", "Silver", "Pale, cool and nearly grey."), ("iron", "Iron", "Dark blue-grey, with pale words.")],
}
DEFAULTS = {"tone": "light", "neutrals": "paper", "accent": "brick", "strength": "natural", "bands": "none", "metal": "gold"}
STARTS = [
    ("warm", "Warm", {"tone": "light", "neutrals": "paper", "accent": "brick", "strength": "vivid", "bands": "poster"}),
    ("artistic", "Artistic", {"tone": "light", "neutrals": "stone", "accent": "brick", "strength": "natural", "bands": "none"}),
    ("professional", "Professional", {"tone": "light", "neutrals": "stone", "accent": "kingfisher", "strength": "muted", "bands": "none"}),
    ("civic", "Civic", {"tone": "light", "neutrals": "stone", "accent": "forest", "strength": "natural", "bands": "none"}),
    ("sorcery", "Sorcery", {"tone": "lamplit", "neutrals": "night", "accent": "amber", "strength": "natural", "bands": "none"}),
    ("gilded-dark", "Gilded dark", {"tone": "dark", "neutrals": "paper", "accent": "amber", "strength": "vivid", "bands": "jewel"}),
    ("lantern-fair", "Lantern fair", {"tone": "lamplit", "neutrals": "wine", "accent": "amber", "strength": "natural", "bands": "poster"}),
    ("almanac-plate", "Almanac plate", {"tone": "light", "neutrals": "night", "accent": "brick", "strength": "natural", "bands": "none", "metal": "brass"}),
    ("catalogue-of-glazes", "Catalogue of glazes", {"tone": "toned", "neutrals": "clay", "accent": "brick", "strength": "muted", "bands": "none"}),
    ("field-journal", "Field journal", {"tone": "toned", "neutrals": "sage", "accent": "kingfisher", "strength": "natural", "bands": "none"}),
    ("repair-cafe", "Repair café", {"tone": "mid", "neutrals": "marigold", "accent": "ink", "strength": "vivid", "bands": "poster", "metal": "iron"}),
]
BUTTON = {"tone": "Read on", "neutrals": "Read on", "accent": "Book", "strength": "Book", "bands": "Join in", "metal": "Enter", "start": "Enter"}


def swatch(option, title, line):
    layer, _, oid = option.partition(":")
    picks = "; ".join(f"{k}: {v}" for k, v in dict(STARTS_BY_ID[oid]).items()) if layer == "start" else f"{layer}: {oid}"
    return (f'<section class="swatch" data-option="{option}">\n'
            f'<p class="copy"></p>\n'
            f'<div class="sheet"><h3>{title}</h3><p class="id">{picks}</p><p>{line}</p><hr>\n'
            f'<button class="btn" type="button">{BUTTON[layer]}</button>\n'
            f'<p class="chips"><span class="chip danger">&#x2715; Full</span> <span class="chip success">&#x2713; Booked</span> '
            f'<span class="chip warning">! Two left</span></p></div>\n'
            f'<div class="under"><span class="ring">Focus</span><svg class="mark" viewBox="0 0 120 40" aria-hidden="true" focusable="false">'
            f'<path d="M4 28C20 6 30 36 46 18S74 4 86 22S108 34 116 10"/><circle cx="58" cy="32" r="3"/></svg></div>\n'
            f'<div class="mats"><span class="plate">Metal</span><span class="tag">Kraft</span></div>\n'
            f'<div class="strip"><span class="b1">Band</span><span class="b2">Band</span><span class="b3">Band</span></div>\n'
            f'</section>')


STARTS_BY_ID = {sid: picks for sid, _, picks in STARTS}
START_LINE = {"warm": "Cream paper, a bold red, and deep bands.", "artistic": "Grey paper and one seal red.",
              "professional": "Cool white and a quiet teal-blue.", "civic": "Plain, cool and clear, with a green go button.",
              "sorcery": "Night-blue room, parchment, one lamp of gold.", "gilded-dark": "Dark brown panes, bright gold, jewel bands.",
              "lantern-fair": "Oxblood night, canvas, lantern amber.", "almanac-plate": "Blue-grey star-chart paper, a red torch.",
              "catalogue-of-glazes": "Bisque paper and iron red.", "field-journal": "Notebook paper, green ink, kingfisher.",
              "repair-cafe": "A sunflower board and black buttons."}


def swatches():
    out = []
    for layer, options in LAYERS.items():
        out.append(f'<h2 class="layer">{layer.capitalize()}</h2>')
        out += [swatch(f"{layer}:{oid}", title, line) for oid, title, line in options]
    out.append('<h2 class="layer">Starting points</h2>')
    out += [swatch(f"start:{sid}", title, START_LINE[sid]) for sid, title, _ in STARTS]
    return "\n".join(out)


def data():
    import json
    return ("const LAYERS = " + json.dumps({k: [o for o, _, _ in v] for k, v in LAYERS.items()}) + ";\n"
            "const DEFAULTS = " + json.dumps(DEFAULTS) + ";\n"
            "const STARTS = " + json.dumps(STARTS_BY_ID) + ";")


if __name__ == "__main__":
    combos, misses, outside, worst = check()
    print(f"{combos} combinations checked in Python: {len(misses)} pairs under the minimum, {len(outside)} colours outside sRGB")
    for (fg, bg), (r, picks) in worst.items():
        print(f"  lowest {fg} on {bg}: {r:.2f} ({', '.join(picks)})")
    for m in misses[:20]:
        print("  MISS", m)
    for o in outside[:20]:
        print("  OUTSIDE", o)
    if len(sys.argv) > 1:
        page = (HERE / "colour-template.html").read_text(encoding="utf-8").replace("/* COLOUR CSS */", css()).replace("<!-- SWATCHES -->", swatches()).replace("/* COLOUR DATA */", data())
        Path(sys.argv[1]).write_text(page, encoding="utf-8")
        print("wrote", sys.argv[1], len(page), "bytes")
    else:
        print(css())
