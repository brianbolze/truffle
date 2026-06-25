---
date: 2026-06-24
run: agent-build packet 2026-06-24-neighbor-discovery (/discover-neighbors verb)
kind: risk-miss
---

**Saw.** The `/discover-neighbors` proposal's `acceptance_checks` validated the artifact's **shape** — spend cap present, `write_scope` held, links referenced-not-paraphrased, `querycheck --strict` passes — but never its **core value**: whether the verb actually surfaces the right companies. Both the independent proposal-mode review and the change-mode gate passed it on those shape checks. Only a post-merge live test (run at Brian's prompting) exposed the failure: exa `/search` found **5 of 32 obvious players** in a cohort Brian knows cold (docs/PM software), and had already silently missed the category-definers in telehealth (hone/ro/hims). The disconfirming test was ~10 minutes and trivially available before merge. **Compounding:** a `2026-06-20-cohort-discovery` bake-off already existed and had ranked discovery feeders by recall (websearch 0.69 > listicle 0.34 > llm 0.24 > store 0.24 > demand 0.21; exa /findSimilar **FAILED to run**), shipped a `cohort-discovery.workflow.js`, and explicitly queued a "SaaS sub-cohort re-run" as the generalizability fast-follow — none of it was read before building the verb on exa alone.

**Not claiming.** Not asserting the fix (a mandatory recall-gate in `acceptance_checks`, a prior-art-search step in `agent-build-propose`, a "test the value claim on a known set" review discipline) — only that the propose → proposal-review → change-mode chain certified a value claim that **no check in the chain tested**, while both the cheap disconfirming test and directly-relevant prior evidence were available the whole time.
