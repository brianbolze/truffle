#!/usr/bin/env python3
"""probe — coded query primitives over the store, to see which earn a script vs a QUERYING.md recipe.

The bet: most consume-side asks are a one-line YAML filter (QUERYING.md already shows them), but a
few are fiddly enough by hand that an agent gets them subtly wrong — the resolver (domain/name/alias
→ one key) and the relation join-check (which parent/owns/alias entries actually point at a profile).
Those are the candidates for code. The rest (count, recent, facet) are conveniences this proves cheap.

Stdlib + PyYAML. Run `python probe.py` for the headline battery, or a single command (see DISPATCH).
"""
import glob
import os
import re
import sys
from collections import Counter
from datetime import date

try:
    import yaml
except ImportError:
    sys.exit("PyYAML not importable — `pip install pyyaml`.")

ROOT = os.environ.get("STORE_ROOT") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STORE = os.path.join(ROOT, "store")


# --- load -----------------------------------------------------------------------------------------
def frontmatter(p):
    t = open(p, encoding="utf-8").read()
    return yaml.safe_load(t.split("---", 2)[1]) if t.startswith("---") else {}


def load():
    """{slug: frontmatter-dict}. slug is the dir name (the actual store key), not the `domain` field."""
    return {os.path.basename(os.path.dirname(p)): frontmatter(p)
            for p in sorted(glob.glob(os.path.join(STORE, "*", "profile.md")))}


def canon(s):
    """Fold a domain / slug / alias to one comparable key: lowercase, scheme+www stripped, dots→dashes.

    This is the whole trick behind 'domain is the key' actually working: the store dir is `honehealth-com`,
    the `domain:` field is `honehealth.com`, and `owns:` entries come BOTH ways (`converse.com` vs the
    slug-form `gshock-casio-com`). canon() collapses all of them so a lookup matches regardless of form.
    """
    s = str(s).strip().lower()
    s = re.sub(r"^https?://", "", s).rstrip("/")
    s = re.sub(r"^www\.", "", s)
    return s.replace(".", "-")


def is_domainish(s):
    """Does this string look like a domain/slug (joinable) vs a free-text name (not)?

    A relation target is either a resolvable domain or a quoted company name — the schema says so.
    Domain markers: a dotted TLD, or the dashed slug-form the store dirs use (`foo-com`, `bar-ai`)."""
    s = str(s).strip().lower()
    return bool(re.search(r"\.[a-z]{2,}$", s)) or bool(re.match(r"^[a-z0-9-]+-(com|ai|io|net|org|co|so)$", s))


def index(P):
    """canon-key → slug, over slug + domain + every alias. The resolver's lookup table."""
    idx = {}
    for slug, fm in P.items():
        keys = {canon(slug), canon(fm.get("domain") or slug)}
        keys |= {canon(a) for a in (fm.get("aliases") or []) if is_domainish(a)}
        keys |= {str(a).strip().lower() for a in (fm.get("aliases") or [])}  # name-form aliases too
        for k in keys:
            idx.setdefault(k, slug)
    return idx


# --- probes ---------------------------------------------------------------------------------------
def cmd_stats(P, *_):
    """count — total + the breakdowns you'd otherwise eyeball. The cheap, obvious one."""
    print(f"{len(P)} profiles in {STORE}\n")
    for field in ("entity_type", "business_model", "primary_industry"):
        c = Counter(fm.get(field) or "—" for fm in P.values())
        print(f"by {field}:")
        for v, n in c.most_common():
            print(f"  {n:>3}  {v}")
        print()
    # multi-selects: count membership, not the tuple (the grep|uniq trap QUERYING.md warns about)
    for field in ("target_market", "offering_category"):
        c = Counter(v for fm in P.values() for v in (fm.get(field) or []))
        print(f"by {field} (membership):")
        for v, n in c.most_common():
            print(f"  {n:>3}  {v}")
        print()


def cmd_find(P, *args):
    """search — is X in the store? Resolves domain / name / alias / slug → the canonical key.

    The value here isn't the happy path (you'd guess the slug); it's the misses an agent makes by hand —
    `granola.so` → granola-ai, `chatgpt.com` → openai-com, `Peter Uncaged MD` → getpetermd-com."""
    if not args:
        return print("usage: find <query>")
    q = " ".join(args)
    idx = index(P)
    # 1) exact, via canon (domain/slug/domainish-alias) or lowercased name-alias
    hit = idx.get(canon(q)) or idx.get(q.strip().lower())
    if hit:
        return print(f"'{q}' → {hit}  (exact)")
    # 2) name match, case-insensitive
    for slug, fm in P.items():
        if q.strip().lower() == str(fm.get("name") or "").lower():
            return print(f"'{q}' → {slug}  (name)")
    # 3) substring fallback — report candidates, don't guess one
    cq = canon(q)
    cands = sorted({slug for slug, fm in P.items()
                    if cq in canon(slug) or cq in canon(fm.get("domain") or "")
                    or any(cq in canon(a) for a in (fm.get("aliases") or []) if is_domainish(a))
                    or q.strip().lower() in str(fm.get("name") or "").lower()})
    if cands:
        return print(f"'{q}' → no exact key; candidates: {', '.join(cands)}")
    print(f"'{q}' → NOT in store")


