# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [query-time-grouping-enough, confidence-grain, schema-edge-entity-type, source-rigor, coverage-caveat]
```

## 30-second operator read

- **Did the run work?** Yes. Store-only calibration of the cold-start value job on a reproducible, deliberately-heterogeneous 6-company sample. Clean positive result with two sharp residual frontiers.
- **What was awkward?** Nothing operationally — frontmatter sorts gave a clean reproducible sample. The only judgment call was honoring "reproducible + non-cherry-picked + spans heterogeneity" with a deterministic slot rule (see C1).
- **What should the next agent know?** Headline: cold-start is **structure-shaped, not brand-shaped** — uniform 9-section skeleton + trust surface across Investor/Holding, deep-tech, telehealth, SaaS, luxury, smart-hardware, vintages 05-30→06-24, schema 2.2→2.6. The contract's "varies unpredictably by company" hypothesis is falsified at the structural level. Residuals: `business_model` frontmatter field mis-serves non-standard monetizers (prose rescues); `unverified_fields` protection is relay/salience-dependent. "No new primitive needed" holds.

## What happened

Surveyed all 136 `store/*/profile.md` frontmatter (entity_type, primary_industry, captured_at, schema_version). Built a reproducible 6-company sample by deterministic slots (rare entity_type, vintage extremes, alpha-first per under-read industry) — receipt C1. Read each profile's full lead surface (frontmatter + Overview + Strategic read + unverified_fields + site_notes) and the section-header skeleton. Mapped the 4 cold-start questions (what / who-for / how-monetizes / what-to-distrust) onto the lead surfaces per company. No external sources, no spend, no store mutation.

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
| S1 | surprise | **Cold-start is structure-shaped, not brand-shaped.** All 6 sampled profiles — spanning Investor/Holding, deep-tech nuclear, longevity-telehealth, no-code SaaS, luxury watch, smart-hardware; vintages 2026-05-30→06-24; schema 2.2→2.6 — carry the *same* 9-section skeleton (count + order uniform; only header capitalization varies — airtable title-case vs sentence-case, corrected per VR1) + uniform classification frontmatter, and the 4 cold-start questions (what/who-for/how-monetizes/what-to-distrust) map ~1:1 onto it. The contract's "cold-start reliability varies unpredictably by company" hypothesis is falsified at the structural level. First direct read of the **cold-start value job** (never read head-on before; all prior runs pre-curated a clean cohort). | That cold-start always succeeds — depth of *peripheral* identity metadata varies by vintage (G1) and a fluent-but-unflagged profile could still trap (none in sample); only that the scaffold + trust surface are uniform across heterogeneous entities. | read.md Result table; header-skeleton grep across the 6; C1 | query-time-grouping-enough, confidence-grain |
| S2 | surprise | **`business_model` is the one lead *field* that breaks cold-start "how it monetizes."** The single-valued closed enum is thin/misleading for 3/6: blueowl `Other` (honest "no taxonomy value fits asset-mgmt fee economics"), eightsleep `Subscription` (one-time hardware + mandatory Autopilot sub — names one leg), blueenergy `Usage-based / Consumption` (PPA power sales — opaque alone). The `How it works/model` prose carries it correctly all 6. A cold reader keying on the frontmatter field alone gets a wrong/empty monetization answer. Cold-start-lens instance of run-037 S1 / run-044 G2 single-valued-`business_model` lossiness. | That the field is broken or a field is needed — single-valued is a deliberate contract choice and prose rescues it; only that the fast-read field mis-serves non-standard monetizers for the cold-start reader. | read.md Result(detail); blueowl profile.md:35; eightsleep:44; blueenergy:39 | schema-edge-entity-type, query-time-grouping-enough |
| S3 | surprise | **"What to distrust" is the *best-served* cold-start question, not the worst** — every profile's `unverified_fields` names the load-bearing soft spot precisely (blueowl AUM self-reported; alange parent inferred from footer; agelessrx prices point-in-time + rotating coupons, true cost behind portal; eightsleep "4th July Sale" snapshot + Pod 5 Ultra price missing; blueenergy PPA pricing + legal entity absent). The cold reader is structurally protected from over-trust — *only if they read `unverified_fields`*. Relay/salience-dependence (038-R1/042-R1/049-G1) on the cold-start surface. | That protection is automatic — it depends on the reader reading the flag block; only that the *content* is present and honest in all 6. | read.md Result(detail); the 6 `unverified_fields` blocks | source-rigor, query-time-grouping-enough |
| G1 | gap | **Schema-vintage drift leaves peripheral-metadata holes but a version-robust cold-start core.** The two oldest captures (blueowl, alange — schema 2.2) lack the `socials`/`legal_entity`/`logos`/`modules` blocks the 2.5/2.6 captures carry; but `description`, `Overview`, `unverified_fields`, and `Strategic read` are present in *all* versions. So cold-start quality is vintage-robust; only peripheral identity metadata varies. | That older captures fail cold-start or need backfill — the cold-start core is intact across versions; only that the newer identity modules are absent on 2.2-vintage profiles. | read.md Gap Map; blueowl/alange (2.2) vs others (2.5/2.6) frontmatter | coverage-caveat, depth-backfill |
| S4 | surprise | **Cold-start quality did not track reader prominence/priors.** The obscure deep-tech (blueenergy) and asset manager (blueowl) profiles were as legible on the 4 cold-start questions as the familiar airtable/alange/eightsleep — evidence the read isn't a reader-prior artifact but a property of the capture contract. (Honest limit: an LLM reader carries broad priors; not a true blind cold-start, so this is suggestive, not proven.) | That the reader is truly blind — an LLM has priors on famous brands; only that legibility tracked the profile structure, not the brand's fame, in this sample. | read.md What Would Change; C1 prominence-mix column | confidence-grain, coverage-caveat |

## Inputs and scope

- **Store slice:** all 136 `store/*/profile.md` frontmatter for the shape survey; 6 full profile lead surfaces for the read (sample rule + spans in receipt C1).
- **Sample (6/136):** blueowl-com, blueenergy-co, agelessrx-com, airtable-com, alange-soehne-com, eightsleep-com.
- **Surfaces read per company:** frontmatter (description, entity_type, target_market, offering_category, business_model, primary_industry, captured_at, schema_version, unverified_fields, site_notes), `## Overview`, `## Strategic read`, and the full `##`-header skeleton.
- **Exclusions:** offerings.md / visual.md / signals not read (lead-surface-only by contract); telehealth deliberately under-sampled (1/6 vs 52% store share) to force heterogeneity; no external sources, no spend, no store mutation.

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

