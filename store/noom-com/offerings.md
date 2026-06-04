---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: noom.com
captured_at: 2026-06-04
site_notes: "Noom Med is a PROGRAM, not a SKU catalog — prices are program/tier-level (homepage + Microdose-page footnotes); individual brand-drug PDPs (/med/<brand>/) are quiz-gated and were not scraped, so per-drug prices are on-request. Molecule tags ride as small labels above each drug card on /med/ (Semaglutide/Tirzepatide/Oral); footnotes (excluded from attestation) name semaglutide→Ozempic/Wegovy, tirzepatide→Zepbound/Mounjaro. Pricing is a snapshot — 'New pricing for new accounts only effective as of March 31, 2026'; all-in med cost varies insurance vs. cash-pay."
---

## Portfolio overview

**Shape finding — this is not a catalog of independent SKUs.** Noom Med is a behavior-change **subscription** with a clinician-selected medication inside it. What looks like a product menu on `/med/` is really **three program tiers** (GLP-1Rx, GLP-1Rx Plus, Microdose) that route to a **menu of medication options** (compounded/generic + brand-name GLP-1s and orals), all wrapped by the **GLP-1 Companion** app. Prices are quoted at the **program** level, not per drug — the per-drug cost depends on the clinician's choice and the member's insurance vs. cash-pay status, so most drug rows are `on-request` with a published program floor.

**Prominence (calibrated):**
- **GLP-1Rx / GLP-1Rx Plus** — `[HIGH]` the company's own hero ("Get Noom's Most Powerful Program… Try Noom GLP-1Rx Plus"; homepage + `/med/` lead card).
- **Microdose GLP-1Rx** — `[HIGH]` a dedicated homepage module ("A Low Dose Way to Start") and its own landing page; the low-cost on-ramp.
- **GLP-1 Companion** — `[MED]` foregrounded as "the true star of our programs," but it's the wrapper, not a standalone purchase.
- **Brand-name drugs (Ozempic®/Wegovy®/Zepbound®/Mounjaro®)** — `[MED]` named prominently as access points, but presented as options within a program, not separately-priced products.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Noom Med | family | — | /med/ | — | — | The telehealth weight-loss program — clinician-prescribed GLP-1/oral meds + the Noom app · quiz/intake-gated |
| Noom GLP-1Rx Program | buyable | /med/ | (no PDP — /lp/clinical?route=clinical quiz route) | "from $149 plus tax and $349 per month plus tax for 12 week subscription thereafter" | partial | GLP-1 (compounded · generic · brand-name) · program floor; med cost varies by insurance/cash-pay · clinician-prescribed |
| Noom GLP-1Rx Plus | buyable | /med/ | (no PDP — /lp/clinical?feature=tirzepatide quiz route) | — (priced as GLP-1Rx) | on-request | "Advanced GLP-1 Program" — tirzepatide track (per feature=tirzepatide route) · clinician-prescribed |
| Noom Microdose GLP-1Rx Program | buyable | /med/ | /med/glp1-microdose/ | "plans start at $79" / "$199 per month… thereafter"; "$99… regardless of insurance, when prescribed" | partial | compounded GLP-1 (footnote: "prescribed compounded GLP-1s") · low/microdose · clinician-prescribed |
| Noom GLP-1 Companion | buyable | /med/ | /med/glp1-companion/ | "included at no additional cost with a Noom plan for eligible members taking GLP-1 medication" | published | digital companion app (SmartDose, Muscle Defense™, AI nutrition, AI Body Scan, Glucose Forecasting) · no-cost add-on, bundled with a Noom plan |
| Wegovy® | buyable | /med/ | /med/wegovy/ | — ("starting at $69 plus… out-of-pocket cost" brand-name floor) | on-request | semaglutide (card tag) · injectable · clinician-prescribed, PDP quiz-gated |
| Ozempic® | buyable | /med/ | /med/ozempic/ | — (brand-name "$69" floor + med cost) | on-request | semaglutide (card tag) · injectable · clinician-prescribed, PDP quiz-gated |
| Zepbound® | buyable | /med/ | /med/zepbound/ | — (brand-name "$69" floor + med cost) | on-request | tirzepatide (card tag) · injectable · clinician-prescribed, PDP quiz-gated |
| Mounjaro® | buyable | /med/ | /med/mounjaro/ | — (brand-name "$69" floor + med cost) | on-request | tirzepatide (card tag) · injectable · clinician-prescribed, PDP quiz-gated |
| Wegovy® Pill | buyable | /med/ | (no PDP — feature=wegovypill quiz route) | — | on-request | molecule not stated on card · oral (card tag) · clinician-prescribed |
| Metformin | buyable | /med/ | /med/metformin/ | — | on-request | metformin (name = molecule) · oral (card tag) · "not FDA-approved for weight loss" (page) · clinician-prescribed |
| Generic liraglutide | buyable | /med/ | /med/liraglutide/ | — | on-request | liraglutide (name = molecule) · form not tagged · clinician-prescribed, PDP quiz-gated |
| Foundayo™ | buyable | /med/ | (no PDP — /lp/clinical quiz route) | — | on-request | molecule not stated · oral (card tag) · Noom-branded oral · clinician-prescribed |

