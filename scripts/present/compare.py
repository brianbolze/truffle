"""compare — the N-company view: one specimen sheet, side by side.

The brief answers "tell me about X"; this answers the brand-strategist's real question —
"show me X against its category" — in horizontal lens bands (lineup, voice, color, type,
audience, offer posture, field specimens), one column per company. It never normalizes
prices across companies (the judgment that once parked this view): money renders only as
price-visibility posture, a closed set. All language is verbatim from the dossiers.
"""

from __future__ import annotations

import colorsys
import re
from collections import Counter
from datetime import date
from typing import Any

from .assets import _hex_rgb, build_fonts
from .md import _peek, _truncate, esc
from .theme import INK, PAPER, css

# ---------------------------------------------------------------- voice harvest

VOICE_SECTIONS = ("overview", "positioning & audience", "strategic read")


def harvest_voice(sections: dict[str, str], names: list[str]) -> list[str]:
    """Verbatim site language, exactly as the dossier quoted it — the sheet never paraphrases.

    Dossier prose quotes the company's own words in "double quotes"; this lifts the first two
    spans that read as brand voice (a tagline, a claim) rather than harvest residue (slugs,
    leading fragments, years, the company's own name/aliases in quotes).
    """
    text = "\n".join(sections.get(k, "") for k in VOICE_SECTIONS)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    self_names = {x.lower() for x in names if x}
    out: list[str] = []
    for m in re.finditer(r'"([^"\n]{6,160})"|“([^”\n]{6,160})”', text):
        q = re.sub(r"[*_`]", "", (m.group(1) or m.group(2))).strip(" .,;:—-")
        words = q.split()
        if len(words) < 2 or len(q) > 120:
            continue
        if re.search(r"https?://|\.com|\d{4}", q):
            continue
        if q[0].islower() and len(words) < 4:  # mid-sentence fragment, not a line
            continue
        if q.lower() in self_names or any(q.lower() in s for s in self_names):
            continue
        if q not in out:
            out.append(q)
        if len(out) == 2:
            break
    return out


def _quote_px(q: str) -> int:
    n = len(q)
    return 27 if n <= 30 else (22 if n <= 60 else (18 if n <= 100 else 16))


# ---------------------------------------------------------------- per-company cells


def _posture(off: dict[str, Any] | None) -> Counter:
    c: Counter = Counter()
    if off:
        for g in off["groups"]:
            for s in g["skus"]:
                v = re.sub(r"[`*]", "", s["vis"]).strip()
                if v in ("published", "partial", "on-request"):
                    c[v] += 1
    return c


_FAMILY_TOKEN = re.compile(r"\[(published|partial|on-request)\]")


def _family_posture(section: str) -> Counter:
    """Price-visibility at family grain, for companies with no per-SKU roster.

    SCHEMA's visibility token is universal on profile offer lines, so the sheet can
    still show *how openly priced* a company is — it just can't claim roster size.
    """
    return Counter(m.group(1) for m in _FAMILY_TOKEN.finditer(section))


def _posture_bar(pc: Counter) -> tuple[str, str]:
    """The stacked visibility bar + its legend — shared by roster and family grain."""
    seg = "".join(
        f'<i class="seg-{k}" style="flex:{v}" title="{v} {k}"></i>'
        for k, v in (("published", pc["published"]), ("partial", pc["partial"]), ("on-request", pc["on-request"]))
        if v
    )
    leg = " / ".join(f"{v} {k}" for k, v in pc.most_common())
    return seg, leg


def _mark_html(m: dict[str, Any]) -> str:
    """The company's wordmark sized for a lineup tile; typographic fallback in its display face."""
    logo = m["logo"]
    if logo["kind"] in ("svg", "img"):
        aspect = logo.get("aspect") or 4.0
        height = max(24, min(52, int(230 / max(aspect, 0.8))))
        if logo["kind"] == "svg":
            inner = re.sub(r"<svg ", f'<svg style="height:{height}px;width:auto;max-width:100%" ', logo["svg"], count=1)
        else:
            inner = f'<img src="{logo["data"]}" style="height:{height}px;width:auto;max-width:100%" alt="{esc(m["name"])}">'
        return f'<span class="plate">{inner}</span>' if logo["plate"] else inner
    size = 26 if len(m["name"]) <= 14 else 19
    return (
        f'<span style="font-family:{m["fonts"]["display"]};font-size:{size}px;font-weight:600;'
        f'color:{m["pal"]["hero_accent"]}">{esc(m["name"])}</span>'
    )


