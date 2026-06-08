---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: prohealth.com
captured_at: 2026-06-07
enumeration: indexed-complete    # Catalog shape → indexed level = lines + tiers + marked exemplars, NEVER leaf SKUs. Roster count is an exemplar count, not a census.
site_notes: "Catalog = hundreds of SKUs across ~40 categories + ~50 active-ingredient filters (Shopify). Collection-grid prices LAZY-LOAD — NOT in markdown; verbatim $ greppable only on PDPs + the Rebuy 'you may also like' widget. Compounded-Rx SKUs (rx0NN) gate price behind a free online visit at rxcheckout.prohealth.com — on-request. To price the catalog, scrape PDPs (≈1 credit/SKU)."
---

## Portfolio overview

ProHealth Longevity is a **Catalog**-shape supplement maker/retailer with a thin compounded-Rx telehealth arm bolted on. The roster below is **shape + exemplars, not a census** — the catalog runs to hundreds of SKUs (own-brand + resold third-party) that aren't individually enumerated here.

Prominence (calibrated):
- **NAD+ / NMN line — `[HIGH]`:** the company's own hero. NMN/NAD+ is the homepage spotlight, the first nav item, and the "Product Spotlight," anchored on own-brand **Uthever® NMN**.
- **Pharmaceuticals (compounded Rx) — `[MED]`:** a dedicated top-level nav item and a "brand-new line," but secondary to the supplement core; lives off-store on the Rx subdomain.
- **At-home lab tests — `[LOW]`:** a small dedicated collection (one main SKU surfaced).
- **The broad supplement catalog — `[LOW]` each:** the long tail (~40 health categories), un-enumerable, the `Catalog` body.

The "shape" finding worth flagging: ProHealth's **"Pharmaceuticals"** are genuinely prescription/compounded (GLP-1, sermorelin, NAD+ injectables) sold via an online medical visit — distinct from the OTC supplement catalog they sit beside. And **BPC-157 is sold OTC** here as a capsule supplement, *not* through the Rx flow.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| NAD+ Boosters | family | — | /collections/nad | — | — | NAD+ precursors (NMN · NR · NMNH · NADH) — the hero line |
| NMN Pro 1000™ — Uthever® *(exemplar)* | buyable | /collections/nad | /products/prohealth-longevity-nmn-pro-1000-enhanced-absorption-featuring-uthever-nmn-60-capsules-ph593 | One-time $64.95 / Subscribe & Save $58.46 | published | Uthever® NMN (nicotinamide mononucleotide) · 1000 mg/serving, 60 capsules · OTC, one-time or autoship |
| NMN Pro™ 500 — Uthever® *(exemplar)* | buyable | /collections/nad | /products/prohealth-nmn-pro-500-enhanced-absorption-500-mg-60-capsules-ph583 | $42.95 | published | Uthever® NMN · 500 mg, 60 capsules · OTC |
| Pure BPC-157 *(exemplar)* | buyable | /collections/all | /products/prohealth-bpc-157-500-mcg-60-capsules-ph703 | $119.95 | published | BPC-157 · 500 mcg, 60 capsules · OTC supplement (NOT the Rx flow) |
| Pharmaceuticals (compounded Rx) | family | — | /collections/pharmaceuticals | — | — | online visit → licensed provider → compounding pharmacy |
| Personalized GLP-1 Injection *(exemplar)* | buyable | /collections/pharmaceuticals | /collections/pharmaceuticals/products/prohealth-longevity-personalized-glp-1-injection-rx013 | — (behind free consult) | on-request | semaglutide / tirzepatide (+B12) · subcutaneous injection · quiz + provider-gated, cash-pay |
| Compounded Sermorelin | buyable | /collections/pharmaceuticals | /collections/pharmaceuticals/products/prohealth-longevity-compounded-sermorelin-rx005 | — | on-request | sermorelin · injection · Rx compounded |
| NAD+ Injection | buyable | /collections/pharmaceuticals | /collections/pharmaceuticals/products/prohealth-longevity-nad-injection-10-ml-rx001 | — | on-request | NAD+ · injection, 10 mL one-month supply · Rx compounded |
| NAD+ Nasal Spray | buyable | /collections/pharmaceuticals | /collections/pharmaceuticals/products/prohealth-longevity-nad-nasal-spray-rx010 | — | on-request | NAD+ · nasal spray · Rx |
| Metformin | buyable | /collections/pharmaceuticals | /collections/pharmaceuticals/products/prohealth-metformin-500-mg-30-capsules-rx007 | — | on-request | metformin · 500 mg, 30 tablets · Rx |
| Methylene Blue | buyable | /collections/pharmaceuticals | /collections/pharmaceuticals/products/prohealth-longevity-methylene-blue-15-mg-rx006 | — | on-request | methylene blue · 15 mg, 30 capsules · Rx |
| At-Home Lab Tests | family | — | /collections/testing | — | — | at-home diagnostic kits |
| TruMe Biological Age Test *(exemplar)* | buyable | /collections/testing | /collections/testing/products/trume-at-home-dna-biological-age-test-tst100 | — (not captured) | published | DNA biological-age / methylation test · at-home kit · OTC |
| Broad supplement catalog | family | — | /collections/all | — | — | ~40 categories (adaptogens · sleep · mood · immune · cardiovascular · joint · blood-sugar · nootropics · beauty · antioxidants · methylation …) + ~50 single-ingredient filters; own-brand + resold (e.g. Niagen® NR). Catalog — not enumerated. |
| Bulk supplements | family | — | /collections/bulk-supplements | — | published | bulk NMN · berberine · TMG · trans-resveratrol (100 g–1 kg) — wholesale on wholesale.prohealth.com |

