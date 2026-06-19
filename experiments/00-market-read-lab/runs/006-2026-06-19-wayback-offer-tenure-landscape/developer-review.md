# Developer Review

Question: **What Truffle system behavior does this run pressure?**

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Capture** | Wayback captures are mostly one URL/domain (root *or* an offer page, rarely both), so brand-vs-offer tenure can't be compared within a brand. Not a primitive gap. | Optional capture-parity task (root + key offer page for the ~10 offer-only brands). Not triage-worthy; a normal capture chore. |
| **Structure** | Tenure is cleanly Signal (captured `first_seen`/snapshots) + downstream Judgment ("how established"). No new field/module needed. | No-op. `query-time-grouping-enough` holds. |
| **Query / access** | 2nd consecutive Signals-consumption read to hand-roll the latest-per-dir + field-extract loop — the exact recurrence Run 005 named as the trigger. | **Append to MRL-002**: documented QUERYING signals-read recipe candidate (latest-per-dir, field extraction, which confound fields to always pull). Pattern-level, not a built helper. |
| **Freshness / automation** | Per-domain signal path worked; no homeless category-level signal surfaced. | No-op note to **MRL-007** (no new evidence; per-domain path fine again). |
| **Synthesis** | The reliable sub-slice (offer-page tenure) is under-surfaced vs the unreliable headline (root `tenure_days`). Output-ergonomics observation. | Watch only. Not a convention yet. |
| **Guardrails** | `tenure_days` reads as decision-grade but is brand-age-misleading for reused domains; the discriminator (snapshot density / status-trail gaps) lives in the JSON unsurfaced. | **Append to MRL-008** (captured-signal-interpretation rigor), with a root-cause note (below). |

## Lenses

**Steward — honest?** Strong. State / Signal / Judgment split maintained: `revival candidate` is
labeled `[Judgment]` in the read and "derived heuristic, not proof of ownership change" in the
receipt; the C5 anachronism is correctly framed as internal-consistency, not an external founding
claim. Confound flags (`snapshots_truncated`, 8 missing-signal packs, offer-vs-root imbalance) all
declared. **Minor readability note:** the Companies Seen "age-credible? yes" column is also Judgment
but isn't marked inline, so the table could read as ground truth if quoted alone — not a provenance
failure. **Accuracy note:** an adversarial verifier recomputed every headline count from raw JSON —
C1 (47/55/49), C2 (39/16), C3 range, C4 spot-checks, offer-page values all CONFIRMED exactly; it
caught one receipt miscount (pre-2020 root pool was stated 29, true deduped count 27 — the raw glob
double-counted onemedical + eden-health) and two silent omissions (lifemd/rexmd from the diagnostic,
tryshed from C5). **All three were corrected in the receipt before review closed.**

**Dev Agent — can toil be removed cheaply?** Both triage appends are the smallest useful response
and neither proposes a build. MRL-002's recurrence condition was met verbatim. MRL-008's evidence is
real, **but the two sightings have structurally different root causes** worth flagging if it ever
graduates: Run 005's Trustpilot confound is an *intrinsically ambiguous field* (score conflates
regard with solicitation no matter how careful the reader); Run 006's tenure confound is a *correct
archive fact misread by naive consumers* (the signal isn't wrong, the interpretation is). The shared
family ("captured-signal confounds must travel with the field") is fine for pattern-watching; the
distinction matters for what any eventual convention says. No over-eager pattern-matching beyond that.

**Founder — compounds the asset, stays light?** Yes — the cleanest run yet on this axis. Store-only,
no spend, no mutation; a free, 3-day-old captured signal produced a durable, generalizable finding
("the clean-looking number is the most wrong") that survives any re-run. Anti-Doro check passes:
nothing proposed needs a standing server, running index, or entity-resolution — "document a recipe
in QUERYING" is durable convention, not living infrastructure. No `brand_age` computed-field
temptation taken.

## Recommendation

- **No-op / keep as observation:** synthesis under-surfacing of the reliable offer-page slice;
  Companies-Seen judgment-label readability; capture-parity chore.
- **Watch for recurrence:** a 3rd Signals-consumption read re-handrolling the density diagnostic
  from raw `snapshots` arrays would firm up the QUERYING-recipe case (MRL-002).
- **Submit triage candidate:** MRL-002 evidence append (2nd Signals-grain sighting); MRL-008
  evidence append (2nd signal-interpretation sighting, with the root-cause distinction noted);
  MRL-007 no-op note.

## Triage submissions

- **MRL-002 — evidence append** (2nd Signals-grain sighting; recurrence Run 005 named).
- **MRL-008 — evidence append** (2nd captured-signal-interpretation sighting; note the
  intrinsic-ambiguity vs naive-read-trap root-cause split).
- **MRL-007 — evidence append** (no-op note: per-domain signal path worked again; no homeless
  category-level signal this run).
- **No new queue item.** No new primitive; the pressures are interpretive/ergonomic, already homed.