No operational friction. Frontmatter sorts produced the reproducible sample cleanly; the lead-surface-only scope kept reads fast.

## Evidence limits

- n=6 of 136 — a sample, not the store; telehealth under-sampled by design (S1 could read differently on a telehealth-weighted draw).
- The reader is an LLM with broad priors, not a true blind cold-start reader (S4 limit) — structural uniformity holds regardless, but "obscure as legible as famous" is suggestive, not proven.
- No fluent-but-unflagged profile appeared; the false-completeness trap is "not found," not "not there" — a larger draw could surface one.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no Firecrawl, no browsing, no store mutation, no primitive creation, no lesson writing)
- Required citations / receipts present and source-graded: **pass** (C1; per-company file:line pointers in read.md)
- No snippet treated as evidence: **pass** (no external sources)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no current/external claims; profile prices treated as point-in-time per their own `unverified_fields`)
- Absence language says "not found", not "not true": **pass** (false-completeness trap reported as "not found in sample")

## Surprises

The strong result is itself the surprise: after a long streak of runs whose value landed on the builder/Pantry rather than the buyer, the cold-start value job — never read head-on — turned out to be one the store serves *well* and uniformly. The failure modes that did appear (`business_model` fast-read field; `unverified_fields` salience) are the lab's recurring "data is right, the fast surface/relay is the risk" shape, not cold-start-specific defects. See Observations S1–S4 / G1.

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

Fired: `query-time-grouping-enough` (cold-start answerable from existing lead surfaces; no new object), `confidence-grain` (the run's design axis — is cold-start quality predictable; reused from run-031), `schema-edge-entity-type` (the `business_model` single-valued field mis-serving non-standard monetizers), `source-rigor` (the `unverified_fields` relay/salience dependence), `coverage-caveat` (schema-vintage peripheral-metadata drift). No new tag needed — `confidence-grain` already exists as a handle (run-031).

"No new primitive needed" is the outcome: the cold-start scaffold + trust surface already work; the two residuals are a fast-read field (fix, if ever, = run-037 W1 ranked multi-select `business_model`, only for a *filtering* consumer) and a salience/relay discipline (no field).

## Next-run advice

- A natural follow-up: a **telehealth-weighted** cold-start draw (the 52% bucket this run under-sampled) to test whether the structural uniformity holds where the store is densest, and to hunt the fluent-but-unflagged false-completeness profile this sample didn't surface.
- Or pair cold-start with the **render surface** (run-049): the S3 `unverified_fields` salience risk is benign in the raw `profile.md` but bites harder once the brief buries flags off the 5-second path — a cold-start-on-the-rendered-brief read would join the two threads.
- Avoid re-running cold-start on a *clean cohort* — that would re-hide the heterogeneity this run was designed to expose.
