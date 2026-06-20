# Scout

## Prior Context Read

- `triage.md`: Active items center on MRL-002 (State-read query-recipe family, now 4
  surfaces deep, Acknowledged P1), MRL-001 (denominator reconciliation; the
  anchored-only-vs-all-offerers under-count has now recurred on 4 cohorts), MRL-008
  (captured-signal confound convention), and the relation pair MRL-005/006 (Submitted,
  partial-fire on run 014). MRL-010 (review/forum bodies) crossed its "3rd sighting" bar
  on run 011 and is graduation-decision-ready (human-gated).
- `scout-context.md`: two-test selection (value vs generic Claude+web; design pressure /
  roadmap learning). Persist runs, not ontology. Under-tested design uncertainties to
  bias toward: **persistence boundary**, **relations/neighborhood**, **change pulse /
  freshness**. Avoid recurrence unless it closes a design decision.
- Last 3 `run-notes.md` (012/013/014): all single-cohort, store-only or bounded-live.
  012 = GLP-1 default-brand leaderboard (bounded-live); 013 = sexual-health structural
  access map (store-only); 014 = GLP-1 backend-counterparty relations (store-only).
  Every one of runs 008-014 reads a **single cohort**.
- Store probe (this session): 135 companies; ~10 distinct `anchor_category` labels
  (GLP-1 ~17, multi/none ~10, longevity/NAD ~8, TRT ~7, sexual-health 3, peptides 2,
  plus womens-HRT / primary-care / labs / hair singletons). No `competitors`/`similar`
  frontmatter exists. Signals coverage: wayback 102, sec_edgar 20, trustpilot 20, but
  exa_similar 2 / serpapi 2 / trends 5 / ads_transparency 1 — the newer signal sources
  are **too thin** for a cohort read, so a new-Signals-source read is not autonomous-safe
  store-only this cycle.

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| **C1.** Across *all* captured telehealth cohorts, which acquisition/commitment mechanics (intake-gating, membership wedge, compounded-vs-FDA-brand, upfront multi-month, price-visibility) are **cohort-agnostic table-stakes** vs **cohort-specific**? | market | yes | store-only | First **cross-cohort** read in the lab (008-014 are all single-cohort). A strategist wants "what's table-stakes in DTC telehealth overall vs what's specific to GLP-1/TRT/etc." — exactly the collation generic Claude can't do without the captured cohort. | `anchor_category` grep per cohort; per-brand structural frontmatter (`pay_model`/`access_model`/`compounding_posture`/`modality`) + price-visibility; quote verbatim; cap denominator to anchored set per cohort. | Overclaiming "telehealth-wide table stakes" from an **anchored, partial** denominator (the 4x-recurring MRL-001 under-count); mixing a cohort-property with a brand-property. |
| **C2.** Is **price publication** a cohort property or a brand property — which cohorts publish price vs gate it behind intake, across the whole store? | market | yes | store-only | Cross-cohort generalization of the price-visibility reads (000/008). | Per-cohort `Visibility` extract; capture dates. | Recurrence of 000/008 **without** a new design decision — would mostly re-confirm MRL-002. |
| **C3.** What do the **`multi/none` generalists** (LifeMD, Nurx, Wisp, …) that fall out of every anchored-cohort grep actually sell, and how many anchored cohorts does each straddle? | market/system-test | yes | store-only | Turns the 4x-recurring MRL-001 under-count into its own read; maps the brands every cohort census silently drops. | `anchor_category: multi/none` set + per-brand offering/condition coverage; cross-tab against each cohort's term-grep. | Risks **merely executing a parked triage next-step** (MRL-001) rather than originating from reader value. |
| **C4.** Across cohorts, which are **compounding-dependent** (`compounding_posture`) vs FDA-brand-dispensing — i.e., which cohorts carry the most regulatory exposure? | market | yes | store-only | Single clean structural cut across cohorts; ties to regulatory change-pulse. | `compounding_posture` per brand per cohort; verbatim. | Narrower than C1; one-field read risks thinness; `unclear` fill-rate (per run 013 fill-rate ceiling). |
| **C5.** What is the store's **freshness profile** — capture-date distribution by cohort/module — and which cohorts/fields are most at risk of having gone stale since capture? | system-test | yes | store-only | Tests the under-exercised **change-pulse/freshness** design uncertainty (only run 002 touched it); trust-the-cache value job. | Per-file capture dates / store clocks by cohort+module; no market claim. | Meta/navel-gazing with weak market-reader value; says nothing a consumer acts on. |
| **C6.** Across cohorts, which are **single-gender franchises** vs all-gender, and where is the women's-health whitespace? | market | yes | store-only | Boundary/membership cut; whitespace is reader-valued. | `audience` field per brand per cohort. | Thin (womens-HRT is a singleton cohort); whitespace claim from a male-skewed store is a coverage artifact, not a market truth. |
| **C7.** Beyond GLP-1, do third-party "best of 2026" listicles name a **default set** for a *second* cohort (TRT or longevity), and how does it compare to the store's captured universe? | market | yes | bounded-live | Tests whether run 012's leaderboard finding (head-stable/tail-bought, cross-source recurrence) **generalizes** off GLP-1. | 2 authoritative listicles per cohort; affiliate-disclosure + cross-source-recurrence rule from MRL-008. | Recurrence of 012; autonomous bounded-live spend; affiliate confound. |

