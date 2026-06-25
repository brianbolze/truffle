# Change Review: `/discover-neighbors` verb

**Mode**: change (patch-after, against the accepted proposal + lead-decision). Boundary intact — `proposal.md` stayed a plan (`Status: accepted`, no receipt in it), the implementation receipt lives in `implementation-notes.md`. Clean change-mode audit, not a collapsed-boundary one.
**Reviewer**: independent (did not author the change this session).
**Date**: 2026-06-24
**Audited**: the three shipped files — `skills/discover-neighbors/SKILL.md` (new), the one-line `QUERYING.md` pointer after Recipe 9, the one-line `tools/exa_search.md` back-link — against Recipe 9 steps 6–7, `exa_search.md`, and `exa_search.py`'s docstring.

Findings first, most important first. Then a recommended lean — a recommendation, not a decision.

## Findings

### 1. Single source of truth: Step 4 references Recipe 9 *and* recaps its mechanics — a real but minor seam
This is the check the lead and proposal-review both singled out (lead-decision §3; proposal-review finding 6b), so I diffed the SKILL.md against Recipe 9 steps 6–7 line by line rather than confirming a pointer exists.

The header reference is clean and correct: line 17 ("the store-diff + propose-don't-write output live in **Recipe 9 steps 6–7**"), and Step 4 opens "**follow [Recipe 9](../../QUERYING.md) steps 6–7.**" That is a genuine link-out, not a paraphrase-in-disguise.

But Step 4 then *recaps* the operating core inline: the `store.py find` command, the in-store rule ("`store/<slug>/profile.md` exists (a stub doesn't count)"), the tiered worklist, the boundary statement, and propose-don't-write. Compare to Recipe 9:
- Step 4 in-store rule vs Recipe 9 step 1 ("count only profiled companies (`store/<slug>/profile.md`), not raw directories or stubs") — **same rule, restated in the SKILL.md.**
- "tiered not-in-store worklist … plus the boundary statement. Propose-don't-write" vs Recipe 9 step 7 ("a caveated coverage statement plus a tiered propose-don't-write worklist") — **same output, restated.**

So it's *reference + recap*, not pure reference. Two things keep this from being a blocker: (a) the recap is **faithful** — nothing weakens or contradicts Recipe 9, which was the real fear; (b) some of it is load-bearing for an agent to act (the `store.py find` command is the actual call). But it is duplicated text on a surface the lead explicitly asked to be reference-only, and it is the bit that will silently drift if Recipe 9's diff rule changes (e.g. if "stub doesn't count" ever softens). The cleanest version states the *command* an agent must run and defers the *rule + output shape* to Recipe 9 by reference, rather than re-asserting "a stub doesn't count" and "tiered worklist + boundary statement" in both files. **Calibration:** this is a seam, not a violation — the SKILL.md does reference, it just also recaps. Whether the recap is acceptable "operating mechanics" or avoidable duplication is a lead judgment; I'm flagging it because it's exactly the failure mode the gate was told to catch, and "it links out *and* restates" is easy to wave through as "it links out."

### 2. Spend ceiling — the required revision — is present, concrete, and checkable
Lead-decision §1 required ≤3 query angles, `--num-results 25`, and stop-and-ask before a 4th angle / any re-run. All three are in the SKILL.md, in two places:
- Dedicated "Spend ceiling (paid API — this is the contract)" section (lines 19–21): "**≤3 query angles**, **`--num-results 25`**, and **stop and ask Brian before a 4th angle or any re-run**. Opt-in only; no standing/scheduled use; it never auto-captures."
- Reinforced in the steps: Step 1 ("**2–3 short description angles**"), Step 2 (the loop is gated "for each angle (≤3)" and the command carries `--num-results 25`).

`--num-results` is a real flag on `exa_search.py` (confirmed: `p.add_argument("--num-results"…)`, line 191). The number-not-word gap the proposal-review flagged (finding 4) is closed. This satisfies the revision cleanly. Note the cap is *checkable by reading the SKILL.md* but not *enforced* — nothing in the tool stops a 4th call; enforcement rests on agent discipline, which is the correct posture for a prompt-level verb but worth naming so it isn't mistaken for a hard limit.

### 3. write_scope held exactly — three files, nothing else
`git status` (scoped) shows exactly the three in-scope changes and nothing more:
- `skills/discover-neighbors/SKILL.md` (new; the dir contains **only** `SKILL.md` — no code, no test, no helper).
- `QUERYING.md` — one added line, a pointer after Recipe 9's caveat. Not a recipe; routes "companies not in the store" to the verb. `git diff` confirms +1 substantive line.
- `tools/exa_search.md` — one added "Consumer verb" back-link line. `git diff` confirms +1 substantive line.

