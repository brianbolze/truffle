---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: getpetermd.com
captured_at: 2026-06-04
site_notes: "Catalog backbone = the public WooCommerce Store API `GET /wp-json/wc/store/v1/products?per_page=100` (145 products, 2 pages) → persisted verbatim to captures/2026-06-04/wc-catalog.md (every price greppable there). Roster indexed at the MEDICATION level (the nav grain: /sildenafil, /tirzepatide, /mens-trt), not the ~145 dose/term leaf SKUs. Prices PDP-side AND in the public API — unusually transparent for the cohort. Plan-tier framing on PDPs (monthly/bi-yearly/yearly, yearly cheapest); WC API shows the per-SKU buyable price (often a 'paid-in-full' lump). Many catalog SKUs sit behind a 'NEEDS PORTAL INVITE' WooCommerce category (consult-approval before purchase) but STILL show a price. Intro 'Get Started' prices understate ongoing (Tirzepatide $149→$249/mo). Re-check prices next run — point-in-time."
---

## Portfolio overview

A broad **Multi-product** men's-health catalog across six care lines plus standalone labs, a women's line, supplements, and merch. The shape worth flagging: PeterMD is **fully price-published** — every medication carries a visible price on its PDP *and* in a public WooCommerce Store API, so the whole roster tags `published` (no quiz-wall — the structural contrast with Hims/Ro, who gate price behind intake). The "indexed level" is the medication (the nav grain); each medication fans out into dose/quantity/term leaf SKUs in the WC catalog (e.g. Sildenafil → 10/15/20/30-tab packs), summarized as a price range here.

Prominence (nav order ∩ homepage section order ∩ about-page grid):
- **Testosterone / TRT `[HIGH]`** — the company's own lead: first nav item, the hero ("Understanding Your Testosterone Levels"), the founding line, the only line with a 6-month commitment.
- **Weight loss (GLP-1 / Tirzepatide) `[MED]`** — nav #2, heavy homepage real estate, the category-of-the-moment.
- **Sexual wellness `[MED]`** — nav #3 (top nav relabeled "Improve Sexual Function"), deep SKU count (19 ED leaf SKUs).
- **Performance · Longevity · Hair `[LOW]`** — present and priced, lower placement.
- Coverage (blind-source agreement: homepage nav ∩ WC Store API ∩ /map `/product/*` slugs): TRT · GLP-1/weight · sexual-health/ED · peptides/performance · longevity/NAD · hair · labs · women's HRT · supplements.

## Roster

