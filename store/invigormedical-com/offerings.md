---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: invigormedical.com
captured_at: 2026-06-04
site_notes: "Prices render on the HOMEPAGE carousels (the price source) — /function category pages omit prices; each /plans/<sku> PDP shows one price. Read 'Starting at $X' as a dose/tier floor (→ partial); a flat '$X per Month/Vial' is published. No membership/subscription gate. All Rx are compounded via named partner pharmacies (503A) except generic orals (sildenafil/tadalafil/finasteride/enclomiphene). Micro-dose GLP-1 variants + ReGrow appear in nav with NO rendered price. Homepage carousels rotate — treat prices as point-in-time."
---

## Portfolio overview

Invigor Medical sells a **~27-SKU, three-pillar prescription catalog — Weight Loss · Longevity · Sexual Health** — as a `Multi-product` DTC telehealth clinic. Every SKU is a `/plans/<sku>` PDP grouped under a `/function/<category>` hub. The defining shape facts:

1. **Prices are published up front — unusually transparent for the cohort.** The homepage carousels show a price for ~24 of 27 SKUs (no membership stacked on top, unlike Hone/Maximus). The visibility split is purely **"Starting at $X" (a dose/tier floor → `partial`, 14 SKUs)** vs. **a flat "$X per Month/Vial" (fully shown → `published`, 10 SKUs)**. Only the micro-dose GLP-1 variants and ReGrow show no price (`on-request`).
2. **Mostly compounded, a few generics.** GLP-1, Trimix, PT-141, NAD+, sermorelin, oxytocin, methylene blue, glutathione, GHK-Cu and TRT are **compounded** (each PDP: *"This is a compounded medication… not FDA-approved"*); sildenafil, tadalafil, finasteride and enclomiphene are generic oral molecules.
3. **"Testosterone" shows up twice** — a standalone **TRT injection** plan (Schedule III, labs-gated, "$49 to start → $199 plan") and **enclomiphene**, framed as *"a non-injectable option to help restore healthy testosterone levels."*
4. **Oral/injectable pairs.** Several molecules ship in both routes (NAD+, glutathione, sermorelin) as separate SKUs with separate prices — the oral is its own slug.

**Prominence (calibrated).** **GLP-1 weight loss is the commercial lead [HIGH]** — the #1 hero tile (*"GLP-1 Treatment — Achieve your goals, feel great doing it"*) and first product card. **TRT is co-lead [HIGH]** — the persistent sitewide banner *"Now Offering Testosterone Replacement Therapy."* **Trimix, NAD+, Sildenafil, PT-141 are the secondary hero cards [MED].** **Section order is mixed [LOW]:** the mega-nav runs Weight Loss → Longevity → Sexual Health, but the homepage category rows run Sexual Health → Longevity → Weight Loss — no single dominant pillar. **Carousel card order [LOW]** — the carousels rotate, so intra-category ranking is not a stable signal.

## Roster

