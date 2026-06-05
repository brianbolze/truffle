---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: defymedical.com
captured_at: 2026-06-04
site_notes: "Two distinct catalogs. (1) CARE LINES on defymedical.com index at the service-line level (/services/<line>); molecules/forms are configured per-protocol inside the gated Patient Portal (defymedicalstore.com) — NOT public priced SKUs, so each care line's 'indexed level' is the line, not the leaf. Only Trimix publishes an on-site price ($1.39–$3.30/injection + a $99 consult) and is the only care line naming sub-products (Super Trimix, Bimix, Super Bimix, Quadmix, Super Quadmix). Other care lines are marketing pages → on-request; molecule attestation is thin off the 6 deep PDPs (nav-only lines = 'not stated'). (2) LAB TESTING routes off-host to testdefy.com — a Magento storefront with PUBLISHED prices: 263 à-la-carte LabCorp tests ($10–$1,179) + ~20 'popular' incl. ~14 curated panels ($59–$599). Index = /all-tests (alphabetical individual tests, paginate ?p=N); curated bundles = /popular-tests. À-la-carte tier = Catalog (exemplars only); curated panels = the indexed level to roster. NY/NJ/PA/RI/MA excluded by state law; lab results carry no provider review."
---

## Portfolio overview

Defy Medical is **Multi-product** — roughly **20 co-equal service lines** across Men's Health, Women's
Health, Weight Loss, General Healthcare, and Aesthetics. The honest **indexed level is the service line**, not
a SKU: the public site sells *access to a category of care*, and the specific molecule, form, and dose are
configured per-patient inside a paid consult and the gated Patient Portal. So this roster is **family-row heavy
by design** — enumerating it down to the med would mean fabricating SKUs the site never publishes.

**Pricing shape — care gated, labs published off-host.** Defy markets **"No subscriptions or contracts… only
pay for what you need,"** but for the **care/Rx lines** the *amounts* live behind a consult + the portal —
**exactly one care line publishes an on-site price: Trimix** (penile injection), at **"$1.39 to $3.30 per
Injection"** plus a **"$99"** Trimix consult, and even that is `partial` (med-only; the consult + shipping stack
on top). The exception is **Lab Testing**, which routes off-host to the **testdefy.com** storefront where
**every price is published**: 263 à-la-carte LabCorp tests **$10.00–$1,179.00** plus ~14 curated panels
(**$59–$599**), self-order, no consult. So the roster carries two priced surfaces — one `partial` (Trimix), one
fully `published` (the lab catalog) — and every other care line is `on-request`.

