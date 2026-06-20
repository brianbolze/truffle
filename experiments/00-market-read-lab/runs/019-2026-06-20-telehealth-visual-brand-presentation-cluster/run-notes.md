# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [query-time-grouping-enough, source-rigor, coverage-caveat]
```

> **Loop 2 outcome (2026-06-20):** Reviewed via a 3-pass adversarial workflow (evidence
> verifier + consumer + developer, Sonnet). **Verifier: PASS-WITH-FIXES** — independently
> reproduced the panel (34), polarity tally (485/366/148 = 999, 15% poor), depth spread
> (9–51), 6 verbatim impression quotes, and the anchor_category cross-tab clean; **one real
> catch** — the price-transparency decline was wrongly justified as "unparseable / n=0 for
> 21/34," but the `offerings.md` `| Visibility |` column *is* parseable for all 34 (a
> prose-grep matched the wrong form). **Fixed in `read.md` + receipt** (re-framed as a decline
> on *scope* / not-well-formed grounds). No-score discipline clean. **Consumer: valuable** —
> lab's strongest brief-facing output; owned-moat/borrowed-weakness framing is brief-ready,
> ceiling is Judgment-on-Judgments + supply-side. **Developer: submit Evidence Logs, NOT a new
> item** — downgraded the run's proposed new MRL item (one sighting); folded into **MRL-002**
> (6th read surface; prose-grain + independent-convergence wrinkle) and **MRL-008** (new
> flavor: a Judgment-dense layer's structured field should not be aggregated at all). No
> graduation; no `store/` mutation; no Human Notes touched.

## 30-second operator read

- **Did the run work?** Yes. **First lab read to consume the `visual.md` visual-evidence
  layer as a cross-company ingredient** (all 18 priors used telehealth/offerings/profile/
  signals). Store-only, zero spend.
- **What was awkward?** The structured `polarity` field is **not** cross-brand-aggregatable
  (capture-depth + rater confounds), and it is fiddly enough that my first parse miscounted
  the vocabulary (`poor`, not `weak`) — corrected. The usable signal lives in the *prose*
  impression, not the field.
- **What should the next agent know?** The headline is a real, cited category pattern —
  **owned-controlled core, borrowed-asset frays; components are table stakes, owned
  imagery/illustration is the moat, and the borrowed/utility layer is where everyone is
  weak.** The design payload: **the visual layer aggregates at the impression/prose grain,
  not the polarity grain — `query-time-grouping-enough`; no visual-cluster object or score
  rollup.** The no-score boundary held and was workable.

## What happened

Took the 34 store domains with both `visual.md` and `telehealth.md`. Tallied polarity
(strong/mixed/poor) + family per brand and the card-depth spread (9–51). Read all 34 `##
Visual & brand impression` paragraphs and coded them for arc / character / type signature.
Cross-tabbed character against `anchor_category`. Attempted a price-transparency cut from
`offerings.md` `visibility`; **declined** it (n=0 for 21/34 → format variance, not a clean
signal). Wrote `read.md` (State vs Judgment-on-Judgments labeled) + one derivation receipt.
No external sources, no spend, no write-back, no field/object/score created.

## Inputs and scope

- **Panel:** `comm -12` of `store/*/visual.md` ∩ `store/*/telehealth.md` basenames → 34
  domains (store-wide: 135 domains, 44 visual.md, 54 telehealth.md). Floor of 54 telehealth
  brands; the opt-in visual layer covers 63%.
- **Read surfaces:** each brand's `## Visual & brand impression` (the synthesis) + polarity/
  family fields (the audit trail) + `anchor_category` (`telehealth.md`); `visibility`
  (`offerings.md`, declined).
- **Exclusions:** 20 telehealth brands without `visual.md` (absent ≠ poor); the 90 non-
  telehealth store domains; demand-side / live evidence (store-only by contract).
- **Receipts:** `receipts/visual-layer-cross-brand-sweep-2026-06-20.md` (S1–S4 / C1–C5).

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

- **No helper to consume the visual layer cross-brand.** Reading 34 impression paragraphs +
  tallying polarity was a hand-rolled python pass. If this read recurs, the reusable shape
  is an **impression-concatenation recipe** (glob `visual.md` → pull `## Visual & brand
  impression` → join `anchor_category`), not a polarity rollup.
- **Polarity vocabulary footgun.** First parse counted `weak` (the contract's *parked-score*
  vocab) and read 0 → wrong; the *instance* negative pole is `poor` (148/999 = 15% on the
  panel). A future visual-layer query recipe should pin the instance vocab (strong/mixed/
  poor) explicitly.
- **`offerings.md` `visibility` is not quick-parseable** — per-row prose format varies, so a
  one-liner under-counts. Reliable extraction is the MRL-001/MRL-002 job.

## Evidence limits

- **Judgment-on-Judgments.** `visual.md` is a Judgment-dense layer (synthesized impression +
  interpreted "visible tells"); my cross-brand clustering compounds that. Its trust rests on
  *independent convergence* of separately-mined captures, not on any single rater.
