# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         store-only
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [query-time-grouping-enough, denominator-reconciliation, coverage-caveat]
```

> **Loop 2 outcome (2026-06-19):** Reviewed via a 3-pass adversarial workflow (evidence
> verifier + consumer + developer, Sonnet). **Verifier:** independently re-derived all five
> load-bearing counts from `store/*/telehealth.md` (5/54 insurance; 2/54 FDA-brand-only;
> TRT 0/8 async vs GLP-1 12/19 async; access_model per-cohort; Nurx+One Medical both-axes
> overlap) with **zero factual discrepancies**; store-only discipline **PASS**. Two cosmetic
> notes (enum `membership-required` shortened to "membership"; TRT 2/8 hybrid omitted from
> the C3 headline) — **both fixed in `read.md`**. **Consumer verdict: valuable** — first
> cross-cohort synthesis; the "table-stakes are the *worst* durable-State candidates"
> inversion is a hard-to-get-elsewhere insight; agnostic claims robust to the partial
> denominator, cohort-specific percentages are floors. **Developer verdict: watch-for-
> recurrence** — State/Judgment boundary held cleanly at cross-cohort grain; the
> persistence-boundary heuristic is real but one-run and needs a 2nd sighting on a different
> field family to harden. **Triage:** appended additive Evidence Logs to **MRL-002**
> (cross-cohort axis + persistence-boundary heuristic) and **MRL-001** (5th-cohort, first
> cross-cohort under-count). No new item; no graduation.

## 30-second operator read

- **Worked.** First **cross-cohort** read in the lab (008–014 are all single-cohort). One
  grep+group+label pass over 54 brands' `telehealth.md` structural frontmatter. Store-only,
  zero spend.
- **Headline:** 2 mechanics are cohort-agnostic table-stakes (cash-pay rail — only 5/54
  bill insurance; compounding-capable — only 2/54 FDA-brand-only), 3 are cohort-specific
  and track the *condition's* clinical shape (modality: TRT 6/8 sync vs GLP-1 12/19 async;
  bundling wedge; audience). The two exceptions on *both* agnostic axes are the same brands
  (Nurx, One Medical — the insurance-taking, FDA-only "real clinic" model).
- **Next agent should know:** the design answer is **no new cross-cohort primitive** — and
  the *reason* is the interesting part: a mechanic is "table-stakes" precisely when it's
  near-constant, and near-constant = low-information = a useless stored cut. "Table-stakes"
  and "durable-State candidate" are in tension. Price-publication (5th mechanic) was left
  on prior-run secondary footing on purpose — it's a 66-file prose column, not a clean
  enum, and re-deriving it risks the MRL-009/010 trap.

## What happened

Scout selected the cross-cohort table-stakes question (C1) over single-cohort recurrence
candidates because the cross-cohort *axis* closes a persistence-boundary design decision no
single-cohort run can. Loop 1: parsed `telehealth.md` frontmatter for 54 brands
(`anchor_category`, `pay_model`, `access_model`, `compounding_posture`, `modality`,
`audience`); grouped by cohort; tabulated value distributions; labeled each mechanic
agnostic vs specific against quoted verbatim counts. Wrote `read.md` (State/Judgment
separated) + one derivation receipt. No external sources, no spend, no `store/` mutation,
no durable object created.

## Inputs and scope

- `store/*/telehealth.md` frontmatter — **54** files carry the full structured field set
  (of 135 store companies). Parsed first `---…---` block per file. (C1–C5; receipt S1.)
- Cohorts scored at n ≥ 3: GLP-1 19, multi/none 10, longevity/NAD 8, TRT 8, sexual-health
  3. peptides (2) + singletons (labs/womens-HRT/hair/primary-care) named as too thin.
- Price-publication (`offerings.md` Visibility column, 66 files) **out of scope** — prior-run
  secondary evidence only (C6).
- Exclusions: no external sources, no Signals layer, no `offerings.md` prose dig, no
  generalists-that-don't-anchor (named as MRL-001 denominator caveat).

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

- The cross-cohort read is the **same MRL-002 State-read recipe** (latest-capture →
  frontmatter field-extract → group/label) run on a *cross-cohort* axis instead of within
  one cohort. No new toil — one parse pass over 54 files. The recipe family clearly
  generalizes across the cohort axis; reinforces (does not move) MRL-002.
- Price-publication is the one mechanic with no clean field — it's a per-SKU prose column
  in `offerings.md`. Pulling it cross-cohort would be a 66-file dig and would re-introduce
  the re-derive-from-prose error class. Bounded it out deliberately; flagged as C6.

## Evidence limits

- **Anchored-only denominator (MRL-001, 5th cohort sighting, now cross-cohort).** Per-cohort
  n's are floors; generalists that sell into a cohort without anchoring fall only under
  `multi/none`. The cohort-*agnostic* claims (C1/C2) are strengthened by this; the
  cohort-*specific* n's are partial.
- `pay_model: unclear` 7/54 (concentrated longevity 3, sexual-health 1) — cash-pay claim is
  "not stated otherwise," reported as captured value, not absence.
- 81/135 store companies lack structured `telehealth.md` and are outside the matrix.
- The agnostic-vs-specific *labels* are Judgments over a partial, anchored sample, tied
  back to verbatim counts — not laws.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a**
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live browse, no spend, no `store/` mutation, no durable object/field created)
- Required citations / receipts present and source-graded: **pass** (C1–C5 → receipt S1, `source_grade: derived`; C6 labeled secondary)
- No snippet treated as evidence: **pass** (no external snippets; all store frontmatter)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (store clock 06-04→06-18; price-publication explicitly NOT claimed at decision grade — C6)
- Absence language says "not found", not "not true": **pass** (`unclear` reported as captured value; anchored n's framed as floors)

## Surprises

- **Modality is almost a pure cohort property.** TRT is **0/8 async, 6/8 sync** while GLP-1
  is 12/19 async — clean enough that you'd predict modality from the condition, not the
  brand. Not anticipated by the question; surfaced only once the cells were lined up.
- **The two "agnostic-axis" exceptions are the same two brands.** Nurx and One Medical are
  simultaneously the only 2 FDA-brand-only brands *and* 2 of the 5 insurance-billers — a
  single coherent "real clinic" outlier cluster inside a cash-pay/compounded DTC store,
  not two unrelated exceptions.
- The read's design answer flipped the question's framing: the cohort-agnostic mechanics
  are the *worst* durable-State candidates precisely because they're universal.

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
| `query-time-grouping-enough` | The whole cross-cohort read was grep+group+label over existing frontmatter; no durable cross-cohort category/object needed or wanted. The design finding *is* "don't store the agnostic mechanics." | append Evidence Log to **MRL-002** — recipe family generalizes to the cross-cohort axis; adds a persistence-boundary heuristic (near-constant ⇒ low-information ⇒ don't store). No-op on graduation. |
| `denominator-reconciliation` | Anchored-only `anchor_category` grep under-counts each cohort; generalists fall only under `multi/none`. 5th cohort sighting — and the **first to show the under-count biting *cross-cohort***. | append Evidence Log to **MRL-001**. |
| `coverage-caveat` | Price-publication (1 of 5 question-mechanics) left on prior-run secondary footing; 81/135 companies lack structured `telehealth.md`; `unclear` 7/54. | watch — a clean cross-cohort price-visibility read would need the 66-file `offerings.md` Visibility extract. Not a triage item yet. |

New tag needed? No. Existing tags covered it.

## Triage submissions

No new triage item. Two additive **Evidence Log** appends for Loop 2 to consider (not
graduation, not canonical-state rewrites):

1. **MRL-002 (State-read query recipes):** the recipe family now demonstrably runs on a
   **cross-cohort axis** (group by `anchor_category` across all cohorts), not just within
   one — a 5th *surface* after price-posture (008), positioning (009), offer-structure
   (010), and structural-access (013). New generalizable nugget: a **persistence-boundary
   heuristic** — a mechanic that is cohort-agnostic *because* near-constant is a *poor*
   durable-State candidate (low entropy), so "table-stakes ⇒ store it" is backwards. Pairs
   with MRL-002's still-recipe-level posture; no helper, no stored cross-cohort object.
2. **MRL-001 (denominator reconciliation):** 5th-cohort recurrence of the
   anchored-only-vs-all-offerers under-count, and the first to show it operating
   **cross-cohort** (every per-cohort n is a floor simultaneously). Reinforces naming the
   anchored-vs-all-offerers cut as a first-class denominator caveat in any future QUERYING
   recipe.

**Do not implement, spike, or recommend immediate graduation from inside the run.**

## Next-run advice

- If anyone wants the price-publication mechanic resolved cross-cohort, it needs the 66
  `offerings.md` `Visibility` columns extracted and labeled — a deliberate, bounded prose
  pass with the MRL-009/010 "quote, don't re-derive" guard. Worth a dedicated run, not a
  bolt-on.
- A **second** cross-cohort read finding the same "near-constant ⇒ low-information ⇒ don't
  store" tension on a different field family would harden this from a one-run Judgment into
  a documented persistence-boundary heuristic — that's the recurrence that would move
  MRL-002, not another single-cohort State read.
- Avoid re-running single-cohort price/offer reads expecting new design signal; MRL-002 is
  saturated at recipe level. The open design edges now are **persistence-boundary** (this
  run) and **relations/neighborhood** (no store frontmatter support yet — would need
  capture, not a query).
