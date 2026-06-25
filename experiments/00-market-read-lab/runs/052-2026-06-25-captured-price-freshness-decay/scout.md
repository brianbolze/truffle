# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L001–L006 (bounded-live coverage radar graduated; headline-confound; uncaptured
  review bodies; partial denominators; query-time-grouping-enough; price-visibility
  token grain). Observations stream runs 036–051. Heavy recent threads:
  `denominator-reconciliation` (industry draw ≠ entity-shape cohort, n≥4),
  `relation-pressure` (horizontal competitor relations absent), `traction-readiness`
  (momentum unanswerable from static State), the "value lands on builder not buyer"
  CR1 frontier, and `query-time-grouping-enough` as the dominant verdict.
- `scout-context.md`: two-test selection (value/reach + design); persist runs not
  ontology; don't optimize for store-answerability; bounded-live allowed with a filled
  light plan + ceilings + fail-closed rules.
- Last 3 `run-notes.md` files: 049 (render brief flag fidelity — salience burial,
  local-existing), 050 (services/consulting bucket overload — store-only),
  051 (cold-start profile reliability — store-only). **Three consecutive inward/
  store-only reflective reads.** The store-only streak runs 045→051 with one
  bounded-live (047) and one local-existing (049) interleaved.
- Current run artifacts: fresh scaffold.

## Candidate Questions

