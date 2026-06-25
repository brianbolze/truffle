# Proposal: `/discover-neighbors` verb — find companies not yet in the store

Date: 2026-06-24
Status: rejected — see lead-decision.md (FINAL: rejected 2026-06-24; implementation unwound)
Source request: work-menu coverage pass (2026-06-24), card #1 — "wire discovery: find companies near X that aren't in the store, over `exa_search.py` + L001." Brian lifted BACKLOG:40's "optional later" park to start it, and asked for a new **verb** (`skills/`) rather than a `QUERYING.md` recipe.

<!-- Status tracks the PROPOSAL lifecycle only: proposed → reviewed → accepted | revise | park | cut.
     The implementation receipt + gate log belong in implementation-notes.md after the decision. -->

## Required Fields

risk: medium
write_scope: New — `skills/discover-neighbors/SKILL.md` (one self-contained playbook; name TBD-final). Pointers (one line each) — `QUERYING.md` (near Recipe 9: "to find companies *not* in the store, use `/discover-neighbors`, not a read recipe"), `tools/exa_search.md`, and optionally `skills/query-companies/SKILL.md`'s "missing capture" hand-off. Do **not** touch `store/`, tool code (`exa_search.py`, `_match.py`), schemas, prompts, SIGNALS paths, or create any new script/store object.
spend_stop: The skill calls a **paid** API (`exa_search.py` → `EXA_API_KEY`, meters in USD via `costDollars`). Discovery is **opt-in and bounded** — a handful of queries per invocation, no standing/scheduled run — and it **never captures**: output is a worklist; `/research-company` stays the only Firecrawl-spending path, separately approved. Stop and escalate if a run wants more than a handful of queries or any automated/scheduled discovery.
acceptance_checks: Manual review confirms the `SKILL.md` (a) frames `exa_search` as a discovery **feeder**, not a denominator/census; (b) **reuses Recipe 9's** store-diff + propose-don't-write output *by reference*, not by restating or weakening it; (c) states the paid-per-query spend posture + opt-in/bounded cap + "never captures"; (d) carries the low-recall / net-new-bias / "corroborate downstream" caveats and the "not in store ≠ not in market" line; (e) keeps the profile-vs-stub diff rule (`store/<slug>/profile.md`, via `store.py find`). Verify: a dry-run invocation produces a tiered not-in-store worklist + boundary statement and mutates nothing (`git status` clean after); `git diff --check` on touched docs; `python3 scripts/querycheck.py --strict` passes if `QUERYING.md` is touched. No new code → no new tests. Receipt → `implementation-notes.md`.
escalate_if: implementation wants to (a) add a helper/tool — `exa_match.py` is explicitly discouraged by `serp_match.py`; any code (even a `_match.py` reuse) exceeds this packet; (b) write to `store/`; (c) persist a discovery panel as a Signal or category object; (d) add an auto-capture / capture-campaign / fast-capture-stub step (a real future arm, but its own packet); (e) stand up a scheduled/standing discovery job (the parked Monitoring item); or (f) grant spend beyond the bounded cap.

## Problem

Truffle's Coverage pillar wants a fast way to ask "which companies near this one are **not yet in the store**?" Both pieces to answer it exist, but nothing stitches them into something you can invoke:

- **`tools/exa_search.py`** (landed 2026-06-20) turns a description into real companies via Exa `/search` + `category:company` — strong at the net-new long-tail, the exact population we're missing.
- **Recipe 9** (the L001 "who is the store missing?" radar) already owns the back half: diff candidates against the **profiled** store, write a boundary statement, emit a tiered propose-don't-write worklist — but its only feeder is bounded-live listicles, and it lives inside a market-read run.

So today an agent re-derives the method from memory or wires `exa_search` ad-hoc with no caveats or spend ceiling. The fix is a **named verb** that joins the exa feeder to Recipe 9's discipline with the right (paid) spend posture.

## Short Answer

Add a thin **`skills/discover-neighbors/` verb** (one `SKILL.md` playbook). It's a coverage-*expansion* action that reaches outward and spends — categorically a sibling to `/research-company`, **not** a read recipe, so it does not belong in `QUERYING.md` (which `/query-companies` routes through, and which is read-only/never-spends by contract). Keep it minimal: reuse `exa_search.py` + `store.py find`, and **reference** Recipe 9 for the store-diff/output rather than duplicating it. No new script.

## Constraints / Non-Goals

