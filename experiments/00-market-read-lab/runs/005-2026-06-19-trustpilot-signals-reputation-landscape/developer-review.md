# Developer Review

Question: **What Truffle system behavior does this run pressure?**

Headline: this is the **first market read to consume the Signals layer** (Runs 000–004 were all
State reads). The good news for the system: a captured Trustpilot signal was query-ready straight
off disk, the per-domain signal path worked cleanly, and the read needed **no new primitive**. The
one real pressure is interpretive, not structural — a consumed reputation Signal carries built-in
confounds that must travel with it.

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Capture** | Trustpilot capture already records the load-bearing confounds (`paid_profile`, `asks_for_reviews`, `claimed`, volume, distribution). Capture grain is *right*. | None — capture is sufficient. Note the win. |
| **Structure** | Reputation is a clean Signal (the score) + a downstream Judgment ("who's trusted"). The read kept them separate. No new State/Signals object needed. | None — confirms the State/Signals/Judgment split holds for sentiment. |
| **Query / access** | Had to hand-roll "latest-`*.json`-per-signal-dir + extract fields." Same in-run query improvisation as the State reads, now at the Signals grain. **First sighting at this grain.** | Watch. If a 2nd signals-read repeats it, a tiny QUERYING "read latest signal per domain" recipe is earned. Not yet. |
| **Freshness / automation** | 2–3 captures already exist per brand but no read diffs them — a trajectory is one step away and unused. | Note as next-run advice (store-only trend diff). No build. |
| **Synthesis** | A consumed reputation Signal will mislead if the score is reported without its confounds + volume. The read path doesn't force them to travel together. | Pattern-level convention candidate (MRL-008 sibling). Watch for recurrence. |
| **Guardrails** | Run stayed store-only, no spend, no re-capture, fail-closed gates all passed. | None. |

## Lenses

**Steward — is the system still honest?** Yes, and notably so: the read refused to turn a payable,
solicited score into a quality verdict, labeled the Judgment, and kept absence as "not captured."
The honesty risk is entirely downstream — a consumer who reads `trust_score: 4.8` from the JSON
without the sibling flags. The provenance is intact; the *interpretation* is the fragile part.

**Dev Agent — can repeated toil be removed?** Not yet. The latest-per-dir + field-extract loop is
mild toil and this is its first appearance at the Signals grain. A grep-verifiable QUERYING recipe
("latest signal per domain, with the confound fields named") would remove it — but one sighting is
a watch, not a build. Prefer documenting the confound-travels-with-score rule over writing code.

**Founder — does it compound the asset while staying light?** Yes. It proved the Signals
investment pays off at read time with zero re-capture, and it did so without adding ontology
gravity (no reputation object, no score normalization, no served surface). The cheapest compounding
move is a documented rule, not infrastructure — squarely on the anti-Doro line.

## Recommendation

- **No-op / keep as observation:** capture grain is sufficient; State/Signals/Judgment split holds
  for sentiment; per-domain signal path worked (gives MRL-007 a clean *negative* data point — no
  homeless category signal here).
- **Watch for recurrence:** (1) the hand-rolled latest-signal-per-dir query loop at the Signals
  grain; (2) the confound-must-travel-with-score interpretation rule.
- **Submit triage candidate:** append a first-sighting evidence note to **MRL-008** generalizing it
  from external-monitoring rigor to *captured-signal interpretation* rigor. Pattern-level, watch
  for recurrence, no build.

## Triage submissions

- **MRL-008 — append Evidence Log (first Signals-consumption sighting).** Extends MRL-008's "source
  rigor" beyond external/snippet monitoring to consuming a *captured* reputation Signal: the score
  conflates regard with solicitation posture, so `profile_flags` + `review_count` must be reported
  with any `trust_score`, and "trusted/distrusted" stays a labeled, volume-weighted Judgment.
  Candidate is a documented rule, not a monitor or helper. First sighting at this grain — watch.

**Do not graduate, spike, or implement system changes.**
