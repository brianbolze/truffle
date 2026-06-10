#!/usr/bin/env python3
"""render — one company dossier (store/<slug>/) → one self-contained HTML brief.

Why: every consumer of the store so far is an agent or a SQL-literate human. This renders the
dossier for a *human who judges design for a living* — dressed in the company's own captured
identity (wordmark, brand_colors, fonts), with the engine's trust surface (capture clocks,
unverified fields, enumeration floors) rendered visibly as the product, not fine print.

One script, one output file, no server, no build step. The markdown stays the source of truth;
the brief is a regenerable lens (same philosophy as the SQLite lens). `--index` renders the
store's human front door: every profiled company, one row, per-layer clocks — local reads only.

Structure: four tabs (Profile / Offer architecture / Brand system / Provenance & limits),
collapsible sections with one-line peeks.

extract_model() and render_html() are deliberately separate so the future N-company compare
sheet can reuse extraction without touching the template.
"""

from __future__ import annotations

import argparse
import base64
import colorsys
import glob
import hashlib
import html as html_mod
import os
import re
import subprocess
import sys
import urllib.request
from datetime import date
from typing import Any

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
if SCRIPTS not in sys.path:  # sibling imports work when imported as a library, too
    sys.path.insert(0, SCRIPTS)

ROOT = os.environ.get("WEB_RESEARCH_HOME") or os.path.dirname(SCRIPTS)
STORE = os.path.join(ROOT, "store")
OUT = os.path.join(SCRIPTS, "_out", "briefs")
FONTCACHE = os.path.join(OUT, ".fontcache")
IMGCACHE = os.path.join(OUT, ".imgcache")

from icons import raw_svg  # noqa: E402
from offeringscheck import SPINE_PREFIXES, parse_roster  # noqa: E402

from store import load as store_load  # noqa: E402
from store import read_doc as store_read_doc  # noqa: E402
from store import resolve as store_resolve  # noqa: E402

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

PAPER = "#F5F1E8"
INK = "#1B1813"

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
        accent, accent_on_dark = "#4A4438", "#C9BFA8"

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
    scaffold_serif = _google_css("Newsreader", "ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400", fetch)
    scaffold_mono = _google_css("Fragment Mono", None, fetch)
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

    display = specs[0]["css"] if specs else f"'Newsreader',{SERIF_STACK}"
    return {
        "css": "\n".join(css_parts),
        "specs": specs,
        "display": display,
        "body": f"'Newsreader',{SERIF_STACK}",
        "mono": f"'Fragment Mono',{MONO_STACK}",
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


def load_screenshot(slug: str) -> dict[str, str] | None:
    """Latest captured homepage screenshot, sips-compressed to a sane embed size. Local-only."""
    shots = sorted(glob.glob(os.path.join(STORE, slug, "captures", "*", ".payloads", "homepage.png")))
    if not shots:
        return None
    src = shots[-1]
    cap_date = os.path.basename(os.path.dirname(os.path.dirname(src)))
    os.makedirs(IMGCACHE, exist_ok=True)
    dst = os.path.join(IMGCACHE, f"{slug}-homepage.jpg")
    if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src):
        r = subprocess.run(
            ["sips", "--resampleWidth", "1200", "-s", "format", "jpeg",
             "-s", "formatOptions", "72", src, "--out", dst],
            capture_output=True)
        if r.returncode != 0:
            dst = src if os.path.getsize(src) < 3_000_000 else ""
    if not dst:
        return None
    data = _b64_file(dst)
    return {"data": data, "date": cap_date} if data else None


# ---------------------------------------------------------------- markdown (subset)

def esc(s: str) -> str:
    return html_mod.escape(str(s), quote=False)


def md_inline(s: str) -> str:
    s = esc(s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\s*\[anchor:[^\]]*\]", "", s)
    s = re.sub(r"\[(HIGH|MED|LOW)([^\]]*)\]",
               lambda m: f'<span class="conf conf-{m.group(1).lower()}">{m.group(1)}{esc(m.group(2))}</span>', s)

    def code(m: re.Match) -> str:
        c = m.group(1)
        vis = re.fullmatch(r"\[?\s*(published|partial|on-request)\s*\]?", c.strip())
        if vis:
            return f'<span class="vis vis-{vis.group(1)}">{vis.group(1)}</span>'
        return f"<code>{c}</code>"
    s = re.sub(r"`([^`]+)`", code, s)
    s = re.sub(r"\*\*\*([^*]+)\*\*\*", r"<strong><em>\1</em></strong>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\w_])_([^_\n]+)_(?![\w_])", r"<em>\1</em>", s)
    return s


def _parse_table(lines: list[str]) -> tuple[list[str], list[list[str]]]:
    def cells(row: str) -> list[str]:
        return [c.strip() for c in row.strip().strip("|").split("|")]
    header = cells(lines[0])
    body = [cells(r) for r in lines[2:] if r.strip().startswith("|")]
    return header, body


