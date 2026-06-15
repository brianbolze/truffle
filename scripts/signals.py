#!/usr/bin/env python3
"""signals — the store-side writer for time-axis Signal captures (a `scripts/` store-manager).

The capture tools (`tools/*.py`) print envelopes to stdout and never touch the store ("print, don't
write"). This is the one place those envelopes LAND: `persist()` writes a capture verbatim to the path
convention `store/<domain>/signals/<source_type>/<captured_at>.json`, so repeat captures accumulate where
`tools/signal_delta.py` can diff them. It lives in `scripts/` because writing the store is a scripts job,
not a capture job.

Earned now, exactly as the [traction approach](../_design/2026-06-15-traction-approach.md) scoped it: the
automated writer graduates "with an automated writer AND a second consumer." Both exist — the **run** verb
(weekly batch capture) and the **import** verb (consolidate scattered captures) are the two callers, sharing
one `persist()` primitive. The card schema-as-contract / lint / SQLite lens stay deferred: every consumer so
far eats *raw envelopes*, never a card.

Four verbs:
  capture  [company] [--tools] [--yes]  drive a default tool set from one company (prompts if omitted)
  persist  <envelope.json | ->          write one envelope (file or stdin) to the convention path
  run      <panel.jsonl> [--dry-run]    batch-invoke captures across a panel, persist each, emit a run log
  import   <path> [<path> ...]          consolidate existing envelope files/dirs into the store

Notes baked in from the dogfood that earned this:
  - **Canonical keying.** The store key folds through `store.resolve()` (an alias in a profile's
    frontmatter resolves to its survivor), so a capture made under an alias (trustpilot's `tryeden.com`)
    lands under the canonical company (`eden-health`), never an orphan `tryeden-com/` dir — the Signals
    enforcement of SCHEMA's "domain is the key". Degrades to a bare `canon()` if PyYAML isn't importable.
  - **capture's subject resolution.** Per tool, the subject is the most-recent *usable* prior capture's
    subject (so Eden's trustpilot reuses `tryeden.com`, never re-probing the missing `eden.health` and
    burning a paid credit), else a primary→aliases seed ladder. Alias-laddering is per-tool: a Trustpilot
    profile follows the brand; a Wayback page does not (an alias is a different site).
  - **Page-slug for multi-URL sources.** wayback is many URLs per domain; the bare
    `signals/<source_type>/<captured_at>.json` collides, so a url-path slug subdir separates them.
  - **Slash-variant dedup.** A URL captured with and without a trailing `/` canonicalizes to one slug.
  - **Interpreter pin.** captures run with `sys.executable`, not a bare `python3` (the pyenv shim flakes
    on some tools).
  - **Company/page-grain only.** A category-grain envelope (serpapi query) has no domain home yet
    (`cohorts/` is deferred) — `persist()` refuses it rather than guess a domain.

Exit codes: 0 clean · 2 operational error (bad input, a category-grain envelope with no domain, unreadable JSON).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

STORE = Path(__file__).resolve().parents[1] / "store"  # scripts/signals.py -> repo root -> store/


def canon(value: str) -> str:
    """Store-dir slug (the `scripts/store.py` rule): lowercase, strip scheme, dots -> dashes."""
    return re.sub(r"^https?://", "", value).strip("/").lower().replace(".", "-")


def _load_profiles() -> dict[str, dict[str, Any]] | None:
    """Preload the profile corpus once per invocation so per-row `_canonical()` folds don't each reload
    it. `None` when the resolver isn't importable (PyYAML missing) — `_canonical` then degrades to a bare
    `canon()` per row, so captures never depend on the resolver being available."""
    try:
        from store import load

        return load()
    except Exception:
        return None


def _canonical(raw_key: str, profiles: dict[str, dict[str, Any]] | None = None) -> str:
    """Fold a derived store key to the *canonical* company slug, so a capture made under an **alias**
    (trustpilot's `tryeden.com`) lands under the canonical company (`eden-health`) instead of orphaning
    a parallel `tryeden-com/` dir. This is the Signals-layer enforcement of SCHEMA's "domain is the key",
    via the same `store.resolve()` the State layer uses (an alias in a profile's frontmatter resolves to
    its survivor). Degrades to this module's own `canon()` (the identical rule) if the resolver/PyYAML
    isn't importable, so a capture never fails just because the resolver is unavailable."""
    try:
        from store import resolve
    except Exception:
        return canon(raw_key)
    return resolve(raw_key, profiles) or canon(raw_key)


def _domain(envelope: dict[str, Any], explicit: str | None = None, profiles: dict[str, dict[str, Any]] | None = None) -> str:
    """The canonical store key for this capture. The raw subject comes from the tool that carries it
    (trustpilot slug, wayback URL host, sec_edgar domain) or the caller's `explicit` (trends keyword, or
    any envelope whose subject isn't a domain); that raw form is then folded to the canonical slug via
    `_canonical()`. A category-grain query has no domain — that's an error."""
    raw = explicit
    if raw is None:
        tool = envelope.get("tool")
        inp = envelope.get("input", {})
        if tool == "trustpilot" and inp.get("slug"):
            raw = inp["slug"]
        elif tool == "wayback" and inp.get("url"):
            raw = re.sub(r"^www\.", "", urlparse(inp["url"]).netloc)  # store slug is the bare domain, not www.
        elif tool == "sec_edgar":
            cand = inp.get("domain") or envelope.get("subject", "")
            if "." in cand:
                raw = cand
    if raw is None:
        raise ValueError(
            f"can't derive a domain for tool={envelope.get('tool')!r} — pass --domain "
            f"(or it's category-grain, e.g. a serpapi query, which has no store home yet → cohorts/, deferred)"
        )
    return _canonical(raw, profiles)


def _page_slug(envelope: dict[str, Any]) -> str | None:
    """A url-path slug subdir for multi-URL-per-domain sources (wayback), so many pages of one domain
    don't collide on `<source_type>/<captured_at>.json`. The trailing slash is stripped first, so a URL
    captured as `…/nad` and `…/nad/` folds onto one slug (the slash-variant dedup)."""
    if envelope.get("tool") != "wayback":
        return None
    path = urlparse(envelope.get("input", {}).get("url", "")).path.strip("/")
    return re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-") or "root"


def _stamp(captured_at: str) -> str:
    """The envelope's `captured_at` -> a filesystem-safe filename stem. `signal_delta` sorts on the
    *internal* captured_at, so this is for tidiness + uniqueness, not for ordering."""
    return captured_at.replace("-", "").replace(":", "")


def persist(
    envelope: dict[str, Any],
    domain: str | None = None,
    root: Path | None = None,
    profiles: dict[str, dict[str, Any]] | None = None,
) -> Path:
    """Write `envelope` verbatim to store/<domain>/signals/<source_type>[/<page-slug>]/<stamp>.json.

    `source_type` is the envelope's own `tool`. The store key is folded to canonical via `_domain()`
    (an alias-keyed capture lands under its canonical company); pass `profiles` to reuse one corpus load
    across a batch. Returns the path written. Same domain+source+slug+stamp overwrites (slash-variant
    twins collapse); a different captured_at accumulates (the real time series).
    """
    dest_dir = (root or STORE) / _domain(envelope, domain, profiles) / "signals" / envelope["tool"]
    if slug := _page_slug(envelope):
        dest_dir = dest_dir / slug
    dest = dest_dir / f"{_stamp(envelope['captured_at'])}.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(envelope, f, indent=2)
    return dest


# --------------------------------------------------------------------------- capture fan-out
# The `capture` verb drives a tool from a *company* instead of a hand-typed subject. Only tools whose
# subject is derivable from a domain belong in the default set — trends (keyword) and serpapi (category
# -grain) stay manual; sec_edgar needs a company name, so it's a `--tools` opt-in, not a zero-config
# default. Each spec is the per-tool knowledge `capture` needs, the same shape `_domain()` branches on:
#   subject_key   — the envelope `input` field that carries the subject (to read a prior capture back)
#   subject_tpl   — how to shape a bare domain into the tool's subject for a cold seed (wayback wants a
#                   homepage URL so it lands under the `root` page-slug — matching a manual `https://…/`
#                   capture, so the two invocation paths don't fork the same page into two timelines)
#   paid          — gate behind a cost-confirm before spending
#   ladder_aliases— on a clean miss, retry the company's aliases? (a Trustpilot profile follows the brand
#                   to tryeden.com; a Wayback page does NOT — an alias is a different site, not a fallback)
#   usable        — did this capture return real data, vs a factual miss (not_found) that's still ok:true?
TOOL_SPEC: dict[str, dict[str, Any]] = {
    "trustpilot": {
        "subject_key": "slug",
        "subject_tpl": "{}",
        "paid": True,
        "ladder_aliases": True,
        "usable": lambda env: env.get("profile_state") == "active",
    },
    "wayback": {
        "subject_key": "url",
        "subject_tpl": "https://{}/",
        "paid": False,
        "ladder_aliases": False,
        "usable": lambda env: bool(env.get("snapshots")),
    },
}
DEFAULT_CAPTURE_TOOLS = ["trustpilot", "wayback"]  # the two cleanly domain-driven, repeat-diffable tools


def _invoke(tool: str, args: list[str]) -> tuple[int, dict[str, Any] | None, str]:
    """Run a capture tool as a subprocess — the shared primitive behind `run` and `capture`. Returns
    (exit_code, parsed_envelope_or_None, stderr_tail). `sys.executable`, never a bare `python3` (the
    pyenv shim flakes on some tools). The envelope parses whenever stdout is JSON; the caller decides
    what a non-zero exit means (a trustpilot exit-3 drift still carries a veto envelope worth keeping)."""
    tools_dir = Path(__file__).resolve().parents[1] / "tools"
    cmd = [sys.executable, str(tools_dir / f"{tool}.py"), *map(str, args)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    env: dict[str, Any] | None = None
    if proc.stdout.strip():
        try:
            env = json.loads(proc.stdout)
        except json.JSONDecodeError:
            env = None
    return proc.returncode, env, proc.stderr.strip()[-300:]


def _resolve_company(company: str, profiles: dict[str, dict[str, Any]]) -> tuple[str, str, list[str], bool]:
    """(canonical_slug, primary_domain, domainish_aliases, in_store) for a company surface form. Resolved
    against the store so `capture eden.health` knows its canonical slug AND its aliases (tryeden.com) for
    the fallback ladder. Not in the store → capture under canon(company) with no alias fallback."""
    try:
        from store import _is_domainish, resolve
    except Exception:
        return canon(company), company, [], False
    slug = resolve(company, profiles) if profiles else None
    if not slug:
        return canon(company), company, [], False
    fm = profiles.get(slug, {})
    primary = fm.get("domain") or company
    aliases = [a for a in (fm.get("aliases") or []) if _is_domainish(a)]
    return slug, primary, aliases, True


def _remembered_subject(slug: str, tool: str, spec: dict[str, Any], root: Path | None = None) -> str | None:
    """The subject from the most-recent **usable** prior capture of this (company, tool) — so a re-capture
    reuses the subject that actually worked (Eden's tryeden.com) instead of re-probing the primary that
    always misses (eden.health), which on a paid tool burns a credit every run. None when there's no usable
    prior capture (cold — fall back to the primary→aliases seed ladder). `rglob` because wayback page-nests."""
    base = (root or STORE) / slug / "signals" / tool
    if not base.is_dir():
        return None
    best_at, best_subject = "", None
    for f in base.rglob("*.json"):
        try:
            with open(f, encoding="utf-8") as fh:
                env = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        if spec["usable"](env) and (at := env.get("captured_at", "")) >= best_at:
            best_at, best_subject = at, env.get("input", {}).get(spec["subject_key"])
    return best_subject


def _capture_tool(
    slug: str,
    tool: str,
    spec: dict[str, Any],
    candidates: list[str],
    profiles: dict[str, dict[str, Any]] | None,
    assume_yes: bool,
    dry_run: bool,
) -> dict[str, Any]:
    """Capture one tool for one company: confirm if paid, then try `candidates` in order, persisting each
    result under the canonical `slug` and stopping at the first usable hit. Only a clean miss (ok:true but
    not usable, e.g. not_found) ladders to the next candidate; a transport/drift error stops the ladder."""
    if dry_run:
        print(f"would capture: {tool} for {slug} via {candidates} ({'paid' if spec['paid'] else 'free'})")
        return {"tool": tool, "subject_candidates": candidates, "dry_run": True}
    if spec["paid"] and not assume_yes:
        prompt = f"  {tool}: capture {slug} via {candidates} (~{len(candidates)} Firecrawl credit(s), paid). Proceed? [y/N] "
        if input(prompt).strip().lower() not in ("y", "yes"):
            sys.stderr.write(f"  [{tool}] skipped (paid, not confirmed)\n")
            return {"tool": tool, "skipped": "paid_not_confirmed"}
    rec: dict[str, Any] = {"tool": tool, "tried": []}
    for subject in candidates:
        rc, env, err = _invoke(tool, [subject])
        attempt: dict[str, Any] = {"subject": subject, "exit_code": rc}
        usable = env is not None and bool(spec["usable"](env))
        if env is not None:
            attempt["persisted"] = str(persist(env, domain=slug, profiles=profiles).relative_to(STORE.parent))
            attempt["usable"] = usable
        else:
            attempt["stderr_tail"] = err
        rec["tried"].append(attempt)
        sys.stderr.write(f"  [{tool}] {subject} exit={rc} usable={usable}\n")
        if not (rc == 0 and env is not None and not usable):
            break  # stop on a usable hit or a transport/drift error; ladder on only a clean miss
    return rec


# --------------------------------------------------------------------------- verbs
def cmd_persist(args: argparse.Namespace) -> int:
    """Write one envelope (a file path, or `-` for stdin) to the convention path."""
    raw = sys.stdin.read() if args.envelope == "-" else Path(args.envelope).read_text(encoding="utf-8")
    dest = persist(json.loads(raw), domain=args.domain, profiles=_load_profiles())
    print(dest.relative_to(STORE.parent))
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    """Batch-invoke captures across a panel (JSONL rows: {id?, tool, args:[...], domain?}), persist each,
    emit a run log. The capture tools are the same `tools/*.py` you'd run by hand — this just stops the
    per-capture mkdir+redirect loop. Captures run with `sys.executable` (the interpreter pin). `--dry-run`
    previews the commands without running them — a cost-preview before a paid panel."""
    rows = [json.loads(line) for line in Path(args.panel).read_text(encoding="utf-8").splitlines() if line.strip()]
    if args.dry_run:
        for row in rows:
            tail = f"  → {row['domain']}" if row.get("domain") else ""
            print(f"would run: {row['tool']} {row.get('args', [])}{tail}")
        return 0
    profiles = _load_profiles()
    records: list[dict[str, Any]] = []
    for row in rows:
        rc, env, err = _invoke(row["tool"], row.get("args", []))
        rec: dict[str, Any] = {"id": row.get("id"), "tool": row["tool"], "exit_code": rc}
        if rc == 0 and env is not None:
            rec["ok"] = env.get("ok")
            rec["cost"] = env.get("cost")
            rec["persisted"] = str(persist(env, domain=row.get("domain"), profiles=profiles).relative_to(STORE.parent))
        else:
            rec["stderr_tail"] = err
        records.append(rec)
        sys.stderr.write(f"  [{row.get('id') or row['tool']}] exit={rc}\n")
    print(json.dumps({"run": "signals", "records": records}, indent=2))
    return 0


def cmd_capture(args: argparse.Namespace) -> int:
    """Capture one company across a default tool set — the ergonomic front door (no panel file, no pipe).

    Prompts for the company when it's omitted, resolves it to its canonical slug + aliases, then for each
    tool picks the subject from the most-recent *usable* prior capture (Eden's trustpilot reuses tryeden.com)
    or seeds a primary→aliases ladder when cold. Persists every result under the canonical company. Paid
    tools confirm before spending (`--yes` to skip); `--dry-run` previews the plan without running anything.
    """
    company = (args.company or input("Company (domain / name)? ")).strip()
    if not company:
        sys.stderr.write("Error: no company given\n")
        return 2
    profiles = _load_profiles() or {}
    slug, primary, aliases, in_store = _resolve_company(company, profiles)
    if not in_store:
        sys.stderr.write(f"note: {company!r} not in the store — capturing under {slug!r} with no alias fallback\n")

    tools = [t.strip() for t in args.tools.split(",")] if args.tools else list(DEFAULT_CAPTURE_TOOLS)
    records: list[dict[str, Any]] = []
    for tool in tools:
        spec = TOOL_SPEC.get(tool)
        if spec is None:
            sys.stderr.write(
                f"  [{tool}] no capture spec — run it directly + `persist` (trends/serpapi are keyword/"
                f"category-grain; sec_edgar needs a company name)\n"
            )
            records.append({"tool": tool, "skipped": "no_capture_spec"})
            continue
        remembered = _remembered_subject(slug, tool, spec)
        candidates = [remembered] if remembered else _seed_candidates(primary, aliases, spec)
        records.append(_capture_tool(slug, tool, spec, candidates, profiles, args.yes, args.dry_run))
    print(json.dumps({"capture": company, "slug": slug, "records": records}, indent=2))
    return 0


def _seed_candidates(primary: str, aliases: list[str], spec: dict[str, Any]) -> list[str]:
    """Cold-start subjects to try in order: the primary domain, then (only for alias-laddering tools) the
    company's domainish aliases — each shaped by the tool's `subject_tpl`. Used once, to seed; thereafter
    `_remembered_subject` short-circuits here."""
    tpl = spec.get("subject_tpl", "{}")
    domains = [primary] + ([a for a in aliases if a != primary] if spec["ladder_aliases"] else [])
    return [tpl.format(d) for d in domains]


def cmd_import(args: argparse.Namespace) -> int:
    """Consolidate existing envelope files into the store (the salvage importer). Each path is a file or a
    dir (globbed for *.json). Only raw capture envelopes (a top-level `tool`) are imported, verbatim."""
    profiles = _load_profiles()
    files: list[Path] = []
    for p in (Path(x) for x in args.paths):
        files.extend(sorted(p.rglob("*.json")) if p.is_dir() else [p])
    imported = 0
    for f in files:
        try:
            env = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if not (isinstance(env, dict) and "tool" in env):
            continue
        try:
            dest = persist(env, domain=args.domain, profiles=profiles)
        except ValueError as e:
            sys.stderr.write(f"  skip {f.name}: {e}\n")
            continue
        imported += 1
        print(dest.relative_to(STORE.parent))
    sys.stderr.write(f"imported {imported}/{len(files)} envelope(s)\n")
    return 0


DISPATCH = {"capture": cmd_capture, "persist": cmd_persist, "run": cmd_run, "import": cmd_import}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="verb", required=True)

    sc = sub.add_parser("capture", help="capture one company across a default tool set (prompts if omitted)")
    sc.add_argument("company", nargs="?", help="company domain / name / store-slug; prompts when omitted")
    sc.add_argument("--tools", help=f"comma-separated tool list (default: {','.join(DEFAULT_CAPTURE_TOOLS)})")
    sc.add_argument("--yes", action="store_true", help="skip the cost-confirm on paid tools")
    sc.add_argument("--dry-run", action="store_true", help="preview the per-tool plan without running anything")

    sp = sub.add_parser("persist", help="write one envelope (file or - for stdin) to the convention path")
    sp.add_argument("envelope", help="path to an envelope JSON, or '-' for stdin")
    sp.add_argument("--domain", help="store key, when the envelope's subject isn't a domain (e.g. trends)")

    sr = sub.add_parser("run", help="batch-invoke captures across a panel and persist each")
    sr.add_argument("panel", help="JSONL panel: one {id?, tool, args:[...], domain?} per line")
    sr.add_argument("--dry-run", action="store_true", help="preview the commands without running them (no spend)")

    si = sub.add_parser("import", help="consolidate existing envelope files/dirs into the store")
    si.add_argument("paths", nargs="+", help="envelope files or dirs (dirs are globbed for *.json)")
    si.add_argument("--domain", help="force the store key for every imported envelope")

    args = p.parse_args()
    try:
        sys.exit(DISPATCH[args.verb](args))
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(2)


if __name__ == "__main__":
    main()
