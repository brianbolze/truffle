---
schema_version: 1

# Identity
domain: benadryl.com
name: Benadryl
aliases: []                          # brand has no alt domains; es.benadryl.com is the Spanish locale, not a rebrand
parent: [kenvue.com]                 # Benadryl is a product brand of Kenvue (Kenvue Brands LLC)
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Marketing/education site only — it does NOT sell (no cart/checkout/prices). 'Buy Now' and /where-to-buy open a client-rendered retailer-locator widget (returns 'We couldn't find any online sellers' without a product/zip context) — channel is OTC retail (drugstores/Amazon), not DTC. So there is NO pricing or business-model signal to capture from this site; that's expected for a CPG brand site, not a miss. Renders cleanly server-side: top nav AND footer ARE in scrape markdown (unlike linear/AG1's client-rendered nav) — markdown alone reconstructs the full IA. Stack: Next.js (rawHtml has /_next/) on a Contentful CMS (images.ctfassets.net, space t975yazu1avh). branding.designSystem.framework reports 'unknown' (another framework miss — trust rawHtml). branding.images.logo is EMPTY — logo fallback chain went favicon (Contentful SVG). branding.fonts ranks generic 'sans-serif' (count 130) FIRST; the real brand font is ProximaSoftBold (count 61) — do not take fonts[0]. branding.colors.primary (#D21F62 magenta) IS a true brand hue here; accent/textPrimary/link are all #005DAB blue (the CTA/text color) — two-color magenta+blue identity. /v2/map returned 68 clean signal URLs (no funnel-noise explosion — contrast AG1's 485). Parent = Kenvue (footer: '©Kenvue Brands LLC. 2026... This site is published by Kenvue Brands LLC.'; privacy notice lives on kenvuebrands.com). No geo/cache contamination this run; US+maxAge:0+waitFor:3000 applied prophylactically."
key_pages:
  products: /products                                          # full catalog hub (filterable by Ages / symptom)
  products_adult: /products/adult-products                     # adult oral + topical
  products_topical: /products/topical-products                 # anti-itch creams/gels/sprays/sticks
  products_children: /products/children-products
  product_finder: /product-finder                              # symptom→product quiz
  compare: /benadryl-difference/compare-allergy-relief-products # Benadryl vs Claritin/Zyrtec/Allegra/Xyzal
  ingredient: /benadryl-difference/diphenhydramine-active-ingredient
  ingredients_list: /benadryl-difference/ingredients-transparency
  where_to_buy: /where-to-buy
  dosing_guide: /benadryl-dosing-guide
  safety: /safety
  espanol: https://es.benadryl.com/                            # Spanish-language sibling site
unverified_fields:
  - "Pricing — none on site (marketing-only; sold via retail/OTC). Not capturable here by design."
  - "Headcount / revenue / manufacturing — belong to the parent (Kenvue), not the brand site."
  - "Per-SKU retailer availability — the /where-to-buy widget is client-rendered and returned no sellers without a product+location context."

# Description — one sentence
description: "Benadryl is Kenvue's flagship over-the-counter antihistamine brand built on diphenhydramine, sold as oral allergy medicines (tablets, Liqui-Gels, children's liquids) and topical anti-itch products (creams, gels, sprays, sticks) through retail pharmacies rather than direct."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Other            # PRODUCT BRAND, not a company — no closed-set value fits "brand-of." The non-Company values are entity flags (Investor/Nonprofit/Gov/Edu/Individual); none cover a CPG brand owned by a parent. Pragmatic alt was "Company + parent note"; chose Other to surface the gap honestly (repeated-Other = taxonomy signal). See body + FINDINGS.
target_market: [B2C]          # markets to consumers (purchased at retail; brand site is consumer-facing education)
offering_category: [Consumer Packaged Goods (CPG), Biotech / Pharma Products]   # primary CPG (drugstore consumer staple, frequently replaced); secondary Pharma (it IS a diphenhydramine drug). Straddle — see body; echoes AG1's consumer-health CPG↔Health line.
portfolio_shape: Single       # ONE antihistamine brand (single active ingredient: diphenhydramine) in many forms/strengths/ages, no sub-brands — borderline but TAXONOMIES' canonical Single
business_model: Transactional / One-time   # consumer buys a box at retail, no recurring commitment. NB the brand site itself transacts nothing; revenue is wholesale-CPG to retailers (a parent-level fact).
primary_industry: Healthcare & Life Sciences   # OTC pharma / consumer health (an approved drug). Same straddle-with-Consumer-Goods as AG1, but cleaner here (it's a real drug).

# Visual identity — lifted from Firecrawl `branding` (homepage pass), confirmed against screenshot
logo_url: https://images.ctfassets.net/t975yazu1avh/7cFJCy50xEKdFV7HgKOdNw/3a6fdf87ceff27a12b29c189ea6602a8/Benadryl_-_Favicon.svg   # branding.images.logo was EMPTY; favicon (Contentful SVG) is the fallback-chain pick — strip the ?w=16&h=16&fm=png resize params for the source SVG
brand_colors: { primary: "#D21F62", accent: "#005DAB", secondary: "#2D3946", background: "#FFFFFF" }   # copied from branding.colors. primary #D21F62 IS the signature magenta (hero band, claim band, packaging); accent/textPrimary/link all #005DAB = the blue CTA/text color. Two-color magenta+blue identity. (Like AG1, primary=brand hue here — opposite of linear, where primary was text.)
fonts: [Proxima Soft]         # branding.fonts ranked generic 'sans-serif' FIRST (count 130, fallback noise); ProximaSoftBold (count 61) is the real brand face
color_scheme: light           # verified from screenshot (white canvas, magenta hero) + branding.colorScheme
design_framework: next.js     # rawHtml /_next/; CMS = Contentful (ctfassets.net). branding.designSystem said "unknown" — another miss
---

## Overview

Benadryl is an **over-the-counter (OTC) antihistamine brand owned by Kenvue** (Kenvue Brands LLC, the consumer-health company spun out of Johnson & Johnson in 2023 — the footer reads *"This site is published by Kenvue Brands LLC."*). It is not a company in its own right; `benadryl.com` is the consumer-facing **marketing and education site** for the brand. Everything Benadryl sells is built on a single active ingredient, **diphenhydramine HCl** (a first-generation antihistamine), delivered in two product families — **oral allergy medicines** and **topical anti-itch** products — across adult and children's forms. The site does not transact: it routes buyers to retail ("Where to Buy"), positions Benadryl against competitor OTC allergy meds, and educates on allergies/itch/cold via a deep content library.

**Parent / ownership (no SCHEMA field for this):** Benadryl → **Kenvue** (`kenvue.com`), relationship *brand-of*. Other Kenvue brands include Tylenol, Zyrtec, Listerine, Neutrogena, Aveeno, Band-Aid. Recorded in prose + `site_notes` because the frontmatter has no `parent` / `brand_of` slot — see Provenance and the experiment FINDINGS.

## What they offer

One brand, one active ingredient (**diphenhydramine**), many **forms/strengths/ages** — roughly 14 SKUs the site organizes by symptom (Children's, Itchy Nose/Throat, Itchy Skin, Itchy/Watery Eyes, Nasal Congestion). A future `offerings.md` would list them breadth-first by family:

- **Oral allergy (antihistamine)** —
  - **Benadryl Allergy ULTRATABS®** (`/products/benadryl-allergy-ultratabs-tablets`, ages 6+) — the flagship tablet.
  - **Extra Strength Allergy** (50 mg diphenhydramine, ages 12+).
  - **Allergy Dye-Free LIQUI-GELS®** (ages 6+).
  - **Allergy Plus Congestion** (adds a decongestant; sinus/nasal; ages 12+).
  - **Children's Benadryl Allergy Liquid** + **Dye-Free** + **Plus Congestion** (cherry/bubblegum flavors; ages 6–11).
- **Topical anti-itch (diphenhydramine topical analgesic)** —
  - **Itch Stopping Cream** — Extra Strength + Original Strength (ages 2+).
  - **Itch Stopping Gel** (Extra Strength, ages 2+).
  - **Extra Strength Anti-Itch Spray** (ages 2+).
  - **Extra Strength Itch Relief Stick** (bug bites/rashes, ages 2+).

**`is_multi_product: false` — but the closest-to-the-line `false` in the corpus.** By the TAXONOMIES test (2+ distinct offerings you'd comparison-shop or buy separately), the SKUs are **forms and strengths of one brand**, not separately-branded products — no sub-brand ever splits off (contrast AG1 → AGZ, which earned its own name and `true`). It reads like **linear's "one thing, many surfaces" `false`**, just expressed as delivery forms instead of software modules. *What makes it nearly `true`:* an oral allergy tablet and a topical itch cream are genuinely different product types for different occasions — a shopper buys the one matching the symptom, not "a Benadryl." Resolved `false` because they share one active ingredient and one brand identity and are positioned as a single family ("there's a BENADRYL® for you"). This is a **third distinct shape** for the field — see FINDINGS.

## How it works / model

**No direct commerce.** The brand site is pure marketing/education; purchase happens at retail (drugstores, mass retailers, Amazon) — the model is **OTC consumer-packaged-goods**, a one-time retail purchase, not subscription or DTC. Customer journey on-site: land → **Product Finder** (a symptom→product quiz) or browse `/products` by symptom/age → **"Where to Buy"** retailer-locator widget → buy off-site. The brand also runs coupons (`/save-on-benadryl`, a "$2 coupon" email signup) and a dosing guide. Revenue/manufacturing are **Kenvue-level** facts, not on this site.

## Positioning & audience

- **Who:** broad B2C allergy and itch sufferers — adults and (heavily) **parents of children** (kid-friendly flavors, children's dosing, a dedicated children's line front-and-center on the homepage).
- **Against:** other OTC allergy meds. The `/compare` page explicitly stacks **Benadryl (diphenhydramine) vs. Claritin® (loratadine), Zyrtec® (cetirizine), Allegra® (fexofenadine), Xyzal® (levocetirizine)** in a comparison chart — an unusually direct, named competitive table. Benadryl's diphenhydramine is the *first-generation* antihistamine (fast-acting but sedating: *"the diphenhydramine in BENADRYL® Allergy can cause drowsiness"*), versus the second-gen non-drowsy rivals — a real positioning tension the brand addresses head-on.
- **Claimed edge:** trusted heritage + ubiquity — *"Bought by more households than any other OTC Allergy brand"* (the headline homepage claim) — plus breadth of forms and a strong children's/safety/dosing-guidance posture.

## Nav structure

Server-rendered — full top nav **and** footer present in scrape markdown (no client-rendered flyout problem here).

```
- Products — /products
  - Adult — /products/adult-products
  - Children's — /products/children-products
  - Topical — /products/topical-products
  - Product Finder — /product-finder
- BENADRYL® Difference — /benadryl-difference
  - Compare BENADRYL® — /benadryl-difference/compare-allergy-relief-products
  - BENADRYL® Uses — /benadryl-difference/uses-indications
  - Our Ingredients — /benadryl-difference/ingredients-transparency
  - About Diphenhydramine — /benadryl-difference/diphenhydramine-active-ingredient
  - What Are Decongestants? — /benadryl-difference/uses-indications/decongestants
  - FAQs — /faq
- Allergy & Cold Guide — /allergy-cold-guide
  - Allergies — /allergies   ·  Children's Allergies — /childrens-allergies
  - Itchy Skin — /itchy-skin  ·  Cold or Allergies? — /cold/cold-or-allergies
- Where To Buy — /where-to-buy
- Utility: Savings — /save-on-benadryl · Dosing Guide — /benadryl-dosing-guide · Español — es.benadryl.com
- Footer · Company: Contact — /contact-us · Sitemap — /sitemap
- Footer · Legal: Legal Notice — /legal · Privacy Notice — kenvuebrands.com/us/privacy-notice (parent domain) · Do Not Sell/Share · AdChoices
- ©Kenvue Brands LLC. 2026
```

## Credibility & proof

- **Category-leadership claim:** *"Bought by more households than any other OTC Allergy brand."*
- **Per-product ratings** (volume of reviews signals scale): Ultratabs 4.x with **(533)** reviews, Children's Allergy Liquid 4.8 **(202)**, Extra Strength Ultratabs **(370)**, etc.
- **Heritage/trust:** legacy household brand; now under Kenvue's consumer-health portfolio.
- **Safety posture:** a dedicated `/safety` page ("Safety Is Our Top Priority"), explicit dosing guide, repeated regulated warnings (*"Do not use more than one diphenhydramine product at the same time. Use products only as directed."*), and an "ingredients transparency" page.
- **Clinical framing:** the compare chart cites Cleveland Clinic drug references for each competing active ingredient.

## Visual & brand impression

Mass-market, **light-mode** consumer-health design — a clean white canvas anchored by Benadryl's signature **magenta (#D21F62)** (the hero band, the household-leadership claim band, packaging accents) with a **royal blue (#005DAB)** for CTAs ("Buy Now"), links, and body emphasis, closing on a dark navy footer (#2D3946). Product photography is straight packaging-front shots; lifestyle imagery is reassuring/domestic (kids outdoors, couples, sleep). The typeface is **Proxima Soft** (rounded, approachable). Overall read: trustworthy, accessible, slightly conservative/corporate — a regulated OTC brand prioritizing clarity, symptom navigation, and safety cues over the editorial polish of a DTC site like AG1. Reinforces the recurring **`brand_colors` instability**: here `branding.colors.primary` IS the brand hue (magenta), inverting linear (where primary was text) — no positional slot is reliably "the brand color."

## Strategic read

The durable state worth recording: Benadryl is a **mature, single-molecule OTC brand** (diphenhydramine) competing on heritage, ubiquity, and breadth of forms in a category where the science has moved past it — its active ingredient is the *drowsy* first-generation antihistamine, while Claritin/Zyrtec/Allegra (two of which, Zyrtec, are *also Kenvue's*) are the non-drowsy second generation. The site leans into trust, children's use, topical anti-itch (a segment where first-gen diphenhydramine is still a mainstay), and safety/dosing guidance rather than efficacy-vs-rivals. The most capture-relevant observation is structural, not strategic: this is a **brand site that doesn't sell** — no price, no cart, no business-model signal — which is the normal shape for a CPG/OTC brand and a useful contrast to the DTC (AG1) and SaaS (linear) sites where the site *is* the storefront.

## Provenance

- **Pages analyzed (all Firecrawl `/v2/scrape`, 2026-05-30, US locale + maxAge:0 + waitFor:3000):** homepage (`/`, full pass: markdown + html + rawHtml + links + branding + full-page screenshot), `/products` (catalog hub), `/products/adult-products`, `/products/topical-products`, `/benadryl-difference/compare-allergy-relief-products`, `/where-to-buy` — each markdown + links + screenshot. Site inventory via `/v2/map` (68 URLs, all signal).
- **Raw payloads + screenshots:** `captures/2026-05-30/.payloads/`; cleaned page markdown: `captures/2026-05-30/*.md`.
- **Visual identity** lifted from the homepage `branding` payload (colors, fonts) and confirmed against the homepage screenshot.
- **Entity boundary (the headline strain):** Benadryl is a **product brand of Kenvue**, not a company — `entity_type: Other`. There is no frontmatter `parent` / `brand_of` field, so the relationship is recorded in the identity NOTE, `description`, Overview, and `site_notes`. Flagged as a SCHEMA gap in the Experiment-3 FINDINGS.
- **Couldn't get (by design, not failure):** pricing / business-model / retailer availability — the site is marketing-only and the where-to-buy widget is client-rendered; see `unverified_fields`.
