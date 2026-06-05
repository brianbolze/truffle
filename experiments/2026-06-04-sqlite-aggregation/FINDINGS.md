# FINDINGS — sqlite-aggregation

Built a derived SQLite lens (`companies` 66 ⋈ `telehealth` 11 ⋈ `offerings` 555 SKU rows) from the live
markdown and ran a telehealth aggregation battery ([`battery.py`](battery.py)). The verdict is sharper than a
yes/no: **the JOIN demand the backlog never tested is real and dense — but it earns *code*, not a *database*,
and the price wall caps the headline use either way.**

## Verdict: stays parked — but re-point the trigger

The [backlog item](../../BACKLOG.md) pins the SQLite trigger to **relations** (23/24 dangling — empty) or
**traction** (doesn't exist). Both are still absent. The *actual* pull that has appeared is the
**`offerings` one-to-many × the `telehealth` cohort cuts** — and it argues for a **light rung
(`store.py` long-table reader), not SQLite**, until two conditions both hold (below).

## What the battery showed

**1. Speed was never the constraint — now confirmed at the SKU layer too.**
Build markdown→SQLite **164ms**; the JOIN query **0.17ms**; the *same* JOIN in pure Python with **no DB at
all, 9ms**. At N=11 / 555 rows the build is the only real cost and queries are free three ways over. SQLite
buys **zero** speed. (coded-queries said this for profile.md; it holds for the one-to-many roster.)

**2. The JOIN is dense — the one place the "empty graph" objection doesn't apply.**
**11/11** telehealth companies have an `offerings.md` (vs **1/24** joinable relation edges). The 3-way JOIN
answers questions that *are* error-prone by hand:
- Q3 — semaglutide SKUs by `pharmacy_model`: `18 SKUs / 6 brands` third-party · `7 / 2` integrated.
- Q5 — published-vs-gated pivot per brand: noom gates 9, eden is 27 `partial` (membership-stacked), hims
  publishes 49. Mentally joining a 555-row table to a cohort cut is exactly the "silently wrong by hand"
  class coded-queries said earns code.

**3. …but "earns code" ≠ "earns SQLite" — two things undercut the database specifically.**
- **The useful grouping is `LIKE` = grep-in-SQL, and the *stored* key fails.** Q6: `WHERE what LIKE
  '%semaglutide%'` → 9 brands, clean. But `GROUP BY molecule` (a stored key) **fragments** "testosterone"
  into **8 dirty buckets** ("testosterone cypionate" / "(ester not stated)" / family-row descriptions leaking
  in). This vindicates the architecture's *"no cross-company canonical molecule key; grouping is query-time
  grep"* line — the JOIN's value rides on `LIKE`, which is just [QUERYING Recipe 4](../../QUERYING.md)'s `rg`,
  not a DB capability.
- **coded-queries' own precedent: error-prone queries graduated into plain `store.py` functions, not a DB.**
  Q3/Q5 are ~5 lines of Python over the parsed dicts (the 9ms baseline proves it). A `store.py` offerings
  long-table loader + two helpers delivers these JOINs with **no build step, no schema, no staleness gap.**

**4. The price wall is decisive — and it's the real ceiling.**
`price_num` is **wrong, not merely lossy**:
| parsed | verbatim |
|---|---|
| `$50` | `Starting at $50 (consult) · $70/month for the first month, then $95/month` |
| `$39` | `$39 for the first month, auto-renews at $99/month thereafter` |
| `$34` / `$44` | `Starting at $34 first month` / `Starting at $44 first month` |

A first-month teaser sorts **above** the real recurring price as "cheapest" (Q7). Any `AVG`/`MIN`/`ORDER BY
price` inherits the lie. The store's verbatim-only discipline is **right**; a DB doesn't fix it — it *launders*
a string the engine deliberately refuses to fake into a number that looks authoritative. Real price
aggregation needs a per-SKU normalization layer (cadence · promo · membership-stacked all-in · dose floor) —
a **judgment layer the store pushes consumer-side**, and the true cost of this feature.

**5. Incidental: a corpus-wide DB is a cross-type footgun.**
`AVG(price_num)` across business types is one easy query away — exactly the per-night-vs-$/mo-vs-take-rate
comparison QUERYING.md forbids. The DB removes the friction that currently protects against meaningless
aggregates. Mild anti-Doro smell: structure invites over-trust.

## Engine notes (independent of the parked decision)

- **A markdown→table loader MUST be header-keyed, not positional.** `eden-health`'s roster adds `Form` /
  `Category` columns (OFFERINGS.md permits project-local columns); a positional loader silently misaligns.
  [`build_db.py`](build_db.py) `col_map()` keys on header name — the rung-3 loader must too.
- A lead-`·`-token molecule grab pulls **family/description rows** into the molecule field; a real loader
  should null `molecule` where `kind = family`.

## Recommendation

1. **Don't build SQLite.** Re-point the backlog trigger from "relations/traction" to the **offerings×cohort
   JOIN**, and gate it on **both**: (a) a human doing sustained *ad-hoc* multi-dimensional exploration (many
   one-off pivots, where writing SQL beats writing a function each time), **and** (b) a paid-for price
   normalization layer (without it the headline price aggregate is a lie generator).
2. **Cheap graduation candidate, if the JOIN pull recurs:** teach `scripts/store.py` to emit the joined
   offerings long-table (companies ⋈ telehealth ⋈ offerings) as dicts/CSV — an agent pivots it in Python ad
   hoc. Captures ~all the JOIN value at ~none of the DB cost; molecule stays `LIKE`/grep. This is the
   one-to-many reader coded-queries didn't build.

*Throwaway: `build_db.py` + `battery.py` are the artifacts, not load-bearing; `_out/store.db` is gitignored.
If recommendation #2 is taken, the graduated `store.py` reader supersedes `build_db.py`.*
