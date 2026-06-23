---
created: 2026-06-23
last_updated: 2026-06-23
authors: both
status: frame — problem framed; frame approved by Brian on 06-23. Now working on proposal(s).
---

# Frame: Skills That Learn

*The general capability — Truffle's verbs, skills, and conventions should get sharper from their own runs — with Agentic Build as the first proving ground.*

## 30-second skim

**We have no learning loop we can trust to make Truffle better instead of worse.** Left alone, lessons stay buried and nothing compounds. But the naive fix — letting agents consolidate and rewrite the system — corrupts it: they overfit to the one case in front of them, bloat the rules, and collapse observation straight into premature solution.

Truffle already learns at the *per-run* grain, and there it works: `/research-company` refines a `site_notes` field each run — e.g. *"`/v2/map` returns URLs that are almost all blog posts; derive structure from homepage links and mega-nav"* — so the next capture of that company runs more efficiently. What's missing is **cross-run, system-level learning**: a verb, or the way we build verbs, getting sharper across many runs and companies. The one real attempt — Market Read Lab's `triage.md` — is actively failing.

*Scope note: Truffle has two verb classes — user-facing (`skills/`) and internal developer skills (`.claude/skills/`) — plus the conventions both follow. Agentic Build is about the developer class and its conventions first; the two may want different solutions.*

## Why this matters

**The prize is a Truffle that runs, learns, and improves itself over time.** The holy grail — arguably the next era of how software and systems get built — and what frees Brian for higher-leverage work: the Telehealth Venture, where his focus and income actually are. Agents carry Truffle forward; Brian steps in only for the calls that genuinely need him.

**We can't get there as the system is today.** An autonomous builder that can't self-correct, learn from its mistakes, or internalize Brian's preferences and context doesn't just fail to help — it *degrades* Truffle, faster than a human would. Autonomy without learning is the worst kind: more motion, the same mistakes, *"repeated mistakes with a clean-looking process around them."* The learning loop isn't a feature of Agentic Build — it's the precondition for trusting it at all.

The pain is already concrete: a useful `workflow_note`, a reviewer's scope catch, or a Brian correction stays buried in one packet file, and the next agent rediscovers it.

## What makes it hard

Market Read Lab is the autopsy — most-documented because it has the most runs, but the same burial already shows in the few Agentic Build packets, and `site_notes` is the positive control (per-run learning works *because the step is forced*).

- **Agents collapse observation into solution.** They jump to a fix for the one case they just saw; across runs that metastasizes into a policy-table soup of forks — what Truffle refuses.
- **Agents anchor on whatever convention they find and mirror it.** A crappy first draft becomes the de-facto template and compounds — which is exactly why the conventions we author upstream are the leverage point.
- **Feedback and the item-of-work get conflated.** An observation ("I was confused when…", "this keeps failing") and the unit of work to fix it are different objects. Fused into one record, it can't dedupe, graduate, or close — it just accretes.
- **Aggressive tidying destroys the richness.** Dedup buys a clean backlog and throws away the divergent signal before anyone sees it.
- **Neither steward scales.** Brian-as-steward → overwhelmed; the agent-steward we tried → overfit and jumped to solutions.
- **The learner can't see across runs.** One session can't tell the same thing happened three runs ago — and cross-run patterns are the whole signal.
- **A clean process can still be aimed wrong.** A mechanically sound loop learns nothing useful if its default incentive points at the wrong target.

<details>
<summary>The Market Read Lab autopsy, in detail</summary>

- **"Leapt to solution-shape."** The retro: runs *"leapt to solution-shape… because that's the shape the machinery kept asking for,"* which *"crowded out plain observation"* and made every run *"converge on the same hammer."* The template shape drove the behavior.
- **~345 → ~2.** Five agents re-reading the *raw* runs pulled ~345 distinct observations; triage had compressed them to ~2 ideas. *"The thinness was the triage's fault, not the lab's."*
- **`MRL-002`** carries ~15 ever-growing Evidence Log paragraphs and still hasn't graduated — the conflation + accretion failure in the flesh.
- **"Rewarded the wrong thing."** The apparatus *"ran clean and safely"* yet produced almost nothing, because its default incentive ("answer from the store") pointed at the wrong target.
- Files: `00-market-read-lab/triage.md` (symptom); the [retro](../00-market-read-lab/_design/retro/2026-06-20-first-20-runs-retro.md) + [idea-harvest](../00-market-read-lab/_design/retro/2026-06-20-idea-harvest.md) (diagnosis); the failed [agent-steward frame](../00-market-read-lab/_design/2026-06-19-triage-agent-context-frame.md).
</details>

## Capability goal

**Long-term vision.** Any Truffle verb, skill, or convention gets sharper from its own runs semi-autonomously, with Brian in the loop only for the important, risky, or ambiguous calls — and the pattern is elegant enough to lift to user-facing verbs and other projects, not overfit to Agentic Build's or Market Read Lab's circumstances.

A good outcome: sharper proposals, better risk calls, less repeated drift — and docs that need fewer iteration / simplification passes. If Brian has to run `/overwhelmed` on a change, that's a bad signal the system should be learning from.

**Must have / do**