- **Polarity cannot rank brands** — capture-depth (9–51 cards) + rater-compression confounds.
- **34/54 telehealth floor**, opt-in layer; absent ≠ poor.
- **Price-transparency correlation not assessed** (declined); not-assessed ≠ no-relationship.
- **Supply-side only** — "premium" = visual control, not market outcome.

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
- No disallowed action happened: **pass** (no live browse, no spend, no `store/` mutation, no
  durable primitive, **no visual-quality score/grade/ranking** — clusters are cited patterns)
- Required citations / receipts present and source-graded: **pass** (S1–S4, `derived`/local-store)
- No snippet treated as evidence: **pass** (all evidence is local store files)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no
  current/news claims; visual capture clocks 2026-06-15→06-18 recorded)
- Absence language says "not found", not "not true": **pass** (20 missing visual layers framed
  as opt-in floor / absent≠poor; price cut framed as not-assessed≠no-relationship)

## Surprises

- **The independent convergence is the real evidence.** 30+ separately-mined captures land on
  the *same* owned-vs-borrowed sentence almost verbatim — that the per-company miners didn't
  coordinate is what makes the cross-brand pattern trustworthy despite the layer being
  Judgment-dense.
- **The delta-able field is again the least useful one** (echoes run 018): the structured,
  greppable `polarity` field is exactly what does *not* aggregate; the unstructured prose is
  what does. The reusable grain is the opposite of the convenient grain.
- **Components have commoditized.** Nearly every brand — premium or budget — has a clean,
  repeatable component kit. Visual differentiation has fully migrated to owned production +
  editorial type; the category competes on a narrower axis than expected.

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
| `query-time-grouping-enough` | First consumption of `visual.md` cross-brand. The read was answerable by globbing impressions + grouping at query time; **no durable visual-cluster object** needed. Extends the MRL-002 recipe family to a **fifth source surface** (`visual.md`), but with a twist: the aggregatable grain is **prose, not a field**. | submit candidate (new item) — name visual-layer cross-brand consumption as query-time-grouping-enough at the *impression grain*; reinforce MRL-002. No helper/object yet. |
| `source-rigor` | New flavor: a **Judgment-dense layer's structured field (`polarity`) does not aggregate** into a cross-brand discriminator (depth + rater confounds); only the *prose* impression does, and only via independent-convergence. Distinct from MRL-008's captured-Signal confounds (those are State fields with integrity siblings; this is a Judgment field that shouldn't be summed at all). | append Evidence Log → MRL-008 (interpreted-layer flavor) and fold into the new item. |
| `coverage-caveat` | 34/54 telehealth brands have `visual.md` (opt-in, 63% floor); capture depth 9–51; 2 QA exclusions. | reinforce; no-op. |

New tag needed? **No.** Existing tags fit; the new *content* is "interpreted/Judgment-dense
layer aggregates at the prose grain, not the field grain," captured under `source-rigor` +
`query-time-grouping-enough`.

## Triage submissions

For Loop 2 to weigh (append Evidence Logs / propose; do not implement):

1. **New candidate — visual-evidence layer as a cross-brand ingredient (suggest P3,
   `Submitted`, area: source-panel/query-recipe).** First lab consumption of `visual.md`
   cross-company. Finding: it **does** aggregate into a trustworthy creative-director
   category read (owned-core/borrowed-frays; 3 characters; italic-serif signature) — **but
   only at the `## Visual & brand impression` prose grain**, via independent convergence of
   separately-mined captures. The structured `polarity`/`family` fields **do not** roll up
   (capture-depth 9–51 + rater confounds; `%poor` 0–56% is noise on thin files). The
   no-score boundary (`modules/VISUAL.md`) **held and was workable**. Proposed framing:
   hold for a 2nd cross-brand visual read (different cohort); if it recurs, the reusable
   shape is a documented **impression-concatenation QUERYING recipe** (glob `visual.md` →
   pull impression → join `anchor_category`) — explicitly **not** a polarity-score rollup,
   a `visual_cluster:` field, or a durable cluster object. Link: MRL-002, MRL-008.
2. **MRL-002 (reinforce):** extends the State-read recipe family to a **fifth source
   surface** (`visual.md`) after price/positioning/offer/access — with the new wrinkle that
   the aggregatable unit is **prose, not a greppable field.** Recipe-level; no helper.
3. **MRL-008 (Evidence Log):** interpreted-layer flavor of "headline field misleads" — a
   Judgment-dense layer's structured field (`polarity`) is not just confounded but
   **should not be aggregated at all**; the trustworthy grain is the cited prose synthesis.

**Do not implement, spike, or recommend immediate graduation from inside the run.**

## Next-run advice

- The natural 2nd sighting is a **cross-brand visual read on a different cohort** (or the
  same panel after a depth-normalized re-mine) — to test whether the *prose-aggregates /
  polarity-doesn't* finding holds, and whether `%poor` becomes usable once capture depth is
  fixed.
- A **bounded-live** corroboration (a "best-designed telehealth sites" listicle panel, or
  owned "vs" pages) would test the three-character clustering + the soft positioning
  correlation demand-side (cf. run 012's listicle-as-coverage-radar).
- **Avoid** leaning on polarity counts as a quality ranking in any future read, and avoid
  re-deriving the price-transparency cut without the MRL-001/MRL-002 denominator work.
- If a human wants the brief-facing version, the impression corpus + the 3-character coding
  is already the raw material for a creative-director one-pager.
