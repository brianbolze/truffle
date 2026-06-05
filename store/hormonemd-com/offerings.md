---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: hormonemd.com
captured_at: 2026-06-04
site_notes: "Roster = the 6 top-level treatment pages (Treatments nav dropdown: /testosterone, /estrogen, /semaglutide, /sermorelin, /metformin, /dhea). Pricing is a FLAT PLATFORM MEMBERSHIP on /pricing ($84/mo annual-prepay · $99/mo monthly), NOT per-treatment — every PDP repeats the same '$84/mo including regular lab work'; per-medication cost is never published (meds at 'low rate pharmacy prices'). No per-SKU price variation, so deepen only Semaglutide (compounded-not-FDA-approved disclaimer). /llms.txt lists a 7th protocol (Rapamycin) with no live page — not enumerable."
---

## Portfolio overview

`Multi-product`: six prescription treatment lines spanning hormones (TRT, BHRT, DHEA), medical weight loss (semaglutide), and longevity/anti-aging (sermorelin, metformin). The **shape finding that drives the whole roster: pricing is a single platform membership, not per-SKU.** Every treatment page advertises the identical "$84/mo including regular lab work," which is the membership fee — it buys unlimited consults, labs, and shipping; the medication itself bills separately at unquoted "low rate pharmacy prices." So all six treatment rows carry the membership price at `partial` visibility (the access fee is shown; the all-in is not). The membership plan itself (/pricing) is the one `published` line.

Prominence (calibrated): **TRT** `[MED]` (brand identity, first Treatments nav item, first homepage carousel card) and **Semaglutide** `[MED]` (leads the homepage benefit grid, "shipped overnight" urgency) edge ahead; the other four sit in a co-equal homepage grid `[LOW]`.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Membership | buyable | — | /pricing | "$84/mo" annual ("Billed $1,008 yearly", "FREE Initiation") · "$99/ Month" ("$99 One-Time Initiation") | published | platform membership · n/a · unlimited consults + regular labs + discreet shipping; meds ordered separately |
| Testosterone (TRT) | buyable | — | /testosterone | "$84/mo" | partial | testosterone · injections, creams, or pills · membership Rx, men (low-T); med cost separate |
| Estrogen (BHRT) | buyable | — | /estrogen | "$84/mo" | partial | bioidentical estrogen/progesterone/testosterone · injections, creams, pills, patches, or suppositories · membership Rx, women (menopause) |
| Semaglutide | buyable | — | /semaglutide | "$84/mo" | partial | compounded semaglutide (GLP-1) · weekly injections or capsules · membership Rx, weight loss |
| Sermorelin | buyable | — | /sermorelin | "$84/mo" | partial | sermorelin (GHRH peptide) · injections, nasal sprays, or pills · membership Rx, "natural HGH" |
| Metformin | buyable | — | /metformin | "$84/mo" | partial | metformin (off-label) · daily pills · membership Rx, longevity / insulin sensitivity |
| DHEA | buyable | — | /dhea | "$84/mo" | partial | DHEA · oral pills or topical cream · membership Rx, hormonal balance |

*All six treatments require the Membership (top-level pages, not nested under it in nav) — Parent left `—`; the economic dependency is the overview's flat-membership finding. Rapamycin is advertised in /llms.txt as a longevity protocol but has **no live page** (absent from nav + a `--search rapamycin` map pass) → not enumerable, not rostered.*

### Verbatim anchors

The footnotes that decide `partial` vs `published`:

- **Membership plans (/pricing):** Popular — "$84/ Month", "\*Billed $1,008 yearly", "$279 Discount", "FREE Initiation", "60-days of medication per order". Intro — "$99/ Month", "\*Billed $99 monthly", "$99 One-Time Initiation", "30-days of medication per order".
- **Why treatments are `partial` (/pricing, step 5):** "Order medications — Low rate pharmacy prices, no upcharges or hidden fees." The membership is shown; the per-medication cost is not.
- **Per-treatment price (each PDP):** "$84/mo" / "including regular lab work" (e.g. /testosterone, /semaglutide) — the membership fee restated on every treatment page, never a treatment-specific price.
- **Molecule audit (page-attested):** semaglutide = "Compounded semaglutide" (/semaglutide); testosterone, estrogen, sermorelin, metformin, DHEA each named on their own PDP. None inferred from the brand name.

## Deep blocks

Only one earns a block — the rest are fully carried by their roster rows.

**Semaglutide — the compounded lane (resolves `compounding_posture` at SKU grain).** /semaglutide is titled "Compounded Semaglutide" and states verbatim: *"Compounded semaglutide itself is not FDA-approved. While the active ingredient semaglutide is used in certain FDA-approved medications, the compounded preparation is a customized medication tailored to an individual patient's specific clinical needs… and therefore does not undergo the same FDA pre-market approval process as mass-produced brand-name products."* Form: "compounded semaglutide injections and capsules," "a single weekly dose." This is the only line that is unambiguously compounded-only; metformin and sermorelin pages assert FDA-approved status, putting the company at `compounding_posture: both`.

*PDP-template anatomy block: not requested this run (opt-in) — skipped.*

## Provenance

- **Pages read:** /pricing, /testosterone, /estrogen, /semaglutide, /sermorelin, /metformin, /dhea (captured 2026-06-04, cited in `captures/2026-06-04/`), plus /llms.txt for the Rapamycin cross-check.
- **Scope:** all 6 live treatment lines + the membership enumerated. Rapamycin noted-but-not-enumerated (no live page). No leaf SKUs below the treatment level — the company indexes at the treatment page, and price/medication detail does not vary per leaf.
- **Gated/unreachable:** per-medication pricing (never published; meds bill at "low rate pharmacy prices"). Dosage/strength tiers are set per-patient post-consult, not catalogued.
- **Point-in-time snapshot:** prices/plans are a 2026-06-04 snapshot ($84/$99 membership, "$279 Discount") and may run promos — re-check next run.
- **Run profile:** part of a guided run that enabled +offerings (with +telehealth, +logos). No custom columns or PDP-anatomy block added — vanilla roster.
