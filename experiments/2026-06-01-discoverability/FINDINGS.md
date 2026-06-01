# Findings — upstream discoverability from a fresh agent in another project

> **Verdict: a clean split, and it's the opposite of the prior worry on one axis and a confirmed gap on
> the other.**
> **Single-company discovery is STRONG and unaided** — 4/4 fresh agents in an unrelated project reached
> the `research-company` skill and used the warm store correctly, including under *indirect* and *casual*
> phrasing and including a *cold* capture, with **zero** mention of the system in the prompt. The skill is
> an effective entry point and it *transitively reveals the store* (skill → SKILL.md's store path →
> corpus). **Cross-company aggregation discovery is BROKEN** — the one comparison probe reached for a
> *different* global skill (`competitive-research-audit`), which has no knowledge of the store, and
> **re-scraped all four brands live from scratch — every one of which was already warm in the store** —
> hitting 403s, timeouts, and aggregator contamination, and shipping several figures it had to flag as
> unverified. That is precisely the "lazy & error-prone WebSearch default" Brian wanted gone, and it maps
> exactly to consumption-affordance **Wall 2** (the rung-2 "wrap querying in a skill" half is unbuilt).

## Scorecard

✓ = reached the system / used the store · ✗ = defaulted to live web, store ignored · $ = Firecrawl spend (objectively verified)

| Probe | Reached system? | First move | Used warm store? | Spend | Outcome |
|---|:--:|---|:--:|:--:|---|
| **P0** reachability | ✓ | inventoried env → found skill **and** store path | — | $0 | Names skill + store + warm-serve logic; picks skill over WebSearch. *Ceiling: the system is reachable.* |
| **P1** explicit, **cold** | ✓ | `Skill(research-company)` | n/a (cold) | $0¹ | Correct cold-capture **plan**, slug resolved, read SCHEMA/playbook, stopped at guard. Meets "a new project can capture." |
| **P2** explicit, **warm** | ✓ | `Skill(research-company)` | ✓ warm-serve | $0 | Cited, store-grounded Hims dossier; correct freshness reasoning; flagged `unverified_fields`; offered refresh. Exemplary. |
| **P3** **indirect**, warm | ✓ | `Skill(research-company)` | ✓ + targeted re-verify | **$3** | Triggered **despite no "research/profile" words**; honored "not stale" by re-scraping only the 3 pricing pages, updated profile. Near-ideal cache-aware behavior. |
| **P4** **aggregation**, warm | ✗ | `Skill(competitive-research-audit)` → WebSearch/Exa | ✗ **ignored store** | $0² | Re-scraped 4 warm brands from live web; 403s/timeouts/aggregator data; multiple figures flagged unverified. **The gap.** |
| **P5** **casual/lazy**, warm | ✓ | `Skill(research-company)` | ✓ warm-serve | $0 | Even "what does X charge these days?" hit the skill and warm-served, cited, with snapshot caveats. |

<sub>¹ plan-first guard held — credits unchanged, no `ro-co` folder created. ² P4 spent no *Firecrawl* (used
WebFetch/Exa) — but that's the point: it bypassed the cache entirely. Credits 1360→1357 across the whole
run = P3's 3 only.</sub>

## The one finding that matters: a competing skill intercepts the aggregation intent

P4 didn't fail because the store is *unfindable* — P0 proves an agent *can* find it. It failed because the
**comparison intent pattern-matches to `competitive-research-audit`** (a global skill whose description
explicitly fires on "comparison across multiple companies / research these competitors / comp scan"), and
**that skill has zero awareness of the web-research store.** So the agent was actively *routed away* from
the cache toward live scraping. The store had clean, already-verified Hims/Hone/Marek/Maximus dossiers; the
agent re-derived them the hard way and got a *worse* result (Hone per-med prices and Marek monthly cost
ended up sourced from third-party aggregators and flagged unverified — the store had primary-source
captures).

The asymmetry is the whole story:

- **Single-company shape** has a global verb (`research-company`) that *is* the entry point and *leads to*
  the store. → discovered 4/4.
