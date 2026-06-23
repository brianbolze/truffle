# 2026-06-01 — coded queries

**Hypothesis.** Most consume-side asks are a one-line YAML filter ([`QUERYING.md`](../../QUERYING.md) already
shows them) — but a few are fiddly enough by hand that an agent gets them *subtly wrong*. Those few are the
ones worth committing as code instead of a prose recipe. Probe the line.

**Method.** [`probe.py`](probe.py) (stdlib + PyYAML, loads frontmatter fresh each call) implements six
candidate primitives and runs them against the live 45-profile store:

| cmd | ask | starter? |
|---|---|---|
| `stats` | count + breakdowns | ✔ count |
| `find <q>` | is X in the store? (domain / name / alias / slug → key) | ✔ search |
| `recent [n]` | capture freshness, newest first + staleness | ✔ recent |
| `relations` | which `parent`/`owns`/alias targets actually resolve to a held profile | ← expansion |
| `facet <field>` | generic group-by on any field | ← expansion |
| `coverage` | how populated is each field across the corpus | ← expansion |

Not in scope: building the SQLite index (rung-3, deferred — and the timing here argues it stays deferred).
The question is *which primitives earn a script*, not *let's build the index*.

**Result → [`FINDINGS.md`](FINDINGS.md).** Two primitives earn code (`find`, `relations`); the rest are
conveniences. The join-check also surfaced four things prose can't: a slug-convention split, a top re-capture
target by in-degree, a mis-typed alias, and the precise size of the cross-corpus JOIN gap.
