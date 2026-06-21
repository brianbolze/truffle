# Scout

## Prior Context Read

- **History map (`question_history.py`):** 31 reviewed runs (000–030). Coverage is
  heavily telehealth-internal State reads (pricing, trust, tenure, funding, positioning,
  offer-ladder, access, backend relations, ownership, visual, audience, proof-devices,
  geography, price-comparability). Recent reach: cross-vertical taxonomy (027), SaaS
  pricing (028), traction coverage (029), external cross-shop (030). Bounded-live
  coverage-radar used on 4 lanes (012/022/024/030).
- **`scout-context.md`:** select for value + reach + roadmap learning, source-family
  diversity, calibration against blind spots — **not** store-answerability. Name the
  builder lens. Gap-probes/calibration reads are first-class. Don't let a candidate merely
  execute a parked triage next-step.
- **Under-probed design uncertainties:** **Confidence / source-grain** (no run has audited
  how the store represents its *own* uncertainty as a reader-facing trust surface) and
  **change-pulse / freshness** (only 018 on signals, 029 on traction — never on profile
  State capture-recency). The recurring `query-time-grouping-enough` verdict and MRL-008's
  source-rigor family touch *specific* confounds but never the cross-store **self-uncertainty
  discipline** as a whole.
- **Store recon (counts rot — captured this run):** 139 dirs / **130 profiled**;
  `captured_at` present in **130/130** profiles; corpus spans **2026-05-30 → ~2026-06-20**
  (33 May / 97 June) — uniformly recent, so pure capture-recency is near-trivial.
  `unverified_fields` present and **non-empty in 130/130**; STRAIN markers in 58. The
  self-uncertainty layer is dense and has never been read cross-store.
- This run is the **autonomous scheduled cycle** (Brian not present). Selected for a
  store-only, autonomous-safe calibration read on the confidence-grain frontier.

## Candidate Questions

Slate generated for reader value + reach + source-family diversity + roadmap learning.