Complete at the indexed (PDP-card) level across all three pillars — 27 buyable SKUs + 3 family rows. Within-company key = **Slug** (the `/plans/<sku>` relative URL, quoted exactly). Price quoted verbatim from the homepage carousel (or PDP where noted). Molecule/form is **page-attested only** — `not stated` where the page is silent; never inferred from the SKU name. Access is identical for every Rx: *"prescribed by a healthcare provider after an online consultation,"* 100% online, no membership — abbreviated **"Rx · online consult"** below.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Weight Loss** | family | — | `/function/weight-loss/` | — | — | Compounded GLP-1 line + B12/naltrexone adjuncts. |
| GLP-1 Treatments | buyable | Weight Loss | `/plans/glp-1-treatments/` | `Starting at $225` | partial | compounded **GLP-1** (specific molecule not page-named; semaglutide-class) · weekly injection · Rx · online consult. PDP confirms "$225", compounded; checkout `/checkouts/compounded-glp1-checkout/`. [hero render] |
| GLP-1 + GIP Treatments | buyable | Weight Loss | `/plans/glp-1-gip-treatments/` | `Starting at $350 per Month` | partial | compounded **GLP-1 + GIP** (dual-agonist; tirzepatide-class, not page-named) · weekly injection · Rx · online consult. |
| GLP-1 Micro-Dosing | buyable | Weight Loss | `/plans/micro-dose-glp-1-treatments/` | — (no price rendered) | on-request | compounded GLP-1, micro-dose protocol · injection · Rx · online consult. Nav-listed; no price on captured pages. |
| GLP-1 + GIP Micro-Dosing | buyable | Weight Loss | `/plans/micro-dose-glp-1-gip/` | — (no price rendered) | on-request | compounded GLP-1+GIP, micro-dose · injection · Rx · online consult. Nav-listed; no price on captured pages. |
| Lipo B12 Injections | buyable | Weight Loss | `/plans/buy-lipo-b12/` | `Starting at $110` | partial | **Lipo B12** (lipotropic + vitamin B12; "MIC"-class not detailed) · injectable · Rx · online consult. |
| LDN Boost | buyable | Weight Loss | `/plans/low-dose-naltrexone/` | `Starting at $180` | partial | **low-dose naltrexone (LDN)** · oral · Rx · online consult. "Normalizing metabolism, reducing cravings." |
| **Longevity** | family | — | `/function/longevity/` | — | — | The deepest pillar — cellular health, vitality/peptides, hair & skin. |
| NAD+ Injections | buyable | Longevity | `/plans/buy-nad-injections/` | `Starting At $340 per Month` | partial | **NAD+** ("Rx Only - Sterile Vial") · injectable (compounded) · Rx · online consult. "Cellular energy support." [hero render] |
| Oral NAD+ | buyable | Longevity | `/plans/buy-oral-nad/` | `Starting at $209 / Month` | partial | NAD+ · oral · Rx · online consult. |
| Glutathione Injections | buyable | Longevity | `/plans/buy-glutathione/` | `Starting at $155` | partial | **glutathione** (antioxidant) · injectable (compounded) · Rx · online consult. |
| Oral Glutathione | buyable | Longevity | `/plans/oral-glutathione/` | `Starting at $155 per Month` | partial | glutathione · oral · Rx · online consult. |
| Methylene Blue | buyable | Longevity | `/plans/buy-methylene-blue/` | `Starting at $225 per Month` | partial | **methylene blue** · oral (compounded) · Rx · online consult. |
| Sermorelin Injections | buyable | Longevity | `/plans/buy-sermorelin/` | `Starting At $220` | partial | **sermorelin** — *"synthetic peptide that stimulates the release of growth hormone"* (GHRH analog; compounded) · injectable · Rx · online consult. [hero render] |
| Oral Sermorelin | buyable | Longevity | `/plans/oral-sermorelin/` | `Starting At $163 1st Month` | partial | sermorelin · oral · Rx · online consult. |
| B12 Injections | buyable | Longevity | `/plans/buy-vitamin-b12/` | `$90 per Month` | published | **vitamin B12** · injectable · Rx · online consult. |
| Enclomiphene | buyable | Longevity | `/plans/buy-enclomiphene/` | `$75 per Month` | published | **enclomiphene** · oral · Rx · online consult. *"A non-injectable option to help restore healthy testosterone levels."* |
| Testosterone Replacement Therapy | buyable | Longevity | `/plans/testosterone-replacement-therapy-injection/` | `Get Started For $49` (PDP: "$49 lab fee… fully credited"; "TRT Injectable Starting at $199") | partial | **testosterone** (ester not stated) · injectable (compounded) · Schedule III; **labs required** · Rx · online consult. [anchor: TRT structure] |
| Finasteride | buyable | Longevity | `/plans/buy-finasteride/` | `Starting at $109 per Month` | partial | **finasteride** · oral · Rx · online consult. *"Reducing DHT levels to preserve and regrow hair."* |
| Oral GHK-Cu | buyable | Longevity | `/plans/oral-ghk-cu/` | `Starting at $230 per Month` | partial | **GHK-Cu** (copper peptide) · oral · Rx · online consult. |
| Follicle Fuel | buyable | Longevity | `/plans/follicle-fuel/` | `Starting at $99 per Month` | partial | molecule **not stated** (hair-growth formula) · form not stated · Rx · online consult. |
| ReGrow | buyable | Longevity | `/plans/regrow/` | — (no price rendered) | on-request | molecule **not stated** (hair regrowth) · form not stated · Rx · online consult. Nav-listed; no price on captured pages. |
| **Sexual Health** | family | — | `/function/sexual-health/` | — | — | ED orals + compounded resistant-ED/libido injectables. |
| Sildenafil | buyable | Sexual Health | `/plans/buy-sildenafil/` | `Starting at $100 per Month` | partial | **sildenafil** ("The Classic") · oral · Rx · online consult. |
| Tadalafil | buyable | Sexual Health | `/plans/buy-tadalafil/` | `Starting at $100 per Month` | partial | **tadalafil** · oral · Rx · online consult. |
| Trimix Injections | buyable | Sexual Health | `/plans/buy-trimix/` | `$229 per Vial` | published | **papaverine + phentolamine + prostaglandin E1** (page-attested; "custom-compounded") · intracavernosal injection · Rx · online consult. [hero render] [anchor: molecule] |
| Passion+ | buyable | Sexual Health | `/plans/buy-passion/` | `$300 per month` | published | molecule **not stated** (combination intimacy formula) · form not stated · Rx · online consult. |
| Oxytocin | buyable | Sexual Health | `/plans/buy-oxytocin/` | `$220 per Month` | published | **oxytocin** · form not stated (sublingual/troche-class) · Rx · online consult. |
| Oxytocin Nasal Spray | buyable | Sexual Health | `/plans/buy-oxytocin-nasal-spray/` | `$135 per Month` | published | **oxytocin** · nasal spray · Rx · online consult. |
| PT-141 | buyable | Sexual Health | `/plans/buy-pt-141/` | `$280 per Month` | published | **PT-141** (named only "PT-141"; bremelanotide not stated) · injectable (compounded) · Rx · online consult. [hero render] |

