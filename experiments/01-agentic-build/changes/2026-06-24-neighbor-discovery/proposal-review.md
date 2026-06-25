# Proposal Review: `/discover-neighbors` verb

**Mode**: proposal (plan-before-code). Boundary intact — packet holds only `proposal.md`, `Status: proposed`, no receipt or implementation-notes. Clean proposal-mode review.
**Reviewer**: independent (did not author the proposal).
**Date**: 2026-06-24

Findings first, most important first. Then a recommended lean — a recommendation, not a decision.

## Findings

### 1. The load-bearing claims are honest — I checked each against source, not memory
All five things the proposal leans on hold up under reading:
- **`exa_search.py` representation is faithful.** The proposal's framing — "discovery feeder, low known-set recall, net-new long-tail bias, paid/metered, caller-side dedup" — matches the docstring verbatim (lines 11-14: "recall of a *curated/known* set is low (a Hone-description search recovered 1/16…), so corroborate downstream; it does not replace a cross-shop read"; line 95: folding mirrors + cross-query dedup is "caller logic… kept out on purpose"; line 183: `cost.usd` from `costDollars.total`). No overclaim, no laundering of recall into a census.
- **Recipe 9 reuse is real, not hand-wave.** Recipe 9 step 6 ("Diff against the profiled store… `head not in store`… say 'not found in the store'") and step 7 ("boundary statement and proposed candidates only… do not auto-capture, mutate `store/`, persist… create a category object") are exactly the diff/output discipline the proposal defers to. The deferral is precise — it names *steps 6 and 7 only*, which is correct (see finding 3).
- **The `serp_match.py` citation is accurate, verbatim.** Lines 11-12: "Do not copy this file into `exa_match.py`, `wayback_match.py`, etc. That wrapper-per-source shape would clutter `tools/` and blur the capture/judgment boundary." The proposal's `escalate_if (a)` cites this correctly as the reason for no new tool.
- **`/query-companies` really is read-only/never-spends by contract.** Stated twice in its SKILL.md ("Read-only: never scrapes, never spends"). The proposal's central category argument — a paid, outward-reaching verb does not belong on that surface — rests on a real contract line, not a convenience.
- **BACKLOG:40 confirms the park, the not-salvageable `exa_similar` ruling, and the known-brand `/vs` carve-out.** All three Constraints/Non-Goals statements trace to BACKLOG:40 text. `exa_search.md` (a pointer target) exists; `querycheck.py` and `store.py` (named in acceptance) exist; no `discover-neighbors`/`find-neighbors` name collides anywhere in the repo.

This is the discipline the reviewer-context asks for ("check before asserting") and the proposal earns it.

### 2. Option 1 (verb) over Option 2 (recipe) is the right call — category, not rationalization
I tested whether the proposer is rationalizing the more-surface option. They aren't. The discriminator they name — *this work spends and reaches outward, which is the opposite of QUERYING's read-only contract* — is the correct axis, and it's load-bearing independent of byte-count. Putting a paid Exa pattern into the read book would either (a) silently break `/query-companies`' "never spends" contract for any agent that routes through it, or (b) require a carve-out caveat that's louder than the recipe. Both are worse than a one-line pointer. Net `QUERYING.md` bloat under Option 1 is genuinely *lower*. The "verbs over services" engine principle (engine-dev.md) backs the verb shape. This is a real argument, not a post-hoc justification for more surface.

### 3. The no-new-code claim is credible — the dedup/diff is genuinely prose, not code in disguise
The stress-test the brief asks for: is the caller-side dedup + store-diff really code wearing a SKILL.md costume? No. Each step the playbook describes is a one-shot shell call or a by-hand judgment an agent already does in market-read runs:
- dedup = "fold `www.`/`api.`/`en.` to apex, dedup across queries" — `_domain_of` already half-does this (lowercases, strips `www.`); the residual is a few-line judgment over a handful of domains, the same caller work Recipe 9 step 4 ("clean before set math") expects by hand.
- store-diff = `store.py find <domain>` per candidate + "profile.md exists, stub doesn't count" — a loop an agent runs inline, identical to Recipe 9 step 1/6.
The volume is bounded (a handful of queries → tens of domains), so by-hand is not just feasible but *cheaper* than a tool. Option 3 (`exa_match.py`/`_match.py`) is correctly demoted to escalation-only. **Caveat on absence:** I'm judging this from the *sketch*; "no code" is only true if the implementer holds the line. The proposal's own `escalate_if (a)` is the guardrail, and it's explicit. The risk isn't the plan — it's drift during the build.

