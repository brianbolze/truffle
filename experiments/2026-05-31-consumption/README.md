# 2026-05-31 — consumption test

**Question:** do the store formats actually answer real queries? (The 2026-05-29 experiment
proved queryability in principle on a different layout; this tests the *current* store —
11 companies — from a cold consumer's seat.)

**Method:** read only README/SCHEMA/TAXONOMIES, ran a 5-query battery (point read, filter/group,
cross-brand aggregate, verbatim primary-source, relational) **by hand** before building anything,
recording cost + friction per query. Then prototyped + measured a rung-2 helper.

**Verdict:** formats are queryable; the thing that fought every query is **contract↔corpus drift**,
not structure. Rung-2 pick = a `QUERYING.md` recipe doc + a thin `facets` helper.

- [`FINDINGS.md`](FINDINGS.md) — the deliverable.
- [`digest.py`](digest.py) — store-aware rung-2 prototype (`facets` + `term`).
- [`_out/`](_out/) — measured outputs.
