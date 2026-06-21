# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [query-time-grouping-enough, depth-backfill, coverage-caveat, source-rigor]
```

## 30-second operator read

- **Did the run work?** Yes. First non-telehealth *market read*. Clean dual result: a
  SaaS price-visibility landscape (published self-serve vs quote-gated sales-led) AND the
  recipe-generalizability verdict run 027 left open.
- **What was awkward?** No greppable price-visibility surface for SaaS — the structured
  token is populated for 3/24, offerings.md for 4/24 — so visibility had to be hand-read
  from prose across 24 profiles. That *is* the finding, not just friction.
- **What should the next agent know?** The MRL-002 read-recipe family is NOT
  telehealth-overfit: the enum-grep and prose-read ingredients generalize; only the
  *structured price-visibility grep* doesn't run, because the universal SCHEMA-2.3 token
  is unbackfilled off telehealth (capture gap, not schema/recipe defect). Avoided the
  contracted trap: did NOT read "no structured token" as "SaaS doesn't gate prices."

## What happened

Grepped `primary_industry: Technology` → 24 profiled cos. Pulled `business_model`
(24/24, clean 15/6/2/1 split). Counted price-visibility tokens (3/24) and offerings.md
(4/24) → structured surface near-empty. Dropped to prose-reading `What they offer` /
Overview for all 24 to classify published/partial/on-request. Cross-read SCHEMA 2.3 to
confirm the token is universal-by-design. Wrote read.md (dual reader+builder result) +
one store-query receipt.

## Discovery ledger

Greedy raw learning for this run. Preserve singletons here before triage compresses
anything, then Loop 2 appends the useful rows to `discovery-ledger.md`.

| ID | Kind | Raw observation / wish / friction / surprise / gap | Evidence or pointer | Why it matters | Discovery clock |
|---|---|---|---|---|---|
| O1 | observation | The MRL-002 read-recipe family is **not telehealth-overfit at the read layer**: enum-grep (`business_model` 24/24) and prose-read (run-010 variant) ingredients both run on SaaS; only the *structured price-visibility grep* fails. First *market read* (not classification audit) outside telehealth. | read.md Result table; C1 | Extends 027's taxonomy-generalizability finding to the *read* layer — the other half of the "universal fields + reusable cuts" claim. | ready-for-triage |
| O2 | observation | SaaS price visibility tracks **GTM motion**: ~14 self-serve/PLG publish rate cards; ~6 enterprise sales-led (clari, alpha-sense, gong, qualtrics, usertesting, listenlabs) are quote-/contact-sales-gated. Same 3-value "can I get a price?" axis that split telehealth. | read.md C2; Market Pattern #1 | Positive calibration that the SCHEMA-2.3 token's "one pricing axis that generalizes" intent is real across verticals. | ready-for-triage |
| O3 | observation | `business_model: Usage-based` is the cloud/AI-infra signature — 6-co sub-cluster (aws, snowflake, twilio, datadog, posthog, waldo) that all publish granular metered rate cards; "published" and "usage-based" co-occur. | read.md Market Pattern #3 | A clean cross-field cohort cut exists off telehealth with no new toil (one grep). | notice-only |
| G1 | gap | The **universal price-visibility token** (SCHEMA 2.3, `[published\|partial\|on-request]`) is populated for only **3/24** Tech profiles; offerings.md for 4/24. The cheap structured query path is unavailable off telehealth. | read.md C3; SCHEMA.md:99,142,147; token count | Capture-era/backfill gap on a convention that already exists — the structural reason the telehealth recipe can't run cheaply here. A concrete non-telehealth depth-backfill instance. | ready-for-triage |
| S1 | surprise | The token correlates with **depth/offerings capture, not date**: linear (06-17) and posthog (06-16) are recent yet token-less, while the 3 token-bearers all also have offerings.md. So backfill isn't a "recapture recent" job — it's an "apply the token" job. | capture clocks; token count | Sharpens the backfill ask: the gap is convention-application, not staleness. | recur-watch |
| W1 | wish | If anything graduates, prefer **backfilling the SCHEMA-2.3 token on the 21 token-less `What they offer` lines** (the intended convention, no new field) over building a SaaS-specific pricing module. Converts the prose read into a one-grep structured read. | read.md What Would Change | Names the light, anti-sprawl fix consistent with the engine's "spend on conventions, not infra" line. | recur-watch |
| F1 | friction | Classifying price visibility required hand-reading 24 `What they offer`/Overview prose blocks; no single greppable visibility field off telehealth. One sighting. | run-notes friction log | Mirrors the recurring multi-surface/prose-read friction (MRL-002 family); recur-watch only. | recur-watch |
| V1 | value-miss/trap-avoided | The contracted failure mode was live: a naive `rg '\[on-request\]'` returns ~nothing → "SaaS doesn't gate prices," the exact inverse of the truth (6 cos are fully quote-gated). The structured-absence-vs-market-absence distinction is the load-bearing guardrail. | read.md Result; scout contract loop1_failure_mode | A reusable guardrail: an empty *structured* surface is a coverage signal, not a market fact — say "not captured," not "not gated." | ready-for-triage |

## Inputs and scope

- Slice: `store/*/profile.md` where `primary_industry` contains `Technology` → 24
  profiled companies. Counted `profile.md`, not directories.
- Fields read: `business_model`, `primary_industry`, `captured_at`, price-visibility
  tokens, `What they offer`/Overview prose; offerings.md presence.
- Contract: `SCHEMA.md` price-visibility token + `business_model` closed set.
- Exclusions: capture-only stubs (no profile.md); non-Tech industries (a SaaS co filed
  under Finance/Healthcare would be missed → denominator is a floor).
- No external sources; no spend.

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

Price visibility had no greppable surface off telehealth (token 3/24, offerings.md 4/24),
so classification was a per-profile prose read across 24 companies (F1). One sighting;
mirrors the recurring MRL-002 prose-read friction — recur-watch, not a tooling ask yet.

## Evidence limits

- Denominator is an industry-grep floor (misses tech-adjacent cos filed under other
  industries; excludes stubs). Not a SaaS census — but the recipe-generalizability
  verdict is substrate-level and holds regardless of count.
- 19/24 captured 2026-05-31 — price *points* may be stale; *visibility posture* is stable.
- Price-visibility labels are a read-time Judgment from prose (no structured token to
  verify against for 21/24); flagged as such in read.md and the receipt Claim Map.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a**
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live web, no spend, no store mutation)
- Required citations / receipts present and source-graded: **pass** (`receipts/tech-slice-fields.md`, primary/local-store)
- No snippet treated as evidence: **pass** (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (store clocks recorded; price *points* flagged possibly-stale, posture-not-points is the claim)
- Absence language says "not found", not "not true": **pass** (G1/V1 frame the empty token surface as "not captured", not "not gated")

## Surprises

The price-visibility token tracks *depth/offerings capture*, not capture date — recent
profiles (linear 06-17, posthog 06-16) are token-less while older depth-captured ones
carry it (S1). And the run's headline builder finding inverted the naive expectation: the
recipe *does* generalize; it's the convention's *population* that doesn't.

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
| `query-time-grouping-enough` | business_model + prose-read answered the market layer with grouping; no durable category object needed. | no-op (reinforces MRL-002 family generalizes off telehealth) |
| `depth-backfill` | The universal price-visibility token is populated 3/24 off telehealth; offerings.md 4/24. | watch for recurrence (a 2nd non-telehealth slice with the same token gap hardens MRL-003-style backfill) |
| `coverage-caveat` | Industry-grep denominator is a floor; bulk captured 05-31. | no-op (MRL-001 directory-vs-profiled flavor already logged in run 027) |
| `source-rigor` | Empty *structured* surface must not be read as market absence (V1 trap). | watch for recurrence (structured-absence-vs-market-absence is an MRL-008-adjacent guardrail) |

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

- A **second non-telehealth read** (e.g. a Finance or Consumer-Goods slice, or a
  relation/competitor read on SaaS) would test whether O1's recipe-generalizability and
  G1's token-backfill gap recur — two sightings would move them toward triage.
- Avoid re-running the bounded-live coverage-radar (already named, 3 sightings).
- Re-check: if anyone backfills the price-visibility token off telehealth, this prose
  read becomes a one-grep structured read — re-run to confirm.
