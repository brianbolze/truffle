# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [relation-pressure, query-time-grouping-enough, denominator-reconciliation, depth-backfill, source-rigor]
```

## 30-second operator read

- **Did the run work?** Yes. Clean gap-probe result: the store can reconstruct the SaaS
  competitor neighborhood, but only from `description` prose (LLM judgment) + a minority of
  competitor-naming body lines — not from any structured field. The horizontal-relation
  axis is absent; the vertical (`parent`/`owns`) axis is rich but has a consistency gap.
- **What was awkward?** The `primary_industry: Technology` draw pulls in 4 non-SaaS entities
  (apple, casio, eightsleep, upwork); had to hand-filter. Competitor prose is at three
  different grains across profiles.
- **What should the next agent know?** "No new primitive needed" stays the honest answer —
  a competitor field would be mostly empty/dangling because the named rivals are off-store.
  The condition that would flip it is named in read.md (capture a few rivals → edges become
  fillable).

## What happened

`grep primary_industry: Technology` → 23 profiles → pulled frontmatter
(`offering_category`/`target_market`/`business_model`/`parent`/`owns`/`description`) →
confirmed structured fields can't separate sub-markets → clustered by description prose
(7 sub-markets, flagged as judgment) → grepped bodies for competitor naming and read the
hits → cross-checked named rivals vs `ls store/` (mostly off-store) → compared the
Grammarly/Coda/Superhuman ownership records. Receipt: `receipts/01-tech-slice-neighborhood.md`.

## Observations

Greedy raw learning for this run. Preserve singletons here, then Loop 2 appends the
useful rows to `learning/observations.md`. Do not merge rows, dedup into backlog items,
or translate wishes into build proposals inside the run.

Use short IDs such as `F1`, `S1`, `W1`, `G1` so reviews can cite them. Kinds are the
closed set: `friction` · `surprise` · `wish` · `gap` · `risk-miss` · `brian-correction`.
Record the symptom in `Saw`; put the boundary you are deliberately not asserting in
`Not claiming` (no fix, no build proposal).

| ID | Kind | Saw | Not claiming | Evidence pointer | Tags |
|---|---|---|---|---|---|
| S1 | surprise | The store splits cleanly on the relation **axis**: it has a first-class **vertical** relation primitive (`parent`/`owns`, rich on this slice — Qualtrics/Delighted, Twilio/SendGrid+Segment, AlphaSense/4 acquisitions) but **zero horizontal** relation (competes-with / substitute / same-sub-market). The competitor neighborhood is structurally invisible while ownership is structurally first-class. | That a horizontal relation field should be built — only that the store's relation support is axis-asymmetric. | read.md Result/Gap Map; parent/owns frontmatter | relation-pressure |
| G1 | gap | **L005 failure-side, first sighting.** Structured fields (`offering_category` one bucket for ~19, `target_market` mostly `[B2B]`, `business_model` mostly `Subscription`) cannot resolve the ~7 sub-markets in the SaaS slice. Every prior L005 confirmation had the corpus *already carrying the cut*; here the corpus does not, so query-time grouping by the enum yields one undifferentiated pile. | That `offering_category` is broken — it's a coarse leaf working as designed; the note is that grouping-by-enough fails when the enum has no sub-market leaf. | read.md Result(1); frontmatter grep; lessons L005 | query-time-grouping-enough, relation-pressure |
| G2 | gap | Competitor neighborhood **is** carried — but only in **prose**, in ~5/23 bodies, at three different grains (Datadog clean list; Gong per-product; Dovetail comparison-page set; Listenlabs legacy+AI-native; Clari category posture only) — and the named rivals are **mostly off-store** (New Relic, Salesloft, Condens, Outset… uncaptured). So even where named, the edges dangle outside the slice. | That the store should capture those rivals or add a competitor field — only that the edge data is prose-grade, uneven, and points outward. Spend/approval-gated. | read.md Result(3)/Source Gaps; datadog:74, gong:59-60, dovetail:85, listenlabs:121 | depth-backfill, source-rigor, relation-pressure |
| G3 | gap | M&A-chain **consistency** gap: the same Grammarly→Coda→Superhuman acquisition is recorded two ways — `coda.io` `parent: [grammarly.com]` vs `superhuman.com` `owns: [coda.io]` ("Grammarly rebranded"). A reader asking "who owns Coda" gets different owners from different profiles; both STRAIN-flagged, neither reconciled. | That the captures are wrong — both are page-attested and honestly flagged; only that the vertical relation has no cross-profile reconciliation, so chains can read inconsistently. | read.md Result; coda.io parent + superhuman.com owns | relation-pressure, source-rigor |
| S2 | surprise | The `primary_industry: Technology` draw is a **leaky cohort key**: it returns apple, casio (hardware), eightsleep (smart hardware), upwork (`Marketplace / Platform`) alongside the ~19 genuine SaaS profiles. A naive industry-draw silently contaminates a SaaS neighborhood with 4 non-SaaS entities. Mirror of run-036 G3 / run-037 G2 (industry is the wrong key for entity-shape cohorts), now on the SaaS slice. | That industry should be re-tagged — the tags are individually defensible; only that an industry draw is not a SaaS-cohort key. | read.md Companies Seen; grep result | denominator-reconciliation |
| W1 | wish | If anything ever graduates from S1/G2, the lightest path is a **query-time recipe** ("read `description` + grep competitor body-lines for the sub-market") — NOT a competitor field or a sub-category enum level. Load-bearing reason: a competitor field would be mostly empty/dangling today (named edges off-store), failing the "a field is a cut you can fill reliably" bar. Mirrors the run-036/037 anti-sprawl W1 landings. | That it should graduate now — only the lightest path *if* a real cross-company neighborhood consumer appears AND the named rivals get captured. "No new primitive needed" stays live. | read.md What Would Change; engine-dev "every field is a cut" | query-time-grouping-enough, relation-pressure |

## Inputs and scope

- **Slice:** 23 profiles from `grep -rl "^primary_industry: Technology" store/*/profile.md`,
  hand-filtered to ~19 genuine SaaS (excluded apple, casio, eightsleep, upwork).
- **Fields read:** `domain`, `offering_category`, `target_market`, `business_model`,
  `description`, `parent`, `owns` (frontmatter); competitor-naming body lines via
  `grep -icE "competitor|compete|alternative to|vs\.|versus|rival"`.
- **Cross-check:** named competitors vs `ls store/` for in-store/off-store.
- **Exclusions:** no external sources, no live browsing, no `store/` mutation (per contract).
- **Denominator:** captured Technology slice — explicitly partial and capture-biased; not
  the SaaS market.

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

- `primary_industry: Technology` is not a SaaS-cohort key — hand-filtering 4 non-SaaS
  entities was required (S2). No structured way to draw "SaaS apps" cleanly.
- Competitor evidence had to be grepped out of free-text bodies and read line-by-line; no
  field surfaces it, and grain differs per profile.

## Evidence limits

- The 7-cluster sub-market map is **LLM judgment over prose**, labeled as a Judgment in the
  read — a different reader could draw boundaries differently.
- Competitor-edge census is bounded by what each captor wrote; absence of a competitor line
  means "not captured," not "no competitor."
- Captured slice is partial and capture-biased; all counts describe the store, not the market.

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
- No disallowed action happened: **pass** (no external sources, no mutation, no primitive)
- Required citations / receipts present and source-graded: **pass** (receipt 01, C1-C5)
- No snippet treated as evidence: **pass** (all local store State)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no current/external claims made; structural read only)
- Absence language says "not found", not "not true": **pass** ("not in the captured slice" used throughout)

## Surprises

- The store's relation support is **axis-asymmetric**: vertical (ownership) is first-class
  and rich; horizontal (competitor) is absent (S1).
- Competitor neighborhood *is* partly captured — in prose — but mostly points to companies
  the store hasn't captured (G2).

## Learning tags

Short `kebab-case` recurrence handles for system pressure this run exposed. They mirror
the run header's `learning_tags`. These are not a fixed taxonomy and not permission to
build — a learning pass decides what, if anything, recurs into a lesson.

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

Which tags fired, if any? Did this run need a new or clearer tag? Mirror them into the
header `learning_tags`.

**Fired:** `relation-pressure` (axis-asymmetric relation support, S1/G2/G3),
`query-time-grouping-enough` (L005 failure-side, G1/W1), `denominator-reconciliation`
(leaky industry key, S2), `depth-backfill` + `source-rigor` (prose-grade uneven competitor
edges, G2/G3). No new tag needed — the guide covered every sighting.

"No new primitive needed" is a valid outcome — and is the honest one here.

## Next-run advice

- A **second non-telehealth slice** (e.g. the survey/feedback sub-cluster on its own, or the
  Energy slice) would test whether S1's axis-asymmetry recurs — moving it from singleton
  toward pattern.
- If a future run wants to *test* the W1 lightest-path recipe, capturing 3-4 named rivals
  (New Relic, Salesloft, Condens) first would make the competitor edges fillable and change
  the calculus — but that is spend/approval-gated, not autonomous.
- Avoid drawing a SaaS cohort by `primary_industry` alone; filter `offering_category` and
  exclude hardware/marketplace entities (S2).
