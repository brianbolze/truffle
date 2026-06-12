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
from .theme import GRAIN, INK, PAPER

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
    return (f'<span style="font-family:{m["fonts"]["display"]};font-size:{size}px;font-weight:600;'
            f'color:{m["pal"]["hero_accent"]}">{esc(m["name"])}</span>')


def _hue_key(hexcode: str) -> tuple[float, float]:
    rgb = _hex_rgb(hexcode) or (0.5, 0.5, 0.5)
    h, light, s = colorsys.rgb_to_hls(*rgb)
    return (h if s > 0.08 else 2 + light, light)  # grays sort after hues, by lightness


# ---------------------------------------------------------------- bands

def _band(no: int, title: str, sub: str, cells: list[str], n: int, extra: str = "") -> str:
    grid = "".join(f'<div class="cell">{c}</div>' for c in cells)
    return (f'<section class="band"><div class="rail"><span class="rno">{no:02d}</span>'
            f'<span class="rtitle">{esc(title)}</span><span class="rsub">{esc(sub)}</span></div>'
            f'<div class="cells" style="grid-template-columns:repeat({n},1fr)">{grid}</div>{extra}</section>')


def render_compare(models: list[dict[str, Any]]) -> str:
    n = len(models)
    today = str(date.today())

    fonts_css: list[str] = []
    scaffold = build_fonts([], fetch=False)["css"]
    fonts_css.append(scaffold)
    for m in models:  # each model's css repeats the scaffold prefix; keep only the company faces
        css = m["fonts"]["css"]
        fonts_css.append(css[len(scaffold):] if scaffold and css.startswith(scaffold) else css)

    # 01 lineup — each mark on its own captured ground
    lineup = []
    for m in models:
        pal = m["pal"]
        lineup.append(
            f'<div class="ground" style="background:{pal["hero_bg"]};color:{pal["hero_fg"]}">{_mark_html(m)}</div>'
            f'<div class="who"><b>{esc(m["name"])}</b><span>{esc(m["domain"])}</span></div>')

    # 02 voice
    voice = []
    for m in models:
        qs = harvest_voice(m["sections"], [m["name"], *m["aliases"]])
        if qs:
            voice.append("".join(
                f'<p class="q" style="font-family:{m["fonts"]["display"]};font-size:{_quote_px(q)}px">'
                f'&ldquo;{esc(q)}&rdquo;</p>' for q in qs))
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
        color.append(f'<div class="stripes">{stripes}</div><div class="hexes">{esc(labels)}</div>'
                     f'<div class="hexes">{esc(scheme)} scheme</div>')
    spectrum = "".join(f'<i style="background:{h}" title="{esc(who)} {h}"></i>'
                       for h, who in sorted(all_sw, key=lambda t: _hue_key(t[0])))
    spectrum_html = (f'<div class="spectrum"><span class="label">cohort spectrum — every captured color, by hue</span>'
                     f'<div class="stripes">{spectrum}</div></div>')

    # 04 type
    typo = []
    for m in models:
        specs = m["fonts"]["specs"]
        if specs:
            typo.append("".join(
                f'<div class="face"><span class="ag" style="font-family:{sp["css"]}">Ag</span>'
                f'<span class="fmeta"><b>{esc(sp["name"])}</b>{sp["role"]} · {sp["class"]}'
                f'{"" if sp["embedded"] else " · substituted"}</span></div>' for sp in specs[:2]))
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
            seg = "".join(
                f'<i class="seg-{k}" style="flex:{v}" title="{v} {k}"></i>'
                for k, v in (("published", pc["published"]), ("partial", pc["partial"]),
                             ("on-request", pc["on-request"])) if v)
            leg = " / ".join(f"{v} {k}" for k, v in pc.most_common())
            count = f"≥{off['buyable']}" if off["enumeration"] == "lines-omitted" else str(off["buyable"])
            offer.append(f'<div class="vitals">{esc(vitals)}</div>'
                         f'<div class="big">{count}<small> SKUs · {off["families"]} lines</small></div>'
                         f'<div class="bar">{seg}</div><div class="leg">{esc(leg) or "no visibility tokens"}</div>')
        else:
            offer.append(f'<div class="vitals">{esc(vitals)}</div>'
                         '<p class="none">family-level capture — no per-SKU roster</p>')

    # 07 field specimens
    spec = []
    for m in models:
        s = m["screenshot"]
        spec.append(f'<div class="shot"><img src="{s["data"]}" alt="{esc(m["name"])} homepage, as captured">'
                    f'<span class="cap">{esc(s["date"])}</span></div>' if s
                    else '<p class="none">no specimen captured</p>')

    # 08 provenance (dark)
    prov = []
    for m in models:
        age = f"{m['age']}d ago" if m["age"] is not None else "age unknown"
        prov.append(f'<b>{esc(m["captured_at"] or "undated")}</b><span>{age} · {esc(m["method"] or "—")}</span>'
                    f'<a href="{esc(m["slug"])}.html">full brief →</a>')
    prov_cells = "".join(f'<div class="cell">{c}</div>' for c in prov)

    names = " · ".join(m["name"] for m in models)
    docno = f"WR/{today.replace('-', '')}/COMPARE·{n}"
    accents = "".join(
        f'.cells .cell:nth-child({i + 1})::before{{background:{m["pal"]["accent"]}}}' for i, m in enumerate(models))

    css = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--paper:{PAPER};--ink:{INK};--desk:#DCD5C4;--rule:color-mix(in srgb,{INK} 16%,{PAPER});
  --mono:'Fragment Mono',ui-monospace,'SF Mono',Menlo,monospace;
  --body:'Newsreader','Iowan Old Style',Palatino,Georgia,serif;--grain:{GRAIN}}}
