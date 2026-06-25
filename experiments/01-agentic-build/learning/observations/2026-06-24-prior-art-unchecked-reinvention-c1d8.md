---
date: 2026-06-24
run: agent-build packet 2026-06-24-neighbor-discovery (/discover-neighbors verb)
kind: friction
---

**Saw.** I built a `/discover-neighbors` discovery verb without checking whether the problem had been worked before — it had, thoroughly. A `2026-06-20-cohort-discovery` experiment already framed the identical problem ("who is even in this market? store-first, in-store vs net-new"), raced six discovery feeders in a bake-off (`FINDINGS.md`), shipped a `cohort-discovery.workflow.js`, and mapped to the same "Discovery tools / Coverage" roadmap row. The `agent-build-propose` flow's "Required Context" is packet-local (read the README, the seed proposal, the template) and includes no step like "search `experiments/`, `experiments/_archive/`, and `_design/` for prior work on this problem before proposing." So a whole validated experiment sat unread while I reinvented a worse version of it (and only found it when Brian asked "did you even check").

**Not claiming.** Not asserting the fix (a prior-art-search step in propose, a lead-context discipline, or an experiments index) — only that nothing in the propose→build chain surfaced directly-relevant existing experiments, and the cost was a duplicated, inferior build.
