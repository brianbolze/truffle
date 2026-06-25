---
date: 2026-06-24
run: changes/2026-06-24-neighbor-discovery
kind: friction
---

**Saw.** Reviewing a `medium`-risk proposal whose whole job is to drive a paid, per-query metered API (`exa_search.py`, billed per call × `numResults`), the `spend_stop` cap was "a handful of queries per invocation, opt-in, no standing run" — honest as posture but with no number anywhere (no query count, no `num_results` ceiling), while the playbook also said to "vary the description across 2-3 angles," so realized spend is (angles × num_results) and unbounded by the written cap. The `acceptance_checks` asked me to confirm "the spend posture is stated" — which it is — but I couldn't check spend against any number, so "stated" and "checkable" came apart at exactly the field meant to bound money.

**Not claiming.** Not claiming every spend_stop needs a number — lead-context explicitly says "spend_stop is posture, not accounting ceremony," and `none`/`unknown` are valid. One sighting on one paid-API packet. The urge I'm resisting: adding a rule that paid-API packets must carry a numeric ceiling. Pressure noted, not patched.