- **Capture honest feedback without forcing a fix.** A run or packet can log an observation, friction, wish, or risk-miss *as feedback* — not as a proposed solution.
- **Make feedback durable and findable** — it accumulates beyond the individual session/packet, so the next agent doesn't rediscover it.
- **Don't let feedback collapse into a fix.** Logging an observation and deciding to act on it are separate steps that shouldn't fuse into one record.
- **Consolidate across runs.** Something with cross-run visibility can spot patterns and propose improvements — to skills, templates, recipes, or rules — for human approval, without overfitting to one case.

**Should have / do**

- **Preserve divergence** — keep raw observations from being compressed away before they're seen; any clean view is downstream of the divergent record, not a replacement.
- **Conventions should be improvable, not calcified** — the recipes/templates agents anchor on shouldn't freeze around the first draft.
- **Promotion stays inspectable** — you can see why something graduated, and challenge it.
- **Product gaps escape the build loop** — a Truffle gap surfaced during a build reaches product planning, not just the build system's own memory.
- **Design the shape to generalize** to user-facing verbs and other projects.

**Bonus / could have**

- **Auto-apply for the safest class** — the lowest-risk improvements proposed *and* applied without a human in every loop, gated by risk class.
- **Replay / eval** — re-run tricky prior cases against a changed skill before trusting the change.

**Out-of-scope / future** *(sequencing, not rejection)*

- The fully-general cross-project improvement system — we want the *pattern* to generalize, not to build the multi-project version now.
- Rolling this out to user-facing `skills/` — Agentic Build is the proving ground first.
- A full replay/eval harness or auto-apply-at-scale — the could-haves are the early slices.

## Non-Goals

*Genuinely not what this is — distinct from "out-of-scope," which we may still want later.*

- **An opaque / black-box memory service.** We *are* chasing semi-autonomous improvement — but whatever we build stays inspectable. Hidden memory and silent mutation are out; the aspiration to a generalizable, legible pattern is not.
- **Standing infrastructure or a daemon** that must keep running to stay true.
- **A task tracker, dashboard, or granular policy-manual** of escalation forks.
- **Extending Market Read Lab's triage machinery as the template.** MRL may be a temporary project we close once it's answered its cohort/category questions; its triage is the cautionary tale, not the thing to generalize.

## Constraints / assumptions

- **Keep the medium open, low-infra.** File-first + git already gives versioning, rollback, and provenance. Whether this layer stays in-repo or uses a tool is a solution-space call — but it must stay attributable (who/what/when), challengeable, and revertible.
- **The learning layer must not bloat itself.** Whatever accumulates has to resist becoming a verbose, ever-growing backlog or a manual of forks. "What does this replace?" applies to a new rule as much as a new field.
- **"Automatic" means surfaced and proposed**, near-term — applying stays human-gated until the safe-class auto-apply earns trust.
- **The corpus is thin today** (~3 implemented packets, one real `workflow_note`). Design for it growing; don't over-build for scale that doesn't exist yet.

## Prior art & early leanings

*Signals from the wallow that point toward solution-space — captured, not yet committed.*

- **Market Read Lab — the autopsy** (detail under *What makes it hard*). Its redesign already prescribes two leanings worth carrying: *observe, don't propose* (a run reports friction; shaping solutions is a separate, later pass) and *keep a divergent stream that never gets merged* (the clean backlog is downstream of it).
- **Feedback ≠ item-of-work (Brian's Linear model).** Dogfood *Feedback* items (land in `Submitted`; flavors Bug / User-feedback / Idea — "what did I observe") stay separate from the *item of work* — a new, linked issue created only when the team decides to act; duplicates are *linked, not deleted*, so evidence isn't wasted. The lean: feedback and work live in distinct workflows; an observation never auto-becomes a solution. (Loosely echoes State / Signals / Judgments.) Linear itself is also a candidate *medium* for this layer.
- **Conventions as the real object.** The system's deepest value may be improving the conventions agents anchor on — not one-off fixes. "Invest in conventions" (an Operating Principle) applied to the build loop: author great recipes/templates upstream so agents don't anchor on, and entrench, a crappy first draft.
- **Anthropic "Dreaming" talk** ([video](https://www.youtube.com/watch?v=tTcxVv8HHNw)). In-band vs out-of-band memory; an out-of-band pass with cross-run visibility that proposes changes *with evidence*, human-approved — plus a subtractive half that cuts stale memory.
- **Truffle's working primitives.** `site_notes` learns per-run *because the step is forced*. And the line already in the proposal: *"Observation is not a rule. A rule is not a skill edit. A skill edit is a change packet."*

## Open questions

- **What evidence corpus can a learning pass actually read?** Packet artifacts + `git log` are certain; full Claude Code session transcripts — are they retained and readable? This bounds how rich learning can get.
- **What's the unit of "feedback" for a build system** (vs a market read)? Bug / friction / idea / risk-miss / heuristic-worth-keeping?
- **What's the minimum that stops an agent curator from overfitting** — what makes the steward role safe to delegate at all?
- **Do user-facing verbs and developer skills want the same solution**, or different ones? Where does the overlap end?
- **Where does feedback attach** — per-packet, per-batch, per-skill?

## Related references

- [`2026-06-21-frame.md`](2026-06-21-frame.md) — parent Agentic Build frame; this is its "Learning loop" should-have, framed in depth.
- [`_design/2026-06-23-learning-system-proposal.md`](./_design/2026-06-23-learning-system-proposal.md) — the solution-space counterpart.
- [Operating Principles](https://app.notion.com/p/38684b6d1f49806a8922e20061e644fa) — "Learning loops" and "Invest in conventions"; file-first, no living infrastructure.