body{{background:var(--desk);font-family:var(--body);color:var(--ink);-webkit-font-smoothing:antialiased}}
.sheet{{position:relative;max-width:{min(1680, 230 + 300 * n)}px;margin:44px auto;padding:0 56px 8px;background:var(--paper);
  box-shadow:0 30px 80px rgba(20,16,8,.28),0 2px 10px rgba(20,16,8,.14)}}
.sheet::before{{content:"";position:absolute;inset:0;pointer-events:none;opacity:.5;
  background-image:var(--grain);background-size:300px 300px}}
.label{{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;
  color:color-mix(in srgb,var(--ink) 62%,var(--paper))}}
.masthead{{padding:46px 0 0}}
.mh-row{{display:flex;justify-content:space-between;align-items:baseline;padding-bottom:10px;
  font-family:var(--mono);font-size:11.5px;letter-spacing:.22em;text-transform:uppercase}}
.mh-row .right{{font-size:10.5px;letter-spacing:.14em;color:color-mix(in srgb,var(--ink) 55%,var(--paper))}}
.rule-heavy{{height:3px;background:var(--ink)}}.rule-thin{{height:1px;background:var(--rule);margin-top:2px}}
.title{{padding:30px 0 26px;border-bottom:1px solid var(--rule)}}
.title h1{{font-size:31px;font-weight:400;font-style:italic;line-height:1.25;max-width:30ch}}
.title .sub{{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;
  margin-top:12px;color:color-mix(in srgb,var(--ink) 55%,var(--paper))}}

.band{{display:grid;grid-template-columns:108px 1fr;gap:0 26px;border-bottom:1px solid var(--ink);padding:26px 0 30px}}
.band:last-of-type{{border-bottom:none}}
.rail{{display:flex;flex-direction:column;gap:7px;border-right:1px solid var(--rule);padding:4px 14px 0 0}}
.rail .rno{{font-family:var(--mono);font-size:11px;color:color-mix(in srgb,var(--ink) 45%,var(--paper))}}
.rail .rtitle{{font-family:var(--mono);font-size:12px;letter-spacing:.18em;text-transform:uppercase}}
.rail .rsub{{font-size:12.5px;font-style:italic;line-height:1.45;color:color-mix(in srgb,var(--ink) 55%,var(--paper))}}
.cells{{display:grid;gap:0 22px}}
.cells .cell{{position:relative;padding-top:12px;min-width:0}}
.cells .cell::before{{content:"";position:absolute;top:0;left:0;width:30px;height:3px}}
{accents}

.ground{{display:flex;align-items:center;justify-content:center;height:108px;padding:16px;
  border:1px solid rgba(0,0,0,.14)}}
.plate{{display:inline-flex;background:var(--paper);padding:9px 14px}}
.who{{display:flex;justify-content:space-between;align-items:baseline;gap:8px;margin-top:9px}}
.who b{{font-size:15px;font-weight:600}}
.who span{{font-family:var(--mono);font-size:10px;letter-spacing:.06em;color:color-mix(in srgb,var(--ink) 55%,var(--paper))}}

.q{{line-height:1.34;margin-bottom:12px;overflow-wrap:break-word}}
.q.fallback{{font-style:italic;font-size:15px;color:color-mix(in srgb,var(--ink) 70%,var(--paper))}}

.stripes{{display:flex;height:46px;border:1px solid var(--rule)}}
.stripes i{{flex:1}}
.hexes{{font-family:var(--mono);font-size:9.5px;letter-spacing:.05em;margin-top:6px;
  color:color-mix(in srgb,var(--ink) 58%,var(--paper))}}
.spectrum{{grid-column:1/-1;margin-top:22px;padding-top:14px;border-top:1px dashed var(--rule)}}
.spectrum .label{{display:block;margin-bottom:8px}}
.spectrum .stripes{{height:16px}}

.face{{display:flex;gap:12px;align-items:center;border:1px solid var(--rule);padding:9px 12px;margin-bottom:8px}}
.face .ag{{font-size:30px;line-height:1;min-width:42px}}
.face .fmeta{{font-family:var(--mono);font-size:10px;letter-spacing:.06em;line-height:1.55;
  color:color-mix(in srgb,var(--ink) 60%,var(--paper))}}
.face .fmeta b{{display:block;color:var(--ink);font-weight:400;font-size:11.5px}}