## Verbatim anchors

- **NMN Pro 1000 (ph593 PDP):** *"One-time Purchase $64.95 / Subscribe & Save 10% $58.46"*; *"60 Capsules, 1000mg per serving • SKU: PH593"*; *"Uthever® NMN… the world's first clinically studied NMN brand."*
- **NMN Pro 500 / BPC-157 (homepage Rebuy widget):** *"NMN Pro™ 500 — Uthever® NMN — 500 mg, 30 servings … Price $42.95"*; *"Pure BPC-157 — 500 mcg, 60 capsules … Price $119.95."*
- **GLP-1 (rx013 PDP) — why on-request:** *"Complete a brief quiz, get matched with the right medication, and receive treatment delivered straight to your home."* No price is shown on the PDP; the only CTA is *"Start Your Free Consultation"* → `rxcheckout.prohealth.com/start-online-visit/rx013`. Molecule page-attested: *"Semaglutide / Tirzepatide," "Semaglutide +B12."*
- **Pharmaceuticals positioning:** *"the same powerful ingredients found in popular prescriptions like Ozempic®, Wegovy®, Mounjaro®, Zepbound®, and clinical NAD+ infusions—without the hefty price tag… All prescriptions are compounded by a US-licensed pharmacy."*

## Deep blocks

- **The compounded-Rx flow (earns a block — resolves "how does a supplement store sell prescriptions?").** The `/collections/pharmaceuticals` SKUs (`rx0NN` slugs) are **not normal add-to-cart products** — each routes to a **free online medical visit** off the main store. Page-attested 4 steps: *"Take the quiz → Provider Review [a licensed doctor reviews and prescribes] → prescription shipped directly from a certified pharmacy."* Clinical layer is **Beluga Health (c/o Jonah Mink MD)**; pharmacy is an unnamed **US-licensed compounding pharmacy**. Price is therefore **never shown pre-consult** → every `rx0NN` row is `on-request`. This is the one line where the roster's price column is structurally empty by design, not by capture gap. (Full vertical classification in `telehealth.md`.)
- **PDP-template anatomy:** not captured (not requested this run).

## Provenance

- **Pages read:** homepage (Rebuy widget prices), /collections/nad (rich), /collections/pharmaceuticals, /collections/testing, /pages/faq, /products/…nmn-pro-1000-ph593 (PDP), /collections/pharmaceuticals/products/…personalized-glp-1-rx013 (PDP). All Firecrawl, `location:US`, `maxAge:0`.
- **Scope note:** **Catalog shape — indexed at line + exemplar grain, NOT a census.** Lines enumerated: NAD+ boosters, Pharmaceuticals (all 6 rx SKUs listed), At-Home Lab Tests, Bulk, and the broad supplement catalog (as one un-enumerated `Catalog` family). **Leaf SKUs across the ~40 supplement categories and ~50 ingredient filters are intentionally not rostered** (Catalog rule). Only 4 prices are grep-verifiable ($64.95, $58.46, $42.95, $119.95) — every other row is unpriced because collection grids lazy-load prices and PDPs weren't swept. Do **not** read the row count as catalog breadth.
- **Point-in-time:** pricing reflects promos/Subscribe & Save active 2026-06-07; the pharma line is a "brand-new" arm and may expand.
- **Run profile:** express add-on alongside profile.md + telehealth.md; vanilla roster (no PDP-anatomy block, no hero images).
