# Scout

## Prior Context Read

- `triage.md`: 16 MRL items. Used only as post-candidate pressure annotation. Most
  relevant to this slate: **MRL-015** (Investor/Holding classification gating is
  under-specified — capital-allocator encoding) is an open, named, *unresolved* schema
  pressure on exactly the entity-type this slate targets; **MRL-002** (the
  cross-vertical read-recipe family) where run-033 W1 explicitly named "a 4th vertical
  (e.g. Finance/VC rate-card vs advisory-quote)" as the bar to graduate the
  `gate-type × gate-grain` reading-discipline addend; **MRL-008** (structured-surface-
  absence branch, confirmed on telehealth/SaaS/luxury — a 4th vertical would re-test it).
- `scout-context.md`: two-test selection (value/reach + design), value jobs, design
  uncertainties, evidence modes. Selecting for value + reach + builder lens, not
  store-answerability.
- Last 3 completed `run-notes.md` (032 freshness-grain, 033 watch price-visibility, 034
  GLP-1 ads-transparency): recent diet is heavy on **builder-facing calibration / trust-
  metadata** (029/031/032) and **price-visibility generalization** (028/033). Two
  signals for this slate: (a) the price-visibility-across-verticals groove is well-worn
  — a 4th vertical is only worth it if it *closes* the run-033 W1 decision, not just
  re-confirms; (b) Finance/Investor is the one major store vertical that has never had a
  dedicated market read AND carries an open schema pressure (MRL-015), so it scores on
  both reader-reach and design novelty.
- `discovery-ledger.md`: run-027 first flagged `schema-edge-entity-type`; MRL-015 grew
  from the Investor/Holding encoding gap. No prior run has read the Finance slice as a
  market.

## Candidate Questions

