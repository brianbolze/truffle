# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [source-rigor, denominator-reconciliation, query-time-grouping-enough, depth-backfill, coverage-caveat]
```

## 30-second operator read

- **Did the run work?** Yes — clean value-read with a structural answer. The store carries verbatim
  metered pricing richly for 5/6, but the cohort is **not cost-comparable** because each brand bills in
  its own consumption unit (host/credit/event/message/%-volume). Third pricing-shape incomparability
  sighting after run-023 (GLP-1) and run-043 (wearable TCO).
- **What was awkward?** Nothing operationally; the one judgment call was excluding two non-infra
  entities (blueenergy, waldo) that the `business_model: Usage-based` grep pulled in.
- **What should the next agent know?** `business_model: Usage-based` is a *clean positive cohort key*
  here (contrast run-039's SaaS collapse), and the price-visibility token is near-absent on this cohort
  (only Stripe tokenizes; 4/6 predate schema 2.3) — absent token ≠ `[published]`.

## What happened

Read `business_model: Usage-based / Consumption` across the store, isolated the dev-infra core
(datadoghq, snowflake, stripe, twilio, posthog, aws), pulled verbatim `/pricing` rates and capture
clocks from each `profile.md`, checked price-visibility-token presence, and compared against five
subscription foils. Store-only, no external sources, no spend. Answer is a structural ceiling, cleanly
mapped: data is present and honest; the un-comparability is a property of metered-SaaS markets.

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
| S1 | surprise | **Third pricing-shape where unit-incommensurability, not missing data, is the ceiling.** All 6 metered dev-infra brands carry verbatim `/pricing` rates, but no two share a billing unit — Datadog $/host, Snowflake $/credit, Twilio $/message, PostHog $/event, Stripe %-of-volume, AWS per-service utility. "Which is cheaper" has no cohort answer without the buyer's own workload. After run-023 (GLP-1 per-month vs per-dose) and run-043 S2 (wearable TCO unit non-uniformity), now on metered B2B infra. | That the store under-captured — pricing is present, exact, and dated; only that the unit is each product's own consumption primitive, so cross-vendor magnitude doesn't compare. | read.md Result(1)/(2), C1/C2; datadog profile:54-64; snowflake:66-71; twilio:59-62; posthog:66-73; stripe:62-66 | source-rigor, denominator-reconciliation |
| S2 | surprise | `business_model: Usage-based / Consumption` is a **clean positive cohort key** — the grep returns exactly the metered businesses (+2 non-infra excluded by hand). Direct contrast to run-039 G1, where `[Software / SaaS]` flattened ~19 sub-markets into one undifferentiated pile. Here the field *recovers* the cohort the question is about. | That `business_model` is always a good key — it's coarse (single-valued, primary leg only) and pulls in non-infra metered firms; only that for *this* question it worked where the SaaS draw failed. | read.md Result(3), C3; run-039 G1; `grep business_model: Usage-based` | denominator-reconciliation, query-time-grouping-enough |
| G1 | gap | **Price-visibility token near-absent on the cohort.** Token (SCHEMA 2.3+) on only 1/6 — Stripe (23 `[published]`, 2 `[on-request]`). Datadog/Snowflake/Twilio/AWS are schema 2.2 (predate it); PostHog's `profile.md` is 2.6 (post-convention) yet carries **zero** tokens on its `What they offer` lines despite publishing verbatim rates. A buyer using the token as a "can I get a price?" filter would be misled by omission (5/6 untokenized though all 6 publish prices). | That the token is broken or backfill is due — SCHEMA says absent = predates-convention, no backfill; only that the token isn't a dependable cross-cohort surface on captures this vintage, and PostHog's v2.6 profile hints it may not fit pure-metered sellers. (PostHog `offerings.md` is also untokenized but is module-schema v1.2 — a separate, mundane vintage gap, not part of the tell; corrected per dev review.) | read.md Result(4), C4; stripe profile:62-66; schema_version 2.2 on 4/6; posthog profile 2.6 untokenized; posthog offerings 1.2; SCHEMA.md:99 | coverage-caveat, depth-backfill |
| S3 | surprise | **Stripe is an L006 *non-trap* — a 2nd entity-type sighting on the safe side.** Stripe is an intermediary (payments) whose monetization (%-of-volume) **is** published to its paying customer (the merchant), so its `[published]` tokens read correctly. Matches run-037 DR3's sharpened scope: the L006 trap fires only when the intermediary leg has *no consumer-facing price* (marketplace take-rate split), not whenever an entity is an intermediary. | That this graduates/alters L006 — decision boundary; only an out-of-band sighting that *confirms* run-037 DR3's scope on a new entity (a transparent intermediary). | read.md Result(5), C5; stripe profile:62; lessons.md L006; run-037 DR3 | source-rigor, query-time-grouping-enough |
| G2 | gap | Single-valued `business_model` **mis-sorts the hybrid**: Notion (`Subscription` primary + a usage-based Notion-credits layer riding on top, per its own inline comment) sits in the *foil* set, so a usage-based-revenue cohort drawn from the field misses it. Same single-valued lossiness as run-037 S1 (wearable hybrids), now on the metered-revenue axis. | That a field should be built — n small, single cohort; only that the cohort key recovers *pure-play* metered businesses, not every business with metered revenue. | read.md Result(3); notion profile business_model comment; run-037 S1 | denominator-reconciliation, query-time-grouping-enough |
| W1 | wish | If anything ever graduates from S1/G2, the lightest path is run-037 W1's landing — a **ranked multi-select `business_model`** (so Notion's hybrid is recoverable) — and **never** a normalized price-magnitude field: unit-incommensurability means a magnitude field would launder false precision, exactly what engine-dev's "evidence, not scores" forbids. This run is positive evidence the human-read case needs neither. | That it should graduate now — only the lightest path *if* a real consumer needs to *filter/sort* metered tools programmatically. "No new primitive needed" stays live. | read.md What Would Change; run-037 W1; .claude/rules/engine-dev.md | query-time-grouping-enough |
| CR1 | surprise | (Consumer review) **Buyer-primary value frontier — 2nd consecutive after run-043.** The run's value lands on the buyer (a dated, cited per-vendor rate table + a usable structural-ceiling framing a CTO can act on), not the builder/Pantry. The G1 token gap and S2 cohort-key contrast are builder-lane *byproduct*. Breaks the 038/039/041 CR1 "lands on builder not buyer" streak for a second value-read running. | That builder findings are absent — they're real but secondary; only that the *reason the run has value* is buyer-facing this time. | consumer-review.md; read.md Result(1)/(2); run-043 S1/CR1; run-039 CR1 | query-time-grouping-enough |
| DR1 | gap | (Developer review) **Precision correction to G1.** PostHog's `offerings.md` is on the *module*-schema track (v1.2), which predates the token convention independently — a routine module-backfill gap, NOT part of the "post-2.3 yet untokenized" tell. The real signal is the v2.6 *profile* being untokenized; merging both into one claim over-stated the "convention may not fit metered sellers" hypothesis. (Corrected in read.md / run-notes G1.) | That the profile-level tell is wrong — the v2.6 profile untokenization stands; only that the offerings.md absence has a separate, mundane explanation the read conflated. | developer-review.md; posthog profile:3 (2.6) vs offerings:3 (1.2); SCHEMA.md:99 | source-rigor, depth-backfill |
| DR2 | surprise | (Developer review) **S2 ↔ run-039 G1 is one field, cohort-shape-dependent — not two opposite outcomes.** `business_model` works as a cohort key when the cohort IS its primary-tag semantics (pure-play metered → clean), and fails when the cohort cuts across models (SaaS leaf too coarse → collapse) or is tagged by primary leg only (hybrids → missed). A queryability guardrail (know the cohort's structural uniformity before keying on the field), distinct from the n=4 industry-draw `denominator-reconciliation` pattern. | That it contradicts run-039 — it's a boundary condition on the same behavior, not a contradiction; only that field-as-key reliability is a cohort-shape property, not a field-quality property. | developer-review.md; read.md Result(3); run-039 G1; run-044 G2 | denominator-reconciliation, query-time-grouping-enough |

## Inputs and scope

- **Store slice:** `business_model: Usage-based / Consumption` grep → core dev-infra cohort
  datadoghq-com, snowflake-com, stripe-com, twilio-com, posthog-com, aws-amazon-com.
- **Excluded (non-infra, named):** blueenergy-co (energy), waldo-fyi (small app).
- **Subscription foils:** cloudflare-com, openai-com, notion-com (hybrid), linear-app, airtable-com.
- **Files read:** each member's `profile.md` (frontmatter + `What they offer` + site_notes); posthog
  `offerings.md`; SCHEMA.md (token convention reference).
- **No external sources, no spend, no `store/` mutation.**

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

No real friction. Pure-grep cohort draw + per-profile read; the only manual step was hand-excluding two
non-infra entities the `business_model` grep returned (blueenergy, waldo).

## Evidence limits

- Metered rates for the 4 schema-2.2 members captured 2026-05-31; pricing pages are volatile, so the
  rates are a dated snapshot, not a durable price (cousin of run-043 S3). No staleness defect found.
- AWS captured at philosophy-grain (no per-service rate) — correct for a 200+-service catalog, but it
  cannot be priced even within its own profile.
- All claims are store-State with capture clocks; no external/current/snippet evidence used.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live browse, no spend, no `store/` mutation, no `learning/` write)
- Required citations / receipts present and source-graded: **pass** (claim IDs C1–C5 → `file:line`, store-State)
- No snippet treated as evidence: **pass** (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (per-profile `captured_at`)
- Absence language says "not found", not "not true": **pass** (G1 absent-token framed as coverage gap, not opacity)

## Surprises

The headline surprise (S1) is a *positive* about the store and a *negative* about the market: capture
quality is high and the un-comparability is structural — every metered vendor deliberately picks its own
consumption unit. The secondary surprise (S2) is that `business_model` worked as a clean cohort key here,
the inverse of run-039's SaaS collapse — same field, opposite outcome, because the cohort *is* what the
field names.

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

Fired: `source-rigor` (S1/S3 — metered units, token grade), `denominator-reconciliation` (S1/S2/G2 —
cohort key behavior), `query-time-grouping-enough` (W1/S2 — no new primitive), `depth-backfill` (G1 —
token convention coverage), `coverage-caveat` (G1 — token vintage). No new tag needed.

"No new primitive needed" is a valid outcome — and it is this run's outcome.

## Next-run advice

- A **post-2.3, fully-tokenized usage-based cohort** would test whether G1's token-absence is a vintage
  artifact (likely) or a sign the token convention doesn't fit pure-metered sellers (PostHog hints at
  the latter). Worth a targeted probe if a tokenized metered cohort exists.
- The runner-up Scout candidate (**C2 — investor-selection differentiation**, L005 on the capital-allocator
  slice) is still un-run and a good next pick.
- Avoid re-running this as "schema fit on entity shape X" — this run is a *pricing-grain* read, and the
  recent 036–042 schema-fit streak is saturated.
