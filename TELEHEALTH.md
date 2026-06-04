# TELEHEALTH.md — the `telehealth` cohort-pack contract

> **What this is.** The contract for the engine's first **cohort pack** — the opt-in `store/<domain>/telehealth.md` that carries the telehealth-specific classification cuts the universal `profile.md` can't tell apart. This is the spec you **obey** when authoring a `store/<domain>/telehealth.md`.

> **CAPS vs lowercase.** `TELEHEALTH.md` (this file, repo root) = the **contract**. `store/<domain>/telehealth.md` = the **instances** that obey it. Same word, two roles — the case tells them apart.

*Companion to [`SCHEMA.md`](SCHEMA.md) (the always-on `profile.md` contract), [`TAXONOMIES.md`](TAXONOMIES.md), and [`QUERYING.md`](QUERYING.md). Lint: [`scripts/cohortcheck.py`](scripts/cohortcheck.py). Module registration + the species distinction: [`SCHEMA.md` → Tier-1 modules](SCHEMA.md#tier-1-modules-opt-in-separate-docs).*

## What a cohort pack is (and isn't)

A **cohort pack** shares `offerings.md`'s machinery — a separate file, its own contract, enablement-by-existence, own `captured_at` — but it's a **different species** from a depth module:

| | **Depth module** (`offerings.md`) | **Cohort pack** (`telehealth.md`) |
|---|---|---|
| Extends | a *universal* dimension at finer grain (what they sell) | *vertical-specific* cuts that don't exist elsewhere (owns-pharmacy?) |
| Schema | cohort-agnostic — any company could have one | defined by the cohort — meaningless for a watchmaker |
| The test | does a consumer need this grain? | does it split companies **within the cohort** on a question we'd act on? |

The pack exists because **the universal profile reads near-identical for every telehealth brand** (all `B2C · Healthcare · Subscription`) — so the cuts that actually separate players are invisible to it. Every field below earns its place on **both** halves: it splits the cohort *and* fills from the company's own site.

**State-only, page-attested, never adjudicated** — the same trust line as `profile.md`. Record what the site *says*; don't verify it, don't rank it, don't compare it to peers. Three things stay out, by design:

- **Judgments** (threat / fit / formidability / "direct competitor?") — relative to *one* asker; a pack is shared across every project that reads the cohort, so an asker-relative verdict poisons it for the next reader. Consumer-side.
- **Cross-company comparison** ("one of only two who own their pharmacy") — rots the moment the cohort grows; it's a **query-time** read (`rg` across the cohort frontmatter), never baked per-file.
- **Deep-research provenance** (founders, legal entity, funding, traction) and **Signals** (news, M&A, a regulatory-exposure *verdict*) — store the page-attested *posture*; let the consumer infer.

## When to write it

Opt-in — **enablement = the file exists** (no config mechanism). Written **alongside `profile.md`** on a telehealth capture, enabled in the `/research-company` step-2.5 pre-flight. Default everywhere else: **don't write the file** — an absent `telehealth.md` reads "not in this cohort."

## `telehealth.md` — frontmatter (the 8 cuts)

Eight **single-select** closed-set fields, plus doc-meta (`schema_version`, `domain`, `captured_at`). Leave a field **empty** when the captured site doesn't determine it — *empty over guessed* — or use the explicit `unclear` value when you looked and the site is genuinely silent. Read each off the company's own pages; **never infer from the brand name**.

| Field | Closed set (single-select) | The cut it makes | Reads off |
|---|---|---|---|
| `value_chain_role` | `DTC brand` · `compounding pharmacy` · `platform/infra` · `diagnostics/labs` · `wholesale/supply` · `unclear` | what kind of telehealth player — the cohort **gate** (compete / buy-from / ignore). Tag what they **are**, not what they **bundle** (a DTC brand with a captive pharmacy is a `DTC brand`). | homepage, nav, /about, JSON-LD `@type` |
| `pharmacy_model` | `integrated` · `third-party` · `is-a-pharmacy` · `none/diagnostics-only` · `unclear` | vertical integration into fulfillment. **Coarse posture only** — `integrated` merges owns + captive-affiliate (the part a page can't verify). The ownership **claim** goes in the body verbatim, never judged true. | /how-it-works, /about, footer |
| `audience` | `men-only` · `men-first` · `all-genders` · `women-first` · `women-only` · `unclear` | the gender the site **leads with** (a `/mens` hub, a male hero) — head-on vs adjacent. **Never the brand name.** Parallel-gendered structures get a body note. | nav, hero, copy |
| `compounding_posture` | `compounded-only` · `both` · `FDA-brand-only` · `OTC/supplement` · `unclear` | sells compounded meds, FDA-brand drugs, or both — the company-level roll-up of the per-SKU lane (which stays in `offerings.md`). | FDA disclaimers on Rx pages |
| `anchor_category` | `TRT` · `GLP-1` · `sexual-health` · `hair` · `skin` · `longevity/NAD` · `peptides` · `womens-HRT` · `labs` · `mental-health` · `primary-care` · `multi/none` · `unclear` | the single vertical the site **leads with** (front door), distinct from full coverage (body). **A/B-volatile** — record point-in-time, flag rotation. `multi/none` tags a generalist leading a co-equal grid. | hero, first nav item, CTAs |
| `modality` | `async` · `hybrid` · `sync` · `N/A` · `unclear` | the **front-door / gating consult's** modality (per-SKU mix stays in `offerings.md`). | "How it works" step-flow |
| `access_model` | `membership-required` · `all-in` · `per-visit` · `à-la-carte/both` · `unclear` | the membership/fee architecture — the finer axis under the universal `business_model: Subscription`. | pricing / membership page |
| `pay_model` | `cash-pay only` · `HSA/FSA eligible` · `bills insurance` · `N/A` · `unclear` | touches a payer rail or is cash-pay. **Asymmetric fill — capture the positive signal:** "bills insurance / HSA-eligible" when page-stated; `cash-pay only` only when the site says direct-pay; **silent ⇒ `unclear`, never an assumed "no."** | "insurance / HSA / direct-pay" copy |

### Machine-readable contract (the lint reads this)

`scripts/cohortcheck.py --cohort telehealth` parses the block below (the first fenced `yaml` block carrying `cohort` + `fields`) and validates every instance's frontmatter against it. Keep it in sync with the table above — this block is the source of truth the lint enforces.

```yaml
cohort: telehealth
doc_meta: [schema_version, domain, captured_at]
fields:
  value_chain_role: [DTC brand, compounding pharmacy, platform/infra, diagnostics/labs, wholesale/supply, unclear]
  pharmacy_model:   [integrated, third-party, is-a-pharmacy, none/diagnostics-only, unclear]
  audience:         [men-only, men-first, all-genders, women-first, women-only, unclear]
  compounding_posture: [compounded-only, both, FDA-brand-only, OTC/supplement, unclear]
  anchor_category:  [TRT, GLP-1, sexual-health, hair, skin, longevity/NAD, peptides, womens-HRT, labs, mental-health, primary-care, multi/none, unclear]
  modality:         [async, hybrid, sync, N/A, unclear]
  access_model:     [membership-required, all-in, per-visit, à-la-carte/both, unclear]
  pay_model:        [cash-pay only, HSA/FSA eligible, bills insurance, N/A, unclear]
```

## `telehealth.md` — body

A light **bold-led** body (lead each line with a bold label + colon, per SCHEMA's body discipline) for what needs verbatim or fills only as prose. Governing rule for all of it: **page-attested, never adjudicated** — record what the site says, don't verify it.

- **Fulfillment** — the pharmacy-ownership **claim, quoted verbatim** (e.g. *"'we own our pharmacy' — homepage"*), + the 503A/503B lane **only when the page states it**. This is where the owns-bit lives — a claim, never resolved to truth. **Allow an earned prose paragraph** (not a forced one-liner) when the real picture is multi-clause (e.g. *503A for orals + a 503B partner for steriles + an owned facility on a sibling domain*) — a single line would flatten true complexity into something falsely clean.
- **Categories served** — the full coverage list as one greppable line (`TRT · GLP-1 · sexual-health · hair · …`), a **token set, never a stored taxonomy** (cross-brand grouping is a query-time grep). `anchor_category` is the frontmatter slice of this.
- **Health-merchant credibility** — the health-specific trust signals that don't generalize to the universal profile: **LegitScript-certified** (footer seal, y/n), **named clinicians** (a `/physicians` page, y/n), pharmacy accreditations (PCAB/ACHC/NABP) when present.
- **Controlled-substance Rx** — `offers Schedule-III (testosterone/TRT) | non-scheduled only | unclear`, backed by the page-attested **product** (does a TRT SKU appear), not an asserted DEA schedule.
- **Labs** — `required-step | optional | none` + draw model (at-home / partner-lab) when stated.
- **Payment & commitment** — the `pay_model` detail (HSA/insurance specifics) + commitment terms (`cancel-anytime | N-month lockup | per-visit`), **page-stated terms only** — never the charged-after-cancel reality (that's a Signal).

### File shape (drop-in template)

```yaml
---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"          # the telehealth-pack version (independent of profile.md's)
domain: maximustribe.com       # company key (same as profile.md)
captured_at: 2026-05-31        # own freshness — posture shifts (adds a women's line, swaps pharmacy)
value_chain_role: DTC brand
pharmacy_model: third-party              # body Fulfillment line carries the verbatim claim
audience: men-first                      # men-origin, women added — read from /about + hero
compounding_posture: both                # compounded TRT/GLP-1 + commercial Kyzatrex
anchor_category: TRT
modality: sync                           # "video visit with a US-licensed physician"
access_model: membership-required
pay_model: cash-pay only                 # "insurance-free / direct-pay" (/about-us)
---

## Fulfillment
- **Pharmacy:** "we strictly partner with US-based, licensed compounding pharmacies… USP standards" — /about-us (claim; no named partner, no owned facility). Lane: not stated.

## Categories served
- **Categories:** TRT · GLP-1 · sexual-health/ED · peptides/GH · hair · labs · mood

## Credibility & access
- **Health-merchant credibility:** LegitScript-certified (footer seal); named clinicians (advisory board, /about-us); pharmacy accreditation not shown
- **Controlled-substance Rx:** offers Schedule-III (injectable testosterone) — /testosterone pages
- **Labs:** optional — at-home test ($99.99); consult proceeds without
- **Payment & commitment:** cash-pay only; 12-month plan for the 50%-off entry, monthly otherwise
```

*A sparse capture is honest: a platform/lab where half the fields don't apply leaves them `unclear`/empty rather than guessing — e.g. `value_chain_role: platform/infra · pharmacy_model: none/diagnostics-only · modality: async`, the rest `unclear`.*

## Capture

**Near-free — it rides the `profile.md` pages, no new endpoints.** Every cut fills from pages the standard recipe already pulls (homepage, /how-it-works, Rx PDPs, /pricing, JSON-LD). Enable the pack in the step-2.5 pre-flight, like `offerings.md`. One genuinely new behavior + two reminders:

1. **Follow the owned-pharmacy sibling domain** — when the site points to an owned pharmacy on another domain (a brand → its `*pharmacy.com`) or the footer names a pharmacy entity, pull it in and record its lane on the **Fulfillment** line. Without this, a vertically-integrated brand reads as a third-party router.
2. **Quote any ownership claim verbatim; adjudicate nothing** — the marketing copy ≠ the truth (a brand can claim "we own our pharmacy" and route to a third party). The engine records the page-attested claim; verifying ownership is a deep-research job.
3. **Flag `anchor_category` rotation** with the stock `unverified_fields` "point-in-time snapshot, not fixed" line (per SCHEMA's live-variable rule) when the hero A/B-tests — the anchor is the most rotation-prone field.

## The rules (what the lint enforces)

`python3 scripts/cohortcheck.py --cohort telehealth` is the gate — it must pass. The load-bearing rules:

1. **Closed-set conformance.** Every non-empty cut value is one of the field's declared values (the machine-readable block above). A value off the list fails — exact strings only, so the cohort stays queryable.
2. **Single-select.** Each cut is one value, never a list — `audience: men-first`, not `[men-first, all-genders]` (a parallel-gendered nuance goes in a body note).
3. **Doc-meta present.** `schema_version`, `domain`, `captured_at` — the frontmatter fence and the three keys.
4. **Empty over guessed.** A field the site doesn't determine is left empty or `unclear`; the lint never demands a value, but it rejects one outside the set.
5. **No stray keys.** A frontmatter key that's neither doc-meta nor a declared cut trips the lint — it catches a typo'd field or a universal `profile.md` field leaking in.
