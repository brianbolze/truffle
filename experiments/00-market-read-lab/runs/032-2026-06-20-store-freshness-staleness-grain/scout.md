# Scout

## Prior Context Read

- `triage.md`: 16 live items. The most-relevant standing pressure for this slate is the
  recurring `freshness-monitoring` tag (fired in runs 006/010/018/023/025/029) and
  **MRL-012** (change-pulse readiness = capture-cadence + subject-identity + tooling, not
  a primitive). Freshness has fired six times but never had a dedicated **State-axis**
  calibration run — run 018/MRL-012 worked the **Signals** axis (cross-capture deltas).
- `scout-context.md`: select for value + reach + roadmap learning, not store-answerability.
  "Trust the cache over time" is a named value job that has **not** had a direct run.
  `query-time-grouping-enough` and the persistence-boundary uncertainty are live design lenses.
- Last 3 `run-notes.md` (029 traction readiness, 030 external cross-shop, 031 self-uncertainty
  /confidence-grain): the lab has been calibrating the engine's **trust-metadata** layers —
  031 did the *confidence* axis (is a present value verified?). The natural untested sibling
  is the *time* axis (is a value still current?). 029/031 both landed "no new primitive,
  the gap is a convention/coverage." Watch for that being the default answer here too —
  but the persistence-boundary question (does freshness earn a durable marker?) is genuinely open.
- Current run artifacts: fresh scaffold, scout-only.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **A. Store freshness/staleness grain.** Across the captured store, can a downstream reader tell which profiles' market-sensitive State (pricing, offers, availability, policy) is at risk of being stale — and is `captured_at` + existing point-in-time prose + signals recency enough to flag that risk, or is there a freshness-grain gap the store cannot self-report? | calibration (+gap-probe) | yes | store-only | "Trust the cache over time" is a named value job with **no** dedicated run; freshness has fired 6× as a tag but only ever on the Signals axis (018/MRL-012). A delegating reader needs to know which facts might be out of date. | Freshness/change-pulse **surface** + persistence boundary: does capture-clock age (alone or with point-in-time prose + signals recency) let a reader gauge staleness risk, or does freshness earn a durable volatility marker? `query-time-grouping-enough` vs a new marker. | Whether the store can **self-report** staleness risk at all — a frontier distinct from "is the fact verified" (031). Whole corpus, cross-vertical (126 profiled, 2026-05-30→06-20 span). | Capture-clock distribution; point-in-time marker census (57 profiles); a sample audit that age ≠ staleness (stable fact / old capture vs volatile fact / fresh capture). | Equating capture **age** with staleness — old capture of a stable fact isn't stale; fresh capture of a volatile fact can be. "Old" ≠ "wrong." |
| B. Cold-start depth calibration. Pick ~8 captured cos across verticals — does one `profile.md` actually cold-start an unfamiliar company for a downstream reader: what's reliably present vs missing? | calibration | yes | store-only | Directly tests the **#1 value job** (Cold-start a company), never run head-on. | Per-company State completeness/depth grain; is the universal field set sufficient cold? | Whether one profile is judgment-ready solo, not just in aggregate. | A rubric of must-have cold-start facts; per-co present/absent scoring. | Subjectivity — "good enough" is reader-relative; risks a vibes read. |
| C. Offerings roster completeness audit. Across the store, can a reader trust offerings.md breadth as comprehensive, or is it a sample — and can the store self-report roster completeness? | gap-probe | yes | store-only | Connects to MRL-003 (depth-backfill) + the `/deepen-offerings` preset; "compare a whole field" needs trustworthy breadth. | The completeness/denominator uncertainty at the **offerings** grain; does a `roster_completeness` marker earn its keep? | Whether the store knows its own catalog completeness (likely no marker → frontier). | offerings.md presence/line-count census; sample vs site catalog spot-check. | Overlaps 031's "store can't self-report" finding; risk of re-deriving the same meta-result one grain over. |
| D. Signal cross-source agreement. For cos with ≥2 signal source-types, do the signals tell a consistent story or conflict? | calibration | yes | store-only | Tests whether multi-signal cos are corroborated or contradictory — a "safe to delegate" input. | Source-panel agreement grain; do signals need reconciliation (the anti-Doro line)? | Whether stacking signals adds confidence or just noise. | Per-co signal inventory + a consistency read. | Tiny N (run 029: only ~20 cos carry any traction signal, fewer with ≥2 types) → underpowered. |
| E. Capture-completeness stub audit. Run 027 found 9 capture-only stubs (no profile.md); how many partial/aborted captures exist store-wide and what breaks for a reader who hits one? | gap-probe | yes | store-only | Quantifies the MRL-001 "directory ≠ profiled" denominator hazard store-wide. | Denominator-reconciliation; the dir-vs-profile gap as a first-class coverage signal. | The store's own coverage honesty at the directory grain. | `ls` census of dirs missing profile.md / offerings.md / signals. | Narrow/mechanical — may be a 20-minute audit, not a market read; thin reader value. |
| F. New-capture loop closure (030 nominees). The run-030 cross-shop nominees (numan, maleexcel, fountaintrt, sesamecare) are now captured — does adding them change run-017's Hone substitute map? | value-read | yes | store-only | Closes the 030→capture loop; tests whether corpus growth shifts a prior relation read. | Relation-pressure + denominator sensitivity to corpus growth. | Whether prior cohort reads are corpus-fragile. | Re-run 017's substitute logic with +4 cos. | Merely executes a parked next step (scout-context "Avoid"); leans on a single prior run's frame. |

