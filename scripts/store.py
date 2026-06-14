#!/usr/bin/env python3
"""store — the consume-side query primitives that are error-prone to do by hand.

QUERYING.md already gives every *easy* read as a one-line YAML filter (count, group-by, recent). This
module exists only for the reads an agent gets subtly wrong by eye, so they're worth committing once:

  resolve(query)  — fold any surface form (domain / name / alias / store-slug) to the one canonical key.
                    "domain is the key" only holds if a single function maps every form to it — canon().
  relations()     — which parent/owns targets actually resolve to a held profile, which dangle (a
                    re-capture candidate, ranked by in-degree), which are name-only (un-joinable by design).

A *derived lens*, never authoritative: the markdown store is the source of truth. Loads frontmatter fresh
(no cache, no index — the whole corpus is ~100KB; see experiments/2026-06-01-coded-queries). Stdlib + PyYAML.

CLI:  python store.py find <query> [<query> ...]   ·   python store.py relations   ·   python store.py health
Lib:  from store import load, canon, resolve, relations
"""

from __future__ import annotations

import glob
import os
import re
import sys
from collections import Counter
from datetime import date
from typing import Any, Callable

try:
    import yaml
except ImportError:
    sys.exit("PyYAML not importable — the resolver needs it to parse frontmatter.")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, "store")

# Hand-maintained mirror of SCHEMA's minor-additive (no backfill, grandfathered) fields.
# display-name → schema_version at which the field/convention was added.
# On a MINOR bump that adds a no-backfill field: append here AND add "append to FIELD_VERSIONS" to
# the SCHEMA version-history line. querycheck --strict asserts this covers every such version SCHEMA names.
FIELD_VERSIONS: dict[str, str] = {
    "price-visibility": "2.3",
    "logos": "2.5",
    "legal_entity": "2.6",
}


