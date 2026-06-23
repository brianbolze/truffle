#!/usr/bin/env python3
"""Probe #1 — de-risk tools/signal_delta.py BEFORE building it (gates that build).

Throwaway prototype (experiments/ is exempt from house style). Proves, on real cached SERP
captures + faithful Trustpilot fixtures, the three things the comparator's correctness hinges on:

  1. PATH ROUND-TRIP   persist a D0 envelope to the convention path, then *discover + read it
                       back* (glob the signals dir, sort by captured_at) to diff vs D7 — i.e.
                       "where did D0 go", not two files handed over in one session.
  2. TRUSTPILOT BRANCH  velocity off cumulative review_count (NOT reviews_last_12m — the rolling
                       window moves and flips the sign); removed/templated profiles become VETO
                       ROWS with empty deltas, never dropped rows.
  3. SERP AIO VETO     organic rank + AIO presence diffed INDEPENDENTLY; the batch-outage veto
                       fires on a *high fraction* of simultaneous AIO drops (probable surface
                       outage) but stays silent on a lone real drop — the 6/7-vs-1/4 discrimination.

Pass = the diff reads cleanly end-to-end AND the vetoes catch the real failure signatures.

Run:  python3 experiments/2026-06-15-signal-delta-trustpilot/probe.py
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures" / "trustpilot"
OUT = HERE / "_out"  # gitignored scratch; the round-trip store roots here
# Real cached SERP captures — same 4 telehealth queries, 3 days apart (no spend).
SERP_D0_DIR = HERE.parent / "2026-06-08-serp-intent-telehealth-smoke" / "captures"
SERP_D7_DIR = HERE.parent / "2026-06-11-serp-intent-telehealth-repeat" / "captures"

OUTAGE_FRACTION = 0.6  # >= this share of previously-present AIO rows dropping at once => surface-outage veto


# --------------------------------------------------------------------------- helpers
def canon(domain: str) -> str:
    """Store-dir slug, the scripts/store.py rule: lowercase, dots -> dashes (honehealth.com -> honehealth-com)."""
    return re.sub(r"^https?://", "", domain).strip("/").lower().replace(".", "-")


def load(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# --------------------------------------------------------------------------- the path convention
def persist(env: dict, root: Path) -> Path:
    """Write a capture verbatim to  <root>/store/<domain>/signals/<source_type>/<captured_at>.json.

    This IS the v1 storage commitment (a path, no machinery). domain = the capture's subject identity;
    source_type = the tool. captured_at (the envelope's, not now()) names the file so D0 and D7 sort.
    """
    domain = canon(env["input"].get("slug") or env["input"].get("domain") or env["source"])
    source_type = env["tool"]
    stamp = env["captured_at"].replace(":", "").replace("-", "")  # filesystem-safe
    dest = root / "store" / domain / "signals" / source_type / f"{stamp}.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(env, f, indent=2)
    return dest


def discover(root: Path, domain: str, source_type: str) -> list[dict]:
    """Find every persisted capture for one subject+source, oldest first — the comparator's input side."""
    sig_dir = root / "store" / canon(domain) / "signals" / source_type
    envs = [load(p) for p in sig_dir.glob("*.json")]
    return sorted(envs, key=lambda e: e["captured_at"])


# --------------------------------------------------------------------------- trustpilot branch
def _non_comparable(d0: dict, d7: dict) -> str | None:
    """Hard fences before any delta — a fail here is a veto row, never a silent skip or a number."""
    s0 = canon(d0["input"]["slug"])
    s7 = canon(d7["input"]["slug"])
    if s0 != s7:
        return f"subject_mismatch: {s0} != {s7} (cross-subject pairing refused)"
    for tag, e in (("D0", d0), ("D7", d7)):
        if e.get("schema_drift"):
            return f"{tag}_schema_drift: {e['schema_drift']} (drift absorbed at capture tool — parsed fields suppressed)"
        if not e.get("ok", True):
            return f"{tag}_capture_not_ok"
    return None


def templating_flag(reviews: list[dict]) -> dict | None:
    """Duplicate/near-duplicate review BODIES => probable farmed/templated burst (integrity caveat on the delta)."""
    bodies = [(r.get("body") or "").strip().lower().rstrip(".!") for r in reviews if r.get("body")]
    if not bodies:
        return None
    dupes = len(bodies) - len(set(bodies))
    if dupes >= 2:  # 2+ identical bodies in a small recent sample is the farmed signature
        return {"flag": "templated_reviews", "duplicate_bodies": dupes, "sample_size": len(bodies)}
    return None


def diff_trustpilot(d0: dict, d7: dict) -> dict:
    """Trustpilot source branch: level-read + delta with integrity vetoes. Every number bound to one
    metric within source_type=trustpilot — a score is not expressible here."""
    subject = canon(d7["input"]["slug"])
    out: dict = {"source_type": "trustpilot", "grain": "company", "subject": subject,
                 "read_mode": "delta", "comparisons": [], "comparability_flags": [], "vetoes": []}

    blocker = _non_comparable(d0, d7)
    if blocker:
        out["vetoes"].append(blocker)
        return out

    # Subject became non-comparable between captures (removed / merged / not a live profile).
    state7 = d7["profile_state"]
    if state7 != "active":
        out["vetoes"].append(f"profile_{state7}_between_captures (was active at D0) — comparison void, deltas empty")
        return out
    if d7["profile_flags"].get("merged_profile") and not d0["profile_flags"].get("merged_profile"):
        out["vetoes"].append("profile_merged_between_captures — review_count no longer apples-to-apples")
        return out

    # --- the delta, on the MONOTONE cumulative count, with the gap surfaced ---
    from datetime import datetime
    t0 = datetime.strptime(d0["captured_at"], "%Y-%m-%dT%H:%M:%SZ")
    t7 = datetime.strptime(d7["captured_at"], "%Y-%m-%dT%H:%M:%SZ")
    gap_days = round((t7 - t0).total_seconds() / 86400, 2)
    rc0, rc7 = d0["review_count"], d7["review_count"]
    delta = rc7 - rc0
    out["comparisons"].append({
        "metric": "review_count",
        "basis": "cumulative_lifetime (monotone)",
        "d0": rc0, "d7": rc7, "delta": delta,
        "velocity_per_day": round(delta / gap_days, 2) if gap_days else None,
        "gap_days": gap_days,
        "unit": "reviews",
    })
    # reviews_last_12m is a rolling window anchored to capture date — LEVEL-READ ONLY, never diffed.
    out["comparisons"].append({
        "metric": "reviews_last_12m",
        "basis": "rolling_12m_window (anchored to each capture date)",
        "d0": d0["reviews_last_12m"], "d7": d7["reviews_last_12m"],
        "delta": None,
        "note": "NOT diffed — the window's left edge moves between captures, so a delta double-counts the moved edge. Level-read only.",
    })

    # --- comparability flags (caveats on the delta, not vetoes) ---
    tf = templating_flag(d7.get("recent_reviews", []))
    if tf:
        out["comparability_flags"].append({**tf, "effect": f"the +{delta} review delta may be partly farmed, not organic"})
    if d7["profile_flags"].get("paid_profile"):
        out["comparability_flags"].append({"flag": "paid_profile", "effect": "paid placement — surfacing/solicitation caveat"})
    if d0["review_count"] and delta / d0["review_count"] > 0.5:
        out["comparability_flags"].append({"flag": "bursty_growth", "effect": f"+{delta} is >50% of the D0 base over {gap_days}d — check for solicitation/farming"})
    return out


# --------------------------------------------------------------------------- serp branch (run-grained)
def domain_of(url: str | None) -> str | None:
    if not url:
        return None
    host = urlparse(url).netloc or url
    return re.sub(r"^www\.", "", host.lower())


def organic_rank_map(env: dict) -> dict[str, int]:
    out: dict[str, int] = {}
    for r in env.get("organic_results", []):
        d = domain_of(r.get("link") or r.get("displayed_link"))
        if d and d not in out:
            out[d] = r.get("position")
    return out


def diff_serp_pair(d0: dict, d7: dict) -> dict:
    """One query, two captures: organic rank movement AND aio presence movement — diffed INDEPENDENTLY.
    No blend: organic and AIO are different stability surfaces (serpapi.py docstring)."""
    m0, m7 = organic_rank_map(d0), organic_rank_map(d7)
    moved = {d: {"d0": m0[d], "d7": m7[d]} for d in m0.keys() & m7.keys() if m0[d] != m7[d]}
    aio0 = d0.get("ai_overview_present") and not d0.get("ai_overview_skipped")
    aio7 = d7.get("ai_overview_present") and not d7.get("ai_overview_skipped")
    return {
        "query": d7["input"]["query"],
        "organic": {
            "moved": moved,
            "dropped": sorted(m0.keys() - m7.keys()),
            "new": sorted(m7.keys() - m0.keys()),
        },
        "aio_presence": {"d0": aio0, "d7": aio7, "movement": _aio_move(aio0, aio7),
                         "d7_reason": d7.get("ai_overview_unavailable_reason")},
    }


def _aio_move(a0: bool, a7: bool) -> str:
    if a0 and not a7:
        return "dropped"
    if a7 and not a0:
        return "appeared"
    return "stable"


def serp_run_diff(d0_list: list[dict], d7_list: list[dict], label: str) -> dict:
    """Run-vs-run: align queries, diff each, THEN apply the batch-outage veto across the whole run.
    The veto is inherently run-level — it needs every row to compute the drop fraction."""
    by_q0 = {e["input"]["query"]: e for e in d0_list}
    by_q7 = {e["input"]["query"]: e for e in d7_list}
    shared = sorted(by_q0.keys() & by_q7.keys())
    rows = [diff_serp_pair(by_q0[q], by_q7[q]) for q in shared]

    present_at_d0 = [r for r in rows if r["aio_presence"]["d0"]]
    dropped = [r for r in rows if r["aio_presence"]["movement"] == "dropped"]
    frac = (len(dropped) / len(present_at_d0)) if present_at_d0 else 0.0

    run_vetoes: list[str] = []
    if present_at_d0 and frac >= OUTAGE_FRACTION:
        affected = [r["query"] for r in dropped]
        run_vetoes.append(
            f"probable_aio_surface_outage: {len(dropped)}/{len(present_at_d0)} previously-present AIO rows "
            f"blanked at once ({frac:.0%} >= {OUTAGE_FRACTION:.0%}) — flag the surface, do NOT report "
            f"{len(dropped)} independent real drops. Affected: {affected}"
        )
        for r in dropped:
            r["aio_presence"]["movement"] = "dropped_OUTAGE_SUSPECTED"

    return {
        "label": label, "source_type": "serp", "grain": "category_query", "read_mode": "delta",
        "aio_drop_fraction": round(frac, 3),
        "outage_threshold": OUTAGE_FRACTION,
        "run_vetoes": run_vetoes,
        "rows": rows,
    }


# --------------------------------------------------------------------------- driver
def banner(title: str) -> None:
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)

    # ---- 1. PATH ROUND-TRIP (honehealth: persist D0 + D7, then DISCOVER + read back to diff) ----
    banner("1. PATH ROUND-TRIP — persist to store/<domain>/signals/<src>/<ts>.json, then read back")
    p0 = persist(load(FIXTURES / "clean-d0.json"), OUT)
    p7 = persist(load(FIXTURES / "clean-d7.json"), OUT)
    print(f"persisted D0 -> {p0.relative_to(OUT)}")
    print(f"persisted D7 -> {p7.relative_to(OUT)}")
    found = discover(OUT, "honehealth.com", "trustpilot")
    print(f"discover('honehealth.com','trustpilot') globbed {len(found)} capture(s), sorted by captured_at:")
    for e in found:
        print(f"   - {e['captured_at']}  review_count={e['review_count']}")
    assert len(found) == 2, "round-trip failed: D0 not found by D7"
    tp_clean = diff_trustpilot(found[0], found[1])
    print("\ndiff (read back from disk, not handed over):")
    print(json.dumps(tp_clean, indent=2))

    # ---- 2. TRUSTPILOT VETOES (removed + templated) ----
    banner("2. TRUSTPILOT INTEGRITY VETOES — removed profile + templated/farmed reviews")
    tp_removed = diff_trustpilot(load(FIXTURES / "getpetermd-d0.json"), load(FIXTURES / "removed-d7.json"))
    print("removed-profile pair:")
    print(json.dumps(tp_removed, indent=2))
    tp_templated = diff_trustpilot(load(FIXTURES / "templated-d0.json"), load(FIXTURES / "templated-d7.json"))
    print("\ntemplated/farmed pair:")
    print(json.dumps(tp_templated, indent=2))

    # ---- 3. SERP AIO VETO (real 1/4 negative case vs constructed high-fraction positive case) ----
    banner("3. SERP AIO BATCH-OUTAGE VETO — real Jun8->Jun11 (1/4) vs constructed high-fraction")
    d0 = [load(p) for p in sorted(SERP_D0_DIR.glob("*.json"))]
    d7_real = [load(p) for p in sorted(SERP_D7_DIR.glob("*.json"))]
    real = serp_run_diff(d0, d7_real, "REAL Jun8->Jun11 (cached, no spend)")
    print("NEGATIVE case — real data, one query's AIO genuinely moved:")
    print(json.dumps(real, indent=2))

    # Positive case: take the real D0 set, blank AIO on a high fraction (3 of 4) -> outage signature.
    d7_outage = [json.loads(json.dumps(e)) for e in d0]  # deep copy of the real D0 captures
    for e in d7_outage[:3]:  # blank 3 of 4 -> 75% drop
        e["ai_overview_present"] = False
        e["ranked_brands"] = []
        e["references"] = []
        e["captured_at"] = "2026-06-11T18:00:00Z"
    outage = serp_run_diff(d0, d7_outage, "CONSTRUCTED 3/4 AIO blanking (outage signature)")
    print("\nPOSITIVE case — 3/4 blanked at once, veto must fire:")
    print(json.dumps(outage, indent=2))

    # ---- verdict ----
    banner("VERDICT")
    checks = {
        "round-trip: D0 discovered + read back by D7": len(found) == 2,
        "velocity diffed off cumulative review_count": tp_clean["comparisons"][0]["delta"] == 180,
        "reviews_last_12m level-read only (not diffed)": tp_clean["comparisons"][1]["delta"] is None,
        "rolling-window trap surfaced (last_12m fell while cumulative rose)":
            found[1]["reviews_last_12m"] < found[0]["reviews_last_12m"] and tp_clean["comparisons"][0]["delta"] > 0,
        "removed profile -> veto, empty deltas": bool(tp_removed["vetoes"]) and not tp_removed["comparisons"],
        "templated reviews -> comparability flag on the delta":
            any(f.get("flag") == "templated_reviews" for f in tp_templated["comparability_flags"]),
        "SERP: real 1/4 drop -> NO outage veto (reported as real movement)":
            not real["run_vetoes"] and any(r["aio_presence"]["movement"] == "dropped" for r in real["rows"]),
        "SERP: 3/4 drop -> outage veto FIRES":
            bool(outage["run_vetoes"]) and outage["aio_drop_fraction"] >= OUTAGE_FRACTION,
        "organic rank + AIO presence diffed independently (separate keys)":
            all("organic" in r and "aio_presence" in r for r in real["rows"]),
    }
    for name, ok in checks.items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"\n{'ALL PASS' if all(checks.values()) else 'SOME FAILED'} — {sum(checks.values())}/{len(checks)}")
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