**Buyable count: 27** — 6 Weight Loss + 14 Longevity (5 cellular + 5 vitality + 4 hair/skin) + 7 Sexual Health. The 3 `family` rows are non-buyable hubs, not counted.

### Verbatim anchors

The footnotes the Price/Visibility/What columns point at — quoted exactly from the cited captures.

- **The visibility rule (no membership stack).** Unlike the membership-gated peers, Invigor stacks **no** mandatory recurring fee on top — the carousel price *is* the price for flat SKUs. The only floor is dose/tier: a card reading **"Starting at $X"** → the real number rises with dose/strength at consult → `partial`; a flat **"$X per Month"** or **"$X per Vial"** → `published`.
- **[anchor: TRT structure] The TRT "$49 → $199" funnel.** Homepage card: *"Testosterone Replacement Therapy — Get Started For $49."* PDP: *"$49 Lab Fee Fully Credited Back — Once you're approved and ready to start treatment, you'll receive a $49 coupon to use on your TRT plan (starting at $199)."* and *"TRT Injectable Starting at $199 / Get $49 Credited Back / Once your labs are reviewed and you're approved, $49 is credited to your account."* → the **$49 is a labs-gate fee credited toward a plan that starts at $199**; hence `partial`.
- **[anchor: molecule] Trimix = 3 molecules, page-attested.** *"Trimix is a compounded injection that combines three medications: **papaverine, phentolamine, and prostaglandin E1**. This powerful combo relaxes the muscles and widens the blood vessels in the penis…"* (PDP). This is the only multi-molecule SKU stated explicitly.
- **Compounded disclaimer (verbatim, on every captured Rx PDP):** *"Compounded medications are legally prescribed under federal law but are not FDA-approved and have not undergone FDA review for safety, effectiveness, or manufacturing quality."* and *"Invigor Medical does not supply FDA-approved branded medications. Instead, compounded alternatives may be prescribed when clinically appropriate… prepared by licensed 503A pharmacies."*
- **GLP-1 non-affiliation (verbatim):** *"FDA-approved medications such as Saxenda®, Victoza®, Wegovy®, and Ozempic® are proprietary to Novo Nordisk™, while Mounjaro® and Zepbound™ are products of Eli Lilly… This website is not affiliated with, endorsed by, or associated with these companies."* → the GLP-1 SKU is a **compounded** alternative; the page never names its own molecule beyond "GLP-1."
- **Molecule-sourcing audit (page-attested only):**
  - **Trimix → papaverine + phentolamine + prostaglandin E1** (attested, above).
  - **Sermorelin → "synthetic peptide… growth hormone"** (GHRH analog) — attested on the PDP.
  - **PT-141 → named only "PT-141"** (bremelanotide NOT stated) — recorded as PT-141.
  - **GLP-1 / GLP-1+GIP → molecule not page-named** (semaglutide/tirzepatide implied by the GLP-1-vs-GLP-1+GIP split + the branded-drug disclaimer, but not stated for the SKU) — recorded "not page-named."
  - **TRT → "testosterone," injectable; ester (cypionate/enanthate) NOT stated.**
  - **Follicle Fuel · ReGrow · Passion+ → molecule "not stated"** (proprietary formula names).
  - Self-naming molecules (the SKU name *is* the molecule, attested in nav/copy): sildenafil, tadalafil, finasteride, enclomiphene, glutathione, methylene blue, NAD+, vitamin B12, low-dose naltrexone, oxytocin, GHK-Cu, Lipo B12.

