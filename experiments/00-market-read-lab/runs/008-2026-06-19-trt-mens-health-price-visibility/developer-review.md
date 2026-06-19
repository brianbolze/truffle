# Developer Review

Question: **What Truffle system behavior does this run pressure?**

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Capture** | No new pressure. The `offerings.md` `Visibility` column carried the entire load off disk, zero re-capture — the cleanest validation yet that the capture contract works for State reads. Only gap: mdpep-com is a bare directory (missing capture, not a schema failure). | None. Optionally backfill mdpep-com. |
| **Structure** | Mild. The only real labor was drawing the TRT/longevity and exogenous-T/SERM boundary by hand from `telehealth.md` frontmatter. The fields (`anchor_category`, `audience`) exist; what's missing is a *convention* for where a multi-cohort straddler (Hone, getOpt, Lifeforce) lands when the boundary changes the answer. Field grain is ambiguous, not absent. | None now — name the straddle explicitly at query time (MRL-001 scope). |
| **Query / access** | Real, confirmed recurrence. The loop — frontmatter grep → latest-capture + `Visibility`-row extract → group/label — has now run identically on GLP-1 (000) and TRT (008), previewed in Signals 005/006/007. | MRL-002: a documented State price-posture recipe. No helper script yet. |
| **Freshness / automation** | No new pressure. Captures ≤16d; the A/B-volatile flag on Marek/Maximus is a data-quality note, not a freshness-loop gap. | None. |
| **Synthesis** | Moderate, at the State→Judgment boundary (below). The Loop 2 correction also shows the read template let an aggregation error (Kingsberg) slip past Loop 1's exit check — an *adversarial verifier pass* caught what the self-check did not. | Keep the adversarial Loop 2 shape; it earned its keep this run. |
| **Guardrails** | Held well. Capture-gap vs intake-gate kept throughout; the one fuzzy case (Kingsberg) was reclassified, not rationalized. Denominator partiality explicit; no absence-as-proof language. | None. |

## Lenses

**Steward — is the system still honest?** Yes, and more so after Loop 2. The honesty mechanisms held
(partial denominator named, capture-gap/intake-gate separated, C3/C4 labeled Judgment, n caveats), and
the adversarial pass *corrected* the one aggregation error (Kingsberg gated→partial) from the brand's
own captured file rather than from outside knowledge. No drift. The notable lesson: Loop 1's self-run
exit check passed an aggregation that was internally contradicted by its own receipt evidence — the
independent verifier is what caught it. That validates the three-pass Loop 2 design.

**Dev Agent — can repeated toil be removed?** The cohort-boundary hand-draw is the one recurring step,
and it splits into two sub-problems: (1) frontmatter grep to derive a working set — *automatable* with
a simple recipe (filter `telehealth.md` by `anchor_category` + `audience`); (2) the boundary judgment
for multi-cohort straddlers — *not* automatable, inherently question-dependent. The right move is a
recipe that automates (1) and **surfaces the straddlers for human judgment** rather than silently
forcing a call. This is MRL-002's scope; no new item.

**Founder — does it compound the asset while staying light?** Yes. Zero new credits, a durable
re-queryable receipt, and a two-category pattern reusable in the next read. The `offerings.md` schema
earned its keep — the `Visibility` column answered the question off disk. No new primitive, no taxonomy
entry, no schema change proposed.

## The State / Judgment boundary (C3, C4)

C3 ("posture tracks business model, not molecule") is a Judgment, correctly labeled — but a *grounded*
one: it's a cross-tabulation of per-brand State across two cohorts, closer to a query-time aggregation
than an opinion. It survived adversarial scrutiny. C4 ("same gaters across categories") is weaker —
now n=2 (Defy, Marek) after Kingsberg was reclassified — and appropriately hedged.

The design signal worth noting (not a triage item): the system has **no durable home for a Judgment
derived from State**. C3/C4 live only in this run's `read.md`; a downstream consumer who wants to build
on them must re-read the run. That is the *right* posture for a prototyping engine today — Judgments
stay out of the shared store, and the engine's frame already flags the Judgments layer as actively
being reworked. But the pattern (State → query → grounded Judgment → no durable home) is now concrete.
If a third category read replicates C3/C4, that pattern will need a home.

## Recommendation

- **No-op / keep as observation:** the State→Judgment artifact gap — right constraint for a prototyping
  engine; do not open an item from one run.
- **Watch for recurrence:** if a third store-only category read (longevity/NAD or sexual-health)
  replicates C3/C4, *then* open a Judgments-persistence item. Also watch the multi-cohort straddler
  encoding (Hone/getOpt/Lifeforce) as it recurs under MRL-001.
- **Submit triage candidate:** none new. The run's self-report is accurate — this adds recurrence
  evidence to MRL-002 (State recipe) and MRL-001 (denominator/straddler), appended as Evidence Log
  entries below.

## Triage submissions

No new items. Evidence Log entries appended to MRL-002 and MRL-001 in `triage.md`.
