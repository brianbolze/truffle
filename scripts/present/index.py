"""index — the corpus front door: every profiled company, grouped and clocked, each row
linking to its brief.

Browsing, not operations: coverage/staleness triage is a different tool (store.py health).
Everything here is computed at render time — counts rot, so nothing is baked.
"""

from __future__ import annotations

from datetime import date
from typing import Any

from .md import _truncate, esc
from .theme import INK, PAPER, css


def render_index_html(rows: list[dict[str, Any]], fonts: dict[str, Any]) -> str:
    """The store's front door, in the engine's own dress (no company palette): a stat band that is
    recomputed every render (counts rot — never bake), then every company grouped by industry,
    each row a per-layer clock linking to its brief."""
    css_vars = (
        f":root{{--paper:{PAPER};--ink:{INK};"
        f"--rule:color-mix(in srgb,{INK} 16%,{PAPER});"
        f"--accent:#4A4438;--accent-dark:#C9BFA8;"
        f"--hero-bg:{INK};--hero-fg:{PAPER};--hero-accent:#C9BFA8;"
        f"--display:{fonts['display']};--body:{fonts['body']};--mono:{fonts['mono']}}}"
    )
    base_css, view_css = css("base") + css("brief"), css("index")
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
{base_css}
{view_css}</style></head><body>
<div class="sheet">
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
