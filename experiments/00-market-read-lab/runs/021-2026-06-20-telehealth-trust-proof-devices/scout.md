# Scout

## Prior Context Read

- `triage.md`: open pressure is dominated by `denominator-reconciliation` (MRL-001),
  `source-rigor` (MRL-008), relation edges (MRL-005/006/011), and category-scoped
  exogenous signals (MRL-007). Relation-as-State and source-rigor are the least-resolved
  threads.
- `scout-context.md`: two-test selection (reader value + design value); start from a
  recognizable market question; `query-time-grouping-enough` is a valid outcome; prefer
  fresh value jobs / design uncertainties over recurrence.
- Last 3 `run-notes.md` files (018 signal-change, 019 visual-cluster, 020 audience-grid):
  all store-only, all landed `query-time-grouping-enough` / no-new-primitive. The lab is
  saturating on **telehealth store-only cohort cuts** — 17 of the last 18 runs cut the
  telehealth cohort by some axis (category, price, audience, signals, visual). Marginal
  design return on another generic cohort cut is low; the under-tested axes are
  **pattern-extraction on a fresh attribute**, **generalization beyond telehealth**, and
  **source-panel / external corroboration**.
- Current run artifacts: fresh scaffold (021).

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| **C1. Across the captured telehealth cohort, what trust/proof devices do brands surface on owned pages — clinician credentialing, regulatory/legal framing (FDA, LegitScript, licensed-pharmacy), efficacy/outcome claims, and commercial-trust devices (money-back, transparent cancellation) — how do they cluster by `anchor_category`, and which are capturable State vs marketing Judgment the store should not harden?** | market | yes | store-only | Trust is the #1 telehealth buyer concern (011 trust-gap was the richest bounded-live read); a proof-device pattern map is brief-ready and beats generic Claude because the store has cited owned-page positioning across ~50+ brands. Fresh **pattern-extraction** axis never cut as primary. | `profile.md` / `offerings.md` proof-claim language across the cohort, graded as *brand-asserted* (owned-page State), with a hard line that asserting a device ≠ the underlying claim is true. | Reading presence of a device as proof the claim is true; reading absence on captured pages as "brand lacks it." |
| C2. Does the offer / price-visibility reading pattern the lab refined on telehealth produce a comparably trustworthy read on a **non-telehealth** store cohort (luxury watches, DTC tech), or does it degrade — and what does that reveal about telehealth-overfit in the cohort machinery? | system-test | yes | store-only | First generalization stress-test in 21 runs; directly addresses overfit risk. | A second cohort captured at comparable depth. | Watches/tech are captured `profile.md`-only (no `offerings.md`) — the read degrades for a boring capture-depth reason, not an interesting one. **Rejected as store-only: no clean second cohort at depth.** |
| C3. Across the telehealth store, which brands are corporate siblings (shared parent/operator), and can the store make ownership rollups knowable — does this recur enough to deserve a parent/owner relation edge? | market/system-test | yes | store-only | Pushes the open relation-as-State thread (MRL-005/011). | Parent/operator names in `profile.md` ownership sections. | **Recurrence fatigue** — 014/016/017 all hit relation edges within the last week; marginal new design signal is low. |
| C4. In the TRT / men's-health cohort, do third-party "best TRT clinic 2026" listicles name the same brands the store anchors, and where's the named-set gap? | market | yes | bounded-live | Source-panel corroboration on a fresh cohort. | A small SERP/listicle panel + the store cohort. | Direct recurrence of 012 (GLP-1 default-brand-leaderboard) with a different cohort — calibration only, lower novelty; bounded-live spend not warranted for a near-repeat this cycle. |
| C5. What intake/acquisition-funnel shape does each telehealth brand use (instant-checkout vs quiz-gated vs sync-consult-required), and what does the friction ladder reveal about buying-effort norms by category? | market | yes | store-only | Pattern-extraction on a fresh attribute (funnel friction). | `profile.md` / `offerings.md` intake-flow descriptions. | Overlaps the price-visibility "intake-gated" axis (000/008/010); partial recurrence; intake-flow detail is inconsistently captured. |
| C6. Across the cohort, what guarantee / cancellation / refund terms are published vs silent, and is "easy cancellation" becoming a table-stakes claim or a differentiator? | market | yes | store-only | Commercial-trust sub-pattern; brief-ready. | Owned-page terms language. | Narrow; largely a slice of C1's commercial-trust bucket — better folded into C1 than run alone. |
| C7. For one under-analyzed captured telehealth brand, can the store + its captured neighbors produce a trustworthy cold-start placement (offer, price posture, audience, backend) without re-capturing? | system-test | yes | store-only | Tests the under-used **cold-start** value job. | One thin-capture brand + neighbor set. | Single-company shape is more a query-recipe test than a market read; lower reader value. |

## Selected Question(s)

1. **C1 — telehealth trust/proof-device pattern map.** Best combined score: strong,
   recognizable reader value (trust is the cohort's load-bearing buyer concern), a genuinely
   fresh pattern-extraction axis (never cut as primary in 21 runs), and a clean design test —
   it forces the **State-vs-Judgment boundary** on claim-type evidence (a brand *asserting*
   "board-certified / FDA-registered" is owned-page State; whether that claim is *true* or
   *differentiating* is Judgment the store must not harden). Store-only and unattended-safe.

These are Scout recommendations until Brian or the operator confirms.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: >-
  Across the captured telehealth cohort, what trust/proof devices do brands surface on
  their owned pages — clinician credentialing (board-certified, named medical directors),
  regulatory/legal framing (FDA, LegitScript, licensed/accredited pharmacy), efficacy/outcome
  claims (quantified results, cited studies), and commercial-trust devices (money-back
  guarantee, transparent cancellation) — how do these cluster by anchor_category, and which
  are capturable owned-page State versus marketing Judgment that the store should not harden?
selected_slug: telehealth-trust-proof-devices
run_type: market
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: >-
  Captured telehealth-cohort domains carrying a profile.md (and offerings.md where present).
  Treat as partial: proof devices may live on owned pages the capture did not reach, so
  absence is "not found on captured pages," never "brand lacks it."
likely_source_panel: >-
  store/<domain>/profile.md and offerings.md across the telehealth cohort; no external panel.
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/ (lab artifacts, read-only context)"
disallowed_actions:
  - "Firecrawl or any paid capture"
  - "live browsing / external fetch / WebSearch"
  - "store/ mutation or write-back"
  - "verifying whether an asserted claim is actually true (out of scope; would need external)"
  - "durable primitive creation or triage graduation"
live_evidence_plan: null  # store-only
approval_needed: no
why_autonomous_safe: >-
  Answerable entirely from already-captured local store files plus lab artifacts; no spend,
  no external fetch, no write-back. The only synthesis risk (asserted-device vs true-claim)
  is handled by an explicit State-vs-Judgment boundary in the read, not by browsing.
loop1_failure_mode: >-
  Treating the presence of a proof device as evidence the underlying claim is true, or reading
  absence on captured pages as proof the brand lacks the device; over-aggregating prose-grain
  claim language into a false-precision count (cf. run 019's polarity-field miscount).
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. The slate deliberately spans three
under-tested directions (fresh pattern axis, generalization, relation/source-panel) so the
rejections are on the record: C2 generalization is the biggest blind spot but has no clean
store-only second cohort at depth (defer to a capture-first run); C3 relation and C4
bounded-live leaderboard are recent recurrences. C1 wins on reader value × design novelty ×
autonomous safety. C6 folds into C1's commercial-trust bucket.
