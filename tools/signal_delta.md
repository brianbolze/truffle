# signal_delta.py — the envelope comparator

Diffs two captures of the same source into **axis-specific deltas + comparability vetoes** — never a
score. The traction approach's one real build; reads the *raw* envelopes the capture tools emit (no card
layer), because drift is already absorbed at the capture tool. Keyless, costless, fetches nothing.

```
python3 tools/signal_delta.py D0.json D7.json                  # pairwise (trustpilot, one serp query)
python3 tools/signal_delta.py runA/ runB/ --min-gap-days 5     # run-vs-run (a SERP panel; trends envelopes)
```

A path can be a **file** (one capture) or a **dir** (a run = many captures). Directory inputs load
`*.json` recursively, so page-grain captures nested under paths such as `wayback/<url-slug>/` are included.
Both input shapes normalize to a list of envelopes, so one code path serves pairwise, run-vs-run, and
multi-subject sources.

## Output shape (trimmed)

```jsonc
{
  "tool": "signal_delta", "source": "local (consumer …)", "captured_at": "…Z",
  "ok": true, "input": { "a": "…", "b": "…", "min_gap_days": 5.0 }, "schema_drift": [],
  "source_types": ["trustpilot"],
  "comparisons": [
    {
      "source_type": "trustpilot", "grain": "company", "subject": "honehealth-com",
      "read_mode": "delta", "gap_days": 7.0,
      "metrics": [
        { "metric": "review_count", "basis": "cumulative_lifetime (monotone)",
          "d0": 11200, "d7": 11380, "delta": 180, "velocity_per_day": 25.71, "unit": "reviews" },
        { "metric": "reviews_last_12m", "delta": null, "unit": "reviews",
          "note": "level-read only — rolling window edge moves" }
      ],
      "comparability_flags": [], "vetoes": []
    }
  ],
  "run_vetoes": []                 // run-level, e.g. a SERP AIO surface outage
}
```

`read_mode` is `delta` (two captures of a subject) or `level` (one). A non-comparable pair is a **veto row
with empty metrics, never a dropped row**.

## Branches (keyed on the envelope's `tool`)

| `tool` | grain | what it diffs | key vetoes / guards |
|---|---|---|---|
| `trustpilot` | company | cumulative `review_count` delta + velocity (gap surfaced) | `reviews_last_12m` is **level-read only** (rolling window); removed / merged-*between-captures* → veto (a stable-merged profile diffs fine); templated/paid/bursty → comparability flags |
| `serpapi` | category_query | organic rank movement **and** AIO presence, **diffed independently** | run-level **batch-outage veto**: ≥60% of previously-present AIO rows blanking at once → probable surface outage, not N real drops |
| `trends` | company | within-keyword trajectory (always) + a **basis-gated** `peak_value` point delta | `renorm_basis_mismatch` when a capture's `peak_date` falls outside the date-overlap (different normalization anchor) |
| `wayback` | page | archive presence, snapshot-count growth, last-seen movement, content-digest change — over two tenure captures | reads the digests `wayback.py` already captured (never re-fetches); the per-snapshot content diff stays `wayback.py diff`'s job |
| `sec_edgar` | company | issuer State fields + dated filing/Form-D event cards | Form-D identity uncertainty and capped newest-filings windows travel as comparability flags; no amount, valuation, or verdict is inferred |
| *(fallback)* | — | — | unknown `tool` → a named veto, never a guessed delta (e.g. a self-contained `wayback_pair_diff` envelope — read it directly, don't re-diff) |

## Gotchas (the value)

- **The dispatch key is the envelope's `tool` value, not a concept.** SerpAPI envelopes carry
  `"tool": "serpapi"` (not `"serp"`) — keying on the wrong string silently routes them to the fallback.
  (Caught only by running real captures; fixtures that invent the tool name hide it.)
- **The SERP outage veto is run-grained.** It needs *every* same-run row to compute the drop fraction —
  a single pair can't tell a real drop (the real 1/4) from an outage (6/7, 11/12). Hand it dirs, not one pair.
- **Trends needs `peak_date`** (added to `trends.py` for this) — the per-keyword normalization anchor. Without
  it the basis-aware veto can't tell a comparable point-level delta from one across mismatched 0-100 scales.
- **No score is expressible by construction** — every number is bound to one `metric` + `source_type` +
  `subject` + `unit`; nothing aggregates across metrics or sources. Don't add a blended field; that's the
  whole point (the [traction frame](../_design/2026-06-14-traction-frame.md)'s asymmetric-failure line).

## Exit codes

`0` produced a report (including an all-vetoes one — a non-comparable pair is data) · `2` operational error
(path missing / holds no envelopes / unreadable JSON). No exit 3: this tool has no version-pinned upstream;
a source envelope's `schema_drift` surfaces as a **veto row**, never the comparator's own drift.

## Where captures live

Company-grain captures persist to `store/<domain>/signals/<source_type>[/<page-slug>]/<captured_at>.json`
(the [architecture](../_design/2026-05-30-architecture.md)'s convention); this tool reads them back.
Category-grain runs (SERP panels) stay in experiments/cohorts until `cohorts/` graduates.

## Growth

- Branches cover the live capture tools (trustpilot, serpapi, trends, wayback, sec_edgar). A new capture tool earns a
  branch when it has two comparable captures; until then the fallback names the gap.
- The card-layer machinery (schema-as-contract, lint, sole-writer, SQLite lens) stays **deferred** until an
  automated writer **and** a second consumer earn it.
