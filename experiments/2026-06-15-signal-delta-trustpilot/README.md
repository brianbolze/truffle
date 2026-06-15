# Probe #1 — signal_delta de-risk

**Gates:** `tools/signal_delta.py` (the envelope comparator). Per the [traction approach](../../_design/2026-06-15-traction-approach.md), no comparator code lands until this reads clean.

**Hypothesis.** The comparator can diff raw tool envelopes into axis-specific deltas + comparability vetoes — *without* a normalized card layer — and the two vetoes the adversarial pass flagged (SERP AIO batch-outage; Trustpilot rolling-vs-cumulative) can be made to fire on the *documented* failure signatures, not just total outages.

**Method (~$0 — cached data + fixtures, no API spend).**
- **SERP** — real cached captures of the same 4 telehealth queries 3 days apart (`../2026-06-08-serp-intent-telehealth-smoke/captures/` → `../2026-06-11-serp-intent-telehealth-repeat/captures/`). The Jun 11 set already carries a real 1/4 AIO drop (TRT) — the *negative* case. The *positive* case is constructed by blanking AIO on 3/4 of the real Jun 8 set.
- **Trustpilot** — faithful hand-built fixtures (`fixtures/trustpilot/`) modelled exactly on `tools/trustpilot.py`'s envelope: a clean velocity pair (with the rolling-window trap baked in), a removed profile, and a templated/farmed profile. No Firecrawl spend; the comparator reads envelope fields, indifferent to who produced them.
- **Round-trip** — persist D0 + D7 to the `store/<domain>/signals/<source_type>/<captured_at>.json` convention (rooted at gitignored `_out/`), then *discover by glob + read back* to diff — exercising "where did D0 go," not two files handed over in one session.

**Run:** `python3 probe.py` (prints each case + a 9-check verdict; exit 0 = all pass).

**Result:** all pass — see [`FINDINGS.md`](FINDINGS.md).
