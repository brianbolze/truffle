"""assets — everything fetched, cached, or computed to dress an artifact in a company's
own identity: color math + palette derivation, font embedding (Google Fonts → data URIs),
wordmarks/logomarks, homepage screenshots.

Cache-first on purpose: every remote fetch lands beside the output so re-renders are
offline and instant, and --no-fetch renders never touch the network at all.
"""

from __future__ import annotations

import base64
import colorsys
import glob
import hashlib
import os
import re
import subprocess
import urllib.request
from typing import Any

from store import STORE

from . import OUT
from .theme import INK, PAPER

FONTCACHE = os.path.join(OUT, ".fontcache")
IMGCACHE = os.path.join(OUT, ".imgcache")

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


# ---------------------------------------------------------------- color math

def _hex_rgb(h: str) -> tuple[float, float, float] | None:
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        return None
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))  # type: ignore[return-value]


def _lum(rgb: tuple[float, float, float]) -> float:
    def lin(c: float) -> float:
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _contrast(a: str, b: str) -> float:
    ra, rb = _hex_rgb(a), _hex_rgb(b)
    if not ra or not rb:
        return 1.0
    la, lb = _lum(ra), _lum(rb)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def _sat(h: str) -> float:
    rgb = _hex_rgb(h)
    if not rgb:
        return 0.0
    _, _, s = colorsys.rgb_to_hls(*rgb)
    return s


def _set_lightness(h: str, light: float) -> str:
    rgb = _hex_rgb(h)
    if not rgb:
        return h
    hh, _, s = colorsys.rgb_to_hls(*rgb)
    r, g, b = colorsys.hls_to_rgb(hh, light, s)
    return f"#{int(r * 255):02X}{int(g * 255):02X}{int(b * 255):02X}"


def _darken_until(h: str, bg: str, target: float = 3.2) -> str:
    """Hue-preserving darken until the color is usable as text/accent on bg."""
    rgb = _hex_rgb(h)
    if not rgb:
        return INK
    _, light, _ = colorsys.rgb_to_hls(*rgb)
    cur = h
    while _contrast(cur, bg) < target and light > 0.08:
        light -= 0.03
        cur = _set_lightness(h, light)
    return cur


def palette(brand_colors: dict[str, str] | None, color_scheme: str | None) -> dict[str, Any]:
    """The brief's color system, derived from the company's captured palette.

    hero_bg: the brand's darkest usable color (the identity band ground).
    hero_accent: the brand color that sings on that ground.
    accent: the brand's most saturated hue, darkened only as far as paper-legibility demands.
    """
    items = [(k, str(v)) for k, v in (brand_colors or {}).items() if _hex_rgb(str(v))]
    swatches = [{"key": k, "hex": v.upper()} for k, v in items]
    hexes = [v for _, v in items]

    dark = [v for v in hexes if _lum(_hex_rgb(v)) < 0.32] or [v for v in hexes if _lum(_hex_rgb(v)) < 0.45]
    hero_bg = min(dark, key=lambda v: _lum(_hex_rgb(v))) if dark else INK

    rest = [v for v in hexes if v != hero_bg]
    cands = [v for v in rest if _contrast(v, hero_bg) >= 2.2]
    hero_accent = max(cands, key=lambda v: _sat(v) * 1.5 + _contrast(v, hero_bg) / 21) if cands else PAPER

    if hexes:
        most_sat = max(hexes, key=_sat)
        accent = most_sat if _contrast(most_sat, PAPER) >= 3.0 else _darken_until(most_sat, PAPER)
        accent_on_dark = most_sat if _contrast(most_sat, INK) >= 2.6 else hero_accent
    else:
        accent, accent_on_dark = "#4D4C47", "#B8B5AD"

    return {
        "swatches": swatches, "scheme": color_scheme or "",
        "hero_bg": hero_bg, "hero_accent": hero_accent,
        "hero_fg": PAPER if _contrast(PAPER, hero_bg) >= 4 else INK,
        "accent": accent, "accent_dark": accent_on_dark,
    }


# ---------------------------------------------------------------- network + assets

def _fetch(url: str, timeout: int = 15) -> bytes | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except Exception:
        return None


SERIF_HINTS = ("serif", "tiempos", "stix", "lora", "playfair", "garamond", "caslon", "georgia",
               "freight", "canela", "recoleta", "charter", "crimson", "domine", "fraunces", "noe",
               "minion", "times", "baskerville", "didot", "bodoni", "newsreader", "utopia",
               "sentinel", "chronicle", "mercury", "publico", "lyon", "austin", "financier",
               "merriweather", "eb garamond", "spectral", "source serif")
