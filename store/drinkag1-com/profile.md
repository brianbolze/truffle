---
schema_version: 1

# Identity
domain: drinkag1.com
name: AG1
aliases: [athleticgreens.com]   # rebrand from Athletic Greens → AG1; athleticgreens.com 301-redirects to drinkag1.com (verified)
parent: []
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Bot-defended DTC site (plain curl to drinkag1.com returns HTTP 429; Firecrawl proxy is mandatory). HAZARD: parallel scrapes — and any scrape using Firecrawl's DEFAULT cache (maxAge) — returned a byte-identical /en-eu/ EUROPEAN homepage shell for 4 different requested URLs, while metadata.sourceURL still reported the correct requested URL each time. So the linear-era sourceURL check PASSES while content is wrong/contaminated; the reliable guard is a content md5 dedup across pages. FIX that worked: scrape each page individually (no parallel burst) with location:{country:US,languages:[en-US]} + maxAge:0 (bypass the default ~2-day cache) + waitFor:~3500 (SPA renders client-side). Nav + footer are client-rendered (NOT in scrape markdown even with all formats) — reconstruct nav from /v2/map + homepage links. Stack: Next.js (rawHtml has __NEXT_DATA__ + /_next/) on a Sanity CMS (cdn.sanity.io/images/jf30o7wb) — branding.designSystem.framework reports 'bootstrap', which is WRONG (trust rawHtml). Pricing $ values ARE in the markdown once US-geo'd (NOT JS-walled like linear). /v2/map returns 485 URLs dominated by marketing-funnel noise (94 /partner/*, 26 /people/*, dozens of /hero-*-lp + /sweepstakes-* + affiliate landers) and 8 locale subtrees (/en-uk, /de-eu, /nl-eu, /en-au, ...) — filter to the ~20 signal pages. branding.colors.primary (#0C3D3D deep green) IS a true brand hue here (logo/packaging/header) — this INVERTS linear, where primary was the text color; accent #46DE46 is the bright CTA green."
key_pages:
  shop_all: /shop                                   # Shop All; sub: /shop/daily-health, /shop/sleep-support, /shop/accessories, /shop/bundles
  ag1_pouch: /products/greens-powder-pouch          # flagship "AG1 Next Gen" greens powder PDP
  agz_sleep: /products/sleep-supplement             # AGZ Nightly Sleep Support PDP
  d3k2: /products/vitamin-d3-k2-liquid
  omega3: /products/omega-3-fish-oil-supplements
  travel_packs: /products/greens-powder-travel-pack
  bundles: /shop/bundles                            # also /bundles/day-and-night-bundle, /bundles/annual-subscription
  ingredients: /ingredients
  research: /learn/research/scientific-research
  quality: /quality-standards
  membership: /ag1-membership
  about: /about-us
  what_is_ag1: /what-is-ag1
  reviews: /about-ag1/reviews/ctr
  account: https://account.drinkag1.com             # member login (subdomain)
unverified_fields:
  - "Leadership / founder names — did not capture /leadership or /impact-report this run (about-us is mission-only). Athletic Greens founding stated only as 'more than a decade ago.'"
  - "AGZ standalone vs. AG1-bundled pricing — PDP shows 30ct at $2.63/serving and 'Unlock $69 pricing with an AG1 Subscription,' but a shared price component also rendered AG1's $79/$99; AGZ's exact standalone subscription price not cleanly isolated."
  - "Headcount / revenue / funding / ownership — not on the marketing site (deep-research job, not capture)."

# Description — one sentence
description: "A DTC consumer-health brand whose flagship AG1 is a once-daily greens 'Daily Health Drink' of 75+ ingredients, sold with a small stack of companion supplements (AGZ sleep, D3+K2, omega-3) on a flexible monthly subscription and backed by clinical trials + NSF certification."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Consumer Packaged Goods (CPG), Retail / E-Commerce]   # CPG = the consumable supplement they make; Retail/E-Commerce = the DTC online motion
portfolio_shape: Flagship + companions   # AG1 is the hero; AGZ (sleep), D3+K2, Omega-3 are a small companion stack — TAXONOMIES' canonical Flagship + companions
business_model: Subscription # primary; one-time purchase ("Buy Once") offered as a secondary path
primary_industry: Healthcare & Life Sciences   # judgment call — straddles Consumer Goods; chose Health for the clinical-research/nutrition-science positioning (see body)

# Visual identity — lifted from Firecrawl `branding` (homepage pass), confirmed against screenshot
logo_url: https://cdn.sanity.io/images/jf30o7wb/production/81bbdfeb78d658d5808328353ff0aab82b19e959-123x55.svg   # hostable SVG via Sanity CDN (branding.images.logo, decoded from the /_next/image wrapper) — NB unlike linear's inline data-URI
brand_colors: { primary: "#0C3D3D", accent: "#46DE46", secondary: "#0F2E2F", background: "#FFFFFF" }   # copied from branding.colors. OPEN SCHEMA Q (see Visual & brand impression): the TRUE signature hue is the green family — deep forest green #0C3D3D (logo/header/footer/pouch) reads as the primary brand color, with bright kelly green #46DE46 as the CTA accent. This INVERTS linear (where primary=#text and accent=brand hue) → no stable positional rule for which `branding.colors` slot is "the brand color."
fonts: [Diatype, DiatypeMono]   # branding.fonts: Diatype=body, DiatypeMono=monospace
color_scheme: light             # verified from screenshot (white canvas) + branding.colorScheme
design_framework: next.js       # rawHtml __NEXT_DATA__ + /_next/ + next/static; CMS = Sanity. branding.designSystem said "bootstrap" — wrong.
---

## Overview

AG1 (formerly **Athletic Greens**, rebranded ~2022; `athleticgreens.com` now 301-redirects here) is a direct-to-consumer health-and-nutrition brand built around a single hero product: **AG1**, a powdered "Daily Health Drink" of 75+ vitamins, minerals, whole-food superfoods, pre/probiotics, and adaptogens taken once a day in water. The pitch is "Foundational Nutrition" — one scoop replaces a cabinet of separate supplements (multivitamin, probiotic, greens, adaptogen, immune, cognitive) at a fraction of the combined cost. Started "more than a decade ago," it sells almost entirely on a **monthly subscription** and leans hard on clinical research, third-party (NSF) certification, and a deep roster of athlete/celebrity/scientist endorsers (Hugh Jackman, Dr. Andrew Huberman, Allyson Felix).

## What they offer

A deliberately **small catalog** anchored by one flagship, now expanding into a companion "stack." (A future `offerings.md` would list AG1 first — it shares the company name.)

- **AG1 (AG1 Next Gen)** — `/products/greens-powder-pouch`. The flagship greens "Daily Health Drink," 75+ ingredients, 13g scoop, contains live probiotics (refrigerate after opening). Underwent a research-backed "Next Gen" reformulation in **Jan 2025**. Variants/flavors are *of AG1*, not separate products: **Original** (pineapple+vanilla), **Citrus** (lemon+orange), **Berry** (blueberry+strawberry), plus **Travel Packs** (single-serve) and accessories (canister, scoop, shaker, tote).
- **AGZ Nightly Sleep Support** — `/products/sleep-supplement`. New evening counterpart, "developed by the same team that created AG1." A **melatonin-free** nighttime drink (magnesium, saffron, ashwagandha, L-theanine, lemon balm, chamomile) marketed as working in three stages (Evening / Sleep / Morning), "supports your body's natural rhythm, not override it." 3 flavors; 30ct and 7ct.
- **AG Vitamin D3+K2** — `/products/vitamin-d3-k2-liquid`. Liquid-drop add-on.
- **Omega-3 fish oil** / **Omega + CoQ10** — `/products/omega-3-fish-oil-supplements`, `/products/omega-coq10`.
- **Bundles** — `/shop/bundles`, incl. a **Day & Night** bundle (AG1 + AGZ) and an annual subscription.

**`is_multi_product: true` — but genuinely debatable.** By the TAXONOMIES test (2+ distinct offerings a customer would comparison-shop or buy separately, distinct in name/page/positioning), AG1 / AGZ / D3+K2 / Omega-3 clearly qualify — each has its own PDP and standalone purchase. *Against* that: the brand explicitly self-positions as anti-proliferation — *"focus on a very small number of products… we never make anything new just to sell you on more"* — and AG1 still carries ~all the brand equity. This is the **opposite resolution from linear** (which was `false`: one app, many surfaces, one price): AG1 is one brand, several separately-bought products, several prices. The flagger-plus-stack shape is the recurring hard case for this field.

## How it works / model

Self-serve DTC e-commerce, **subscription-first** with a one-time escape hatch. Customer journey: land (heavy paid/influencer funnel) → product page → choose subscription cadence or one-time → checkout → recurring shipment + member portal (`account.drinkag1.com`).

Pricing (verbatim, US, from the AG1 PDP — recovered from markdown after forcing US geo):

- **AG1 — Monthly Delivery: $79/mo** (Save 20%), vs. **~~$99~~** one-time value. 30-day supply, ships every 30 days. *"less than $3 a day when you subscribe."*
- **AG1 — 3-Month Delivery: $219** (Save 26%), vs. **~~$297~~**.
- **AG1 — Buy Once: $99 + $9 shipping** (one-time, no commitment).
- **First subscription includes** a Welcome Kit free-gift stack: Canister/Scoop/Shaker (~~$28~~ free), AG1 Sample Pack 3ct (~~$19~~ free), Members-Only Perks — ~$43 value.
- **AGZ:** 30 servings at $2.63/serving; 7ct at $3.57/serving; "**Unlock $69 pricing with an AG1 Subscription**."

**Membership perks** (`/ag1-membership`): exclusive member pricing + premium welcome kit; **$15 referral credit** (friend also gets a free D3+K2 + 5 travel packs); event invites; first access to launches; **pause / skip / cancel anytime**; **90-day money-back guarantee**; dedicated member-experience team; **HSA/FSA eligible** via a Truemed partnership. Homepage runs a head-to-head value table: AG1 at $79/mo vs. **$225/mo** to buy six supplement categories separately.

## Positioning & audience

- **Who:** broad B2C "health-conscious individuals" — busy professionals, athletes, people improving gut health/energy, and notably **people on GLP-1s** wanting nutritional support (an explicit homepage callout + a `/glp-1-landing-page`).
- **Against:** the cabinet of individual supplements (the comparison table) and the wider "greens powder" category — AG1 insists it's *"not another greens powder"* but a clinically-backed Daily Health Drink that *replaces* multiple premium supplements.
- **Claimed edge:** *Foundational Nutrition* — simplicity (one scoop), clinical backing (4 randomized placebo-controlled trials on AG1 Next Gen, a UC Davis partnership), quality/safety (NSF Certified for Sport, third-party contaminant testing), and an unusually heavy **endorsement + social-proof** apparatus (60,000+ verified 5-star reviews; Huberman since 2012).

## Nav structure

Top mega-nav + footer are **client-rendered** (absent from scrape markdown, like linear); reconstructed from `/v2/map` (485 URLs) + homepage links + the PDP breadcrumb ("Shop All").

```
- Shop — /shop  (Shop All)
  - Daily Health — /shop/daily-health
    - AG1 (Next Gen Pouch) — /products/greens-powder-pouch
    - AG1 Travel Packs — /products/greens-powder-travel-pack
    - AG Vitamin D3+K2 — /products/vitamin-d3-k2-liquid
    - Omega-3 — /products/omega-3-fish-oil-supplements  ·  Omega + CoQ10 — /products/omega-coq10
  - Sleep Support — /shop/sleep-support
    - AGZ Nightly Sleep Support — /products/sleep-supplement  (variety pack, 7ct)
  - Accessories — /shop/accessories  (canister, scoop, shaker, tote)
  - Bundles — /shop/bundles  (Day & Night — /bundles/day-and-night-bundle; Annual — /bundles/annual-subscription)
- Science / Learn
  - Ingredients — /ingredients  ·  AGZ Ingredients — /sleep/agz-ingredients
  - Scientific Research — /learn/research/scientific-research
  - Quality Standards — /quality-standards
  - Blog — /blog  ·  Health Guides — /health-guides  ·  Recipes — /recipes
- About
  - About Us — /about-us  ·  What is AG1 — /what-is-ag1
  - Leadership — /leadership  ·  Impact Report — /impact-report
  - Reviews — /about-ag1/reviews/ctr
- Membership — /ag1-membership
- Support — /contact-us/customer-service  ·  Find AG1 Near Me — /retail-locations
- Account — account.drinkag1.com  /  /members/login
- Locales: /en-uk, /en-eu, /de-eu, /nl-eu, /es-eu, /se-eu, /en-au, /en-nz, /apac-us
```

## Credibility & proof

- **Scale / social proof:** "**60,000+ verified 5-star reviews** for AG1 products"; "Over 60,000 Satisfied Customers."
- **Certification & testing:** **NSF Certified for Sport®** ("the gold standard"); third-party tested for pesticides, herbicides, heavy metals, and banned substances; "what's on the label is what's in the product."
- **Clinical:** "**four randomized, placebo-controlled trials**" on AG1 Next Gen showing closure of nutrient gaps; a self-perceived-efficacy study (80% reported improved digestion at 3 months); a **UC Davis** research partnership; a dedicated `/learn/research/scientific-research` page.
- **Endorsers (unusually deep):** Hugh Jackman (since 2021, the homepage hero), **Dr. Andrew Huberman** (partner, since 2012), Allyson Felix, Mick Fanning, Sloane Stephens, Dan Churchill, plus alpinists/marathoners/rugby champions. Press: Forbes, Vogue, Bon Appétit.
- **Risk reversal:** **90-day money-back guarantee**; pause/skip/cancel anytime; HSA/FSA eligibility (Truemed).

## Visual & brand impression

High-maturity, premium-wellness DTC aesthetic — **light-mode**, near-white/cream canvas with generous whitespace and large lifestyle/product photography. The brand's signature is **green**, expressed in two registers: a **deep forest/teal green (#0C3D3D / #0F2E2F)** used for the wordmark, header, footer, and the iconic AG1 pouch, and a **bright kelly green (#46DE46)** used for CTAs, links, and highlights. Type is **Diatype** (a clean grotesk) with **DiatypeMono** for technical/label accents. The page mixes editorial credibility cues (press logos, clinical-trial stats, supplement-facts modules) with aspirational athlete/celebrity portraiture — reading as "clinical but premium-lifestyle," not clinical-sterile.

**Open SCHEMA question — `brand_colors` semantics (flag, not solved here).** Firecrawl's `branding.colors` gives positional slots (`primary`, `accent`, `secondary`, …) but those slots are **not semantically stable across sites**: for linear, `primary` was the body **text** color and the true brand hue was `accent`; for AG1, `primary` (#0C3D3D) **is** a true brand hue and `accent` (#46DE46) is a secondary brand/CTA green. AG1 also genuinely has a *two-color* brand identity (deep green + bright green), so "the brand color" is itself ambiguous. Net: any rule like "always take accent as the brand color" is wrong — the field needs either both colors retained (current approach) or a vision-confirmed pick. Logged for the SCHEMA decision; not resolved in this capture.

## Strategic read

The capture catches AG1 mid-transition from **single-hero-product brand → multi-product "health stack."** For a decade AG1 *was* the company (and still carries the brand equity and the "we don't make things just to sell more" ethos), but the launch of **AGZ** (a same-team evening/sleep counterpart) plus D3+K2 and Omega-3 add-ons signals a deliberate move to own more of the customer's daily supplement routine — the "day-and-night" bundle is the tell. The durable state worth recording: a subscription-first DTC nutrition brand competing on *clinical credibility + certification + celebrity trust* rather than price, with a heavy paid/influencer/affiliate acquisition machine (the map's 94 `/partner/*`, 26 `/people/*`, and dozens of campaign/sweepstakes landers) feeding a flexible monthly membership. The explicit GLP-1 targeting is a notable 2025 positioning bet.

## Provenance

- **Pages analyzed (all Firecrawl `/v2/scrape`, 2026-05-30):** homepage (`/`, full pass: markdown + html + rawHtml + links + branding + full-page screenshot), `/products/greens-powder-pouch` (AG1 PDP), `/products/sleep-supplement` (AGZ PDP), `/ingredients`, `/ag1-membership`, `/about-us` — each with markdown + html + links + full-page screenshot. Site inventory via `/v2/map` (485 URLs).
- **Capture mechanics:** the 4 content pages + about-us first returned an identical geo-misrouted `/en-eu/` homepage shell under Firecrawl's default cache / parallel burst (sourceURL still reported the right URL — caught via content md5 dedup); re-scraped individually with `location:{country:US}` + `maxAge:0` + `waitFor:3500` to get correct US content. See `site_notes`.
- **Raw payloads + screenshots:** `captures/2026-05-30/.payloads/`; cleaned page markdown: `captures/2026-05-30/*.md`.
- **Visual identity** lifted from the homepage `branding` payload (colors, fonts) and confirmed against the homepage screenshot.
- **Couldn't get cleanly:** client-rendered mega-nav/footer contents (reconstructed from map + links); leadership/founder names (didn't capture `/leadership`); AGZ standalone subscription price (shared price component bled AG1's $79/$99) — see `unverified_fields`.
</content>
</invoke>
