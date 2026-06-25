# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L001 (bounded-live coverage radar = membership), L005 (query-time grouping enough when
  corpus carries the cut), L006 (price-visibility token grain). Observations show a
  strong recent streak: runs 036–046 are **11 consecutive store-only schema-fit / buyer
  reads** across non-telehealth slices. Saturated tags: `query-time-grouping-enough`,
  `denominator-reconciliation` (n=5 "industry draw ≠ entity-shape cohort key"),
  `schema-edge-entity-type`, and the n=4 **"decision-grade fact lives off the captured
  surface"** frontier (036 G2, 037, 038 G2, 042 G4).
- `scout-context.md`: select for **value + reach + source-family diversity + calibration**,
  not store-answerability. Gap-probes first-class when bounded. The recent streak under-
  tested the **bounded-live / external source-panel** lane and the **horizontal relation**
  frontier (039 found competitor edges are prose-only, dangling off-store; vertical
  ownership is first-class, horizontal absent).
- Last 3 `run-notes.md` files: 044 (usage-based pricing comparability, store-only,
  buyer-primary), 045 (agency schema-fit, store-only), 046 (consumer-goods buyer read,
  store-only). All store-only. **040** (the most recent bounded-live) failed closed on a
  **spend-ceiling breach**: one `parsers:[pdf]` scrape of a 15-page ToS billed 15 credits
  vs a 10-credit ceiling — per-page PDF cost is invisible pre-call (coined tag
  `bounded-live-spend`). Any new bounded-live plan must ban PDF/multi-page parses and cap
  tightly.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **(C1 — SELECTED)** For one under-resolved SaaS sub-market from run-039 (observability, anchor = Datadog), does a light public listicle/SERP panel ("Datadog alternatives", "best observability tools 2026") recover a competitor edge-set, and how does that external set compare to the store's prose-named rivals (New Relic/Dynatrace/Splunk/Grafana/Elastic) and to who's actually captured? | gap-probe | yes | bounded-live | Directly tests 039's horizontal-relation frontier with reach: are competitor edges **cheaply recoverable externally**? That informs the roadmap question behind 039 W1 — should the store ever hold horizontal edges, given they dangle off-store today. | Relation / source-panel: does an external listicle panel recover directed competitor edges the store can't surface structurally; would captured edges be fillable. | Past the cached answer (store carries edges only in ~5/23 prose bodies, mostly off-store) into whether a public panel resolves the neighborhood. | ≥2 independent listicles naming an edge before "external-corroborated"; exact URLs + capture dates + source grade; snippets are leads only. | Sliding from a directed edge-check into open-ended "map the whole observability market" crawl; treating one listicle as the denominator (L004). |
| C2 | In the store's payments/fintech slice, can a competitor neighborhood be drawn from State alone (Stripe vs Adyen vs Braintree…)? | gap-probe | yes | store-only | Tests whether 039's SaaS finding (horizontal absent) repeats on a different sub-market. | relation-pressure | Little — likely re-confirms 039 store-only. | Frontmatter + prose grep. | Just re-running 039 store-only on a new slice (low reach). |
| C3 | Across captured agencies/consultancies (run-045 cohort), do named client logos in `Credibility & proof` resolve to other captured companies (relation-via-proof)? | gap-probe | yes | store-only | A fresh relation *flavor* (client edges, not competitor/parent). | relation-pressure | Modest reach; novel edge type but store-only. | Body-line grep + store cross-match. | Mostly dangling edges (clients off-store), repeating 039 G2's "edges dangle outside the slice." |
| C4 | For a brand whose store pricing is freshness-flagged, does a single live page fetch confirm or refute the captured price? | calibration | yes | bounded-live | Tests the freshness/staleness frontier with one cheap fetch. | freshness-monitoring | Reaches live verification. | One single-page scrape + capture date. | n=1; narrow; little design payload beyond "store can be stale." |
| C5 | Across the captured store, which buyer questions are answerable for a *delegated agent* vs need off-surface sources (synthesize the n=4 "off-captured-surface" frontier into one map)? | calibration | yes | store-only | Consolidates a recurring frontier into a reader-facing map. | source-panel | Low reach (re-reads existing observations). | Existing read.md/observation pointers. | Navel-gazing; re-deriving the learning stream as a "read." Reject. |
| C6 | Does a public "best of 2026" listicle panel for a non-telehealth vertical (e.g. observability) name a default set the store is missing (coverage radar)? | gap-probe | yes | bounded-live | Reader-recognizable coverage check. | denominator-reconciliation | Reaches external membership. | SERP → ≥2 listicles → token-match diff. | **Already graduated as L001** — re-running membership radar adds little; C1 is the *edge* variant, which L001 does not cover. |

