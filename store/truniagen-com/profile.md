---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: truniagen.com
name: Tru Niagen
aliases: []
legal_entity: Niagen Bioscience, Inc.    # footer "© … Niagen Bioscience, Inc … All rights reserved" (storefront operating entity); confirmed by first-party SEC registered_name "Niagen Bioscience, Inc." (ticker CDXC, ex-ChromaDex). Tru Niagen is a consumer brand/line, not separately incorporated per the site.
parent: [niagenbioscience.com]           # nav "Our Parent Company - Niagen Bioscience" → niagenbioscience.com; about page "Developed by Niagen Bioscience, formerly ChromaDex"; SEC CDXC (ex-ChromaDex)
owns: []
socials:
  instagram: https://www.instagram.com/truniagen/
  facebook: https://www.facebook.com/TruNiagen
  linkedin: https://www.linkedin.com/company/niagenbioscience/   # brand's "LinkedIn" routes to the shared parent (Niagen Bioscience) company page
  tiktok: https://www.tiktok.com/@truniagen
  x: https://x.com/truniagen
  youtube: https://www.youtube.com/truniagen
  pinterest: https://www.pinterest.com/truniagen_/
external:
  trustpilot: https://www.trustpilot.com/review/truniagen.com   # third-party record (signals/ captured 2026-06-15: 2.4 "Poor", 16 reviews)

# Capture meta
captured_at: 2026-06-16
capture_method: firecrawl
site_notes: "Shopify storefront (shopId 60927377477; *.myshopify). Catalog backbone = /products.json (14 SKUs: 8 single products + 6 bundles) — products.json prices are the ONE-TIME/regular prices; the PDP/collections grid shows Subscribe & Save 'From' prices at ~10% off (e.g. $44.10 vs $49). HSA/FSA accepted via Truemed (Shopify tags truemed-eligible on all but NanoCloud, which is truemed-ineligible + onetime-purchase-only). Sister/related hosts: niagenplus.com (Rx pharma-grade NAD+, separate profile), pro.truniagen.com (HCP site), quiz.truniagen.com (product-finder), transparency.truniagen.com (per-lot COA lookup, 'Trace My Bottle'). Brand hue is deep blue #053584 (branding payload labels it accent/textPrimary/link; its 'primary' #405372 is muted slate UI chrome — confirm hue from the navy hero, not the slot name). No JSON-LD on homepage. Hero/promo is seasonal+rotating (Father's Day '#1 NAD+ booster for the #1 Dad' + free 7-day Stick Pack with $50+, and a NanoCloud skincare banner) — treat captured hero/promo as point-in-time."
key_pages:
  home: /
  shop_all: /collections/all
  bundles: /collections/bundles
  our_story: /pages/our-story
  quality: /pages/quality
  science: /pages/niagen-nr-science
  all_benefits: /pages/all-benefits
  pdp_300mg: /products/tru-niagen-300mg
  pdp_pro_1000mg: /products/tru-niagen-1000mg
  pdp_nanocloud: /products/niagen-nanocloud
  hsa_fsa: /pages/hsa-fsa-program
  quiz: /pages/quiz
unverified_fields:
  - "Hero/promo + Subscribe & Save 'From' prices are a point-in-time snapshot, not fixed — seasonal (Father's Day) promo + rotating hero (no A/B tool fingerprinted; treat as rotation)."
  - "Subscribe & Save discount: site shows ~10% off via the 'From' price (e.g. $44.10 vs $49) and 'your price stays the same … month or 6 months'; the exact % is not stated verbatim."
  - "Tru Niagen Beauty / Immune companion actives — Beauty is '100mg Niagen + targeted beauty actives' (specific actives not enumerated on captured pages); Immune adds Vitamin C + Curcumin per the Alkemist COA filenames on /pages/quality. PDPs not individually scraped."
  - "Line-level financials / headcount — not on the marketing site (parent is public: CDXC / Niagen Bioscience)."

