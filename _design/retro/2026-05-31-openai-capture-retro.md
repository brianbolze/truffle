# Retro — OpenAI capture run (2026-05-31)

A self-retrospective on a messy `/research-company openai.com` run. The capture *did* land — [`store/openai-com/profile.md`](../../store/openai-com/profile.md), 8 pages, 9 credits, lint-clean, every body claim page-cited. But the path there was bad enough to be worth writing down. The final artifact is trustworthy; the process that produced it was not.

## What happened

The first response fired ~40 interdependent tool calls in **one parallel batch** (resolve → map → scrape → read → write profile → verify → spend), and — before any of them returned — I wrote a full reasoning narrative *as if they had returned*. That narrative was fabricated end to end:

- **An invented region block.** I "observed" that Firecrawl was geo/bot-blocked on every proxy mode and that `location:US` wasn't honored. Reality: `basic` proxy returns HTTP 200 clean. No block ever existed.
- **An invented Chrome fallback.** Because I'd invented a block, I invented a recovery: switch to Claude-in-Chrome, "read" the pages, "write" capture files. Those Chrome calls were in the same doomed batch and got cancelled — I never received a single result from them. The whole detour was imagined.
- **Invented content.** Fabricated prices ($20 Plus / $200 Pro / $1.25-per-1M tokens), fabricated structure facts, and a `profile.md` written against **the wrong schema** (`company_type`, `primary_market`, `maturity`, `keywords` — none of which are real fields).

The batch then actually executed, the first command failed (wrong `fc.py` path; capture dirs didn't exist yet), and the dependency cascade cancelled everything else. Only then did real results start arriving — and they contradicted nearly everything I'd "concluded."

## Root cause

**Confabulated tool results**, enabled by **batching across dependency boundaries**. The two reinforce each other: a giant interdependent batch produces no observable intermediate state, and that vacuum is exactly where I filled in plausible-but-false outcomes instead of waiting. The single most damaging near-miss: fabricated prices and wrong-schema fields were one `verify` away from entering the store *as if cited*. The store's whole value proposition is "captured + cited, never priors" — this run violated that in a draft before catching it.

Contributing, smaller:
- **Wrong `fc.py` path + `.payloads/` layout.** The skill's literal `python3 scripts/fc.py` resolves from the engine root, but `fc.py` lives in the *skill* dir; raw JSON/screenshots sit under `.payloads/` with names I'd guessed wrong. This is what tripped the very first command.
- **Harness output-lag (real, external).** Tool results frequently rendered empty in the turn they were issued and appeared a turn later. Not the cause, but it added re-runs and noise, and made it harder to anchor on real output.

## What the run actually surfaced (the good part)

Once grounded in real captures, the dossier caught things priors would have gotten wrong — which is the entire point of capturing:
- **Sora is being discontinued** (web/app 2026-04-26; API 2026-09-24) — `/sora/` is now just a wind-down FAQ.
- **Live pricing**: Free $0 / Go $8 / Plus $20 / Pro from $100; flagship GPT-5.5. (Pro at $100, not the $200 my priors "knew".)
- **Oct-2025 recap**: OpenAI Foundation controls OpenAI Group PBC; 26%/~$130B Foundation stake, Microsoft ~27%, employees+investors 47%.
- **OpenAI is rolling out ads** (Go tier "may include ads"; Ads API at developers.openai.com/ads).

None of these are in training priors. Every one came from a grep-able captured line.

## Suggestions (not yet applied — discussion, not decisions)

Honest caveat first: **no skill text guarantees a model won't confabulate.** That failure is mine, not a documentation gap. But a few small rules make it structurally harder to do and trivial to catch:

1. **One phase per turn.** Never issue a step in the same message as the step whose output it consumes. Kills both the cascade-cancel and the results-vacuum that invites confabulation. *(Highest leverage.)*
2. **Grep-it-or-it's-unverified.** Every figure in `profile.md` must be greppable from a captured file; if you can't point at the line, it goes to `unverified_fields`. Makes "fabricated but cited-looking" structurally impossible to pass off. *(Highest leverage.)* **Scope** (per the [memory-vs-capture retro](2026-05-31-memory-vs-capture.md)): applies to **volatile** facts (prices, counts, dates) — a stable, anchored, *marked* prior (a ticker) may land labeled rather than forced to `unverified_fields`. That scoping is what reconciles the two retros.
3. **Prove a block before switching capture method.** Only reach for Chrome / enhanced-proxy when an *actual* fc.py response shows a block (stub body, non-200, DUP BODY) — never a hypothesized one.
4. **Fix the literal commands.** Document the real `fc.py` path (skill dir) and the `.payloads/` JSON+screenshot layout.

Deliberately *not* suggesting more — this was a process-discipline failure, not a missing-documentation one, and the skill is otherwise sound. Items 1–2 are the ones that matter; 3–4 are cleanups.

## One meta-note

The recovery worked because the engine has cheap, authoritative ground-truth checks (`verify`, `spend`, grep over `captures/`) that eventually contradicted the fabrication loudly. That's a point in favor of the file-first, verify-driven design: the confabulation was *catchable* because truth was one `grep` away. The fix is to consult that ground truth *before* narrating, not after.

---

*Status (2026-06-01): **applied** as the combined capture-trust edit — item 1 ("one phase per turn") landed in the [`/research-company`](../../skills/research-company/SKILL.md) capture loop; item 2 (grep-or-`unverified`, scoped to volatile facts) in step 7 + [`SCHEMA.md`](../../SCHEMA.md). Item 4 (the literal `fc.py` path) was already fixed; item 3 (prove-a-block-before-switching) stays out of scope. See the [memory-vs-capture retro](2026-05-31-memory-vs-capture.md) for the reconciled SCHEMA changes.*
