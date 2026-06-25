# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable? Yes** — and notably, the value lands on a genuine end-reader (the cold-starter), breaking the long 038/039/041/047/048/049/050 "value lands on the builder, not the buyer" streak. This is the second consecutive register after 043/044 where a real consumer (not just the Steward) gets the payload.
- **Why:** the run answers a question every Truffle consumer actually has — "can I trust a profile I've never seen to brief me in 60 seconds?" — and the answer is a calibrated *yes, with two named caveats*. That is directly actionable for anyone deciding whether to lean on a cold profile.
- **Where Truffle added value:** the per-company profile is a strong cold-start instrument — uniform 9-section skeleton + uniform trust surface (`unverified_fields`/`site_notes`/`STRAIN`) across wildly different entities (an asset manager, a nuclear-plant developer, a luxury watchmaker). The `Strategic read` section gives a real "so what" synthesis, not just facts (e.g. alange "the whole site is engineered to *not* sell online"; eightsleep "deliberate march from hardware to recurring health platform").
- **Where Truffle added little or fell short:** for the fast-read consumer who scans *frontmatter only*, `business_model` is a trap on non-standard monetizers (blueowl `Other`, eightsleep `Subscription`, blueenergy `Usage-based`). And the "what to distrust" protection, though present 6/6, sits in a block the reader must choose to read — not forced onto the path.
- **What the consumer can do now:** trust a cold profile's *what/who-for/what-to-distrust* on sight; but read the `How it works/model` prose (not the `business_model` field) for monetization, and always read `unverified_fields` before quoting a number.
- **What made it safer / better than generic Claude + web search:** generic web search has no uniform trust surface — it can't tell you *what to distrust* about a company in a structured, dated, self-flagged way. The profile's `unverified_fields` is exactly the ingredient a web search won't volunteer.
- **Biggest limit:** n=6 of 136, telehealth under-sampled by design; no fluent-but-unflagged profile appeared, so the false-completeness trap is "not found," not "not there."
- **Human follow-up needed:** none required; a telehealth-weighted re-draw would harden S1 and hunt the missing false-completeness case (see run-notes Next-run advice).

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Clear answer, decision aid, or next step. | Yes — a usable rule for cold readers: trust 3 of the 4 questions on sight; read prose for monetization; read `unverified_fields` before quoting. |
| **Judgment-ready** | Fresh, rare, cited ingredients. | The cold-start verdict is the run's own Judgment (CR1); the underlying State (skeleton, fields, flags) is cited per-company to file:line. |
| **Sourced & cited** | Claims trace to dated captures / files. | Strong — every claim ties to a profile file:line; sample rule + counts in receipt C1; an independent verifier confirmed 4/5 claims and corrected the 5th (VR1). |
| **Deep enough** | Covers the intended set. | Adequate for a calibration (6 spanning slots); explicitly a sample, telehealth under-weighted by design. |
| **Fresh enough** | Capture dates / staleness visible. | Yes — vintage spread (05-30→06-24) is part of the test; point-in-time prices flagged in each profile's own `unverified_fields`. |
| **Kept / reusable** | Warm files for the next ask. | Reproducible sample rule (C1) makes a re-draw cheap; the cold-start question/answer is reusable as a store-health check. |
| **Shortfall mapped** | Names where Truffle could not support. | Yes — the `business_model` fast-read trap and the `unverified_fields` salience dependence are named with evidence. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Cold-start a company** | **Directly — this is the run.** Trustworthy cited cold profile confirmed for 6/6 on what/who-for/what-to-distrust; monetization via prose. | Hunt a fluent-but-unflagged profile (none in sample) to test the false-completeness edge. |
| **Make AI safe to delegate to** | Partly — a delegated agent reading frontmatter-only would mis-read `business_model` on non-standard monetizers; the prose is the safe surface. | A *filtering* agent would need run-037 W1's ranked multi-select `business_model`; the human reader needs nothing. |
| **Five-second brief input** | Adjacent — the `Strategic read` is brief-ready, but salience of `unverified_fields` is the open risk on the rendered surface (run-049). | Cold-start-on-the-rendered-brief read would join the threads. |

## Lens check

- **Strategist:** lands plainly — "the profile is a good cold-start instrument; trust 3 of 4 questions on sight, read prose for the 4th, always read the distrust block." Novel because no prior run read the cold-start job head-on.
- **The Pantry / downstream system:** the *State* (uniform skeleton, fields, flags) is high-quality reusable ingredient; the *cold-start verdict* is the run's labeled Judgment (map, not a queryable ingredient — the recurring CR1 frontier), but here the map is genuinely consumer-facing.
- **First Contact:** yes — a new reader would trust the run: it samples reproducibly, caveats its n, and an independent verifier corrected its one overreach (the "identical"→"same" header fix).

## Raw learning to preserve

Run-notes Observations S1–S4, G1 carry the value-side learning. Consumer-review-specific sighting to lift: **CR1** (value lands on a real end-reader, breaking the builder-not-buyer streak — the cold-start job is one the store *serves well*, the inverse of the usual "store falls short for the buyer" finding).

**No lessons proposed, nothing graduated, no system change implemented.**