description: "The #1 US NAD+ supplement brand — sells Niagen® (its parent's patented nicotinamide riboside, an NAD+ precursor) as oral capsules, on-the-go stick packs, and a topical skincare sachet, direct-to-consumer on a Subscribe & Save model."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company                  # own Shopify cart + P&L, sells direct → Company even under a parent (mirrors sister niagenplus.com)
target_market: [B2C]
offering_category: [Consumer Packaged Goods (CPG)]   # food-grade dietary supplement + a topical skincare line — a frequently-replaced consumer good, NOT a drug (explicit "not intended to diagnose, treat, cure"); distinct from sister Niagen Plus's Rx Biotech/Pharma posture
portfolio_shape: Flagship + companions   # hero = Tru Niagen 300mg (original NR capsule) in 3 dose tiers/forms; companions = Pro 1,000mg, Beauty, Immune, NanoCloud skincare + 6 bundles — all one molecule (Niagen® NR)
business_model: Subscription          # Subscribe & Save (~10% off) is the default/pushed model; one-time purchase also offered
primary_industry: Healthcare & Life Sciences

# Visual identity — Firecrawl branding is a hint to verify; confirmed against the homepage screenshot
logo_url: https://www.truniagen.com/cdn/shop/files/TN_Logo.svg?v=1723656218&width=320   # canonical wordmark (hostable CDN SVG, the real brand mark)
logos:
  wordmark: { src: "https://www.truniagen.com/cdn/shop/files/TN_Logo.svg?v=1723656218&width=320", w: 149, h: 20 }   # "Tru Niagen" wordmark, deep-blue on light; hostable SVG (no committed file needed)
  logomark: { src: "https://www.google.com/s2/favicons?domain=truniagen.com&sz=256", px: 32, transparent: false }   # "TN" mark; google-s2 returned a 32px JPG (sz=256 ignored) — under the 128px deck bar, recorded anyway; JPG → opaque background
  og:       { src: "http://www.truniagen.com/cdn/shop/files/2025_10_US_Homepage_SEO_Image_1200x628_e9b42f18-1942-434b-b360-bc2f595ca3d0_1200x628.png?v=1763685486", w: 1200, h: 628 }   # SEO homepage cover (declared 1200x628, verified)
brand_colors: { primary: "#053584", accent: "#405372" }   # deep royal/navy blue is the brand hue (vision-confirmed: navy hero band, headers, CTAs); #405372 slate is secondary UI. branding payload inverts these labels — slot names not trusted.
fonts: [Figtree, Nunito Sans]         # branding payload (Figtree = body); vision-consistent clean sans
color_scheme: light
design_framework: shopify             # rawHtml: cdn.shopify.com + myshopify + shopId 60927377477
---

## Overview

Tru Niagen is the flagship direct-to-consumer supplement brand of **Niagen Bioscience** (NASDAQ: **CDXC**) — the company formerly known as **ChromaDex** until its 2025 rebrand. It sells **Niagen®**, the parent's patented form of **nicotinamide riboside (NR)** — an NAD⁺ precursor and form of vitamin B3 — as a daily oral supplement to support "cellular health" and healthy aging. The single ingredient is sold across dose tiers (150 / 300 / 1,000 mg), formats (vegetarian capsule, on-the-go stick pack, and as of 2025 a topical skincare sachet), and a few actives-added companions (Beauty, Immune). The brand's entire positioning rests on a **quality / scientific-rigor moat** — it owns the patented ingredient, funds the clinical research, and publishes per-lot certificates of analysis — explicitly contrasting itself with the unregulated NR/NAD⁺ supplement market. It is the consumer tier of a three-part Niagen franchise: **Tru Niagen** (oral, food-grade, this site) · **Niagen Plus** (Rx, pharmaceutical-grade injectable/IV — [`niagenplus.com`](../niagenplus-com/profile.md)) · an **HCP pro** channel (pro.truniagen.com).

## What they offer

