---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: defymedical.com
captured_at: 2026-06-04
site_notes: "Catalog indexes at the service-line level (/services/<line>); individual molecules/forms are configured per-protocol inside the gated Patient Portal (defymedicalstore.com) — NOT public priced SKUs, so the roster's 'indexed level' is the line, not the leaf. Only ONE line publishes on-site pricing: Trimix ($1.39–$3.30/injection + a $99 consult). Lab prices live on the separate testdefy.com store (not captured this run). Trimix is also the only line that enumerates named sub-products (Super Trimix, Bimix, Super Bimix, Quadmix, Super Quadmix). Most lines are marketing pages with no price and no per-SKU detail → on-request. Molecule attestation is thin off the 6 deep-captured PDPs; nav-only lines carry 'not stated'."
---

## Portfolio overview

Defy Medical is **Multi-product** — roughly **20 co-equal service lines** across Men's Health, Women's
Health, Weight Loss, General Healthcare, and Aesthetics. The honest **indexed level is the service line**, not
a SKU: the public site sells *access to a category of care*, and the specific molecule, form, and dose are
configured per-patient inside a paid consult and the gated Patient Portal. So this roster is **family-row heavy
by design** — enumerating it down to the med would mean fabricating SKUs the site never publishes.

**Pricing shape — almost entirely gated.** Defy markets **"No subscriptions or contracts… only pay for what
you need,"** but the *amounts* live behind a consult + the portal. **Exactly one line publishes an on-site
price: Trimix** (penile injection), at **"$1.39 to $3.30 per Injection"** plus a **"$99"** Trimix consult — and
even that is `partial` (the per-injection figure is med-only; the consult and shipping stack on top). Lab
pricing exists but on a *different* store (testdefy.com, not captured). Every other line is `on-request`.

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
| **Lab Testing** | family | — | `/services/lab-tests-online` | — | on-request | panels — Men's / Women's Complete Hormone Health, Thyroid Function, B12, CBC, STD, allergen · ordered on **testdefy.com** (prices on that store, not captured). |
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

- **Molecule sourcing audit** (where molecules ARE page-attested vs `not stated`):
  - **TRT** — testosterone (injectable/topical/pellet/nasal-gel) + supplemental meds: stated on /services/trt.
  - **Trimix family** — Phentolamine, Alprostadil, Papaverine (+ Atropine in Quadmix): stated on /services/trimix-injections.
  - **ED** — Sildenafil, Tadalafil, Trimix: stated on /services/trt (not on a captured ED PDP).
  - **BHRT** — estradiol, estriol, progesterone, testosterone, DHEA, pregnenolone: stated on /services/hormone-therapy.
  - **Semaglutide / Tirzepatide / Liraglutide** — stated on the two weight-loss PDPs.
  - **All other lines** — `not stated`: no PDP captured this run; molecule NOT inferred from the line name.

## Deep blocks

Only one line earns a block — it's the sole line with on-site pricing **and** a real `partial`-vs-`published`
disambiguation. Every other line is a marketing page with no price/SKU detail, so the roster carries them.

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

## Provenance

- **Pages read:** /services (rich index), /services/trt, /services/hormone-therapy,
  /services/semaglutide-for-weight-loss, /tirzepatide-online, /services/trimix-injections,
  /services/lab-tests-online, /about-us, /get-started, /about-us/about-us-vendor-information, homepage —
  Firecrawl, 2026-06-04 (shared with the profile.md capture).
- **Scope:** all ~20 service lines enumerated at the indexed (line) level from captured nav; the 6 deep-captured
  PDPs carry molecule/form detail, the rest carry `not stated`. Trimix's 6 named variants are the only
  enumerated sub-products. Per-protocol meds inside the Patient Portal and per-test lab SKUs on testdefy.com are
  **noted but not enumerated** (gated / off-host).
- **Gated / unreachable:** medication prices (paid consult + Patient Portal); lab prices (testdefy.com store, not
  captured); per-consult fees beyond Trimix's $99 (FAQ-referenced, amounts not captured).
- **Point-in-time:** the lone published price (Trimix) is "an estimate and not a price guarantee."
- **Run profile:** guided — telehealth cohort run; `offerings.md` + a hero **product image** were requested.
  Image capture ran on the flagship PDPs; only Trimix yielded a product-style asset (promoted) — the rest of the
  site is lifestyle/icon imagery (services clinic, no isolated SKU renders).