## Deep blocks

Earned blocks for the SKUs where a verbatim molecule/price/structure resolves what a roster cell can't — and the **flagship hero product renders** the run requested (clean isolated vial shots, promoted to `captures/2026-06-04/images/`, referenced as assets, never roster columns).

### Flagship hero renders (asset index)

Five clean isolated product renders captured from the flagship PDPs (`fc.py hero`, top-candidate eyeballed), color-coded by molecule, promoted from `.payloads/hero/` to the durable `images/` dir:

- **GLP-1** (green vial) → `captures/2026-06-04/images/glp-1-treatments.webp`
- **NAD+** (blue vial, "Rx Only - Sterile Vial") → `captures/2026-06-04/images/buy-nad-injections.webp`
- **Trimix** (blue vial) → `captures/2026-06-04/images/buy-trimix.webp`
- **PT-141** (coral vial) → `captures/2026-06-04/images/buy-pt-141.webp`
- **Sermorelin** (orange vial) → `captures/2026-06-04/images/buy-sermorelin.webp`

*TRT has no clean isolated render — its PDP imagery is lifestyle/UI (a phone "Lab Order Confirmed," a delivery, a doctor), so no product shot was promoted.* All renders share one studio system: a single hand holding a labelled glass vial (or a free-standing vial) on a white/light ground, the "Invigor MEDICAL" wave mark on each label — a consistent, deck-ready asset set.

### Trimix Injections — the 3-in-1 compounded flagship (`$229 per Vial`, published)

- **Parent:** Sexual Health · **slug:** `/plans/buy-trimix/` · **price:** `$229 per Vial` · **visibility:** `published` · render: `images/buy-trimix.webp` (blue vial).

> **H1:** "Buy Trimix Injections." · Positioned for **resistant ED** — *"Proven results for men who've tried everything,"* *"For cases where oral medications aren't effective."*
> **Molecule (verbatim):** *"Trimix is a compounded injection that combines three medications: papaverine, phentolamine, and prostaglandin E1. This powerful combo relaxes the muscles and widens the blood vessels in the penis, helping you achieve a firm, long lasting erection fast and without relying on arousal."*
> **Compounded (verbatim):** *"\*Prescription medications available only if prescribed by the healthcare provider after an online consultation. This is a compounded medication."*

**Why it earns a block:** the only multi-molecule SKU, fully page-attested (papaverine/phentolamine/PGE1) — a roster cell can't carry the three-drug composition or the "resistant ED, when orals fail" positioning. Priced per **Vial** (one-time), not monthly — the cleanest `published` example.

### Testosterone Replacement Therapy — the labs-gated funnel (`$49 → $199`, partial)

- **Parent:** Longevity (Vitality) · **slug:** `/plans/testosterone-replacement-therapy-injection/` · **price:** `Get Started For $49` → plan `Starting at $199` · **visibility:** `partial` · Schedule III · no isolated render.