Scout selected for reader value, reach, source-family diversity, and roadmap learning —
not store-answerability.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1.** Across the captured Finance & Fintech + Investor/Holding slice (~16 entities), what business model and fee/pricing posture does each disclose, and does the store's telehealth-shaped schema actually capture what a finance/investor firm *is* — or do the load-bearing facts (AUM/fund focus, fee/rate structure, who they serve) fall outside the captured fields? | value-read + gap-probe | yes | store-only | First-ever market read on the store's Finance/Investor vertical; a recognizable downstream question (how do finance/advisory firms charge?) that simultaneously stress-tests the schema on the hardest entity-type. | **MRL-015 + MRL-002 run-033 W1 + MRL-008.** Tests whether "universal fields + reusable cuts" survives `entity_type: Investor/Holding`, and whether the price-visibility axis composes on a 4th vertical (rate-card vs advisory-quote) — the named graduation bar. | Schema-edge: does the engine *describe* a capital allocator, or force-fit a product company shape? Plus the structured-surface-absence branch on a new vertical. | `profile.md` business_model/pricing prose + frontmatter for ~16 cos; `entity_type`, `primary_industry`, `unverified_fields`; quote verbatim, don't re-derive. | Overclaiming a "finance market pattern" from n≈16 of heterogeneous subtypes (VC vs bank vs asset-mgr vs fintech-product); conflating *schema can't capture it* with *firm didn't disclose it*. |
| **C2.** Does the competitive/substitute relation read (MRL-011, built on telehealth Hone in run 017) generalize to the SaaS/Technology slice — can the store tier "true substitute vs adjacent peer" for a software anchor, or is the relation even less enum-derivable off telehealth? | gap-probe | yes | store-only | Tests whether the lab's one relation-tiering recipe is telehealth-bound; relations are a named roadmap edge. | MRL-011 cross-vertical; relation-as-Judgment. | Relations/neighborhood off the design vertical. | A SaaS anchor + `primary_industry: Technology` grep + offerings overlap read. | Substitute-tiering is buyer-relative and even fuzzier in B2B SaaS; thin evidence → weak verdict. |
| **C3.** Across the captured store, which companies expose a **SERP-visibility** signal (`signals/serp/`), and what does that captured signal actually measure vs mislead (branded vs non-branded, position vs presence) — the one major repeatable signal family the lab hasn't dedicated a read to? | calibration | yes | store-only | Completes the signals-family calibration set (Trustpilot/Wayback/SEC/ads all read; SERP not). | MRL-008 confound family on a new signal grain; source-rigor. | Source-panel coverage + signal integrity siblings. | `ls store/*/signals/serp/`, read the JSON schema + a few captures. | Coverage may be near-zero → degenerates into a pure coverage caveat with little market signal. |
| **C4.** Cutting the **Consulting & Professional Services** slice (~6 cos), how do these firms present what they sell and whether they price it — is "engagement/advisory-quote" a 4th distinct gate-type, or the same enterprise-quote gate as SaaS? | value-read | yes | store-only | A second professional-services lens on the gate-type question; pairs/contrasts with C1. | MRL-002 run-033 W1 gate-type generalization. | Pattern extraction on a thin, services-shaped vertical. | `primary_industry` grep + offerings/pricing prose. | n≈6, likely all "advisory-quote" → low entropy, restates the obvious. |
| **C5.** Across the captured store, can a reader distinguish a company's **funding/ownership stage** (bootstrapped vs VC-backed vs PE-owned vs public) from existing State (`parent`/`owns` frontmatter + SEC signal + prose), and at what coverage — a market-structure read a downstream strategist would want? | gap-probe | yes | store-only | Market-structure is a recognizable strategist question; tests whether the store supports it without a new field. | denominator + relation-pressure; persistence boundary. | Boundary/membership on ownership stage. | `parent`/`owns` grep + `signals/sec_edgar/` + prose. | Stage is rarely stated directly; high inference risk (claim-not-truth); overlaps run-026 ownership map. |
| **C6.** For a bounded panel of up to 6 captured brands across 2 verticals, does the **Wayback offer-tenure** signal corroborate the ads-tenure signal (run 034) — do "long-advertising" brands also show long-lived offer pages, or do the two tenure surfaces disagree? | gap-probe | yes | bounded-live | Cross-signal corroboration is a fresh shape; tests whether two tenure proxies agree. | source-panel; signal triangulation. | Relations between two captured signal families + light live check. | `signals/wayback/` + `signals/ads_transparency/` captures; ≤2 live ad re-checks. | Both signals are presence/tenure proxies with different confounds; "agreement" may be spurious; bounded-live adds spend for marginal gain. |
| **C7.** Across the full store, how complete is the **`offerings.md`** roster layer (which companies have it, how many SKUs, which verticals are backfilled vs bare) — the depth-backfill gap MRL-003/MRL-008 keep flagging, measured once cleanly? | calibration | yes | store-only | Turns a recurring scattered caveat into one clean coverage map a builder can act on. | depth-backfill; coverage-caveat. | Persistence/coverage boundary on the roster module. | `ls store/*/offerings.md` + line counts. | Pure inventory read; low *market*-reader value (builder-only); counts rot. |

## Selected Question(s)

1. **C1** — Finance & Fintech + Investor/Holding business-model & fee-posture read,
   framed as a schema/entity-type fit gap-probe. *(recommended)*