Nothing touched in `store/`, tool code (`exa_search.py` / `_match.py` untouched), schemas, prompts, SIGNALS paths, or `query-companies`. No `escalate_if` condition tripped: no helper/tool added (a), no `store/` write (b), no Signal/category object (c), no auto-capture/fast-capture step (d), no scheduled job (e), no spend beyond the cap (f). The `query-companies` missing-capture hand-off was correctly *deferred* (it was "optional" in write_scope and lead-decision §2's "defer optional arms").

### 4. Boundaries intact — never-captures, no code, light-to-start
- **Never captures:** stated three times (description line 8 "it NEVER captures", body line 15, Step-5/Scope line 39 "discovery only … never a capture, store write, stored panel, or scheduled job. To capture a surfaced candidate, hand off to `/research-company`"). The output is a worklist; `/research-company` stays the only Firecrawl-spending path. Clean.
- **No new code:** confirmed (finding 3). The dedup (Step 3) and diff (Step 4) are by-hand caller work over a bounded set (≤3 angles × 25 = ≤75 domains), exactly the "genuinely prose, not code in disguise" the proposal-review accepted (finding 3).
- **Light to start:** `disable-model-invocation: true` is set, so a *paid* verb never auto-fires (lead-decision §2). The SKILL.md is ~40 lines, thinnest-viable. The fast-capture arm is fenced to a future packet (Scope line 39 names the exclusions).

### 5. Caveats travel faithfully — the tool is represented honestly, not laundered
Step 5 + the description carry the load-bearing caveats and they match `exa_search.py` / `exa_search.md` verbatim-in-spirit: "low known-set recall + net-new long-tail bias," "*not surfaced ≠ not a neighbor*," Recipe 9's "*not in the store ≠ not in the market*," "corroborate downstream," "does not replace the owned-`/vs` + review co-shop read for *known* brands." These trace directly to the docstring ("recall of a *curated/known* set is low (a Hone-description search recovered 1/16…), so corroborate downstream; it does not replace a cross-shop read"). Per acceptance-check (a)/(d): Exa is framed as a *feeder*, never a denominator/census — no overclaim. Note this is the one place restating-from-source is *correct*: a caveat that travels with the verb is the point; the SSOT concern in finding 1 is about the diff *mechanics*, not these caveats.

### What this review could not see
- I did **not** run a live `--num-results 25` dry-run (it spends real Exa money). So I confirmed the worklist/boundary/propose-don't-write **instructions** are present and faithful; I did not observe a real invocation producing a mutation-free worklist. The proposal-review already flagged that the acceptance dry-run itself has a (small) paid spend (its finding 6); that trade-off is unchanged. "No store write possible from the verb" is credible because `exa_search.py` is print-only and the SKILL.md adds no write step — but it is reasoned, not observed-at-runtime.
- I audited the patch as text against the cited canonical sources; I did not exercise the `git diff --check` / `querycheck.py --strict` gate (implementation-notes routes those to the gate log). Their pass/fail is the deterministic gate's to report, not this judgment review's.

## Recommended lean (a recommendation — the lead decides)

**Accept (merge) — optionally with one trim.** The required revision (concrete spend ceiling) is satisfied cleanly and checkably; write_scope held exactly; every boundary (never-captures, no code, `disable-model-invocation`, fenced fast-capture, deferred optional edit) is intact; the tool is represented honestly. This is a clean `should have`-sized patch that matches what was accepted.

The single substantive finding is #1: Step 4 *references* Recipe 9 steps 6–7 **and** recaps the diff rule + output shape inline. It's a faithful recap (nothing weakened), so it's not a correctness problem — but it duplicates text on the one surface the lead asked to stay reference-only, and it's the bit most likely to drift if Recipe 9 changes. Two clean dispositions, lead's call:
- **Accept as-is** if the recap reads as necessary operating mechanics (defensible — the `store.py find` command does need to be in the verb).
- **Accept with a one-line trim** that keeps the *command* in Step 4 but defers the *rule* ("a stub doesn't count") and *output shape* ("tiered worklist + boundary statement") to Recipe 9 by reference, removing the duplicated assertions.

Either way the patch is mergeable; the trim is a hardening of the SSOT discipline, not a gate failure.

---
*No decision was made; the reviewed artifact was not edited.*
