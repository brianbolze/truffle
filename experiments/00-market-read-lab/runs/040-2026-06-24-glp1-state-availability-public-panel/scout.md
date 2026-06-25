# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L002 (headline Signal needs confound sibling), L003 (review bodies uncaptured),
  L004 (denominators partial, reconciliation travels), L005 (query-time grouping enough
  only when corpus carries the cut), L006 (price-visibility token = buyer-reachability,
  not intermediary take rate; `proposed`). Observation stream is dominated by runs
  036–039: `schema-edge-entity-type`, `query-time-grouping-enough`,
  `denominator-reconciliation` (now n=3: industry-draw is the wrong key for an
  entity-shape cohort), `relation-pressure`, and a **3×-recurring frontier** — the
  decision-grade fact lives *off the captured marketing surface* (036 G2 marketplace
  take rate off-site; 037 hybrid economics off-site; 038 G2 all-in price + state
  availability behind intake / in filings).
- `scout-context.md`: two-test selection (value/reach + design); select for reader value,
  reach, source-family diversity, calibration against blind spots — NOT store-answerability.
  Gap-probes first-class with a bounded plan.
- Last 3 `run-notes.md` files (037, 038, 039): all `store-only`; all non-telehealth or
  delegation-calibration schema/cohort reads. Source-family diversity is thin — no
  `bounded-live` run since **034** (5 store-only runs in a row).
- Current run artifacts: fresh scaffold, temp slug `scout-candidates`.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1 [SELECTED]** For a small panel of GLP-1 telehealth brands the store is blind to on state availability (038 G1), can a *light, non-gated public source panel* — brand-owned state/license pages + SERP "[brand] available in [state]" — recover state-level availability, or is the buyer's #1 deciding fact only reachable inside the intake funnel? | gap-probe | yes | bounded-live | State availability is the buyer's deciding fact (038 CR1) and the store can't ground it. The run reaches the 3×-recurring "decision-grade-off-surface" frontier and tests whether a bounded public panel makes it tractable. | **Source panel** — does a repeatable *non-gated* public surface for state availability exist, or is it structurally intake-gated? Tests an off-site source family without entering a funnel. | Past the cached store answer; tests whether the recurring off-surface gap is a capture-scope choice or a true reachability wall. | Brand state/license pages + SERP results with exact URLs, capture dates, source grade; "not found" not "not there"; no intake-funnel data entry. | Sliding from a non-gated public-panel test into entering intake funnels (disallowed), or treating a SERP snippet as a confirmed state list. |
| C2 | For a small GLP-1 cohort whose store pricing is several days old, does a live spot-check of the advertised entry price match the captured price — i.e. how stale is the cache over a short window? | calibration | yes | bounded-live | Calibrates "trust the cache over time" with real live evidence. | Freshness — does short-window cache drift exist at the advertised-price grain? | Past the assumption that captured price = current price. | Live brand pricing page URLs + capture dates vs store `captured_at`. | Prices likely stable over days → low reach; risks a null/boring result. |
| C3 | For the SaaS slice (039), resolve the competitor neighborhood live via Exa neighbors / SERP — do named off-store rivals (New Relic, Dynatrace, Salesloft…) form a coherent sub-market, and can external evidence draw the horizontal edge the store can't? | gap-probe | yes | bounded-live | 039 mapped the horizontal-relation gap store-only; this would test live resolution. | Relation — can an external panel draw competes-with edges? | Past the store's vertical-only relation support. | Exa/SERP results with grades + URLs. | Overlaps run-030 (external cross-shop) and risks merely *executing 039's parked next step* rather than teaching something new. |
| C4 | Take a company NOT in the store and attempt a store-only cold-start profile — map exactly what a cold-start needs that the store can't supply. | calibration | yes | store-only | Tests the under-exercised "cold-start a company" value job. | Coverage / persistence boundary. | The empty-store frontier. | n/a (store-only). | Known-fail by construction → low reach, predictable result. |
| C5 | Re-read cross-cohort price-visibility table-stakes across the full store as of today. | value-read | yes | store-only | Reader-friendly summary. | None new. | Nothing past the cached answer. | Store grep. | Pure re-tread of 008/023/028; fails the reach test. |
| C6 | Recover marketplace take rate / GMV from 10-K / IR filings for airbnb, uber (036 G2). | gap-probe | **no** | live-external-needs-approval | Would close 036 G2's off-site economics gap. | Source panel (filings). | The filings source family. | SEC/IR primary docs. | Filings panel is broad, login-ish, sprawl-prone → exceeds a light bounded plan; not autonomous-safe. |
| C7 | Detect telehealth ownership / M&A changes since capture via SERP news for the captured cohort. | gap-probe | yes (caveated) | bounded-live | Tests change-pulse for the `relation-pressure` axis. | Change pulse / freshness. | Events the store's State snapshot can't show. | Primary news/press-release URLs + dates; snippets are leads only. | News-claim rigor is demanding; high risk of snippet-grade overclaim within a light ceiling. |

