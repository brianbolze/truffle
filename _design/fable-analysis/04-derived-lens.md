# The derived lens — corpus-wide, fenced, honest about staleness

*Proposal (prototyping-stage). All changes land in `scripts/build_db.py` + ~a paragraph of QUERYING Recipe 7. Serves both first-class consumers: Brian in Beekeeper and agents with many-pivot questions. Markdown stays source of truth; the db stays regenerable + gitignored.*

## 1. Scope: corpus-wide tables, cohort-only ranking

**Recommended: corpus-wide tables + per-cohort ranking views.** The current "telehealth-scoped" line is half-abandoned in practice (`companies` already carries every profile) and now silently lossy: **six rosters are invisible to the lens** (airbnb, clerky, ford, notion, stripe, warbyparker) — a db-based "who sells X" already misses files grep finds. The Recipe-7 trigger ("generalizes when a second cohort earns it") fired, just not as predicted: it was dropped rows + stubs, not a second cohort.

- `offerings` un-gates to **all** rosters; `companies` stays as is; `telehealth` / `telehealth_full` unchanged. Future cohorts get a `<cohort>_full` view only when a pack contract exists (today: none).
- **New `coverage` table** — one row per store *folder*: `has_profile / has_offerings / has_telehealth`, the three clocks, `enumeration`. This is the capture-status manifest the live consumer asked for, the stub-visibility fix, and the scout's dedupe ("in store but not captured" becomes one WHERE clause). It replaces the db-half of `store.py health` — if both exist, `health` prints what `coverage` holds, one derivation.
- **Ranking stays cohort-gated** *(adversarial catch — the original draft contradicted itself here)*: `offerings_stats` must be **gated to cohort membership**, or `ORDER BY sku_count` over a corpus-wide GROUP BY is exactly the Ford-vs-Hims league table the design rejects. Cohort-specific aggregates (`glp1_skus`) live only in the cohort view — not as permanent telehealth noise on Ford/Notion/Stripe rows.
- **Extend the join-density `--check` assert to all rosters** — un-gating without it reproduces the rugiet-class silent drop (a ford roster parsing to zero rows, nothing telling you) that motivated this design.

**The fence, restated honestly** *(adversary verified the old wording is now false)*: with corpus-wide rows, a cross-type `AVG` is no longer "structurally impossible" — SQLite coerces leading-digit text (`'2.9% + 30c'` → 2.9; `AVG(price_verbatim)` returns a confident-looking float). The real fence is: **(a)** no numeric price column may exist in any table (`--check`-enforced, kept); **(b)** ranking surfaces (count/visibility ORDER BYs) exist only inside `<cohort>_full` views — the corpus `offerings` table is for membership/lookup (`LIKE`), never league tables. Say "no sortable number exists; coercion yields visible garbage, not plausible answers" — never "impossible."

## 2. Placement: a defined split — bless what the consumer already did

- **Engine owns** the faithful, fenced corpus lens (`build_db.py` → `store.db`) and the **importable parsers** (`offeringscheck.parse_roster`, the frontmatter reader).
- **Projects own judgment lenses** built on those parsers — canonical molecule, normalized price, enrichment. That's not a workaround to absorb; it's the architecture: cartography kept those columns honest only via a judge→verify→repair pipeline with per-value trace. Absorbing it crosses the State/Judgments line and re-grows Doro. Cartography (`build_base.py` already imports `parse_roster`) is the **reference implementation**; one sentence in Recipe 7 records the split.
- **Do not ship a JSON-export verb yet** — one consumer is a rule of one. Trigger: a *second* project rebuilds the spine; then graduate a `build_db.py --json` packets flag and name `build_base.py`'s spine-half as what it replaces.

## 3. Staleness: `_meta` in the db + rebuild-before-read as the only agent rule

- **`_meta`**: a one-row table written at build — `built_at`, row counts — plus a `days_old` view (`julianday('now') − julianday(built_at)`) so the staleness number recomputes on every open, **plus caveat rows** (`"counts are floors — read catalog_breadth"`, `"no price number exists — price_verbatim only"`). The GUI user never reads QUERYING.md; **the fences must live in the artifact.**
- **The agent convention** (one Recipe 7 line): **rebuild before you read** — full build + check ≈ 0.5s at current N, cheaper than any freshness check. This replaces hooks, wrappers, and drift detectors.
- **Rejected:** rebuild-on-capture hooks — the store has many writers (capture skills, backfills, manual edits, project sessions); a hook catches some and then *lies*, because "built today" reads fresh after an un-hooked edit. Partial freshness automation is worse than none. **Also cut** *(adversary)*: the mtime-fingerprint "check instead of rebuild" escape hatch — one staleness mechanism, not one-and-a-half, and iCloud mtimes are unreliable anyway.
- **The Beekeeper inode gotcha** (one Recipe 7 sentence): a rebuild replaces the file while an open GUI connection keeps reading the deleted inode. The live `days_old` view is what saves the human — the stale connection's `built_at` stays old, so the number visibly grows. Reconnect after rebuild.

## 4. The human consumer: four cheap Beekeeper moves

1. `_meta` sorts first in an alphabetical table list (the underscore) — staleness + caveats are the first thing seen.
2. **Stable path is the contract**: `scripts/_out/store.db`, declared in Recipe 7; never dated filenames.
3. **Caveats ride in column adjacency, not renames**: `catalog_breadth` rendering `≥N (floor)` beside `sku_count` is the proven pattern. Don't rename `sku_count` → `sku_count_floor` — floor-ness is conditional on `enumeration`; a static name overstates.
4. Naming convention, stated once: bare nouns = corpus tables (`companies`, `offerings`, `coverage`); `<cohort>_full` = the ranked, fenced views.

## Surface accounting

**Adds:** `coverage` + `_meta` (with days_old view) · un-gates one glob · extends one assert · ~a paragraph of Recipe 7.
**Deletes/replaces:** the stray-rows `--check` assert · the "telehealth-scoped today" Recipe 7 line · the db-half of `store.py health` · every staleness mechanism heavier than the rebuild convention.
**Explicitly not built:** JSON export (rule of two) · rebuild hooks · speculative cohort views · judgment columns · corpus-wide ranking · the store-scan term-inventory utility and the logo asset-path contract (each observed once — named here so deferral is visible, with the obvious trigger: a second consumer).

## Adversarial review — what changed

Verdict *needs-changes*; skeleton conceded ("best-formed proposal the engine has seen… the discipline isn't applied uniformly"). Folded in: `offerings_stats` cohort-gated (the draft re-shipped the footgun it rejected) · "structurally impossible" softened to the two-part fence (the adversary *ran* `AVG(price_verbatim)` and got 0.967) · join-density assert extended corpus-wide · fingerprint escape hatch cut · `_meta` shape pinned to one-row-table + view · the QUERYING number-strip cross-referenced to [doc 02](02-trust-surface.md) rather than left to chance · declined frictions named in Surface accounting. Unverified residue, flagged as such: Beekeeper's actual sort order for `_meta`, and the Recipe-7 edit growing toward a paragraph — watch that Recipe 7 doesn't become the new bloat point.
