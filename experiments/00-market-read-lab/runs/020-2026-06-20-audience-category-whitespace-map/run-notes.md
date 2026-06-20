# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [denominator-reconciliation, coverage-caveat, query-time-grouping-enough]
```

> **Loop 2 outcome (2026-06-20):** Reviewed via a 3-pass adversarial workflow (evidence
> verifier + consumer + developer, Sonnet). **Verifier: PASS** — independently reproduced
> 54/54 field coverage, the audience buckets (34/8/7/3/2), the full audience×category grid
> (column totals 15/5/34, grand total 54), and all named sets with **zero discrepancies**;
> caveat discipline clean (no empty cell read as market whitespace; asymmetry never claimed
> as a market fact). **Consumer: valuable** — clearest "beats generic Claude + web" case in
> the lab (verbatim-field enumeration of 54 brands' audience positioning); the coverage
> caveat *adds* trust rather than gutting value; biggest limit is the selection-bias ceiling.
> **Developer: submit MRL-001, watch MRL-002** — the selection-bias denominator flavor
> (corpus-construction-time bias, distinct from the query-time anchored-only under-count) is
> a real sharpening of MRL-001 with a compound-caveat synthesis/guardrails implication;
> downgraded the orthogonal-axis nugget to a *watch* Evidence Log on MRL-002 (one sighting).
> Cosmetic fix: removed a blank duplicate Loop-1-exit-check block. No graduation; no `store/`
> mutation; no `Human Notes` touched.

## 30-second operator read

- **Did the run work?** Yes. Store-only, zero spend. **First lab read to use `audience`
  as the primary axis** — all 20 priors cut by `anchor_category`. 54/54 brands carry both
  `audience` and `anchor_category` verbatim, so the cross-tab fell out of one parse pass.
- **What was awkward?** Nothing in execution. The hard part is *interpretive*: the headline
  pattern (15 men-leaning vs 5 women-leaning brands; TRT/ED all-male) is **doubly coverage-
  bounded** — by intentional cohort selection-bias *and* by the anchored-only under-count —
  so almost the entire risk is over-claiming captured supply as market structure.
- **What should the next agent know?** The honest payload is **a gender-thinness map of the
  *captured store* plus a testable whitespace hypothesis**, not a market whitespace finding.
  Design answer: **`audience` is a clean enum that rolls up trivially → query-time-grouping-
  enough; no audience-cohort object needed** (extends MRL-002 to a 7th, *orthogonal* axis).
  The new design nugget is a **selection-bias denominator flavor** distinct from MRL-001's
  anchored-only under-count (see Pressure tags).

## What happened

Parsed all 54 `store/*/telehealth.md` for `audience` + `anchor_category` (value verbatim,
inline comment stripped, never inferred from brand name per contract). Bucketed audience
into MEN/WOMEN/ALL lean, cross-tabbed against `anchor_category`, pulled the load-bearing
named sets (women-leaning 5; all-male TRT/ED cells; gender-neutral longevity 8; the 10
generalists). Wrote `read.md` (State grid + labeled Judgments + a whitespace stated as
coverage-bounded) and one derivation receipt. No external sources, no spend, no write-back,
no field/object/score created.

## Inputs and scope

- **Panel:** the 54 store domains with a `telehealth.md`; all 54 carry `audience` +
  `anchor_category`. Store-wide there are 135 domains; the other 81 are non-telehealth or
  un-moduled and out of scope by construction.
- **Read surfaces:** `audience` and `anchor_category` frontmatter only (both clean enums);
  field comments consulted for straddler notes.
- **Exclusions:** demand-side / live evidence (store-only by contract); the 81 non-cut
  domains.
- **Receipts:** `receipts/audience-category-crosstab-2026-06-20.md` (S1; C1–C4).

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

- **No friction in extraction** — `audience` and `anchor_category` are both clean,
  greppable enums; the whole cross-tab is one parse pass. This is the *opposite* of run 019
  (visual prose) and run 010 (offer-structure prose): the load-bearing axis here is a
  discrete field, so the MRL-002 "quote-don't-re-derive" guard is trivially satisfied — like
  run 013's discrete-enum access read.
- **The one footgun is interpretive, not mechanical:** the field comment on several brands
  explicitly warns the *name* misleads about audience (`men-first` brands with non-gendered
  weight-loss lines; "read from pages, not the name"). Taking the field value verbatim (not
  the name) is the contract — followed.

## Evidence limits

- **Selection-bias ceiling (load-bearing):** the 15-vs-5 men/women lean asymmetry is bounded
  by the cohort's intentional men's-hormone tilt (prior runs 001/008/014/016 seeded TRT/men's
  captures). This is *not* a market fact and the read says so repeatedly.
- **Anchored-only under-count (MRL-001):** the 10 `multi/none` generalists (8 all-genders)
  serve TRT/HRT/longevity/sexual-health without anchoring, so every per-category audience
  cell is a **floor** — "0 women in TRT" = no women-*anchored* TRT brand captured, not "women
  unserved."
- **`audience` is positioning, not customer mix** — supply-side front-door framing, not a
  measured customer base. Empty cells = not-captured, not market-absent.
- **No demand-side evidence** — thin captured supply ≠ small market.

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
  durable audience-cohort object/field/score, empty cells framed as coverage absence)
- Required citations / receipts present and source-graded: **pass** (S1, derived/local-store)
- No snippet treated as evidence: **pass** (all evidence is local store frontmatter)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no
  current/news/pricing claims; pure State cross-tab)
- Absence language says "not found", not "not true": **pass** (every empty cell framed as
  store-coverage absence + a testable hypothesis, never as market whitespace)

## Surprises

- **GLP-1 is the only category that drew dedicated women-anchored brands** (3 of the 5
  women-leaning brands). The established hormone lane (TRT) is 7/0/1 male; the *new*
  gender-balanced lane is where women-framed wedges actually appeared. Plausible but
  demand-blind.
- **longevity/NAD is 8/8 all-genders** — the single most audience-homogeneous cell. No
  gendered front door at all, contra TRT/ED.
- **The clean, convenient axis was also the *fully* trustworthy one this time** — unlike
  runs 018/019 where "the delta-able/greppable field is the least useful one." `audience`
  rolls up cleanly *and* is decision-relevant; the catch is entirely downstream (coverage
  bias), not in the field grain. Worth noting as a counter-example to the recent "convenient
  grain ≠ useful grain" pattern.

## Surprise caveat note

honehealth is `all-genders`/longevity in the field despite a men's-health brand reputation
(run 017 treated it as a TRT/longevity anchor). Took the field verbatim per contract; flag
only as a reminder that the `audience`/`anchor_category` fields encode the *current captured
front door*, which can lag a brand's market reputation.

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
| `denominator-reconciliation` | New flavor: a **selection-bias denominator** — the whole 15-vs-5 asymmetry is bounded by *which brands the lab chose to capture* (intentional men's-hormone tilt), distinct from MRL-001's anchored-only *under-count* (which brands fall out of a cohort grep). Both bound this read simultaneously. | append Evidence Log → MRL-001 (name the selection-bias flavor alongside the anchored-only flavor). |
| `coverage-caveat` | 54/54 cut, but the cohort is non-representative by construction; every empty cell is coverage-absence. | reinforce; no-op. |
| `query-time-grouping-enough` | `audience` is a clean enum; the cross-tab is one parse pass. Extends MRL-002's State-read recipe family to a **7th surface and the first orthogonal axis** (audience, not category). No audience-cohort object, `audience_cluster` field, or score needed. | append Evidence Log → MRL-002 (orthogonal-axis flavor). |

New tag needed? **No.** Existing tags fit. The new *content* is the **selection-bias
denominator** distinction (captured-set bias vs anchored-only under-count) — a sharpening of
MRL-001, not a new tag.

## Triage submissions

For Loop 2 to weigh (append Evidence Logs / propose; do not implement):

1. **MRL-001 (Evidence Log):** name a **selection-bias denominator** flavor. Prior MRL-001
   entries all track the *anchored-only under-count* (brands that fall out of an
   `anchor_category` grep). This run surfaces a structurally different denominator risk: the
   captured *cohort itself* is non-representative (intentional men's-hormone tilt), so a
   whitespace/asymmetry read is coverage-bounded **before** any grep. A future QUERYING recipe
   for whitespace/asymmetry reads must carry **both** caveats: cohort-selection bias *and*
   anchored-only under-count.
2. **MRL-002 (reinforce):** 7th read surface, and the **first orthogonal axis** — every prior
   State-read cut by `anchor_category` (or its straddlers); this cut by `audience` and
   cross-tabbed *against* category. Confirms the recipe family generalizes to a second clean
   enum with no new toil. Recipe-level; no helper, no audience-cohort object.
3. **No new MRL item proposed.** A whitespace/audience read is `query-time-grouping-enough`;
   the design lesson folds into MRL-001 + MRL-002. Hold for a 2nd audience-axis read before
   any QUERYING recipe graduates.

**Do not implement, spike, or recommend immediate graduation from inside the run.**

## Next-run advice

- The natural 2nd sighting is **any second audience-axis or whitespace read** (different
  cohort, or audience × pricing/offer), to test whether the selection-bias caveat and the
  clean-enum roll-up hold.
- The **bounded-live** corroboration is the high-value variant: a "best women's telehealth
  2026" listicle panel + a few owned women's-health sites would test whether the dedicated-
  women's-hormone/longevity whitespace is real market or just store-absent (mirrors run 012's
  listicle-as-coverage-radar). That is the only way to convert the hypothesis into a finding.
- **Avoid** repeating any reading of the 15-vs-5 asymmetry as a market fact, and avoid
  treating empty audience×category cells as proven whitespace without a live denominator.