## Selected Question(s)

1. **C1** — GLP-1 state-availability public-panel reachability probe (bounded-live gap-probe).

Runner-up: **C2** (freshness spot-check) if a non-news bounded-live is preferred, though
its reach is lower.

Why C1 over the field: it scores highest on the two tests at once — real buyer value
(the deciding fact per 038 CR1), genuine reach (it leaves the cached answer and tests an
off-site source family), and it pressure-tests the **single most-recurring frontier** in
the stream (decision-grade-off-surface, n=3) by asking whether that gap is a capture-scope
choice or a true reachability wall. It also restores source-family diversity after five
straight store-only runs. It is a legitimate repeat of the 025/038 state-availability
shape because it tests a **materially different source family + evidence mode** (live
public panel vs store-only), not a re-answer — and it stops cleanly at the intake-funnel
wall, which keeps the bounded plan honest.

C3 and C6 were rejected for autonomous selection: C3 risks executing 039's parked next
step and overlaps 030; C6's filings panel is too broad for a light bounded plan.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: >
  For a small panel of GLP-1 telehealth brands the store is blind to on state
  availability (run-038 G1), can a light, non-gated public source panel — brand-owned
  state/license pages plus SERP "[brand] available in [state]" — recover state-level
  availability, or is the buyer's deciding fact only reachable by entering the intake
  funnel?
selected_slug: glp1-state-availability-public-panel
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: bounded-live
expected_denominator: >
  A fixed 5-brand panel from run-038's blind set — henrymeds, joinfound, remedymeds,
  ivimhealth, hellowisp — read against their captured store profiles plus a light public
  panel. Not a market census; the point is source-family tractability, not coverage.
likely_source_panel: >
  (1) brand-owned state/availability/licensing pages (deeper than the captured marketing
  page); (2) SERP results for "[brand] available in [state]" / "[brand] states served".
builder_lens: >
  Source panel — whether a repeatable NON-GATED public surface for state-level
  availability exists, or whether the fact is structurally intake-gated. Tests the
  3×-recurring decision-grade-off-surface frontier at the buyer's deciding-fact grain.
reach_reason: >
  Leaves the cached store answer (which 038 G1 already showed is blind for ~6/8) to test
  whether a light public panel makes the off-site fact tractable, or confirms a true
  reachability wall. Either outcome is load-bearing learning.
allowed_sources:
  - store/ (captured profiles for the 5-brand panel + any state lines already captured)
  - experiments/00-market-read-lab/learning/
  - brand-owned state/availability/licensing pages (public, non-gated)
  - SERP results for state-availability queries (direction-finding; primary confirmation
    must come from a brand-owned page)
disallowed_actions:
  - entering or advancing any intake/eligibility funnel, or any flow requiring personal
    data, login, or a gated state-picker
  - paywalled, login-gated, or private sources
  - review/forum panels or any third source family beyond the two named
  - broad crawl; mutating store/; write-back; durable primitive creation; lesson graduation
live_evidence_plan:
  budget_class: light
  evidence_goal: >
    Verify or falsify whether a non-gated public panel (brand state pages + SERP)
    recovers state-level availability for the 5-brand panel that the store cannot ground.
  source_families_allowed:
    - brand-owned site (state/availability/licensing pages)
    - SERP / listicle (direction-finding only)
  source_families_preferred:
    - brand-owned site (only primary-grade confirmation for a state claim)
  source_families_disallowed:
    - intake/eligibility funnels and gated state-pickers
    - review/forum
    - filings/IR
    - paywalled or login-gated
  ceilings:
    source_families: 2
    outside_sources_read_or_captured: 6
    paid_capture_credits: 10   # tighter than the default 20; prefer free reads
  fail_closed_when:
    - the only way to a state list is through an intake funnel or gated picker
    - the next step would add a third source family or exceed any ceiling
    - it would require login / paywall / private data
    - it broadens into an open-ended crawl or a market census
  stop_rules:
    - stop as insufficient-evidence (record what was found) rather than entering a funnel
    - SERP snippets are leads only; a state-availability claim is confident only with a
      brand-owned page URL + capture date + source grade
approval_needed: no
why_autonomous_safe: >
  Standing bounded-live policy; light panel of two public source families; fixed 5-brand
  scope; hard stop at the intake-funnel wall; tight ceilings (2 families / 6 sources /
  ≤10 credits); no write-back, no store mutation, no primitive creation.
loop1_failure_mode: >
  Sliding from a non-gated public-panel test into entering intake funnels to "get the
  real list," or letting a SERP snippet stand as a confirmed state list without a
  brand-owned primary page.
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. C1 was chosen for the value/reach
+ design double-hit and for restoring bounded-live source-family diversity after five
store-only runs; the bounded plan stays honest by failing closed at the intake-funnel
wall — the very boundary the run is probing — so "still off-surface even with a public
panel" is a valid, valuable result.