## Selected Question(s)

1. **Candidate A — Store freshness/staleness grain.** Strongest on value (an untested named
   value job), reach (whole corpus, cross-vertical, probes whether the store can self-report
   staleness at all), and a genuinely open design question (persistence boundary: does freshness
   earn a durable marker, or is capture-clock + point-in-time prose + signals recency enough?).
   It generalizes the most-fired-but-never-dedicated `freshness-monitoring` tag onto the **State**
   axis, sibling to run 031's confidence-grain read on the same trust-metadata layer.

   Runner-up: Candidate C (offerings completeness) — deferred to avoid re-deriving 031's
   "store can't self-report" meta-result one grain over; revisit if A lands clean.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Across the captured store, can a downstream reader tell which profiles' market-sensitive State (pricing, offers, availability, policy) is at risk of being stale — and is the capture clock (captured_at) plus existing point-in-time prose plus signals recency enough to flag that risk, or is there a freshness-grain gap the store cannot self-report?"
selected_slug: store-freshness-staleness-grain
run_type: mixed
question_mode: calibration
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "126 profiled companies (130 captured profile.md minus run-027 stub list; verify in Loop 1). captured_at present on 130 profiles; point-in-time prose on ~57; signals dirs on ~49."
likely_source_panel: "store/<domain>/profile.md frontmatter (captured_at, point-in-time/volatile markers in site_notes + unverified_fields) + store/<domain>/signals/<type>/<clock>.json clocks. No outside sources."
builder_lens: "The freshness/change-pulse SURFACE on the State axis + the persistence boundary: does capture-clock age (alone, or combined with point-in-time prose and signals recency) let a reader gauge staleness RISK, or does freshness earn a durable volatility/freshness marker? Tests query-time-grouping-enough vs a new durable marker."
reach_reason: "Probes whether the store can self-report staleness risk at all — a frontier distinct from confidence (031) and from Signals-axis change deltas (018/MRL-012). Whole corpus, naturally cross-vertical."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/ (lab artifacts, prior runs, triage, discovery-ledger)"
  - "SCHEMA.md, TAXONOMIES.md, _design/ (contract + freshness/change-pulse design intent)"
disallowed_actions:
  - "No live browsing, WebSearch, curl, or Firecrawl."
  - "No store/ mutation or write-back."
  - "No durable primitive creation; no triage graduation."
  - "No paid capture spend."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from local store frontmatter, signals clocks, and lab artifacts. Zero spend, read-only, no external sources."
loop1_failure_mode: "Equating capture-clock AGE with staleness (a clean count of old captures presented as a staleness map) without testing that age != staleness on a real sample — i.e. overclaiming a freshness problem from the easy distribution instead of mapping whether the store can flag VOLATILITY-weighted risk. Also: presenting the point-in-time marker census as a queryable freshness surface when it is heterogeneous prose (the 031 trap, one axis over)."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. Candidate A clears both tests:
**value** (a named, never-run value job with a real delegating reader) and **design**
(an open persistence-boundary call, not a foregone "no primitive"). It is deliberately
framed as a calibration/gap-probe so a "capture-clock is enough, no marker needed" result
is a first-class win, not a failure. The slate was optimized for reader value and
calibration against the freshness blind spot, not for store-answerability — though A is
store-answerable, its reach is whether the store can *see its own staleness*, which is not
guaranteed.