Complete at the **medication (indexed) level**; family rows are the care lines. Price = verbatim entry→range across the line's leaf SKUs (full per-dose prices in `captures/2026-06-04/wc-catalog.md`). All `published`.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Increase Testosterone | family | — | `/buy-testosterone-therapy` | — | — | TRT care line · the funnel spine |
| Injectable TRT | buyable | Increase Testosterone | `/mens-trt` | "$79"–"$139" /mo by term (reg "$1668") | published | testosterone (cypionate) · IM injection · Rx, free consult → in-person labs (Ryan Haight), 6-mo commitment |
| Oral TRT (Enclomiphene) | buyable | Increase Testosterone | `/enclomiphene` | "$278.00" /bimonthly | published | enclomiphene ("purified isomer of Clomid") · oral · Rx |
| HCG | buyable | Increase Testosterone | `/hcg` | "$147.00" (10000iu "$301.00") | published | HCG · injection · Rx |
| Lose Weight | family | — | `/pmd-weight-loss` | — | — | medical weight-loss care line |
| GLP-1 (semaglutide) | buyable | Lose Weight | `/glp1-b12` | "$270.00" /mo sub (reg "$417.00") | published | semaglutide (WC category "SEMAGLUTIDE"; compounded, w/ B12) · injection · Rx |
| Tirzepatide | buyable | Lose Weight | `/tirzepatide` | "$149" start → "$249 per month"; 60mg "$647.00", 120mg "$1,094.00" | published | tirzepatide ("AKA Zepbound", GLP-1/GIP) · injection · "compounded version… combines an active B vitamin" |
| B12 + MIC | buyable | Lose Weight | `/b12-mic` | "$79.00" (B12 alone "$59.00") | published | MIC + B12 · injection · lipotropic adjunct |
| Improve Sexual Function | family | — | `/sexual-wellness` | — | — | ED / sexual-health care line (19 ED leaf SKUs) |
| Sildenafil | buyable | Improve Sexual Function | `/sildenafil` | "$62.50"–"$180.00" by tab count | published | sildenafil ("active ingredient in Viagra", FDA-approved) · oral tablet · Rx |
| Tadalafil | buyable | Improve Sexual Function | `/tadalafil` | "$72.50"–"$210.00" by tab count | published | tadalafil (FDA-approved) · oral tablet · Rx |
| Mount Everest | buyable | Improve Sexual Function | `/mount-everest` | "$50.00"–"$300.00" by supply | published | compounded ED combo (sildenafil/tadalafil family) · oral · Rx |
| Scream Cream | buyable | Improve Sexual Function | `/scream-cream` | "$107.00" | published | compounded topical arousal cream (women's) · topical · Rx |
| Cabergoline | buyable | Improve Sexual Function | `/cabergoline` | "$97.75" (reg "$104.00") | published | cabergoline 0.5mg · oral · Rx |
| Enhance Performance | family | — | `/enhance-performance` | — | — | peptide / performance care line |
| Sermorelin | buyable | Enhance Performance | `/sermorelin` | "$211.65" (1mo)–"$585.00" (3mo) | published | sermorelin · injection · compounded peptide, Rx |
| Thyroid Optimization | buyable | Enhance Performance | `/thyroid-treatment` | "$88.00" | published | thyroid treatment (molecule not stated) · Rx |
| Live Longer | family | — | `/live-longer` | — | — | longevity care line |
| Metformin | buyable | Live Longer | `/metformin` | "$60.00"–"$160.00" by supply | published | metformin 500mg · oral · Rx |
| NAD+ | buyable | Live Longer | `/nad` | injection "$369.00"; capsule "$125.65"–"$310.00" | published | NAD+ · injection or capsule · Rx/supplement |
| Hair Loss | family | — | `/hair-loss` | — | — | hair-loss care line |
| Finasteride | buyable | Hair Loss | `/finasteride` | "$60.00" (30) / "$90.00" (60) | published | finasteride 1mg (FDA-approved) · oral · Rx |
| Follicure RX (minoxidil) | buyable | Hair Loss | `/follicure-rx` | "$70.00" / "$140.00" (2-pack) | published | minoxidil · topical spray · Rx |
| ReGenX Bundle | buyable | Hair Loss | `/finasteride-minoxidil-bundle` | "$130.00" | published | finasteride + minoxidil bundle · oral + topical |
| Blood Work | family | — | `/blood-work` | — | — | standalone diagnostics (insurance-billable, $25 fee) |
| Testosterone Labs (In-Person) | buyable | Blood Work | `/testosterone-panel` | "$45.00" (reg "$190.00") | published | testosterone panel · lab draw · qualifying step for TRT |
| Thyroid Panel | buyable | Blood Work | `/thyroid-panel-with-tsh` | "$55.00" | published | thyroid panel w/ TSH · lab draw |
| For Her — Women TRT | buyable | For Her | `/women-trt-product` | "$198.00" /bimonthly | published | women's testosterone · Rx (parallel-gendered line) |
| For Her — Women's HRT | buyable | For Her | `/womens-al-la-carte-hrt` | à-la-carte "$188.00"; 1-hormone "$447.00"/qtr; all-incl "$567.00"/qtr | published | women's HRT · Rx |

## Verbatim anchors

The footnotes the Price column leans on, quoted from the cited captures:

- **TRT term ladder** (`/mens-trt`): "$79/Month" (yearly), "$109/Month" (bi-yearly), "$139/Month" (monthly); "Regular price: $1668"; 6-month minimum commitment (how_it_works.md: "the only exception being our TRT programs which will require at least a 6 month commitment").
- **Tirzepatide** (`/tirzepatide`): "Get Started for $149" then "$249 per month"; WC leaf SKUs "Tirzepatide – 60mg — $647.00", "Tirzepatide – 120mg — $1,094.00"; "We offer a compounded version the combines an active B vitamin" (molecule + compounding attestation, verbatim).
- **Sildenafil** (`/sildenafil`): "$62.50" (Tier 1, 10 tablets), "$90.00" (15), "$120.00" (20), "$180.00" (30); "SILDENAFIL IS THE ACTIVE INGREDIENT IN VIAGRA, WHICH IS FDA-APPROVED TO TREAT ED."
- **Price floor** (how_it_works.md): "Our plans start from as little as $29 per month."
- **Molecule-sourcing audit:** molecules attested by generic product name + PDP/WC copy where present (sildenafil/tadalafil/finasteride explicitly "FDA-approved"; tirzepatide named + compounding stated). `semaglutide` for the GLP-1 line is taken from the WC product **category label "SEMAGLUTIDE"**, not PDP prose — flagged, not asserted as PDP-attested. `Thyroid Optimization` molecule **not stated** on captured pages (no levothyroxine/T3 attestation) — left "not stated". Mount Everest's exact compound ratio not enumerated on captured pages.

## Deep blocks

Earned only where a roster row can't carry the nuance.

### Injectable TRT — the $79 headline vs. the real ladder
The hero "$79/month" is the **yearly-plan, 6-month-committed** floor; month-to-month is "$139/Month" and bi-yearly "$109/Month" (all three shown on `/mens-trt`; reg "$1668"). Unlike the rest of the catalog, TRT is **gated by in-person labs first** (Ryan Haight, Schedule-III testosterone) and a **6-month lock-in** — the one line where "cancel anytime" doesn't apply. Hero render: `captures/2026-06-04/images/testosterone.png` (testosterone-cypionate vial).

### Tirzepatide — "compounded version… combines an active B vitamin"
The disambiguation a roster row flattens: PeterMD's tirzepatide is a **compounded tirzepatide + B-vitamin** preparation (PDP, verbatim), not branded Zepbound/Mounjaro ("AKA: Zepbound" is used descriptively for the molecule). Dual GLP-1/GIP. Priced as an intro ("$149") → ongoing ("$249 per month") with dose tiers in the WC catalog (60mg "$647.00", 120mg "$1,094.00"). Hero render: `captures/2026-06-04/images/tirzepatide.png`.

### Hero product renders (opt-in asset capture — this run)
Clean isolated product renders pulled from the WooCommerce CDN (transparent PNGs, ~800px), one per care line — for a design / rendering-reference consumer. Saved to `captures/2026-06-04/images/`:

- **testosterone.png** — TRT (Testosterone-Cypionate vial) · flagship `/mens-trt`
- **tirzepatide.png** — Weight loss (Tirzepatide liquid vial) · flagship `/tirzepatide`
- **sildenafil.png** — Sexual wellness (Sildenafil tablets) · flagship `/sildenafil`
- **sermorelin.png** — Performance (Sermorelin syringe) · flagship `/sermorelin`
- **nad.png** — Longevity (NAD+ vial) · flagship `/nad` (394px — smaller source)
- **finasteride.png** — Hair loss (Finasteride bottle) · flagship `/finasteride`

## Provenance

- **Pages:** the public **WooCommerce Store API** (`/wp-json/wc/store/v1/products?per_page=100`, 145 products → `wc-catalog.md`, free curl) as the priced backbone, reconciled against the homepage nav and three flagship PDPs (`/mens-trt`, `/tirzepatide`, `/sildenafil`, Firecrawl). Hero images headed-fetched from the WC CDN (free).
- **Scope:** enumerated at the **medication level** across all 6 care lines + labs + women's line (28 rows). NOT enumerated: every dose/quantity/term leaf SKU (those live in `wc-catalog.md`), supplements (29 SKUs), merch, and the BEARIT collection — noted, not rostered.
- **Visibility:** the entire roster is `published` — prices are shown on PDPs and exposed by a public API; no quiz-wall. Consult-gating ("NEEDS PORTAL INVITE" category) governs *purchase approval*, not price disclosure.
- **Point-in-time:** prices are a snapshot (plan-term tiers, intro/promo framing, dose ladders) — re-verify next run. No A/B tool fingerprinted, so the read is stable run-to-run.
- **Run profile:** offerings module run with the +hero-images archetype (6 flagship renders); no PDP-template-anatomy block (not requested).
