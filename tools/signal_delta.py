#!/usr/bin/env python3
"""Envelope comparator — diffs two captures of the same source into axis-specific deltas, never a score.

This is [`tools/BACKLOG.md`](BACKLOG.md)'s top comparator item and the [traction approach](../_design/2026-06-15-traction-approach.md)'s
one real build. It reads the *raw* envelopes the capture tools already emit (trustpilot / serp / trends /
…) and, per `source_type`, produces per-metric deltas + comparability vetoes. It diffs raw — not a
normalized "card" layer — because drift is already absorbed at the capture tool (a reshaped upstream sets
`ok:false` + `schema_drift` and blanks parsed fields *before* any consumer reads them), so a drifted
capture reaches this comparator as a ready-made veto, and the integrity signals (templated reviews, AIO
presence, `schema_drift`, `parser_version`, Trends `peak_date`) stay directly under its eye.

Safe by construction — the properties that keep this honest:
  - **No score is expressible.** Every number is bound to one metric within one `source_type` + `subject`
    + `unit`; there is no field that combines metrics, and nothing aggregates across sources. Axis-specific
    cited evidence, never a blend.
  - **Level-read before delta.** One capture of a subject -> current values + caveats; two -> ordered deltas.
  - **A non-comparable pair is a VETO ROW with empty deltas, never a dropped row** (a silent skip hides the
    disagreement that is itself the signal).
  - **The grain + source_type + subject alignment fence is hard.** A cross-source / cross-grain / cross-subject
    pairing is a veto, never a silent average. (Unit-tested in tests/test_signal_delta.py.)

Inputs are paths — a FILE (one capture) or a DIR (a run = many captures). Both are normalized to a list of
envelopes, so the same code path serves pairwise (file vs file), run-vs-run (dir vs dir, e.g. a SERP panel
whose AIO outage veto needs every row), and multi-subject sources (one Trends envelope holds many keywords).

It is a CONSUMER: it never fetches and never writes. Captures it reads live at the company-grain path
`store/<domain>/signals/<source_type>/<captured_at>.json` (the convention in the [architecture](../_design/2026-05-30-architecture.md));
category-grain runs (SERP panels) stay in experiments/cohorts until `cohorts/` graduates.

CLI:
  python3 tools/signal_delta.py D0.json D7.json                 # pairwise (trustpilot, one serp query, …)
  python3 tools/signal_delta.py runA/ runB/ --min-gap-days 5    # run-vs-run (SERP panel; trends envelopes)

Exit codes:
  0  produced a comparison report (INCLUDING one that is all vetoes — a non-comparable pair is data)
  2  operational error (a path that doesn't exist / holds no envelopes; unreadable JSON)
  (no exit 3: this tool has no version-pinned parsed upstream; source schema_drift surfaces as a veto row,
   never the comparator's own drift.)

Source-aware branches (keyed on the envelope's `tool`): trustpilot (pairwise), serpapi (run-grained
AIO/organic), trends (multi-subject, basis-aware), wayback (per-URL presence/snapshot/content-digest over
two tenure captures — never re-fetches). Unknown source_types hit the fallback (a named veto, never a
guessed delta).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse

# Fixed grain per source_type — a stamped field, so a missing card never reads as "no demand" and the fence
# can refuse a cross-grain pairing. v1 emits only company- and category_query-grain (see the approach's #2).
GRAIN: dict[str, str] = {
    "trustpilot": "company",
    "serpapi": "category_query",
    "trends": "company",  # per-brand-keyword search interest; subject = the keyword, caller maps it to a domain
    "wayback": "page",  # per-URL archive record; subject = the URL (a page on the company's domain)
}
OUTAGE_FRACTION = 0.6  # >= this share of previously-present AIO rows blanking at once => surface-outage veto
TEMPLATE_DUPES = 2  # >= this many identical review bodies in a recent sample => templated/farmed signature


def _utc_now() -> str:
    """When the diff ran — the envelope's `captured_at`. A consumer's wall-clock, not a source date."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def canon(value: str) -> str:
    """Store-dir slug (scripts/store.py's rule): lowercase, strip scheme, dots -> dashes."""
    return re.sub(r"^https?://", "", value).strip("/").lower().replace(".", "-")


