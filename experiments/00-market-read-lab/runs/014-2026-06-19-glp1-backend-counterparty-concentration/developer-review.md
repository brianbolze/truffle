# Developer Review

**Question: What Truffle system behavior does this run pressure?**

This run was the designed MRL-005 recurrence re-test. It answers the question structurally — and the
answer is "partially fires, in a different direction from the original hypothesis." An independent
evidence-verifier pass confirmed every load-bearing number against `store/` (19; 16/3; OpenLoop ×2;
3 dangling pharmacies; 14 unnamed) with no overclaims.

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Capture** | Named pharmacy counterparties (CraftedRx, Triad Rx, RedRock, Beaker) appear on owned pages but have **no store profiles** — the edge would dangle even if a schema could hold it. The clinical name (OpenLoop) *does* have a profile and resolves cleanly. | No capture action now. If MRL-005 graduates, pharmacy-name profiles become prerequisites, not side-effects. |
| **Structure** | Answering "who does brand X depend on" needed *both* `profile.md` frontmatter (`parent`/`owns`) and `telehealth.md` prose. The only clean joinable relation is the clinical-provider edge, not the pharmacy edge. MRL-006's split is real and stable across two cohorts. | No schema change. The minimal shape — a dotted-domain frontmatter key (`clinical_provider:`/`pharmacy_partner:`) populated only when the entity resolves to a store profile — remains right but **does not need to exist yet**. |
| **Query / access** | "Named vs unnamed" is a per-body prose read, not a field lookup; per-entity resolution is a manual `ls store/*<name>*`. Tolerable at cohort size; two cohorts (001 + 014) now share the loop. | Absorb into MRL-002 as a relation-read recipe variant *only* if a third cohort re-invents it. No helper. |
| **Freshness / automation** | Not pressured — pure store State, no Signals touched. | None. |
| **Synthesis** | State/Signals/Judgment stayed clean: named-vs-unnamed = State; OpenLoop recurrence = observed State; "concentration" explicitly refused; the clinical-lead verdict labeled Judgment. The "absence of a name ≠ absence of a relationship" floor framing is the right posture. | Candidate language for a future relation-read recipe: *"report the named floor, not an inferred ceiling — absence on owned pages is 'not stated,' not 'no relationship.'"* |
| **Guardrails** | No violations: no store mutation, no auto-graduation, Loop 1 exit check clean. The read refused "concentration" for a 2-brand recurrence — exactly the discipline the guardrails exist for. | None. Threshold note: a *third* brand naming OpenLoop makes "concentration" defensible. |

## Lenses

**Steward** — The read is honest; the three-layer separation held. The "floor, not ceiling" framing on
the 14/19 unnamed majority is the right move. One flag for any future graduation: the read calls eden's
Eden Pharmacy an "owned sibling" because it sits in `profile.md` `owns:`, but Eden Pharmacy has **no
store profile** — the `owns:` edge is structurally clean yet the join target is stub-only. The read notes
this correctly; the steward should watch that future relation guidance doesn't conflate structural
cleanness with profile completeness.

**Dev Agent** — The manual loop is two cohorts old (grep anchored cohort → read each `telehealth.md`
body for named entities → resolve via `ls store/*<name>*`). Tolerable; the per-entity resolution step is
the only thing near toil, and "near" is not "there." No helper warranted. Bigger structural point: the
pharmacy edge is un-answerable at join depth not because the schema can't hold it but because the
pharmacy profiles don't exist — a corpus-health dependency that should gate any MRL-005 graduation talk.

**Founder** — Compounded the warm asset correctly: existing captured State, a narrow structural question,
a genuinely novel finding (clinical-backend, not pharmacy) the original hypothesis missed, at zero
credits and no live browse. No ontology gravity — the run explicitly rejected the edge-table and landed
on the minimal dotted-domain shape. The durable prior worth keeping: white-label *clinical*
infrastructure is more visible on owned pages than white-label *pharmacy* infrastructure, so the
clinical-provider edge is likely the more answerable relation surface store-only long-term.

## MRL-005 graduation call

**Hold, but update the framing.** What the run added over run 001: a second cohort confirming
"named is the minority" (5/19); the first concrete store-joinable cross-brand counterparty (OpenLoop, 2
brands); proof the joinable edge is *clinical*, not pharmacy. What's still thin: one recurring entity /
two brands (a lead, not a pattern); the pharmacy edge remains un-answerable at join depth; the clinical
edge is a sub-question MRL-005 didn't anticipate, so graduating on a different edge than the one that
motivated the item would be sloppy. The item should no longer be framed *purely* as a pharmacy edge —
run 014 shows clinical-provider is the higher-signal surface. Graduation bar: a third brand naming
OpenLoop (or another clinical network recurring across ≥2 brands in a second cohort). The dotted-domain
frontmatter shape (`clinical_provider: openloophealth-com`, populated only when the entity resolves to a
profile) is the correct minimal surface — grep-verifiable, no living infrastructure, no relation
registry — it just doesn't need to exist yet.

## Recommendation

- **No-op / keep as observation:** Eden Pharmacy stub-only join target; joinfridays uncaptured partner list.
- **Watch for recurrence:** Clinical-backend shared-infrastructure across non-GLP-1 cohorts (OpenLoop,
  SteadyMD, Wheel in hormone/men's-health/ED). A third brand naming OpenLoop in any cohort → revisit MRL-005.
- **Submit triage candidate:** Additive Evidence Log entries to MRL-005, MRL-006, MRL-001 (in `triage.md`).