.chips b{{display:inline-block;font-family:var(--mono);font-weight:400;font-size:10.5px;letter-spacing:.08em;
  border:1px solid var(--rule);padding:3px 9px;margin:0 6px 6px 0}}
.line{{font-size:13.5px;font-style:italic;line-height:1.5;color:color-mix(in srgb,var(--ink) 72%,var(--paper))}}

.vitals{{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:10px;
  color:color-mix(in srgb,var(--ink) 55%,var(--paper))}}
.big{{font-size:38px;font-weight:600;line-height:1}}
.big small{{font-size:11px;font-weight:400;font-family:var(--mono);letter-spacing:.06em;
  color:color-mix(in srgb,var(--ink) 55%,var(--paper))}}
.bar{{display:flex;height:13px;margin:12px 0 7px;border:1px solid var(--ink)}}
.seg-published{{background:var(--ink)}}
.seg-partial{{background:color-mix(in srgb,var(--ink) 38%,var(--paper))}}
.seg-on-request{{background:repeating-linear-gradient(45deg,transparent,transparent 3px,
  color-mix(in srgb,var(--ink) 38%,var(--paper)) 3px,color-mix(in srgb,var(--ink) 38%,var(--paper)) 4px)}}
.leg{{font-family:var(--mono);font-size:9.5px;letter-spacing:.05em;color:color-mix(in srgb,var(--ink) 58%,var(--paper))}}

.shot{{border:1px solid var(--rule)}}
.shot img{{display:block;width:100%;height:300px;object-fit:cover;object-position:top;
  -webkit-mask-image:linear-gradient(to bottom,#000 82%,transparent);mask-image:linear-gradient(to bottom,#000 82%,transparent)}}
.shot .cap{{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;padding:6px 9px;
  border-top:1px solid var(--rule);color:color-mix(in srgb,var(--ink) 55%,var(--paper))}}
.none{{font-family:var(--mono);font-size:11px;letter-spacing:.06em;color:color-mix(in srgb,var(--ink) 48%,var(--paper))}}

.prov{{margin:0 -56px;padding:34px 56px 30px;background:var(--ink);color:color-mix(in srgb,var(--paper) 88%,var(--ink))}}
.prov .grid{{display:grid;gap:0 22px;grid-template-columns:108px repeat({n},1fr)}}
.prov .cell{{display:flex;flex-direction:column;gap:4px;font-family:var(--mono);font-size:10.5px;letter-spacing:.05em}}
.prov b{{font-weight:400;font-size:13px;letter-spacing:.08em;color:var(--paper)}}
.prov span{{color:color-mix(in srgb,var(--paper) 55%,transparent)}}
.prov a{{color:color-mix(in srgb,var(--paper) 80%,transparent);text-decoration:none;
  border-bottom:1px solid color-mix(in srgb,var(--paper) 30%,transparent);width:fit-content;margin-top:3px}}
.prov .plabel{{font-family:var(--mono);font-size:10px;letter-spacing:.18em;text-transform:uppercase;
  color:color-mix(in srgb,var(--paper) 48%,transparent)}}
.foot{{padding:24px 0 34px;text-align:center;font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;
  text-transform:uppercase;color:color-mix(in srgb,var(--ink) 48%,var(--paper));line-height:2}}

@media (max-width:900px){{
  .sheet{{margin:0;padding:0 18px 8px}}
  .band{{grid-template-columns:1fr}}
  .rail{{flex-direction:row;align-items:baseline;border-right:none;border-bottom:1px solid var(--rule);
    padding:0 0 8px;margin-bottom:14px}}
  .cells{{overflow-x:auto;grid-auto-columns:minmax(200px,1fr)}}
  .prov{{margin:0 -18px;padding:26px 18px}}
  .prov .grid{{grid-template-columns:repeat({n},minmax(150px,1fr));overflow-x:auto}}
}}
@media print{{
  body{{background:#fff}}.sheet{{box-shadow:none;margin:0;max-width:none}}
  .band,.shot,.face{{break-inside:avoid}}
  .ground,.prov,.stripes{{print-color-adjust:exact;-webkit-print-color-adjust:exact}}
}}
"""

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
{css}</style></head><body>
<div class="sheet">
<header class="masthead">
  <div class="mh-row"><span>Web&middot;Research — <b style="font-weight:400">Comparison Sheet</b></span>
  <span class="right">{esc(docno)}</span></div>
  <div class="rule-heavy"></div><div class="rule-thin"></div>
</header>
<div class="title"><h1>{esc(names)}</h1>
<div class="sub">{n} companies · one lens · captured {esc(caps)}</div></div>
{"".join(bands)}
<section class="prov"><div class="grid"><div class="cell"><span class="plabel">captured</span></div>{prov_cells}</div></section>
<footer class="foot">Generated {esc(today)} · captured states, not live sites — the dossiers remain the source of truth<br>
prices are never normalized across companies; posture (published / partial / on-request) is the only money lens here</footer>
</div>
</body></html>"""
