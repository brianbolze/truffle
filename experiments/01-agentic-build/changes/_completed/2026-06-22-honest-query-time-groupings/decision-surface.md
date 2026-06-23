# Decision surface — The grouping stamp

**Outcome: merged to master 2026-06-23 (commit `4fcaa16`).** Brian approved; the body below is the pre-merge decision snapshot.

**Problem.** When Truffle answers about a *group* of companies, the answer can look more solid than it is (store coverage read as market coverage; an empty field read as "they don't"). The approved fix is a writing rule, no code.

**Decision needed.** Merge the two-file change to master, hold, or revise.

**Recommendation: merge.** Review and the blind probe battery both came out clean; risk is low and reversible.

**What changed** (2 files, words only, +31/−2):
- `QUERYING.md` — new `§0 — The grouping stamp` before Recipe 1: the `Group · Set · Leaves out · Claim` line, four set-types each with a required caveat, the "open question" escape, and the empty-field + coverage reflexes. Defers mechanics to Recipes 2/4/6/7/9.
- `skills/query-companies/SKILL.md` — one Step + one Trust-Rules bullet.

**Risk:** low. Docs-only; no schema/store/code; no escalate_if trigger fired.

**Checks run:** independent patch review → APPROVE-WITH-NITS (in scope, plain, rolls up without contradiction). Blind probe battery → **4/4 honest** per an independent Opus grader; anti-overfitting flag clear (answerers never saw the pass conditions, each did real store work). `/drift-sweep` gate green — the lone `visualcheck` failure is pre-existing (fails on master too) and worktree-environmental (gitignored tiles), unrelated.

**Surprises / your call:**
1. Change lives in an isolated worktree (`agentic-build/grouping-stamp`); **merging is yours** — nothing touched master.
2. One nit left unfixed by choice: §0 doesn't restate Recipe 2's `socials`/`external` empty-means-found carve-out (its wording already excludes those fields). Fold in or leave.

Detail + verbatim answers: [`implementation-notes.md`](implementation-notes.md).
