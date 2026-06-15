# FINDINGS — Probe #1 (signal_delta de-risk)

**Verdict: PASS (9/9). The comparator build is cleared** — with two capture-tool prerequisites and one shape decision the probe surfaced (below).

## What's de-risked

- **Raw-envelope diffing works — no card layer needed.** Each source branch reads the tool's own envelope and emits per-metric deltas bound to one `source_type`. A blended score is *not expressible* (every number carries its metric + unit + basis). The drift/integrity signals stay directly under the comparator's eye.
- **The cumulative-vs-rolling trap is real and caught.** On the clean pair, lifetime `review_count` rose **+180 (≈25.7/day over 7d)** while `reviews_last_12m` *fell* (3100→3050) — the rolling window's left edge moved. Diffing `reviews_last_12m` would have reported negative velocity for a growing brand. The comparator diffs cumulative `review_count` and **level-reads `reviews_last_12m` only** (delta = null + a basis note).
- **Integrity failures are veto rows, never dropped rows.** Removed profile → `profile_removed_between_captures`, empty deltas. Merged profile → same. Templated/farmed D7 (3 identical bodies in a 5-sample) → the +160 delta still computes but carries `templated_reviews` + `bursty_growth` comparability flags ("may be partly farmed, not organic").
- **The SERP AIO batch-outage veto discriminates correctly — the adversarial pass's #1 catch.** Diffed independently from organic rank:
  - **Real 1/4 drop (TRT, Jun 8→11):** veto stays silent; reported as a genuine per-query AIO movement. ✅
  - **Constructed 3/4 drop:** veto **fires** — flags a probable surface outage on all 3 rows, explicitly *not* "3 independent real drops." ✅
  - Threshold `OUTAGE_FRACTION = 0.6` cleanly separates 0.25 from 0.75 (prior-art outages were 6/7≈0.86, 11/12≈0.92).
- **Real data exercised real movement.** The cached pair has live organic churn even over 3 days (`fifty410.com` 7→3, `forbes.com` 4→7, `empowerpharmacy.com` 6→9 on tirzepatide) — so level-read→delta and independent diffing ran on real signal, not just fixtures.
- **Path round-trip holds.** D0 persisted to `store/honehealth-com/signals/trustpilot/<ts>.json`, discovered by glob, sorted by `captured_at`, read back, diffed. Accumulation is a findable-path problem, and the path solves it.

## Prerequisites the probe surfaced (do these before / with the build)

1. **`trends.py` needs `peak_date`.** The envelope emits `peak` (the value) but not the *date* of the peak — the per-keyword normalization anchor. The comparator's basis-aware Trends veto ("both captures' `peak_date` must fall inside the date-overlap, else `renorm_basis_mismatch`") can't run without it. It's derivable from `points`, but the plan's call to surface it as a labeled field is right — a one-line `summarize_series` change (→ **milestone 3**). *No cached trends envelope exists, so this is from the code, not a run.*
2. **The SERP branch is run-grained, not pairwise.** The batch-outage veto needs *every* same-run row to compute the drop fraction — it cannot be decided from a single `<a.json> <b.json>` pair. Implication for `signal_delta.py`: the SERP branch takes a **run vs run** (a dir/glob of query-aligned envelopes), with the outage veto as a run-level pass; Trustpilot stays single-subject pairwise. This also tracks the **grain split** — SERP is `category_query` grain → it belongs in the architecture's deferred `cohorts/`, *not* `store/<domain>/signals/` (which is company-grain: Trustpilot, Wayback, per-brand Trends, funding). v1 emits company-grain only; the SERP branch is built but its captures don't land in the company path.

## Carried into the build (`tools/signal_delta.py`)

- Branches validated here: **trustpilot** (pairwise) + **serp** (run). To add per the plan: **trends** (after #1), **wayback** (thin over `wayback.py diff`), **fallback** (reserved-key facts only).
- The **alignment fence** (subject + source_type + grain must match, else veto) is load-bearing — unit-test it; a cross-subject pairing must veto, never average.
- A capture with `schema_drift` or `ok:false` reaches the comparator as a ready-made veto (drift is absorbed at the capture tool) — confirmed by the fence logic; no re-validation downstream.
