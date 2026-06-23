# CAVEATS — using the SQLite lens without getting a confident wrong answer

Read before trusting any number out of `telehealth_full` or the `store.db` lens. The database's whole danger
is that it makes a wrong answer **fast, clean, and confident** — a sorted column *looks* authoritative even
when the underlying fact is a capture artifact. These are the guardrails, ordered by how likely each is to
bite. *(If the SQLite layer ever graduates from this experiment, this folds into [`QUERYING.md`](../../QUERYING.md).)*

## 1. Counts are a FLOOR, not a census — the enumeration trap ⚠️ the big one

`sku_count`, `glp1_skus`, `published_skus` count **what got enumerated**, and `offerings.md` deliberately does
**not** always enumerate the whole catalog — it captures "complete at the *indexed level*" and stops short of
leaf detail (and sometimes whole lines) to spare Firecrawl credits (OFFERINGS.md `portfolio_shape` depth dial
+ Provenance scope). So a low count means **either** "small catalog" **or** "the capture stopped early," and
the DB cannot tell them apart.

> **The proof:** Ro.co sorted dead-last on `sku_count` (8) — but it's a broad multi-line brand; the prior run
> enumerated weight-loss + testosterone only and marked the rest "out of this run's scope." The count
> laundered a *capture-scope decision* into an apparent *fact about the company*.

**Rules:** never rank/compare brands by `sku_count` alone · read every count as "**≥ this, at the captured
depth**" · before trusting a low count, check that brand's Provenance scope (`audit_completeness.py`) · a count
is only comparable across brands captured at the **same depth**.

## 2. Price magnitude does not aggregate — the price wall

No `AVG`/`MIN`/`MAX`/`ORDER BY` on price as a brand statistic. `price_num` is a best-effort *first-`$`* grab and
is **wrong, not just lossy**: a `$50 (consult)` fee parses as the price; first-month teasers (`$34`/`$39`) sort
*below* real recurring prices. Units fragment (`/mo` vs `/use` vs `/yr`). The `mo_price_min/max` band is
published-`/mo`-only and still floor-y — Hims spans **`$15–$958/mo`**, which is exactly why a per-company
average is nonsense. Use `price_verbatim` for truth; normalize by hand only within a single molecule + unit.

## 3. Molecule is page-attested free text — group by `LIKE`, never `GROUP BY`

`GROUP BY molecule` fragments ("testosterone" → 8 buckets: cypionate / "ester not stated" / family-row
descriptions). Use `WHERE what LIKE '%semaglutide%'` for membership (robust, = the QUERYING Recipe 4 grep).
`molecule IS NULL` / "not stated" means **the page was silent**, not "absent." Ambiguous molecules are noisy —
`%testosterone%` catches OTC *supplements* alongside TRT.

## 4. `unclear` / empty ≠ "no"

A blank cohort cut (`pharmacy_model`, `audience`, …) means "looked, couldn't tell" — a sparse platform/lab pack
honestly leaves cuts empty. Never report a within-cohort negative ("none bill insurance") without confirming
the cut was actually determinable. Same for `socials`/`external` (absent = "none found" only post-2.2 backfill).

## 5. Cross-type aggregates are meaningless — and the DB invites them

Don't aggregate price or SKUs across `business_model` types: the corpus-wide `companies`/`offerings` tables span
per-night, `$/mo`, take-rate, AUM-fee. `telehealth_full` is safely intra-cohort by construction; the raw tables
are **not**. One stray `AVG(price_num) ... GROUP BY` over all 73 companies is a confident lie. The friction that
normally protects against this (it's annoying by hand) is exactly what the DB removes.

## 6. It's a derived lens — rebuild it, and watch three clocks

Markdown is source of truth; the DB is regenerable and **stale the moment a capture lands**. Re-run
`build_db.py` before trusting numbers. Freshness has **three** independent stamps: `captured_at` (profile),
`telehealth_captured_at` (cohort pack), and the offerings file's own `captured_at` — a brand can have a fresh
profile and a month-old roster.

---

**What it's genuinely good at** (lean here): filter / group / count on **closed-set categorical** columns — the
8 cohort cuts, `visibility`, `business_model`, `anchor_category` — joined across profile × cohort × offerings.
That's the real win (expressiveness over three tables at once). For anything price-magnitude, molecule-exact,
or completeness-sensitive, drop to the markdown.