## Selected Question(s)

1. **C1 — Cross-cohort acquisition/commitment mechanics: cohort-agnostic table-stakes
   vs cohort-specific.** (Recommended.) Strongest on both tests: genuinely novel axis
   (first cross-cohort read), clear strategist value, and a sharp design test — the
   **persistence boundary** (does a cohort-agnostic pattern earn durable *cross-cohort*
   State, or is query-time grouping enough across cohorts too?).
2. **C4** (compounding-dependence across cohorts) as the runner-up — cleaner one-field
   cut if C1 proves too broad to land crisply.

These are Scout recommendations for the autonomous cycle; C1 is selected.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: >-
  Across all captured telehealth cohorts (GLP-1, TRT, longevity/NAD, sexual-health,
  multi/none, peptides, womens-HRT, hair, primary-care, labs), which acquisition and
  commitment mechanics — intake-gating, membership wedge, compounded-vs-FDA-brand
  dispensing, upfront multi-month commitment, and price publication — are cohort-agnostic
  table-stakes versus cohort-specific? And does any cohort-agnostic pattern argue for
  durable cross-cohort State, or is query-time grouping enough?
selected_slug: cross-cohort-offer-table-stakes
run_type: mixed
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: >-
  The anchored brand set per cohort (grep `anchor_category:` over store/*/telehealth.md),
  treated as PARTIAL by construction — the multi/none generalists that sell into a cohort
  without anchoring to it (MRL-001 under-count, 4 prior cohorts) are out of the per-cohort
  census and must be named as a known gap, not silently dropped.
likely_source_panel: >-
  store/*/telehealth.md frontmatter (`anchor_category`, `pay_model`, `access_model`,
  `compounding_posture`, `modality`, `audience`) and offerings.md Visibility rows /
  profile.md pricing-visibility, all already captured. No external sources.
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/triage.md"
disallowed_actions:
  - "live browsing or SERP/listicle fetches"
  - "any Firecrawl or paid capture spend"
  - "store/ mutation or write-back to any project system"
  - "creating a durable cross-cohort category/cohort object or new frontmatter field"
  - "graduating any triage item"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: >-
  Answerable entirely from already-captured store frontmatter via grep/group/label
  (the MRL-002 State-read recipe family). No live evidence, no spend, no mutation. The
  only judgment surface is labeling a mechanic cohort-agnostic vs cohort-specific, which
  is tied back to quoted verbatim cells.
loop1_failure_mode: >-
  Overstating "telehealth-wide table stakes" from an anchored, partial denominator
  (MRL-001), or letting a per-field `unclear`/low fill-rate (MRL-002 fill-rate ceiling,
  run 013) silently inflate a cohort-agnostic claim. Mitigate: report fill-rate per
  load-bearing field; treat the anchored set as partial; quote cells, don't re-derive
  from prose (MRL-009/010 guard).
```

## Selection Notes

C1 is selected over the single-cohort recurrence candidates (C2/C7) because it changes
the **axis** — cross-cohort rather than within-cohort — which is the materially-different
test scout-context allows recurrence for: it closes a *persistence-boundary* design
decision (cohort-agnostic pattern → durable State vs query-time grouping) that no
single-cohort run can. C3 was rejected as the lead because it risks merely executing the
MRL-001 parked next-step rather than originating from reader value, though C1 will touch
the same under-count as a *named denominator caveat*, not as the question itself. C5
(freshness) is the other genuinely under-tested design uncertainty but scores weak on
market-reader value, so it is held. Newer Signals sources (exa_similar/serpapi/trends/
ads) are too thin (≤5 captures) to carry a store-only cohort read this cycle.
