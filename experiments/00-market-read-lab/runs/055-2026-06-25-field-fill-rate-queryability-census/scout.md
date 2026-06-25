# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  Read. L005 (query-time grouping enough *when the corpus carries the cut*) and its
  corollary (structured-absence ≠ market-absence) is the most-load-bearing lesson for a
  reliability census. Observations 036–054 show a heavy recent streak of store-only
  schema-fit / cohort-key / relation-pressure probes, with a recurring `denominator-
  reconciliation` n=5 finding (`primary_industry` ≠ entity-shape cohort key) and a
  recurring "decision-grade fact lives off the captured surface" gap (036 G2 / 037 / 038
  G2 / 042 G4). Many runs end on a CR1 "lands on builder/Pantry not buyer" frontier.
- `scout-context.md`: two-test selection (value/reach + design); don't optimize for
  store-answerability; name the builder lens; gap-probes are first-class.
- Last 3 `run-notes.md` files (052 price-freshness-decay bounded-live, 053 wearable
  coverage-radar bounded-live, 054 sleep/recovery JTBD-substitution store-only): the
  last two bounded-live runs both probed the *external* coverage/freshness frontier;
  054 re-confirmed the horizontal-relation absence at buyer-goal grain. **Gap in the
  recent slate:** no run has measured the store's *own* reliability substrate — every
  cohort/schema-fit run assumes fields are populated and reasons from whichever are; none
  has asked store-wide "which fields can a downstream system actually rely on being there."
- Current run artifacts, if resuming: fresh scaffold (055), Scout-only.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1 (REC) — Field fill-rate / queryability census.** Across all ~136 captured `profile.md` files, what is the population rate of each SCHEMA frontmatter field, and which fields are populated reliably enough that a downstream system can *filter/group* on them vs which are so sparse (or default-valued) that grouping on them silently drops companies? | calibration | yes | store-only | Directly serves the "build on top without re-capturing" value job: a downstream consumer needs to know which fields are dependable ingredients. No run has measured the store's reliability substrate store-wide — every prior schema-fit run *assumes* it. | persistence/queryability boundary — which fields are real cuts per engine-dev's "a field is a cut only if you can fill it reliably"; the empirical substrate L005 assumes. | Reaches past any single cohort to the *whole* store; quantifies the structured-absence-vs-market-absence trap L005 names but no run has sized. | A field-presence grep over all profiles; per-field non-empty rate; flag list-fields that are present-but-`[]`; distinguish a captured default (`[B2C]`) from a discriminating value. | Counting a populated default value as a real cut; conflating "field absent" with "field present, empty list"; over-claiming a fill-rate number as a market fact rather than a capture-coverage fact. |
| C2 — Comparison-sheet heterogeneity. When a reader asks for a side-by-side of N companies that span entity types (e.g. a SaaS + a marketplace + a hardware brand), does the shared frontmatter yield a usable comparison or do incommensurable fields collapse it? | gap-probe | yes | store-only | "Compare a whole field" at the *output* grain rather than the data grain. | output comparability boundary across entity shapes. | Reaches the cross-entity comparison surface. | Assemble a 6-row mixed-entity table from frontmatter; mark which columns are comparable vs N/A. | Heavy overlap with prior schema-fit runs (036/037/044/050); risks re-proving "schema is telehealth-shaped." |
| C3 — Offerings-roster completeness self-disclosure. For the ~71 companies with `offerings.md`, does the profile honestly disclose whether the roster is comprehensive or a sample (via `site_notes` / `unverified_fields`), or can a reader mistake a partial catalog for the whole? | calibration | yes | store-only | "Trust the cache" / "build on top" at SKU grain; `/deepen-offerings` exists precisely because rosters are often partial. | coverage-honesty boundary at the offering grain. | Reaches the roster-completeness axis (depth-backfill). | grep `offerings.md` + `unverified_fields` for completeness language across the 71; rate disclosed-vs-silent. | Treating a long roster as comprehensive; "not captured" ≠ "doesn't sell it." |
| C4 — `key_pages` reliability for a delegated agent. Do captured `key_pages` give a delegated agent dependable entry points (pricing/about/contact), or are they sparse/inconsistent enough that an agent can't navigate the company from State alone? | gap-probe | yes | store-only | "Make AI safe to delegate to" at the navigation grain. | tooling/navigation-substrate boundary. | Reaches the delegated-navigation axis. | grep `key_pages:` keys across all profiles; tabulate which page types appear and fill-rate. | Subset of the C1 census; lower standalone value. |
| C5 — Telehealth-vs-non-telehealth depth asymmetry. Is the store materially deeper on telehealth than other verticals (field fill, body length, module presence), and would that bias a naive cross-vertical read? | calibration | yes | store-only | "Trust the cache / know the blind spots"; cohort bias is *intentional* (deep telehealth) but unmeasured as a depth asymmetry. | calibration of corpus bias; confidence/source-grain uncertainty. | Reaches the known-blind-spot calibration. | bucket profiles by vertical; compare module presence + body length. | Partly subsumed by C1 if C1 cuts by vertical; risks re-stating the known intentional bias without new design payload. |
| C6 — Bounded-live reach: mainstream-brand pricing-model gap. For a mainstream category the store covers thinly, do third-party lists + the brands' own pages reveal a pricing-model pattern the store is structurally blind to? | gap-probe | yes | bounded-live | Tests the external frontier past the cached answer. | source-panel / coverage. | Reaches outside the store. | small SERP + 2 listicle panel, brand pages. | 052 + 053 just ran two consecutive bounded-live external probes; another now over-weights the external frontier and risks repeating the coverage-radar shape. Hold as the parked reach sibling. |