# --------------------------------------------------------------------------- subject identity
def subject_of(env: dict[str, Any]) -> str:
    """The alignment key for one capture, per source_type — what makes two captures "the same thing".

    Cross-subject pairings are refused by the fence; getting this key right is what the fence rests on.
    """
    src = env.get("tool", "")
    inp = env.get("input", {})
    if src == "trustpilot":
        return canon(inp.get("slug", "") or env.get("source", ""))
    if src == "serpapi":
        return inp.get("query", "").strip().lower()
    if src == "trends":
        return src  # a trends envelope is multi-subject; its real subjects are per-keyword (handled in-branch)
    if src == "wayback":
        return inp.get("url", "").strip().lower().rstrip("/")  # the exact URL keys the archive record
    return canon(inp.get("url", "") or inp.get("slug", "") or env.get("source", src))


def _gap_days(earlier: dict[str, Any], later: dict[str, Any]) -> float:
    t0 = datetime.strptime(earlier["captured_at"], "%Y-%m-%dT%H:%M:%SZ")
    t1 = datetime.strptime(later["captured_at"], "%Y-%m-%dT%H:%M:%SZ")
    return round((t1 - t0).total_seconds() / 86400, 2)


def _fence(earlier: dict[str, Any], later: dict[str, Any]) -> str | None:
    """The hard alignment guard: same source_type, same grain, same subject — else a veto string.

    Drift/`ok:false` at either end is also a fence stop (the capture tool already suppressed its parse).
    """
    sa, sb = earlier.get("tool"), later.get("tool")
    if sa != sb:
        return f"source_type_mismatch: {sa} vs {sb} — cross-source pairing refused"
    if GRAIN.get(sa) != GRAIN.get(sb):
        return f"grain_mismatch: {GRAIN.get(sa)} vs {GRAIN.get(sb)} — cross-grain pairing refused"
    if subject_of(earlier) != subject_of(later):
        return f"subject_mismatch: {subject_of(earlier)} vs {subject_of(later)} — cross-subject pairing refused"
    for tag, e in (("D0", earlier), ("D7", later)):
        if e.get("schema_drift"):
            return f"{tag}_schema_drift: {e['schema_drift']} — parsed fields suppressed at the capture tool; comparison void"
        if not e.get("ok", True):
            return f"{tag}_capture_not_ok — comparison void"
    return None


def _row(source_type: str, subject: str, **extra: Any) -> dict[str, Any]:
    """A comparison row skeleton — uniform shape so a consumer reads every source the same way."""
    return {"source_type": source_type, "grain": GRAIN.get(source_type, "unknown"), "subject": subject,
            "read_mode": "delta", "metrics": [], "comparability_flags": [], "vetoes": [], **extra}


