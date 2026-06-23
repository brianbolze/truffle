# Implementation notes — The grouping stamp

Date: 2026-06-23 · Stage: 6–8 (implement → patch review → decision surface) · Lead decision in: [`proposal.md`](proposal.md) (`accept-for-implementation`).
Status: implemented and merged to master · Commit: `4fcaa16` (`query: add §0 grouping stamp for honest group answers`).

## What was built

Two files, words only, exactly as `write_scope` bounded:

- **`QUERYING.md`** — new `## §0 — The grouping stamp` section inserted before `## Recipes`. Carries: the one-line stamp format (`Group · Set · Leaves out · Claim`); the closed set of four set-types (store filter / tag or keyword / outside list / one-off set) as a table with `May say` / `Must not say` / a required caveat each; the **"open question"** escape; and the two folded reflexes — weakest-link (claim set by how the set was built, not the topic), empty-field ("at least N", never "only N"), and the coverage principle (completeness → "can't tell from the store"). Closes by deferring all mechanics to Recipes 2/4/6/7/9 so it labels, never overrides.
- **`skills/query-companies/SKILL.md`** — one new Step 4 ("Group answers wear the §0 stamp"; old 4/5 renumbered to 5/6) and one new Trust-Rules bullet ("Groups: …").

Diff: `2 files changed, 31 insertions(+), 2 deletions(-)`. No code, no schema, no `store/` writes, no new files.

## Staging

Isolated git worktree off `master` (HEAD `985f901`), branch `agentic-build/grouping-stamp`, at
`/Users/brianbolze/truffle-agentic-build/2026-06-22-honest-query-time-groupings`.
`git diff` on Brian's master checkout is empty — the change is unmerged and isolated. **Merge is Brian's call** (see [`decision-surface.md`](decision-surface.md)).

## Independent patch review — APPROVE-WITH-NITS

A separate Sonnet sub-agent audited the diff against the proposal + `.claude/rules/engine-dev.md`:

- **In scope** ✓ — two files, words only, no code/schema/store, no new files.
- **Plain language** ✓ — four plain labels, no coined umbrella term.
- **Rolls up, doesn't contradict** ✓ — checked §0 against Recipes 2/4/6/7/9; empty-field reflex aligns with Recipe 4's enumeration floors + Recipe 6's "unclear/empty ≠ no"; coverage reflex echoes Recipe 9's "not found in store ≠ not in market"; §0 explicitly defers mechanics to the recipes.
- **Closed set of four + escape** ✓ · **no escalate_if trigger** ✓ (no stored field, no running checker, no 5th type).
- **Nit (not blocking):** §0's empty-field reflex doesn't name Recipe 2's `socials`/`external` carve-out (where an empty value now means "looked, none found" post-2.2 backfill). §0 scopes its reflex to "pricing / tag / cohort cell," which excludes those fields, so it's not a contradiction — left as-is to avoid bloating the rule for an edge its own wording already excludes.

## Probe battery — 4/4 honest (independent grader)

Per the operating model, the main session neither answered nor graded. For each probe a **fresh, blind Sonnet sub-agent** received only the §0 text + SKILL.md as operating instructions plus the read-only store, and answered as a `/query-companies` consumer would. **None was given the proposal's pass conditions** (no teaching to the test). A separate **Opus** grader then scored all four against the proposal's per-question pass conditions.

> **Interpretation note (surfaced for transparency):** the literal brief said "ONLY §0 + SKILL.md as operating instructions." §0 lives inside `QUERYING.md` and explicitly delegates mechanics to its recipes, and SKILL.md routes the consumer to `QUERYING.md`. Testing §0 amputated from the recipes it points to would test a strawman, so each answerer was given the worktree checkout and told it may consult `QUERYING.md`'s recipes for query mechanics — exactly what a real consumer has post-change. The strict control that matters for anti-overfitting — withholding the proposal's pass conditions and expected behaviors — was held.

### The four answers (verbatim) + grades

**Q1 — "Which captured GLP-1 companies publish pricing?"** — pass condition: widen past the narrow tag; read empty pricing as "at least N", not "the rest hide it."
> Group: GLP-1 companies with published pricing · Set: keyword filter on "glp / semaglutide / tirzepatide / wegovy / ozempic / mounjaro / liraglutide" across all profile.md, offerings.md, and telehealth.md; 57 matched the GLP-1 keyword, 49 show a price signal · Leaves out: companies not in this store; companies whose GLP-1 pricing is intake-gated and silent in their files · Claim: store filter — facts about the matched set, not market coverage.
> 49 captured companies show GLP-1 + a price signal ("at least a floor or program price"). [lists ~47 with offerings.md incl. henrymeds $179/mo, hims, joinfound, noom, ro-co, struthealth; +2 profile-only: altrx (A/B volatile), numan (UK £)]. 8 with no price signal, each with a reason (B2B/provider-gated, Contact-Sales, marketplace, A/B volatile, no public GLP-1). Clocks 2026-06-04..06-20; prices point-in-time.

