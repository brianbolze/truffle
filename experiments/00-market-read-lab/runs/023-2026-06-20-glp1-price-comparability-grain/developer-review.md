# Developer Review

Question: **What Truffle system behavior does this run pressure?**

**Recommendation up front: no-op-with-watch + two Evidence Log appends.** A clean, steward-
correct run that *defends* an existing boundary rather than pressuring a new one. No new triage
item; the two submissions add genuine color to MRL-002 and MRL-008 but are reinforcement, not
novelty.

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Capture** | Nothing new — store-only meta-audit; existing captures were sufficient and well-graded. | No-op. |
| **Structure** | The `visibility: published/partial` field is doing the comparability work, but it was designed as a price-*transparency* flag and is being read here as a price-*completeness* gate. Those mostly coincide, not always. | Document the nuance in the MRL-002 recipe; **do not** add a field. |
| **Query / access** | "Comparable price" is a query-time normalization over 4 axes (what's-included via `visibility`; cadence/commitment; steady-state-vs-promo; binding-vs-floor) — all reconstructible from existing State. | Recipe candidate for MRL-002. No persisted normalized-price field. |
| **Freshness / automation** | ~8/19 prices are promo/point-in-time; a price-compare is freshness-bound. | Recurrence of MRL-012; no-op. |
| **Synthesis** | The read's derived-figure fencing ([J], "computing them *is* the failure mode") is a model for judgment-labeling caveat language. | Keep as a positive exemplar. |
| **Guardrails** | Run proactively flags against graduating a derived effective-price field. | Keep the anti-graduation note on MRL-002. |

## Lenses

**Steward** — System stayed honest. Provenance (verbatim store reads, per-brand capture dates),
grain (entry-tier only, explicitly floored), and the State/Signals/Judgment line all held. The
intra-brand conflicts (directmeds, tryshed) were *held, not resolved* — correct; "which surface
bills" is framed `not found`, not absent. The State→Judgment boundary on the derived figures
(eden ~$198, hims ~$298) is the strongest part of the run: labeled `[J]`, broken into their own
claim class, argued *against* persisting. No leak.

**Dev Agent** — The one real toil signal: pricing lives in ≥3 shapes per `offerings.md` (Roster
`Price (verbatim)` row vs `site_notes` prose vs Verbatim-anchors block), so extraction needs
per-file judgment, not one grep. This does **not** earn a helper — one sighting at this grain,
and a parser over three freeform shapes is exactly the brittle living code the engine resists.
The right response is the *recipe* note ("read per-file; prefer the `Price (verbatim)` +
`Visibility` columns"), not a tool.

**Founder** — Compounds the warm/cited/cheap asset perfectly: zero spend, zero writes, and it
*protects* the asset by refusing an ontology-gravity field that would make the store lie over
time. Exactly the light move. This is the no-auto-graduation convention used proactively.

## Is the "no new primitive" call right?

Yes, and earned rather than asserted. A persisted `effective_monthly_price` would (a) rot —
8/19 inputs are promo/point-in-time, several flagged "subject to change"; (b) bake a judgment
into State — every axis collapse is a modeling choice. That is living infrastructure wearing a
State costume, against the engine's "spend on durable conventions, not living infrastructure"
line. The verbatim string + `visibility` flag + `site_notes` + a query-time rubric is the
lighter, truer substrate.

## New evidence vs recurrence (honest)

- **MRL-002 (query recipes):** *Genuinely additive, modestly.* ~9th State-read surface, and the
  first where the load-bearing finding is a *normalization rubric* rather than a group/label cut.
  New flavor; same conclusion (no helper, no field).
- **MRL-008 (source-rigor):** *Additive flavor.* A new price-specific member of the confound
  family — promo-framing is a *within-kind* confound (the number isn't steady-state even after
  the unit is fixed). Overlaps the run-012 listicle/affiliate entry; narrow novelty.
- **MRL-001 (denominator) / MRL-012 (freshness):** Pure recurrence; correctly tagged no-op in
  run-notes.

## Recommendation

- **No-op / keep as observation:** the run as a system-change driver. No new item.
- **Watch for recurrence:** the `visibility` transparency-vs-completeness dual reading; the ≥3-
  surface price-extraction toil.
- **Submit triage candidate:** two Evidence Log appends only (below). No graduation.

## Triage submissions

Append-only Evidence Log color for existing items — steward decides folding:

- **MRL-002** — *Run 023: normalization-rubric flavor.* "Comparable price" is a query-time 4-axis
  rubric (what's-included via `visibility`; cadence/commitment; steady-state-vs-promo; binding-
  vs-floor) over existing State — no persisted normalized field. Nuance: `visibility` is being
  read as a *completeness* gate adjacent to its *transparency* origin. Friction: price lives in
  ≥3 `offerings.md` surfaces; prefer the `Price (verbatim)` + `Visibility` columns. **Explicit
  anti-graduation flag:** do not persist a derived effective-monthly field (rots, judgment-laden).
- **MRL-008** — *Run 023: promotional / point-in-time price sub-case.* ~8/19 entry prices are
  struck-through / code-gated / sale-framed; 2 brands (directmeds, tryshed) carry intra-brand
  conflicts. A promo-framed captured price should be treated snippet-grade for any
  "cheapest/ranking" claim until reduced to the recurring rate. Additive; does not move the
  graduation clock.

**Did not graduate, spike, or implement any system change.**