MONO_HINTS = ("mono", "courier", "consolas")

SERIF_STACK = "'Iowan Old Style','Palatino Linotype',Palatino,Georgia,serif"
SANS_STACK = "'Helvetica Neue',Helvetica,Arial,sans-serif"
MONO_STACK = "ui-monospace,'SF Mono',Menlo,Consolas,monospace"


def _classify(name: str) -> str:
    n = name.lower()
    if any(h in n for h in MONO_HINTS):
        return "mono"
    if any(h in n for h in SERIF_HINTS):
        return "serif"
    return "sans"


def _google_css(family: str, axes: str | None, fetch: bool) -> str | None:
    """Fetch Google Fonts css2 for a family, keep latin subsets, inline woff2 as data URIs."""
    key = hashlib.md5(f"{family}|{axes}".encode()).hexdigest()[:16]
    cache = os.path.join(FONTCACHE, f"{key}.css")
    if os.path.exists(cache):
        with open(cache, encoding="utf-8") as f:
            cached = f.read()
        return cached or None  # empty file = remembered miss
    if not fetch:
        return None
    fam = family.replace(" ", "+") + (f":{axes}" if axes else "")
    raw = _fetch(f"https://fonts.googleapis.com/css2?family={fam}&display=swap")
    os.makedirs(FONTCACHE, exist_ok=True)
    if raw is None:
        return None  # network failure: don't cache, retry next run
    css = raw.decode("utf-8", "replace")
    if "@font-face" not in css:
        with open(cache, "w", encoding="utf-8") as f:
            f.write("")  # remembered miss (family not on Google Fonts)
        return None
    blocks = re.findall(r"/\* ([a-z0-9-]+) \*/\s*(@font-face\s*\{[^}]+\})", css)
    keep = [b for sub, b in blocks if sub == "latin"] or [b for _, b in blocks]
    out_blocks: list[str] = []
    for b in keep:
        m = re.search(r"url\((https://[^)]+)\)", b)
        if not m:
            continue
        woff = _fetch(m.group(1))
        if woff is None:
            return None
        data = "data:font/woff2;base64," + base64.b64encode(woff).decode()
        out_blocks.append(b.replace(m.group(1), data))
    final = "\n".join(out_blocks)
    with open(cache, "w", encoding="utf-8") as f:
        f.write(final)
    return final or None


def build_fonts(company_fonts: list[str], fetch: bool) -> dict[str, Any]:
    """Scaffold faces (Newsreader + Fragment Mono) + the company's own faces where embeddable."""
    css_parts: list[str] = []
    scaffold_serif = _google_css("Source Serif 4", "ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400", fetch)
    scaffold_mono = _google_css("DM Mono", "wght@400;500", fetch)
    if scaffold_serif:
        css_parts.append(scaffold_serif)
    if scaffold_mono:
        css_parts.append(scaffold_mono)

    specs: list[dict[str, Any]] = []
    for i, name in enumerate([f for f in (company_fonts or []) if f]):
        cls = _classify(name)
        css = _google_css(name, "wght@400;600;700", fetch) or _google_css(name, None, fetch)
        if css:
            css_parts.append(css)
        stack = {"serif": SERIF_STACK, "mono": MONO_STACK}.get(cls, SANS_STACK)
        specs.append({
            "name": name, "embedded": bool(css), "class": cls,
            "css": f"'{name}',{stack}",
            "role": "display" if i == 0 else "body",
        })

    display = specs[0]["css"] if specs else f"'Source Serif 4',{SERIF_STACK}"
    return {
        "css": "\n".join(css_parts),
        "specs": specs,
        "display": display,
        "body": f"'Source Serif 4',{SERIF_STACK}",
        "mono": f"'DM Mono',{MONO_STACK}",
    }


def _b64_file(path: str) -> str | None:
    ext = os.path.splitext(path)[1].lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
            "webp": "image/webp", "svg": "image/svg+xml", "gif": "image/gif"}.get(ext, "image/png")
    try:
        with open(path, "rb") as f:
            return f"data:{mime};base64," + base64.b64encode(f.read()).decode()
    except OSError:
        return None


def _svg_fill_luminance(svg_text: str) -> float:
    """Mean luminance of explicit fills — decides dark-ground vs paper-plate placement."""
    named = {"white": "#ffffff", "black": "#000000"}
    lums = []
    for fill in re.findall(r'fill="([^"]+)"', svg_text):
        rgb = _hex_rgb(named.get(fill.lower(), fill))
        if rgb:
            lums.append(_lum(rgb))
    return sum(lums) / len(lums) if lums else 0.0  # no explicit fill → renders black → dark


