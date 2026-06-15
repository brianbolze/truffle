#!/usr/bin/env python3
"""Google Trends (pytrends) — solo-per-brand search-interest capture, captured not judged.

Give it a LIST of keywords; it captures each one's Google Trends interest-over-time series in
its OWN single-keyword pytrends call, sequentially, and emits one envelope with a per-keyword
`series` payload. This tool OWNS THE LOOP on purpose — unlike serpapi/exa (one input per call),
the hard-won value here is the solo-per-brand capture shape plus the rate-limit management
(sequential calls, multi-second sleeps, a single 429 retry). Splitting to one-keyword-per-
invocation would orphan all of that onto the caller.

Why solo-per-brand (the load-bearing methodology — see trends.md + the primer):
  pytrends returns a 0-100 daily score normalized to the daily max ACROSS THE BATCH, not to each
  keyword's own peak. Batch brands of different magnitudes together and the big ones crush the
  small ones — the same brand swung 10-40x run-to-run on batch composition (Hone Health: 4.37 in
  a Function-Health-dominated batch vs 61.2 solo). So each keyword gets its own call; its series
  is normalized to its own peak. The cost: scores are NOT cross-keyword comparable for absolute
  volume — they're good for TIER (mean_to_peak_ratio = sustained vs spiky) and TRAJECTORY
  (within-keyword delta), not "brand X is N times brand Y." That caveat is surfaced in the
  payload (`note` + per-item `mean_to_peak_ratio`) so a consumer can't misread it.

Generic on purpose: no cohort / Notion / vertical / importance-filter baked in (the source script
read a Notion-derived cohort and filtered by importance — all stripped). The tool captures the
keywords it's handed and surfaces the raw signal. WHICH names to override or skip for common-word
collisions (Eden -> biblical noise, Fridays -> day-of-week, Gala -> events) is the CALLER's
judgment, not the tool's — supply a disambiguating query via the `label::query` form.

CLI:
  python3 tools/trends.py "Hone Health" "AgelessRx" "Lifeforce"
  python3 tools/trends.py "Hims & Hers::Hims"          # label kept clean, query disambiguated
  python3 tools/trends.py "Eden::Eden hormone therapy" "Ro::ro.co"   # collision / too-short overrides
  python3 tools/trends.py "Hone Health" --geo US --timeframe "today 12-m" --sleep 8

A positional keyword is the query (and label). Append `::<query>` to override the query while
keeping a clean display label — the only place this tool accepts the optional {label, query} shape.

Exit codes:
  0  clean capture (INCLUDING zero/near-zero series — "rarely searched by name" is data, not failure;
     AND partial runs where some keywords failed/were skipped — the captured rest is still emitted)
  2  total failure: pytrends unavailable, or every attempted keyword failed even after its retry
     (endpoint down / hard rate-limit). Partial JSON is still printed.
  (no exit 3: pytrends is not a version-pinned parsed surface. If Google changes the unauth endpoint
   it BREAKS -> exit 2 transport, it doesn't silently reshape. `schema_drift` stays [] for envelope
   uniformity; the capture methodology is carried as payload provenance `method`/`method_version`.)

No API key — pytrends is the unofficial/unauthed Google Trends client. No SLA; it breaks when Google
changes the endpoint. Don't migrate this signal to paid SerpAPI Trends ($50/mo) without a Brian
decision — same underlying data + batch-normalization, only uptime differs (see trends.md).

method_version: v2 — bump on an intentional capture-methodology change (e.g. solo -> something else),
never to paper over a transient pytrends hiccup.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from typing import Any

METHOD = "solo-per-brand"
METHOD_VERSION = "v2"
DEFAULT_TIMEFRAME = "today 3-m"  # daily points; the validated default. Other timeframes change point granularity.
DEFAULT_GEO = "US"
DEFAULT_SLEEP_S = 7.0  # 5s is borderline per the rate-limit INVARIANT; 7-8s clears most 429s.
RETRY_SLEEP_S = 30.0  # single back-off retry — a 2nd failure is usually keyword-level limiting; waiting longer won't help.
MIN_QUERY_LEN = 4  # GTrends needs >=4-char keywords; "Ro"/"Ulo" return noise. Caller overrides via `::ro.co`.
TRAJECTORY_RISING_RATIO = 1.20
TRAJECTORY_FADING_RATIO = 0.80

NORMALIZATION_NOTE = (
    "Solo-per-brand: each keyword is normalized to its OWN peak day in the window (pytrends' 0-100 "
    "is per-batch; with batch size 1 it's per-keyword). Scores are within-keyword — NOT cross-keyword "
    "comparable for absolute search volume. Read mean_to_peak_ratio for tier (sustained vs spiky) and "
    "delta_7d_vs_prior_7d_pct for trajectory. Trailing-window stats assume the default daily 'today 3-m' "
    "granularity; a coarser timeframe reinterprets them as last-N-points."
)


def _utc_now() -> str:
    """This invocation's capture time, UTC ISO 8601 — the envelope's `captured_at` (the run's start).

    Per-keyword fetches land seconds-to-minutes apart (sleeps + 429 retries), so each `series` item
    carries its OWN `captured_at`; the library rule that source-specific times live inside payload
    items, not lifted to the envelope, applies even though the "source date" here is our own per-call
    wall-clock rather than a date Google reports.
    """
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_keyword(arg: str) -> dict[str, str]:
    """A positional keyword -> {label, query}. `Label::query` splits; a plain string is both.

    `::` is the override seam: it lets a caller keep a clean display label while disambiguating a
    collision-prone or too-short name ('Hims & Hers::Hims', 'Ro::ro.co'). `::` effectively never
    occurs inside a brand name, so it's a safe separator. Choosing WHICH names need it is the
    caller's judgment — the tool just captures what each side resolves to.
    """
    if "::" in arg:
        label, query = arg.split("::", 1)
        return {"label": label.strip(), "query": query.strip()}
    arg = arg.strip()
    return {"label": arg, "query": arg}


def fetch_series(pytrends: Any, query: str, timeframe: str, geo: str) -> Any:
    """One solo pytrends call -> the keyword's interest-over-time pandas Series, or None if empty.

    `interest_over_time()` returns a frame with the keyword column + an `isPartial` flag column; we
    take the keyword column (the most recent point may be a partial period — kept, as the source did).
    """
    pytrends.build_payload([query], timeframe=timeframe, geo=geo)
    df = pytrends.interest_over_time()
    if df is None or df.empty or query not in df.columns:
        return None
    return df[query]


def _trajectory_label(ratio: float | None) -> str:
    if ratio is None:
        return "unknown"
    if ratio >= TRAJECTORY_RISING_RATIO:
        return "rising"
    if ratio <= TRAJECTORY_FADING_RATIO:
        return "fading"
    return "flat"


def summarize_series(item: dict[str, str], series: Any, captured_at: str) -> dict[str, Any]:
    """A captured Series -> the per-keyword payload entry: raw `points` + tier/trajectory convenience.

    Emits the raw daily `points` (the actual capture — a consumer can recompute any window) alongside
    two curated, within-keyword reads the primer endorses: `mean_to_peak_ratio` (tier: sustained vs
    spiky) and `delta_7d_vs_prior_7d_pct` + `trajectory` (within-keyword momentum). Deliberately does
    NOT emit tiers or cross-keyword rankings — those are cohort-relative judgments for the consumer.
    A flat-zero series is a valid capture (rarely-searched brand), not a failure.
    """
    points = [{"date": idx.strftime("%Y-%m-%d"), "value": int(v)} for idx, v in series.items()]
    peak = float(series.max())
    # peak_date is the per-keyword normalization ANCHOR: pytrends pins this keyword's 0-100 scale to its
    # own peak day, so a point-level value is only comparable across captures that share that anchor. The
    # comparator (signal_delta.py) reads peak_date to veto a renorm-basis mismatch between two captures.
    peak_date = series.idxmax().strftime("%Y-%m-%d") if peak > 0 else None
    mean = float(series.mean())
    mean_to_peak = round(mean / peak, 3) if peak > 0 else None

    # Within-keyword trajectory: last 7 points vs the prior 7. Both windows share the same per-keyword
    # peak normalization, so the delta is robust where absolute magnitude isn't. Needs >=14 points.
    delta_pct: float | None = None
    ratio: float | None = None
    if len(series) >= 14:
        recent = float(series.tail(7).mean())
        prior = float(series.iloc[-14:-7].mean())
        if prior > 0:
            ratio = recent / prior
            delta_pct = round((ratio - 1) * 100, 1)

    return {
        **item,
        "captured_at": captured_at,
        "ok": True,
        "peak_value": round(peak, 2),  # the keyword's peak 0-100 in-window (was `peak`); pairs with peak_date
        "peak_date": peak_date,  # the per-keyword normalization anchor — signal_delta's basis-aware veto reads it
        "mean": round(mean, 2),
        "mean_to_peak_ratio": mean_to_peak,  # tier proxy: ~sustained (high) vs spiky (low)
        "delta_7d_vs_prior_7d_pct": delta_pct,  # within-keyword momentum; null if <14 points or prior==0
        "trajectory": _trajectory_label(ratio),
        "points": points,  # raw daily 0-100 — the actual capture; everything above is derived from it
    }


def capture(
    keywords: list[dict[str, str]],
    timeframe: str = DEFAULT_TIMEFRAME,
    geo: str = DEFAULT_GEO,
    sleep_s: float = DEFAULT_SLEEP_S,
) -> tuple[dict[str, Any], int]:
    """Full pipeline: loop the keywords solo, sequentially -> the shared envelope + `series` payload.

    Returns (envelope, attempted_count). Sequential with sleeps between calls and a single 30s retry
    per keyword (carried gotcha: pytrends rate-limits at ~20 calls/min). A too-short query is skipped
    with a reason rather than fetched (GTrends needs >=4 chars). Raising only happens if pytrends
    itself is unavailable — main() maps that to exit 2.
    """
    try:
        from pytrends.request import TrendReq
    except ImportError as exc:  # surfaced loud as transport-class — the unofficial client isn't installed
        raise RuntimeError("pytrends not installed — run: pip install pytrends") from exc

    run_captured_at = _utc_now()
    pytrends = TrendReq(hl="en-US", tz=360, timeout=(10, 30))

    series_out: list[dict[str, Any]] = []
    fetch_errors: list[dict[str, str]] = []
    attempted = 0
    captured = 0

    for i, item in enumerate(keywords, 1):
        label, query = item["label"], item["query"]
        if len(query) < MIN_QUERY_LEN:
            sys.stderr.write(f"  [{i}/{len(keywords)}] {label!r}: query {query!r} too short — skipped\n")
            series_out.append(
                {
                    **item,
                    "captured_at": _utc_now(),
                    "ok": False,
                    "reason": f"query shorter than {MIN_QUERY_LEN} chars — GTrends won't match (override via '{label}::<longer query>')",
                }
            )
            continue

        attempted += 1
        sys.stderr.write(f"  [{i}/{len(keywords)}] {label:30s} query={query!r}\n")
        series = None
        try:
            series = fetch_series(pytrends, query, timeframe, geo)
        except Exception as exc:  # transient 429 / network — one back-off retry, then give up on this keyword
            sys.stderr.write(f"    fetch error: {exc}; retrying after {RETRY_SLEEP_S}s\n")
            time.sleep(RETRY_SLEEP_S)
            try:
                series = fetch_series(pytrends, query, timeframe, geo)
            except Exception as exc2:
                fetch_errors.append({"label": label, "query": query, "error": str(exc2)})
                sys.stderr.write(f"    retry failed: {exc2}\n")

        if series is not None:
            captured += 1
            series_out.append(summarize_series(item, series, _utc_now()))
        elif not any(e["query"] == query for e in fetch_errors):
            # pytrends returned an empty frame (no error raised) — genuinely no data for this keyword.
            series_out.append({**item, "captured_at": _utc_now(), "ok": False, "reason": "pytrends returned an empty series"})
        else:
            series_out.append({**item, "captured_at": _utc_now(), "ok": False, "reason": "fetch failed after retry (see fetch_errors)"})

        if i < len(keywords):
            time.sleep(sleep_s)

    envelope: dict[str, Any] = {
        # --- shared envelope (reserved keys, identical across the tools/ library) ---
        "tool": "trends",
        "source": "trends.google.com",  # the external system hit (via the unofficial pytrends client)
        "captured_at": run_captured_at,  # the RUN's start; per-keyword times live inside each `series` item
        "ok": captured == len(keywords),  # clean iff every keyword yielded a series (no errors, no skips)
        "input": {"keywords": keywords, "timeframe": timeframe, "geo": geo, "sleep_seconds": sleep_s},
        "schema_drift": [],  # always [] — pytrends has no version-pinned parser; kept for uniformity (no exit 3)
        # NB: no `parser_version` (not a parsed surface) and no `cost` (pytrends is free/unmetered).
        # --- payload, beside the spine ---
        "method": METHOD,  # capture-methodology provenance, in place of parser_version
        "method_version": METHOD_VERSION,
        "timeframe": timeframe,
        "geo": geo,
        "note": NORMALIZATION_NOTE,  # the cross-keyword-incomparability caveat, made legible in-band
        "keywords_in_scope": len(keywords),
        "keywords_captured": captured,
        "fetch_errors": fetch_errors,
        "series": series_out,
    }
    return envelope, attempted


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("keywords", nargs="+", help="Keywords to capture. Plain string = label+query; 'Label::query' overrides the query.")
    p.add_argument("--geo", default=DEFAULT_GEO, help=f"Google Trends geo (default: {DEFAULT_GEO}; '' = worldwide)")
    p.add_argument("--timeframe", default=DEFAULT_TIMEFRAME, help=f"GTrends timeframe (default: {DEFAULT_TIMEFRAME!r}; daily points)")
    p.add_argument("--sleep", type=float, default=DEFAULT_SLEEP_S, help=f"Seconds between sequential calls (default: {DEFAULT_SLEEP_S})")
    args = p.parse_args()

    keywords = [parse_keyword(k) for k in args.keywords]
    sys.stderr.write(f"trends: {len(keywords)} keyword(s), solo-per-brand, geo={args.geo}, sleep={args.sleep}s\n")

    try:
        result, attempted = capture(keywords, timeframe=args.timeframe, geo=args.geo, sleep_s=args.sleep)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(2)

    print(json.dumps(result, indent=2))

    # Total failure (tried >=1 keyword, captured none) -> transport-class exit 2. Partial runs exit 0:
    # the captured keywords are real signal, and per-item ok=false + fetch_errors carry the gaps.
    if attempted > 0 and result["keywords_captured"] == 0:
        sys.exit(2)


if __name__ == "__main__":
    main()