> **Banner (sitewide):** "Now Offering Testosterone Replacement Therapy." · **PDP:** "# How It Works — Start with $49. Get it back. Save on your first month." · *"Prescribed by U.S. Doctors, 100% online."*
> **Price structure (verbatim):** *"$49 Lab Fee Fully Credited Back — Once you're approved and ready to start treatment, you'll receive a $49 coupon to use on your TRT plan (starting at $199)."* · *"TRT Injectable Starting at $199 · Get $49 Credited Back."*
> **Compounded (verbatim):** *"Our partner compounding pharmacies… run quality control checks for every lot of compounded medications…"*

**Why it earns a block:** the price is a **two-stage funnel** (a $49 labs gate credited toward a ≥$199 plan) that a single Price cell flattens; it's the only **Schedule-III** SKU and the catalog's most-promoted line (the sitewide banner). The ester (cypionate/enanthate) is **not page-stated** — recorded as "testosterone, ester not stated."

### GLP-1 Treatments — compounded, not branded (`Starting at $225`, partial)

- **Parent:** Weight Loss · **slug:** `/plans/glp-1-treatments/` · **price:** `Starting at $225` · **visibility:** `partial` · render: `images/glp-1-treatments.webp` (green vial).

> **H1:** "Get Started on GLP-1 Treatment." · Hero tile: *"GLP-1 Treatment — Achieve your goals, feel great doing it"* (the #1 homepage card).
> **Compounded (verbatim):** *"The GLP-1 treatment available through Invigor Medical is prescribed based on an individualized medical evaluation by a licensed clinician."* + the full *"compounded… not FDA-approved"* disclaimer and the **Novo Nordisk / Eli Lilly non-affiliation** statement (Wegovy/Ozempic/Mounjaro/Zepbound).
> **Checkout:** routes to `/checkouts/compounded-glp1-checkout/`.

**Why it earns a block:** the commercial lead SKU, and the cleanest example of the catalog-wide pattern — a **compounded** alternative whose own molecule the page never names (only "GLP-1"), explicitly disclaiming the branded drugs it substitutes for. The GLP-1+GIP sibling implies tirzepatide-class but is likewise unnamed.

## Provenance

- **Pages read (10, all `captures/2026-06-04/`):** `homepage` (the price surface) + 3 category hubs (`cat-weight-loss`, `cat-sexual-health`, `cat-longevity`) + 6 flagship PDPs with `--images` (`pdp-glp1`, `pdp-trt`, `pdp-trimix`, `pdp-pt141`, `pdp-nad`, `pdp-sermorelin`). `/v2/map` (~470 URLs) confirmed the `/plans/*` catalog is complete at the card level. Context: [`profile.md`](profile.md), [`telehealth.md`](telehealth.md). All scrapes verified — sourceURLs match, bodies md5-unique.
- **Scope — enumerated:** all 27 `/plans/` SKUs (the indexed card level) across the 3 pillars, prices verbatim. **Not enumerated (PDP not captured):** 21 of 27 PDPs — molecule/form/price for non-flagship SKUs comes from the homepage cards + category/nav copy (page-attested), so non-flagship esters/molecules stay "not stated" where the card is silent.
- **Gated / unreachable:** prices for micro-dose GLP-1 (×2) + ReGrow (nav-listed, no rendered price → `on-request`); exact dose-tier pricing behind each "Starting at" floor (set at consult); the GLP-1/TRT specific molecules + esters (not page-named).
- **Run profile:** opt-in **hero product images** captured per the request — 5 flagship vial renders eyeballed from `fc.py hero` candidates and promoted to `captures/2026-06-04/images/` (referenced from the deep blocks as assets). Deep blocks limited to the 3 ambiguity-resolving flagships (Trimix molecules, TRT funnel, GLP-1 compounded-not-branded) + the render asset index; no per-flagship quota.
- **Point-in-time snapshot, not fixed:** homepage carousels rotate and TRT runs a "$49 get-started" promo — captured prices are a snapshot; this module's `captured_at` + a short TTL are the guard. Re-capture before trusting a price as current.
