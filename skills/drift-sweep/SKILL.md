---
name: drift-sweep
description: >
  Catch drift after a change to the web-research engine. Run it once you've edited a contract, script,
  or doc and want to know what went stale: the deterministic gate (linters + tests + checks) first, then
  a quick doc-staleness pass scoped to what changed. Trigger on "/drift-sweep", "sweep for drift", "check
  the repo for staleness", "did my change break any pointers/docs", "drift check after my edits". An
  explicit maintenance verb for THIS engine — not for capturing or querying companies, and it never
  auto-fixes (it proposes). Use after engine edits; skip for company captures/queries.
---

# drift-sweep — catch drift after an engine change

Run after editing the engine (a contract, a script, a doc) to catch drift before it ships: deterministic
checks first (cheap, every time), then a quick doc-staleness pass over **only what changed**. It **proposes**
fixes — never auto-applies them. Keep the whole thing bounded and cheap; a tiny change needs only the gate.

## 1. Run the gate — deterministic, the cheap pass

From the repo root, run the gate block in [`MAINTAINING.md`](../../documentation/MAINTAINING.md) (the "run the gate"
section). Each non-zero exit is drift — note which check failed and why. The command list lives in
MAINTAINING.md, not here, so the two can't fork. A visualcheck/clock-skew failure on a company you didn't
touch is pre-existing, not your change — say so, don't fix it.

## 2. Doc-staleness pass — the LLM part, bounded by the diff

**Scope:** default to the working-tree diff (`git status` + `git diff`; fall back to the last commit if the
tree is clean). Sweep only docs touched by — or downstream of — the change. A *full* sweep (every contract +
root doc) only when asked.

- **Small change (a few files):** read them inline, no sub-agents.
- **Broad change:** fan out a few **Sonnet** sub-agents (this is mechanical reading — use the cheap model),
  one per doc area (contracts / skills / tools / _design).

Look for drift only — a short, generic list (don't enumerate every doc; the *method* shouldn't need upkeep):

- a **pointer that moved** — a path, filename, function, or `file:line` that no longer exists or now points
  wrong;
- a **broken cross-doc link**, or a doc that restates another's rule and now **contradicts** it;
- a **baked count / inventory** ("N tools", example lists) that no longer matches reality;
- for each contract the diff touched, walk its row in [`MAINTAINING.md`](../../documentation/MAINTAINING.md) and confirm the
  listed **downstreams actually moved**.

## 3. Report — propose, don't write

One tight digest:

- **Clean** — what passed (a wall of green is one line).
- **Drifted** — each finding as `file:line → what's stale → proposed fix`.
- **Needs a human call** — anything ambiguous (a judgment, a migrate-vs-grandfather decision).

Apply fixes only if the user says go. This skill spends nothing but Claude reasoning — no captures, no credits.
