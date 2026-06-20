# Dynamic workflows — when to ask Claude Code for a harness

*Consult when a task is large, parallel, adversarial, or structured enough that one context window will fumble it. Condensed from Anthropic's "[A harness for every task](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code)" — cut to what helps you decide *when* and *how* to invoke one.*

## What it is

Claude Code writes its own multi-agent harness on the fly — a JavaScript file that spawns and coordinates [subagents](https://code.claude.com/docs/en/sub-agents), each with its own clean context window. It picks the models, decides isolation (worktrees), and can resume if interrupted. You don't write the script; you describe the task and the shape, and Claude builds the orchestration.

## Why bother (the failure modes it fixes)

A single context window planning *and* executing a long task degrades in three specific ways. Workflows beat them structurally by giving each subagent one focused job:

- **Agentic laziness** — quits after partial progress (35 of 50 review items) and calls it done.
- **Self-preferential bias** — trusts its own output when asked to verify or judge it. *A separate agent has no ego in the result.*
- **Goal drift** — original constraints ("don't do X", edge cases) get lost across turns and compaction.

## When to reach for one — and when not

**Reach for it** when the task is long-running, massively parallel, highly structured, or adversarial — and high-value. The tell: it needs *more compute than one window can hold*, or it needs *an independent judge*.

**Skip it** for normal coding. Most tasks don't need a panel of 5 reviewers, and workflows burn significantly more tokens. Ask: does this *really* need more compute?

## How to invoke

- **Just ask** Claude to "use a workflow to…", or say **`ultracode`** to force it.
- **Quick workflows** are fine too — "do a quick adversarial review of this assumption" is a valid one-step harness.
- **Cap the spend:** "use 10k tokens" sets a hard budget.
- **Repeat it:** pair with `/loop` (run on an interval — triage, research) and `/goal` (hard completion bar).
- **Keep it:** press `s` in the workflow menu → saves to `~/.claude/workflows`, or ship it inside a skill (reference the `.js` file from `SKILL.md`; tell Claude to treat it as a *template*, not a verbatim script).

## The patterns (compose these)

Name the pattern in your prompt to steer how Claude builds the harness:

| Pattern | Shape | Use for |
|---|---|---|
| **Fan-out-and-synthesize** | split → agent per piece → merge (barrier) | many small steps, or steps that must not cross-contaminate |
| **Adversarial verification** | each agent's output checked by a separate agent vs. a rubric | anything where being *wrong* is costly; defeats self-bias |
| **Generate-and-filter** | brainstorm many → filter/dedupe/verify → keep the best | ideation where quality > coverage |
| **Tournament** | N agents attempt the *same* task differently → pairwise judge → winner | taste calls (naming, design); sorting big lists by judgment |
| **Classify-and-act** | classifier routes each item to the right agent/model | mixed input; model routing (Sonnet vs. Opus by complexity) |
| **Loop-until-done** | keep spawning until a stop condition (no new findings) | unknown-size work; better than a fixed number of passes |

*Comparative judgment (pairwise) is more reliable than absolute scoring — prefer tournaments over "rate each 1–10" for ranking.*

## Where it shines (beyond code)

The blog's strongest claim: workflows are often *more* useful for non-technical work. Worth remembering these as prompt seeds:

- **Deep research / verification** — fan out sources, adversarially check each claim, synthesize cited (the `/deep-research` skill is this). Or: verify every factual claim in a draft against the codebase.
- **Triage at scale** — classify each item in a backlog, dedupe against what's tracked, act or escalate. *Quarantine pattern:* agents reading untrusted content can't take privileged actions; a separate agent acts.
- **Root-cause / post-mortem** — generate competing hypotheses from *disjoint* evidence (logs vs. files vs. data), each faced by verifiers and refuters. Works for sales ("why did March drop?") and pipelines, not just bugs.
- **Mining your own sessions** — cluster recurring corrections across recent sessions, verify each ("would this rule have prevented a real mistake?"), distill survivors into `CLAUDE.md`.
- **Migrations** — one worktree subagent per callsite/test/module makes the fix, another reviews adversarially, merge. (Bun's Zig→Rust rewrite used this.)

---

*Source: [Anthropic — A harness for every task: dynamic workflows in Claude Code](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code) (Jun 2026). Trimmed to the decision (when/why) and the pattern vocabulary; the JS API surface and the full use-case gallery live in the [workflows docs](https://code.claude.com/docs/en/workflows).*