## Selected Question(s)

1. **C1** — competitor-edge external recovery for observability (anchor Datadog). It is
   the highest value + reach + source-diversity pick: it breaks the 11-run store-only
   streak, tests the under-served bounded-live lane, and directly extends run-039's
   horizontal-relation frontier with a question a real reader (a buyer building a
   shortlist, or a builder deciding whether to capture edges) would recognize. It is
   distinct from L001 (membership radar) — directed edges from one anchor, not category
   membership — and from run-030 (Exa similarity, multi-anchor demand-side).

These may be Scout recommendations until Brian or the operator confirms one.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: >
  For the observability SaaS sub-market (anchor = Datadog), does a light public
  listicle/SERP panel recover a competitor edge-set, and how does that external set
  compare to (a) the store's prose-named rivals for Datadog and (b) which of those
  rivals are actually captured in the store?
selected_slug: saas-competitor-edge-external-recovery
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: bounded-live
expected_denominator: >
  Not a census. The store's captured SaaS/observability slice (Datadog + any captured
  rivals) plus a small external listicle panel; both treated as partial per L004.
likely_source_panel: SERP/search + 2 independent comparison/listicle pages.
builder_lens: >
  Tests whether horizontal competitor edges are cheaply recoverable from an external
  listicle panel, and whether the recovered edges would be a fillable cut or mostly
  dangle off-store — the roadmap input behind run-039 W1.
reach_reason: >
  Reaches past the cached answer (edges live in ~5/23 prose bodies, mostly off-store)
  to test whether an external panel resolves the neighborhood the store cannot surface.
allowed_sources:
  - "store/ (Datadog + captured SaaS profiles)"
  - "experiments/00-market-read-lab/learning/"
  - "SERP/search (firecrawl_search), as direction-finding leads"
  - "up to 2 single-page HTML comparison/listicle pages (firecrawl_scrape, no PDF)"
disallowed_actions:
  - "parsers:[pdf] or any multi-page document parse (per run-040 bounded-live-spend)"
  - "entering intake funnels, gated pickers, login, or paywalled pages"
  - "adding a 3rd source family or broadening into a crawl/census"
  - "store/ mutation, write-back, durable primitive creation, lesson graduation"
live_evidence_plan:
  budget_class: light
  evidence_goal: >
    Verify/falsify whether a light public listicle/SERP panel recovers a directed
    competitor edge-set for Datadog, and diff it against the store's prose-named rivals
    and captured slice.
  source_families_allowed: [SERP/search, comparison/listicle]
  source_families_disallowed: [PDF/multi-page docs, intake funnels/gated pickers, review/forum, filings/IR, paywalled/login]
  ceilings:
    source_families: 2
    outside_sources_read_or_captured: 6
    paid_capture_credits: 6   # tighter than the 20 default, hardened against run-040
  fail_closed_when:
    - a needed source is a PDF or multi-page parse (cost invisible pre-call)
    - the next step adds a 3rd source family or exceeds any ceiling
    - login/paywall/gated picker/funnel is the only path
    - the probe broadens from a directed edge-check into mapping the whole market
  stop_rules:
    - SERP snippets are leads; an edge is "external-corroborated" only when named by >=2 independent listicles
    - prefer the listicle HTML page over the snippet; scrape at most 2 single HTML pages
    - stop as insufficient-evidence rather than enter a funnel or parse a PDF
approval_needed: no
why_autonomous_safe: >
  Standing bounded-live policy; light, hardened plan (2 families, 6 outside sources,
  6-credit ceiling, explicit no-PDF/no-multi-page rule learned from run-040); read-only
  on store/; no write-back. Fails closed before any uncertain-cost capture.
loop1_failure_mode: >
  Broadening from a directed Datadog-edge check into an open-ended observability market
  map, or treating one listicle as a denominator instead of a corroboration source.
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. C1 is chosen to break an 11-run
store-only streak and exercise the under-served bounded-live + horizontal-relation
frontier. The plan is deliberately hardened against run-040's spend trap: PDF and
multi-page parses are disallowed, the credit ceiling is 6 (not the 20 default), and the
fail-closed rules trigger before any capture whose cost is invisible pre-call. If Loop 1
finds the only recovering surface is a PDF/funnel, the correct outcome is
`insufficient-evidence`, not a ceiling breach.