Rationale: C1 is the only candidate that scores high on **both** tests at once — it is a
recognizable reader question (how do finance/advisory/investor firms disclose what they
do and how they charge) **and** it lands directly on an *open, unresolved* design
pressure (MRL-015 Investor/Holding encoding) while supplying the run-033 W1 4th-vertical
data point (rate-card vs advisory-quote gate-type) and re-testing the MRL-008 structured-
surface-absence branch on a never-read vertical. It avoids the "store-answerability"
trap by leading with the schema-fit gap-probe: a clean *failure* (the schema can't
describe a capital allocator) is as valuable as a clean answer. C3 (SERP signal
calibration) is the strong runner-up and the natural next pick, but it risks degenerating
into a coverage caveat if `signals/serp/` coverage is near-zero; C1's substrate (~16
entities) is confirmed to exist.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Across the captured Finance & Fintech + Investor/Holding slice (~16 entities), what business model and fee/pricing posture does each disclose, and does the store's telehealth-shaped universal schema actually capture what a finance/investor firm IS — or do the load-bearing facts (AUM/fund focus, fee/rate structure, who they serve, capital-allocator role) fall outside the captured fields?"
selected_slug: finance-investor-schema-fit-fee-posture
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Store profiles with primary_industry 'Finance & Fintech' (~9) plus entity_type 'Investor / Holding' (~7); union ~16, treated as PARTIAL and reconciled in Loop 1 (whitespace-dirty industry values; some Investor/Holding may also be Finance). Consulting & Professional Services (~6) is adjacent context only, not the denominator."
likely_source_panel: "store-only: profile.md frontmatter (entity_type, primary_industry, business_model, parent/owns, unverified_fields) + business-model/pricing/overview prose + offerings.md where present + SCHEMA.md/TAXONOMIES.md for the contracted field set."
builder_lens: "Schema/entity-type generalizability on the hardest entity-type (Investor/Holding, MRL-015): does the universal field set + reusable cuts describe a capital allocator, or force-fit a product-company shape? Secondary: the run-033 W1 gate-type x gate-grain 4th-vertical bar (rate-card vs advisory/AUM-fee vs deal-by-deal), and the MRL-008 structured-surface-absence branch re-test."
reach_reason: "First market read on the store's Finance/Investor vertical; reaches past the comfortable telehealth/SaaS substrate to the entity-type the engine was least designed for, against an OPEN triage pressure (MRL-015) rather than a closed one."
allowed_sources:
  - "store/ (profile.md, offerings.md, frontmatter, prose for the Finance & Fintech + Investor/Holding union; Consulting & Professional Services as adjacent context)"
  - "SCHEMA.md and TAXONOMIES.md (the contracted universal field set, to judge schema fit)"
  - "experiments/00-market-read-lab/triage.md and discovery-ledger.md (design-pressure context only, not evidence)"
disallowed_actions:
  - "No store/ mutation, no write-back, no durable primitive/field creation"
  - "No live browsing, no Firecrawl/Exa spend, no SERP/listicle fetch (store-only run)"
  - "No re-deriving frontmatter fields from prose; quote verbatim per the MRL-002/009 guard"
  - "No completeness claims from the partial denominator; say 'not found', not 'not there'"
  - "No triage graduation; no implementing/spiking system changes"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Fully answerable from already-captured local store files + the in-repo schema contract. No spend, no live browsing, no write-back. Reads a bounded ~16-22 company union of existing profiles."
loop1_failure_mode: "Two coupled traps: (1) conflating 'the schema can't capture it' with 'the firm didn't disclose it' (a real disclosure gap masquerading as a schema gap, or vice versa) — must separate not-captured-by-schema from not-disclosed-by-firm; (2) overclaiming a single 'finance market pattern' across heterogeneous subtypes (VC firm vs bank vs asset manager vs fintech product) from n≈16 — report by subtype, flag low entropy, never crown a vertical-wide pattern from a thin, mixed cohort."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. This slate optimized for reader
value + reach + design novelty + source-family/cohort diversity against known blind
spots. The Finance/Investor vertical is the store's largest never-read slice and the one
open *unresolved* schema pressure (MRL-015), which is why C1 outranks another telehealth
price/relation read. The repeat of the price-visibility *axis* (run-033 W1) is justified
under `scout-context.md`'s repeat rule because the recurrence is designed to **close a
named design decision** (the 4th-vertical gate-type bar) on a **materially different
cohort/entity-type**, not to re-confirm a settled answer. `repeat_reason` for C1 is
therefore `calibration` (closes the MRL-002 run-033 W1 gate + supplies the first MRL-015
market-read evidence), not `new` and not idle recurrence.
