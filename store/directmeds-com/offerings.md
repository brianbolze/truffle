---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: directmeds.com
captured_at: 2026-06-04
site_notes: "Catalog = /all-solutions/<category>/ listing cards (product name + monthly price + /medications/<slug> link) — the authoritative backbone; commerce/checkout lives in the /portal app (not scraped). Detail PDPs at /medications/<slug> are WP marketing pages with the all-inclusive monthly price at the BOTTOM and the molecule on an 'Important' line. PRICES DISAGREE listing vs PDP for the GLP-1 injections (semaglutide-10: $297.00 listing / $347 PDP; tirzepatide: $399.00 listing / $547 PDP), and decimal listing prices ($179.10, $224.10) imply a new-customer promo — point-in-time. Molecule is page-attested on the 4 captured PDPs (sema, tirz, elastira, ortharex) and from listing-heading parentheticals; non-captured PDPs leave form/molecule 'not stated'. No ED product page despite ED blog content."
---

## Portfolio overview

`Multi-product` telehealth catalog with a clear **GLP-1 weight-loss anchor [HIGH** — JSON-LD title "Buy GLP-1 Medications Online," hero, the dedicated GLP-1 buying guide, and the popular-meds carousel all lead with semaglutide/tirzepatide**]** and a broad compounded long-tail across six wellness categories (anti-aging/longevity, hair, skin, pain, muscle/energy) **[LOW–MED** — equal-weight category grid, single PDP each**]**. Two shape findings matter: (1) the weight-loss line splits into **compounded Rx GLP-1** (semaglutide & tirzepatide, each injection + sublingual drops) and a separate **OTC appetite-supplement** sub-line (Citradine/Sinetrol, SatiaLean/DNF-10, Calocurb) — different lanes under one category; (2) **prices are inconsistent across surfaces** — the same SKU shows one figure on the category listing and a higher one on its PDP, and the listing GLP-1 prices carry promo decimals. All SKUs are all-inclusive monthly, cash-pay, no membership. The split that drives `Visibility`: the **GLP-1 Rx** lines are dose-laddered and disagree listing↔PDP → `partial`; the **fixed supplements/topicals/hair** lines show a single self-contained monthly price → `published`.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Semaglutide (injection) | buyable | — | /medications/semaglutide-10 | "$297.00 / mo." (listing; PDP states "$347/month") | partial | semaglutide (compounded GLP-1 RA) · once-weekly subcutaneous injection · Rx, quiz-gated |
| Semaglutide (sublingual) | buyable | — | /medications/semaglutide-sublingual-drops | "$179.10 / mo." | partial | semaglutide (compounded) · sublingual drops (under-tongue, every 1–2 days) · Rx, quiz-gated |
| Tirzepatide (injection) | buyable | — | /medications/tirzepatide | "$399.00 / mo." (listing; PDP states "$547/month") | partial | tirzepatide (compounded, dual GLP-1/GIP) · once-weekly subcutaneous injection · Rx, quiz-gated |
| Tirzepatide (sublingual) | buyable | — | /medications/tirzepatide-sublingual-drops | "$224.10 / mo." | partial | tirzepatide (compounded) · sublingual drops · Rx, quiz-gated |
| Citradine (Sinetrol) | buyable | — | /medications/citradine-sinetrol | "$59.99 / mo." | published | Sinetrol (botanical appetite-control ingredient) · not stated · OTC supplement |
| SatiaLean (DNF-10) | buyable | — | /medications/satialean-dnf-10 | "$59.99 / mo." | published | DNF-10 (botanical appetite-control ingredient) · not stated · OTC supplement |
| Calocurb | buyable | — | /medications/calocurb | "$79.99 / mo." (listing renders "$$79.99 / mo.") | published | not stated · not stated · OTC supplement |
| Sermorelin (Sermorix) | buyable | — | /medications/sermorix-sermorelin | "$299.99 / mo." | published | sermorelin (peptide / GH secretagogue) · not stated · Rx |
| NAD+ | buyable | — | /medications/nad | "$399.99 / mo." | published | NAD+ · not stated · Rx |
| Elastira | buyable | — | /medications/elastira | "$139.00 / mo." | published | Tretinoin 0.025% · Glycolic Acid 8% · Niacinamide 4% · Hyaluronic Acid 0.5% (compounded) · topical cream (nightly) · Rx |
| Ortharex | buyable | — | /medications/ortharex | "$139.99 / mo." | published | Diclofenac 3% · Baclofen 2% · Lidocaine 5% · Meloxicam 1% (compounded) · topical cream (2–3×/day) · Rx |
| Minoxalune (Minoxidil) | buyable | — | /medications/minoxalune-minoxidil | "$89.00 / mo." | published | minoxidil · not stated · Rx/OTC, quiz-gated |
| Capilyn (Finasteride) | buyable | — | /medications/capilyn-finesteride | "$89.00 / mo." | published | finasteride (page spells "Finesteride") · not stated · Rx |

