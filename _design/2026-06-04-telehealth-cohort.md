# Design: the `telehealth` cohort pack — the engine's first *cohort pack*

> **What this is.** The reasoning behind the engine's first **cohort pack** — `store/<domain>/telehealth.md`, the per-company telehealth-specific classification the universal `profile.md` can't carry. The spec you *obey* is [`TELEHEALTH.md`](../modules/TELEHEALTH.md); this doc is the *why*. Companion to the [frame](2026-05-29-frame.md) (scope) and [architecture](2026-05-30-architecture.md) (lifecycle, modules).

## Why it exists

`profile.md`'s universal classification is built to **sort across the whole corpus** — telehealth vs watches vs SaaS. The price of a cut that generalizes is that *inside* one vertical it goes flat: the telehealth set came back **13/13 identical** on every universal classification field (all `B2C · Healthcare & Life Sciences · Services + Pharma · Subscription`). So the questions that actually separate telehealth players — *does it own its pharmacy? who does it lead with? async or sync? compounded or FDA-brand?* — are **invisible to the universal schema**.

A **cohort pack** is the fix: a small set of vertical-specific cuts that only make sense inside one cohort, written to a separate per-company file, enabled where a consumer needs them. Telehealth is first because it has the first live consumer — the Teleprescribe venture's competitive work.

## A cohort pack is a different *species* of module

It shares `offerings.md`'s machinery — a separate file, its own contract, enablement-by-existence, own `captured_at` — but answers a different question:

| | **Depth module** (`offerings.md`, `brand.md`) | **Cohort pack** (`telehealth.md`) |
|---|---|---|
| Extends | a *universal* dimension at finer grain (what they sell) | *vertical-specific* cuts that don't exist elsewhere |
| Schema | cohort-agnostic — a watch brand fills the same columns | defined by the cohort — `owns-pharmacy?` is meaningless for a watchmaker |
| The test | does a consumer need this grain? | **within-cohort information gain** — does it split companies *inside* the cohort on a question we'd act on? |

The within-cohort test is sharper than the universal "every field is a cut": a cohort field that *also* goes near-uniform across the cohort is decoration, even if it'd cut the whole corpus. `audience` is the worked example — the coarse `men/women/both` returns 21/30 "both" (flat), so the pack reads *who the site leads with*, which re-splits that mass.

The cohort pack also **stretches the module definition** a touch: a depth module carries a real gather *recipe* (offerings has its own enumeration ladder); a cohort pack mostly **rides the `profile.md` pages** — its cuts read off the same homepage / how-it-works / pricing pages the base capture already pulls. So it's "schema + destination" with a thin recipe, not a mini-verb. That's why it's near-free.

## State-only, page-attested, never adjudicated

Same trust line as `profile.md`. Three things stay **out**, by design — and each reason survives *because the store is shared* across every project that reads the cohort:

- **Judgments** (threat / fit / formidability) are relative to *one* asker; a shared pack can't hold them without poisoning the next reader. They live consumer-side — for the first consumer, the venture's deep-research reports *are* that judgment layer.
- **Cross-company comparison** ("one of only two who own their pharmacy") rots the moment the cohort grows — it's a **query-time** read over the pack's frontmatter ([QUERYING Recipe 6](../QUERYING.md)), never baked per-file.
- **Deep-research provenance** (founders, legal entity, funding) and **Signals** (a regulatory-exposure *verdict*) — the pack stores the page-attested *posture*; the consumer infers the rest.

The exemplar is `pharmacy_model`: sites **lie** about owning their pharmacy (a brand markets "we own our pharmacy" and routes to a third party). So the frontmatter carries only the **coarse page-attested posture**; the ownership **claim** is quoted verbatim in the body and **never adjudicated** — verifying it is deep-research, not capture. Same discipline as `offerings.md`'s page-attested molecule.

## One contract, one generic linter

The 8 cuts and their closed sets live in [`TELEHEALTH.md`](../modules/TELEHEALTH.md) — **not** `TAXONOMIES.md`, which holds the *universal* sets; a cohort owns its own vocabulary. The contract carries a **machine-readable closed-set block**, so [`scripts/cohortcheck.py`](../scripts/cohortcheck.py) is **one generic linter for every cohort pack**, not one script per cohort: `cohortcheck.py --cohort telehealth` reads telehealth's block. The next cohort ships a contract, not a script.

## Registration, not a version bump

A cohort pack is a separate file with its own `schema_version` — it changes nothing in `profile.md`, so registering it is a **docs edit to SCHEMA's Tier-1 modules section, not a `profile.md` version bump** (exactly how `offerings.md` was added). Membership is **file existence** — an absent `telehealth.md` reads "not in this cohort"; no universal pointer field (parity with `offerings.md`).

## Open: the directory layout

The contracts stay **top-level CAPS files** for now (`OFFERINGS.md`, `TELEHEALTH.md`) — one depth module + one cohort pack isn't enough to earn a directory. **Deferred, with a flag:** the natural `cohorts/` name **collides** with the architecture's store-level [`cohorts/<category-slug>/`](2026-05-30-architecture.md) cross-company *signals* layer (a different thing — Signals, keyed by category, not per-domain State). So when a 2nd module earns a directory, the likely move is **one `modules/` dir for all contracts** (species noted inside, as SCHEMA's Tier-1 section already does), leaving `cohorts/` free for the signals concept. Don't prematurely pick `cohorts/`.

## De-risked

Validated on a real **Hone** `telehealth.md` (the contract's first instance) — two cuts honestly `unclear` (its site doesn't state pharmacy ownership or insurance stance), and `audience: all-genders` from its co-equal men/women hubs (the men-origin read is a consumer-side judgment, kept in a body note). Rolling the pack across the remaining cohort is deferred capture work.

*Designed in a Teleprescribe CSO pass (the venture is the first consumer); the contract is venture-neutral so any project researching telehealth competitors can read it.*