def cmd_recent(P, *args):
    """recency — captured_at, newest first; flags staleness. captured_at parses as a real date, so this sorts free."""
    n = int(args[0]) if args and args[0].isdigit() else len(P)
    today = date.today()

    def cap(fm):
        v = fm.get("captured_at")
        return v if isinstance(v, date) else date.fromisoformat(str(v)[:10])

    rows = sorted(((cap(fm), slug) for slug, fm in P.items()), reverse=True)
    print(f"capture freshness (of {len(rows)}; today {today}):\n")
    for d, slug in rows[:n]:
        print(f"  {d}  ({(today - d).days:>3}d)  {slug}")
    oldest = rows[-1]
    print(f"\noldest: {oldest[1]} @ {oldest[0]} ({(today - oldest[0]).days}d)")


def cmd_relations(P, *_):
    """relations / join-check — THE one prose can't do reliably: which parent/owns/alias entries resolve.

    Each target is one of: joinable (→ a profile we hold), dangling (domain-shaped but no profile yet =
    a re-capture candidate), or name (un-joinable by design). Doing this by eye across 45 profiles is
    where an agent quietly miscounts."""
    idx = index(P)
    joinable, dangling, named = [], [], []
    for slug, fm in P.items():
        for field in ("parent", "owns"):
            for t in (fm.get(field) or []):
                row = (slug, field, t)
                if not is_domainish(t):
                    named.append(row)
                elif canon(t) in idx:
                    joinable.append(row + (idx[canon(t)],))
                else:
                    dangling.append(row)
    print(f"relation targets: {len(joinable)} joinable · {len(dangling)} dangling · {len(named)} name-only\n")
    print("JOINABLE (resolves to a held profile):")
    for slug, field, t, hit in joinable:
        print(f"  {slug:>22} --{field}--> {t}  → {hit}")
    print("\nDANGLING (domain-shaped, no profile yet — re-capture candidates):")
    for slug, field, t in dangling:
        print(f"  {slug:>22} --{field}--> {t}")
    print("\nNAME-ONLY (un-joinable by design):")
    for slug, field, t in named:
        print(f"  {slug:>22} --{field}--> {t!r}")


def cmd_facet(P, *args):
    """facet — generic group-by on any field; lists membership for multi-selects. Proves the recipe is one call."""
    if not args:
        return print("usage: facet <field>")
    f = args[0]
    multi = any(isinstance(fm.get(f), list) for fm in P.values())
    if multi:  # count membership across the lists
        c = Counter(v for fm in P.values() for v in (fm.get(f) or []))
    else:      # scalar — count the value itself (don't iterate the string's chars)
        c = Counter(fm.get(f) or "—" for fm in P.values())
    for v, n in c.most_common():
        print(f"  {n:>3}  {v}")


def cmd_coverage(P, *_):
    """coverage — how populated is each field across the corpus? Surfaces where the store is thin."""
    fields = ["domain", "name", "aliases", "parent", "owns", "entity_type", "target_market",
              "offering_category", "portfolio_shape", "business_model", "primary_industry",
              "logo_url", "brand_colors", "design_framework", "unverified_fields"]
    n = len(P)
    for f in fields:
        have = sum(1 for fm in P.values() if fm.get(f) not in (None, "", []))
        bar = "█" * round(20 * have / n)
        print(f"  {have:>3}/{n}  {bar:<20}  {f}")


DISPATCH = {"stats": cmd_stats, "find": cmd_find, "recent": cmd_recent,
            "relations": cmd_relations, "facet": cmd_facet, "coverage": cmd_coverage}


if __name__ == "__main__":
    P = load()
    if len(sys.argv) > 1 and sys.argv[1] in DISPATCH:
        DISPATCH[sys.argv[1]](P, *sys.argv[2:])
    else:
        if len(sys.argv) > 1:
            print(f"unknown command {sys.argv[1]!r}; commands: {', '.join(DISPATCH)}\n")
        print(f"probe.py — {len(P)} profiles. commands: {', '.join(DISPATCH)}")