**Prominence (calibrated).**
- **Company-stamped "Popular" nav badges [HIGH]** (Defy's own label): **TRT, Erectile Dysfunction, Trimix,
  Hormone Therapy, Female Sexual Dysfunction, Semaglutide, Tirzepatide, Lab Testing, Ketamine Therapy,
  Hair Loss.**
- **Anchor positioning [HIGH]:** TRT / HRT — "The World's Leading Hormone Replacement Clinic," TRT is the first
  nav item, and Expert-Care copy "specializes in Men's Health… TRT."
- **Homepage "Core Services" foreground [MED]:** TRT + ED (For Men); Hormone Therapy + Sexual Dysfunction
  (For Women) — the four the homepage pulls out of the menu.
- Nav grouping order (Men's → Women's → Weight Loss → General → Aesthetics) and card order **[LOW]**.

## Roster

Complete at the indexed level (Defy's /services/* lines), grouped as the site groups them. Slugs are attested
from captured nav/PDPs. Price quoted verbatim where shown (Trimix only); molecule/form **page-attested only** —
`not stated` where no PDP was captured for that line (see the molecule audit under Verbatim anchors). A slug
here is never asserted equal to another brand's.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Testosterone Replacement Therapy (TRT)** | family | — | `/services/trt` | — | on-request | testosterone · injectable / topical / pellet / nasal-gel · + supplemental meds (testicular health, fertility, estrogen control); consult + portal-gated. |
| Erectile Dysfunction | family | — | `/services/erectile-disfunction` | — | on-request | sildenafil · tadalafil · trimix · oral + injection · attested via the TRT PDP ("ED medications like Sildenafil, Tadalafil, and Trimix"); no PDP captured. |
| **Trimix** | family | Erectile Dysfunction | `/services/trimix-injections` | `Trimix Injections from $1.39 to $3.30 per Injection.*` | partial | compounded penile (ICP) injection · Phentolamine + Alprostadil + Papaverine · med-only price; $99 consult + shipping on top (see anchors). |
| Super Trimix | buyable | Trimix | `/services/trimix-injections` | — | on-request | Phentolamine (doubled) + Alprostadil + Papaverine · injection · for non-responders to original Trimix. |
| Bimix | buyable | Trimix | `/services/trimix-injections` | — | on-request | Papaverine + Phentolamine (no Prostaglandin) · injection · for Prostaglandin-sensitive/allergic men. |
| Super Bimix | buyable | Trimix | `/services/trimix-injections` | — | on-request | Papaverine + Phentolamine (doubled) · injection · for non-responders to Bimix. |
| Quadmix | buyable | Trimix | `/services/trimix-injections` | — | on-request | Phentolamine + Alprostadil + Papaverine + Atropine · injection · usually for long-term Trimix patients. |
| Super Quadmix | buyable | Trimix | `/services/trimix-injections` | — | on-request | Quadmix with doubled Phentolamine · injection · reserved for severe ED. |
| Anabolic / Androgenic Therapies | family | — | `/services/anabolic-androgenic-therapies` | — | on-request | not stated · not stated · no PDP captured. |
| **Hormone Therapy (BHRT)** | family | — | `/services/hormone-therapy` | — | on-request | estradiol / estriol · progesterone · testosterone · DHEA · pregnenolone · injectable / topical / capsule / pellet (bioidentical); consult + portal-gated. |
| Menopause | family | — | `/services/menopause` | — | on-request | not stated · not stated · no PDP captured. |
| Female Sexual Dysfunction | family | — | `/services/female-sexual-dysfunction` | — | on-request | not stated · not stated · no PDP captured. |
| **Semaglutide** | family | — | `/services/semaglutide-for-weight-loss` | — | on-request | semaglutide · weekly GLP-1 injection · + adjuncts (B12, lipotropic, appetite suppressants, topical spot treatments); consult + portal-gated. |
| **Tirzepatide** | family | — | `/tirzepatide-online` | — | on-request | tirzepatide · weekly GIP/GLP-1 injection · "FDA-approved [for T2D] under a brand name"; consult + portal-gated. |
| Weight Management | family | — | `/services/weight-loss` | — | on-request | GLP-1 (semaglutide / tirzepatide / liraglutide) + adjuncts · attested via the Semaglutide/Tirzepatide PDPs; no own PDP captured. |
| **Lab Testing** | family | — | `/services/lab-tests-online` | — | on-request | off-host marketplace on **testdefy.com** (Magento): **263** à-la-carte LabCorp tests **$10.00–$1,179.00** + ~14 curated panels; self-order, no consult, **no provider review of results**; **NY/NJ/PA/RI/MA excluded**. Curated panels enumerated below; à-la-carte tier is Catalog (exemplars only). |
| Comprehensive Hormone & Wellness Panel — Men (Initial) | buyable | Lab Testing | `testdefy.com/717` | `$299.00` | published | LabCorp panel · blood draw · flagship men's hormone work-up (Defy's headline lab). |
| Comprehensive Hormone & Wellness Panel — Women (Initial) | buyable | Lab Testing | `testdefy.com/719` | `$299.00` | published | LabCorp panel · blood draw · flagship women's hormone work-up. |
| Ultra Comprehensive Wellness Panel — Men | buyable | Lab Testing | `testdefy.com/4562` | `$599.00` | published | LabCorp panel · blood draw · broadest men's panel (catalog ceiling for panels). |
| Ultra Comprehensive Wellness Panel — Women | buyable | Lab Testing | `testdefy.com/4561` | `$549.00` | published | LabCorp panel · blood draw · broadest women's panel. |
| STD Panel | buyable | Lab Testing | `testdefy.com/471` | `$284.00` | published | LabCorp panel · blood draw · common STDs. |
| Complete Thyroid Panel | buyable | Lab Testing | `testdefy.com/923` | `$245.00` | published | LabCorp panel · blood draw · hyper-/hypothyroid work-up. |
| Heart Health Lab Panel | buyable | Lab Testing | `testdefy.com/541` | `$237.00` | published | LabCorp panel · blood draw · cardiovascular markers. |
| Comprehensive Hair Loss Panel | buyable | Lab Testing | `testdefy.com/4155` | `$220.00` | published | LabCorp panel · blood draw · hair-loss work-up. |
| Comprehensive Weight-Loss Support Panel | buyable | Lab Testing | `testdefy.com/4563` | `$179.00` | published | LabCorp panel · blood draw · metabolism / fat-loss markers. |
| Vitamin/Mineral Panel | buyable | Lab Testing | `testdefy.com/4157` | `$139.00` | published | LabCorp panel · blood draw · vitamin & mineral status. |
| Annual Health Checkup Panel | buyable | Lab Testing | `testdefy.com/4158` | `$110.00` | published | LabCorp panel · blood draw · CMP + lipid + CBC bundle. |
| Weight Management Lab Panel | buyable | Lab Testing | `testdefy.com/943` | `$59.00` | published | LabCorp panel · blood draw · weight-gain marker screen (cheapest curated panel). |
| À-la-carte LabCorp test *(exemplar)* | buyable | Lab Testing | `testdefy.com/301` | `$20.00` | published | the 263-SKU Catalog leaf, **not** enumerated — e.g. CBC $20.00 (`/301`) · Hemoglobin A1c $25.00 (`/303-12`) · Testosterone Free+Total $39.00 (`id 5298`) · Allergen Profile, Respiratory Area-13 $899.00 (`/2157-l`); full range $10.00–$1,179.00. |
| Primary Care | buyable | — | `/services/primary-care` | — | on-request | not stated · telemedicine consult · no PDP captured. |
| Ketamine Therapy | buyable | — | `/services/ketamine-therapy` | — | on-request | ketamine · form not stated · no PDP captured. |
| Thyroid Disease | family | — | `/services/thyroid-therapy` | — | on-request | thyroid hormone (not further stated) · attested via Tirzepatide PDP cross-link; no own PDP captured. |
| Vitamins & Supplements | family | — | `/services/vitamins-and-supplements` | — | on-request | not stated · supplements via Fullscript (FAQ); wholesale-sourced; no PDP captured. |
| IV Therapy | buyable | — | `/services/iv-therapy` | — | on-request | not stated · IV infusion · no PDP captured. |
| Joint Pain | buyable | — | `/services/joint-pain` | — | on-request | not stated · not stated · no PDP captured. |
| Advice-Only Consultations | buyable | — | `/services/services-advice-only-consultation` | — | on-request | consult only · telemedicine · for international/out-of-network patients (no Rx shipped overseas). |
| Performance Consultations | buyable | — | `/services/sexual-performance-consults` | — | on-request | consult · telemedicine · sexual-health performance consult (FAQ notes a per-consult fee, amount not captured). |
| Hair Loss | family | — | `/services/hair-loss` | — | on-request | not stated · PRP referenced in nav/FAQ; no PDP captured. |
| Cosmetic Injections | buyable | — | `/services/cosmetic-injections` | — | on-request | not stated · injectable aesthetics · no PDP captured. |
| Skin Care | buyable | — | `/services/skin` | — | on-request | not stated · not stated · no PDP captured. |

## Verbatim anchors

- **Trimix price + footnote** (/services/trimix-injections), verbatim — the figures that decide `partial`:
  > "**Trimix Injections from $1.39 to $3.30 per Injection.\***"
  > "*Calculated from minimum dosage to maximum dosage. This is an estimate and not a price guarantee. Does not include the initial consultation or shipping. The Trimix consultation cost is **$99** and is specific to ICP injections. This consult does not include hormone evaluations or TRT.*"
  → med-only per-injection floor; a mandatory **$99** consult (+ shipping) sits on top → **`partial`**.

- **No-subscription / pay model** (/get-started, /services/semaglutide-for-weight-loss), verbatim:
  > "No subscriptions or contracts — You control your schedule and cost decisions, and only pay for what you need."
  > "To provide reliable and affordable pricing, Defy Medical does not accept insurance or communicate with insurance companies directly."

- **testdefy.com lab catalog** (/all-tests, /popular-tests), verbatim — the figures behind the `published` lab rows:
  > "All Tests — Items 1-15 of **263**"; price filter **"$10.00 … $1,179.00"**; "**263 products**".
  > "*Due to state regulations, Defy Medical does not offer on-demand lab testing in New York, New Jersey, Pennsylvania, Rhode Island, or Massachusetts.*"
  > "*This service does not include review of results by a medical provider.*"
  → labs are self-order, **published**, consult-free — the inverse of Defy's gated Rx lines.

- **Molecule sourcing audit** (where molecules ARE page-attested vs `not stated`):
  - **TRT** — testosterone (injectable/topical/pellet/nasal-gel) + supplemental meds: stated on /services/trt.
  - **Trimix family** — Phentolamine, Alprostadil, Papaverine (+ Atropine in Quadmix): stated on /services/trimix-injections.
  - **ED** — Sildenafil, Tadalafil, Trimix: stated on /services/trt (not on a captured ED PDP).
  - **BHRT** — estradiol, estriol, progesterone, testosterone, DHEA, pregnenolone: stated on /services/hormone-therapy.
  - **Semaglutide / Tirzepatide / Liraglutide** — stated on the two weight-loss PDPs.
  - **All other lines** — `not stated`: no PDP captured this run; molecule NOT inferred from the line name.

## Deep blocks

Two lines earn a block — the only two with real pricing structure: **Trimix** (on-site, the `partial`-vs-
`published` disambiguation) and **Lab Testing** (off-host testdefy.com, a published Catalog with a curated-panel
tier). Every other line is a marketing page with no price/SKU detail, so the roster carries them.

### Trimix — the one priced (and the only enumerated) line

- **Spine:** the only Defy line that publishes a number on-site, and the only one that names discrete
  sub-products. The price is **med-only and per-injection** — `partial`, because the all-in adds a mandatory
  **$99** ICP-specific consult plus shipping (verbatim footnote above). A vial "typically last[s] 2-3 months,"
  which is how Defy frames it as "a convenient and affordable ED therapy."
- **Formulations (page-attested), strongest → mildest selection logic:** Trimix → Super Trimix (2× Phentolamine)
  for non-responders; Bimix (drops Prostaglandin) for sensitivity/allergy → Super Bimix (2× Phentolamine);
  Quadmix (adds Atropine) for long-term patients → Super Quadmix (2× Phentolamine) for severe ED. "Most men
  start with the original Trimix formula and go from there."
- **Hero image (opt-in asset):** `captures/2026-06-04/images/trimix-medication.webp` — the page's clean isolated
  **medication icon** (blister pack + vial on a neutral ground). NB: this is the *only* product-style asset on
  the whole site; Defy is a services clinic, so there are **no photographic SKU renders** — other lines carry
  only lifestyle stock photography and category-icon illustrations.

### Lab Testing — the off-host published Catalog (testdefy.com)

- **Spine:** Defy's *only* fully `published` surface. /services/lab-tests-online is marketing; the actual store
  is **testdefy.com**, a Magento storefront selling **263** individual LabCorp tests from **$10.00 to
  $1,179.00**, self-order with **no consult and no provider review of results** — the inverse of Defy's
  consult-gated Rx care. **NY, NJ, PA, RI, MA are excluded** by state law.
- **Two tiers:** (1) the **263-SKU à-la-carte Catalog** — individual LabCorp assays (exemplars: CBC $20, A1c
  $25, Testosterone Free+Total $39, up to Allergen Respiratory Area-13 $899); (2) **~14 curated panels** (the
  indexed level rostered above), **$59–$599**, anchored by the **Comprehensive Hormone & Wellness** panels
  ($299 men / $299 women) and topped by the **Ultra Comprehensive Wellness** panels ($599 men / $549 women).
- **Catalog discipline:** the roster enumerates the finite curated-panel tier and leaves the 263 à-la-carte
  leaves as **shape + exemplars** (OFFERINGS Catalog rule), not SKU-by-SKU. Index pages for next run:
  `/all-tests` (alphabetical individual tests, paginate `?p=N`), `/popular-tests` (the curated set).

## Provenance

- **Pages read:** /services (rich index), /services/trt, /services/hormone-therapy,
  /services/semaglutide-for-weight-loss, /tirzepatide-online, /services/trimix-injections,
  /services/lab-tests-online, /about-us, /get-started, /about-us/about-us-vendor-information, homepage —
  Firecrawl, 2026-06-04 (shared with the profile.md capture).
  **Deepen run (2026-06-04):** testdefy.com/all-tests, testdefy.com/popular-tests (+`?p=2`) — the off-host lab
  store, capturing the curated-panel tier with verbatim prices.
- **Scope:** all ~20 care lines enumerated at the indexed (line) level from captured nav; the 6 deep-captured
  PDPs carry molecule/form detail, the rest carry `not stated`. Trimix's 6 named variants are the only
  enumerated sub-products among the care lines. The **testdefy.com lab store is now enumerated at the curated-
  panel tier** (~14 panels, published prices); its 263 à-la-carte LabCorp tests are left as Catalog exemplars.
  Per-protocol Rx meds inside the Patient Portal remain **noted but not enumerated** (gated).
- **Gated / unreachable:** medication prices (paid consult + Patient Portal, defymedicalstore.com); per-consult
  fees beyond Trimix's $99 (FAQ-referenced, amounts not captured).
- **Point-in-time:** the lone published price (Trimix) is "an estimate and not a price guarantee."
- **Run profile:** guided — telehealth cohort run; `offerings.md` + a hero **product image** were requested.
  Image capture ran on the flagship PDPs; only Trimix yielded a product-style asset (promoted) — the rest of the
  site is lifestyle/icon imagery (services clinic, no isolated SKU renders).
- **Run profile (deepen, 2026-06-04):** `/deepen-offerings` — chased the one breadth gap last run flagged, the
  off-host **testdefy.com** lab store. Lab Testing went from a single `on-request` family row to a published
  curated-panel tier (~14 panels, $59–$599) + Catalog exemplars; the main-host `/services` index was already
  complete (the only unrostered nav item, `/services/defy-medical-app`, is the patient app, not a care
  offering). +3 lab pages, 3 credits; no new spend on the care lines.
