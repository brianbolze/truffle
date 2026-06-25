# Run Notes

```yaml
run_status: needs-human-review
evidence_mode: bounded-live
autonomous_eligible: yes
termination_reason: failed-loop1-exit-check
learning_tags: [source-panel, coverage-caveat, source-rigor, depth-backfill, bounded-live-spend]
```

## 30-second operator read

- **Did the run work?** Partly. The read landed a sharp, useful finding (below), but the
  run **fails closed to `needs-human-review`** on a **spend-ceiling breach**: a single
  PDF parse cost 15 credits, taking total spend to ~23 paid credits against the Scout's
  10-credit ceiling. Evidence-gathering stopped at that point.
- **What was awkward?** PDF/multi-page capture cost is invisible before the call — a
  Firecrawl `scrape ... parsers:[pdf]` of a 15-page ToS billed 15 credits where a normal
  page is ~1–2. One in-scope, intended action breached the tight ceiling.
- **What should the next agent know?** Finding is real and source-graded: a non-gated
  public panel *partially* recovers state availability — the **legal/ToS surface**
  recovers the all-50 binary (remedymeds ToS = all 50 + DC, primary), the marketing
  funnel the store captured does not, and the **precise per-state list** for partial
  brands stays a true reachability wall (funnel/picker only). Do **not** re-run for free:
  the answer is in `read.md`; what's blocked is the spend posture, not the conclusion.

## What happened

Scout selected a bounded-live gap-probe (C1) testing whether a light public panel can
recover state availability for run-038's 5-brand blind set. Loop 1 read the 5 store
profiles (baseline: 4/5 blind, hellowisp the exception), then ran one SERP query per blind
brand (henry/remedy/found/ivim) and scraped the one load-bearing primary positive
(remedymeds ToS). The ToS PDF parse billed 15 credits → cumulative ~23 vs the 10 ceiling.
Stopped all capture, wrote `read.md` + receipt, and failed the Loop 1 exit check on spend.

## Observations

Greedy raw learning. Loop 2 (after the block is cleared) should append the useful rows to
`learning/observations.md`. One row per sighting; do not merge.

