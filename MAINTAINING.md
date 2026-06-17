# MAINTAINING — the contract change-map

The markdown **contracts** are the source of truth: [`SCHEMA.md`](SCHEMA.md) + [`TAXONOMIES.md`](TAXONOMIES.md) (the `profile.md` record), [`modules/OFFERINGS.md`](modules/OFFERINGS.md), [`modules/VISUAL.md`](modules/VISUAL.md), the cohort packs [`TELEHEALTH.md`](modules/cohort-packs/TELEHEALTH.md) + [`PRODUCTIVITY_SAAS.md`](modules/cohort-packs/PRODUCTIVITY_SAAS.md) (and any future pack), [`SIGNALS.md`](SIGNALS.md). Code (`scripts/`, `scripts/present/`, `tools/`) and the `store/` records are **downstream** — a contract edit can silently break a consumer that still assumes the old shape.

This table is the blast radius: change a thing on the left, move the things in the middle, and the right-hand **check** is your mechanical backstop. **Where the check column is `—`, nothing guards it yet** — that's exactly where a human sweep (`/drift-sweep`) earns its keep.

## After any contract change, run the gate

Cheap + deterministic — run it before you call the change done:

```sh
ruff check scripts tools && python3 -m pytest tests/ -q
python3 scripts/querycheck.py --strict     # profiles vs SCHEMA/TAXONOMIES + FIELD_VERSIONS sync
python3 scripts/offeringscheck.py          # offerings.md roster contract + price-greppability
python3 scripts/cohortcheck.py --cohort telehealth          # once per active cohort pack…
python3 scripts/cohortcheck.py --cohort productivity_saas   # …(telehealth + productivity_saas today)
python3 scripts/visualcheck.py             # visual.md contract (no score/quality)
python3 scripts/build_db.py --check        # the SQLite lens's structural invariants
python3 scripts/store.py health            # staleness, stubs, module clock skew
```

## Change-map

| Change this contract… | …and these move with it | Mechanical check |
|---|---|---|
| **`profile.md` frontmatter field** (`SCHEMA.md`) — add / rename | bump `schema_version`; `PROFILE_FIELDS` in `build_db.py` (else absent from the `companies` table); `store.py` if `resolve()` reads it; `QUERYING.md` recipes + the `/query-companies` verb if it names the field; `present/model.py` if shown in a brief; if it can't backfill, append `name → version` to `FIELD_VERSIONS` in `store.py` | `querycheck --strict` (closed-set conformance + FIELD_VERSIONS sync). **`PROFILE_FIELDS` completeness is *not* auto-checked — verify by hand.** |
| **`profile.md` body section** (`SCHEMA.md` section table) — rename / add | `SECTION_ORDER` in `present/model.py` (else the section is silently dropped from every HTML brief) | **—** (eyeball / sweep) |
| **Closed-set value** (`TAXONOMIES.md`) — add / rename | existing profiles carrying the old value — migrate, or grandfather if it's a *meaning* change (→ MAJOR) | `querycheck --strict` (derives the set from the doc) |
| **`offerings.md` roster / visibility / enumeration** (`OFFERINGS.md`) | `offeringscheck.py` (`SPINE_PREFIXES` / `VISIBILITY_OK` / `ENUMERATION_OK`) — **`build_db.py` imports these, so it follows automatically**; `present/` if rendered | `offeringscheck`, `build_db --check` |
| **Cohort cut** (`TELEHEALTH.md` / a pack) — add / rename | existing `<cohort>.md` records with the old value (migrate). **Nothing in code by hand** — `cohortcheck` reads the contract and `build_db` derives `TELEHEALTH_CUTS` from it | `cohortcheck --cohort <x>`, `build_db --check` |
| **New cohort pack** | ship a `<COHORT>.md` with a machine-readable ```yaml``` block (`cohort` + `fields`) — **no new linter** (`cohortcheck` serves every pack); add a `<cohort>_full` view to `build_db.py` only if you want corpus aggregation | `cohortcheck --cohort <new>` |
| **`visual.md` contract** (`VISUAL.md`) | `visualcheck.py`; the visual section in `present/model.py` | `visualcheck` |
| **Signals path / envelope shape** (`SIGNALS.md`) | `signals.py persist()` owns the path; `signal_delta.py` if envelope keys change; the tool's paired `.md` | `tests/test_signals.py`, `tests/test_signal_delta.py` |
| **New capture tool** (`tools/`) | paired `tools/<tool>.md`; the `tools/README.md` table; `TOOL_SPEC` in `signals.py` if it's domain-drivable; `SIGNALS.md` if it's central | the tool's `tests/` file |

## Version + migration (don't restate — decide it in SCHEMA.md)

Whether a change bumps the version, and whether existing records **migrate** or **grandfather**, is decided once in [`SCHEMA.md`](SCHEMA.md)'s `schema_version` section. The short of it:

- **MAJOR** (`1`→`2`) — a field removed/renamed, or a value whose *meaning* changed. Old records are now non-conformant: migrate `store/`, re-capture where needed, **re-stamp every record**, then `querycheck --strict`.
- **MINOR** (`1.0`→`1.1`) — a new *optional* field / value / section. **No backfill, no re-stamp** — grandfather the old number so an empty new field reads "predates the field." If the field can't backfill, append `name → version` to `FIELD_VERSIONS` in `store.py`.
