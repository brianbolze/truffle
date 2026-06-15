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

Three verbs:
  persist  <envelope.json | ->        write one envelope (file or stdin) to the convention path
  run      <panel.jsonl> [--dry-run]  batch-invoke captures across a panel, persist each, emit a run log
  import   <path> [<path> ...]        consolidate existing envelope files/dirs into the store

Notes baked in from the dogfood that earned this:
  - **Page-slug for multi-URL sources.** wayback is many URLs per domain; the bare
    `signals/<source_type>/<captured_at>.json` collides, so a url-path slug subdir separates them.
  - **Slash-variant dedup.** A URL captured with and without a trailing `/` canonicalizes to one slug.
  - **Interpreter pin.** `run` invokes captures with `sys.executable`, not a bare `python3` (the pyenv
    shim flakes on some tools).
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


def _domain(envelope: dict[str, Any], explicit: str | None = None) -> str:
    """The store key for this capture. Derived from the subject where the tool carries it (trustpilot
    slug, wayback URL host, sec_edgar domain); else the caller must pass `explicit` (trends keyword,
    or any envelope whose subject isn't a domain). A category-grain query has no domain — that's an error."""
    if explicit:
        return canon(explicit)
    tool = envelope.get("tool")
    inp = envelope.get("input", {})
    if tool == "trustpilot" and inp.get("slug"):
        return canon(inp["slug"])
    if tool == "wayback" and inp.get("url"):
        return canon(re.sub(r"^www\.", "", urlparse(inp["url"]).netloc))  # store slug is the bare domain, not www.
    if tool == "sec_edgar":
        cand = inp.get("domain") or envelope.get("subject", "")
        if "." in cand:
            return canon(cand)
    raise ValueError(
        f"can't derive a domain for tool={tool!r} — pass --domain "
        f"(or it's category-grain, e.g. a serpapi query, which has no store home yet → cohorts/, deferred)"
    )


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


def persist(envelope: dict[str, Any], domain: str | None = None, root: Path | None = None) -> Path:
    """Write `envelope` verbatim to store/<domain>/signals/<source_type>[/<page-slug>]/<stamp>.json.

    `source_type` is the envelope's own `tool`. Returns the path written. Same domain+source+slug+stamp
    overwrites (slash-variant twins collapse); a different captured_at accumulates (the real time series).
    """
    dest_dir = (root or STORE) / _domain(envelope, domain) / "signals" / envelope["tool"]
    if (slug := _page_slug(envelope)):
        dest_dir = dest_dir / slug
    dest = dest_dir / f"{_stamp(envelope['captured_at'])}.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(envelope, f, indent=2)
    return dest


# --------------------------------------------------------------------------- verbs
def cmd_persist(args: argparse.Namespace) -> int:
    """Write one envelope (a file path, or `-` for stdin) to the convention path."""
    raw = sys.stdin.read() if args.envelope == "-" else Path(args.envelope).read_text(encoding="utf-8")
    dest = persist(json.loads(raw), domain=args.domain)
    print(dest.relative_to(STORE.parent))
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    """Batch-invoke captures across a panel (JSONL rows: {id?, tool, args:[...], domain?}), persist each,
    emit a run log. The capture tools are the same `tools/*.py` you'd run by hand — this just stops the
    per-capture mkdir+redirect loop. Captures run with `sys.executable` (the interpreter pin). `--dry-run`
    previews the commands without running them — a cost-preview before a paid panel."""
    tools_dir = Path(__file__).resolve().parents[1] / "tools"
    rows = [json.loads(line) for line in Path(args.panel).read_text(encoding="utf-8").splitlines() if line.strip()]
    if args.dry_run:
        for row in rows:
            tail = f"  → {row['domain']}" if row.get("domain") else ""
            print(f"would run: {row['tool']} {row.get('args', [])}{tail}")
        return 0
    records: list[dict[str, Any]] = []
    for row in rows:
        cmd = [sys.executable, str(tools_dir / f"{row['tool']}.py"), *map(str, row.get("args", []))]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        rec: dict[str, Any] = {"id": row.get("id"), "tool": row["tool"], "exit_code": proc.returncode}
        if proc.returncode == 0 and proc.stdout.strip():
            env = json.loads(proc.stdout)
            rec["ok"] = env.get("ok")
            rec["cost"] = env.get("cost")
            rec["persisted"] = str(persist(env, domain=row.get("domain")).relative_to(STORE.parent))
        else:
            rec["stderr_tail"] = proc.stderr.strip()[-300:]
        records.append(rec)
        sys.stderr.write(f"  [{row.get('id') or row['tool']}] exit={proc.returncode}\n")
    print(json.dumps({"run": "signals", "records": records}, indent=2))
    return 0


def cmd_import(args: argparse.Namespace) -> int:
    """Consolidate existing envelope files into the store (the salvage importer). Each path is a file or a
    dir (globbed for *.json). Only raw capture envelopes (a top-level `tool`) are imported, verbatim."""
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
            dest = persist(env, domain=args.domain)
        except ValueError as e:
            sys.stderr.write(f"  skip {f.name}: {e}\n")
            continue
        imported += 1
        print(dest.relative_to(STORE.parent))
    sys.stderr.write(f"imported {imported}/{len(files)} envelope(s)\n")
    return 0


DISPATCH = {"persist": cmd_persist, "run": cmd_run, "import": cmd_import}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="verb", required=True)

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