| ID | Kind | Saw | Not claiming | Evidence pointer | Tags |
|---|---|---|---|---|---|
| R1 | risk-miss | **Spend-ceiling breach.** A single Firecrawl `scrape parsers:[pdf]` of remedymeds' 15-page ToS billed **15 credits**, taking the run to ~23 paid credits against the Scout's 10-credit ceiling (over the 20 default too). PDF/multi-page capture cost is not visible before the call, so a tight bounded-live ceiling can be breached by one intended, in-scope action; the run had to fail closed *after* the spend, not before. | That the ceiling is wrong or the scrape was off-scope — the action was in-plan and load-bearing; only that per-page PDF pricing is invisible pre-call, so "stop before exceeding" is not enforceable for multi-page captures with the info a Loop 1 agent has. | This run-notes header; receipt S1 (creditsUsed 15); scrape metadata numPages:15 | bounded-live-spend, source-rigor |
| S1 | surprise | The non-gated surface that recovers state availability is the **legal/ToS page**, not the marketing funnel the store captured. remedymeds' ToS (non-gated, primary, "Last Updated 2025-12-05", reachable at the 2026-06-01 capture) states "available in all fifty (50) states plus DC" — flipping the store's "states served — not on captured pages." The blindness was a **capture-scope artifact** (funnel + PDPs only) for the all-50 binary, not a reachability wall. | That the store should capture ToS pages — only that the availability *binary* lives on an under-captured public surface; spend/scope-gated. | read.md Result table; remedymeds profile.md:27/127; receipt C1 | depth-backfill, source-panel, coverage-caveat |
| G1 | gap | The **precise per-state list** for partial-coverage brands (henrymeds, joinfound, ivimhealth) is a **true reachability wall** for a light public panel: it lives only inside the intake funnel (disallowed) or an interactive state-picker (joinfound `/insurance`), never on a non-gated public page. Sharpens run-038 G1 — the off-surface gap is real *at the list grain*, even though the *binary* is partly recoverable (S1). | That the list is unreachable in principle — only that a non-gated light public panel can't reach it; entering intake (disallowed) might. The two grains (binary vs list) behave differently. | read.md Gap Map; joinfound profile.md:36; ivimhealth (no list on-site) | source-panel, coverage-caveat |
| S2 | surprise | Recovery is **surface-shaped, not brand-shaped** (mirrors run-038 S1's ingredient-type framing): one probe, four brands, four distinct public-surface outcomes — ToS-clean (remedy), disclaimer-only/no-list (ivim), marketing-silent + 3rd-party-only (henry), picker-gated (found). "Is this brand's availability public?" is the wrong question; "which public surface does it use?" is right. | That brand richness never matters — hellowisp's on-site per-state license page shows it can; only that the dominant axis here is *surface type*. | read.md Result table; run-038 S1 | query-time-grouping-enough, coverage-caveat |
| W1 | wish | If anything ever graduates from S1, the lightest path is a **capture/recipe note** — "for state availability, also read the brand's ToS / legal / provider-credentials pages, not just the marketing funnel" — NOT a structured state-availability field. Load-bearing reason: only the *binary* is recoverable from the under-captured surface; the per-state *list* stays funnel-gated (G1), so a field would be mostly-empty and fail engine-dev's "a cut you can fill reliably" bar. Mirrors run-036/037/039 anti-sprawl W1 landings. | That it should graduate now — only the lightest path *if* a real consumer needs it AND a 2nd brand shows ToS-states-disclosure (n=1 primary positive here). "No new primitive needed" stays live. | read.md What Would Change; .claude/rules/engine-dev.md | depth-backfill, query-time-grouping-enough |
| G2 | gap | Off-scope but surfaced by the same panel (noted, not chased): remedymeds' ToS names its **MSO backend** (OpenLoop / Rezilient / JMP / J.P. Medical professional entities) — `relation-pressure` relevance, the legal page exposes backend structure the marketing page hides; and an **FDA warning letter to Remedy Meds (2025-09-09)** appeared in SERP — a regulatory change-signal. | That this run should pursue them — only that the ToS/SERP panel incidentally exposes backend + regulatory surfaces a marketing-only capture misses. | read.md Source Gaps; remedymeds ToS §2(a); FDA SERP result | source-panel, relation-pressure |

## Inputs and scope

Fixed 5-brand panel from run-038's blind set: henrymeds.com, joinfound.com,
remedymeds.com, ivimhealth.com, hellowisp.com. Store profiles read for the baseline;
public panel = brand-owned pages + SERP. No denominator/census. hellowisp not re-probed
live (already the captured exception).

## Live evidence plan

```yaml
live_evidence_plan:
  budget_class: light
  evidence_goal: >
    Verify/falsify whether a non-gated public panel (brand state/legal pages + SERP)
    recovers state-level availability for the 5-brand run-038-blind panel.
  source_families_allowed: [owned/official (state/legal pages), SERP/listicle]
  source_families_disallowed: [intake funnels/gated pickers, review/forum, filings/IR, paywalled/login]
  ceilings:
    source_families: 2
    outside_sources_read_or_captured: 6
    paid_capture_credits: 10
  fail_closed_when:
    - only path to a state list is an intake funnel or gated picker
    - next step adds a 3rd source family or exceeds a ceiling
    - login/paywall/private required
    - broadens into a crawl/census
  stop_rules:
    - stop as insufficient-evidence rather than enter a funnel
    - SERP snippets are leads; a state claim is confident only with a brand-owned page
# OUTCOME: ceiling on paid_capture_credits (10) was BREACHED — actual ~23 (see R1).
# Source-family + funnel-entry + no-crawl rules were all HONORED.
```

## Live evidence used

```yaml
live_evidence_used:
  - source_or_query: "Henry Meds available states list (SERP)"
    source_family: SERP/listicle + owned/official
    action_taken: searched
    reason: find a non-gated brand-owned state enumeration for henrymeds
    source_grade: direction-finding (brand pages); secondary (Forbes)
    captured_at: 2026-06-24
    spend_note: paid-credit  # 2
    claim_ids_supported: [C3]
  - source_or_query: "Remedy Meds which states available (SERP)"
    source_family: SERP/listicle + owned/official
    action_taken: searched
    reason: find remedymeds state availability
    source_grade: direction-finding
    captured_at: 2026-06-24
    spend_note: paid-credit  # 2
    claim_ids_supported: [C1]
  - source_or_query: "Found joinfound which states available terms (SERP)"
    source_family: SERP/listicle + owned/official
    action_taken: searched
    reason: find a non-gated joinfound state list off the picker
    source_grade: direction-finding
    captured_at: 2026-06-24
    spend_note: paid-credit  # 2
    claim_ids_supported: [C4]
  - source_or_query: "Ivim Health which states available (SERP)"
    source_family: SERP/listicle + owned/official
    action_taken: searched
    reason: find ivimhealth state availability
    source_grade: primary (qualifier, snippet)
    captured_at: 2026-06-24
    spend_note: paid-credit  # 2
    claim_ids_supported: [C2]
  - source_or_query: "https://remedymeds.com/remedymeds/documents/terms-of-service.pdf"
    source_family: owned/official (legal PDF)
    action_taken: captured (scrape, parsers:[pdf])
    reason: confirm the one load-bearing primary positive (all-50 claim) per the no-snippet rule
    source_grade: primary
    captured_at: 2026-06-24
    spend_note: paid-credit  # 15 (15 pages) — ceiling breach, see R1
    claim_ids_supported: [C1]
# Totals: 5 outside actions (within 6 ceiling); ~23 credits (OVER the 10 ceiling).
```

## Friction log

The Firecrawl PDF-scrape credit model (per-page) is the friction: a 15-page ToS billed
15 credits with no pre-call estimate, against a 10-credit run ceiling. The "stop before
exceeding any ceiling" rule is only enforceable for sources whose cost is knowable in
advance — multi-page PDF parses are not. Captured as R1.

## Evidence limits

- C1 is n=1 primary positive (ToS-states-disclosure may be a remedymeds idiosyncrasy).
- C2/C3/C4 are SERP-snippet leads, not full scrapes: C2 a low-risk primary negative, C3
  third-party secondary, C4 gated/social.
- Precise per-state lists for partial brands not obtained (funnel/picker only — disallowed).

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`/`local-existing`/planned `bounded-live`: **pass** (bounded-live)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` present and followed: **FAIL** — plan present; the `paid_capture_credits` ceiling (10) was exceeded (~23) by the PDF parse (R1).
- If `bounded-live`, every outside source logged in `live_evidence_used`: **pass**
- If `bounded-live`, stop rules and spend notes recorded: **pass** (recorded, incl. the breach)
- No disallowed action happened: **pass** (no funnel entry, no picker operation, no 3rd source family, no crawl)
- Required citations / receipts present and source-graded: **pass**
- No snippet treated as evidence: **pass** (only the full-scraped C1 used for a confident primary claim)
- Current/pricing/policy claims carry capture dates and source grade: **pass**
- Absence language says "not found", not "not true": **pass**

**Overall: FAIL** on the spend-ceiling item → `run_status: needs-human-review`,
`termination_reason: failed-loop1-exit-check`. The conclusion is sound; the blocker is
spend posture. Do not start Loop 2 until a human clears the block.

## Surprises

The recovering surface is the legal/ToS page, not the marketing funnel (S1); and the
recovery axis is surface-type, not brand (S2). See Observations.

## Learning tags

| Tag | Fired? | Why |
|---|---|---|
| `source-panel` | yes | The legal/ToS source family is the load-bearing under-captured surface; the precise list needs the funnel. |
| `coverage-caveat` | yes | Store blindness was a capture-scope artifact (binary) + a true wall (list). |
| `source-rigor` | yes | Primary (ToS) vs secondary (Forbes) vs social (FB) grades drove what could be claimed. |
| `depth-backfill` | yes | A specific public surface (ToS/legal) is uncaptured across the panel. |
| `bounded-live-spend` | yes (coined) | **New tag.** Use when bounded-live spend behavior — ceiling enforceability, invisible per-call cost (e.g. per-page PDF parsing) — is the system pressure, distinct from source *grade* (`source-rigor`) or panel *composition* (`source-panel`). |

"No new primitive needed" stays the live default (W1).

## Next-run advice

- **Spend:** before scraping a PDF/multi-page doc under a tight ceiling, treat it as
  high-variance cost; prefer the SERP snippet as a lead and only parse if the claim is
  load-bearing AND the ceiling has clear headroom. Consider Scout setting a separate,
  higher PDF/parse sub-ceiling, or banning `parsers:[pdf]` under a 10-credit plan.
- **Conclusion is bankable** without more spend; a human need only clear the spend block.
- A wider panel (n>1 primary positive) would test whether ToS-states-disclosure is a
  pattern or a remedymeds idiosyncrasy — but that's a fresh contract, not a re-run.
