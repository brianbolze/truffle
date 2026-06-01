#!/usr/bin/env python3
"""store — the two consume-side query primitives that are error-prone to do by hand.

QUERYING.md already gives every *easy* read as a one-line YAML filter (count, group-by, recent). This
module exists only for the two that an agent gets subtly wrong by eye, so they're worth committing once:

  resolve(query)  — fold any surface form (domain / name / alias / store-slug) to the one canonical key.
                    "domain is the key" only holds if a single function maps every form to it — canon().
  relations()     — which parent/owns targets actually resolve to a held profile, which dangle (a
                    re-capture candidate, ranked by in-degree), which are name-only (un-joinable by design).

A *derived lens*, never authoritative: the markdown store is the source of truth. Loads frontmatter fresh
(no cache, no index — the whole corpus is ~100KB; see experiments/2026-06-01-coded-queries). Stdlib + PyYAML.

CLI:  python store.py find <query>   ·   python store.py relations
Lib:  from store import load, canon, resolve, relations
"""

from __future__ import annotations

import glob
import os
import re
import sys
from collections import Counter
from typing import Any, Callable

try:
    import yaml
except ImportError:
    sys.exit("PyYAML not importable — the resolver needs it to parse frontmatter.")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, "store")


def _frontmatter(path: str) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return yaml.safe_load(text.split("---", 2)[1]) if text.startswith("---") else {}


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


# --- CLI ------------------------------------------------------------------------------------------
def _cli_find(profiles: dict[str, dict[str, Any]], *args: str) -> None:
    if not args:
        return print("usage: store.py find <query>")
    q = " ".join(args)
    hit = resolve(q, profiles)
    if hit:
        return print(f"'{q}' → {hit}")
    cq = canon(q)
    cands = sorted(
        {
            slug
            for slug, fm in profiles.items()
            if cq in canon(slug)
            or cq in canon(fm.get("domain") or "")
            or any(cq in canon(a) for a in (fm.get("aliases") or []) if _is_domainish(a))
            or q.strip().lower() in str(fm.get("name") or "").lower()
        }
    )
    print(f"'{q}' → no exact key; candidates: {', '.join(cands)}" if cands else f"'{q}' → NOT in store")


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


_DISPATCH: dict[str, Callable[..., None]] = {
    "find": _cli_find,
    "relations": _cli_relations,
}


def main() -> None:
    profiles = load()
    if len(sys.argv) > 1 and sys.argv[1] in _DISPATCH:
        _DISPATCH[sys.argv[1]](profiles, *sys.argv[2:])
    else:
        if len(sys.argv) > 1:
            print(f"unknown command {sys.argv[1]!r}\n")
        print(
            f"store.py — {len(profiles)} profiles. commands: {', '.join(_DISPATCH)}\n"
            f"  find <query>   domain/name/alias/slug → canonical key\n"
            f"  relations      parent/owns join-check + re-capture ranking"
        )


if __name__ == "__main__":
    main()