def read_doc(path: str) -> tuple[dict[str, Any], str]:
    """Read a store markdown file as (frontmatter, body)."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        return yaml.safe_load(fm) or {}, body
    return {}, text


def _frontmatter(path: str) -> dict[str, Any]:
    return read_doc(path)[0]


def load() -> dict[str, dict[str, Any]]:
    """{slug: frontmatter-dict}. slug is the dir name — the actual store key, not the `domain` field."""
    return {os.path.basename(os.path.dirname(p)): _frontmatter(p) for p in sorted(glob.glob(os.path.join(STORE, "*", "profile.md")))}


def canon(s: str) -> str:
    """The store's join key: fold a domain / store-slug / alias to one comparable token.

    Lowercase, strip scheme + `www.`, dots→dashes — so `honehealth.com`, `HoneHealth.com`, and the dir
    `honehealth-com` all collapse to `honehealth-com`. SCHEMA stores relations as dotted domains; the dirs
    are dashed; canon() is the documented rule that bridges them, so a JOIN never breaks on form alone.
    """
    s = str(s).strip().lower()
    s = re.sub(r"^https?://", "", s).rstrip("/")
    s = re.sub(r"^www\.", "", s)
    return s.replace(".", "-")


def _is_domainish(s: str) -> bool:
    """A relation/alias target is either a resolvable domain or a quoted name — which is this?

    Domain markers: a dotted TLD (`converse.com`) or the dashed slug-form (`gshock-casio-com`). Anything
    else (`Jordan Brand`, `Hims & Hers Health, Inc.`) is a name, un-joinable by design.
    """
    s = str(s).strip().lower()
    return bool(re.search(r"\.[a-z]{2,}$", s)) or bool(re.match(r"^[a-z0-9-]+-(com|ai|io|net|org|co|so)$", s))


def index(profiles: dict[str, dict[str, Any]]) -> dict[str, str]:
    """canon-key → slug, over slug + `domain` + every alias (domain- and name-form). The resolver's table.

    Aliases are the M&A / rebrand escape hatch (SCHEMA), so a merged entity's old domain resolves to the
    survivor: `salesloft.com → clari-com`. That's intended — query the acquired co, get who it's now part of.
    """
    idx: dict[str, str] = {}
    for slug, fm in profiles.items():
        keys = {canon(slug), canon(fm.get("domain") or slug)}
        for a in fm.get("aliases") or []:
            keys.add(canon(a) if _is_domainish(a) else str(a).strip().lower())
        for k in keys:
            idx.setdefault(k, slug)
    return idx


def resolve(query: str, profiles: dict[str, dict[str, Any]] | None = None) -> str | None:
    """Any surface form → canonical slug, or None. Exact match on canon(slug/domain/domainish-alias) or a
    lowercased name-alias, then on `name`. (The CLI adds a fuzzy candidate fallback; the library stays exact.)
    """
    profiles = load() if profiles is None else profiles
    idx = index(profiles)
    hit = idx.get(canon(query)) or idx.get(str(query).strip().lower())
    if hit:
        return hit
    for slug, fm in profiles.items():
        if str(query).strip().lower() == str(fm.get("name") or "").lower():
            return slug
    return None


def relations(profiles: dict[str, dict[str, Any]] | None = None) -> dict[str, Any]:
    """Classify every parent/owns target. Returns {joinable, dangling, named, dangling_indegree}.

    joinable: (slug, field, target, resolved_slug) — points at a held profile.
    dangling: (slug, field, target) — domain-shaped but no profile yet; dangling_indegree ranks re-captures.
    named:    (slug, field, target) — a quoted name, un-joinable by design."""
    profiles = load() if profiles is None else profiles
    idx = index(profiles)
    joinable, dangling, named = [], [], []
    indeg: Counter[str] = Counter()
    for slug, fm in profiles.items():
        for field in ("parent", "owns"):
            for t in fm.get(field) or []:
                if not _is_domainish(t):
                    named.append((slug, field, t))
                elif canon(t) in idx:
                    joinable.append((slug, field, t, idx[canon(t)]))
                else:
                    dangling.append((slug, field, t))
                    indeg[canon(t)] += 1
    return {
        "joinable": joinable,
        "dangling": dangling,
        "named": named,
        "dangling_indegree": indeg,
    }


# --- trust surface helpers -----------------------------------------------------------------------


def _ver_tuple(v: object) -> tuple[int, int] | None:
    m = re.fullmatch(r"\s*(\d+)(?:\.(\d+))?\s*", str(v))
    return (int(m.group(1)), int(m.group(2) or 0)) if m else None


def _days_ago(date_val: object) -> int | None:
    try:
        d = date.fromisoformat(str(date_val))
        return (date.today() - d).days
    except (TypeError, ValueError):
        return None


def _stub_capture_date(slug: str) -> str | None:
    """Latest date-named subdir under captures/, or None."""
    caps = os.path.join(STORE, slug, "captures")
    if not os.path.isdir(caps):
        return None
    entries = sorted(e for e in os.listdir(caps) if re.match(r"\d{4}-\d{2}-\d{2}", e))
    return entries[-1] if entries else None


def _predates(schema_ver: object) -> list[str]:
    """FIELD_VERSIONS names that predate the given schema_version (conservative if None)."""
    sv = _ver_tuple(schema_ver)
    if sv is None:
        return list(FIELD_VERSIONS.keys())
    return [name for name, fv in FIELD_VERSIONS.items() if sv < (_ver_tuple(fv) or (0, 0))]


def _resolve_stub(query: str) -> str | None:
    """Resolve query to a stub slug (folder with no profile.md), or None.

    Tries exact canon match first, then prefix match ('norexi' → 'norexi-org' if unique).
    """
    cq = canon(query)
    stub_slugs = [
        os.path.basename(d)
        for d in sorted(glob.glob(os.path.join(STORE, "*")))
        if os.path.isdir(d) and not os.path.exists(os.path.join(d, "profile.md"))
    ]
    if cq in stub_slugs:
        return cq
    prefix_hits = [s for s in stub_slugs if s.startswith(cq + "-")]
    return prefix_hits[0] if len(prefix_hits) == 1 else None


def _profile_line(query: str, slug: str, fm: dict[str, Any]) -> str:
    """Format one 'find' result line for a profile with per-layer clocks and predates annotation."""
    parts: list[str] = []
    ca = fm.get("captured_at")
    if ca:
        d = _days_ago(ca)
        parts.append(f"captured {ca} ({d}d)")
    slug_dir = os.path.join(STORE, slug)
    for mod in ("offerings", "telehealth"):
        mod_path = os.path.join(slug_dir, f"{mod}.md")
        if os.path.exists(mod_path):
            mca = _frontmatter(mod_path).get("captured_at")
            if mca:
                parts.append(f"{mod} {mca}")
    sv = fm.get("schema_version")
    pre = _predates(sv)
    sv_str = f"schema {sv}" + (f" — predates: {', '.join(pre)}" if pre else "")
    parts.append(sv_str)
    return f"{query} → {slug:<26} {' · '.join(parts)}"


# --- CLI ------------------------------------------------------------------------------------------
def _hit_line(query: str, profiles: dict[str, dict[str, Any]]) -> str | None:
    """A definite 'find' hit — profile (with clocks) or stub — formatted; None on a miss."""
    hit = resolve(query, profiles)
    if hit:
        return _profile_line(query, hit, profiles[hit])
    stub = _resolve_stub(query)
    if stub:
        cap = _stub_capture_date(stub)
        cap_str = f"({cap})" if cap else "(no captures)"
        return f"{query} → {stub:<26} STUB — captures only {cap_str}, no profile"
    return None


def _miss_line(query: str, profiles: dict[str, dict[str, Any]]) -> str:
    """The miss half of 'find': fuzzy candidates across all folders (profiles + stubs), or NOT in store."""
    cq = canon(query)
    all_dirs = {os.path.basename(d) for d in glob.glob(os.path.join(STORE, "*")) if os.path.isdir(d)}
    cands = sorted(
        {
            slug
            for slug in all_dirs
            if cq in canon(slug)
            or (
                slug in profiles
                and (
                    cq in canon(profiles[slug].get("domain") or "")
                    or any(cq in canon(a) for a in (profiles[slug].get("aliases") or []) if _is_domainish(a))
                    or query.strip().lower() in str(profiles[slug].get("name") or "").lower()
                )
            )
        }
    )
    return f"{query} → no exact key; candidates: {', '.join(cands)}" if cands else f"{query} → NOT in store"


def _cli_find(profiles: dict[str, dict[str, Any]], *args: str) -> None:
    if not args or args[0].startswith("-"):
        return print("usage: store.py find <query> [<query> ...]")
    # Unquoted multi-word names are the common case, so all args are tried as ONE query first.
    # But a joined miss must never mask per-company hits — `find "Marek Health" "Defy Medical"`
    # once printed a single false NOT-in-store — so on a miss, each arg is retried as its own query.
    joined = " ".join(args)
    line = _hit_line(joined, profiles)
    if line:
        return print(line)
    if len(args) > 1:
        per_arg = [(query, _hit_line(query, profiles)) for query in args]
        if any(hit for _, hit in per_arg):
            for query, hit in per_arg:
                print(hit or _miss_line(query, profiles))
            return
    print(_miss_line(joined, profiles))


def _cli_relations(profiles: dict[str, dict[str, Any]], *_: str) -> None:
    r = relations(profiles)
    print(f"relation targets: {len(r['joinable'])} joinable · {len(r['dangling'])} dangling · {len(r['named'])} name-only\n")
    print("JOINABLE (resolves to a held profile):")
    for slug, field, t, hit in r["joinable"]:
        print(f"  {slug:>24} --{field}--> {t}  → {hit}")
    print("\nDANGLING (no profile yet — re-capture candidates, by in-degree):")
    rank = r["dangling_indegree"]
    for slug, field, t in sorted(r["dangling"], key=lambda x: (-rank[canon(x[2])], x[2])):
        deg = rank[canon(t)]
        print(f"  {slug:>24} --{field}--> {t}" + (f"   [{deg} refs]" if deg > 1 else ""))
    print("\nNAME-ONLY (un-joinable by design):")
    for slug, field, t in r["named"]:
        print(f"  {slug:>24} --{field}--> {t!r}")


def _cli_health(profiles: dict[str, dict[str, Any]], *_: str) -> None:
    all_dirs = sorted(os.path.basename(d) for d in glob.glob(os.path.join(STORE, "*")) if os.path.isdir(d))
    stubs = [d for d in all_dirs if d not in profiles]

    print(f"store health — {len(profiles)} profiles · {len(stubs)} stubs\n")

    # Stubs
    if stubs:
        print(f"STUBS ({len(stubs)}):")
        for s in stubs:
            cap = _stub_capture_date(s)
            suffix = f"  (captures only {cap})" if cap else ""
            print(f"  {s}{suffix}")
        print()

    # Staleness ranking (oldest 10 by captured_at)
    ages: list[tuple[int, str, object]] = []
    for slug, fm in profiles.items():
        ca = fm.get("captured_at")
        d = _days_ago(ca)
        if d is not None:
            ages.append((d, slug, ca))
    ages.sort(reverse=True)
    top = ages[:10]
    print(f"STALENESS (oldest {len(top)}):")
    for age, slug, ca in top:
        print(f"  {age:3d}d  {slug:<32} {ca}")
    print()

    # Module clock skew (any module whose captured_at diverges from profile's)
    skews: list[tuple[str, str, int, object, int, object]] = []
    for slug, fm in profiles.items():
        pd = _days_ago(fm.get("captured_at"))
        if pd is None:
            continue
        slug_dir = os.path.join(STORE, slug)
        for mod in ("offerings", "telehealth"):
            mod_path = os.path.join(slug_dir, f"{mod}.md")
            if not os.path.exists(mod_path):
                continue
            mca = _frontmatter(mod_path).get("captured_at")
            md = _days_ago(mca)
            if md is not None and abs(pd - md) > 0:
                skews.append((slug, mod, pd, fm.get("captured_at"), md, mca))
    if skews:
        skews.sort(key=lambda x: abs(x[2] - x[4]), reverse=True)
        print("MODULE CLOCK SKEW:")
        for slug, mod, pd, pdate, md, mdate in skews:
            diff = abs(pd - md)
            direction = "profile older" if pd > md else "module older"
            print(f"  {slug:<28} profile {pdate} ({pd}d) · {mod} {mdate} ({md}d)  [{diff}d, {direction}]")
        print()


_DISPATCH: dict[str, Callable[..., None]] = {
    "find": _cli_find,
    "relations": _cli_relations,
    "health": _cli_health,
}


def main() -> None:
    profiles = load()
    if len(sys.argv) > 1 and sys.argv[1] in _DISPATCH:
        _DISPATCH[sys.argv[1]](profiles, *sys.argv[2:])
    else:
        if len(sys.argv) > 1:
            print(f"unknown command {sys.argv[1]!r}\n")
        all_dirs = sum(1 for d in glob.glob(os.path.join(STORE, "*")) if os.path.isdir(d))
        stubs = all_dirs - len(profiles)
        print(
            f"store.py — {len(profiles)} profiles · {stubs} stubs. commands: {', '.join(_DISPATCH)}\n"
            f"  find <query>   domain/name/alias/slug → profile or stub info\n"
            f"  relations      parent/owns join-check + re-capture ranking\n"
            f"  health         stubs · staleness · module-clock skew"
        )


if __name__ == "__main__":
    main()