def _hue_key(hexcode: str) -> tuple[float, float]:
    rgb = _hex_rgb(hexcode) or (0.5, 0.5, 0.5)
    h, light, s = colorsys.rgb_to_hls(*rgb)
    return (h if s > 0.08 else 2 + light, light)  # grays sort after hues, by lightness


# ---------------------------------------------------------------- bands


def _band(no: int, title: str, sub: str, cells: list[str], n: int, extra: str = "") -> str:
    grid = "".join(f'<div class="cell">{c}</div>' for c in cells)
    return (
        f'<section class="band"><div class="rail"><span class="rno">{no:02d}</span>'
        f'<span class="rtitle">{esc(title)}</span><span class="rsub">{esc(sub)}</span></div>'
        f'<div class="cells" style="grid-template-columns:repeat({n},1fr)">{grid}</div>{extra}</section>'
    )


def render_compare(models: list[dict[str, Any]]) -> str:
    n = len(models)
    today = str(date.today())

    fonts_css: list[str] = []
    scaffold = build_fonts([], fetch=False)["css"]
    fonts_css.append(scaffold)
    for m in models:  # each model's css repeats the scaffold prefix; keep only the company faces
        fcss = m["fonts"]["css"]
        fonts_css.append(fcss[len(scaffold) :] if scaffold and fcss.startswith(scaffold) else fcss)

    # 01 lineup — each mark on its own captured ground
    lineup = []
    for m in models:
        pal = m["pal"]
        lineup.append(
            f'<a class="linkcell" href="{esc(m["slug"])}.html">'
            f'<div class="ground" style="background:{pal["hero_bg"]};color:{pal["hero_fg"]}">{_mark_html(m)}</div>'
            f'<div class="who"><b>{esc(m["name"])}</b><span>{esc(m["domain"])}</span></div></a>'
        )

    # 02 voice
    voice = []
    for m in models:
        qs = harvest_voice(m["sections"], [m["name"], *m["aliases"]])
        if qs:
            voice.append(
                "".join(
                    f'<p class="q" style="font-family:{m["fonts"]["display"]};font-size:{_quote_px(q)}px">&ldquo;{esc(q)}&rdquo;</p>'
                    for q in qs
                )
            )
        else:
            voice.append(f'<p class="q fallback">{esc(_truncate(m["description"], 110))}</p>')

    # 03 color — per-company stripes + one cohort spectrum
    color = []
    all_sw: list[tuple[str, str]] = []
    for m in models:
        sw = m["pal"]["swatches"]
        all_sw += [(s["hex"], m["name"]) for s in sw]
        stripes = "".join(f'<i style="background:{s["hex"]}" title="{esc(s["key"])} {s["hex"]}"></i>' for s in sw)
        labels = " · ".join(s["hex"] for s in sw)
        scheme = m["pal"]["scheme"] or "—"
        color.append(
            f'<div class="stripes">{stripes}</div><div class="hexes">{esc(labels)}</div><div class="hexes">{esc(scheme)} scheme</div>'
        )
    spectrum = "".join(f'<i style="background:{h}" title="{esc(who)} {h}"></i>' for h, who in sorted(all_sw, key=lambda t: _hue_key(t[0])))
    spectrum_html = (
        f'<div class="spectrum"><span class="label">cohort spectrum — every captured color, by hue</span>'
        f'<div class="stripes">{spectrum}</div></div>'
    )

    # 04 type
    typo = []
    for m in models:
        specs = m["fonts"]["specs"]
        if specs:
            typo.append(
                "".join(
                    f'<div class="face"><span class="ag" style="font-family:{sp["css"]}">Ag</span>'
                    f'<span class="fmeta"><b>{esc(sp["name"])}</b>{sp["role"]} · {sp["class"]}'
                    f"{'' if sp['embedded'] else ' · substituted'}</span></div>"
                    for sp in specs[:2]
                )
            )
        else:
            typo.append('<p class="none">typefaces not captured</p>')

    # 05 audience
    aud = []
    for m in models:
        cls = m["classification"]
        chips = "".join(f"<b>{esc(t)}</b>" for t in cls["market"]) or "<b>—</b>"
        line = _peek(m["sections"].get("positioning & audience", ""), 150)
        aud.append(f'<div class="chips">{chips}</div><p class="line">{line or "—"}</p>')

    # 06 offer posture
    offer = []
    for m in models:
        cls = m["classification"]
        vitals = " · ".join(x for x in (cls["model"], cls["shape"]) if x)
        off = m["offerings"]
        if off:
            pc = _posture(off)
            seg, leg = _posture_bar(pc)
            count = f"≥{off['buyable']}" if off["enumeration"] == "lines-omitted" else str(off["buyable"])
            offer.append(
                f'<div class="vitals">{esc(vitals)}</div>'
                f'<div class="big">{count}<small> SKUs · {off["families"]} lines</small></div>'
                f'<div class="bar">{seg}</div><div class="leg">{esc(leg) or "no visibility tokens"}</div>'
            )
        elif fp := _family_posture(m["sections"].get("what they offer", "")):
            seg, leg = _posture_bar(fp)
            offer.append(
                f'<div class="vitals">{esc(vitals)}</div>'
                f'<div class="big">{sum(fp.values())}<small> offer lines · family grain</small></div>'
                f'<div class="bar">{seg}</div><div class="leg">{esc(leg)} · no per-SKU roster</div>'
            )
        else:
            offer.append(f'<div class="vitals">{esc(vitals)}</div><p class="none">family-level capture — no per-SKU roster</p>')

    # 07 field specimens
    spec = []
    for m in models:
        s = m["screenshot"]
        spec.append(
            f'<div class="shot"><img src="{s["data"]}" alt="{esc(m["name"])} homepage, as captured">'
            f'<span class="cap">{esc(s["date"])}</span></div>'
            if s
            else '<p class="none">no specimen captured</p>'
        )

    # 08 provenance (dark)
    prov = []
    for m in models:
        age = f"{m['age']}d ago" if m["age"] is not None else "age unknown"
        prov.append(
            f"<b>{esc(m['captured_at'] or 'undated')}</b><span>{age} · {esc(m['method'] or '—')}</span>"
            f'<a href="{esc(m["slug"])}.html">full brief →</a>'
        )
    prov_cells = "".join(f'<div class="cell">{c}</div>' for c in prov)

    names = " · ".join(m["name"] for m in models)
    names_linked = " · ".join(f'<a href="{esc(m["slug"])}.html">{esc(m["name"])}</a>' for m in models)
    docno = f"WR/{today.replace('-', '')}/COMPARE·{n}"
    accents = "".join(f".cells .cell:nth-child({i + 1})::before{{background:{m['pal']['accent']}}}" for i, m in enumerate(models))

    css_vars = (
        f":root{{--paper:{PAPER};--ink:{INK};"
        f"--rule:color-mix(in srgb,{INK} 16%,{PAPER});"
        "--mono:'DM Mono',ui-monospace,'SF Mono',Menlo,monospace;"
        "--body:'Source Serif 4','Iowan Old Style',Palatino,Georgia,serif}}"
    )
    # The sheet's width, the per-column accent ticks, and the provenance grid all depend on N —
    # they're the only style computed here; everything static is css/compare.css.
    dyn_css = (
        f".sheet{{{{max-width:{min(1680, 230 + 300 * n)}px}}}}\n{accents}\n"
        f".prov .grid{{{{grid-template-columns:108px repeat({n},1fr)}}}}\n"
        f"@media (max-width:900px){{{{.prov .grid{{{{grid-template-columns:repeat({n},minmax(150px,1fr));overflow-x:auto}}}}}}}}"
    )
    sheet_css = css("base") + css("compare")

    bands = [
        _band(1, "Lineup", "each mark on its own captured ground", lineup, n),
        _band(2, "Voice", "the company's own words, verbatim", voice, n),
        _band(3, "Color", "palette as captured", color, n, extra=spectrum_html),
        _band(4, "Type", "faces as captured", typo, n),
        _band(5, "Audience", "who they sell to", aud, n),
        _band(6, "Offer posture", "roster size + how openly priced", offer, n),
        _band(7, "Field specimens", "homepages as captured", spec, n),
    ]
    caps = " — ".join(sorted({m["captured_at"] for m in models if m["captured_at"]}))
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(names)} — Comparison Sheet</title>
<style>{"".join(fonts_css)}
{css_vars}
{sheet_css}
{dyn_css}</style></head><body>
<div class="sheet">
<header class="masthead">
  <div class="mh-row"><span class="mh-left"><a class="home" href="00-index.html">Web&middot;Research</a> — <b>Comparison Sheet</b></span>
  <span class="mh-right">{esc(docno)}</span></div>
  <div class="rule-heavy"></div><div class="rule-thin"></div>
</header>
<div class="title"><h1>{names_linked}</h1>
<div class="sub">{n} companies · one lens · captured {esc(caps)}</div></div>
{"".join(bands)}
<section class="prov"><div class="grid"><div class="cell"><span class="plabel">captured</span></div>{prov_cells}</div></section>
<footer class="foot">Generated {esc(today)} · captured states, not live sites — the dossiers remain the source of truth<br>
prices are never normalized across companies; posture (published / partial / on-request) is the only money lens here</footer>
</div>
</body></html>"""
