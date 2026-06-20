# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [query-time-grouping-enough, source-rigor, tooling-ergonomics, depth-backfill, coverage-caveat]
```

> **Loop 2 outcome (2026-06-20):** Reviewed via a 3-pass adversarial workflow (evidence verifier
> + consumer + developer, Sonnet). **Verifier: PASS-WITH-FIXES** — independently re-derived the
> five load-bearing tallies and found **4 of 5 outside the read's own ±2–3 bar**, all from one
> root cause (a positive/negated **polarity error**: "…not shown / not observed" lines counted as
> present). Corrected in `read.md` + receipt: **LegitScript ~33/54 (~61%)** not ~42/56; **named
> clinicians ~38 shown / ~16 not-shown** not ~29/~25; **C3 accreditation positives** had 4
> "not-shown" brands removed (defymedical, brellohealth, maximustribe, ro-co); and a **ghost
> citation** (struthealth "180-day money-back") deleted. **The headline pattern was independently
> confirmed and is unchanged** — LegitScript the majority floor, pharmacy accreditation the
> rare/unspent differentiator, named clinicians tracking business model. **Consumer: partly
> valuable** — real, brief-ready, beats generic Claude+web; gated on the exemplar/count
> corrections (now applied). **Developer: submit 2 Evidence Logs, no new item** — folded into
> **MRL-002** (8th read surface + quantified prose-polarity-error rate) and **MRL-008** (proof-
> device State/Judgment flavor + polarity-error recurrence vs run 019); the `proof_devices:`
> frontmatter-promotion idea held as a one-sighting watch. No graduation; no `store/` mutation;
> no Human Notes touched.

## 30-second operator read

- **Did the run work?** Yes. Store-only, zero spend. First lab read on a **proof/trust-device**
  axis. The decisive find came early: the `telehealth.md` cohort pack **already carries a
  standardized credibility checklist** ("Health-merchant credibility" + "Payment & commitment"
  lines, with explicit `y`/`n`/`not shown` flags), so the read is an aggregation of an existing
  cut, not a new extraction.
- **What was awkward?** The cut is **prose, not frontmatter** — positive-vs-negated has to be
  grep-classified, which carries a ±2–3 error bar and left a few cells (e.g. hims's clinician
  bench) unmatched by the heuristic. Same prose-grain fiddliness that miscounted run 019's
  polarity field; I kept integers directional and let the *pattern* carry the weight.
- **What should the next agent know?** Headline is a real, cited category pattern: **LegitScript
  is table stakes (~42/56); pharmacy accreditation (PCAB/ACHC/NABP) is the least-surfaced device
  (~36/54 "not shown"); named clinicians split ~evenly and the split tracks business model**
  (provider-fronted optimization brands show them, commodity GLP-1 compounders don't). Design
  answer: **query-time-grouping-enough + already-captured → no new primitive.** The whole read
  rides a **State/Judgment boundary** — device-*presence* is owned-page State; device-*truth/
  credibility* is Judgment the store must not harden. The one build-shaped nugget (promote the
  prose checklist to a small `proof_devices:` frontmatter block) is a triage candidate only.

## What happened

`find store -name telehealth.md` → 56-pack cohort denominator. Grepped the standardized
"Health-merchant credibility" / "Payment & commitment" lines for four device families
(clinician credentialing, regulatory/legal seals, efficacy/outcome claims, commercial-trust),
classified each positive vs negated, and joined `anchor_category` per domain for a by-category
cross-tab. Wrote `read.md` + one derived receipt. No fetch, no Firecrawl, no `store/` mutation.

## Inputs and scope

- **Store slice:** all 56 `store/<domain>/telehealth.md` cohort packs (54 carry the explicit
  credibility cut; 2 phrase it differently, read by hand). Per-`captured_at` clocks span
  ~2026-05-30 → 2026-06-20.
- **Devices read:** LegitScript, PCAB/ACHC/NABP, 503A/503B lane, named clinicians/medical
  director, board-certified, FDA-approved/registered, CLIA, cancel-anytime, money-back/outcome
  guarantee.
- **Exclusions:** non-telehealth store domains (luxury, SaaS, VC, aerospace — no telehealth.md);
  external verification of any device (disallowed by contract).
- **Receipts:** `receipts/proof-device-sweep-2026-06-20.md` (S1; C1–C5).

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
# For bounded-live, paste the selected Scout plan here.
```

## Live evidence used

Required for every outside source used in `bounded-live`. Leave `[]` for local-only runs.

```yaml
live_evidence_used: []
# For bounded-live entries:
# - source_or_query:
#   source_family:
#   action_taken: searched | opened | captured | scraped | read-local-signal
#   reason:
#   source_grade: primary | secondary | direction-finding
#   captured_at:
#   spend_note: none | free | paid-credit
#   claim_ids_supported: []
```

## Friction log

- The device checklist lives in **cohort-pack prose**, not frontmatter, so every tally is a
  grep-and-classify pass with manual positive-vs-negated disambiguation. A `proof_devices:`
  frontmatter block would turn the whole read into a one-line query. (Same prose-grain friction
  flagged by run 019.)
