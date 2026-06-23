# sqlite-aggregation — does a derived SQLite lens earn its keep for cohort aggregation?

**Probes** the parked [rung-3 SQLite item](../../BACKLOG.md) on the telehealth cohort — but deliberately
*not* the way the backlog frames it. Throwaway; the FINDINGS feed the backlog item, the scripts don't.

## The reframe (why this isn't a coded-queries redo)

The backlog pins the index trigger to **relations** (discovery) or **time-series** (traction).
[`2026-06-01-coded-queries`](../2026-06-01-coded-queries/FINDINGS.md) already showed the *single-table*
group/filter/count battery stays a one-line `Counter` recipe (whole battery ~1.3s, no index) and the
relation JOIN is **23/24 dangling** — empty. So "is SQLite faster at counting?" is settled: no, and it
doesn't matter at this N.

What changed **after** coded-queries ran: two structured layers landed —
- `offerings.md` (designed 2026-06-03): a **one-to-many** per-SKU roster (the store's first relational shape; hims ≈ 75 rows).
- `telehealth.md` (2026-06-04): the cohort pack — 8 vertical cuts the universal profile can't carry.

Telehealth is the only slice with **three dense tables per company**, and (verified) **all 11
`telehealth.md` companies also have `offerings.md`** — a fully populated JOIN, the exact opposite of the
empty relation graph. That's the untested demand.

## Hypotheses (priors, to test — not foregone)

1. **Trivial single-table aggregation** (count by `pharmacy_model`, the within-cohort filter) — SQLite works
   but adds nothing over the QUERYING.md recipe. *Expect: parity, no win.*
2. **The 3-way JOIN** (`offerings` SKU rows ⋈ `telehealth` cuts ⋈ `companies`) — e.g. "semaglutide SKU count
   by `pharmacy_model`", "who sells compounded GLP-1 *and* leads men-first" — is the first class that's
   genuinely error-prone by hand (mentally joining a ~150-row SKU table to a cohort cut). *Expect: the real
   value, if any, is here — expressiveness, not speed.*
3. **Price magnitude aggregation** (`AVG`/`MIN`/`ORDER BY` price for a molecule) — blocked upstream: price is
   a verbatim string by design, units fragment (`/mo` vs `per use` vs first-month promo vs membership-stacked
   `partial`). *Expect: SQLite can hold a best-effort `price_num`, but it's lossy/wrong often enough to prove
   the store's verbatim-only line right.*

## Method

- `build_db.py` — parse `store/*/profile.md` + `*/telehealth.md` + `*/offerings.md` frontmatter/rosters into
  3 SQLite tables, keyed on slug. Roster parse is **header-keyed** (eden-health adds `Form`/`Category` cols —
  position-based parsing breaks). Adds two derived, deliberately-lossy columns to probe the wall: `molecule`
  (lead token of the `What` cell) and `price_num`/`price_unit` (first `$`-figure + cadence).
- `battery.py` — runs the questions across all three hypotheses, **times each**, and pairs the headline JOIN
  with a pure-Python baseline (no DB) to isolate whether SQLite buys speed (it shouldn't at this N) or only
  expressiveness.

## The rubric (inherited from coded-queries)

A query earns code when it's *(a)* error-prone or *(b)* silently-wrong by hand. coded-queries graduated such
queries into **plain `scripts/store.py` functions, not a database** — so the bar here is sharper: does the
JOIN surface earn *SQLite specifically* (ad-hoc SQL over joined tables) over one more `store.py` function?
And: markdown stays source-of-truth — any DB is a regenerable lens that inherits a build + staleness cost.

## Follow-up artifacts (2026-06-04)

- **`telehealth_full` view + offerings aggregates** (in `build_db.py`) — the joined surface: every profile
  field + 8 cohort cuts + 9 per-company offerings aggregates (`sku_count`, visibility counts, `glp1_skus`, a
  fenced published-`/mo` price band). `mo_price` magnitude is fenced on purpose (see CAVEATS #2).
- **`audit_completeness.py`** — reads each telehealth `offerings.md`'s completeness self-report (no Firecrawl)
  to find where the roster likely *understates* the catalog. Born from the Ro.co enumeration trap (FINDINGS
  follow-up): `sku_count` conflates "small catalog" with "capture stopped early."
- **`CAVEATS.md`** — usage guidelines for the lens. The enumeration trap is #1. Read before trusting a number.
