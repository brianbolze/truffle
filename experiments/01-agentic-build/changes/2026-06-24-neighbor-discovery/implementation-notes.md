# Implementation Notes: `/discover-neighbors` verb

Date: 2026-06-24
Status: REJECTED & unwound — 2026-06-24 (see lead-decision.md → FINAL DECISION)
Decision: `lead-decision.md` (accept with revision)

## What shipped

- **New verb:** `skills/discover-neighbors/SKILL.md` — a thin playbook (~40 lines): purpose, spend ceiling, 5 link-out steps. **No new code.**
- **Pointer — `QUERYING.md`:** one line after Recipe 9 routing "companies not in the store" to the verb (the read surface gains a pointer, not a recipe).
- **Pointer — `tools/exa_search.md`:** one "consumer verb" back-link.

## How it honored the revision + constraints

- **Concrete spend ceiling (required revision):** SKILL.md names ≤3 query angles, `--num-results 25`, stop-and-ask before a 4th angle / any re-run. Checkable, not posture.
- **Light to start:** thinnest viable SKILL.md; `disable-model-invocation: true` so a paid verb never auto-fires; the optional `query-companies` hand-off edit was deferred.
- **Single source of truth (link out, don't duplicate):** tool mechanics + recall caveats → `exa_search.md`; store-diff + propose-don't-write output → Recipe 9 steps 6–7; diff command → `store.py`. SKILL.md adds only the verb framing, spend ceiling, and sequence.
- **Scope held:** never captures, no store writes, no new tool/script/Signal/category, no scheduled job; fast-capture arm fenced to a future packet.

## Files touched (vs write_scope)

- `skills/discover-neighbors/SKILL.md` (new)
- `QUERYING.md` (one pointer line)
- `tools/exa_search.md` (one pointer line)
- Not touched: `store/`, tool code, schemas, prompts, SIGNALS paths, `query-companies`.

## Verification — gate passed

- `git diff --check` (QUERYING.md, exa_search.md) → clean.
- `python3 scripts/querycheck.py --strict` (QUERYING.md touched) → OK (structure + closed sets conform).
- Independent **change-mode review** → **accept (merge)**; see `packet-review.md`. Spend ceiling concrete + checkable; write_scope held exactly; never-captures / no-new-code boundaries intact; caveats faithful to source.
- One seam flagged (Step 4 referenced Recipe 9 but recapped its diff rule + output shape inline) → **trim applied**: Step 4 now defers the rule + worklist/boundary shape to Recipe 9 by reference and keeps only the `store.py find` command + the verb-specific cross-angle note.

## UNWOUND — 2026-06-24

This implementation was **rejected and reverted**; nothing reached the committed engine. See `lead-decision.md` → FINAL DECISION for why.

- **Deleted:** `skills/discover-neighbors/` (the verb).
- **Reverted to HEAD:** `QUERYING.md`, `tools/exa_search.md` (both pointer lines removed via `git checkout`).
- **Verified:** `git diff` clean on those paths; `skills/discover-neighbors` gone; `querycheck --strict` OK.
- **Kept** (records/learning, not engine changes): this packet's docs, the session's observations, and the `skills-keep-light-link-out` memory (a standing preference, independent of this packet).