- **Cross-company shape** has **no store-aware entry point**. `QUERYING.md` (the rung-2 consume contract)
  is *inside the Web Research repo* and is only visible once you're already at the store — a fresh agent in
  another project never sees it. A *rival* skill owns the intent instead. → discovered 0/1.

This is consumption-affordance's **Wall 2**, now observed from the outside: "discoverability rests on
entering at the store root… the 'wrap it in a skill the agent reaches for' half of the Frame is still
unbuilt." The unbuilt half is exactly where the miss happened.

## Recommendations — cheapest rung first (per the engine's "spend on conventions, resist additions")

**1. [cheapest, fixes the exact miss] Make `competitive-research-audit` store-aware — a "Step 0: check the
local store."** That skill is Brian's, global, at `~/Development/ai-skills/claude-skills/competitive-
research-audit`. Add a first step: *before* any live scraping, resolve the web-research store
(`WEB_RESEARCH_HOME` or the canonical iCloud path), and for each company in the comparison, serve a warm
fresh `profile.md` if present; only go live for misses/stale/out-of-scope. This alone turns P4 from a
4-brand live re-scrape into a ~$0 read. No new surface — patches the skill that already won the intent.

**2. [the real structural fix] Build the unbuilt rung-2 half: a global "consume the company store" verb.**
A skill whose description triggers on *consumption/aggregation* intents — "compare these companies," "what
do these competitors charge/offer," "is X already in our research," "pull our notes on Y" — that routes to
the store, reads `QUERYING.md`, and filters the corpus **before** any web work. This is the missing
upstream entry point for Surface B and the literal thing the Frame's rung 2 and Wall 2 call for. Write its
description to **compose with / win over** `competitive-research-audit` for the cache-first step. (Open
design choice: one new `query-company-store` skill vs. folding consumption into `research-company`'s
description so the *same* verb covers "one or many." Lean: a sibling verb — keeps capture vs. consume
clean.)

**3. [substrate enabler, trivial] Implement `WEB_RESEARCH_HOME`.** The architecture's intended discovery
mechanism is **not actually set** in `~/.claude/settings.json` (verified) — `research-company`'s SKILL.md
falls back to a hardcoded iCloud path. Add the env var so (a) the store location is a first-class resource
both skills above lean on, and (b) the brittle hardcoded path goes away. Doesn't drive discovery by itself
(agents don't scan env for stores), but it's the clean substrate under #1/#2.

**4. [already-decided cheap insurance, from Wall 2] Self-document the entry point.** One-line header
pointer in every `profile.md` (`> querying this store: ../../QUERYING.md`) and/or have the consume verb
hand `QUERYING.md` to the caller. Helps agents that reach a *deep* path (single `profile.md`) without
passing the README. Lower priority for the upstream gap, but cheap and orthogonal.

**Explicitly NOT now:** a rung-3 SQLite index. The corpus is ~45 companies / ~100KB; grep + YAML-parse
already carried the aggregation in consumption-affordance. Don't build ahead of demand (anti-Doro line).

## What this *doesn't* claim (honesty)

- **P5's "casual phrasing still hit the skill" is the softest result** — Agent-tool sub-agents are primed-
  to-work; a real lazy top-level session might still reflexively WebSearch a one-liner. Re-run on the
  headless harness (default **sonnet**, not Opus) before banking it.
- **Model generalization untested.** Everything here is Opus. Brian's default is sonnet; the prior
  experiment flagged Opus-contingency. The single-company win and the aggregation gap are both likely
  robust (the gap is *structural*, not model-dependent), but the *margins* (does casual phrasing still
  trigger on sonnet?) are not.
- **n=1 per cell.** Directional. The single-company result has 4 corroborating cells + objective signals;
  the aggregation gap has 1 cell but an unambiguous, objectively-verified failure mode.

## Net

The system is **more discoverable than the Frame feared on the single-company path** (the global verb is a
working, self-revealing entry point) and **exactly as gapped as Wall 2 predicted on the aggregation path**
(no store-aware consume verb; a rival skill owns the intent and goes to live web). The fix is small and
already-designed-on-paper: teach the existing comparison skill to check the store first (#1), then build
the consume verb that should own the intent (#2), on a real `WEB_RESEARCH_HOME` (#3).