def load_logo(slug: str, fm: dict[str, Any], fetch: bool) -> dict[str, Any]:
    """The hero mark: wordmark slot → logo_url (non-favicon) → typographic fallback.

    `plate` = mark is dark, set it on a paper plate instead of the dark hero ground
    (a white-fill wordmark goes straight on the ground).
    """
    logos = fm.get("logos") or {}
    wm = logos.get("wordmark") or {}
    src = wm.get("src") or ""
    w, h = wm.get("w"), wm.get("h")

    def from_svg_text(text: str) -> dict[str, Any]:
        text = re.sub(r"<\?xml[^>]*\?>", "", text).strip()
        lum = _svg_fill_luminance(text)
        vb = re.search(r'viewBox="([\d.\s-]+)"', text)
        aspect = None
        if vb:
            parts = vb.group(1).split()
            if len(parts) == 4 and float(parts[3]) > 0:
                aspect = float(parts[2]) / float(parts[3])
        text = re.sub(r"<svg ", '<svg class="mark-svg" ', text, count=1)
        return {"kind": "svg", "svg": text, "plate": lum < 0.55, "aspect": aspect or 4.0}

    if src.startswith("assets/"):
        path = os.path.join(STORE, slug, src)
        if os.path.exists(path) and path.endswith(".svg"):
            with open(path, encoding="utf-8") as f:
                return from_svg_text(f.read())
        data = _b64_file(path)
        if data:
            return {"kind": "img", "data": data, "plate": True, "aspect": (w / h) if w and h else 4.0}
    elif src.startswith("http") and fetch:
        raw = _fetch(src)
        if raw:
            if b"<svg" in raw[:2000]:
                return from_svg_text(raw.decode("utf-8", "replace"))
            mime = "image/png" if src.lower().endswith("png") else "image/jpeg"
            data = f"data:{mime};base64," + base64.b64encode(raw).decode()
            return {"kind": "img", "data": data, "plate": True, "aspect": (w / h) if w and h else 4.0}

    url = str(fm.get("logo_url") or "")
    if url.startswith("http") and "favicon" not in url and not url.endswith(".ico") and fetch:
        raw = _fetch(url)
        if raw:
            if b"<svg" in raw[:2000]:
                return from_svg_text(raw.decode("utf-8", "replace"))
            ext = "png" if ".png" in url.lower() else "jpeg"
            data = f"data:image/{ext};base64," + base64.b64encode(raw).decode()
            return {"kind": "img", "data": data, "plate": True, "aspect": 4.0}

    return {"kind": "text", "plate": False, "aspect": None}


def load_logomark(slug: str, fm: dict[str, Any], fetch: bool) -> str | None:
    lm = (fm.get("logos") or {}).get("logomark") or {}
    src = lm.get("src") or ""
    if src.startswith("assets/"):
        return _b64_file(os.path.join(STORE, slug, src))
    if src.startswith("http") and fetch:
        raw = _fetch(src)
        if raw:
            mime = "image/svg+xml" if b"<svg" in raw[:2000] else "image/png"
            return f"data:{mime};base64," + base64.b64encode(raw).decode()
    return None


def load_screenshot(slug: str, width: int = 1200) -> dict[str, str] | None:
    """Latest captured homepage screenshot, sips-compressed to a sane embed size. Local-only.

    width is the resample target: the brief embeds full-column (1200); the comparison sheet
    shows N narrow specimens and passes something smaller so an N-up file stays AirDrop-able.
    """
    shots = sorted(glob.glob(os.path.join(STORE, slug, "captures", "*", ".payloads", "homepage.png")))
    if not shots:
        return None
    src = shots[-1]
    cap_date = os.path.basename(os.path.dirname(os.path.dirname(src)))
    os.makedirs(IMGCACHE, exist_ok=True)
    dst = os.path.join(IMGCACHE, f"{slug}-homepage-{width}.jpg")
    if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src):
        r = subprocess.run(
            ["sips", "--resampleWidth", str(width), "-s", "format", "jpeg",
             "-s", "formatOptions", "72", src, "--out", dst],
            capture_output=True)
        if r.returncode != 0:
            dst = src if os.path.getsize(src) < 3_000_000 else ""
    if not dst:
        return None
    data = _b64_file(dst)
    return {"data": data, "date": cap_date} if data else None