| Question | Mode | Auto-eligible? | Evidence | Why worth a run | Builder lens / design test | What it reaches | Trustworthy evidence needs | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **[SELECTED] Across the captured store, how does each profile mark its own uncertainty (`unverified_fields`, STRAIN markers, hedged `site_notes` prose, absence-as-not-found), and can a downstream reader distinguish a high-confidence captured fact from an inferred/point-in-time/scope-omitted one at query grain — or is the store's "honesty layer" a heterogeneous catch-all that doesn't compose into a trust signal?** | calibration (gap-probe) | yes | store-only | First cross-store audit of the engine's *self-uncertainty* discipline — the substrate the "make AI safe to delegate to" value job depends on. Reader-valued (which fields can I trust?) and roadmap-valued (is confidence a queryable surface or only per-file prose?). | **Confidence / source-grain persistence boundary.** Whether `unverified_fields` is a consistent, reader-usable trust surface or a mixed bucket (genuine field-uncertainty vs point-in-time caveat vs scope decision vs capture-note). Tests false-completeness discipline across 130 profiles without creating any primitive. | Reaches past every prior *content* read into the store's **trust metadata** layer — never read cross-store. Probes whether a consumer can mechanically separate verified from unverified State. | `unverified_fields` body read across 130 profiles + taxonomize the caveat kinds; STRAIN-marker sample; `site_notes` hedge patterns; SCHEMA.md on what `unverified_fields`/STRAIN are *contracted* to mean; absence-discipline ("not found" vs "not there"). | (a) Counting field presence (130/130) and calling the discipline "complete" — the question is *composability*, not presence. (b) Treating a heterogeneous caveat bucket as a clean unverified-field list. (c) Reading STRAIN (mostly Firecrawl branding-payload, per run-027) as field-uncertainty. Must taxonomize, not tally. |
| Across the store, how fresh is the profiled corpus — capture-date distribution by cohort/vertical, median staleness, and can a reader tell at query grain whether a profile is current enough to act on? | calibration | yes | store-only | "Trust the cache over time" value job, directly. | Freshness/persistence boundary — is capture-recency vs content-currency a queryable surface? | Reaches the freshness frontier on *profile State* (018 was signals only). | `captured_at` distribution; per-cohort cut; SCHEMA freshness contract. | Corpus is uniformly <1mo old → capture-recency is trivially "all fresh"; the real (harder) finding is capture-recency ≠ content-currency, which collapses into MRL-012's change-pulse gap. Lower marginal learning than the confidence read; recorded as the strong alternative. |
| In the captured watches/luxury + consumer-goods slice (Richemont brands, Casio, Nike, etc.), how does brand/price positioning cluster and how concentrated is ownership — does a *consumer-goods* market read run on the same recipe SaaS (028) and telehealth use? | value-read | yes | store-only | Third-vertical generalizability of the read-recipe family. | Read-recipe generalizability on a non-B2B, non-Rx vertical. | Reaches a third vertical. | `primary_industry` slice + positioning/price/parent fields. | 027/028 already settled "recipe generalizes for sellers"; a 3rd confirm is lower marginal learning unless it tests a *different* recipe. Held as alternative. |
| Re-run Hone Health's substitute/adjacent map (run 017) now that 4 of its named cross-shop neighbors (Numan, Male Excel, Fountain TRT, Sesame) were just captured — did corpus growth change the competitive read? | value-read | yes | store-only | Tests whether MRL-009 capture-worklist action improved a relation read. | Coverage→relation feedback loop. | Reaches the post-capture relation delta. | run-017 set + new profiles. | **Rejected as a parked next-step** — it directly executes run-030's MRL-009 worklist follow-up rather than originating a reader-valued question; better as a human-chosen re-read. |
| A second NON-hormone-cohort store-only traction read, scored against the 5-rung ladder, to harden MRL-016's "machinery ahead of coverage." | gap-probe | yes | store-only | Would harden a roadmap fact. | Traction-readiness ladder, 2nd cohort. | Reaches a 2nd traction data point. | signals/ walk on a non-hormone cohort. | **Rejected** — this is the literal parked next-step named *inside* MRL-016's `proposed_next_step`; scout-context says triage must not originate the candidate. |
| Bounded-live: spot-check 4–5 store `unverified_fields` caveats against the live site to see how many resolved/changed since capture. | gap-probe | yes | bounded-live | Would test whether caveats decay. | Confidence-decay over time. | Reaches live verification of caveats. | 2 families, ≤6 sources, ≤20 credits. | Deferred — the store-only *structure* of the honesty layer is the higher-information reach this cycle and spends nothing; live caveat-decay is a clean follow-up once the structure is mapped. |

## Selected Question(s)

1. **Across the captured store, how does each profile mark its own uncertainty
   (`unverified_fields`, STRAIN markers, hedged prose, absence-as-not-found), and can a
   downstream reader distinguish a high-confidence captured fact from an
   inferred/point-in-time/scope-omitted one at query grain — or is the honesty layer a
   heterogeneous catch-all that doesn't compose into a trust signal?**

Rationale: this is the lab's first cross-store audit of the engine's *self-uncertainty*
discipline — the exact substrate the "make AI safe to delegate to" value job rests on. It
is reader-valued (which captured facts can I trust without re-verifying?), roadmap-valued
(is confidence a queryable surface or only per-file prose?), store-only, and
autonomous-safe. Recon proves it is non-trivial: `unverified_fields` is non-empty in all
130 profiles but already visibly heterogeneous (scope decisions vs point-in-time price
caveats vs genuine field-uncertainty), so the load-bearing question is **composability,
not presence**. The contracted failure mode is the guardrail: do not tally field presence
and call the discipline complete; taxonomize the caveat kinds and test whether a reader can
mechanically separate verified from unverified State.

## Selected Run Contract

This block is the canonical handoff to Loop 1. If it disagrees with the candidate table,
Loop 1 trusts this block.

