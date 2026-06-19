# Market Read Lab Loop and Routine Research & Decision Memo

## 30-second answer

Market Read Lab should use a v0/v1 autonomy posture of **local, staged, fail-closed runs**: keep Scout, Read, Review, and Triage as separate stages; persist each run as files; advance stages only when `run_status` exactly matches the expected prior state; allow only planned `bounded-live` source panels, and require human approval before broad live browsing, unplanned paid capture, risky current-event claims, or write-back into shared State. For local automation, the best next design is a local scheduled chain that invokes fresh-stage sessions and uses file handoffs, because Claude `-p` plus system cron has fresh context, local file access, and scriptable exit behavior, while Claude Desktop Scheduled Tasks and Codex Automations are useful alternatives but depend on the app and machine being awake ([Claude Code Headless Docs](https://code.claude.com/docs/en/headless), [Claude Code Desktop Scheduled Tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks), [Codex Automations](https://developers.openai.com/codex/app/automations)).

Adopt deterministic verification before adding more autonomy: a source-rigor checklist, no-snippets-as-evidence check, receipt completeness check, current-claim volatility flag, `run_status` idempotency check, triage duplicate check, no-auto-graduation check, and spend/live-browse approval gate. Use an LLM reviewer only as an advisor for structural critique and rubric adherence, not as the final authority on factual accuracy, because LLM judges degrade when evaluating questions they cannot answer correctly and need human or external grounding for hard factual checks ([No Free Labels](https://arxiv.org/html/2503.05061v1), [LLMs-as-Judges Survey](https://arxiv.org/html/2412.05579v2)).

Avoid cloud-first Routines as the primary Market Read Lab runner, single long-running sessions, self-mutating ontologies, category objects, graph/relationship registries, always-on monitors, and broad LLM-judge infrastructure. Claude Routines are strong for cloud-native repo workflows but cannot access local files natively, while `/loop` is session-scoped and accumulates context, which cuts against Market Read Lab’s local-first and fresh-stage design ([Claude Code Routines Docs](https://code.claude.com/docs/en/routines), [Claude Code Scheduled Tasks Docs](https://code.claude.com/docs/en/scheduled-tasks)).

The biggest unknowns are operational rather than conceptual: whether Codex missed-run catchup is officially guaranteed, whether Codex cloud triggers are generally available, exact account-specific Claude Routine caps, and how reliably local scheduled runs execute on Brian’s actual machine without sleep/app-state misses ([Codex Automations](https://developers.openai.com/codex/app/automations), [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/), [Claude Code Routines Docs](https://code.claude.com/docs/en/routines)).

## 2026-06-19 operational update

The first local Claude Routine dry run showed a hard product constraint: `update_scheduled_task`
requires explicit approval even in Auto mode. That means a Scout task cannot reliably arm Loop 1,
and Loop 1 cannot reliably arm Loop 2, without Brian approving each handoff.

This does **not** invalidate the stage contract. It only invalidates self-arming scheduled tasks
as the unattended runner. The next recommended shape is a **single local Claude Routine** with a
tiny scheduler prompt that delegates to the repo skill and runs the full cycle inside one session:
Scout, gated Read, gated Review, then stop. The routine can still use subagents for fresh-lens
review, but stage rules, permissions, and artifact contracts should live in the repo.

Fallback if the single routine proves too slow: fixed staggered schedules where each stage scans
for the next eligible run by `run_status`. Avoid a self-mutating task chain unless the product
approval behavior changes.

## 2026-06-19 bounded-live update

The active contract now permits `evidence_mode: bounded-live` for autonomous Market
Read Lab runs when Scout provides a filled `live_evidence_plan`. This narrows the memo's
original "human approval before live browsing / paid capture" rule: broad or unplanned
live work still fails closed, but a light planned source panel may run unattended with
source-family bounds, stop rules, receipts, `live_evidence_used`, and spend notes.

## Recommendation

Market Read Lab should move next to **v1 local scheduled stages with verification gates**, not to a supervisor platform. The design should preserve the current Scout to Read to Review to Triage loop, add `run_status` as the stage lock, add `needs-human-review` as the fail-closed state, and introduce a lightweight receipt template plus verification checklist. This is the smallest design that preserves learning while making repeated autonomous runs safer.

The runner should be local and boring. Prefer `claude -p` stages driven by OS scheduling where available, because each stage starts fresh by default, can read and write local files, can be constrained by allowed tools and permission modes, and can fail with a process exit that a wrapper can treat as a hard stop ([Claude Code Headless Docs](https://code.claude.com/docs/en/headless), [Claude Code Permission Modes](https://code.claude.com/docs/en/permission-modes)). Claude Desktop Scheduled Tasks are a good lower-friction alternative for weekly Scout or single-stage runs because they create fresh sessions with local file access, but they require the machine and Desktop app to be running and only perform one catch-up run for the most recent missed time in the last seven days ([Claude Code Desktop Scheduled Tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)). Codex Automations are plausible for a Codex-centered workflow, but the official docs require the local Codex app to be running, the machine to be powered on, and the selected project to remain available on disk at schedule time, so they should not be treated as reliable cloud routines unless those constraints are acceptable ([Codex Automations](https://developers.openai.com/codex/app/automations)).

The verification layer should be deterministic first and LLM-assisted second. Programmatic or checklist-style gates should decide whether an artifact is complete enough to advance, while an LLM reviewer can comment on whether the read is useful, whether the evidence is overclaimed, and whether the triage item is duplicative. Anthropic’s evaluator-optimizer pattern is useful only when clear criteria already exist, and contract-first design argues that model output should remain untrusted until it passes an explicit acceptance layer ([Building Effective Agents](https://www.anthropic.com/research/building-effective-agents), [AI Orchestration Reliability](https://brendan-davies.dev/ai-orchestration-reliability.html)).

Do not add a standing overwatch agent yet. Add the smallest useful “advisor” pass after Loop 1 only: it reads `read.md`, `run-notes.md`, and `receipts/`; fills a verification checklist; may set `run_status: needs-human-review`; may block Review if evidence is incomplete; and may only comment on system design pressure rather than approving engine changes. A full supervisor architecture becomes justified only after repeated runs show specialist-agent overload, tool-choice confusion, or reviewer fatigue at scale, which is the problem supervisor patterns are meant to solve ([Databricks Supervisor Agent Architecture](https://www.databricks.com/blog/multi-agent-supervisor-architecture-orchestrating-enterprise-ai-scale), [OpenAI Agent Orchestration](https://openai.github.io/openai-agents-python/multi_agent/)).

## Source map

| Source | URL | Type | Date accessed | Claim it supports | Confidence |
|---|---|---:|---:|---|---|
| Claude Code Scheduled Tasks Docs | [code.claude.com/docs/en/scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks) | official | 2026-06-19 | `/loop` is in-session scheduling with local context, session dependency, jitter, and limited recovery. | High |
| Claude Code Desktop Scheduled Tasks | [code.claude.com/docs/en/desktop-scheduled-tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks) | official | 2026-06-19 | Desktop scheduled tasks run fresh local sessions, have local file access, configurable permissions, and machine/app-awake constraints. | High |
| Claude Code Routines Docs | [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) | official | 2026-06-19 | Routines are cloud-hosted, machine-independent, support schedule/API/GitHub triggers, but cannot access local files natively. | High |
| Claude Code Headless Docs | [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) | official | 2026-06-19 | `claude -p` supports non-interactive local execution, local file access, structured outputs, fresh sessions, and scripted stage chaining. | High |
| Claude Code Permission Modes | [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) | official | 2026-06-19 | Permission modes such as `default`, `acceptEdits`, `auto`, `dontAsk`, and `bypassPermissions` define unattended behavior and safety limits. | High |
| Claude Code Memory Docs | [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) | official | 2026-06-19 | CLAUDE.md, MEMORY.md, and local output files are the cross-session persistence primitives. | High |
| Claude Code Changelog | [code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog) | official release notes | 2026-06-19 | Confirms relevant Claude Code feature timing, including `/loop` and `/schedule` availability. | High |
| Long-running Claude | [Anthropic Research](https://www.anthropic.com/research/long-running-Claude) | official lab article | 2026-06-19 | Supports the pattern of persistent project instructions, progress logs, and recoverable work units for long-running work. | High |
| Claude Code Auto Mode | [Anthropic Engineering](https://www.anthropic.com/engineering/claude-code-auto-mode) | official engineering post | 2026-06-19 | Classifier-based permissions reduce prompts but can block or abort unattended work after repeated classifier blocks. | High |
| Codex Automations | [OpenAI Developers](https://developers.openai.com/codex/app/automations) | official | 2026-06-19 | Codex supports standalone and thread automations, but local project automations require the machine/app/project to be available at run time. | High |
| Codex Sandboxing | [OpenAI Developers](https://developers.openai.com/codex/concepts/sandboxing) | official | 2026-06-19 | Codex sandbox modes constrain file writes, network, external apps, and automation risk. | High |
| Codex Features | [OpenAI Developers](https://developers.openai.com/codex/app/features) | official | 2026-06-19 | Codex app settings and automation behavior include machine-local constraints and feature surfaces. | High |
| Codex Changelog | [OpenAI Developers](https://developers.openai.com/codex/changelog) | official release notes | 2026-06-19 | Confirms June 2026 automation fixes and feature maturity around thread automations and approval-mode behavior. | High |
| Introducing the Codex app | [OpenAI](https://openai.com/index/introducing-the-codex-app/) | official blog | 2026-06-19 | Cloud-based triggers were announced as a roadmap item, not confirmed as shipped by the fetched official docs. | Medium |
| Codex for almost everything | [OpenAI](https://openai.com/index/codex-for-almost-everything/) | official blog | 2026-06-19 | Codex can schedule future work for itself and thread automations preserve context across scheduled wakes. | High |
| Run long horizon tasks with Codex | [OpenAI Developers](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex) | official blog | 2026-06-19 | Codex’s internal loop is plan, edit, run tools, observe, repair, update, and repeat. | High |
| GPT-5.2-Codex System Card Addendum | [OpenAI PDF](https://cdn.openai.com/pdf/ac7c37ae-7f4c-4442-b741-2eabdeaf77e0/oai_5_2_Codex.pdf) | official safety card | 2026-06-19 | Documents the risk that simple commands can mask destructive actions in unattended full-access automation. | High |
| Building Effective Agents | [Anthropic](https://www.anthropic.com/research/building-effective-agents) | official lab post | 2026-06-19 | Defines evaluator-optimizer, orchestrator-workers, and programmatic gate patterns. | High |
| LLM Powered Autonomous Agents | [Lilian Weng](https://lilianweng.github.io/posts/2023-06-23-agent/) | reputable commentary | 2026-06-19 | Summarizes ReAct, Reflexion, critique loops, and the limits of self-reflection. | High |
| No Free Labels | [arXiv](https://arxiv.org/html/2503.05061v1) | academic preprint | 2026-06-19 | LLM-as-judge performance depends on whether the judge can answer the question and improves with human-written references. | High |
| LLMs-as-Judges Survey | [arXiv](https://arxiv.org/html/2412.05579v2) | academic survey | 2026-06-19 | Summarizes presentation, social, verbosity, self-enhancement, and domain-limit biases in LLM judges. | High |
| AI Orchestration Reliability | [Brendan Davies](https://brendan-davies.dev/ai-orchestration-reliability.html) | reputable practitioner | 2026-06-19 | Contract-first design and deterministic acceptance layers reduce automation corruption. | Moderate-high |
| Good Agent Tools Fail Closed | [Roger Chappel](https://rogerchappel.com/blog/fail-closed-agent-tools/) | reputable practitioner | 2026-06-19 | Agent tools should stop with structured errors when preconditions fail rather than guessing. | High |
| OpenAI New Tools for Building Agents | [OpenAI](https://openai.com/index/new-tools-for-building-agents/) | official product announcement | 2026-06-19 | Guardrails and human oversight are first-class primitives for sensitive agent actions. | High |
| LangGraph | [LangChain](https://www.langchain.com/langgraph) | official framework docs | 2026-06-19 | Stateful graph workflows, interrupts, and HITL gates are common orchestration patterns. | High |
| OpenAI Agent Orchestration | [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/multi_agent/) | official framework docs | 2026-06-19 | Distinguishes LLM-driven and code-driven multi-agent orchestration and handoffs. | High |
| Auditable AI Agent Loop | [arXiv](https://arxiv.org/html/2603.17381v3) | academic working paper | 2026-06-19 | Run ledgers, immutable evaluators, editable surfaces, and audit logs improve transparency in research loops. | High |
| Ledger-Verified Run Certificates | [arXiv](https://arxiv.org/html/2509.10550v1) | academic paper | 2026-06-19 | Provides a more formal argument for replayable ledgers, though practical use is heavier than Market Read Lab needs now. | Moderate |
| Databricks Supervisor Agent Architecture | [Databricks](https://www.databricks.com/blog/multi-agent-supervisor-architecture-orchestrating-enterprise-ai-scale) | official technical blog | 2026-06-19 | Supervisor architectures help when tool choice, context size, and specialist delegation overwhelm a single agent. | High |
| Auditing and Logging AI Agent Activity | [LoginRadius Engineering](https://www.loginradius.com/blog/engineering/auditing-and-logging-ai-agent-activity) | engineering blog | 2026-06-19 | Watchdogs should monitor iteration count, cost, tool calls, schema validation rates, and error distributions. | Moderate |
| What Is Loop Engineering? | [MindStudio](https://www.mindstudio.ai/blog/what-is-loop-engineering-ai-coding-agents) | weak-to-moderate practitioner lead | 2026-06-19 | Provides the term definition, but the source is commercial and the term is not a formal academic category. | Moderate |
| Deterministic AI and Guardrails | [Zingtree](https://zingtree.com/blog/the-authoritative-guide-to-deterministic-ai-and-guardrails-for-auditable-workflows) | weak lead | 2026-06-19 | Identified as a lead for deterministic guardrails but not used as evidence. | Low |
| Andrej Karpathy Software 3.0 | [YouTube](https://www.youtube.com/watch?v=96jN2OCOfLs) | contextual weak lead | 2026-06-19 | Relevant only as broad background; no fetched text source supported specific design claims. | Low |

## Capability matrix

| Surface or pattern | Can run unattended? | Local file/store access? | Fresh context per stage? | Can chain stages? | Can self-reschedule? | Permission behavior | Good fit for Market Read Lab? | Main failure mode |
|---|---|---|---|---|---|---|---|---|
| Claude `/loop` | Partial, because it runs inside an active CLI session and depends on that session remaining available ([Claude Code Scheduled Tasks Docs](https://code.claude.com/docs/en/scheduled-tasks)). | Yes, because it uses the local working directory and configured session tools ([Claude Code Scheduled Tasks Docs](https://code.claude.com/docs/en/scheduled-tasks)). | No, because iterations append to the same session context ([Claude Code Scheduled Tasks Docs](https://code.claude.com/docs/en/scheduled-tasks)). | Yes for simple repeated turns, but not as a clean stage DAG ([Claude Code Scheduled Tasks Docs](https://code.claude.com/docs/en/scheduled-tasks)). | Partially, because Claude can create or delete cron tasks, but this is still session-scoped ([Claude Code Scheduled Tasks Docs](https://code.claude.com/docs/en/scheduled-tasks)). | Governed by the active permission mode, so unattended use can stall or abort if tools are not approved ([Claude Code Permission Modes](https://code.claude.com/docs/en/permission-modes)). | Poor as the primary runner; acceptable for short polling or “keep checking until done.” | Context accumulation, session death, no clean missed-run recovery. |
| Claude Desktop Scheduled Tasks | Yes if the machine is awake and the Desktop app is running ([Claude Code Desktop Scheduled Tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)). | Yes, with the configured local working folder ([Claude Code Desktop Scheduled Tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)). | Yes, each scheduled task runs a fresh session ([Claude Code Desktop Scheduled Tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)). | Yes by file handoff and separate tasks, not by a native DAG ([Claude Code Desktop Scheduled Tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)). | Yes via `update_scheduled_task` MCP from within a session ([Claude Code Desktop Scheduled Tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)). | Configurable per task, with best practice to pre-approve required tools ([Claude Code Desktop Scheduled Tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)). | Good for v1 weekly Scout and simple local runs. | Machine/app sleep or closure skips runs, and older missed runs are discarded. |
| Claude Routines and `/schedule` | Yes, because Routines run in Anthropic-managed cloud infrastructure ([Claude Code Routines Docs](https://code.claude.com/docs/en/routines)). | No local store access, because Routines clone GitHub repos fresh and do not access the local filesystem ([Claude Code Routines Docs](https://code.claude.com/docs/en/routines)). | Yes, each run is a fresh cloud session ([Claude Code Routines Docs](https://code.claude.com/docs/en/routines)). | Yes via repo commits, PRs, API triggers, or scheduled triggers, but not via local file handoff ([Claude Code Routines Docs](https://code.claude.com/docs/en/routines)). | Not a good fit for self-mutating local schedules; API `/fire` exists but is experimental ([Claude Code Routines Docs](https://code.claude.com/docs/en/routines)). | No in-run permission prompts; the routine runs autonomously once configured ([Claude Code Routines Docs](https://code.claude.com/docs/en/routines)). | Poor as primary Market Read Lab runner because Truffle is local-first. | Looks reliable but cannot see the local store and green status may not mean task success. |
| Claude `-p` plus local cron | Yes, if the machine and scheduler run successfully ([Claude Code Headless Docs](https://code.claude.com/docs/en/headless)). | Yes, it runs locally in the working directory ([Claude Code Headless Docs](https://code.claude.com/docs/en/headless)). | Yes by default, unless explicitly resumed ([Claude Code Headless Docs](https://code.claude.com/docs/en/headless)). | Yes through file handoffs and shell stage sequencing ([Claude Code Headless Docs](https://code.claude.com/docs/en/headless)). | Not inherently; self-rescheduling requires editing the external schedule, which should be gated. | `--allowedTools` and permission modes can constrain unattended runs ([Claude Code Headless Docs](https://code.claude.com/docs/en/headless), [Claude Code Permission Modes](https://code.claude.com/docs/en/permission-modes)). | Best primary v1 runner if local scheduling is acceptable. | OS scheduling, permissions, or sleep can cause skipped or partial runs unless wrapped fail-closed. |
| Codex standalone automations | Yes if the local Codex app is running, the machine is powered on, and the project remains on disk ([Codex Automations](https://developers.openai.com/codex/app/automations)). | Yes within the project and sandbox mode constraints ([Codex Sandboxing](https://developers.openai.com/codex/concepts/sandboxing)). | Yes for standalone automations, which start fresh each tick ([Codex Automations](https://developers.openai.com/codex/app/automations)). | Yes by shared files and staggered automations, but no native cross-automation DAG is documented ([Codex Automations](https://developers.openai.com/codex/app/automations)). | Yes, Codex can create or update automations from a thread or skill ([Codex Automations](https://developers.openai.com/codex/app/automations), [Codex for almost everything](https://openai.com/index/codex-for-almost-everything/)). | Automations default to no approval if policy allows it, but sandbox and admin policy can block or hang runs ([Codex Automations](https://developers.openai.com/codex/app/automations)). | Good if Truffle standardizes on Codex and accepts app-awake dependency. | Missed runs, sandbox-blocked network, and no native failure alerting. |
| Codex thread automations | Yes under the same machine/app/project constraints as Codex automations ([Codex Automations](https://developers.openai.com/codex/app/automations)). | Yes within the project and sandbox mode constraints ([Codex Sandboxing](https://developers.openai.com/codex/concepts/sandboxing)). | No, because thread automations preserve accumulated conversation context ([Codex Automations](https://developers.openai.com/codex/app/automations)). | Yes for heartbeat-style ongoing tasks ([Codex Automations](https://developers.openai.com/codex/app/automations)). | Yes, Codex can schedule future work for itself ([Codex for almost everything](https://openai.com/index/codex-for-almost-everything/)). | Non-interactive approval can be powerful but risky if paired with broad access ([GPT-5.2-Codex System Card Addendum](https://cdn.openai.com/pdf/ac7c37ae-7f4c-4442-b741-2eabdeaf77e0/oai_5_2_Codex.pdf)). | Not ideal for Scout to Read to Review because fresh-stage context is preferred. | Context drift and missed machine/app execution. |
| Code-driven DAG pattern | Yes when run by a scheduler or workflow runner ([OpenAI Agent Orchestration](https://openai.github.io/openai-agents-python/multi_agent/), [LangGraph](https://www.langchain.com/langgraph)). | Depends on runner; local-first is straightforward if the DAG runs locally. | Yes if each node starts a fresh process or fresh model session. | Yes by design. | Usually externalized to the scheduler, not decided by the model. | Human and deterministic gates can be explicit at nodes ([LangGraph](https://www.langchain.com/langgraph)). | Good as a pattern, but do not adopt a framework yet. | Over-engineering and premature platform gravity. |
| Evaluator-optimizer pattern | Yes inside a bounded loop if max iterations and thresholds are explicit ([Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)). | Depends on implementation. | Usually yes if evaluator and generator are separate calls. | Yes inside the evaluation loop. | No, not a scheduler. | Requires a pre-defined rubric and stop criteria ([Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)). | Good for Review and advisor checks, not for autonomous factual truth. | Rubric drift, LLM judge overconfidence, and non-convergence. |
| Run ledger and watchdog pattern | Yes as an external monitor or post-run verifier ([Auditable AI Agent Loop](https://arxiv.org/html/2603.17381v3), [Auditing and Logging AI Agent Activity](https://www.loginradius.com/blog/engineering/auditing-and-logging-ai-agent-activity)). | Yes if logs are local files. | Yes, because ledgers summarize stage outcomes rather than carrying context. | Yes by checking stage status and termination reason. | No; it should alert or block, not self-expand scope. | Deterministic health checks are preferable to model-only judgment. | Very good as a lightweight convention. | If too heavy, it becomes infrastructure before evidence proves need. |

## Loop design options

| Option | Pros | Cons | Failure modes | What would make it worth choosing | Recommendation |
|---|---|---|---|---|---|
| Current manual Scout to Loop 1 to Loop 2 | Keeps judgment close to the operator, avoids premature infrastructure, and preserves the learning posture. | Slow, inconsistent, and hard to repeat at enough volume to discover recurring pressure. | Review gaps, inconsistent receipts, weak recurrence tracking, and human memory becoming the hidden system. | Choose while prompts and artifact conventions are still changing after every run. | Keep as v0 baseline and reference process. |
| Local scheduled chain using `run_status` | Fits local-first Truffle, gives fresh stage context, uses file handoff, and makes reruns idempotent. | Requires local machine reliability and explicit handling of missed runs. | Stage runs against wrong status, partial run advances, live-browse gate bypass, or schedule fires while machine is asleep. | Choose once `run_status`, verification checklist, receipt template, and `needs-human-review` are added. | Choose next for v1. |
| Single long-running loop or session | Simple to start and useful for polling or monitoring one open question. | Accumulates context, blurs stage boundaries, and encourages the model to remember rather than read artifacts. | Context drift, compaction loss, stale assumptions, and hidden state leaking judgments into State. | Only worth using for bounded “wait and re-check” tasks with short duration and explicit stop criteria. | Avoid as the primary Market Read Lab loop. |
| Supervisor/evaluator model | Separates Scout, Read, Verifier, Reviewer, and Triage roles, and can hold gates centrally. | Risks becoming a workflow platform and increasing ceremony before recurrence proves need. | Supervisor invents structure, over-blocks, rubber-stamps, or becomes a second ontology. | Worth adding when there are many concurrent reads, repeated tool-choice errors, or reviewer fatigue. | Add only the smallest advisor pass now; defer full supervisor. |

### Option assessment

The current manual loop is still valuable because the product question is not “how can Market Read Lab run more often?” but “what durable evidence object makes future reads cheaper and more trustworthy?” A manual loop preserves that learning posture, but it does not create enough repeated pressure to discover stable source panels, denominator reconciliation patterns, or verification gaps.

The local scheduled chain is the right next step because it preserves separate artifacts and stage boundaries. It should be armed only after Scout proposes one or two candidate questions, and each downstream stage should no-op unless `run_status` exactly matches the expected prior state. That design borrows the strongest lesson from task DAGs without adopting a framework: fixed control flow should be code- or convention-driven, while LLM judgment should stay inside bounded nodes ([OpenAI Agent Orchestration](https://openai.github.io/openai-agents-python/multi_agent/), [LangGraph](https://www.langchain.com/langgraph)).

The single-session loop is the wrong default because Market Read Lab wants accumulated evidence in files, not accumulated model context. Claude `/loop` is useful for in-session repeated checks, but its context accumulation and session dependency are mismatched to fresh-stage research reads ([Claude Code Scheduled Tasks Docs](https://code.claude.com/docs/en/scheduled-tasks)).

The supervisor/evaluator model is conceptually attractive but should not be built as a platform. Supervisor patterns are valuable when a single agent has too many tools, too much context, or too many specialist responsibilities, but Market Read Lab’s immediate issue is weaker: it needs receipt hygiene, source-grade discipline, and stage idempotency ([Databricks Supervisor Agent Architecture](https://www.databricks.com/blog/multi-agent-supervisor-architecture-orchestrating-enterprise-ai-scale)).

## Verification and evaluation proposal

### Deterministic checks

| Check | What it verifies | Fail-closed behavior | Why it matters |
|---|---|---|---|
| Source-rigor check | Every claim requiring freshness has exact URL, capture date, source type, and primary/secondary label. | Set `run_status: needs-human-review`; block confident language. | Current claims need external grounding, not model memory. |
| No-snippets-as-evidence check | Any search/news snippet is labeled as a lead unless the underlying URL was captured or fetched. | Block `read-done`; require receipt or downgrade to lead. | Prevents the Run 002 failure pattern. |
| Receipt completeness | Each accepted source has URL, capture date, source type, excerpt or saved receipt, and claim IDs. | Block Review until receipts are complete or explicitly waived. | Makes future reads cheaper and auditable. |
| Current-claim volatility | Claims involving news, pricing, policy, regulation, launches, or app-store/review motion carry freshness and volatility flags. | Require `needs-human-review` for volatile claims before confident synthesis. | Avoids turning dated signals into stale State. |
| `run_status` and idempotency | Stage only runs when status matches expected prior state and only writes allowed artifacts. | No-op with a short status note. | Makes reruns safe. |
| Triage duplication | New triage items are compared against existing queue titles, pressure lenses, source gap type, and target convention. | Append as “possible duplicate” rather than new item. | Prevents pressure inflation. |
| No auto-graduation | Triage submissions cannot mutate shared State, prompts, templates, or engine conventions automatically. | Block write-back and require human approval. | Preserves the anti-Doro line. |
| Spend and live-browse gate | Firecrawl spend, broad web browsing, current-event sourcing, or paid capture is declared before execution. | Stop at `needs-human-approval`. | Keeps autonomy from silently increasing cost or claim risk. |

These deterministic checks are the core of v1. Contract-first design says the acceptance layer should be deterministic even if model generation is probabilistic, and fail-closed agent tools should stop when preconditions are missing rather than continuing with a confident story ([AI Orchestration Reliability](https://brendan-davies.dev/ai-orchestration-reliability.html), [Good Agent Tools Fail Closed](https://rogerchappel.com/blog/fail-closed-agent-tools/)).

### LLM reviewer checks

The LLM reviewer should not decide whether a factual claim is true. It should answer bounded questions: whether the read overclaims beyond receipts, whether snippets were treated as evidence, whether the source-grade rubric was applied consistently, whether the denominator was stated, whether missing-company radar is separated from membership claims, and whether triage items duplicate known pressure lenses.

This aligns with the evaluator-optimizer pattern only if the rubric exists before the loop starts. Anthropic’s pattern works when clear evaluation criteria exist and LLM feedback can mimic useful human feedback, but the “No Free Labels” result argues against trusting an LLM judge on hard factual questions without human-written or external reference grounding ([Building Effective Agents](https://www.anthropic.com/research/building-effective-agents), [No Free Labels](https://arxiv.org/html/2503.05061v1)).

Recommended reviewer prompt outputs:

| Field | Allowed values | Purpose |
|---|---|---|
| `verdict` | `pass`, `pass_with_caveats`, `needs_human_review`, `fail_closed` | Keeps reviewer output bounded. |
| `blocking_issues` | list | Only includes issues that should stop stage advancement. |
| `nonblocking_comments` | list | Captures advisory improvements without blocking. |
| `source_rigor_findings` | list | Flags weak receipts, snippets, missing capture dates, or overclaiming. |
| `triage_duplicate_candidates` | list | Suggests possible duplicates without auto-merging. |
| `recommended_run_status` | enum | Suggests status; deterministic wrapper or human decides final state. |

### Human approval gates

Human approval should be required before live external browsing beyond a pre-approved small panel, paid capture or Firecrawl spend, confident current-event or regulatory claims, promotion of triage items into engine changes, write-back into shared State, and any new durable category/cohort primitive. OpenAI’s agent tooling treats guardrails and human oversight as first-class controls for sensitive or high-blast-radius actions, and LangGraph’s interrupt pattern shows the useful model: stop at a node, present the state, and resume only after approval ([OpenAI New Tools for Building Agents](https://openai.com/index/new-tools-for-building-agents/), [LangGraph](https://www.langchain.com/langgraph)).

The gate should be selective, not constant. Human-in-the-loop systems fail when reviewers face too much volume and begin rubber-stamping, so Market Read Lab should gate only high-risk transitions and not every minor artifact edit ([Designing Agentic Workflows](https://dev.to/danielbutlerirl/designing-agentic-workflows-where-agents-fail-and-where-we-fail-4a95)).

## Overwatch and advisor recommendation

Market Read Lab does need a small advisor pass now, but it does not need a standing supervisor or overwatch agent. The smallest useful version is a post-Loop-1 verifier that runs after `read.md` and `run-notes.md` exist, checks receipts and claims against a static checklist, and writes a compact `verification.md` or verification section in `run-notes.md`.

### Smallest useful advisor

| Dimension | Recommendation |
|---|---|
| When it runs | After Loop 1 Read, before Consumer Review and Developer Review. |
| Inputs | `read.md`, `run-notes.md`, `receipts/`, candidate question metadata, pressure lenses, and existing triage queue if available. |
| It can block | Advancement from `read-done` to Review when receipts are incomplete, snippets are used as evidence, current claims lack capture dates, or live/spend approval is missing. |
| It can only comment on | Category design pressure, source panel usefulness, possible triage duplicates, and whether the run suggests a future convention change. |
| It cannot do | Promote State primitives, edit shared company profiles, auto-merge triage items, launch live browsing, or modify schedules. |

This advisor should be deterministic plus LLM-based. Deterministic checks should produce hard pass/fail findings, while the LLM should provide interpretive critique against the checklist. The design borrows from evaluator-optimizer loops without building a broad judge infrastructure, and it borrows from run-ledger/watchdog patterns without turning Market Read Lab into an observability platform ([Building Effective Agents](https://www.anthropic.com/research/building-effective-agents), [Auditable AI Agent Loop](https://arxiv.org/html/2603.17381v3), [Auditing and Logging AI Agent Activity](https://www.loginradius.com/blog/engineering/auditing-and-logging-ai-agent-activity)).

### Trigger for a fuller overwatch agent

Add a fuller supervisor only if at least two of these conditions recur across several runs:

- Scout repeatedly chooses questions that are not answerable by the store or approved sources.
- Reads repeatedly need live browsing after claiming they are store-only or local-existing.
- Reviewer output repeatedly finds snippet-as-evidence violations.
- Triage accumulates duplicate or near-duplicate system-pressure items.
- Multiple scheduled stages fail silently or run out of order.
- Source panels become stable enough that missing-source detection is a repeated, mechanical task.
- More than one domain-specific research loop is running concurrently and tool-choice confusion becomes a real source of failures.

Until then, a supervisor would likely recreate the workflow-platform path Truffle is intentionally avoiding.

## Concrete recommendations for Market Read Lab

### Adopt now

- **Add `run_status` as a stage lock**: Use `scout-only`, `read-done`, `needs-human-review`, and `reviewed`; each stage should no-op unless the status exactly matches the expected previous state.
- **Add a verification checklist**: Include source rigor, no snippets as evidence, receipt completeness, current-claim volatility, status/idempotency, triage duplication, no auto-graduation, and bounded-live/spend gates.
- **Add `needs-human-review`**: Use it as the fail-closed state when receipts are incomplete, current claims are volatile, or a requested action exceeds approval scope.
- **Add a lightweight receipt template**: Require URL, capture date, source type, primary/secondary status, claim IDs supported, and excerpt or saved capture path.
- **Modify Scout prompt**: Scout should label each candidate with `autonomous_eligible`, `evidence_mode`, expected denominator, likely source panel, and whether live browsing would be needed.
- **Modify Read prompt**: Read should use the store first, report denominator reconciliation explicitly, separate State from Signals from Judgments, and downgrade unsupported current claims to leads.
- **Modify Review prompts**: Consumer Review should ask usefulness and decision impact; Developer Review should ask what system pressure recurred and whether a convention, not a primitive, would reduce future cost.
- **Add a post-Read advisor pass**: Let it block only evidence hygiene and approval-scope violations; let it comment on system pressure without approving engine changes.
- **Chain scheduled tasks only after Scout**: Weekly Scout can be autonomous; Read and Review can be armed after Scout only when candidate metadata says the question is autonomous-eligible.
- **Notify instead of continuing for risky paths**: When evidence mode is `live-external-needs-approval`, the task should stop and ask for approval rather than browsing. Planned `bounded-live` runs are allowed only inside their `live_evidence_plan`.

### Defer

- **Defer category-level Signals primitive**: Run 002 surfaced the gap, but one sighting is not enough to define the primitive.
- **Defer relation subsystem**: Run 001 showed supplier/backend edges may matter, but capture grain and query ergonomics are the nearer pressure.
- **Defer source-panel registry**: Let repeated runs reveal stable panels before formalizing them.
- **Defer broad entity resolution**: Keep domain-keyed company State as the center of gravity.
- **Defer fully autonomous write-back**: Triage remains a queue of submissions, not approvals.

### Suggested v1 run contract

Each run should declare:

| Field | Purpose |
|---|---|
| `run_id` | Stable local identifier for repeatability. |
| `question` | The exact market/system-test question. |
| `run_status` | Stage lock and idempotency guard. |
| `autonomous_eligible` | Whether downstream stages may run without approval. |
| `evidence_mode` | `store-only`, `local-existing`, `bounded-live`, or `live-external-needs-approval`. |
| `allowed_sources` | Store, curated list, or approved external panel. |
| `disallowed_actions` | Live browsing, paid capture, write-back, or category primitive creation unless approved. |
| `pressure_lenses_fired` | Recurrence tracking only, not an approval mechanism. |
| `termination_reason` | `completed`, `needs-human-review`, `blocked-by-approval`, `insufficient-evidence`, or `failed-checklist`. |

This contract is intentionally smaller than a ledger system, but it borrows the auditability principle that every run should record the objective, allowed modifications, evaluator/checklist, and outcome ([Auditable AI Agent Loop](https://arxiv.org/html/2603.17381v3)).

## Anti-Doro check

Do not build these yet:

- **Category ontology**: Durable categories lack a clean natural key, and premature category objects would pull Truffle toward an ontology problem.
- **Graph of market entities**: Relation edges are useful only after repeated runs prove which relation types recur and can be verified.
- **Always-on monitor**: Scheduled Scout is enough; always-on monitoring would increase current-claim and spend risk before source rigor is solved.
- **Generic market score**: Signals should stay dated, source-specific, and append-only rather than being blended into a generic score.
- **Relation-type registry**: Run 001 showed backend/supplier relations are sparse and hard to verify, so the near-term fix is capture grain and query ergonomics.
- **Multi-agent workflow platform**: The loop is still discovering conventions, and a platform would freeze guesses too early.
- **Broad LLM judge infrastructure**: LLM judges are useful for structural critique but unreliable as final factual authorities on hard or under-specified questions ([No Free Labels](https://arxiv.org/html/2503.05061v1), [LLMs-as-Judges Survey](https://arxiv.org/html/2412.05579v2)).
- **Auto-mutating downstream project knowledge bases**: Triage items should remain submissions, not approvals, until repeated pressure justifies a human-approved convention change.

## Final answer to the design question

Market Read Lab should use a local scheduled stage chain next, gated by `run_status`, `evidence_mode`, and a deterministic verification checklist. The first autonomous unit should be weekly Scout, because Scout can propose questions and stop without changing State. Read and Review can be armed for `store-only`, `local-existing`, or planned `bounded-live` questions; broader live external sourcing, unplanned paid capture, or write-back should fail closed into `needs-human-review`.

The added verification mechanism should be a post-Read advisor pass, not a full overwatch system. It should combine deterministic checks with an LLM reviewer that comments against a static rubric, and it should be allowed to block only stage advancement when evidence hygiene or approval scope fails. That is enough to address the early evidence from Runs 000 to 002: denominator reconciliation remains a query/reporting convention, backend relations stay a capture-grain issue, and category-level external events become carefully receipted Signals candidates rather than a new primitive.
