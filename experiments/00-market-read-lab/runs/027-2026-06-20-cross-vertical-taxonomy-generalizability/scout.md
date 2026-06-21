# Scout

## Prior Context Read

- `triage.md`: 13 live items. Dominant pressure: MRL-001 (denominator reconciliation),
  MRL-002 (query recipes), MRL-008 (source-rigor/confound), MRL-006 (counterparty
  capture-grain gap), MRL-009 (capture worklist). **None** concerns cross-vertical
  taxonomy generalizability — the closed-set classification layer has only ever been
  exercised inside telehealth.
- `scout-context.md`: select for value + reach + roadmap learning, not
  store-answerability; calibration reads that show where Truffle added little are
  first-class; name the builder lens for any reader-value question.
- Last 3 `run-notes.md` files (024 behavioral-health boundary, 025 geographic
  availability, 026 ownership consolidation): all three are **telehealth-cohort-internal**.
  024 reframed the corpus as "DTC Rx-commerce, not telehealth" (selection-bias, MRL-001
  3rd sighting). 026 found the clean `parent`/`owns` relation dangles 18/21 because
  targets are uncaptured.
- Current run artifacts: fresh scaffold; no prior `scout.md`.

## Standing observation driving the slate

All 26 completed runs read **inside the telehealth / DTC-Rx slice** (~64 of 135 are
Healthcare & Life Sciences). The store also holds a large, well-captured **non-telehealth
slice**: ~23 Technology, 6 Finance/Fintech (incl. VC firms), 6 Consumer Goods (incl.
7 luxury-watch brands), 5 Energy/Utilities, 3 Automotive, 2 Industrial. The lab has
never read it. The engine's design claim is "**universal fields + reusable vertical/cohort
cuts**." That claim has been tested on exactly one vertical. The slate's reach axis this
cycle is **cross-vertical generalizability**, not another telehealth cut.

## Candidate Questions

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **A. Is Truffle's universal classification taxonomy telehealth-overfit? Read the non-telehealth slice (~71 cos) and map where the closed-set `offering_category` / `primary_industry` / `business_model` fields strain, improvise per-row rules, or go empty.** | calibration | yes | store-only | Tests the engine's core "universal layer" claim against the one slice that never shaped it; the frontmatter already carries `# STRAIN` markers and gating rules as self-reported evidence | Persistence boundary + closed-set taxonomy generalizability — is the universal State layer actually universal? | Whether the schema bends gracefully or breaks outside telehealth; the VC-firm `offering_category: []` strain; maker-vs-reseller / Investor-Holding gating rules | Grep over `offering_category` / `primary_industry` / `business_model` frontmatter incl. inline `# STRAIN` / rule comments; count strained rows vs clean rows | Over-reading inline comments as defects when they are honest, working disambiguation; conflating "rare value" with "broken value" |
| B. Across the non-telehealth slice, who publishes pricing vs gates it, and does the price-visibility axis (heavily used in telehealth runs) even mean the same thing for watches / enterprise SaaS / VC? | calibration | yes | store-only | Re-tests the lab's most-used axis cross-vertical | Whether a telehealth-born read axis transfers | Price-visibility semantics outside DTC-Rx | Grep pricing/offerings fields across slice | Forcing a DTC frame onto B2B/enterprise where "contact sales" is normal, not hiding |
| C. For the 7 luxury-watch brands (Rolex/Patek/AP/ALS/Cartier/Casio/Swatch), does the `offerings.md` roster + profile capture a catalog-shape business as usefully as it captures a telehealth menu? | calibration | yes | store-only | Concrete single-cohort generalizability probe | Catalog vs menu offering grain | Whether `portfolio_shape: Catalog` is served by the same offerings machinery | Read 2-3 watch `offerings.md` + profile | Treating thin capture as schema failure when it's just a shallow capture pass |
| D. How many captured companies are non-company entities (VC firms, holdings, investors) and does `entity_type` carry them where `offering_category` cannot? | calibration | yes | store-only | Probes the one row-type that breaks the product taxonomy | Entity-type vs offering-category division of labor | The `offering_category: []` + Investor/Holding gating convention | Grep `entity_type` + empty `offering_category` rows | Singleton over-generalization |
| E. Does the store contain placeholder / malformed / non-domain captures (e.g. `beta-team`, `cfs-energy`, `heco-partners`, `home-medvi-org`) and what hygiene gap do they reveal? | gap-probe | yes | store-only | Store-hygiene radar | Capture-keying integrity | Non-canonical-domain slugs | List store dirs, inspect the odd slugs | Mistaking intentional non-`.com` captures for errors |
| F. Across the whole store, which `business_model` values are actually used and does the closed set leave any captured company unclassifiable? | calibration | yes | store-only | Lighter-weight version of A on one field | Closed-set coverage of `business_model` | Unused / over-used / strained model values | Grep `business_model` | Field-only view misses the multi-field strain A captures |
| G. (reach/live) Pull a third-party "best luxury watch brands 2026" listicle set and diff against the store's 7 captured watch brands — is the watch slice a coherent cohort or incidental captures? | gap-probe | yes | bounded-live | Tests whether a non-telehealth cohort even has a denominator | Cohort-membership outside telehealth | Whether non-telehealth captures form cohorts or are one-offs | 1-2 listicles, light ceiling | Sprawl into a watch-market census; low roadmap payoff vs A |