## Verbatim anchors

The footnotes the Price column points at (homepage / Microdose page / Med FAQ), quoted exactly:

- **GLP-1Rx (homepage footnote 1):** "Initial 3 week subscription and 4 weeks of medication from $149 plus tax and $349 per month plus tax for 12 week subscription thereafter. New pricing for new accounts only effective as of March 31, 2026." → `partial` (program floor; the medication itself can carry separate cost depending on insurance/cash-pay).
- **Microdose (homepage footnote 2 / Microdose page footnote 1):** "Initial 4 week subscription from $79 plus tax and $199 per month plus tax for 12 week subscription thereafter." → `partial`.
- **Microdose (Med FAQ):** "The Noom Microdose GLP-1Rx Program provides direct access to GLP-1s starting at $99, regardless of insurance, when prescribed." (a second framing of the same program; $99 = med-inclusive, $79 = subscription start.)
- **Brand-name (Med FAQ):** "Noom Med also includes access to brand-name medications like Ozempic® and Zepbound® starting at $69 plus any out-of-pocket cost for the medication itself depending on insurance coverage." → the `$69` is the program floor; the drug cost is separate ⇒ brand rows `on-request`.
- **GLP-1 Companion (PDP FAQ):** "Noom's GLP-1 Companion is included at no additional cost with a Noom plan for eligible members taking GLP-1 medication." → `published` (no-cost add-on, bundled with a Noom plan).
- **Molecule-sourcing audit (the `not stated` rows):** Wegovy® Pill, Foundayo™ — card tag is `[ORAL]` (form), no molecule named in product copy (the disclaimer's "semaglutide → Wegovy" is a footnote, excluded from attestation). Generic liraglutide / Metformin — molecule = the SKU name itself (generic INN, page-stated). Brand injectables (Wegovy/Ozempic/Zepbound/Mounjaro) carry an explicit molecule card tag.

## Deep blocks

None earned — the roster carries this company. The medication "SKUs" share one PDP shell (`/med/<brand>/` → safety-info + a quiz CTA) and one price story (program floor + clinician-selected drug); a per-drug deep-dive would re-quote the same gated-quiz pattern without resolving a real ambiguity. The one genuine nuance — that prices are program-level, not per-drug — is captured in the Portfolio overview.

## Provenance

- **Pages read:** `/med/` (the roster backbone — drug cards + molecule tags + the price FAQ), `/med/glp1-microdose/` (Microdose pricing + footnote), `/med/glp1-companion/` (Companion no-cost framing), homepage (program pricing footnotes), `/glp-1-access-and-transparency/` (compounded/generic/brand confirmation). Captured 2026-06-04 under `captures/2026-06-04/`.
- **Scope:** enumerated at the program + medication-option level (the level `/med/` indexes at). The individual brand-drug PDPs (`/med/wegovy/`, `/med/ozempic/`, …) were **not scraped** — their slugs are attested links from `/med/`, but per-drug pricing/dosing is quiz-gated and noted `on-request`.
- **Gated / unreachable:** per-drug prices, dose ladders, and the GLP-1Rx Plus tier price (all behind the `/ps/` + `/lp/clinical` intake quiz).
- **Point-in-time:** pricing runs new-account promos and is explicitly dated ("effective as of March 31, 2026"); re-check next run.
- **Run profile:** opt-in `offerings.md` enabled in the guided pre-flight (emphasis "center on Noom Med"); standard roster, no added columns or PDP-anatomy block, no hero-image capture.
