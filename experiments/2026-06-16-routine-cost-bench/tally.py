#!/usr/bin/env python3
"""Append one cost row for a routine-cost-bench variant — run INSIDE the benchmarked
session, after the verb finishes.

Three numbers, three honest sources (never a guess):
  * credits  — this run's capture manifest (store/<slug>/captures/<today>/.payloads/
               manifest.jsonl, Firecrawl's own per-call creditsUsed). 0 for variants
               that don't scrape (visual-evidence, a warm serve-and-stop).
  * tokens   — THIS session's own transcript, found by the unique marker the prompt
               printed (grep across ~/.claude/projects). Sums message.usage across turns.
  * minutes  — the start/end epochs the prompt stamped around the verb.

Estimate-grade by design: the final (tally) turn isn't flushed to the transcript yet,
so tokens slightly undercount — fine for budgeting. Throwaway probe; not house-style code.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import os
import subprocess
from pathlib import Path

HOME = Path(os.environ.get("WEB_RESEARCH_HOME") or Path(__file__).resolve().parents[2])
RESULTS = Path(__file__).resolve().parent / "results.csv"
PROJECTS = Path.home() / ".claude" / "projects"
COLUMNS = [
    "variant", "brand", "slug", "date", "credits", "minutes",
    "tokens_in", "tokens_out", "tokens_cache_create", "tokens_cache_read", "notes",
]


def manifest_for(slug: str, date: str, start: float, end: float) -> Path | None:
    """This run's capture manifest — the today-manifest written DURING this run's window
    [start, end]. Windowing by mtime is what keeps same-day variants from counting each
    other's scrape: a sibling variant's manifest was written outside this window. Prefer the
    given slug; else the newest in-window manifest (the verb may canonicalize the slug).
    None ⇒ nothing scraped in-window (visual-evidence, a warm serve-and-stop)."""
    cands = list(HOME.glob(f"store/*/captures/{date}/.payloads/manifest.jsonl"))
    in_window = [p for p in cands if start - 2 <= p.stat().st_mtime <= end + 2]
    direct = HOME / "store" / slug / "captures" / date / ".payloads" / "manifest.jsonl"
    if direct in in_window:
        return direct
    return max(in_window, key=lambda p: p.stat().st_mtime) if in_window else None


def credits_for(slug: str, date: str, start: float, end: float) -> tuple[int, int]:
    """(credits, billable_calls) summed from this run's manifest; (0, 0) when nothing scraped."""
    mf = manifest_for(slug, date, start, end)
    if not mf:
        return 0, 0
    total = calls = 0
    for line in mf.read_text().splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if rec.get("credits") is not None:
            total += rec["credits"]
        calls += 1
    return total, calls


def transcript_for(marker: str) -> Path | None:
    """This session's transcript — the newest *.jsonl under ~/.claude/projects containing
    the marker (newest handles a re-run of the same variant)."""
    try:
        out = subprocess.run(
            ["grep", "-rl", marker, str(PROJECTS)],
            capture_output=True, text=True, timeout=120,
        ).stdout
    except Exception:
        return None
    files = [Path(x) for x in out.splitlines() if x.endswith(".jsonl")]
    return max(files, key=lambda p: p.stat().st_mtime) if files else None


def tokens_for(marker: str) -> tuple[int, int, int, int] | None:
    """(in, out, cache_create, cache_read) summed across the session's assistant turns."""
    tr = transcript_for(marker)
    if not tr:
        return None
    ti = to = cc = cr = 0
    for line in tr.read_text(errors="ignore").splitlines():
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        usage = (obj.get("message") or {}).get("usage")
        if not usage:
            continue
        ti += usage.get("input_tokens", 0)
        to += usage.get("output_tokens", 0)
        cc += usage.get("cache_creation_input_tokens", 0)
        cr += usage.get("cache_read_input_tokens", 0)
    return ti, to, cc, cr


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", required=True)
    ap.add_argument("--brand", required=True)
    ap.add_argument("--slug", required=True, help="store slug (domain dots→dashes, e.g. joinmochi-com)")
    ap.add_argument("--marker", required=True, help="the unique COSTBENCH:: string the prompt printed")
    ap.add_argument("--start", type=float, required=True, help="epoch seconds at verb start")
    ap.add_argument("--end", type=float, required=True, help="epoch seconds at verb end")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--notes", default="")
    a = ap.parse_args()

    credits, calls = credits_for(a.slug, a.date, a.start, a.end)
    minutes = round((a.end - a.start) / 60, 1)
    tok = tokens_for(a.marker)
    if tok is None:
        ti = to = cc = cr = -1  # marker not found — flag, don't fake a zero
        a.notes = (a.notes + " | TOKENS-NOT-FOUND (read /cost manually)").strip(" |")
    else:
        ti, to, cc, cr = tok

    row = {
        "variant": a.variant, "brand": a.brand, "slug": a.slug, "date": a.date,
        "credits": credits, "minutes": minutes,
        "tokens_in": ti, "tokens_out": to, "tokens_cache_create": cc, "tokens_cache_read": cr,
        "notes": f"{a.notes} ({calls} calls)".strip(),
    }
    new = not RESULTS.exists()
    with open(RESULTS, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if new:
            w.writeheader()
        w.writerow(row)
    print(",".join(str(row[c]) for c in COLUMNS))


if __name__ == "__main__":
    main()