## Selected Question(s)

1. **C1 — Field fill-rate / queryability census** (recommended). It is the highest-value
   under-tested run on the board: it serves the "build on top without re-capturing"
   pillar directly, measures the reliability substrate every prior schema-fit run merely
   assumed, and sizes the structured-absence trap L005 names but no run has quantified.
   Store-only and unattended-safe. C3 (offerings completeness) is the strongest runner-up
   and a natural next run; C6 is the parked bounded-live reach sibling, deliberately held
   because 052+053 already ran two consecutive external probes.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Across all captured profile.md files, what is the population rate of each SCHEMA frontmatter field, and which fields are populated reliably enough that a downstream system can filter/group on them — versus which are so sparse or default-valued that grouping on them silently drops companies?"
selected_slug: field-fill-rate-queryability-census
run_type: system-test
question_mode: calibration
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "All store/<domain>/profile.md files (~136). Partial by construction — this is a census of the captured corpus, not of any market; the fill-rate of a field is a capture-coverage fact, never a market fact."
likely_source_panel: "Local store frontmatter only (grep/awk over profile.md). No external sources. SCHEMA.md as the field-contract reference."
builder_lens: "Persistence / queryability boundary — which frontmatter fields are reliably filled enough to be dependable query/group keys for a downstream consumer, and which are present-but-empty or default-valued and therefore silently lossy. Tests engine-dev's 'a field is a cut only if you can fill it reliably' against the live corpus."
reach_reason: "Reaches past every single-cohort schema-fit run to the whole-store reliability substrate those runs assumed; quantifies the structured-absence-vs-market-absence trap (L005 corollary) that no run has yet sized."
allowed_sources:
  - "store/ (all profile.md frontmatter; bodies only to confirm a field's empty-vs-default reading)"
  - "SCHEMA.md and TAXONOMIES.md (field-contract reference)"
  - "experiments/00-market-read-lab/learning/ (context)"
disallowed_actions:
  - "No live browsing, Firecrawl, or any external source."
  - "No store/ mutation, write-back, or durable primitive creation."
  - "No re-capture or deepen."
  - "Do not report a fill-rate as a market fact; it is a capture-coverage fact."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Read-only grep/awk over local store frontmatter plus the local SCHEMA contract; no spend, no external sources, no mutation."
loop1_failure_mode: "Counting a populated default (e.g. [B2C], the modal offering_category) as a discriminating cut; conflating an absent field with a present-but-empty list; over-claiming a fill-rate as a market fact rather than a coverage fact; treating telehealth-driven fill rates as store-wide without cutting by vertical."
```

## Selection Notes

The recent slate has leaned store-only schema-fit (036–051) and external bounded-live
(052/053), with 054 a store-only JTBD probe. C1 is intentionally a *different shape*: a
whole-store reliability census rather than a cohort read. It is a calibration/system-test
run whose design payload is a reusable map of which fields a downstream consumer can
build on — and it should be unsurprising if the honest outcome is "no new primitive
needed, but here is the dependability frontier." Per scout-context, it names its builder
lens (queryability/persistence boundary) and does not optimize for store-answerability:
the *point* is to find where the structured substrate is too sparse to be a cut.