## Verbatim anchors

The footnotes the Price column points at + the molecule-attestation audit:

- **All-inclusive framing (every PDP):** *"all-inclusive pricing … doctor visits, prescription medications, supplies, and ongoing support — all bundled into one predictable monthly fee."* No membership; HSA/FSA accepted; new-customer + 6-/12-month bulk discounts (homepage FAQ).
- **GLP-1 price conflict (drives `partial`):** Semaglutide injection — *"Direct Meds Semaglutide All-Inclusive Monthly Price: $347/month"* (/medications/semaglutide-10) **vs** listing *"$297.00 / mo."* (/all-solutions/weight-loss) **vs** FAQ *"$297/month for injections."* Tirzepatide injection — *"Direct Meds Tirzepatide All-Inclusive Monthly Price: $547/month"* (/medications/tirzepatide) **vs** listing *"$399.00 / mo."* The number that bills is set in the quiz-gated /portal checkout; not reconciled.
- **FAQ floor vs listing:** *"Plans start at $249/month for sublingual Semaglutide, and $297/month for injections"* (homepage FAQ) — yet the sublingual-Sema **listing** shows *"$179.10 / mo."* (and Tirz sublingual *"$224.10 / mo."*); the .10 decimals read as a ~10% new-customer discount on the displayed cards.
- **Calocurb typo:** the listing renders the literal string *"$$79.99 / mo."* (double dollar sign) — recorded as $79.99/mo.
- **Molecule audit (`not stated`):** Calocurb names no active on any captured page → `not stated` (not inferred as Amarasate). Sermorelin, NAD+, Minoxalune, Capilyn have **no captured PDP** → molecule taken from the listing-heading parenthetical (sermorelin / NAD+ / minoxidil / finasteride) but **form is `not stated`** (a PDP could also carry a different price than the listing, as the two GLP-1 PDPs did). Citradine "Sinetrol" / SatiaLean "DNF-10" are branded ingredients named in the listing heading; their underlying botanicals are not page-attested → kept as the named ingredient.
- **Compounded disclaimer (every Rx PDP):** *"Compounded medications are not FDA-approved. They are prepared by licensed compounding pharmacies under the supervision of healthcare providers."*

## Deep blocks

- **GLP-1 injection price conflict** — `/medications/semaglutide-10` & `/medications/tirzepatide`. The only ambiguity a roster row can't carry cleanly: the same SKU is priced **lower on its category listing than on its own PDP**, with a third figure in the FAQ. Verbatim, semaglutide injection: PDP **"$347/month"** · listing **"$297.00 / mo."** · FAQ **"$297/month for injections."** Tirzepatide injection: PDP **"$547/month"** · listing **"$399.00 / mo."** No page reconciles them; the all-in figure is finalized in the /portal quiz/checkout (not captured). Treat any single number as point-in-time. *(No per-flagship deep-dive quota applied; no PDP-anatomy block — not requested this run.)*

## Provenance

- **Pages read:** `captures/2026-06-04/` — homepage + all-solutions hub + 6 category pages (weight-loss, anti-aging, hair, skin, pain, muscle-energy) for the roster backbone/prices; 4 PDPs (semaglutide-10, tirzepatide, elastira, ortharex) for molecule/form attestation + the price conflict.
- **Scope:** all **13 distinct SKUs** across the 6 categories enumerated (complete at the indexed `/medications/<slug>` level). ED is **content-only** (blog posts, no product/category page) — noted, not rostered. GLP-1 dose ladders are not exploded into per-dose rows (quiz/portal-gated).
- **Gated/unreachable:** exact per-dose & per-plan prices set in the /portal checkout (not submitted); PDPs for the 9 non-GLP-1 SKUs not individually captured (prices from listings; could differ as the GLP-1 PDPs did).
- **Point-in-time:** prices are a snapshot and **disagree across surfaces** (listing/PDP/FAQ) with promo-looking decimals — re-capture before quoting.
- **Run profile:** guided — `offerings.md` enabled alongside `profile.md` + `telehealth.md` + `logos`; plain roster (no hero-image capture, no PDP-anatomy block).
