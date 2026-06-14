"""model — the read side of the lens: store records in, plain dicts out. No HTML here.

Why separate: extraction is "reading the agent surface," rendering is "speaking human" —
the store↔artifact translation boundary lives in exactly this one place, so every view
(brief / comparison sheet / index) describes a company from the same dicts.
"""

from __future__ import annotations

import glob
import os
import re
from datetime import date
from typing import Any

from offeringscheck import SPINE_PREFIXES, parse_roster

from store import STORE
from store import load as store_load
from store import read_doc as store_read_doc
from store import resolve as store_resolve

from .assets import IMGCACHE, _b64_file, _fetch, build_fonts, load_logo, load_logomark, load_screenshot, palette

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


def extract_visual(slug: str) -> dict[str, Any] | None:
    """The blind visual-evidence layer's brief-facing read: the cited prose impression (card-id
    citations stripped for the reader — the cards stay in visual.md as the audit trail) + its own
    freshness clock. None when no visual.md exists. The brief prefers this over profile.md's body
    section: same slot, but blind and evidence-backed."""
    path = os.path.join(STORE, slug, "visual.md")
    if not os.path.exists(path):
        return None
    fm, body = store_read_doc(path)
    impression = _split_sections(body).get("visual & brand impression", "").strip()
    impression = re.sub(r"\s*\[[a-z0-9_]+\]", "", impression)
    return {
        "captured_at": _datestr(fm.get("captured_at")),
        "age": _age_days(fm.get("captured_at")),
        "qa_status": str(fm.get("qa_status") or ""),
        "impression": impression,
    }


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
        "visual": extract_visual(slug),
        "generated": str(date.today()),
    }
