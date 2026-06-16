#!/usr/bin/env python3
"""Roll up what the engine actually spent — read-only, zero new spend.

The authoritative cost data already lives in the store; nothing aggregated it (the
prose `## Provenance` "Credits:" line is a lossy human echo — this reads the machine
ledger underneath it). Two sources, both written at capture time:

  * Firecrawl capture credits — `store/<slug>/captures/<date>/.payloads/manifest.jsonl`,
    one JSONL line per billable `fc.py` call carrying Firecrawl's own
    `metadata.creditsUsed` (+ per-call fetch latency). This is the per-run credit truth
    `fc.py spend` sums for ONE run; runcost rolls it across the whole corpus and cuts it
    by verb (once `fc.py` tags runs), company, or date.
  * Signal-tool cost — `store/<slug>/signals/<source>/<ts>.json` envelopes carry a `cost`
    field in the tool's NATIVE unit (`firecrawl_credits` | `credits` | `usd`). Units are
    heterogeneous on purpose — we report each unit separately and never invent an FX rate.

Use it to budget routines: median / p90 / range credits per run, split by verb, plus the
SerpAPI / Exa / Trustpilot signal spend a refresh routine adds on top. Note Trustpilot
spends Firecrawl credits, so the true Firecrawl budget = capture credits + Trustpilot.
Stdlib-only (the engine's no-dep line); a derived, regenerable lens — never a source of truth.

Usage:
  runcost.py all      [--since YYYY-MM-DD]               # default — the headline table
  runcost.py captures [--by verb|slug|date] [--since ...]
  runcost.py signals  [--since YYYY-MM-DD]
"""

from __future__ import annotations

import argparse
import json
import statistics
from collections import defaultdict
from collections.abc import Iterator
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]  # scripts/runcost.py -> repo root
STORE = ROOT / "store"


# --- Firecrawl capture credits (the manifest ledger) ------------------------


def iter_manifests() -> Iterator[tuple[str, str, Path]]:
    """Every capture manifest as (slug, date, path). One per run; the per-call
    credit + latency lines live inside it (written by fc.py)."""
    for mf in STORE.glob("*/captures/*/.payloads/manifest.jsonl"):
        parts = mf.parts
        slug = parts[parts.index("store") + 1]
        date = parts[parts.index("captures") + 1]
        yield slug, date, mf


def run_records(since: str | None) -> list[dict[str, Any]]:
    """Collapse each manifest into one run record — the unit you budget a routine in.

    `credits` sums only lines Firecrawl billed (legacy lines predate the field and are
    counted as `no_credit`, never guessed). `verb` is the run's tag: the single value if
    all tagged lines agree, `(mixed)` if they disagree, `(untagged)` if none carry one
    (legacy runs + any call made before fc.py's --verb tag existed)."""
    runs: list[dict[str, Any]] = []
    for slug, date, mf in iter_manifests():
        if since and date < since:
            continue
        with open(mf, encoding="utf-8") as f:
            lines = [json.loads(ln) for ln in f if ln.strip()]
        credits = sum(r["credits"] for r in lines if r.get("credits") is not None)
        has_credit = sum(1 for r in lines if r.get("credits") is not None)
        verbs = {r["verb"] for r in lines if r.get("verb")}
        verb = next(iter(verbs)) if len(verbs) == 1 else "(mixed)" if verbs else "(untagged)"
        runs.append(
            {
                "slug": slug,
                "date": date,
                "verb": verb,
                "credits": credits,
                "has_credit": has_credit,
                "no_credit": len(lines) - has_credit,
                "secs": round(sum(r.get("secs") or 0 for r in lines), 1),
                "calls": len(lines),
            }
        )
    return runs


# --- stats helpers ----------------------------------------------------------


def dist(values: list[float]) -> dict[str, float]:
    """median / mean / p90 / max / total / n for a list — p90 because the tail (huge
    catalogs, PDF brochures) is what blows a routine budget, not the median."""
    vs = sorted(values)
    p90 = vs[-1] if len(vs) < 2 else statistics.quantiles(vs, n=10)[8]
    return {
        "n": len(vs),
        "median": statistics.median(vs),
        "mean": statistics.mean(vs),
        "p90": p90,
        "max": vs[-1],
        "total": sum(vs),
    }


def fmt_dist(values: list[float], unit: str = "cr") -> str:
    """One-line distribution summary, or a clear empty marker."""
    if not values:
        return "  (no credit-recorded runs)"
    d = dist(values)
    return (
        f"  n={d['n']:<4} median={d['median']:.0f}{unit}  mean={d['mean']:.1f}  "
        f"p90={d['p90']:.0f}  max={d['max']:.0f}  total={d['total']:.0f}{unit}"
    )


# --- signal-tool cost (the envelope `cost` field) ---------------------------