def md_blocks(md: str) -> str:
    """The dossier's markdown subset → HTML: paragraphs, lists, tables, fences, quotes, h3/h4."""
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("```"):
            j = i + 1
            buf = []
            while j < len(lines) and not lines[j].startswith("```"):
                buf.append(lines[j])
                j += 1
            out.append("<pre>" + esc("\n".join(buf)) + "</pre>")
            i = j + 1
            continue
        if line.startswith("#"):
            out.append(f'<h4 class="subhead">{md_inline(line.lstrip("# "))}</h4>')
            i += 1
            continue
        if line.strip().startswith("|"):
            j = i
            buf = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                buf.append(lines[j])
                j += 1
            if len(buf) >= 2:
                header, body = _parse_table(buf)
                th = "".join(f"<th>{md_inline(h)}</th>" for h in header)
                trs = "".join("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in r) + "</tr>" for r in body)
                out.append(f'<div class="tablewrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')
            i = j
            continue
        if line.strip().startswith(">"):
            j = i
            buf = []
            while j < len(lines) and lines[j].strip().startswith(">"):
                buf.append(lines[j].strip().lstrip("> "))
                j += 1
            out.append("<blockquote>" + "<br>".join(md_inline(b) for b in buf) + "</blockquote>")
            i = j
            continue
        if re.match(r"^\s*-\s+", line):
            j = i
            items: list[tuple[int, str]] = []
            while j < len(lines) and (re.match(r"^\s*-\s+", lines[j]) or (lines[j].startswith("  ") and lines[j].strip() and items)):
                m = re.match(r"^(\s*)-\s+(.*)$", lines[j])
                if m:
                    items.append((len(m.group(1)), m.group(2)))
                else:
                    items[-1] = (items[-1][0], items[-1][1] + " " + lines[j].strip())
                j += 1
            out.append(_render_list(items))
            i = j
            continue
        j = i
        buf = []
        while j < len(lines) and lines[j].strip() and not re.match(r"^(\s*-\s+|#|```|\||>)", lines[j]):
            buf.append(lines[j].strip())
            j += 1
        para = md_inline(" ".join(buf))
        cls = ' class="callout"' if re.match(r"<strong>(Shape finding|Prominence)", para) else ""
        out.append(f"<p{cls}>{para}</p>")
        i = j
    return "\n".join(out)


def _render_list(items: list[tuple[int, str]]) -> str:
    out = ["<ul>"]
    prev = items[0][0] if items else 0
    base = prev
    for indent, text in items:
        if indent > prev:
            out.append("<ul>")
        elif indent < prev:
            out.append("</li></ul>" * max(1, (prev - indent) // 2))
            out.append("</li>")
        elif out[-1] != "<ul>":
            out.append("</li>")
        body = md_inline(text)
        cls = ' class="def"' if re.match(r"<strong>[^<]+:</strong>", body) else ""
        out.append(f"<li{cls}>{body}")
        prev = indent
    out.append("</li>" + "</ul>" * (1 + max(0, (prev - base) // 2)))
    return "".join(out)


# ---------------------------------------------------------------- extraction

def _split_sections(body: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    cur, buf = None, []
    for line in body.split("\n"):
        if line.startswith("## "):
            if cur:
                sections[cur] = "\n".join(buf).strip()
            cur, buf = line[3:].strip().lower(), []
        elif cur:
            buf.append(line)
    if cur:
        sections[cur] = "\n".join(buf).strip()
    return sections


def _datestr(v: Any) -> str:
    return str(v) if v else ""


def _age_days(v: Any) -> int | None:
    try:
        return (date.today() - date.fromisoformat(str(v))).days
    except (TypeError, ValueError):
        return None


def extract_offerings(slug: str) -> dict[str, Any] | None:
    path = os.path.join(STORE, slug, "offerings.md")
    if not os.path.exists(path):
        return None
    fm, body = store_read_doc(path)
    sections = _split_sections(body)
    header, rows = parse_roster(body)
    groups: list[dict[str, Any]] = []
    buyable = 0
    if header:
        hdr = [h.lower() for h in header]
        ci = {pref: next((i for i, h in enumerate(hdr) if h.startswith(pref)), None) for pref in SPINE_PREFIXES}
        cur: dict[str, Any] | None = None
        for r in rows:
            def cell(row: list[str], key: str) -> str:
                idx = ci.get(key)
                return row[idx] if idx is not None and idx < len(row) else ""

            name = cell(r, "offering")
            if not name:
                continue
            kind = cell(r, "kind").lower()
            if kind == "family":
                cur = {"name": re.sub(r"\*\*", "", name), "what": cell(r, "what"), "skus": []}
                groups.append(cur)
            else:
                buyable += 1
                if cur is None:
                    cur = {"name": "", "what": "", "skus": []}
                    groups.append(cur)
                cur["skus"].append({"name": re.sub(r"\*\*", "", name), "slug": cell(r, "slug"),
                                    "price": cell(r, "price"), "vis": cell(r, "visibility"), "what": cell(r, "what")})
    return {
        "captured_at": _datestr(fm.get("captured_at")),
        "age": _age_days(fm.get("captured_at")),
        "enumeration": str(fm.get("enumeration") or ""),
        "site_notes": str(fm.get("site_notes") or ""),
        "overview_md": sections.get("portfolio overview", ""),
        "groups": groups,
        "buyable": buyable,
        "families": len([g for g in groups if g["name"]]),
    }


def extract_telehealth(slug: str) -> dict[str, Any] | None:
    path = os.path.join(STORE, slug, "telehealth.md")
    if not os.path.exists(path):
        return None
    fm, _ = store_read_doc(path)
    cuts = {k: str(v) for k, v in fm.items()
            if k not in ("schema_version", "domain", "captured_at") and v is not None and not isinstance(v, (dict, list))}
    return {"captured_at": _datestr(fm.get("captured_at")), "cuts": cuts}


def _index_mark(slug: str, domain: str, fetch: bool) -> str | None:
    """Newest locally-captured logomark, else the company favicon (Google s2) disk-cached on first
    fetch — so the index renders offline after one warm run. No mark, no fetch → letter tile."""
    hits = sorted(glob.glob(os.path.join(STORE, slug, "captures", "*", ".payloads", "logos", "logomark-s2.png")))
    if hits:
        return _b64_file(hits[-1])
    if not domain:
        return None
    cache = os.path.join(IMGCACHE, f"{slug}-favicon.png")
    if not os.path.exists(cache):
        if not fetch:
            return None
        raw = _fetch(f"https://www.google.com/s2/favicons?domain={domain}&sz=256")
        if not raw:
            return None
        os.makedirs(IMGCACHE, exist_ok=True)
        with open(cache, "wb") as f:
            f.write(raw)
    return _b64_file(cache)


def extract_index(fetch: bool = True) -> list[dict[str, Any]]:
    """One light row per profiled company — frontmatter + layer clocks only, none of the brief's
    heavy assets (fonts/screenshots/remote logos). Everything is computed at render time."""
    rows: list[dict[str, Any]] = []
    for slug, fm in sorted(store_load().items()):
        off = extract_offerings(slug)
        rows.append({
            "slug": slug,
            "name": str(fm.get("name") or fm.get("domain") or slug),
            "domain": str(fm.get("domain") or ""),
            "description": str(fm.get("description") or ""),
            "industry": str(fm.get("primary_industry") or "Unclassified"),
            "captured_at": _datestr(fm.get("captured_at")),
            "age": _age_days(fm.get("captured_at")),
            "buyable": off["buyable"] if off else None,
            "roster_at": off["captured_at"] if off else "",
            "cohort": extract_telehealth(slug) is not None,
            "mark": _index_mark(slug, str(fm.get("domain") or ""), fetch),
        })
    return rows


SECTION_ORDER = [
    ("overview", "Overview"),
    ("what they offer", "Offer architecture"),
    ("how it works / model", "Model & monetization"),
    ("positioning & audience", "Positioning"),
    ("credibility & proof", "Proof & trust signals"),
    ("visual & brand impression", "Brand system"),
    ("strategic read", "Strategic read"),
    ("nav structure", "Site structure"),
]
KNOWN = {k for k, _ in SECTION_ORDER} | {"provenance"}


def extract_model(query: str, fetch: bool = True) -> dict[str, Any] | None:
    profiles = store_load()
    slug = store_resolve(query, profiles)
    if not slug:
        return None
    fm, body = store_read_doc(os.path.join(STORE, slug, "profile.md"))
    raw_sections = _split_sections(body)
    extras = [(k.title(), v) for k, v in raw_sections.items() if k not in KNOWN]

    fonts = build_fonts(list(fm.get("fonts") or []), fetch)
    pal = palette(fm.get("brand_colors"), fm.get("color_scheme"))

    return {
        "slug": slug,
        "name": str(fm.get("name") or fm.get("domain") or slug),
        "domain": str(fm.get("domain") or ""),
        "aliases": [str(a) for a in (fm.get("aliases") or [])],
        "description": str(fm.get("description") or ""),
        "captured_at": _datestr(fm.get("captured_at")),
        "age": _age_days(fm.get("captured_at")),
        "method": str(fm.get("capture_method") or ""),
        "schema_version": str(fm.get("schema_version") or ""),
        "classification": {
            "entity": str(fm.get("entity_type") or ""),
            "industry": str(fm.get("primary_industry") or ""),
            "model": str(fm.get("business_model") or ""),
            "market": [str(t) for t in (fm.get("target_market") or [])],
            "shape": str(fm.get("portfolio_shape") or ""),
            "category": [str(c) for c in (fm.get("offering_category") or [])],
        },
        "socials": dict(fm.get("socials") or {}),
        "external": dict(fm.get("external") or {}),
        "unverified": [str(u) for u in (fm.get("unverified_fields") or [])],
        "site_notes": str(fm.get("site_notes") or ""),
        "pal": pal,
        "fonts": fonts,
        "company_fonts": list(fm.get("fonts") or []),
        "logo": load_logo(slug, fm, fetch),
        "logomark": load_logomark(slug, fm, fetch),
        "screenshot": load_screenshot(slug),
        "sections": raw_sections,
        "extras": extras,
        "offerings": extract_offerings(slug),
        "telehealth": extract_telehealth(slug),
        "generated": str(date.today()),
    }


# ---------------------------------------------------------------- render

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%}
body{background:var(--desk);font-family:var(--body);color:var(--ink);
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
::selection{background:var(--hero-accent);color:var(--hero-bg)}
a{color:var(--accent);text-decoration:none;border-bottom:1px solid color-mix(in srgb,var(--accent) 40%,transparent)}
a:hover{border-bottom-color:var(--accent)}
.sheet{position:relative;max-width:1060px;margin:44px auto;padding:0 64px;
  background:var(--paper);
  box-shadow:0 30px 80px rgba(20,16,8,.28),0 2px 10px rgba(20,16,8,.14)}
.sheet::before{content:"";position:absolute;inset:0;pointer-events:none;opacity:.5;
  background-image:var(--grain);background-size:300px 300px}
.crop{position:absolute;width:18px;height:18px;pointer-events:none;opacity:.55}
.crop::before,.crop::after{content:"";position:absolute;background:var(--ink)}
.crop::before{width:18px;height:1px;top:9px}
.crop::after{width:1px;height:18px;left:9px}
.crop.tl{top:14px;left:14px}.crop.tr{top:14px;right:14px}
.crop.bl{bottom:14px;left:14px}.crop.br{bottom:14px;right:14px}

.mono,.label{font-family:var(--mono)}
.label{font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:color-mix(in srgb,var(--ink) 62%,var(--paper))}

/* masthead */
.masthead{padding:48px 0 0}
.mh-row{display:flex;justify-content:space-between;align-items:baseline;padding-bottom:10px}
.mh-left{font-family:var(--mono);font-size:11.5px;letter-spacing:.22em;text-transform:uppercase}
.mh-left b{font-weight:400;color:var(--accent)}
.mh-right{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;color:color-mix(in srgb,var(--ink) 55%,var(--paper))}
.rule-heavy{height:3px;background:var(--ink);transform-origin:left;animation:drawX .9s cubic-bezier(.22,1,.36,1) both}
.rule-thin{height:1px;background:var(--rule);margin-top:2px;transform-origin:left;animation:drawX .9s .08s cubic-bezier(.22,1,.36,1) both}

/* hero */
.hero{position:relative;margin:30px -64px 0;padding:52px 64px 58px;background:
  radial-gradient(900px 420px at 88% -12%,color-mix(in srgb,var(--hero-accent) 16%,transparent),transparent 62%),
  var(--hero-bg);color:var(--hero-fg);animation:rise .8s .15s both}
.hero-top{display:flex;justify-content:space-between;align-items:flex-start;gap:24px}
.hero .eyebrow{font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;
  color:color-mix(in srgb,var(--hero-fg) 64%,transparent);padding-top:4px}
.hero .eyebrow a{color:var(--hero-accent);border-bottom:1px solid color-mix(in srgb,var(--hero-accent) 32%,transparent);
  padding-bottom:2px;transition:border-color .2s}
.hero .eyebrow a:hover{border-bottom-color:var(--hero-accent)}
.hero .eyebrow a .ic{width:11px;height:11px;vertical-align:-1px;margin-left:4px}
.caprec{text-align:right;font-family:var(--mono);border-top:2px solid var(--hero-accent);padding-top:9px;min-width:200px}
.caprec .cr-label{display:block;font-size:9.5px;letter-spacing:.22em;text-transform:uppercase;
  color:color-mix(in srgb,var(--hero-fg) 55%,transparent)}
.caprec .cr-date{display:block;font-size:17px;letter-spacing:.1em;color:var(--hero-accent);margin:4px 0 3px}
.caprec .cr-sub{display:block;font-size:10px;letter-spacing:.08em;
  color:color-mix(in srgb,var(--hero-fg) 55%,transparent)}
.hero-mark{margin:30px 0 8px;animation:rise .8s .3s both}
.mark-plate{display:inline-block;background:var(--paper);padding:16px 26px;border:1px solid rgba(0,0,0,.12)}
.mark-text{font-family:var(--display);font-weight:600;color:var(--hero-accent);line-height:1.02;letter-spacing:-.01em}
.alias{font-family:var(--mono);font-size:11px;letter-spacing:.12em;margin-top:14px;
  color:color-mix(in srgb,var(--hero-fg) 52%,transparent)}
.hero-desc{font-family:var(--display);font-size:var(--desc-size,29px);line-height:1.32;font-weight:400;
  max-width:38ch;margin-top:22px;animation:rise .8s .42s both}

/* classification + cohort cuts — quiet chip strips; corpus-cut keys, deliberately demoted */
.cohort{padding:18px 0 20px;border-bottom:1px solid var(--rule);animation:rise .8s .5s both}
.cohort>.label{display:block;margin-bottom:11px}
.cohort .cuts{display:flex;flex-wrap:wrap;gap:8px}
.cut{font-family:var(--mono);font-size:11px;letter-spacing:.05em;padding:4px 10px;border:1px solid var(--rule)}
.cut b{font-weight:400;color:var(--accent)}
.cut.unclear{color:color-mix(in srgb,var(--ink) 45%,var(--paper));border-style:dashed}
.cut.unclear b{color:inherit}

/* tab bar */
.tabbar{position:sticky;top:0;z-index:60;display:flex;gap:4px;background:var(--paper);
  margin:0 -64px;padding:0 64px;border-bottom:2px solid var(--ink);animation:rise .8s .6s both}
.tabbtn{display:block;cursor:pointer;font-family:var(--mono);
  font-size:12px;letter-spacing:.14em;text-transform:uppercase;padding:18px 18px 15px;
  color:color-mix(in srgb,var(--ink) 48%,var(--paper));border-bottom:3px solid transparent;margin-bottom:-2px;
  -webkit-tap-highlight-color:transparent;user-select:none}
.tabbtn .n{color:var(--accent);margin-right:7px}
.tabbtn:hover{color:var(--ink)}
/* CSS-only tabs (no JS — survives iOS Quick Look on an AirDropped file) */
.tabin{position:absolute;width:1px;height:1px;opacity:0;pointer-events:none}
.panel{display:none;padding-top:32px;min-height:300px}
.panel.flush{padding-top:0}
#t-profile:checked~.panel[data-t="profile"],
#t-offer:checked~.panel[data-t="offer"],
#t-brand:checked~.panel[data-t="brand"],
#t-trust:checked~.panel[data-t="trust"]{display:block;animation:rise .4s both}
#t-profile:checked~.tabbar label[data-t="profile"],
#t-offer:checked~.tabbar label[data-t="offer"],
#t-brand:checked~.tabbar label[data-t="brand"],
#t-trust:checked~.tabbar label[data-t="trust"]{color:var(--ink);border-bottom-color:var(--accent)}
#t-profile:focus-visible~.tabbar label[data-t="profile"],
#t-offer:focus-visible~.tabbar label[data-t="offer"],
#t-brand:focus-visible~.tabbar label[data-t="brand"],
#t-trust:focus-visible~.tabbar label[data-t="trust"]{outline:2px solid var(--accent);outline-offset:-2px}
.panel-label{display:none}

/* sections (collapsible) */
details.sec{border-top:1px solid var(--ink)}
details.sec:first-of-type{border-top:none}
details.sec summary{list-style:none;cursor:pointer;display:flex;align-items:baseline;gap:14px;
  padding:21px 0 19px;-webkit-tap-highlight-color:transparent}
details.sec summary::-webkit-details-marker{display:none}
.sec-title{font-family:var(--mono);font-size:12.5px;letter-spacing:.2em;text-transform:uppercase;white-space:nowrap}
summary:hover .sec-title{color:var(--accent)}
.sec-peek{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
  font-style:italic;font-size:14.5px;color:color-mix(in srgb,var(--ink) 52%,var(--paper))}
details[open] .sec-peek{visibility:hidden}
.sec-meta{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;white-space:nowrap;
  color:color-mix(in srgb,var(--ink) 50%,var(--paper))}
.sec-toggle{font-family:var(--mono);font-size:15px;color:var(--accent);width:16px;text-align:center}
.sec-toggle::before{content:"+"}
details[open] .sec-toggle::before{content:"−"}
.sec-body{padding:4px 0 36px}

.panel p{font-size:17.5px;line-height:1.66;margin-bottom:16px;max-width:74ch}
.panel p strong{font-weight:600}
.notcaptured{font-family:var(--mono);font-size:12px;letter-spacing:.08em;
  color:color-mix(in srgb,var(--ink) 48%,var(--paper));padding:6px 0 14px}
.subhead{font-family:var(--mono);font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;
  margin:30px 0 14px;color:color-mix(in srgb,var(--ink) 70%,var(--paper))}
.panel ul{list-style:none;margin:4px 0 20px}
.panel ul ul{margin:6px 0 4px 22px}
.panel li{font-size:16.5px;line-height:1.6;padding:11px 0;border-top:1px solid var(--rule);max-width:78ch}
.panel ul ul li{border-top:none;padding:3px 0;font-size:15.5px}
.panel li.def strong{font-family:var(--display);font-size:1.06em;font-weight:600}
.callout{border-left:3px solid var(--accent);padding:4px 0 4px 18px;max-width:72ch}
code{font-family:var(--mono);font-size:.88em;background:color-mix(in srgb,var(--ink) 6%,transparent);padding:1px 5px}
pre{font-family:var(--mono);font-size:12.5px;line-height:1.6;padding:20px 22px;overflow-x:auto;
  border:1px solid var(--rule);background:color-mix(in srgb,var(--ink) 3%,transparent);margin-bottom:16px}
blockquote{border-left:2px solid var(--rule);padding-left:16px;font-style:italic;margin:10px 0 16px;
  color:color-mix(in srgb,var(--ink) 78%,var(--paper));font-size:16px;line-height:1.6;max-width:72ch}
.conf{font-family:var(--mono);font-size:10px;letter-spacing:.08em;padding:2px 6px;vertical-align:1px;white-space:nowrap}
.conf-high{background:var(--ink);color:var(--paper)}
.conf-med{border:1px solid var(--ink)}
.conf-low{border:1px dashed color-mix(in srgb,var(--ink) 50%,var(--paper));color:color-mix(in srgb,var(--ink) 55%,var(--paper))}
.vis{font-family:var(--mono);font-size:10px;letter-spacing:.08em;padding:2px 7px;white-space:nowrap;text-transform:uppercase}
.vis-published{border:1px solid var(--accent);color:var(--accent)}
.vis-partial{border:1px dashed var(--accent);color:var(--accent)}
.vis-on-request{border:1px dashed color-mix(in srgb,var(--ink) 45%,var(--paper));color:color-mix(in srgb,var(--ink) 55%,var(--paper))}

/* generic tables (body markdown) */
.tablewrap{overflow-x:auto;margin:8px 0 20px}
.tablewrap table{width:100%;border-collapse:collapse;font-size:14px}
.tablewrap th{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;text-align:left;
  padding:8px 10px;border-bottom:2px solid var(--ink)}
.tablewrap td{padding:8px 10px;border-bottom:1px solid var(--rule);vertical-align:top;line-height:1.5;overflow-wrap:break-word}

/* offer architecture */
.statband{display:flex;gap:56px;align-items:flex-end;padding:18px 0 32px;flex-wrap:wrap}
.stat .num{font-family:var(--display);font-size:50px;font-weight:600;line-height:1;color:var(--ink)}
.stat .label{display:block;margin-top:8px}
.enum{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;padding:6px 12px;margin-bottom:9px;display:inline-block}
.enum-complete{border:1px solid var(--accent);color:var(--accent)}
.enum-floor{border:1px dashed var(--ink)}
.enum-unknown{border:1px dashed color-mix(in srgb,var(--ink) 40%,var(--paper));color:color-mix(in srgb,var(--ink) 55%,var(--paper))}
.roster-wrap{overflow-x:auto}
.roster{width:100%;border-collapse:collapse;font-size:14px;margin:10px 0 8px;table-layout:fixed}
.roster th{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;text-align:left;
  padding:6px 10px 8px;border-bottom:2px solid var(--ink)}
.roster td{padding:9px 10px;border-bottom:1px solid var(--rule);vertical-align:baseline;line-height:1.45;overflow-wrap:break-word}
.roster .fam td{font-family:var(--display);font-size:17.5px;font-weight:600;padding:26px 10px 7px;
  border-bottom:2px solid var(--ink);overflow-wrap:normal}
.roster .fam .famwhat{font-family:var(--body);font-size:13.5px;font-weight:400;font-style:italic;
  color:color-mix(in srgb,var(--ink) 65%,var(--paper))}
.roster td.price{font-family:var(--mono);font-size:12px;line-height:1.5}
.roster td.price code{background:none;padding:0;font-size:1em}
.roster td.what{font-size:13.5px;color:color-mix(in srgb,var(--ink) 78%,var(--paper))}
.roster a{color:inherit;border-bottom:none}
.roster a:hover{color:var(--accent)}

/* brand system */
.brandgrid{display:grid;grid-template-columns:1fr 1fr;gap:44px;margin:16px 0 36px}
.swatches{display:grid;grid-template-columns:repeat(auto-fill,minmax(112px,1fr));gap:10px}
.swatch{border:1px solid var(--rule)}
.swatch .chip{height:64px;border-bottom:1px solid var(--rule)}
.swatch .meta{padding:8px 10px;font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;line-height:1.6}
.swatch .meta b{font-weight:400;display:block;color:color-mix(in srgb,var(--ink) 55%,var(--paper));text-transform:uppercase}
.typespec{border:1px solid var(--rule);padding:14px 16px;margin-bottom:10px;display:flex;gap:18px;align-items:center}
.typespec .ag{font-size:42px;line-height:1;min-width:66px}
.typespec .tmeta{font-family:var(--mono);font-size:11px;letter-spacing:.08em;line-height:1.7;
  color:color-mix(in srgb,var(--ink) 62%,var(--paper))}
.typespec .tmeta b{font-weight:400;color:var(--ink);font-size:12.5px}
.marks{display:flex;gap:12px;flex-wrap:wrap;margin-top:10px}
.marktile{border:1px solid var(--rule);width:calc(50% - 6px);min-width:180px}
.marktile .tile{display:flex;align-items:center;justify-content:center;height:110px;padding:18px}
.marktile .cap{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;
  padding:7px 10px;border-top:1px solid var(--rule);color:color-mix(in srgb,var(--ink) 55%,var(--paper))}
.specimen{margin:10px 0 16px;border:1px solid var(--rule)}
.specimen img{display:block;width:100%;max-height:540px;object-fit:cover;object-position:top;
  -webkit-mask-image:linear-gradient(to bottom,#000 78%,transparent);mask-image:linear-gradient(to bottom,#000 78%,transparent)}
.specimen .cap{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;
  padding:9px 12px;border-top:1px solid var(--rule);display:flex;justify-content:space-between;
  color:color-mix(in srgb,var(--ink) 55%,var(--paper))}

/* provenance */
.prov{margin:0 -64px;padding:54px 64px 50px;background:var(--ink);color:color-mix(in srgb,var(--paper) 88%,var(--ink))}
.prov .label{color:color-mix(in srgb,var(--paper) 48%,transparent)}
.prov-clocks{display:flex;gap:44px;flex-wrap:wrap;padding-bottom:30px;border-bottom:1px solid color-mix(in srgb,var(--paper) 18%,transparent);margin-bottom:32px}
.clock .label{display:block;margin-bottom:6px}
.clock .val{font-family:var(--mono);font-size:16px;letter-spacing:.06em;color:var(--accent-dark)}
.clock .val small{font-size:10.5px;color:color-mix(in srgb,var(--paper) 55%,transparent)}
.prov-grid{display:grid;grid-template-columns:1.35fr 1fr;gap:52px}
.provrow{display:grid;grid-template-columns:128px 1fr;gap:20px;padding:12px 0;
  border-top:1px solid color-mix(in srgb,var(--paper) 12%,transparent)}
.provrow .pk{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  padding-top:4px;color:color-mix(in srgb,var(--paper) 55%,transparent)}
.provrow .pv{font-size:14px;line-height:1.65;max-width:62ch}
.provrow .pv strong{color:var(--paper);font-weight:600}
.prov h4{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--accent-dark);margin-bottom:14px}
.prov ul{list-style:none}
.prov li{font-size:14.5px;line-height:1.6;padding:8px 0;border-top:1px solid color-mix(in srgb,var(--paper) 12%,transparent);max-width:70ch}
.prov li strong{color:var(--paper);font-weight:600}
.prov p{font-size:14.5px;line-height:1.6;margin-bottom:10px;max-width:70ch}
.prov code{background:color-mix(in srgb,var(--paper) 10%,transparent);color:inherit}
.prov a{color:var(--accent-dark);border-bottom-color:color-mix(in srgb,var(--accent-dark) 40%,transparent)}
.prov .conf-high{background:var(--paper);color:var(--ink)}
.prov .conf-med{border-color:var(--paper)}
.fieldnotes{margin-top:30px;padding-top:22px;border-top:1px solid color-mix(in srgb,var(--paper) 18%,transparent)}
.fieldnotes p{font-family:var(--mono);font-size:11.5px;line-height:1.8;letter-spacing:.02em;
  color:color-mix(in srgb,var(--paper) 62%,transparent);max-width:none}

/* footer */
.foot{padding:30px 0 38px;text-align:center}
.foot p{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;
  color:color-mix(in srgb,var(--ink) 48%,var(--paper));line-height:2.1}
.foot a{color:inherit}

@keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
@keyframes drawX{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}

@media (max-width:760px){
  .sheet{margin:0;padding:0 22px}
  .hero{margin:20px -22px 0;padding:34px 22px 38px}
  .hero-top{flex-direction:column}
  .caprec{text-align:left;min-width:0}
  .prov{margin:0 -22px;padding:40px 22px}
  .provrow{grid-template-columns:1fr;gap:6px}
  .tabbar{margin:0 -22px;padding:0 12px;overflow-x:auto}
  .tabbtn{padding:15px 12px 12px;white-space:nowrap}
  .brandgrid,.prov-grid{grid-template-columns:1fr}
  .hero-desc{font-size:min(23px,var(--desc-size,29px))}
  .sec-peek{display:none}
}
@media print{
  body{background:#fff}
  .sheet{box-shadow:none;margin:0;max-width:none}
  *{animation:none!important}
  .hero,.prov{print-color-adjust:exact;-webkit-print-color-adjust:exact}
  .tabbar{display:none}
  .panel{display:block!important}
  .panel-label{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.22em;
    text-transform:uppercase;border-top:3px solid var(--ink);padding:14px 0 4px;margin-top:18px}
  .sec-toggle{display:none}
  details.sec summary{break-after:avoid}
  .statband,.typespec,.swatch,.marktile{break-inside:avoid}
  .roster tr{break-inside:avoid}
}
"""

GRAIN = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E"
         "%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E"
         "%3CfeColorMatrix values='0 0 0 0 0.35 0 0 0 0 0.32 0 0 0 0 0.24 0 0 0 0.05 0'/%3E%3C/filter%3E"
         "%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E\")")

# Tabs are CSS-only (radio + :checked) so they work with JS disabled — e.g. iOS Quick Look on
# an AirDropped file. The only JS is a progressive enhancement: expand every <details> before
# printing so a printed brief is complete. No-JS viewers simply print whatever's open.
JS = "window.addEventListener('beforeprint',()=>document.querySelectorAll('details').forEach(d=>d.open=true));"


def _truncate(s: str, n: int = 130) -> str:
    s = s.strip()
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0]
    return cut.rstrip(" ·,;") + " …"


def _peek(md: str, n: int = 120) -> str:
    """First plain-prose line of a section, stripped of markdown — the closed-state teaser."""
    for line in md.split("\n"):
        t = line.strip()
        if not t or t.startswith(("#", "```", "|", ">")):
            continue
        t = re.sub(r"\[anchor:[^\]]*\]", "", t)
        t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
        t = re.sub(r"[*_`]", "", t)
        if t.startswith("- "):
            t = t[2:]
        return esc(_truncate(t, n))
    return ""


def _dsec(title: str, body_html: str, peek: str = "", open_: bool = False, meta: str = "") -> str:
    meta_html = f'<span class="sec-meta">{meta}</span>' if meta else ""
    return (f'<details class="sec"{" open" if open_ else ""}><summary>'
            f'<span class="sec-title">{esc(title)}</span>'
            f'<span class="sec-peek">{peek}</span>{meta_html}'
            f'<span class="sec-toggle"></span></summary>'
            f'<div class="sec-body">{body_html}</div></details>')


def _hero_mark_html(m: dict[str, Any]) -> str:
    logo = m["logo"]
    if logo["kind"] == "svg":
        aspect = logo.get("aspect") or 4.0
        height = max(40, min(88, int(440 / max(aspect, 0.8))))
        svg = re.sub(r"<svg ", f'<svg style="height:{height}px;width:auto;display:block" ', logo["svg"], count=1)
        return f'<div class="mark-plate">{svg}</div>' if logo["plate"] else svg
    if logo["kind"] == "img":
        aspect = logo.get("aspect") or 4.0
        height = max(36, min(80, int(400 / max(aspect, 0.8))))
        img = f'<img src="{logo["data"]}" style="height:{height}px;width:auto;display:block" alt="{esc(m["name"])} wordmark">'
        return f'<div class="mark-plate">{img}</div>' if logo["plate"] else img
    name = m["name"]
    size = 64 if len(name) <= 12 else (50 if len(name) <= 20 else 40)
    return f'<div class="mark-text" style="font-size:{size}px">{esc(name)}</div>'


def _roster_html(m: dict[str, Any]) -> str:
    off = m["offerings"]
    enum = off["enumeration"]
    if enum == "indexed-complete":
        badge = '<span class="enum enum-complete">complete at the indexed level</span>'
        count = str(off["buyable"])
    elif enum == "lines-omitted":
        badge = '<span class="enum enum-floor">floor — lines omitted</span>'
        count = f"≥{off['buyable']}"
    else:
        badge = '<span class="enum enum-unknown">enumeration unverified</span>'
        count = f"{off['buyable']}"

    # first paragraph of the portfolio overview stays visible; the shape findings collapse
    paras = [p for p in re.split(r"\n\s*\n", off["overview_md"]) if p.strip()]
    lead = md_blocks(paras[0]) if paras else ""
    findings_md = "\n\n".join(paras[1:])

    out = [lead]
    out.append('<div class="statband">')
    out.append(f'<div class="stat"><div class="num">{count}</div><span class="label">buyable SKUs</span></div>')
    out.append(f'<div class="stat"><div class="num">{off["families"]}</div><span class="label">product lines</span></div>')
    out.append(f'<div class="stat">{badge}<span class="label">roster of {off["captured_at"]}</span></div>')
    out.append("</div>")

    if findings_md:
        n_findings = len(re.findall(r"\*\*Shape finding", findings_md))
        title = f"Shape findings ({n_findings})" if n_findings else "Catalog shape"
        out.append(_dsec(title, md_blocks(findings_md), peek=_peek(findings_md), open_=False))

    rows: list[str] = ['<div class="roster-wrap"><table class="roster">'
                       '<colgroup><col style="width:24%"><col style="width:17%"><col style="width:9%"><col style="width:50%"></colgroup>'
                       '<thead><tr><th>Offering</th><th>Price (verbatim)</th><th></th><th>What</th></tr></thead><tbody>']
    base = f"https://{m['domain']}" if m["domain"] else ""
    for g in off["groups"]:
        if g["name"]:
            rows.append(f'<tr class="fam"><td colspan="2">{esc(g["name"])}</td>'
                        f'<td colspan="2" class="famwhat">{md_inline(_truncate(g["what"], 110))}</td></tr>')
        for s in g["skus"]:
            slug_raw = re.sub(r"[`*]", "", s["slug"]).strip()
            name_html = esc(s["name"])
            if base and slug_raw.startswith("/") and " " not in slug_raw:
                name_html = f'<a href="{base}{slug_raw}">{name_html}</a>'
            vis = re.sub(r"[`*]", "", s["vis"]).strip()
            vis_html = f'<span class="vis vis-{vis}">{vis}</span>' if vis in ("published", "partial", "on-request") else esc(vis)
            rows.append(f'<tr><td>{name_html}</td><td class="price">{md_inline(s["price"])}</td>'
                        f'<td>{vis_html}</td><td class="what">{md_inline(_truncate(s["what"]))}</td></tr>')
    rows.append("</tbody></table></div>")
    out.append(_dsec(f"Full roster — {off['buyable']} SKUs", "".join(rows), open_=True,
                     meta=f"as captured {off['captured_at']}"))
    return "".join(out)


def _brand_system_html(m: dict[str, Any]) -> str:
    out = []
    prose = m["sections"].get("visual & brand impression")
    if prose:
        out.append(md_blocks(prose))
    else:
        out.append('<p class="notcaptured">Visual impression — not captured in this dossier.</p>')

    out.append('<div class="brandgrid"><div>')
    out.append('<h4 class="subhead">Palette — as captured</h4>')
    if m["pal"]["swatches"]:
        out.append('<div class="swatches">')
        for sw in m["pal"]["swatches"]:
            out.append(f'<div class="swatch"><div class="chip" style="background:{sw["hex"]}"></div>'
                       f'<div class="meta"><b>{esc(sw["key"])}</b>{sw["hex"]}</div></div>')
        out.append("</div>")
    else:
        out.append('<p class="notcaptured">Brand colors — not captured.</p>')
    marks = []
    logo = m["logo"]
    if logo["kind"] in ("svg", "img"):
        inner = (re.sub(r"<svg ", '<svg style="max-height:56px;max-width:100%;width:auto" ', logo["svg"], count=1)
                 if logo["kind"] == "svg" else f'<img src="{logo["data"]}" style="max-height:56px;max-width:100%" alt="">')
        ground = "background:" + (m["pal"]["hero_bg"] if not logo["plate"] else "var(--paper)")
        marks.append(f'<div class="marktile"><div class="tile" style="{ground}">{inner}</div><div class="cap">wordmark</div></div>')
    if m["logomark"]:
        marks.append(f'<div class="marktile"><div class="tile"><img src="{m["logomark"]}" style="max-height:52px" alt=""></div>'
                     '<div class="cap">logomark</div></div>')
    if marks:
        out.append('<h4 class="subhead" style="margin-top:24px">Marks</h4><div class="marks">' + "".join(marks) + "</div>")
    out.append("</div><div>")
    out.append('<h4 class="subhead">Typography — as captured</h4>')
    if m["fonts"]["specs"]:
        for sp in m["fonts"]["specs"]:
            status = "embedded from Google Fonts" if sp["embedded"] else "substituted — face not freely embeddable"
            out.append(f'<div class="typespec"><span class="ag" style="font-family:{sp["css"]}">Ag</span>'
                       f'<span class="tmeta"><b>{esc(sp["name"])}</b><br>{sp["role"]} · {sp["class"]} · {status}</span></div>')
    else:
        out.append('<p class="notcaptured">Typefaces — not captured in this dossier.</p>')
    out.append("</div></div>")

    shot = m["screenshot"]
    if shot:
        out.append(f'<div class="specimen"><img src="{shot["data"]}" alt="Homepage as captured">'
                   f'<div class="cap"><span>Field specimen — homepage, as captured</span><span>{shot["date"]}</span></div></div>')
    return "".join(out)


def _prov_rows_html(md: str) -> str | None:
    """Top-level '- **Label:** text' bullets → a quiet label/value grid; None if the shape differs."""
    items: list[str] = []
    for line in md.split("\n"):
        if re.match(r"^- ", line):
            items.append(line[2:].strip())
        elif items and line.strip():
            items[-1] += " " + line.strip()
        elif not items and line.strip():
            return None
    if not items:
        return None
    rows: list[str] = []
    for it in items:
        m2 = re.match(r"\*\*(.+?):?\*\*:?\s*(.*)", it, re.S)
        if not m2:
            return None
        label = m2.group(1).rstrip(":")
        rows.append(f'<div class="provrow"><span class="pk">{esc(label)}</span>'
                    f'<div class="pv">{md_inline(m2.group(2))}</div></div>')
    return "".join(rows)


def _provenance_html(m: dict[str, Any]) -> str:
    out = ['<section class="prov">']
    clocks = [("profile", m["captured_at"], m["age"])]
    if m["offerings"]:
        clocks.append(("offerings roster", m["offerings"]["captured_at"], m["offerings"]["age"]))
    if m["telehealth"]:
        clocks.append(("cohort pack", m["telehealth"]["captured_at"], _age_days(m["telehealth"]["captured_at"])))
    out.append('<div class="prov-clocks">')
    for label, dt, age in clocks:
        age_s = f" <small>{age}d ago</small>" if age is not None else ""
        out.append(f'<div class="clock"><span class="label">{esc(label)}</span><span class="val">{esc(dt)}{age_s}</span></div>')
    method = m["method"] or "—"
    out.append(f'<div class="clock"><span class="label">method</span><span class="val">{esc(method)} <small>schema {esc(m["schema_version"])}</small></span></div>')
    out.append("</div>")

    out.append('<div class="prov-grid"><div><h4>Capture record</h4>')
    prov_md = m["sections"].get("provenance", "")
    rows = _prov_rows_html(prov_md) if prov_md else None
    out.append(rows or (md_blocks(prov_md) if prov_md else "<p>Provenance section not captured.</p>"))
    out.append("</div><div><h4>What we couldn't verify</h4>")
    if m["unverified"]:
        out.append("<ul>" + "".join(f"<li>{md_inline(u)}</li>" for u in m["unverified"]) + "</ul>")
    else:
        out.append("<p>No unverified fields flagged on this capture.</p>")
    out.append("</div></div>")

    notes = m["site_notes"]
    if notes:
        out.append(f'<div class="fieldnotes"><h4>Field notes — read before trusting a number</h4><p>{esc(notes)}</p></div>')
    out.append("</section>")
    return "".join(out)


def _profile_panel(m: dict[str, Any]) -> str:
    # Positioning rides second and open: the brief's first external reader is a brand strategist —
    # who a company sells to and how it talks to them outranks how it monetizes.
    order = [("overview", "Overview", True),
             ("positioning & audience", "Positioning & audience", True),
             ("how it works / model", "Model & monetization", False),
             ("credibility & proof", "Proof & trust signals", False),
             ("strategic read", "Strategic read", False)]
    parts = []
    for key, title, open_ in order:
        content = m["sections"].get(key)
        if content:
            parts.append(_dsec(title, md_blocks(content), peek=_peek(content), open_=open_))
        else:
            parts.append(_dsec(title, f'<p class="notcaptured">{esc(title)} — not captured in this dossier.</p>',
                               peek="not captured in this dossier"))
    for title, content in m["extras"]:
        parts.append(_dsec(title, md_blocks(content), peek=_peek(content)))
    nav = m["sections"].get("nav structure")
    if nav:
        parts.append(_dsec("Site structure", md_blocks(nav),
                           peek="navigation tree, as serialized from the captured homepage"))
    return "".join(parts)


def _offer_panel(m: dict[str, Any]) -> str:
    if m["offerings"]:
        return _roster_html(m)
    content = m["sections"].get("what they offer")
    if content:
        note = ('<p class="notcaptured">Family-level view — a per-SKU roster has not been captured '
                "for this company.</p>")
        return md_blocks(content) + note
    return '<p class="notcaptured">What they offer — not captured in this dossier.</p>'


def render_html(m: dict[str, Any]) -> str:
    pal, fonts = m["pal"], m["fonts"]
    cls = m["classification"]
    desc = esc(m["description"]) or "—"
    # A hero headline shouldn't run 5-6 lines: step the display size down with description length.
    dlen = len(m["description"])
    desc_size = 29 if dlen <= 110 else (25 if dlen <= 170 else 21)

    css_vars = (
        f":root{{--paper:{PAPER};--ink:{INK};--desk:#DCD5C4;"
        f"--rule:color-mix(in srgb,{INK} 16%,{PAPER});"
        f"--accent:{pal['accent']};--accent-dark:{pal['accent_dark']};"
        f"--hero-bg:{pal['hero_bg']};--hero-fg:{pal['hero_fg']};--hero-accent:{pal['hero_accent']};"
        f"--display:{fonts['display']};--body:{fonts['body']};--mono:{fonts['mono']};"
        f"--grain:{GRAIN}}}"
    )

    docno = f"WR/{m['captured_at'].replace('-', '')[:8] or 'UNDATED'}/{m['slug'].upper().replace('-', '·')}"
    alias_html = ""
    others = [a for a in m["aliases"] if a.lower() != m["name"].lower()]
    if others:
        alias_html = f'<div class="alias">a.k.a. {esc(" · ".join(others))}</div>'

    # Classification is the store's corpus-cut vocabulary — deliberately generic, so it renders as
    # one quiet chip strip, not a datasheet. "Sells to" leads; the default entity (Company) is noise.
    chips: list[tuple[str, str]] = []
    if cls["market"]:
        chips.append(("sells to", " · ".join(cls["market"])))
    if cls["industry"]:
        chips.append(("industry", cls["industry"]))
    if cls["model"]:
        chips.append(("model", cls["model"]))
    if cls["category"]:
        chips.append(("offering", " · ".join(cls["category"])))
    if cls["shape"]:
        chips.append(("portfolio", cls["shape"]))
    if cls["entity"] and cls["entity"] != "Company":
        chips.append(("entity", cls["entity"]))
    specs_html = ""
    if chips:
        cuts = "".join(f'<span class="cut">{esc(lbl)} <b>{esc(val)}</b></span>' for lbl, val in chips)
        specs_html = f'<div class="cohort"><span class="label">classification</span><div class="cuts">{cuts}</div></div>'

    cohort_html = ""
    if m["telehealth"]:
        cuts = "".join(f'<span class="cut{" unclear" if v == "unclear" else ""}">{esc(k.replace("_", " "))} <b>{esc(v)}</b></span>'
                       for k, v in m["telehealth"]["cuts"].items())
        cohort_html = (f'<div class="cohort"><span class="label">telehealth cohort cuts</span>'
                       f'<div class="cuts">{cuts}</div></div>')

    offer_meta = f" · {m['offerings']['buyable']}" if m["offerings"] else ""
    tab_defs = [
        ("profile", "Profile"),
        ("offer", f"Offer architecture{offer_meta}"),
        ("brand", "Brand system"),
        ("trust", "Provenance & limits"),
    ]
    tab_inputs = "".join(
        f'<input class="tabin" type="radio" name="brieftab" id="t-{t}"{" checked" if i == 0 else ""}>'
        for i, (t, _) in enumerate(tab_defs))
    tabbar = '<nav class="tabbar">' + "".join(
        f'<label class="tabbtn" for="t-{t}" data-t="{t}"><span class="n">{i + 1:02d}</span>{esc(label)}</label>'
        for i, (t, label) in enumerate(tab_defs)) + "</nav>"

    panels = {
        "profile": _profile_panel(m),
        "offer": _offer_panel(m),
        "brand": _brand_system_html(m),
        "trust": _provenance_html(m),
    }
    panels_html = "".join(
        f'<div class="panel{" flush" if t == "trust" else ""}" data-t="{t}">'
        f'<div class="panel-label">{i + 1:02d} — {esc(label)}</div>{panels[t]}</div>'
        for i, (t, label) in enumerate(tab_defs))

    links = []
    if m["domain"]:
        links.append(f'<a href="https://{m["domain"]}">{m["domain"]}</a>')
    for k, v in list(m["socials"].items()) + list(m["external"].items()):
        if v:
            links.append(f'<a href="{esc(str(v))}">{esc(k)}</a>')

    age_s = f"{m['age']} days ago" if m["age"] is not None else "age unknown"
    entity = esc(cls["entity"] or "Company")
    eyebrow = (f'<a href="https://{esc(m["domain"])}">{esc(m["domain"])}{raw_svg("arrow-up-right")}</a> · {entity}'
               if m["domain"] else entity)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(m['name'])} — Company Brief</title>
<style>{fonts['css']}
{css_vars}
{CSS}</style></head><body>
<div class="sheet">
<div class="crop tl"></div><div class="crop tr"></div><div class="crop bl"></div><div class="crop br"></div>
<header class="masthead">
  <div class="mh-row"><span class="mh-left">Web&middot;Research — <b>Company Brief</b></span>
  <span class="mh-right">{esc(docno)}</span></div>
  <div class="rule-heavy"></div><div class="rule-thin"></div>
</header>
<section class="hero">
  <div class="hero-top">
    <span class="eyebrow">{eyebrow}</span>
    <div class="caprec"><span class="cr-label">captured</span><span class="cr-date">{esc(m['captured_at'] or 'undated')}</span>
    <span class="cr-sub">{age_s} · {esc(m['method'] or 'method unknown')} · schema {esc(m['schema_version'] or '—')}</span></div>
  </div>
  <div class="hero-mark">{_hero_mark_html(m)}</div>
  {alias_html}
  <p class="hero-desc" style="--desc-size:{desc_size}px">{desc}</p>
</section>
{specs_html}
{cohort_html}
{tab_inputs}
{tabbar}
{panels_html}
<footer class="foot"><p>Generated {esc(m['generated'])} from store/{esc(m['slug'])}/ — a regenerable lens; the dossier remains the source of truth.<br>
{' · '.join(links)}</p></footer>
</div>
<script>{JS}</script>
</body></html>"""


# ---------------------------------------------------------------- corpus index

INDEX_CSS = r"""
.ix-stats{border-bottom:1px solid var(--rule);padding:26px 0 6px;animation:rise .8s .15s both}
.ix-rows{padding:4px 0 30px;animation:rise .8s .3s both}
.ghead{display:flex;justify-content:space-between;align-items:baseline;font-family:var(--mono);
  font-size:11px;letter-spacing:.2em;text-transform:uppercase;padding:32px 0 9px;border-bottom:2px solid var(--ink)}
.ghead span:last-child{color:var(--accent)}
a.row{display:grid;grid-template-columns:26px minmax(180px,230px) 1fr auto;gap:16px;align-items:center;
  padding:11px 0;border-top:1px solid var(--rule);border-bottom:none;color:inherit}
.ghead+a.row{border-top:none}
a.row:hover{background:color-mix(in srgb,var(--ink) 4%,transparent)}
img.rmark{width:26px;height:26px;object-fit:contain}
span.rmark{width:26px;height:26px;display:grid;place-items:center;border:1px solid var(--rule);
  font-family:var(--display);font-weight:600;font-size:14px;color:var(--accent)}
.rname{font-family:var(--display);font-weight:600;font-size:16.5px;line-height:1.2}
.rdom{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.06em;font-weight:400;
  color:color-mix(in srgb,var(--ink) 52%,var(--paper));margin-top:3px}
.rdesc{font-size:13.5px;line-height:1.45;color:color-mix(in srgb,var(--ink) 72%,var(--paper));
  min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rmeta{text-align:right;font-family:var(--mono);white-space:nowrap}
.rmeta b{display:block;font-weight:400;font-size:11px;letter-spacing:.08em}
.rmeta .rlayers{display:block;font-size:9.5px;letter-spacing:.06em;margin-top:3px;color:var(--accent)}
@media (max-width:760px){a.row{grid-template-columns:24px 1fr auto}.rdesc{display:none}}
@media print{a.row{break-inside:avoid}}
"""


def render_index_html(rows: list[dict[str, Any]], fonts: dict[str, Any]) -> str:
    """The store's front door, in the engine's own dress (no company palette): a stat band that is
    recomputed every render (counts rot — never bake), then every company grouped by industry,
    each row a per-layer clock linking to its brief."""
    css_vars = (
        f":root{{--paper:{PAPER};--ink:{INK};--desk:#DCD5C4;"
        f"--rule:color-mix(in srgb,{INK} 16%,{PAPER});"
        f"--accent:#4A4438;--accent-dark:#C9BFA8;"
        f"--hero-bg:{INK};--hero-fg:{PAPER};--hero-accent:#C9BFA8;"
        f"--display:{fonts['display']};--body:{fonts['body']};--mono:{fonts['mono']};"
        f"--grain:{GRAIN}}}"
    )
    today = str(date.today())
    n_roster = sum(1 for r in rows if r["roster_at"])
    n_sku = sum(r["buyable"] or 0 for r in rows)
    n_cohort = sum(1 for r in rows if r["cohort"])
    newest = max((r["captured_at"] for r in rows if r["captured_at"]), default="—")

    groups: dict[str, list[dict[str, Any]]] = {}
    for r in rows:
        groups.setdefault(r["industry"], []).append(r)

    body: list[str] = []
    for industry, members in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        body.append(f'<div class="ghead"><span>{esc(industry)}</span><span>{len(members)}</span></div>')
        for r in sorted(members, key=lambda x: str(x["name"]).lower()):
            mark = (f'<img class="rmark" src="{r["mark"]}" alt="">' if r["mark"]
                    else f'<span class="rmark">{esc(str(r["name"])[:1])}</span>')
            layers = []
            if r["buyable"]:
                layers.append(f"{r['buyable']} SKUs")
            elif r["roster_at"]:
                layers.append("roster")
            if r["cohort"]:
                layers.append("cohort")
            age_s = f" · {r['age']}d" if r["age"] is not None else ""
            body.append(
                f'<a class="row" href="{esc(r["slug"])}.html">{mark}'
                f'<span class="rname">{esc(r["name"])}<span class="rdom">{esc(r["domain"])}</span></span>'
                f'<span class="rdesc">{esc(_truncate(r["description"], 150))}</span>'
                f'<span class="rmeta"><b>{esc(r["captured_at"] or "undated")}{age_s}</b>'
                f'<span class="rlayers">{esc(" · ".join(layers) or "profile only")}</span></span></a>')

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Web Research — Company Index</title>
<style>{fonts['css']}
{css_vars}
{CSS}
{INDEX_CSS}</style></head><body>
<div class="sheet">
<div class="crop tl"></div><div class="crop tr"></div><div class="crop bl"></div><div class="crop br"></div>
<header class="masthead">
  <div class="mh-row"><span class="mh-left">Web&middot;Research — <b>Company Index</b></span>
  <span class="mh-right">WR/{today.replace("-", "")}/INDEX</span></div>
  <div class="rule-heavy"></div><div class="rule-thin"></div>
</header>
<div class="statband ix-stats">
  <div class="stat"><div class="num">{len(rows)}</div><span class="label">companies profiled</span></div>
  <div class="stat"><div class="num">{n_roster}</div><span class="label">SKU rosters</span></div>
  <div class="stat"><div class="num">{n_sku:,}</div><span class="label">buyable SKUs enumerated</span></div>
  <div class="stat"><div class="num">{n_cohort}</div><span class="label">cohort packs</span></div>
</div>
<div class="ix-rows">{"".join(body)}</div>
<footer class="foot"><p>Generated {today} from store/ — computed at render time, nothing baked · newest capture {esc(newest)}<br>
Each row links to its brief — render them with --all so the links resolve.</p></footer>
</div>
</body></html>"""


# ---------------------------------------------------------------- CLI

def main() -> None:
    ap = argparse.ArgumentParser(description="render store/<slug>/ into self-contained HTML briefs")
    ap.add_argument("company", nargs="*", help="company name, domain, alias, or store slug")
    ap.add_argument("--all", action="store_true",
                    help="render every company in the store — pre-warms font/logo/image caches so a live demo never waits on a fetch")
    ap.add_argument("--index", action="store_true",
                    help="render the corpus index (index.html) — the store's human front door; pair with --all so row links resolve")
    ap.add_argument("--no-fetch", action="store_true", help="skip remote logo/font fetches; use local assets and fallbacks")
    args = ap.parse_args()

    queries = sorted(store_load()) if args.all else args.company
    if not queries and not args.index:
        ap.error("name at least one company, or pass --all / --index")

    os.makedirs(OUT, exist_ok=True)
    for q in queries:
        m = extract_model(q, fetch=not args.no_fetch)
        if m is None:
            print(f"{q} → not in store (try: python scripts/store.py find '{q}')")
            continue
        out_path = os.path.join(OUT, f"{m['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(render_html(m))
        size = os.path.getsize(out_path) // 1024
        print(f"{q} → {out_path}  ({size} KB)")
        # The brief is invisible unless the link lands in the agent's reply — hand over the exact
        # markdown (angle brackets: the repo path contains spaces) so no one re-derives it from prose.
        print(f"  paste into your reply: [Open {m.get('name') or m['slug']} brief](<{out_path}>)")

    if args.index:
        rows = extract_index(fetch=not args.no_fetch)
        # 00- prefix: the index sorts to the top of the briefs folder, where a human looks first.
        out_path = os.path.join(OUT, "00-index.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(render_index_html(rows, build_fonts([], fetch=not args.no_fetch)))
        print(f"index → {out_path}  ({len(rows)} companies, {os.path.getsize(out_path) // 1024} KB)")
        print(f"  paste into your reply: [Open the company index](<{out_path}>)")


if __name__ == "__main__":
    main()
