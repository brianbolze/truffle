# Trust surface — the smallest ship-set

*Shipped 2026-06-09. Two files touched: `scripts/store.py` and `QUERYING.md`. Everything is computed at call time; the one hand-maintained artifact gets a lint fence. This shipped before doc 03's verb and sets up doc 04's lens assumptions.*

**Empirical grounding** (from the probe + a full store scan, [evidence](01-evidence.md)): stubs are **binary** — every folder either has a full profile or only `captures/`; there is no skeletal-profile state to detect. Staleness is mild but bimodal (a third of the corpus was captured in one sprint and will age as a block). Module clocks diverge from profile clocks by up to 4 days — today always *newer* (deepen-offerings refreshed rosters); the dangerous inverse arrives at the first profile re-capture. `unverified_fields` is non-empty on every profile.

## 1. `store.py find` learns the whole store *(prerequisite for everything else)*

Today `load()` globs `store/*/profile.md` — **stubs are structurally invisible**: `find norexi` returns "NOT in store" while `store/norexi-org/captures/` holds paid-for evidence. That is the scout's false-negative, verbatim.

Change: resolve over folders, not just profiles. Per hit, print:

```
brello → brellohealth-com   captured 2026-06-04 (5d) · offerings 2026-06-04 · schema 2.5
norexi → norexi-org         STUB — captures only (2026-06-02), no profile
```

plus, for grandfathered profiles: `schema 2.2 — predates: price-visibility, logos`.

**Replaces:** hand-matching, the remembered stamp-check rule, and the scout's requested "in store but not captured" priority rule (the distinction is now in the output).

## 2. `store.py health` — one subcommand, no generated files

Stub list · staleness ranking (oldest N, day counts) · module-clock skew lines · one `store.db built <date>; N markdown files newer` line. ~40 lines on the existing `_DISPATCH`.

**Replaces:** the probe's missing "Q7 recipe" (stalest/stubs had no documented path) and every consumer's ad-hoc stub detection. A generated `STATUS.md` is rejected: it's a second derived surface that rots exactly the way `store.db` and "13/13" rotted — silently. **Computed-at-call-time has no drift mode.**

## 3. `QUERYING.md` — strip the lies, add one convention

- **Delete the three baked live numbers** (relations "1 joinable / 23 dangling / 8 name-only" → actual 3/31/8; cohort "13/13" → actually 49; footer "written against schema_version: 1" → corpus at 2.5). Replace with mechanics-only phrasing ("run `store.py relations`"). The consume verb (doc 03) routes *more* traffic into this doc — shipping it while it holds known-wrong numbers amplifies the lie.
- **Add the stub definition** (one line): *a folder without `profile.md` is a raw capture cache, not a dossier; "is X captured?" means "does `store/<x>/profile.md` exist."* No `capture_status` frontmatter — the artifact needing the flag has no frontmatter file to carry it, and the scout runs that create stubs are project-side and won't load a marker rule. No deletion/quarantine — stubs are paid-for evidence consumers already grep in place.
- **Add the answer-trust convention** (one sentence, beside the existing negative-trust rules): *quote the clock, the floor, and the gaps* — point reads end with `as of <captured_at> (Nd)` using the **governing clock** (module clock for module facts); **cohort answers use a range form** (`captures 2026-05-30..06-07, oldest 10d`) rather than ~40 per-row clauses an agent would satisfice into dropping; counts state their `enumeration` status; fields appearing in that profile's `unverified_fields` get said out loud. Cheap to follow because item 1 puts the clocks in `find`'s output — the agent copies, it doesn't remember.

## 4. `FIELD_VERSIONS` — the one mirror, fenced

A ~5-line dict in `store.py` — `{price_visibility_token: "2.3", logos: "2.5"}` — lets `find`/`health` print `predates: …` computed from each profile's stamp, so the grandfather rule arrives *in the data the agent just read* instead of as a remembered rule. (Drop `run_profile`: SCHEMA says its absence reads "plain capture" — no trust hazard, so no entry.)

**The fence (non-negotiable, from adversarial review):** this dict is a hand-maintained mirror of SCHEMA's version history, and its failure mode is *worse* than the status quo — an un-updated dict prints `predates: (nothing)` for a profile that does predate a 2.6 field: a confident wrong negative. So: `querycheck --strict` asserts the dict covers every grandfathered field SCHEMA names, and SCHEMA's minor-bump note gains "append to FIELD_VERSIONS." Mirror + lint, or don't ship it.

**Replaces:** the remembered stamp-check as the safety mechanism. Re-stamping the 2.2 profiles would lie (2.3/2.5 are no-backfill *by design* — tokens and logos need re-capture); re-capturing them is the true retirement path but spends Firecrawl — the dict makes waiting safe for ~8 lines.

## Named non-goals (so silence isn't mistaken for coverage)

- **Enumeration debt** (37/47 rosters `unknown`) — this set makes the floor *quoted*, never *retired*. Retirement = a `/deepen-offerings` backfill pass across the active cohort = Firecrawl spend. **Brian's call** ([README](README.md) open decisions).
- **The P4 routing miss** — everything here lives in/behind QUERYING.md, which the bypassing agent never reaches. That is the verb's job (doc 03, now shipped with an implicit-routing re-test caveat).
- **`store.db` staleness for the Beekeeper consumer** — `health`'s mtime line is invisible to someone sitting inside a GUI. That fence belongs *in the db* (`_meta`, doc 04). The original design rejected `_meta` as redundant with `health`; the adversary correctly flipped it — by this design's own logic (data-you-just-read beats rules-you-must-recall), the GUI consumer needs the signal in the surface being consumed.

## Adversarial review — what changed

The reviewer verdict was *needs-changes*, with the skeleton conceded as "not over-engineered; under-finished." Folded in: the "nothing can drift" headline softened (FIELD_VERSIONS *is* a mirror — hence the lint fence); the QUERYING number-strip pulled into this set (the design quoted that rot as rationale while leaving it in place); the per-company as-of recitation replaced with the range form; `run_profile` cut; the `find` change re-scoped honestly (it's a resolution-surface extension, not a print tweak); `_meta` re-assigned to the lens; the two unscoped frictions named above.
