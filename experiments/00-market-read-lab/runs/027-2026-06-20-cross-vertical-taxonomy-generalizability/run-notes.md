# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [query-time-grouping-enough, schema-edge-entity-type, denominator-reconciliation, coverage-caveat]
```

> **Loop 2 outcome (2026-06-20):** Reviewed via a 3-pass adversarial workflow (evidence
> verifier + consumer + developer, Sonnet). **Verifier: PASS** — independently re-derived
> every load-bearing count from `store/*/profile.md` (7 Investor/Holding firms; the 4-way
> `offering_category` split; gating rule honored 3/7; `business_model: Other` exactly once
> store-wide = blueowl; 126 `profile.md` across 135 dirs). No overclaims; absence
> discipline and State/Judgment boundary clean. **Consumer: partly valuable** — high
> roadmap value, low direct reader value; an honest internal schema audit, the lab's first
> read outside telehealth, earns its slot via engine learning not a deliverable. **Developer:
> submit-triage** — new item **MRL-015** (Investor/Holding encoding under-specified; prefer
> a gating convention over a new value) + **G2 evidence onto MRL-001** (directory count 135
> ≠ profiled 126). Cross-run discovery ledger appended (O1–W1, F1). No graduation, no
> `store/` mutation, no `Human Notes` touched.

## 30-second operator read

- **Did the run work?** Yes — first lab read of the **non-telehealth slice** (26/26 prior
  runs were telehealth-internal). Clean calibration result: the universal taxonomy is
  **not broadly telehealth-overfit**. It carries watches, SaaS, consumer, auto, and
  marketplace rows cleanly (escape hatches almost unused). It has **one** structural
  break — and it's not telehealth-shaped: **capital allocators** (7 `Investor / Holding`
  firms produced **4 different `offering_category` encodings**; the store's only
  `business_model: Other` is blueowl's AUM-fee row).
- **What was awkward?** Nothing mechanical (pure frontmatter grep). The one judgment
  discipline: most `# STRAIN` markers store-wide are **brand_color/logo** capture-fidelity
  notes, not taxonomy strains — the contracted failure-mode trap. Partitioned them and
  read only the ~6 classification-field strains.
- **What should the next agent know?** The taxonomy's edge is a **non-offering entity
  type**, not a vertical. The schema already anticipated it (`Investor / Holding` +
  gating rule) but the rule is under-specified — 7 firms, 4 encodings. Also surfaced a
  denominator caveat: **9 of 135 store dirs are capture-only stubs** (no profile.md), so
  profiled N = 126.

## What happened

Built the non-Healthcare roster from `primary_industry` buckets, pulled the 5
classification fields for the 7 `Investor / Holding` firms + 7 watch brands + a SaaS
sample, ran a store-wide `# STRAIN` and `Other` census, and detected the 9 capture-only
stubs. Read SCHEMA/TAXONOMIES for the closed-set + gating rules. No external sources, no
spend, no mutation. See `read.md` + receipt R1.

## Discovery ledger

Greedy raw learning for this run. Preserve singletons here before triage compresses
anything, then Loop 2 appends the useful rows to `discovery-ledger.md`. Do not merge
rows, dedup into backlog items, or translate wishes into build proposals inside the run.

Use short IDs such as `O1`, `W1`, `F1`, `S1`, or `G1` so reviews can cite them.

| ID | Kind | Raw observation / wish / friction / surprise / gap | Evidence or pointer | Why it matters | Discovery clock |
|---|---|---|---|---|---|
| O1 | observation | The universal taxonomy is **not telehealth-overfit**: watches (7), SaaS (~22), consumer, auto, marketplace all classify with the closed sets and almost no escape hatches. | read.md Result/Gap Map; receipt R1 (C2, C3) | Positive calibration evidence for the engine's central "universal fields + reusable cuts" claim — first time tested outside the design vertical. | ready-for-triage |
| O2 | observation | The one structural break is **capital allocators** (`Investor / Holding`), a non-offering entity type — not a vertical/industry. | read.md Result; receipt R1 (C4) | Reframes where the schema's edge actually is: entity-type scope, not telehealth bias. | ready-for-triage |
| S1 | surprise | 7 `Investor / Holding` firms produced **4 different `offering_category` encodings** (`[]`, `[Financial]`, `[Financial, Services]`, `[Services]`); the gating rule ("leave empty") was honored only **3/7**. | read.md C4; spero-vc:38, thrivecap:34, firstround:44, sequoiacap:40 | Breaks the closed-set grouping promise — you can't filter to "all capital allocators." A recurrence (7 sightings) at the promote threshold. | ready-for-triage |
| S2 | surprise | The store's **only** category-field `Other` store-wide is blueowl `business_model: Other` (AUM fee economics) — *"no taxonomy value fits asset-management fee economics."* | read.md C5; blueowl:35,62 | The taxonomy has no model value for "fees on managed capital"; the lone `Other` marks exactly the allocator gap. | ready-for-triage |
| G1 | gap | No `offering_category` value for *investing / asset management / capital allocation*, and no `business_model` value for *AUM/fee economics*. | read.md What Would Change; TAXONOMIES.md | The structural root of S1/S2 — the missing-value, not a misclassification. | ready-for-triage |
| G2 | gap | **9 of 135 store dirs are capture-only stubs** (no `profile.md`): belmarpharmasolutions, ddpmedical, dewittpharma, exaveyra, mdpep, medsupplysolutions, norexi, pfizerpro, stemnova. | read.md C6; `ls store/<stub>/` | Profiled N = 126, not 135. Any directory-count denominator over-counts profiled cos by ~7% — an MRL-001-flavored caveat surfaced incidentally. | recur-watch |
| O3 | observation | The majority of store-wide `# STRAIN` markers are `brand_colors`/`logo`/`design_framework` notes (Firecrawl branding-payload corrections), **not** classification strains. | `grep -rn STRAIN store/*/profile.md` | Conflating capture-fidelity strain with taxonomy strain would overstate the problem ~4×; they are orthogonal layers. | notice-only |
| W1 | wish | If anything graduates, prefer an **`entity_type: Investor / Holding`-gated convention** that pins one encoding over adding a new `offering_category` value (which re-imports the "is investing a service?" debate). | read.md What Would Change | Names the lighter fix consistent with the anti-sprawl taxonomy posture (fix with a rule/gating, not a new value). | recur-watch |

## Inputs and scope

- **Slice:** all `store/*/profile.md` (135 dirs → 126 profiled). Non-Healthcare operating
  cos (~54) + 7 `Investor / Holding` + 7 watch brands; SaaS sample of 6; full census for
  the headline counts (investors, watches, stubs, `Other`).
- **Fields read:** `entity_type`, `offering_category`, `business_model`, `portfolio_shape`,
  `primary_industry` + inline `# STRAIN` comments.
- **Contract docs:** `TAXONOMIES.md`, `SCHEMA.md` (closed sets, gating rules, maker-vs-reseller).
- **Exclusions:** no external sources; the telehealth Healthcare slice (~64) read only for
  contrast counts, not enumerated.

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
# For bounded-live, paste the selected Scout plan here.
# Default light ceilings: 2 source families, 6 outside sources read/captured,
# 20 paid capture credits. Lower if Scout set a tighter plan.
# Fail closed before exceeding the ceiling, adding an unplanned source family,
# broadening into search/crawl, or using login/paywalled/private sources.
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

Minimal. Building the slice needed a roster loop (`primary_industry` bucket) then a
per-field grep; no single "give me the classification table for cohort X" helper exists.
One sighting only — recur-watch, not a tooling ask. The 9 stubs were found incidentally
(empty `primary_industry` resolved to "no profile.md"), not by a hygiene check.

## Evidence limits

- store-only and intrinsic: says nothing about market completeness — only how the schema
  behaves on captured rows.
- The SaaS rows are an illustrative sample; the load-bearing counts (7 investors, 7
  watches, 9 stubs, 1 `Other`) are full store-wide enumerations.
- Consistency-of-encoding is what's audited, not whether each individual call is the
  single best fit.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live browsing, no spend, no store mutation)
- Required citations / receipts present and source-graded: **pass** (receipt R1, derived/local-store)
- No snippet treated as evidence: **pass** (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **n/a** (no current claims; all durable State)
- Absence language says "not found", not "not true": **pass** ("no taxonomy value fits", "9 stubs not yet profiled")

## Surprises

The slate expected to find telehealth-overfit classification fields; instead the
operating-company taxonomy generalized cleanly and the single break was an orthogonal
axis (capital-allocator entity type). The 4-way encoding split on a single entity_type,
and blueowl being the lone store-wide `Other`, were the sharp surprises (S1, S2).

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

Coined one narrow tag — **`schema-edge-entity-type`**: fires when a classification field
breaks or improvises not because of a *vertical* but because of a *non-offering entity
type* (investor/holding, nonprofit, government) that the offering-centric closed sets
weren't shaped for. The existing tags (`depth-backfill`, `denominator-reconciliation`)
don't capture "the value set has no slot for this *kind of entity's* economics."

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `query-time-grouping-enough` | For operating-company verticals (watches, SaaS, etc.) the closed sets group cleanly at query time — no new category object needed. | no-op — positive calibration; the universal layer holds |
| `schema-edge-entity-type` (new) | 7 `Investor / Holding` firms → 4 `offering_category` encodings + the only store-wide `business_model: Other`; gating rule honored 3/7. | submit triage candidate — recurrence (7) at the promote threshold; prefer entity-type-gated convention over a new value |
| `denominator-reconciliation` | 9 of 135 store dirs are capture-only stubs; profiled N = 126. | watch for recurrence — append as MRL-001 evidence (directory ≠ profiled company) |
| `coverage-caveat` | The allocator break may be the first found, not the only one; only a small non-telehealth slice is captured. | watch for recurrence — a larger non-telehealth capture pass would test for more edges |

## Optional triage evidence

Normally none. Add only concrete backlog evidence, with priority/status suggestions,
when the run has more than a raw singleton or when review adds evidence to an existing
item. Keep this to 1-3 backlog-ready bullets plus pointers to the Discovery ledger,
`discovery-ledger.md`, or run artifacts.

**Do not implement, spike, or recommend immediate graduation from inside the run.**
Raw learning belongs in the run Discovery ledger and `discovery-ledger.md`. Submit
triage only when the run adds enough evidence for a stewarded backlog item or Evidence
Log entry.

## Next-run advice

- **Loop 2:** the load-bearing review question is whether the capital-allocator finding
  is mature enough for a triage candidate (a new `schema-edge-entity-type` item or
  evidence onto an existing taxonomy item) vs. recur-watch. 7 sightings / 4 encodings is
  a strong recurrence signal. Also append G2 as MRL-001 evidence (directory ≠ profiled co).
- **Avoid** re-running this as another telehealth cut — the value here was *leaving* the
  design vertical. A natural follow-up is the nonprofit/`.org` entity types (norexi-org,
  home-medvi-org) to test whether `schema-edge-entity-type` recurs on a second
  non-offering entity kind.
- **Re-check** the 9 stubs before any "N captured companies" claim; they inflate
  directory counts.
