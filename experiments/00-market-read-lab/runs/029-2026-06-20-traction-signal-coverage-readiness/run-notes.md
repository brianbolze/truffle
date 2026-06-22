# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [coverage-caveat, depth-backfill, denominator-reconciliation, freshness-monitoring, traction-readiness]
```

## 30-second operator read

- **Did it work?** Yes — clean gap-probe on the engine's *traction* axis, the lab's first.
  Store-only, no spend. Verdict: the store is at **rungs 1+3 of the frame's 5-rung ladder** —
  capture path + durable accumulation built and correct; traction *coverage* (16% of profiled
  cos), *comparability* (9% delta-able), and *cohort-rollup* (none) thin-to-absent. **No new
  primitive is the gap** — coverage + comparator-completeness + the deferred cohort layer are.
- **What was awkward?** Wayback's page-grain (`signals/wayback/<page>/<clock>.json`) needs a
  deeper walk than the other source-types — the MRL-012/run-018 enumeration trap, avoided here.
- **Next agent should know:** the traction substrate is the sec_edgar+trustpilot **batch
  campaign on ~20 hormone/men's-health brands** → it inherits the corpus selection bias (MRL-001)
  *before* any rollup runs. Any "traction map" off today's store maps the campaign, not a market.

## What happened

Defined traction per `_design/2026-06-14-traction-frame.md` (Signals, 5-rung ladder). Walked
every `store/*/signals/` dir (Python) → per-company source-type × capture-count × delta-able
inventory; mapped each source-type to its traction axis (sec_edgar=capital, trustpilot=demand/
trust-flow, trends/serp/ads=attention; wayback/exa = NOT traction). Scanned `profile.md`
frontmatter+prose for any State traction field. Overlaid the inventory on the GLP-1 cohort
(19 strict-anchored; Loop-1 first mis-grepped 21, fixed in Loop-2) and telehealth-wide (54) to
test cohort-rollup readiness. Scored the store against the frame's
5 rungs. One receipt (R1). Emitted **no** traction/formidability score (frame's hard line held).

## Discovery ledger

Greedy raw learning for this run. Preserve singletons here before triage compresses
anything, then Loop 2 appends the useful rows to `discovery-ledger.md`. Do not merge
rows, dedup into backlog items, or translate wishes into build proposals inside the run.

Use short IDs such as `O1`, `W1`, `F1`, `S1`, or `G1` so reviews can cite them.

| ID | Kind | Raw observation / wish / friction / surprise / gap | Evidence or pointer | Why it matters | Discovery clock |
|---|---|---|---|---|---|
| O1 | observation | Only **20 of 126 profiled cos (16%)** carry a genuine traction signal (sec_edgar/trustpilot/trends/serpapi/ads), though 49 carry a `signals/` dir. | read.md C2; R1 inventory | The traction substrate is far thinner than the raw `signals/`-dir count implies — capture coverage, not architecture, is the binding rung-1 constraint. | ready-for-triage |
| O2 | observation | The **most-captured signal is the least traction-relevant**: Wayback covers 47 cos but measures page tenure/continuity, not "how is it doing"; exa (2) is neighbors. | read.md C3; R1 per-type table | Capture *volume* ≠ traction signal — the frame's grain-trap made concrete; a naive "49 cos have signals → traction-ready" read would be wrong. | ready-for-triage |
| O3 | observation | The 20 traction-signal cos are a near-identical **sec_edgar+trustpilot batch campaign on hormone/men's-health brands**; no behavioral/women's/SaaS co carries a traction signal except waldo/niagenplus. | R1 "traction-signal cos"; MRL-001 | Traction inherits the corpus selection bias *before any rollup* — a cohort traction-map would be doubly coverage-bounded (MRL-001 generalizes onto the traction axis). | ready-for-triage |
| G1 | gap | **Comparability (rung 2) is weak:** only 11/126 (9%) were delta-able on a traction type at run time, and most deltas were blocked/confounded — sec_edgar had no `signal_delta.py` branch then (4 cos; branch shipped 2026-06-22), SERP pairs hit subject-identity (2), Trends single-snapshot+fragile (5), only ~6 Trustpilot diff cleanly and that = solicitation cadence, not demand. | read.md C4,C5; run-018/MRL-012 | "Delta-able by cadence" ≠ "usable velocity." The comparator-completeness sub-gap narrowed on 2026-06-22, but the one broadly-covered clean axis is still the most confounded — rung 2 remains weak. | ready-for-triage |
| G2 | gap | **Cohort-rollup (rung 4) is not buildable today:** GLP-1 (most-captured cohort, **19** strict-anchored) has 5/19 any-signal, 4/19 delta-able, all sharing only Trustpilot; telehealth-wide 10/54 delta-able scattered across 3 axes — no axis ranks half a cohort. | read.md C7; R1 cohort overlay | Confirms with numbers why the maps consumer can't shortcut rung 4 from the per-company layer; validates the frame deferring it to a sibling frame. | ready-for-triage |
| V1 | value-miss/surprise | Loop-1 used a loose `^anchor_category:.*GLP-1` grep → denominator **21**; the Loop-2 evidence verifier caught it — strict value-field parse = **19** (nurx/prohealth carry GLP-1 in the `#` comment of a non-GLP-1 anchor line). The **run-016 "parse the value, not the comment" footgun, recurring**. Numerators (5/4) unaffected; fractions corrected to 5/19, 4/19. | verifier verdict; read.md C7; R1 method caveat | Third sighting of the anchored-only/comment-parse denominator hazard (MRL-001 family) — the adversarial pass is what caught it, exactly as in run-016. | ready-for-triage |
| V2 | value-miss | Consumer review: the 20-co **axis distribution** (≈all sec+trustpilot, only 5 trends, 2 serp, 1 ads) lived only in R1, not inline in read.md; and rung-3 "Accumulate=Yes" lacked the no-refresh-cadence caveat. Both folded into read.md. | consumer-review.md lens check | First-pass synthesis-shape misses a fast reader could trip on; fixed, not a template change. | notice-only |
| S1 | surprise | The store has built the traction **plumbing** (path + comparator + 6 tools, v1) but not the **substance** — rungs 1/3/5 are built/correct, rungs 2/4 are thin/absent. "Machinery ahead of coverage." | read.md Result ladder table | Reframes the traction gap as coverage+comparator+cohort-layer work, NOT a missing primitive — consistent with MRL-012, now generalized from change-pulse to the whole traction axis. | ready-for-triage |
| S2 | surprise | State layer carries **0** structured traction fields — and that is **correct**, not a gap (the frame says traction never lands in `profile.md`); 29 profiles mention funding/public-market status only incidentally in prose. | read.md C6 | The State/Signals boundary held under a real traction read; calling "0 traction fields" a defect would be the failure-mode trap, avoided. | notice-only |
| W1 | wish | If anything graduates, it's **coverage + comparator completeness + the deferred cohort layer**, not a new primitive: a traction-capture campaign on one real cohort plus the now-shipped sec_edgar delta branch (MRL-012) is the lightest path from "not buildable" toward "testable." | read.md What Would Change | Names the lightest path to a real cohort traction-map. The code branch shipped 2026-06-22; the capture campaign remains spend/approval-gated. | recur-watch |
| F1 | friction | Inventorying signals needed a per-source-type walk plus a **deeper page-grain descent for Wayback** (`signals/wayback/<page>/<clock>.json`); a company-grain glob silently under-counts Wayback subjects. | run-notes friction log; MRL-012 run-018 catch | Mirrors the recurring multi-grain enumeration friction (MRL-001/012 family); one sighting, recur-watch only. | recur-watch |

## Inputs and scope

- **Universe:** 135 store dirs / 126 profiled (`profile.md`) / 54 with `telehealth.md` / 49 with `signals/`.
- **Queries:** Python walk of `store/*/signals/` (source-type × capture count × distinct-timestamp delta-able), with page-grain descent for Wayback. `awk` frontmatter + grep prose scan over `profile.md`. `anchor_category: GLP-1` grep over `telehealth.md`.
- **Design inputs:** `_design/2026-06-14-traction-frame.md` (5-rung ladder, axis vocabulary), `_design/2026-06-15-traction-approach.md` (v1 signals path), MRL-012 / runs/018 (comparability findings).
- **Exclusions:** no live web, no signal re-capture, no `signal_delta.py` execution (cited run-018's deltas instead — store-only discipline), no score/verdict emission.

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

The only friction was the Wayback page-grain descent (F1) — a company-grain glob silently
under-counts Wayback subjects, so the walk had to descend to `signals/wayback/<page>/<clock>.json`.
Same multi-grain enumeration family as MRL-001/012; one sighting, recur-watch.

## Evidence limits

- **Coverage counts are capture-campaign artifacts, not market facts.** `signals/` presence
  reflects which companies a prior campaign captured (hormone/men's-health-heavy), not which have
  real-world traction. Absence = **not captured**, never "no traction."
- **"Delta-able" overstates rung-2 quality.** It means ≥2 dated captures of a traction type
  (cadence exists), not a clean usable velocity — the gap between the two is itself the finding
  (G1), grounded in run-018/MRL-012 rather than a fresh delta run.
- **Cited, not re-derived:** comparability *quality* numbers (≈6 clean Trustpilot velocities, no
  sec_edgar branch, SERP subject-identity) come from run-018/MRL-012, not a new `signal_delta.py`
  sweep — store-only discipline. The *coverage* census (20/11, cohort overlays) is fresh this run.
- **Axis mapping is interpretive** but follows the frame + SIGNALS.md; the wayback/exa = NOT-traction
  calls are the load-bearing interpretation and are stated as such.

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
- No disallowed action happened: **pass** (no live web, no spend, no store mutation, no score emitted)
- Required citations / receipts present and source-graded: **pass** (R1, all claims C1–C8 mapped)
- No snippet treated as evidence: **pass** (all store-derived)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no external/current claims made; capture clocks recorded in R1)
- Absence language says "not found", not "not true": **pass** ("not captured" / "capture-campaign artifact" used throughout)

## Surprises

- **Plumbing ahead of substance (S1):** I expected either "no traction layer" or "a working
  traction layer." Reality is neither — the *architecture* (path/comparator/tools) is built and
  correct, but it's populated for only 16% of profiled cos on a non-traction-dominated mix. The
  gap is coverage+comparability, not design.
- **The richest captured signal is the least useful one (O2):** Wayback dominates capture volume
  (47 cos) but is the one source-type that isn't traction at all.
- **The State/Signals boundary held cleanly (S2):** 0 structured traction fields in `profile.md`
  is exactly what the frame prescribes — the absence is a feature, and the failure-mode trap
  (reading it as a defect) was real and avoidable.

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
| `coverage-caveat` | Only 20/126 cos carry a traction signal; the substrate is a hormone-batch capture artifact, not market-representative. | watch — this is the binding rung-1 constraint |
| `depth-backfill` | The traction signal layer is missing across most otherwise-relevant cos; a cohort capture campaign would backfill it. | watch — feeds the rung-4 prerequisite |
| `denominator-reconciliation` | The 49 (any-signal) vs 20 (traction) vs 11 (delta-able) distinction, plus inherited selection bias (O3), governs every count. | watch — MRL-001 generalizes onto the traction axis |
| `freshness-monitoring` | Captures cluster 06-08→06-15 with no refresh cadence; a traction read is only as live as the last manual capture. | watch — MRL-012 cadence gap |
| `traction-readiness` *(new)* | **Coined.** The store's position on the traction-frame's 5-rung ladder (built: 1/3/5; thin/absent: 2/4) — no existing tag captures "capability-ladder rung position on the engine's named future axis"; `coverage-caveat`/`depth-backfill` cover symptoms, not the ladder framing. | submit-candidate (Loop 2): first sighting on the traction axis; recurrence handle for a 2nd traction read |

## Optional triage evidence

Normally none. Add only concrete backlog evidence, with priority/status suggestions,
when the run has more than a raw singleton or when review adds evidence to an existing
item. Keep this to 1-3 backlog-ready bullets plus pointers to the Discovery ledger,
`discovery-ledger.md`, or run artifacts.

**Do not implement, spike, or recommend immediate graduation from inside the run.**

**Staged for Loop 2 (not submitted to triage from Loop 1):** This run is mature evidence,
not a singleton — candidate for a **new MRL item** (`traction-readiness`: the store sits at
rungs 1+3 of the frame ladder; binding constraints are coverage → comparability → cohort layer,
in that order, none a missing primitive). It also adds an Evidence Log entry to **MRL-012**
(change-pulse generalizes to the whole traction axis: comparator incomplete at run time, sec_edgar
branch was the cheapest fix and shipped 2026-06-22) and to **MRL-001** (selection-bias denominator now bounds the traction
substrate). Loop 2 decides whether to open the new item or fold into MRL-012. Do **not** propose
a traction score/field — the frame's hard line and W1 both say coverage+comparator+cohort-layer,
no new primitive.

## Next-run advice

- **Highest-leverage follow-up (spend-gated, not autonomous):** a bounded traction-capture
  campaign on one *real* cohort — e.g. capture sec_edgar+trustpilot+trends+serp for all 21 GLP-1
  brands, twice with pinned subjects — to move rung 4 from "not buildable" to "testable." This is
  the MRL-009 worklist pattern on the traction axis; needs Firecrawl approval.
- **Cheapest code fix:** the sec_edgar delta branch in `signal_delta.py` (MRL-012, ~30 min) —
  shipped 2026-06-22. It turns existing repeated SEC captures into source-local capital-axis deltas;
  the remaining blocker is capture coverage/cadence, not this branch.
- **To harden the pattern:** run a 2nd traction read on a *non-hormone* cohort; if it finds the
  same 1+3-built / 2+4-thin shape, "plumbing ahead of coverage" becomes a roadmap fact, not a
  one-run pattern. Tag it `traction-readiness` for the recurrence grep.
- **Avoid:** reading any empty traction cell as "no traction" (it's "not captured"), and never
  emit a traction/formidability verdict — the open edge stays with the consumer.