One molecule — **Niagen® (nicotinamide riboside)** — across dose tiers, formats, and a topical line; bold-led with verbatim one-time price + visibility token. Per-SKU detail in [`offerings.md`](offerings.md).

- **Tru Niagen® 300mg (Foundational):** the original / "minimum daily recommended serving"; veg capsule, 30 / 90 / 180 ct — **$49 / $127 / $244** (one-time; Subscribe & Save ~10%, "From $44.10"); "clinically shown to increase NAD+ levels by over 50%" `[published]`
- **Tru Niagen® Pro 1,000mg:** "clinical-strength" serving (two 500 mg veg capsules), 60 ct — **$116** ("From $104.40"); "clinically proven to increase NAD+ by up to 150%" in "as little as three weeks"; NSF Certified for Sport® `[published]`
- **Tru Niagen® 150mg:** "lowest starter serving … smaller capsule," 120 ct — **$94** ("From $84.60") `[published]`
- **Tru Niagen® 300mg Stick Packs:** powder "on the go, plus daily prebiotic support," 30 ct — **$58** ("From $52.20"); 7-pack trial — **$15**; NSF Certified for Sport® `[published]`
- **Tru Niagen® Beauty:** "once-daily 100mg Niagen supplement with targeted beauty actives," 30 ct — **$49** `[published]`
- **Tru Niagen® Immune:** Niagen® + immune actives (Vitamin C + Curcumin per the COA filenames), 30 ct — **$41** `[published]`
- **Niagen NanoCloud™ (Skincare):** waterless, water-activated topical NAD⁺ sachet (Niagen® + low-molecular-weight hyaluronic acid) — "the same patented NAD+ precursor … now topically, for the first time"; 1-pack (30 ct) / 2-pack (60 ct) — **$59 / $99** ("From $53.10"); Limited Release, Final Sale `[published]`
- **Bundles (6):** Whole-Body / Beauty / Immune combinations of the above — **$85–$194** `[published]`

## How it works / model

- **Channel:** a Shopify DTC storefront — browse → add to cart → checkout, or take the on-site **product-finder quiz** (quiz.truniagen.com). No prescription, no intake; a food-grade OTC supplement.
- **Money:** product sales, with **Subscribe & Save** (recurring auto-ship at ~10% off, "your price stays the same whether you subscribe for a month or 6 months") pushed as the default over one-time purchase. **HSA/FSA accepted** via Truemed.
- **Trust mechanics:** per-lot **certificate-of-analysis lookup** ("Trace My Bottle," transparency.truniagen.com) and a heavy science/quality content layer (Science, Quality, Benefits pages) carry the conversion argument rather than a clinician funnel.
- **Franchise routing:** the site cross-links to the Rx tier (**niagenplus.com**, "Pharma-Grade Niagen") and a healthcare-provider site (**pro.truniagen.com**).

## Positioning & audience