- **Not a market census/denominator** — Recipe 9's caveat holds; "not in store ≠ not in market."
- **Never captures** — output is candidates only; capture stays the separately-approved `/research-company` path. (A `--capture-stubs` fast-read arm is a plausible *future* packet, explicitly out of scope here.)
- **Not a standing/scheduled job** — that's the parked Monitoring item.
- **No new tool, script, store object, Signal, or category** — one `SKILL.md` + pointer lines.
- **Doesn't revive `exa_similar`** (confirmed not-salvageable for cross-shop) and **doesn't replace** the owned-`/vs` + review co-shop path for *known*-brand cross-shop.

## Options considered

1. **New thin `skills/discover-neighbors/` verb** — `SKILL.md` reusing `exa_search.py` + `store.py find`, deferring to Recipe 9 for diff/output. Correct category (expansion verb, reaches out, spends); matches the "verbs over services" principle; nameable, discoverable, and has a growth path (fast-capture arm later). [should have] — **recommended**
2. **Docs-only `QUERYING.md` recipe (Recipe 10).** Smallest bytes, reuses Recipe 9 by reference — but wrong surface: it bloats the read book with a paid, outward-reaching pattern that clashes with `/query-companies`' read-only/no-spend contract, and it's undiscoverable (an agent wanting to *find new companies* won't grep read recipes). [should have]
3. **A `_match.py`-based step or `exa_match.py` consumer** mechanizing the dedup/diff. Explicitly discouraged by `serp_match.py`'s "do not make `exa_match.py`" ruling and the listicle packet's "a helper adds knobs around judgment." Escalation-only if a real run proves the by-hand diff is the friction. [could have]

## Recommendation

**Option 1.** The discriminator is category, not byte-count: this work spends and reaches outward to expand coverage, which is the opposite of `QUERYING`/`query-companies`' read-only contract, so a recipe there is a category error regardless of length. A verb is the engine's sanctioned shape for "repeatable work that starts, writes evidence, and stops," it's nameable and discoverable, and it can grow a fast-capture arm later — none of which a buried recipe offers. Net bloat to `QUERYING.md` is *lower* (a one-line pointer, not a recipe). The cost is one new verb's surface; the guardrail (below) keeps it thin.

## Implementation Sketch

No new code. One `SKILL.md`, mirroring the lean shape of `deepen-offerings`:

1. **When to use** — you have an anchor cohort/description and want companies *not yet profiled*, especially the long tail listicles (Recipe 9) miss. Complement to Recipe 9; not a replacement for known-brand cross-shop.
2. **Spend posture** (loud, up top) — paid per query; opt-in, a handful of queries per run, no standing/scheduled use; never captures.
3. **Feed** — `python3 tools/exa_search.py "<description>" --category company` (neural pinned); vary the description across 2–3 angles, since per-query recall of a known set is low.
4. **Normalize + dedup** returned domains caller-side (fold `www.`/`api.`/`en.`/i18n mirrors to apex; dedup across queries) — the tool leaves this to the caller by design.
5. **Diff against the profiled store** (defer to Recipe 9 step 6) — `store.py find <domain|name>`; "in store" = `store/<slug>/profile.md` exists; a stub doesn't count.
6. **Output** (defer to Recipe 9 step 7) — a tiered not-in-store worklist (corroborated-across-queries = stronger; single-query = weaker lead) + boundary statement; propose-don't-write.
7. **Caveats travel** — exa `/search` is a feeder with low known-set recall and net-new bias: "not surfaced" ≠ "not a neighbor," "not in store" ≠ "not in market"; corroborate downstream.
8. **Pointers** — one line each in `QUERYING.md` (near Recipe 9), `tools/exa_search.md`, and optionally `query-companies`' missing-capture hand-off. No other files.

## Review Notes

- **Scope-creep watch:** any drift toward a helper/tool, a stored panel, an auto-capture/fast-capture step, or a scheduled job exceeds this packet (see `escalate_if`). The fast-capture arm is real and tempting — hold it for its own packet.
- **Open call for review:** final verb name (`/discover-neighbors` vs `/find-neighbors`) and whether the one-line `query-companies` hand-off is worth touching that skill.
- **Risk = medium:** no code and no store writes, but it shapes autonomous *paid-API* behavior — the spend/caveat lines must read louder than the mechanics (same posture the listicle packet took).
- **Out-of-scope observation logged separately:** archived experiments still have live-path inbound links — `BACKLOG:40` + `exa_search.py:15` → `experiments/2026-06-20-cohort-discovery/` (now `_archive/`), and `BACKLOG:43` → `experiments/2026-06-13-adaptive-capture-depth-frame/` (now `_archive/`). Small archive-link drift, not this packet's job.
