---
date: 2026-06-24
run: changes/2026-06-24-capture-parser-fixtures
kind: surprise
---

**Saw.** Framing the parser-fixture packet, I traced the "silent-misroute" edge: `signal_delta.py` routes on the literal envelope `tool` string — `DISPATCH.get(src, branch_fallback)` (`signal_delta.py:641`) and `subject_of()` switching on `env.get("tool")` (`signal_delta.py:82`). The same canonical name is also asserted by `signals.py`'s `TOOL_SPEC` and emitted independently by each of ~8 capture tools. Nothing binds these three to one source of truth, and a divergence (a renamed or hand-built envelope) doesn't error — it falls through to `branch_fallback`, a named veto, so a real source quietly reads as "undiffable" instead of being diffed.

**Not claiming.** Not claiming this has bitten a real run, and not claiming the packet's dispatch-tie test is insufficient — it pins the case in scope. Only noting that the underlying binding is convention spread across ~8 files with no shared registry. The urge I'm resisting: extract a single `TOOL_NAMES` constant and key DISPATCH/TOOL_SPEC off it — a production change, out of scope for a tests-only packet.
