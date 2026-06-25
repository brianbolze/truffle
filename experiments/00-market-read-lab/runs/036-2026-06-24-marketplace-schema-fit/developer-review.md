# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | Strength: 3/5 take-rate schedules captured verbatim in prose. Gap: filings/IR source family missing for off-site economics (airbnb, uber fee %). | etsy/doordash/upwork prose vs airbnb:28 / uber:71 unverified_fields | O2 · gap; G2 · gap; S1 · surprise |
| **Structure** | Strength: marketplace shape is a *positive, designed-for* fit (`Marketplace / Platform` + `Marketplace / Commission`) — better than the run-035 investor subtractive gate. Gap: no structured economics (take rate / GMV / monetized side); the `[published]` token is consumer-offering-grained, not platform-monetization-grained. | TAXONOMIES:47/:83; SCHEMA:142; read.md Result(1)(2) | O1 · surprise; G1 · gap |
| **Query / access** | Gap: `business_model` (not `primary_industry`) is the only field that recovers the marketplace cohort — industry grep is structurally blind to entity-shape cohorts. | 5 brands scatter across 5 industries | G3 · gap *(re-kinded from friction per dev review)* |
| **Synthesis** | Strength: two-stacked-absence discipline (schema-can't vs firm-didn't-on-site) applied cleanly; *not-captured ≠ not-charged* held throughout. Gap: economics table initially omitted Etsy's consolidated-scope caveat (now fixed). | read.md Result(3); Etsy GMS row | S1 · surprise; R2 · gap |
| **Guardrails** | Strength: store-only contract honored — no spend, no live browse, no store mutation; no lesson proposed or graduated. | run-notes exit check (all pass) | — |

## Lenses

**Steward** — Honest. Provenance (capture clocks), grain (prose vs field), and the
State/Signals/Judgment boundary are all visible. The one honesty risk the review caught —
Etsy's consolidated GMS presented without scope — is now carried in the table and logged
(R2). The store profile already held the caveat in `unverified_fields`; the read surface
just hadn't propagated it.

**Dev Agent** — The repeated toil (per-profile prose extraction of economics) is the
standing MRL-002 query-machinery friction on an economics grain; not worth a helper at
n=5. The reusable contract is G3: *draw cross-shape cohorts on `business_model`, not
`primary_industry`* — a grep-verifiable convention note if it recurs.

**Founder** — The run compounds the warm/cited asset without adding ontology gravity.
W1 correctly resists a take-rate/GMV field family: the load-bearing reason is
**unit-incomparability** (per-listing vs per-delivery-tier vs per-contract), not
prose-by-default — a future reader citing W1 should see that reason (noted for the
observation row).

## Recommendation

- **No-op / keep as observation:** Yes. "No new primitive needed" is the honest verdict;
  the marketplace shape is well-served by existing structured fields + prose.
- **Watch for recurrence:** `schema-edge-entity-type`, `query-time-grouping-enough`,
  `depth-backfill`, `source-panel`, `denominator-reconciliation`. W1 stays at recur-watch;
  graduates only with a real cross-marketplace economics consumer + a 2nd homogeneous cohort.
- **Severe risk-miss to surface now:** None. R1 (token readability trap) and R2 (Etsy
  consolidated GMS) are real but bounded reader-expectation risks, logged, not severe.

## Raw learning to preserve

New review-surfaced sighting appended to `learning/observations.md`: **R2** (gap — Etsy
house-of-brands consolidated GMS not propagated from profile `unverified_fields` to the
read surface; no structured entity-grain flag for single-brand vs house-of-brands). The
preserved run-notes rows O1/O2/S1/G1/G2/G3/W1 are also lifted.

**No lessons proposed, nothing graduated, no system change implemented.**