Targets health-conscious adults — skewing **older / longevity-minded** (PDP testimonials lead with 76–81-year-olds; lifestyle imagery shows active mid-life-to-senior adults; the current hero is a Father's-Day "#1 NAD+ booster for the #1 Dad") pursuing **healthy aging and "cellular health."** Claimed edge is threefold and consistent across every page: (1) **the patented ingredient** — Niagen® NR as "the most well-researched, efficient NAD+ precursor," superior to direct NAD⁺ or other precursors; (2) **scientific authority** — Nobel-laureate advisors, the NR discoverer (Dr. Charles Brenner) as Chief Scientific Advisor, 45+ human clinical studies; (3) **quality & transparency** — FDA NDI/GRAS notifications, ISO-accredited testing, third-party verification, per-lot COAs — weaponized against the rest of the category (homepage study: "87% of NR Supplements Fail to Meet Label Claims … Consumers are being duped"). Audience is broadly **all-genders** (no gendered hub), longevity-anchored.

## Nav structure

```
- Shop
  - Explore Our Products — /collections
    - Foundational: Tru Niagen® 300mg · 300mg Stick Packs · 150mg
    - Pro: Tru Niagen Pro® 1,000mg
    - Beauty: Tru Niagen® Beauty
    - Immune: Tru Niagen® Immune
  - Explore Bundles — /collections/bundles
    - Whole-Body Bundles: 300mg 30ct + Beauty · Pro 1,000mg + Beauty · 300mg 30ct + Immune · Pro 1,000mg + Immune · Whole-Body Benefits · Pro Whole-Body Benefits
  - Explore Skincare: Niagen NanoCloud™
  - Pharma-Grade Niagen: Clinical-guided NAD+ therapies → niagenplus.com
- Science & Benefits
  - Benefits — /pages/all-benefits: Healthy Aging · Cellular Health · Muscle Health · Brain Health · Reproductive Health · Lifestyle Stress Management · Heart Health · Immune Health
  - Science: Niagen/NR Science — /pages/niagen-nr-science
  - Blog: Tru Niagen Blog — /blogs/tru-niagen-labs
- About Us
  - Our Story — /pages/our-story
  - Our Quality — /pages/quality
  - Latest News — /pages/news
  - Our Parent Company - Niagen Bioscience → niagenbioscience.com
  - ChromaDex External Research Program (CERP) → chromadex.com/research/cerp
- Blog — /blogs/tru-niagen-labs
- (top bar) Pharma-Grade Niagen → niagenplus.com · HCP Pro Site → pro.truniagen.com
```

## Credibility & proof

- **Category leadership (self-reported):** "Tru Niagen® is the **number one NAD+ brand in the United States**" — flagged ³ "Based on revenue per largest U.S. e-commerce marketplace (Jan. 2025 – Dec. 2025)" (i.e., Amazon).
- **Scientific advisory board:** Nobel laureates **Sir John Walker** (Cambridge) and **Dr. Roger Kornberg** (Stanford, Chemistry); **Dr. Charles Brenner** (Chief Scientific Advisor — discovered NR's NAD⁺-boosting utility in 2004; City of Hope); Dr. Vilhelm Bohr (NIA), Dr. Rudolph Tanzi (Harvard/MGH), Dr. Brunie Felding (Scripps), Dr. Bruce German (UC Davis), Dr. Pinchas Cohen (USC).
- **Research scale (self-reported):** "45+ peer-reviewed published human clinical studies on Niagen® NR," "500+ published scientific studies," "60+ proprietary NR patents," "300+ global research collaborations" via the **Niagen Research Program™ (formerly CERP®)"; supplied Niagen® to "200+ leading universities and scientific institutions."
- **Regulatory notifications:** FDA reviewed Niagen under the **New Dietary Ingredient (NDI)** program twice (2015, 2018) and the ingredient was **notified GRAS** (Generally Recognized As Safe) in 2016 — presented as "extra assurance," with the standard "not evaluated by the FDA … not intended to diagnose, treat, cure, or prevent any disease" disclaimer.
- **Quality / testing:** Niagen® = **nicotinamide riboside chloride (NRCl)**; "at least 19 quality tests per batch" (13 ingredient + 6 finished); **ISO/IEC 17025:2017-accredited** lab (Longmont, CO); facility certs **NSF, Star-K (Kosher), IFANCA (Halal)**; **Alkemist Assured™** third-party testing on all products *except* 1,000mg & Stick Packs, which are **NSF Certified for Sport®**; per-lot **certificate of analysis** at transparency.truniagen.com; **TESTED by SuppCo** certified; "Made in the U.S.A. with internationally sourced materials."
- **Awards:** Consumer Choice Award; "Most Beloved Brand" (2023); Niagen — "Healthy Aging Ingredient of the Year" (2024); "Best Ingredient Supplier" (2019).
- **On-site product ratings:** 300mg 4.5 (591) · Pro 1,000mg 4.7 (161) · 150mg 4.7 (20) · Stick Packs 5.0 (5) · NanoCloud 5.0 (4).
- **Third-party reputation (NOT self-reported — Trustpilot, signals/ 2026-06-15):** Trust Score **2.4 "Poor," 16 reviews, 63% 1-star** (claimed profile, not paid) — a sharp contrast with the on-site product ratings; low review *count* suggests Trustpilot isn't where this brand's reviews concentrate (its volume is on Amazon / on-site).
- **Payments / access:** HSA/FSA eligible (Truemed).

## Visual & brand impression

High design maturity — a clean, clinical **premium-mass** aesthetic built on a confident **deep royal/navy blue** (`#053584`) over white, with the blue Tru Niagen bottle as the recurring hero object. Clear modular sections (product grid → "backed by 25 years" band → science explainer with DNA/brain/heart iconography → advisory-board portraits → warm lifestyle photography of active older adults). Figtree/Nunito-Sans sans-serif throughout reads accessible-scientific rather than luxury. The overall feel is *trustworthy supplement-as-science* — closer to a credible pharma-adjacent wellness brand than a trendy DTC, fitting the quality-moat positioning. *(A deeper, falsifiable visual layer lives in [`visual.md`](visual.md).)*

## Strategic read

Tru Niagen is the **consumer engine of a vertically-integrated, IP-anchored NAD⁺ franchise**: parent Niagen Bioscience (ex-ChromaDex, public CDXC) owns the patented molecule (Niagen® / NR), funds the science, and monetizes it across tiers — **oral food-grade (Tru Niagen, this brand)**, **Rx pharmaceutical-grade (Niagen Plus)**, and ingredient B2B/HCP. The defensible position isn't a clever funnel — it's **owning the ingredient + the evidence base + the testing apparatus**, then using that to claim the "#1 US NAD+ brand" spot and to attack the rest of a crowded, quality-variable NR/NAD⁺ supplement market on transparency ("87% of competitors fail label claims"). The 2025 moves — the Beauty/Immune actives extensions and the **NanoCloud topical skincare** line ("NAD⁺ skincare … for the first time") — show the brand stretching the single molecule into new formats and a new category (skincare) to grow beyond the core capsule. Relevant to Teleprescribe as a **longevity/NAD adjacency** (Notion: "Different audience / Low" for this consumer brand; the Rx sister Niagen Plus is flagged "High"): a model of how a credentialed-ingredient + clinical-evidence moat is built and merchandised in the cellular-health space.

## Provenance

- **Pages:** homepage, /collections/all (rich — prominence), /pages/our-story, /pages/niagen-nr-science, /pages/quality, PDPs (tru-niagen-300mg, tru-niagen-1000mg, niagen-nanocloud) — analyzed; Firecrawl, 2026-06-16. Full 14-SKU roster enumerated from the Shopify /products.json registry (saved to captures/). FAQs, all-benefits, hsa-fsa-program noted, not scraped.
- **Verify:** 8 pages — all sourceURLs matched, all bodies md5-unique (no geo/cache contamination), no junk soft-404s.
- **Credits:** 9 (1 map + 1 homepage + 1 collections + 6 key pages). Logos module ran free over the cached homepage payload; /products.json + signals (Trustpilot, SEC) are non-Firecrawl.
- **Couldn't get:** Subscribe & Save exact % (shown via "From" price, not stated); Beauty/Immune full actives list (PDPs not scraped); line-level financials (off-site; parent public CDXC).
- **Enriched (model knowledge):** "ChromaDex" as Niagen Bioscience's former name — corroborated this run by the about page ("Niagen Bioscience, formerly ChromaDex") and the captured SEC signal (registered_name "Niagen Bioscience, Inc.", ticker CDXC, CIK 0001386570).
- **Run profile:** express — +telehealth.md cohort pack, +logos, +offerings.md (explicit arg "including offerings.md" — a `deep` override of the project relevance gate, which alone would baseline this brand: Companies row reads "Different audience / Low"). Schema 2.6.
