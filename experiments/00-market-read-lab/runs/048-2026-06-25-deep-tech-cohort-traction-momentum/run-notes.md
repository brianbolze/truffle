# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [traction-readiness, freshness-monitoring, source-rigor, denominator-reconciliation, query-time-grouping-enough]
```

## 30-second operator read

- **Did the run work?** Yes. Gap-probe, store-only. Clean result: static State supports a
  size/stage ranking (which duplicates run-042's maturity read) but **not** a momentum/
  "who's gaining" triage. `0/8` of the cohort has any `signals/` capture.
- **What was awkward?** Nothing operationally; the read is a clean negative. The one thing
  to watch is the level-vs-delta line — easy to write the size table and call it momentum.
- **What should the next agent know?** The payload is a roadmap finding for the traction
  frame: comparability (#2) + durable time-series home (#3) are the missing pieces, not
  capture (#1 — the levels are already capturable, and beta-team's cheap auditable anchor
  exists yet uncaptured). "No new primitive needed now" stays live.

## What happened

Re-used run-042's named-8 deep-tech cohort (electra-aero, verdegoaero, blueenergy, cfs,
euclid-foil, evoloh, sorafuel, beta-team). Confirmed `0/8` have a `signals/` dir (receipt
C1). Read the funding/milestone/demand prose + `unverified_fields` from each profile and
assembled a per-company capital/round/milestone **level** table (receipt C2). Found the
level read supports a size/stage ordering but no velocity, and that the ordering largely
re-derives run-042's maturity ranking. No spend, no external sources, no store mutation.

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
| G1 | gap | **Traction is structurally unanswerable from static State.** Every capital/order/milestone figure is a *level at one capture* (all 8 `captured_at: 2026-06-14`); there is no second capture to diff, so "is the pipeline growing / is fundraising accelerating / who's gaining ground" has no answer. The store supports a *size/stage* ranking, never a *velocity/momentum* one — the traction frame's #1 grain trap (level≠delta) hit head-on. | That a momentum field/layer should be built — n=8, single cohort; only that the comparative axis the traction frame defers is the load-bearing absence, and "no new primitive needed now" stays live (no cohort-momentum consumer yet). | read.md Result(2)/Gap Map; C2; all 8 `captured_at` | traction-readiness, freshness-monitoring, query-time-grouping-enough |
| G2 | gap | **`0/8` of the cohort has any `signals/` capture** (C1). The engine's actual comparability machinery (the append-only `signals/` layer + `signal_delta.py`) was never run on deep-tech — telehealth-only to date. So the gap that blocks a momentum read is **not capture** (the levels are present and capturable) but the missing **time-series home** (traction frame #3) and **comparability** (frame #2). Sharpens run-029's store-wide traction-coverage census onto a specific cohort + the cohort-roll-up (#4) question. | That `signals/` should be run on this cohort — spend/approval-gated; only that its absence is exactly what makes the momentum read impossible, and locates the missing piece as comparability/durable-home, not capture. | read.md Result(2)/Source Gaps; receipt C1; run-029 | traction-readiness, source-panel, coverage-caveat |
| S1 | surprise | **The cheap, first-party, auditable traction anchor exists in the cohort yet is uncaptured.** beta-team is a public NYSE filer (ticker `BETA`, 2025 IPO >$1B, Q1 2026 10-Q linked from its investor page) — exactly the "capture easy, obvious, first-party signal" the traction frame says to grab and refuse the paid-data swamp for. Yet beta-team has no `signals/` capture either. So the gap for this cohort is **not discoverability** — the single most reliable signal in the set is in plain view — it's that the cheap-capture floor was never run. | That the store should capture it — only that discoverability is not the bottleneck for at least the public-filer case; the floor is just unrun. | read.md Result(3); beta-team profile.md:123; receipt C1 | traction-readiness, source-rigor |
| S2 | surprise | **Static State carries two loosely-correlated level axes — and they disagree.** A *stage* ordering re-derives run-042's maturity read, but a *capital* ordering does **not**: cfs raised the most ($2B cumulative) yet sits near the bottom on maturity (zero power, pre-demonstration), while beta-team is high on both. So "traction-from-State" does **not** cleanly collapse onto "maturity-from-State" — there are ≥2 partly-independent level axes (capital, stage). What unifies them is the absence that matters: **none carries a delta**. [Corrected per VR1 from an "collapses onto maturity" overreach.] | That capital and maturity are unrelated — they correlate loosely; only that capital-raised is not a maturity proxy (cfs is the counterexample), so the read can't reduce traction to one ordering. | read.md Market Pattern / Result(1); run-042 maturity read; cfs-energy profile.md:61,109; C2 | traction-readiness, query-time-grouping-enough |
| VR1 | risk-miss | (Evidence verifier) read.md originally claimed the "size/stage ranking largely re-derives run-042's maturity read" and that "traction-from-State collapses onto maturity-from-State" (S2) — but **cfs-energy raised the most capital ($2B) while ranking near the bottom on maturity**, so a capital-size ordering and a maturity ordering disagree. A precision overreach the adversarial verifier caught; corrected in read.md Lead / Result(1) / Market Pattern and S2. The core finding (levels yes, delta no) survives and is sharpened (two level axes, not one). Same verifier-catches-a-slip value as run-042 VR1 / 045 VR1 / 047 VR1. | That the finding was wrong — the no-momentum core holds; only that "collapses onto maturity" conflated two partly-independent level axes. | read.md Lead/Result(1)/Market Pattern pre/post; cfs-energy profile.md:61,109 vs beta-team:123 | source-rigor, traction-readiness |
| G3 | gap | **Cross-cohort capital is unit-incommensurable.** cfs "$2B cumulative" vs sora "$14.6M single round" vs blue "$380M" vs verdego/euclid (no $ at all); demand signals span pre-orders (electra 2,200) / backlog (beta 800) / binding orders (evoloh 500MW) / signed intent (evoloh 16GW) / offtake LoI (sora). No common unit to sort momentum or even size cleanly. Cousin of run-023/043/044 price-incomparability, now on the funding/traction axis. | That a normalized capital field should be built — unit-incommensurability would launder false precision (engine-dev "evidence, not scores"); only that the magnitudes don't compare. | read.md Result(1)/Gap Map; C2 | denominator-reconciliation, source-rigor |
| S3 | surprise | **The capture clock can't date the traction *event*.** Recent events (blue $380M Apr 2026, sora $14.6M Apr 2026, euclid acquisition Apr 2026) and stale ones (electra Series B Apr 2025, cfs $2B undated) all sit under the same `captured_at: 2026-06-14`. Event recency lives only in prose milestone blocks, never a structured field — so "what moved lately" needs per-profile prose reading, not a query. Cousin of run-047 CR2 (capture clock dates the profile, not the named third-party/event state). | That a structured event-date field should be built — only that `captured_at` is per-profile freshness, not per-event recency, so it can't carry a "what's new" read. | read.md Result(2)/Gap Map; all 8 `captured_at`; run-047 CR2 | freshness-monitoring, source-rigor |
| W1 | wish | If anything ever graduates from G1/G2, the lightest path is a **query-time recipe + the cheap first-party capture** (ticker/10-Q for public filers like beta-team; dated funding-news for the private 7) — **NOT** a normalized traction-magnitude field, which unit-incommensurability (G3) would turn into laundered false precision. Load-bearing reason: the comparative read needs a *second dated capture*, not a new field on the static snapshot. Mirrors the 036–047 anti-sprawl W1 landings. | That it should graduate now — only the lightest path *if* a real cohort-momentum consumer AND the comparability machinery (2nd capture + delta) appear. "No new primitive needed" stays live. | read.md What Would Change; .claude/rules/engine-dev.md; _design/2026-06-14-traction-frame.md | traction-readiness, query-time-grouping-enough |
| CR1 | gap | (Consumer review) **Value lands on the builder/Pantry, not the investor — "map-not-ingredient" on the traction axis.** The investor's literal ask (momentum) is the one thing the store can't ground; the buyer-facing deliverable is negative space ("size and stage yes, movement no"). Momentum is the run's own Judgment from a single snapshot, not a store-queryable ingredient. Same frontier as run-039/043/047 CR1, now on traction. | That the read failed — it's a gap-probe that lands its builder payload; only that the strongest value is not investor-facing. | consumer-review.md Verdict/Lens; read.md Lead | traction-readiness, query-time-grouping-enough, coverage-caveat |
| DR1 | surprise | (Developer review) **The traction bottleneck is *unrun capture*, not undiscoverable signal — sharpens S1.** For the public-filer case (beta-team) the cheapest, most-reliable traction signal (ticker/10-Q) is in plain view and free to capture; the engine simply never ran a Signal here. So the frame's #1 (capture easy first-party signals) is *available* for at least part of the cohort — what's missing is #2 comparability + #3 durable-home, i.e. running it twice and diffing. Locates the graduation work off "capture more" and onto "run the cheap floor + make it comparable." | That capture should start now — spend/approval-gated; only that discoverability is not the blocker for public filers, so "capture more data" is the wrong default framing for this gap. | developer-review.md Capability/Founder; beta-team profile.md:123; C1 | traction-readiness, source-panel, tooling-ergonomics |

## Inputs and scope

- **Store slice:** the 8 deep-tech profiles from run-042's named cohort (`store/{electra-aero,
  verdegoaero-com,blueenergy-co,cfs-energy,euclidpower-com,evoloh-com,sorafuel-com,beta-team}/
  profile.md`), all `captured_at: 2026-06-14`, single capture each.
- **Membership:** hand-built named-8 (euclidpower the commercial foil); NOT a
  `primary_industry` grep — run-042 G3 established an industry draw scatters this cohort and
  pulls in commercial firms. Treated as partial.
- **Queries:** `signals/` presence count (C1); funding/milestone/demand prose + `unverified_fields`
  read per profile (C2).
- **Exclusions:** no external sources, no `signals/` capture, no store mutation, no spend.

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

No operational friction — store-only read over 8 profiles plus one `signals/` count.
No missing helpers; the named-8 cohort was reusable from run-042 verbatim.

## Evidence limits

- Single capture per company (all 2026-06-14) — no diffable second point exists, which is
  itself the finding (G1).
- 7/8 funding/order/milestone figures are self-reported on the company's own site
  (secondary grade); only beta-team's IPO/10-Q is auditable, and it isn't captured (S1).
- cfs "$2B" and several offtake/partner claims are undated on captured pages — even the
  level read has gaps (G3/S3).
- Absence is stated as **not captured / not found**, never not-true (C1 limits).

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
- No disallowed action happened: **pass** (no live browsing, no spend, no store mutation, no primitive)
- Required citations / receipts present and source-graded: **pass** (C1, C2 + file:line anchors)
- No snippet treated as evidence: **pass** (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (store clocks + self-reported grade flagged)
- Absence language says "not found", not "not true": **pass**

## Surprises

Two: (S1) the cohort's cheapest, most-reliable traction anchor — beta-team's public ticker
+ 10-Q — is in plain view yet uncaptured, so discoverability is not the bottleneck for the
public-filer case; (S2) traction-from-State collapses onto run-042's maturity read, because
the axis that distinguishes traction (velocity) is exactly what a single-capture store can't
carry. (S3) the capture clock dates the profile, not the traction event.

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

**Fired:** `traction-readiness` (G1/G2/S1/S2/W1 — the load-bearing axis, 2nd sighting after
run-029), `freshness-monitoring` (G1/S3 — single-capture, no delta), `source-rigor`
(self-reported 7/8; undated figures), `denominator-reconciliation` (G3 unit-incommensurable
capital; named-8 not an industry draw), `query-time-grouping-enough` (the W1 anti-sprawl
landing). No new tag needed — `traction-readiness` already exists from run-029 and fits.

"No new primitive needed" is a valid outcome — and is the standing outcome here.

## Next-run advice

- The clean follow-on is the **telehealth-Signals-delta momentum read** (scout candidate 3):
  the telehealth slice is the one cohort with real 2+ dated `signals/` captures, so it tests
  frame #2 (comparability) where this cohort couldn't. Watch for run-018 overlap.
- A second probe: **run `signals/` once on beta-team** (public filer, cheapest case) to see
  whether a single SEC/IR capture + a later diff produces a usable per-company momentum read
  — but that is spend/approval-gated, out of an autonomous store-only cycle.
- Avoid re-running the size/stage read on another static cohort — it will keep collapsing
  onto maturity (S2). Traction only becomes its own axis once a 2nd capture exists.
