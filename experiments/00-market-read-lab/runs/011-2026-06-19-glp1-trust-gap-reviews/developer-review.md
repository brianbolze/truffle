# Developer Review — Run 011: GLP-1 Trust Gap Reviews

**Question:** What Truffle system behavior does this run pressure?

Run 011 is the first bounded-live execution in the lab's history. All prior 7 reviewed runs were store-only. The question is not just "did the read work" — it is whether a standing, fully-wired convention ran correctly unattended, and what it teaches about three open system questions: bounded-live operability, MRL-010 status, and MRL-008's score-vs-body confound.

> **Adversarial verifier note (2026-06-19):** Loop 2 ran a 3-pass workflow (evidence verifier + consumer + developer, Sonnet). The verifier confirmed C1/C2/C4/C6 against the receipts verbatim and rated C3 and C5 *partial* on **framing**, not fact: C3 (henrymeds degradation) led with description before the Signal label, and C5 (owned-page gap) stated a flat owned-page claim where the evidence only supports "as captured in store State." Both were tightened in `read.md` after review (Signal label moved to the front of the C3 bullet; C5 scoped to captured State with an explicit "not re-fetched live" note). No fabricated quotes; bounded-live discipline audited PASS.

---

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Capture** | Review/forum bodies are high-signal for trust/objection questions and reachable via bounded-live at ~3-5 credits without sprawl. Trustpilot `?stars=` filter + `waitFor` worked first try; no retry, no proxy. The bilateral shape (live bodies + store State as rebuttal lookup) avoided paid re-fetch of owned pages entirely. | Recipe-level: name this bilateral read shape for reuse. No scraper, monitor, or new schema yet. |
| **Structure** | The store captures Trustpilot headline scores in Credibility blocks but not the review bodies. Score and body are different grains with different integrity contexts. A score-only read would conclude remedymeds is near-excellent (4.6); the bodies reveal the dominant billing-trap cluster. The store today holds the cause (billing terms in State) but not the effect (customer objection content). | Append MRL-008 evidence: score-vs-body confound flavor. MRL-010 third sighting. |
| **Query / access** | Store-State-as-rebuttal-lookup (free) + bounded-live bodies (paid) is a clean routing decision. No query recipe was needed; the read used straightforward grep on `profile.md` Credibility blocks + revenue-model lines. | No new recipe needed. The bilateral shape is worth noting for MRL-002 if it recurs on a second cohort. |
| **Freshness / automation** | henrymeds June-2026 service-degradation signal appeared in review bodies and post-dates the 2026-06-04 store capture. The store's captured State would have entirely missed it. The bounded-live layer is where freshness-sensitive signals emerge; no current mechanism routes them to a Signal capture path. | Watch. The degradation sits correctly as a labeled Signal; no auto-escalation needed. If it recurs, a review-body→Signals handoff convention earns a look. |
| **Synthesis** | The bilateral structure (live objection panel + store owned-page rebuttal lookup) is a reusable read shape for trust/objection questions. One synthesis judgment ("the credibility lane is saturated") crossed into positioning territory without a Judgment label. | Watch. Minor; consider a read-template note about labeling competitive/positioning conclusions as Judgments. |
| **Guardrails** | Stop rules held: Reddit kept snippet-only, bounded to 3 brands, no owned-page live re-fetch when State sufficed, no store write-back, no graduation. The `loop1_failure_mode` prediction ("treating a sampled panel as 'customers think X'") did not materialize. | Pass. No guardrail change needed. |

---

## Did the bounded-live convention work?

**Yes, cleanly.** The plan executed unattended inside its stated budget (5 credits, 4 sources, 3-brand cut, stopped at plan boundary). Stop-rules failed closed rather than expanding into a crawl. Evidence: `live_evidence_used` logs all 4 sources with spend notes, capture dates, and source grades; Reddit held at snippet/direction-finding; owned-page rebuttal from captured State, not a paid re-fetch; henrymeds degradation labeled a Signal; no scope creep to the other 16 GLP-1 store brands despite "People also looked at" surfacing adjacents.

One judgment call: the run stopped because "clusters were obvious after 3 brands." Right call, but it relied on the agent reading a qualitative stop rule. If a future run has murkier clusters the stop decision is harder. No change needed now — watch item for the 3-run review window.

**What bounded-live did that store-only could not:** the entire objection-cluster dimension — billing-after-cancel, CS ghosting, dose-step price bait-and-switch — is invisible in the store. It holds the billing terms (cause) but not the objection content (effect). The bounded-live layer recovered the effect at minimal cost.

---

## MRL-010 status: does the worked example change it?