```yaml
selected_question: "Across the captured store, how does each profile mark its own uncertainty (unverified_fields, STRAIN markers, hedged site_notes prose, absence-as-not-found), and can a downstream reader distinguish a high-confidence captured fact from an inferred / point-in-time / scope-omitted one at query grain — or is the store's honesty layer a heterogeneous catch-all that does not compose into a usable trust signal?"
selected_slug: store-self-uncertainty-confidence-grain
run_type: mixed
question_mode: calibration
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Profiled store companies (130 profile.md of 139 dirs — count profile.md, per MRL-001 run-027 stub caveat). unverified_fields present in 130/130; STRAIN markers in ~58. Treat the caveat population as a census of the discipline, but remember absence of a caveat is not proof of certainty (the read must say 'no caveat recorded', not 'verified')."
likely_source_panel: "store/<domain>/profile.md frontmatter (unverified_fields, captured_at) + body (# STRAIN markers, site_notes hedges, Overview absence language); SCHEMA.md / TAXONOMIES.md for what unverified_fields and STRAIN are CONTRACTED to mean and the absence-discipline rule; MRL-008 triage entries (source-rigor + absence-disambiguation flavors) and run-026 bare-parent finding as adjacent prior art; run-027 STRAIN-marker characterization (mostly branding-payload, not classification strain)."
builder_lens: "Confidence / source-grain persistence boundary. Whether the store's self-uncertainty layer (unverified_fields + STRAIN + hedged prose + absence-as-not-found) composes into a reader-usable trust signal at QUERY grain, or is a heterogeneous per-file catch-all. Taxonomize what unverified_fields actually holds (genuine field-uncertainty / point-in-time caveat / scope-omission / capture-method note). Tests false-completeness discipline and the State/confidence boundary without creating any primitive."
reach_reason: "First cross-store read of the engine's TRUST-METADATA layer rather than its content. Reaches past every prior State/Signals read into how the store represents its own uncertainty — the substrate the 'safe to delegate' job depends on and that no run has audited."
allowed_sources:
  - "store/"
  - "SCHEMA.md"
  - "TAXONOMIES.md"
  - "experiments/00-market-read-lab/triage.md"
  - "experiments/00-market-read-lab/discovery-ledger.md"
disallowed_actions:
  - "No Firecrawl / live web / scraping / SERP / re-capture."
  - "No store/ mutation or write-back."
  - "No durable primitive / field / schema / category creation."
  - "No re-verifying any caveat against a live source (that is the deferred bounded-live follow-up)."
  - "No triage graduation."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from local store files (profile.md frontmatter + body) and the SCHEMA/TAXONOMIES contract; no spend, no live browsing, no write-back, no primitive creation."
loop1_failure_mode: "Three traps. (a) Presence-as-completeness: counting unverified_fields 130/130 and concluding the honesty discipline is complete — the real question is whether the bucket composes into a trust signal, which requires taxonomizing the caveat KINDS. (b) Conflating layers: reading STRAIN (mostly Firecrawl branding-payload corrections, per run-027) as field-uncertainty, or treating a scope-omission ('roster not written this run') as a data-confidence flag. (c) Absence overclaim: reading 'no caveat recorded' as 'field verified' — must say 'no caveat recorded / not flagged', never 'verified' or 'certain'. Map the structure; do not score or rank profiles by trustworthiness."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. This run is deliberately a
calibration/gap-probe on the engine's confidence/source-grain frontier — the value-read
layer is a real "can I trust a captured fact without re-verifying it?" answer the
"safe-to-delegate" consumer needs, and the gap-probe layer is the roadmap learning
(does confidence compose into a queryable surface, or stay per-file prose?). The two
rejected candidates (Hone re-read, 2nd traction read) were cut because they execute parked
triage next-steps rather than originate reader-valued questions; the freshness and
consumer-goods reads are recorded as the strongest alternatives.