## Selected Question(s)

1. **Candidate A** — Is Truffle's universal classification taxonomy telehealth-overfit?
   Map where the closed-set classification fields strain, improvise, or go empty across
   the ~71-company non-telehealth slice.

Rationale: highest roadmap leverage (tests the engine's central "universal + reusable
cuts" claim on the slice that never shaped it), genuinely new design territory (26/26
prior runs were telehealth-internal), store-only and fully autonomous-safe, and the
evidence is unusually clean — the taxonomy's own `# STRAIN` / gating-rule comments are
self-reported stress markers. B/C/D/F are narrower facets of A; A subsumes them.

## Selected Run Contract

```yaml
selected_question: "Is Truffle's universal classification taxonomy telehealth-overfit? Read the non-telehealth slice of the store (~71 companies across Technology, Finance/VC, Consumer Goods/watches, Energy, Automotive, Industrial) and map where the closed-set classification fields (offering_category, primary_industry, business_model, portfolio_shape, entity_type) strain, improvise per-row rules, or go empty — and where they carry cleanly."
selected_slug: cross-vertical-taxonomy-generalizability
run_type: system-test
question_mode: calibration
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Captured companies whose primary_industry is NOT Healthcare & Life Sciences (~71 of 135); cross-checked by offering_category != the telehealth [Services/Consulting, Biotech/Pharma] convention."
likely_source_panel: "store/*/profile.md frontmatter only — offering_category, primary_industry, business_model, portfolio_shape, entity_type, plus inline # STRAIN / gating-rule comments. No external sources."
builder_lens: "Closed-set classification-taxonomy generalizability + the persistence boundary: is the engine's universal State layer actually universal, or telehealth-overfit? Where does the taxonomy bend gracefully (rare-but-valid value) vs break (no value fits / forced empty / per-row improvised rule)?"
reach_reason: "Every prior run read inside telehealth; this is the first read of the slice that never shaped the taxonomy. It probes whether the central engine claim (universal fields + reusable cuts) holds beyond the design vertical."
allowed_sources:
  - "store/ (profile.md frontmatter and inline comments only)"
  - "SCHEMA.md"
  - "TAXONOMIES.md"
  - "experiments/00-market-read-lab/ (lab artifacts)"
disallowed_actions:
  - "live browsing / WebSearch / Firecrawl spend"
  - "store/ mutation or write-back"
  - "durable primitive / taxonomy-value creation"
  - "triage graduation"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Pure read over already-captured local frontmatter and the two contract docs; no spend, no external sources, no mutation."
loop1_failure_mode: "Reading honest inline disambiguation comments as taxonomy defects (over-claiming breakage), or conflating a rarely-used-but-valid value with a broken one. Must distinguish graceful-bend from break, and say 'strained' not 'broken' unless a row truly has no fitting value."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. A is a calibration/system-test
read: its value is mapping where Truffle adds little (or strains) outside its design
vertical — explicitly first-class per the value/reach test. It does not prefer
store-answerability; it deliberately points the read at the substrate most likely to
expose a frontier. The honest-comment-vs-defect trap is the load-bearing failure mode
and is written into the contract.
