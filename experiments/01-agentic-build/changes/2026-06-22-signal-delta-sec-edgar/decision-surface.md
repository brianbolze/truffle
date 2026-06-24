# Decision surface: signal_delta SEC EDGAR branch

**Problem.** `signal_delta.py` (the local Signals comparator) had no branch for `sec_edgar`, so repeat SEC captures fell through to a veto instead of showing what new dated filing/Form-D events became visible since last capture. A free capital-signal source couldn't answer "what changed?" — a named Market Read Lab gap.

**What changed.** A source-local `sec_edgar` branch: compares two existing SEC envelopes by issuer State fields and dated EDGAR event cards. Amount-free, verdict-free, no scores, no live fetches, no persistence/schema changes, no cross-source reconciliation. Docs updated (`QUERYING.md`, `SIGNALS.md`, `tools/signal_delta.md`, two BACKLOG files, MRL notes).

**Risk: medium.** Driver is the committed-tool contract — future agents may trust this delta, so a sloppy capital-signal read creates false confidence. Stays clear of `high`: no persistence, schema, write authority, or paid capture.

**Checks.** `pytest tests/test_signal_delta.py` → 23 passed (re-run, confirmed). `py_compile` + `git diff --check` pass. Ruff not run (not installed). Independent **proposal-mode** review exists and leans **accept (sound decision)**. No independent **change-mode** review of the actual diff/tests has been done.

**Decision needed.** Implemented + reviewed → **merge** or **hold-after-review**.

**Surprise worth flagging — one real, untested risk.** The reviewer's one substantive carry-forward is unresolved, and I confirmed it in the code: the event key includes `citation` (`SEC_EVENT_FIELDS`, line 424), so a re-parsed card whose citation/flag changes — same underlying event — surfaces as "newly visible / no longer visible," i.e. churn dressed as movement. No fixture pins this case. That's exactly the false confidence the packet's own risk note warns against, in a `medium`-risk committed tool. Everything else (no-amount/no-score boundary, identity caveats, capped-window wording) is pinned and solid.

---

## Recommendation — *Brian decides*

**hold-after-review** until one `change`-mode pass either confirms event-key stability is acceptable or adds a fixture proving a re-parsed card doesn't masquerade as movement. The branch is otherwise right-sized and boundary-clean; this is the single load-bearing correctness gap, it's cheap to close (one test + possibly dropping `citation` from the key), and merging without it ships the exact failure mode the tool exists to prevent. If you read the re-parse risk as low-frequency and tolerable for v0, **merge** is defensible — but flag the gap on the MRL ticket so it isn't silently trusted.