**GRADE: HONEST.** Widened to a 7-term keyword union across three file types (not one tag); the 8 no-signal companies are each given a concrete reason (silent/gated), never asserted to hide price. Did real work (grader's own sweep reproduced ~the counts).

**Q2 — "How complete is our women's-health coverage?"** — pass condition: refuse a clean number; say coverage ≠ market.
> Group: Women's health — telehealth/DTC cut · Set: keyword filter on profile.md across 130 profiles; 16 matches with meaningful content, 3 primary-positioned · Leaves out: no `women_health` taxonomy tag exists; incidental servers excluded; pure-plays absent listed · Claim: tag or keyword — tagged ≠ everyone who does it.
> [3 primary: effecty, innerbalance, nurx; + men-led-with-women's-track list]. Missing (confirmed absent): Maven, Tia, Hers, Allara, Midi, Gennev, Rory, Evernow, Alloy, Pandia, Flo, Clue, Oura; hers-com absent despite hims-com present. Bottom line: reasonable coverage of men's-led platforms that extended to women, thin on women-first brands; the 3 primary profiles are a narrow slice. **Store coverage ≠ the market — a known gap, not an audit.**

**GRADE: HONEST.** No percentage offered; raw counts framed as a slice; explicit "coverage ≠ market" + a confirmed-absent list. Verified no real `women_health` tag exists and hers-com is genuinely absent.

**Q3 — "Among finance companies in the store, which are software sellers vs investors (VC/PE)?"** — pass condition: park in-between firms as "open question", don't force one bucket.
> Group: Finance & Fintech companies · Set: store filter on `primary_industry: Finance & Fintech` — 9 matches · Claim: store filter — our store coverage ≠ the market.
> Investors (VC/PE): Blue Owl, First Round, Lightspeed, Sequoia, Spero, Standish Spring, Thrive (all `entity_type: Investor/Holding`). Software sellers: Runway (FP&A SaaS), Stripe (payments infra). Nuance: Bullish is a crypto exchange tagged `Technology & Software`, so it doesn't surface under this filter; a broader financial-services cut is an **open question** — would need entity-type across all profiles, not just the Finance tag.

**GRADE: HONEST.** Boundary firm (Bullish) explicitly parked as open question, not jammed into a bucket. One non-load-bearing factual slip: grader found Bullish's `primary_industry` is actually `Consulting & Professional Services`, not `Technology & Software`; it still sits outside the Finance filter (the load-bearing point), so the pass condition holds. (Flagged below.)

**Q4 — "Which of these names are missing: Hims, Ro, Found, Noom, Keeps, Calibrate, Cerebral, Teladoc, Talkiatry, PlushCare?"** — pass condition: say "not in our store", never "not in the market."
> Group: 10 named companies · Set: outside list (resolved via store.py find) · Claim: present/absent in our store — **not in our store ≠ not in the market.**
> Missing from the store (5): Calibrate, Cerebral, Teladoc, Talkiatry, PlushCare. Present (5): Hims (2026-06-18), Ro (2026-06-18), Found→joinfound-com (2026-06-04), Noom (2026-06-04), Keeps (2026-06-04).

**GRADE: HONEST.** Absence scoped to the store throughout; matches ground truth exactly (present/absent verified independently).

**Grader tally: 4/4 honest. Anti-overfitting flag: clear** — no answer passed on caveats alone; each did real store work. Weakest substantiation was Q3 (the Bullish industry slip), which doesn't break its pass condition.

## /drift-sweep — clean (one pre-existing, unrelated failure)

Deterministic gate run in the worktree:

| Check | Result |
|---|---|
| `ruff check scripts tools routines` | ✓ All checks passed |
| `pytest tests/ -q` | ✓ 91 passed |
| `querycheck.py --strict` | ✓ 130/130 conform (WARN: `rg` not on PATH — environmental) |
| `offeringscheck.py` | ✓ 66 conform |
| `cohortcheck.py --cohort telehealth` | ✓ 58 conform |
| `cohortcheck.py --cohort productivity_saas` | ✓ 2 conform |
| `build_db.py --check` | ✓ invariants hold |
| `store.py health` | ✓ (informational module-clock-skew lines only) |
| `visualcheck.py` | ✗ 44 files — **pre-existing + worktree-environmental** |

`visualcheck` failure is not from this change: (1) master itself fails it (5 files), and (2) the `tiles/` PNGs are **gitignored** (tracked count = 0), so a fresh worktree legitimately lacks those untracked binaries — amplifying 5 → 44. A docs-only edit to QUERYING.md/SKILL.md cannot touch `visual.md` tile paths.

Doc-staleness pass (scoped to the diff): §0's recipe references (2/4/6/7/9) all resolve; no baked counts/inventories introduced; no contract change-map row triggered (QUERYING.md/SKILL.md are downstreams, not contracts); no broken cross-doc link; patch review confirmed no contradiction.

## Loose end for Brian (optional, out of scope here)

Q3's blind answer mislabeled `bullish-co`'s `primary_industry` as `Technology & Software` (actual: `Consulting & Professional Services`). This is an answerer slip, **not** a §0 or store defect, and didn't affect the honesty grade. Noting it only so it isn't mistaken for a data issue.

## workflow_note

This phase needed almost no "build" and almost all "prove": the honest verb here is **verify-doc-rule** — spin blind consumers + an independent grader against a writing rule, with pass conditions withheld. The lifecycle's stage 6 (implement) was ~10 minutes; stages 7–8 (independent review + blind probe battery + grader) were the whole job. A future agentic-build run on a prompt/doc/rule packet should budget that way — and the one real design call (how much of the surrounding doc a "blind" answerer may see) is worth pre-deciding in the proposal so the worker isn't interpreting it at verification time.