def signal_costs(since: str | None) -> dict[str, dict[str, list[float]]]:
    """Per source_type, the cost samples grouped by native unit. {source: {unit: [vals]}}.
    A source with no cost-bearing envelope (wayback/sec/trends are free) maps to {}."""
    agg: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for fp in STORE.glob("*/signals/*/*.json"):
        parts = fp.parts
        source = parts[parts.index("signals") + 1]
        with open(fp, encoding="utf-8") as f:
            env = json.load(f)
        if since and (env.get("captured_at", "")[:10] < since):
            continue
        agg.setdefault(source, defaultdict(list))
        cost = env.get("cost")
        if isinstance(cost, dict):
            for unit, val in cost.items():
                if isinstance(val, (int, float)):
                    agg[source][unit].append(val)
    return {src: dict(units) for src, units in agg.items()}


def count_signal_captures(source: str, since: str | None) -> int:
    """How many envelopes exist for a source (cost-bearing or not) — denominator for
    'cost-bearing X/N', so a free source reads as captured-but-free, not absent."""
    n = 0
    for fp in (STORE).glob(f"*/signals/{source}/*.json"):
        if not since:
            n += 1
            continue
        with open(fp, encoding="utf-8") as f:
            if json.load(f).get("captured_at", "")[:10] >= since:
                n += 1
    return n


# --- commands ---------------------------------------------------------------


def cmd_captures(args: argparse.Namespace) -> None:
    """Firecrawl capture-credit distribution, optionally cut by verb / slug / date."""
    runs = run_records(args.since)
    recorded = [r for r in runs if r["has_credit"]]
    legacy = [r for r in runs if not r["has_credit"]]
    print("== Firecrawl capture credits ==")
    print(f"runs: {len(runs)}  (credit-recorded {len(recorded)}, legacy/no-field {len(legacy)})")
    print("overall:")
    print(fmt_dist([r["credits"] for r in recorded]))
    print("fetch-latency secs/run (Firecrawl only — NOT full session):")
    print(fmt_dist([r["secs"] for r in runs if r["secs"]], unit="s"))
    by = getattr(args, "by", None)  # the `all` parser doesn't define --by
    if by:
        print(f"\nby {by}:")
        groups: dict[str, list[float]] = defaultdict(list)
        for r in recorded:
            groups[str(r[by])].append(r["credits"])
        for key in sorted(groups, key=lambda k: -sum(groups[k])):
            print(f"  {key}")
            print("  " + fmt_dist(groups[key]).strip())


def cmd_signals(args: argparse.Namespace) -> None:
    """Signal-tool spend by source + unit. Reports each native unit; flags the FC overlap."""
    costs = signal_costs(args.since)
    print("== Signal-tool spend (by source) ==")
    fc_from_signals = 0.0
    unit_totals: dict[str, float] = defaultdict(float)
    for source in sorted(set(costs) | _known_sources()):
        n = count_signal_captures(source, args.since)
        units = costs.get(source, {})
        if not units:
            print(f"  {source:14} captures={n:<4} free")
            continue
        bits = []
        for unit, vals in units.items():
            total = sum(vals)
            unit_totals[unit] += total
            if unit == "firecrawl_credits":
                fc_from_signals += total
            money = f"${total:.3f}" if unit == "usd" else f"{total:.0f} {unit}"
            med = f"${statistics.median(vals):.3f}" if unit == "usd" else f"{statistics.median(vals):.0f}"
            bits.append(f"{money} (median {med}, n={len(vals)})")
        print(f"  {source:14} captures={n:<4} " + "; ".join(bits))
    print("\ntotals by unit: " + ", ".join(f"${v:.3f}" if u == "usd" else f"{v:.0f} {u}" for u, v in sorted(unit_totals.items())))
    if fc_from_signals:
        print(f"  ↳ {fc_from_signals:.0f} of those are Firecrawl credits (Trustpilot) — same budget as captures")


def _known_sources() -> set[str]:
    """All source_types present on disk, so free sources still show as captured-but-free."""
    return {fp.parts[fp.parts.index("signals") + 1] for fp in STORE.glob("*/signals/*/*.json")}


def cmd_all(args: argparse.Namespace) -> None:
    """The headline planning table: capture credits + signal spend + combined FC total."""
    runs = run_records(args.since)
    recorded = [r for r in runs if r["has_credit"]]
    cap_credits = sum(r["credits"] for r in recorded)
    cmd_captures(args)
    print()
    cmd_signals(args)
    sig_fc = sum(sum(vals) for units in signal_costs(args.since).values() for unit, vals in units.items() if unit == "firecrawl_credits")
    print("\n== Combined Firecrawl budget ==")
    print(f"  captures {cap_credits:.0f} + signals {sig_fc:.0f} = {cap_credits + sig_fc:.0f} FC credits (recorded)")


DISPATCH = {"all": cmd_all, "captures": cmd_captures, "signals": cmd_signals}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    for name in DISPATCH:
        p = sub.add_parser(name)
        p.add_argument("--since", help="only runs/captures on/after this YYYY-MM-DD")
        if name == "captures":
            p.add_argument("--by", choices=["verb", "slug", "date"], help="group the distribution")
    args = ap.parse_args()
    if not args.cmd:
        args = ap.parse_args(["all"])
    DISPATCH[args.cmd](args)


if __name__ == "__main__":
    main()