**Yes — this crosses the stated hold threshold.** The item's `proposed_next_step` said "hold for a third sighting." Run 011 is the third sighting and the first that actually *used* the missing surface. New datum: bounded-live makes review/forum bodies reachable at ~3-5 credits per read without sprawl, and the ratings-vs-bodies delta is now evidenced (remedymeds 4.6 Excellent → dominant billing-trap cluster, individual accounts of ~$2,400 in charges). Submit to the human steward for a graduation decision; the open question is grain (profile.md pull-quotes vs `signals/<source_type>` vs bounded-live recipe only). **Do not graduate from this review.**

---

## MRL-008: score-vs-body confound flavor

Existing MRL-008 evidence covers external-snippet rigor (002) and captured-signal confounds for Trustpilot trust scores, Wayback tenure, SEC hits (005/006/007). Run 011 adds a new flavor within the Trustpilot family: the store captures the *headline score* (e.g., remedymeds "Excellent 4.7" badge), but score and body are different grains. A score-only read concludes remedymeds (4.6) is near-excellent and hims (3.0) is the trust problem; the bodies show remedymeds' dominant objection cluster is billing-after-cancel, structurally identical to hims'. The score gap reflects invited-review posture, not a real quality gap. Append to MRL-008 evidence log.

---

## State / Signals / Judgments boundary

**Mostly clean, one wobble.** Clean: henrymeds degradation labeled a Signal with a capture-date caveat; billing terms sourced from captured State and matched verbatim against bodies (the objection *is* the published term); score confounds surfaced as integrity context; prevalence not claimed. The wobble (now noted in `read.md`): the Market Pattern "credibility lane is commoditized / post-purchase layer wide open" mixes a State observation with a competitive-positioning Judgment that the 3-brand panel can't fully support. Plausible and useful, but watch-level.

---

## Lenses

**Steward:** Honest about what it has — source grades, capture dates, denominator caveats, snippet-vs-body discipline, absence framing all correct. The verifier's two framing flags were minor and have been tightened. henrymeds degradation correctly flagged as needing primary-source confirmation the run can't provide. Pass.

**Dev Agent:** The bilateral read shape (live bodies + store State rebuttal lookup) is a recipe that could be named without building a surface. Stop-rule operability is proven. The `review_after: 3 bounded-live runs` trigger now earns a lightweight retrospective before the next bounded-live run. No repeated toil needs automation. The "People also looked at" sidebar is a free denominator cross-check that happened ad hoc — if it recurs, a sentence in the denominator convention, not a tool.

**Founder:** 5 credits produced a strategist-ready answer the store could not produce alone, and the store's captured billing terms made the live bodies interpretable at zero extra cost — the bilateral architecture earning its keep. No new schema, monitor, or standing surface added. Budget gate held. `review_after`-3-runs clock at 1/3 — don't graduate after one success.

---

## Recommendation

- **Submit triage candidate (MRL-010):** third sighting + first actual use; submit for human steward graduation decision. Do not graduate here.
- **Append MRL-008 evidence:** review-score / review-body confound flavor.
- **Watch (no triage item):** bilateral read shape as a named recipe; recurrence on a second cohort (e.g., TRT) before adding to QUERYING.
- **Watch (no triage item):** Trustpilot "People also looked at" as a free denominator cross-check; one sighting, hold.
- **Watch (no triage item):** unlabeled positioning Judgment in Market Pattern; consider a read-template note. Not urgent.
- **Watch (no triage item):** review-body→Signals handoff gap (a bounded-live Signal that would change store State has no handoff path); single sighting, hold.
- **Keep observation:** stop-rule qualitative reliance ("clusters were obvious"); works now, watch for ambiguous cases.

## Triage submissions

**MRL-010 — append Evidence Log (3rd sighting + first actual use), submit for graduation decision.**
> 2026-06-19 · 3rd sighting + first actual use (run 011): bounded-live makes review/forum bodies reachable at ~3-5 credits per trust/objection read without sprawl. Prior sightings (008, 009) named the gap store-only; run 011 filled it. The surface is high-signal: objections invisible in scores (remedymeds 4.6 → dominant billing-trap cluster in bodies) are visible in bodies. Concrete delta remains ratings-vs-bodies; the new datum is that bounded-live is the access mechanism and it ran cleanly at plan cost. Crosses the stated hold threshold; submit for human steward graduation decision. Open question is grain: profile.md pull-quotes vs signals/<source_type> vs bounded-live recipe only.

**MRL-008 — append Evidence Log (review-score / review-body confound flavor).**
> 2026-06-19 · Review-score / review-body confound flavor (run 011): the store captures Trustpilot headline scores in Credibility blocks without paid-subscription/invited-review/merged-profile integrity siblings, and without the objection bodies the scores obscure. A score-only read concludes remedymeds (4.6) is near-excellent and hims (3.0) is the trust problem; the bodies show remedymeds' dominant cluster is billing-after-cancel, structurally identical to hims'. The score gap reflects invitation posture, not a quality gap. New flavor within MRL-008's confound family: the headline Signal (score) and the decision-grade Signal (body) are different grains, and the store currently holds only the former.

**Do not graduate, spike, or implement system changes.**