Scout selects for reader value, reach, source-family diversity, and roadmap learning.
Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1 (SELECT) — Captured-price freshness decay.** For a small panel of store brands whose pricing was captured on the open marketing page (oura, eightsleep, therabody, hyperice, peloton — several captured *mid-promotion*), does the live marketing-page price still match the captured price, and what does the divergence rate say about how fast captured pricing State rots? | gap-probe / calibration | yes | bounded-live | First **empirical** test of the recurring 041/048 gap ("captured State has no change-detection; `captured_at` dates the profile, not the event"). 032/041/048 reasoned about staleness *internally*; this measures it. If prices are stable, the no-change-home gap is low-priority; if they rot fast (esp. the sale-snapshot captures), it's high-priority roadmap input. Directly serves the under-exercised "trust the cache over time" value job. | `freshness-monitoring` / does captured pricing decay fast enough to need a re-capture trigger or staleness flag, or is it durable? Open-marketing-page prices are re-checkable in one plain fetch — no intake funnel. | Reaches past the store-only streak; verifies captured State against the live web (the store cannot self-check freshness). | Each live re-check is itself a point-in-time snapshot; a captured *sale* price differing from today is "a different promo," not a proven decay rate. Must say "M of N prices differ at re-check," never "prices decay at X%/week." Plain-markdown scrape only — no PDF/JSON-extraction (run-040/047 spend-breach class). | Treating one re-check as a decay rate; scope-creep into more brands; intake-gated prices forcing a funnel (excluded by panel choice). |
| C2 — Cross-store ownership consolidation map beyond telehealth. | value-read | yes | store-only | Maps `parent`/`owns` concentration store-wide. | relation-pressure (vertical axis). | Little — vertical relation is already structured. | Frontmatter only. | **Reject: near-duplicate of run-026.** |
| C3 — Which captured SaaS/Tech tools name an integration/partner ecosystem, and is that a load-bearing relation? | value-read | yes | store-only | Partner/ecosystem is a distinct relation axis from competitor/parent. | relation-pressure (partner axis). | A relation sub-axis less-tested than competes-with. | Prose grep for "integrates with". | Likely another "prose-grade, dangles off-store" finding (run-039/047 shape); lower marginal learning. |
| C4 — Per-company "what's the catch": the single most load-bearing caveat across a cohort's `unverified_fields`. | value-read | yes | store-only | Buyer-facing synthesis of trust flags. | source-rigor / salience. | Overlaps 031/049/051 (trust-surface salience). | Store only. | **Reject: near-repeat** of 031/051 confidence-grain reads. |
| C5 — GLP-1 / telehealth captured-price freshness (same shape as C1 on telehealth). | gap-probe | no | bounded-live | Same freshness question on a higher-stakes cohort. | freshness-monitoring. | Telehealth headline prices are intake-gated (run-040). | Would need to enter funnels. | **Reject for autonomy: intake-gated → fails closed** (run-040). C1's open-page panel is the safe substrate for the same probe. |
| C6 — Deep-tech funding/milestone recency via external press (date the events run-048 couldn't). | gap-probe | no | live-external-needs-approval | Tests the off-surface press/filings panel for traction event-dating. | traction-readiness / source-panel. | The off-surface panel 048 G2/S3 named. | Press is broad and sprawl-prone; no clean bounded panel. | **Reject for autonomy: source family too broad** for a light unattended plan; 048 just covered the static side. |
| C7 — Luxury/watch captured-price freshness. | gap-probe | partial | bounded-live | Freshness on a third cohort. | freshness-monitoring. | Most luxury brands don't publish price (run-033). | Thin price surface. | **Reject: worse panel than C1** (no published prices to re-check). |

## Selected Question(s)

1. **C1 — Captured-price freshness decay** (bounded-live, light plan). The strongest
   reach + roadmap-learning candidate: it empirically tests the most-recurring static-State
   gap on a re-checkable open-marketing-page panel, breaks the store-only streak, and
   serves the "trust the cache over time" value job head-on. The selected panel is chosen
   because several of these captures are explicitly promotional snapshots (run-043/046),
   making the rot test sharp rather than abstract.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 trusts this block.

```yaml
selected_question: "For a small panel of store brands whose pricing was captured on the open marketing page (oura, eightsleep, therabody, hyperice, peloton — several captured mid-promotion), does the live marketing-page price still match the captured price, and what does the divergence say about how fast captured pricing State rots?"
selected_slug: captured-price-freshness-decay
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: bounded-live
expected_denominator: "Up to 5 store brands with open-marketing-page (non-intake-gated) headline pricing already captured in profile.md/offerings.md, prioritizing the promotional-snapshot captures flagged in runs 043/046."
likely_source_panel: "Each brand's own live pricing/product marketing page (vendor first-party), fetched as plain markdown."
builder_lens: "freshness-monitoring — empirically measure whether captured pricing State diverges from live within weeks, to weigh whether the store needs a staleness flag / re-capture trigger (the 041/048 no-change-home gap) or whether captured pricing is durable enough that query-time + capture clock suffice."
reach_reason: "Verifies captured State against the live web — something the store structurally cannot self-check. Breaks a 7-run mostly-store-only streak with a tightly-bounded external check."
allowed_sources:
  - "store/ (captured profile.md / offerings.md for the panel brands; receipts of capture dates)"
  - "experiments/00-market-read-lab/learning/ (context)"
  - "each panel brand's own live pricing/product marketing page, vendor-first-party, plain-markdown scrape only"
disallowed_actions:
  - "No intake-funnel entry, login, account creation, or cart/checkout steps"
  - "No PDF parsing (parsers:[pdf]) and no LLM/JSON extraction (formats:[json]) — the run-040/047 variable-cost spend-breach class; plain markdown only"
  - "No expansion beyond the panel; no SERP/listicle/third-party-aggregator browsing"
  - "No store/ mutation, no write-back, no durable primitive, no re-capture into the store"
  - "No claiming a decay rate from a single re-check"
live_evidence_plan:
  budget_class: light
  evidence_goal: "Verify, for each panel brand, whether the live marketing-page headline price (device and/or membership) still matches the captured value, and record the capture date so the divergence has a measured age."
  allowed_source_families:
    - "vendor first-party marketing/pricing page (the brand's own site)"
  preferred_first: "Read the captured price + captured_at from store/ before any live fetch; only then fetch the matching live page."
  disallowed_source_families:
    - "SERP / listicle / third-party aggregator / review-forum / PDF / paywalled / private"
  ceilings:
    source_families: 1
    outside_sources_read_or_captured: 5
    paid_capture_credits: 8
  fail_closed_when:
    - "A live price would require entering an intake funnel, login, or checkout -> record 'not verifiable on open page', do not enter"
    - "A fetch would need a variable-cost format (PDF/JSON-extraction) -> stop, plain markdown only"
    - "The 5-source or 8-credit ceiling would be exceeded -> stop as insufficient-evidence"
    - "The question would widen beyond price-match verification -> stop"
  stop_rules:
    - "Stop after at most 5 live vendor-page fetches"
    - "If 3+ panel prices are open-page-verifiable, the divergence read is already complete; do not add brands to chase a rounder number"
approval_needed: no
why_autonomous_safe: "Standing bounded-live policy: 1 source family (each brand's own marketing page), <=5 plain-markdown fetches, <=8 credits, no funnels/login/PDF/JSON-extraction, no write-back. Every claim is a price-match check against an already-captured value; absence language ('not verifiable on open page') is fail-closed, not a guess."
loop1_failure_mode: "Overstating a decay *rate* from single point-in-time re-checks; or scope-creeping the panel / source families past the ceiling when a price is gated."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. C1 selected for the highest
combination of reader value ("trust the cache over time"), reach (live verification of
captured State, which the store cannot self-perform), and roadmap learning (it puts a
*measurement* under the most-recurring static-State gap instead of restating it). C5/C6
were rejected for autonomy (intake-gated / source-family-too-broad), C2/C4 as near-repeats,
C3/C7 as lower-marginal-learning. The bounded plan is hardened against the known
`bounded-live-spend` breach class (run-040 PDF, run-047 JSON-extraction) by disallowing
variable-cost formats explicitly, not just by example.