# --------------------------------------------------------------------------- trustpilot branch (pairwise)
def _templating_flag(reviews: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Duplicate review BODIES in a recent sample => probable farmed/templated burst (a caveat on the delta)."""
    bodies = [(r.get("body") or "").strip().lower().rstrip(".!") for r in reviews if r.get("body")]
    dupes = len(bodies) - len(set(bodies))
    if dupes >= TEMPLATE_DUPES:
        return {"flag": "templated_reviews", "duplicate_bodies": dupes, "sample_size": len(bodies),
                "effect": "the review-count delta may be partly farmed, not organic"}
    return None


def _level_trustpilot(env: dict[str, Any]) -> dict[str, Any]:
    """One capture, no prior — current values + caveats (a baseline read before a delta exists)."""
    row = _row("trustpilot", subject_of(env), read_mode="level")
    if env.get("profile_state") != "active":
        row["vetoes"].append(f"profile_{env.get('profile_state')} — not a live profile; nothing to level-read")
        return row
    row["metrics"].append({"metric": "review_count", "basis": "cumulative_lifetime", "value": env.get("review_count"), "unit": "reviews"})
    row["metrics"].append({"metric": "trust_score", "basis": "current", "value": env.get("trust_score"), "unit": "stars(0-5)"})
    if (tf := _templating_flag(env.get("recent_reviews", []))):
        row["comparability_flags"].append(tf)
    return row


def _delta_trustpilot(earlier: dict[str, Any], later: dict[str, Any]) -> dict[str, Any]:
    """Two captures of one brand: velocity off the MONOTONE cumulative review_count, with the gap surfaced.

    reviews_last_12m is level-read only — it's a rolling window anchored to each capture's date, so diffing
    it across an uneven gap double-counts the moved left edge (it can fall while lifetime growth is positive).
    """
    subject = subject_of(later)
    if (blocked := _fence(earlier, later)):
        return _row("trustpilot", subject, vetoes=[blocked], metrics=[])

    state = later.get("profile_state")
    if state != "active":
        return _row("trustpilot", subject,
                    vetoes=[f"profile_{state}_between_captures (active at D0) — comparison void, deltas empty"])
    if later["profile_flags"].get("merged_profile") and not earlier["profile_flags"].get("merged_profile"):
        return _row("trustpilot", subject,
                    vetoes=["profile_merged_between_captures — review_count no longer apples-to-apples"])

    gap = _gap_days(earlier, later)
    delta = later["review_count"] - earlier["review_count"]
    row = _row("trustpilot", subject, gap_days=gap)
    row["metrics"].append({
        "metric": "review_count", "basis": "cumulative_lifetime (monotone)",
        "d0": earlier["review_count"], "d7": later["review_count"], "delta": delta,
        "velocity_per_day": round(delta / gap, 2) if gap else None, "unit": "reviews",
    })
    row["metrics"].append({
        "metric": "reviews_last_12m", "basis": "rolling_12m_window (anchored to each capture date)",
        "d0": earlier.get("reviews_last_12m"), "d7": later.get("reviews_last_12m"), "delta": None, "unit": "reviews",
        "note": "level-read only — the window's left edge moves between captures, so a delta double-counts it",
    })
    if (tf := _templating_flag(later.get("recent_reviews", []))):
        tf["effect"] = f"the +{delta} review delta may be partly farmed, not organic"
        row["comparability_flags"].append(tf)
    if later["profile_flags"].get("paid_profile"):
        row["comparability_flags"].append({"flag": "paid_profile", "effect": "paid placement — solicitation/surfacing caveat"})
    if earlier.get("review_count") and delta / earlier["review_count"] > 0.5:
        row["comparability_flags"].append({"flag": "bursty_growth", "effect": f"+{delta} is >50% of the D0 base over {gap}d — check for solicitation/farming"})
    return row


def branch_trustpilot(a_envs: list[dict[str, Any]], b_envs: list[dict[str, Any]]) -> dict[str, Any]:
    """Group by subject (robust to runs of many brands); delta where paired, level where solo."""
    by_a = {subject_of(e): e for e in a_envs}
    by_b = {subject_of(e): e for e in b_envs}
    rows = []
    for subj in sorted(by_a.keys() | by_b.keys()):
        if subj in by_a and subj in by_b:
            rows.append(_delta_trustpilot(by_a[subj], by_b[subj]))
        else:
            only = by_b.get(subj) or by_a[subj]
            row = _level_trustpilot(only)
            row["comparability_flags"].append({"flag": "unpaired_capture", "effect": "only one capture for this subject — level-read, no delta"})
            rows.append(row)
    return {"comparisons": rows, "run_vetoes": []}


# --------------------------------------------------------------------------- serp branch (run-grained)
def _domain_of(url: str | None) -> str | None:
    if not url:
        return None
    return re.sub(r"^www\.", "", (urlparse(url).netloc or url).lower())


def _organic_ranks(env: dict[str, Any]) -> dict[str, int]:
    out: dict[str, int] = {}
    for r in env.get("organic_results", []):
        d = _domain_of(r.get("link") or r.get("displayed_link"))
        if d and d not in out:
            out[d] = r.get("position")
    return out


def _aio_present(env: dict[str, Any]) -> bool:
    return bool(env.get("ai_overview_present")) and not env.get("ai_overview_skipped")


def _delta_serp_pair(earlier: dict[str, Any], later: dict[str, Any]) -> dict[str, Any]:
    """One query: organic rank movement AND AIO presence movement — diffed INDEPENDENTLY, never blended
    (they are different stability surfaces; their disagreement is the AIO-instability tell)."""
    subject = subject_of(later)
    if (blocked := _fence(earlier, later)):
        return _row("serpapi", subject, vetoes=[blocked])
    ranks0, ranks7 = _organic_ranks(earlier), _organic_ranks(later)
    row = _row("serpapi", subject, gap_days=_gap_days(earlier, later))
    row["metrics"].append({
        "metric": "organic_rank", "basis": "domain -> first-position in top-10",
        "moved": {d: {"d0": ranks0[d], "d7": ranks7[d]} for d in ranks0.keys() & ranks7.keys() if ranks0[d] != ranks7[d]},
        "dropped": sorted(ranks0.keys() - ranks7.keys()), "new": sorted(ranks7.keys() - ranks0.keys()), "unit": "rank",
    })
    aio0, aio7 = _aio_present(earlier), _aio_present(later)
    row["metrics"].append({
        "metric": "aio_presence", "basis": "AI Overview rendered for this query",
        "d0": aio0, "d7": aio7, "movement": "dropped" if aio0 and not aio7 else "appeared" if aio7 and not aio0 else "stable",
        "d7_unavailable_reason": later.get("ai_overview_unavailable_reason"), "unit": "present(bool)",
    })
    return row


def branch_serp(a_envs: list[dict[str, Any]], b_envs: list[dict[str, Any]]) -> dict[str, Any]:
    """Align queries across two runs, diff each, THEN apply the run-level AIO batch-outage veto.

    The veto is inherently run-level: a high fraction of previously-present AIO rows blanking AT ONCE is a
    probable surface outage (live-observed at 6/7 and 11/12), not N independent real drops — it can't be
    decided from one pair. A lone drop (the real 1/4) stays a genuine per-query movement.
    """
    by_a = {subject_of(e): e for e in a_envs}
    by_b = {subject_of(e): e for e in b_envs}
    rows = []
    for subj in sorted(by_a.keys() | by_b.keys()):
        if subj in by_a and subj in by_b:
            rows.append(_delta_serp_pair(by_a[subj], by_b[subj]))
        else:
            row = _row("serpapi", subj, read_mode="level",
                       comparability_flags=[{"flag": "unpaired_capture", "effect": "query in only one run — no delta"}])
            rows.append(row)

    paired = [r for r in rows if r["read_mode"] == "delta" and not r["vetoes"]]
    present_d0 = [r for r in paired if _aio_metric(r)["d0"]]
    dropped = [r for r in paired if _aio_metric(r)["movement"] == "dropped"]
    frac = len(dropped) / len(present_d0) if present_d0 else 0.0
    run_vetoes = []
    if present_d0 and frac >= OUTAGE_FRACTION:
        affected = [r["subject"] for r in dropped]
        run_vetoes.append(
            f"probable_aio_surface_outage: {len(dropped)}/{len(present_d0)} previously-present AIO rows blanked "
            f"at once ({frac:.0%} >= {OUTAGE_FRACTION:.0%}) — flag the surface, do NOT report "
            f"{len(dropped)} independent real drops. Affected: {affected}"
        )
        for r in dropped:
            _aio_metric(r)["movement"] = "dropped_OUTAGE_SUSPECTED"
    return {"comparisons": rows, "run_vetoes": run_vetoes}


def _aio_metric(row: dict[str, Any]) -> dict[str, Any]:
    return next(m for m in row["metrics"] if m["metric"] == "aio_presence")


# --------------------------------------------------------------------------- trends branch (multi-subject, basis-aware)
def _series_window(item: dict[str, Any]) -> tuple[str, str] | None:
    pts = item.get("points") or []
    return (pts[0]["date"], pts[-1]["date"]) if pts else None


def _delta_trends_keyword(earlier: dict[str, Any], later: dict[str, Any], subject: str) -> dict[str, Any]:
    """One keyword across two Trends captures. The SAFE read is each capture's own within-keyword trajectory
    (both windows share that capture's peak normalization). A point-LEVEL delta is only valid when both
    captures' `peak_date` falls inside their date-overlap — same normalization anchor — else a veto."""
    row = _row("trends", subject)
    if not earlier.get("ok") or not later.get("ok"):
        row["vetoes"].append("a keyword capture failed/skipped (ok:false) — comparison void")
        return row

    # Always emit the within-keyword trajectory — a level-read of the robust signal, always comparable.
    row["metrics"].append({
        "metric": "within_capture_trajectory", "basis": "each capture's own 7d-vs-prior-7d (peak-normalized)",
        "d0": {"delta_7d_pct": earlier.get("delta_7d_vs_prior_7d_pct"), "trajectory": earlier.get("trajectory")},
        "d7": {"delta_7d_pct": later.get("delta_7d_vs_prior_7d_pct"), "trajectory": later.get("trajectory")},
        "unit": "pct / label",
    })

    # Basis-aware gate on any point-level (cross-capture magnitude) read.
    win0, win7 = _series_window(earlier), _series_window(later)
    if not win0 or not win7:
        row["vetoes"].append("renorm_basis_unknown: a capture has no points to bound its window")
        return row
    lo, hi = max(win0[0], win7[0]), min(win0[1], win7[1])
    if lo > hi:
        row["vetoes"].append(f"no_date_overlap: D0 {win0} vs D7 {win7} — point levels not comparable")
        return row
    peak0, peak7 = earlier.get("peak_date"), later.get("peak_date")
    if not (peak0 and peak7 and lo <= peak0 <= hi and lo <= peak7 <= hi):
        row["vetoes"].append(
            f"renorm_basis_mismatch: a peak_date falls outside the overlap [{lo}..{hi}] "
            f"(D0 peak {peak0}, D7 peak {peak7}) — pytrends pins each 0-100 to its own peak, so point levels "
            f"are on different scales. Trajectory above is still valid."
        )
        return row
    row["metrics"].append({
        "metric": "peak_value", "basis": f"shared peak-normalized scale; both peaks inside overlap [{lo}..{hi}]",
        "d0": earlier.get("peak_value"), "d7": later.get("peak_value"),
        "delta": round(later["peak_value"] - earlier["peak_value"], 2), "unit": "interest(0-100)",
    })
    return row


def branch_trends(a_envs: list[dict[str, Any]], b_envs: list[dict[str, Any]]) -> dict[str, Any]:
    """A Trends envelope is multi-subject — flatten its `series` to {keyword: item} across both sides, align."""
    def flat(envs: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
        out: dict[str, dict[str, Any]] = {}
        for e in envs:
            for item in e.get("series", []):
                out[(item.get("query") or item.get("label") or "").strip().lower()] = item
        return out

    fa, fb = flat(a_envs), flat(b_envs)
    rows = [_delta_trends_keyword(fa[k], fb[k], k) for k in sorted(fa.keys() & fb.keys())]
    for k in sorted(fa.keys() ^ fb.keys()):
        rows.append(_row("trends", k, read_mode="level",
                         comparability_flags=[{"flag": "unpaired_capture", "effect": "keyword in only one capture — no delta"}]))
    return {"comparisons": rows, "run_vetoes": []}


# --------------------------------------------------------------------------- wayback branch (pairwise, per-URL)
def _latest_digest(env: dict[str, Any]) -> str | None:
    """The content digest of the most-recent archived snapshot — the Wayback CDX hash, captured already
    (no re-fetch). A change in this between two captures means the archive holds new page content."""
    snaps = env.get("snapshots") or []
    if not snaps:
        return None
    return max(snaps, key=lambda s: s.get("timestamp", "")).get("digest")


def _delta_wayback(earlier: dict[str, Any], later: dict[str, Any]) -> dict[str, Any]:
    """Two tenure captures of one URL: archive presence, snapshot growth, last-seen movement, content-digest
    change — a thin run-to-run read over the digests `wayback.py` already captured (never re-fetches). The
    per-snapshot content diff stays `wayback.py diff`'s job; this is movement between OUR capture runs."""
    subject = subject_of(later)
    if (blocked := _fence(earlier, later)):
        return _row("wayback", subject, vetoes=[blocked])
    e_present, l_present = earlier.get("snapshot_count", 0) > 0, later.get("snapshot_count", 0) > 0
    row = _row("wayback", subject, gap_days=_gap_days(earlier, later))
    row["metrics"].append({
        "metric": "archive_presence", "basis": "URL has >=1 archived snapshot",
        "d0": e_present, "d7": l_present,
        "movement": "lost" if e_present and not l_present else "gained" if l_present and not e_present else "stable",
        "unit": "present(bool)",
    })
    row["metrics"].append({
        "metric": "snapshot_count", "basis": "distinct-content captures (CDX collapse=digest)",
        "d0": earlier.get("snapshot_count"), "d7": later.get("snapshot_count"),
        "delta": (later.get("snapshot_count") or 0) - (earlier.get("snapshot_count") or 0), "unit": "snapshots",
    })
    row["metrics"].append({
        "metric": "last_seen", "basis": "latest archived snapshot timestamp",
        "d0": earlier.get("last_seen"), "d7": later.get("last_seen"),
        "advanced": bool(later.get("last_seen") and earlier.get("last_seen") and later["last_seen"] > earlier["last_seen"]),
        "unit": "timestamp",
    })
    e_dig, l_dig = _latest_digest(earlier), _latest_digest(later)
    row["metrics"].append({
        "metric": "content_digest", "basis": "digest of the most-recent archived snapshot (no re-fetch)",
        "d0": e_dig, "d7": l_dig, "changed": bool(e_dig and l_dig and e_dig != l_dig), "unit": "sha-ish digest",
    })
    return row


def branch_wayback(a_envs: list[dict[str, Any]], b_envs: list[dict[str, Any]]) -> dict[str, Any]:
    """Group by URL; delta where paired, level (presence + current digest) where solo."""
    by_a = {subject_of(e): e for e in a_envs}
    by_b = {subject_of(e): e for e in b_envs}
    rows = []
    for subj in sorted(by_a.keys() | by_b.keys()):
        if subj in by_a and subj in by_b:
            rows.append(_delta_wayback(by_a[subj], by_b[subj]))
        else:
            env = by_b.get(subj) or by_a[subj]
            rows.append(_row("wayback", subj, read_mode="level",
                             metrics=[{"metric": "archive_presence", "value": env.get("snapshot_count", 0) > 0,
                                       "digest": _latest_digest(env), "unit": "present(bool)"}],
                             comparability_flags=[{"flag": "unpaired_capture", "effect": "one capture for this URL — no delta"}]))
    return {"comparisons": rows, "run_vetoes": []}


# --------------------------------------------------------------------------- fallback
def branch_fallback(a_envs: list[dict[str, Any]], b_envs: list[dict[str, Any]]) -> dict[str, Any]:
    """Unknown source_type: a named veto, never a guessed delta over a payload the comparator can't read."""
    tool = (a_envs or b_envs)[0].get("tool", "?")
    return {"comparisons": [_row(tool, subject_of((a_envs or b_envs)[0]),
                                 vetoes=[f"no source-aware delta for '{tool}' — add a branch or compare by hand"])],
            "run_vetoes": []}


DISPATCH: dict[str, Callable[[list[dict[str, Any]], list[dict[str, Any]]], dict[str, Any]]] = {
    "trustpilot": branch_trustpilot,
    "serpapi": branch_serp,
    "trends": branch_trends,
    "wayback": branch_wayback,
}


# --------------------------------------------------------------------------- driver
def _load_envelopes(path: Path) -> list[dict[str, Any]]:
    """A path -> list of envelopes. A file is one capture; a dir is a run (recursive *.json, sorted)."""
    if path.is_dir():
        files = sorted(path.rglob("*.json"))
    elif path.is_file():
        files = [path]
    else:
        raise FileNotFoundError(f"{path} is neither a file nor a directory")
    envs = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            envs.append(json.load(fh))
    if not envs:
        raise ValueError(f"{path} holds no JSON envelopes")
    return envs


def compare(a_envs: list[dict[str, Any]], b_envs: list[dict[str, Any]], min_gap_days: float = 0.0) -> dict[str, Any]:
    """Group both sides by source_type, DISPATCH each branch, merge. The grouping IS the first fence:
    only same-source envelopes ever reach the same branch."""
    by_src_a: dict[str, list[dict[str, Any]]] = {}
    by_src_b: dict[str, list[dict[str, Any]]] = {}
    for e in a_envs:
        by_src_a.setdefault(e.get("tool", "?"), []).append(e)
    for e in b_envs:
        by_src_b.setdefault(e.get("tool", "?"), []).append(e)

    comparisons: list[dict[str, Any]] = []
    run_vetoes: list[str] = []
    for src in sorted(set(by_src_a) | set(by_src_b)):
        branch = DISPATCH.get(src, branch_fallback)
        result = branch(by_src_a.get(src, []), by_src_b.get(src, []))
        comparisons.extend(result["comparisons"])
        run_vetoes.extend(result["run_vetoes"])

    # min-gap-days is a comparability caveat on every delta row, never a veto (a short gap is noisier, not void).
    if min_gap_days:
        for row in comparisons:
            if row["read_mode"] == "delta" and 0 < row.get("gap_days", 0) < min_gap_days:
                row["comparability_flags"].append(
                    {"flag": "short_gap", "effect": f"gap {row['gap_days']}d < {min_gap_days}d — delta may be capture noise"})

    return {"comparisons": comparisons, "run_vetoes": run_vetoes,
            "source_types": sorted({r["source_type"] for r in comparisons})}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("a", help="D0 capture: a file (one capture) or a dir (a run)")
    p.add_argument("b", help="D7 capture: a file or a dir")
    p.add_argument("--align-on", default="subject", choices=["subject"],
                   help="alignment key (only 'subject' in v1 — source-type defines what that means)")
    p.add_argument("--min-gap-days", type=float, default=0.0,
                   help="flag deltas whose capture gap is shorter than this as possible noise (a caveat, not a veto)")
    args = p.parse_args()

    try:
        a_envs = _load_envelopes(Path(args.a))
        b_envs = _load_envelopes(Path(args.b))
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
        sys.stderr.write(f"Error reading inputs: {e}\n")
        sys.exit(2)

    payload = compare(a_envs, b_envs, min_gap_days=args.min_gap_days)
    envelope = {
        "tool": "signal_delta",
        "source": "local (consumer — diffs tools/ capture envelopes, fetches nothing)",
        "captured_at": _utc_now(),  # when the diff ran
        "ok": True,
        "input": {"a": args.a, "b": args.b, "align_on": args.align_on, "min_gap_days": args.min_gap_days},
        "schema_drift": [],  # always [] — no parsed upstream; source drift surfaces as a veto row
        **payload,
    }
    print(json.dumps(envelope, indent=2))


if __name__ == "__main__":
    main()