- No single helper aggregates a cohort-pack cut; this is the read-recipe gap already tracked as
  MRL-002.

## Evidence limits

- Tallies are ±2–3 directional (prose classification); the *pattern* is robust, the integers are
  not decision-grade.
- Every count is **device-presence on captured pages** — not claim-truth, and "not shown" ≠
  "absent." Capture depth bounds the "not shown" set; a deeper re-capture could move cells.
- The cohort itself is a selected sample (MRL-001 selection-bias), so this is the *captured*
  cohort's proof-device norm, not an adjudicated market norm.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no fetch, no spend, no `store/` mutation, no truth-verification)
- Required citations / receipts present and source-graded: **pass** (S1, derived/local-store)
- No snippet treated as evidence: **pass** (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no current-claims; pack `captured_at` clocks noted)
- Absence language says "not found", not "not true": **pass** (every "not shown" framed as not-found-on-captured-pages)

## Surprises

The proof-device cut **already exists** in the store — I expected to extract it from scattered
`profile.md` prose, but the `telehealth.md` pack has been quietly capturing a standardized
LegitScript / clinician / accreditation / lane checklist with explicit y/n flags all along. That
turns the design question from "should we capture proof devices?" to "should we *promote* an
existing prose cut to structured frontmatter?" — a much smaller, depth-backfill-shaped question.

## Pressure tags

Short `kebab-case` tags for system pressure this run exposed. These are recurrence handles, not a fixed taxonomy and not permission to build.

Use an existing tag when it fits; coin a narrow tag only when the guide misses the thing.

| Tag | Use when |
|---|---|
| `denominator-reconciliation` | The answer depends on defining / cleaning / reconciling the company or source **set**. |
| `source-rigor` | Source grade blocks confidence: snippets, weak secondary sources, missing URLs, or missing capture dates. |
| `source-panel` | A repeated external source **set** seems needed to answer this kind of question. |
| `coverage-caveat` | Store coverage, stale captures, or incomplete modules materially limit the answer. |
| `depth-backfill` | A specific field/module is missing across otherwise relevant companies. |
| `query-time-grouping-enough` | The read was answerable by grouping existing store evidence; no durable category object is needed. |
| `freshness-monitoring` | Current pricing, news, policy, regulation, or launch motion could change or materially improve the answer. |
| `relation-pressure` | Competitors, named parents, suppliers, partners, or other counterparties seem repeatedly useful. |
| `tooling-ergonomics` | Repeated manual steps suggest a helper, query recipe, or template tweak. |

Which tags fired, if any? Did this run need a new or clearer tag?

"No new primitive needed" is a valid outcome.

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `query-time-grouping-enough` | The proof-device read was answerable by grouping an existing cohort-pack cut; no durable proof-device object needed. | no-op — reinforces the standing pattern (17th run to land here) |
| `source-rigor` | The cut is brand-asserted device-*presence*, explicitly not claim-truth; positive/negated split is grep-classified. State/Judgment boundary is the load-bearing caveat. | watch — folds into MRL-008 (a new flavor: device-presence is State, device-credibility is Judgment) |
| `tooling-ergonomics` | Aggregating a cohort-pack cut is a manual grep-and-classify pass; no helper. | watch — folds into MRL-002 (cohort-pack read recipe) |
| `depth-backfill` | The device checklist is consistent prose across ~54 packs but lives below frontmatter; a small `proof_devices:` block would make it a one-line query. | submit watch — candidate field-promotion, NOT built here |
| `coverage-caveat` | "Not shown" is capture-depth-bounded; cohort is a selected sample (MRL-001). | no-op — standing caveat |

## Triage submissions

Loop 1 surfaces these as **candidates for Loop 2 to weigh**; no implementation, no graduation.

1. **MRL-008 (existing) — add a flavor note:** for a Judgment-adjacent evidence layer (proof
   devices), the *presence* of a device is capturable owned-page State, but its *credibility /
   differentiation* is Judgment that must not be hardened or scored. Mirrors the run-019
   visual-layer finding (aggregate the prose, not the verdict).
2. **MRL-002 (existing) — 7th read surface:** "aggregate a cohort-pack credibility cut" joins the
   list of reads that want a cohort-pack query recipe; reinforces the prose-grain wrinkle.
3. **Watch only — proof-device field promotion (relates to MRL-003 depth-backfill):** ~54 packs
   already record LegitScript / clinicians / accreditation / lane consistently in prose; *one
   sighting* of "this should be frontmatter." Do **not** graduate — needs recurrence before it's
   worth the schema churn, and the prose form preserves the honest "not shown" nuance a boolean
   would flatten.

## Next-run advice

- This is the 17th store-only cohort cut to land on `query-time-grouping-enough`. The signal is
  saturated; the marginal design return on another telehealth cohort cut is low. **Bias the next
  Scout toward the genuinely under-tested directions:** generalization beyond telehealth (needs a
  capture-first run to give a second cohort real depth), or external-corroboration `bounded-live`.
- If a future run wants the proof-device field promoted, gather the *second and third* sightings
  first — don't graduate on this one.
- Avoid re-running any device-presence read as if it measured trustworthiness; the State/Judgment
  line is the whole discipline here.
