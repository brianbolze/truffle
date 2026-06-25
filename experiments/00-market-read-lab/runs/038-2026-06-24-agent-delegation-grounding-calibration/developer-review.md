# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | Gap (source-scope, not miss): the two ungroundable types — state-level availability and audited price/scale — live **off the marketing site** (behind intake, or in filings/IR). No marketing-page capture recovers them; the store flags the boundary honestly. | read.md Result(4), Source Gaps | G1 · gap; G2 · gap |
| **Structure** | Strength: the schema holds everything the captured surface exposes — price-visibility tokens, business_model, `unverified_fields` all did their job. The frontier is *what was capturable*, not *what the schema can express*. | read.md Result(1)-(2); price tokens 7/8 | (no structural defect) |
| **Query / access** | Strength: one grep set the panel; per-ingredient-type judgment was the work. The reusable contract insight is "gate delegation by ingredient *type*, not by per-company readiness" (S1). | read.md Companies Seen; S1 | S1 · surprise |
| **Freshness / automation** | Note: prices are promo/A-B snapshots; the structural read is unaffected, but an all-in-price read would need refresh + intake. | read.md Missing/Stale Coverage | (evidence-limit, not a system gap) |
| **Synthesis / Guardrails** | The load-bearing pressure: self-reported proof/scale is captured *with* honest flags, but the flag is **prose-grade** — protection is read-discipline-dependent. A delegated agent relaying the claim without the flag launders marketing into fact. The fix (if any) is a relay convention, not a field (W1). | read.md Result(3); R1; W1 | R1 · risk-miss; W1 · wish |

## Lenses

**Steward** — System stays honest. State / Signals / Judgment separation held cleanly: the
read labeled "brand asserts X" vs "X is true," and tied its one market Judgment (the
grounding frontier mirrors the industry's disclosure frontier) back to State. The integrity
risk is downstream of the store (relay, R1), not in it.

**Dev Agent** — No toil to remove; the denominator was one grep. The reusable insight is a
*reading/relay convention*, not a helper: carry the self-reported flag and the intake-gated
price caveat into any delegated output (mirrors L004's "reconciliation travels with the
read"). Grep-verifiable, no new knob.

**Founder** — Compounds the warm asset (the typed grounding map + panel are reusable) and
stays light — lands "no new primitive needed," resists both an availability field and a
provenance field. The temptation to "capture intake-flow data" is correctly parked behind a
real consumer + spend gate (G2).

## Recommendation

Record the disposition as an observation; do not propose or graduate a lesson here.

- **No-op / keep as observation:** yes — "no new primitive needed" is right at n=8 with no
  filter-needing delegated consumer. W1 names the lightest path (a relay convention) *if* it
  ever graduates. The developer review surfaces **no new gap** beyond the run's own rows —
  G1/R1/S1/G2/W1 cover the pressure; no DR rows added (no-op on new dev sightings).
- **Watch for recurrence** (`learning_tags`): the "decision-grade lives off the captured
  surface" boundary now has **three sightings** (036 marketplace take rate, 037 hybrid
  economics, 038 GLP-1 price/availability via `source-panel` + `coverage-caveat`). A
  learning pass may cluster these into one "the store's grounding frontier *is* the
  source-scope frontier" lesson. That is the pass's call, not this run's.
- **Severe `risk-miss` to surface now:** R1 (prose-grade self-reported flags + relay risk)
  is the one to flag — it is a live integrity risk against the engine's #1 value job
  (safe delegation), though scoped as a relay-discipline observation, not a proven defect.
  It is a delegation-grain cousin of L002 (a headline reads decision-grade only with its
  confound sibling) — worth a pass's attention alongside L002.

## Raw learning to preserve

Appended to `learning/observations.md` this pass: the run's own rows — **G1** (state
availability systematically invention-forcing, intake-gated), **R1** (self-reported flags
are prose-grade; relay risk), **S1** (grounding is ingredient-type-shaped, not
brand-shaped), **G2** (both shortfalls share the off-surface root; 3rd sighting), **W1**
(lightest path is a relay convention, not a field). No developer-discovered rows added —
the run's rows already carry the capability pressure.

**Did not propose lessons, graduate, spike, or implement system changes.**