### 4. The spend cap is honest but soft on one edge — "a handful of queries" has no number
`spend_stop` is the right shape: paid-per-query, opt-in, bounded, no standing/scheduled run, **never captures** (Firecrawl stays on `/research-company`). All true and verifiable. The boundary that matters most — *output is a worklist, capture is a separate approved path* — is clean and matches `exa_search.py`'s print-only contract (no store write possible from the tool itself).

The one soft edge: **"a handful of queries per invocation" is the only spend ceiling, and it's a word, not a number.** `exa_search` is `numResults`-billed per call and the playbook tells the agent to "vary the description across 2-3 angles" — so spend is (angles × `num_results`), and nothing in the cap names a `--num-results` ceiling or a hard query count. "A handful" is honest as posture but not *checkable* against a number at review time. This is consistent with lead-context's "spend_stop is posture, not accounting ceremony," so it's not a blocker — but if the implementer wants the acceptance check to be verifiable, the SKILL.md should state a concrete soft ceiling (e.g. "≤3 queries, default `num_results`, stop and ask beyond that"). Flagging so the lead decides whether posture-only is enough for a paid API.

### 5. Nothing here is improperly additive — but confirm the one retire-or-keep question
The reviewer-context flags "additive-only changes (what does it replace?)." This verb is genuinely net-new capability (there's no existing "find companies not in the store" verb), so it's not displacing anything — that's legitimate, not a smell. The honest accounting: it adds one SKILL.md + three pointer lines and retires nothing, because the capability didn't exist. Recipe 9 is *not* retired or weakened — the proposal explicitly reuses it by reference and the "Option 2 rejected" reasoning keeps the read book clean. Good. The only open additive question is cosmetic (finding 7).

### 6. Acceptance checks are mostly checkable before merge — with two caveats
Checks (a)-(e) are manual-review assertions about SKILL.md content; all are inspectable in the artifact at review time. The mechanical checks are real: `git status` clean (no store mutation), `git diff --check`, `querycheck.py --strict` if `QUERYING.md` is touched (script exists). Two caveats:
- **The "dry-run invocation produces a worklist + mutates nothing" check spends real money** — a dry run of a paid-API skill is a live Exa call. That's fine and probably necessary to prove the skill works, but it means "acceptance" itself has a (small) spend, which the packet should acknowledge so it isn't a surprise. Minor.
- **"Reuses Recipe 9 by reference, not by restating or weakening it" (check b)** is the subtlest check and the easiest to fail silently — an implementer paraphrasing Recipe 9 steps 6-7 into the SKILL.md *is* restating, which both bloats and risks drift when Recipe 9 changes. The reviewer of the *change* should diff the SKILL.md against Recipe 9 for paraphrase, not just confirm a pointer exists. Worth naming now so the change-mode review knows to look.

### 7. Scope-creep watch: the fenced fast-capture arm is correctly fenced — hold the line
The `--capture-stubs` / fast-capture arm is named three times (Non-Goals, Options, Review Notes) and routed to `escalate_if (d)` as its own future packet. That's the right disposition — it's the one place this verb could quietly grow store-write or capture-spend authority, and the proposal fences it explicitly rather than smuggling a hook. No standing/scheduled job (escalate_if e). No Signal/category persistence (escalate_if c). The fencing is thorough; the only residual risk is implementer discipline, same as finding 3. The open naming question (`/discover-neighbors` vs `/find-neighbors`) and the optional `query-companies` hand-off line are genuinely minor — lead's call, not a blocker.

### What this review could not see
- I reviewed the *plan*, not a SKILL.md (none exists yet). Findings 3, 6b, and 7 all reduce to "the plan is sound **if** the implementer holds the no-code / reuse-by-reference / no-capture lines." Those are change-mode checks, not provable now.
- I did not run `exa_search.py` live, so I'm trusting the docstring's recall/cost claims (which are themselves probe-backed per the cited 2026-06-20 write-up) rather than re-deriving them.

## Recommended lean (a recommendation — the lead decides)

**Accept, with one revision before/at implementation.** The category argument is correct, the tool is represented honestly, the Recipe 9 reuse is real, and the no-code claim is credible. The single substantive gap is finding 4: **the spend cap is posture-only with no number.** Recommend the lead require the SKILL.md to name a concrete soft ceiling (query count + `num_results` default, with "stop and ask" beyond it) so the paid-API spend boundary is *checkable*, not just *stated* — given it's a paid API, "verifiable" is worth the one line. Everything else (naming, the optional hand-off, the dry-run-spends note) is minor and can ride into implementation. The fenced fast-capture arm should stay fenced; the change-mode review should diff the SKILL.md against Recipe 9 to catch paraphrase-instead-of-reference (finding 6b).

This is a clean `should have`-sized packet at honest `medium` risk; the risk lives entirely in implementer discipline (no code / no capture / reuse-by-reference), which the `escalate_if` lines already guard.

---
*No decision was made; the reviewed artifact was not edited.*
