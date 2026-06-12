"""brief — the single-company view: one dossier → one self-contained HTML brief.

Dressed in the company's own captured identity (wordmark, brand_colors, fonts), with the
engine's trust surface (capture clocks, unverified fields, enumeration floors) rendered
visibly as the product. Four tabs (Profile / Offer architecture / Brand system /
Provenance & limits), CSS-only so the file survives iOS Quick Look after an AirDrop.
"""

from __future__ import annotations

import re
from typing import Any

from .md import _peek, _truncate, esc, md_blocks, md_inline
from .model import _age_days
from .theme import ARROW_SVG, INK, PAPER, css

# Tabs are CSS-only (radio + :checked) so they work with JS disabled — e.g. iOS Quick Look on
# an AirDropped file. The only JS is a progressive enhancement: expand every <details> before
# printing so a printed brief is complete. No-JS viewers simply print whatever's open.
JS = "window.addEventListener('beforeprint',()=>document.querySelectorAll('details').forEach(d=>d.open=true));"


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
    sheet_css = css("base") + css("brief")
    cls = m["classification"]
    desc = esc(m["description"]) or "—"
    # A hero headline shouldn't run 5-6 lines: step the display size down with description length.
    dlen = len(m["description"])
    desc_size = 29 if dlen <= 110 else (25 if dlen <= 170 else 21)

    css_vars = (
        f":root{{--paper:{PAPER};--ink:{INK};"
        f"--rule:color-mix(in srgb,{INK} 16%,{PAPER});"
        f"--accent:{pal['accent']};--accent-dark:{pal['accent_dark']};"
        f"--hero-bg:{pal['hero_bg']};--hero-fg:{pal['hero_fg']};--hero-accent:{pal['hero_accent']};"
        f"--display:{fonts['display']};--body:{fonts['body']};--mono:{fonts['mono']}}}"
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
    eyebrow = (f'<a href="https://{esc(m["domain"])}">{esc(m["domain"])}{ARROW_SVG}</a> · {entity}'
               if m["domain"] else entity)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(m['name'])} — Company Brief</title>
<style>{fonts['css']}
{css_vars}
{sheet_css}</style></head><body>
<div class="sheet">
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
