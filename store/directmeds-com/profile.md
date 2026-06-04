---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: directmeds.com
name: Direct Meds
aliases: ["DirectMeds"]               # "© DirectMeds" / logo wordmark is the no-space form; JSON-LD Organization name is "Direct Meds"
parent: []
owns: []
socials:
  facebook: https://www.facebook.com/directmedsusa
  instagram: https://www.instagram.com/direct_meds_usa
  youtube: https://www.youtube.com/@DirectMeds
external: {}                          # looked (JSON-LD sameAs = own channels only); no crunchbase/wikipedia/trustpilot record. LegitScript cert → Credibility.

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "WordPress (Bedrock layout on WP Engine: rawHtml has /app/uploads ×368, /app/themes ×15, 'directmedsdev.wpenginepowered.com' on PDPs; branding.designSystem says 'custom' — ignore §5.4). Commerce/checkout live in the /portal app (portal.directmeds.com login; PDP 'Get this medication' → /portal/products/<slug>); product detail PDPs at /medications/<slug> are WP marketing pages with the all-inclusive monthly price at the BOTTOM. Category listings at /all-solutions/<category>/ carry product cards + prices (the offerings backbone). Funnel is quiz-gated (dm-q2spc/questionnaire-*.php?...&affid= — affiliate params). PRICES DISAGREE ACROSS SURFACES: listing card vs PDP vs FAQ (e.g. semaglutide-10 = $297 listing / $347 PDP), and decimal listing prices ($179.10, $224.10) imply a new-customer promo — treat as point-in-time. /about-us, /understanding-the-price, /meet-the-pharmacy are blog-style pages, not structured. Serves US + Canada (separate Canadian pharmacy partners). Skin/pain compounds name partner pharmacy 'CraftedRx'."
key_pages:
  how_it_works: /how-it-works
  all_solutions: /all-solutions
  pricing_explainer: /understanding-the-price
  meet_the_pharmacy: /meet-the-pharmacy
  about: /about-us
  weight_loss: /all-solutions/weight-loss
unverified_fields:
  - "Prices/IA are a point-in-time snapshot, not fixed — listing cards, PDPs, and the homepage FAQ disagree (Semaglutide inj: $297.00 listing/FAQ vs $347 PDP; Tirzepatide inj: $399.00 listing vs $547 PDP; FAQ floor '$249/mo sublingual Semaglutide' vs $179.10 listing), and decimal listing prices ($179.10, $224.10) imply a new-customer discount."
  - "Exact plan/dose price is set in the quiz-gated /portal checkout (not submitted)."
  - "Self-reported customer count + rating conflict across surfaces: homepage/FAQ 'more than 53,000 satisfied patients … average 4.8-star'; a stale JSON-LD FAQ says '25,000'; JSON-LD AggregateRating says '4.3 / 2,530 reviews.' Recorded, not reconciled."
  - "Founding date, founder, headcount, and legal entity not stated on the site."

description: "Delivers compounded GLP-1 weight-loss medications plus hair, skin, pain, longevity, and energy treatments to U.S. and Canadian adults through licensed telehealth providers, on all-inclusive monthly plans with no membership fee."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; verified against screenshots + the decoded wordmark
logo_url: https://directmeds.com/app/uploads/2025/06/logo.svg   # canonicalized to the wordmark (2.5); JSON-LD `logo` + branding agree
logos:
  wordmark: { src: "https://directmeds.com/app/uploads/2025/06/logo.svg", w: 160, h: 37 }   # mortar+pestle+cross mark + "DirectMeds" (Direct=white, Meds=blue); WHITE/reverse variant on transparent (built for dark bg)
  logomark: { src: "https://www.google.com/s2/favicons?domain=directmeds.com&sz=256", px: 192, transparent: true }   # mortar-&-pestle + cross icon alone, light blue, transparent (larger than the 180px apple-touch-icon)
  og:       { src: "https://directmeds.com/app/uploads/2025/07/DirectMeds.jpg", w: 1200, h: 675 }   # full brand lockup on deep-navy — a true brand cover, not an SEO card
brand_colors: { primary: "#092A3B", accent: "#1F546F" }   # STRAIN: deep navy (OG bg + text) + steel-teal; the logo "Meds" + CTAs use a brighter cyan-blue not in the payload
fonts: [Plus Jakarta Sans]   # branding body+heading; real (not a generic "sans-serif" rank-1)
color_scheme: light
design_framework: wordpress   # rawHtml: /app/uploads, /app/themes, wp-content, WP Engine dev host — Bedrock layout (NOT "custom")
---

## Overview

Direct Meds is a DTC telehealth brand selling **compounded** prescription treatments — anchored on GLP-1 weight loss (semaglutide & tirzepatide) and extending into hair, skin, pain, longevity/anti-aging, and energy/muscle lines, alongside a few OTC appetite-control supplements. The model is insurance-free and **async**: a patient takes a "60-second" online quiz, a licensed provider reviews the intake within hours (no appointment or video visit), and — if prescribed — medication is compounded at a partner U.S. pharmacy and mailed within one business day, with ongoing licensed-nurse support. Everything is sold on an **all-inclusive monthly price** with **no membership fee**. The brand operates in the U.S. and Canada (separate Canadian pharmacy partners) and leans heavily on testimonial/social-proof and a GLP-1 "buying guide" content funnel.

## What they offer

Seven category lines, all all-inclusive monthly, cash-pay (bold lead-in, verbatim price + visibility token; per-SKU depth in `offerings.md`). Prices below are the category-listing figures — **note the PDP and FAQ disagree** (see `unverified_fields`):

- **Weight loss — GLP-1 (the anchor):** compounded semaglutide & tirzepatide, each as once-weekly **injection** or **sublingual drops** — **"$179.10 / mo."** (sublingual Sema) to **"$399.00 / mo."** (Tirz injection); PDPs list higher ($347 / $547) `[published]`
- **Weight loss — appetite supplements:** Citradine (Sinetrol), SatiaLean (DNF-10), Calocurb — OTC botanical appetite-control — **"$59.99 / mo."–"$79.99 / mo."** `[published]`
- **Anti-aging / longevity:** NAD+ **"$399.99 / mo."**, Sermorelin (Sermorix peptide) **"$299.99 / mo."**, Elastira (anti-aging cream) **"$139.00 / mo."** `[published]`
- **Hair loss / hair growth:** Minoxalune (minoxidil) & Capilyn (finasteride) — **"$89.00 / mo."** `[published]`
- **Skin & aesthetic:** Elastira (compounded tretinoin cream) **"$139.00 / mo."**; also Capilyn, Minoxalune, Ortharex `[published]`
- **Pain relief & recovery:** Ortharex — compounded topical diclofenac/baclofen/lidocaine/meloxicam — **"$139.99 / mo."** `[published]`
- **Muscle recovery / energy / performance:** Sermorelin **"$299.99 / mo."**, NAD+ **"$399.99 / mo."** (shared with longevity) `[published]`

GLP-1 is the front door; the rest is a broad compounded catalog. No ED product/category page exists despite ED blog content (content-only). Per-SKU roster + molecule attestation in `offerings.md`.

## How it works / model

Three steps, async by default: **(1) Find out if you qualify** — a "secure online quiz and intake form," no appointments, "no doctor visit required"; **(2) Get your prescription approved** — "a licensed medical provider reviews your case within just a few business hours" (review-only, no video visit mentioned); **(3) Receive medication — fast** — if approved, compounded at "a certified U.S. pharmacy" and shipped "within 1 business day" with free priority shipping, plus ongoing licensed-nurse access. Revenue is an **all-inclusive monthly subscription** per treatment that bundles the provider visit, medication, supplies, shipping, and nurse support; **"No memberships. No hidden fees."** Accepts **HSA/FSA**; offers new-customer discounts and 6-/12-month bulk plans; no insurance billed. Fulfillment runs through **third-party** licensed compounding pharmacies (named partner *CraftedRx* on skin/pain; an unnamed U.S. pharmacy for GLP-1; Canadian partners for Canada).

## Positioning & audience

All-genders general-consumer telehealth (testimonials skew weight-loss, mixed men and women), GLP-1-weight-loss-led, positioned on **transparency, all-inclusive pricing, and no membership** ("No memberships. No hidden fees. Just fast, medically guided results.") plus a **human nurse-support** differentiator ("Real Care, From Real Nurses … most online providers leave patients on their own after checkout"). Sits in the Hims/Henry Meds/Ro compounded-GLP-1 tier, competing on price clarity and support rather than brand prestige.

## Nav structure

```
- All Solutions — /all-solutions/   (category gateway; the storefront)
  - Weight Loss / Body Composition — /all-solutions/weight-loss/
  - Anti-Aging / Longevity — /all-solutions/anti-aging/
  - Muscle Recovery / Energy / Performance — /all-solutions/muscle-recovery-energy/
  - Pain Relief & Recovery — /all-solutions/pain-management/
  - Hair Loss / Hair Growth — /all-solutions/hair-loss-hair-growth/
  - Skin & Aesthetic — /all-solutions/skin-aesthetic/
- How It Works — /how-it-works/
- Patient Success — /direct-meds-reviews/
- GLP-1 Buying Guide — # (flyout)
  - Intro: Guide to Buying GLP-1 Medications Online — /guide-to-buying-glp-1-medications-online/
  - Chapter 1: Ordering Semaglutide Online — /guide-to-buying-glp-1-medications-online/ordering-semaglutide-online/
  - Chapter 2: Buying Tirzepatide Online — /guide-to-buying-glp-1-medications-online/buying-tirzepatide-online/
  - Chapter 3: Weight Loss Injections — /guide-to-buying-glp-1-medications-online/weight-loss-injections/
  - Chapter 4: Oral Semaglutide — /guide-to-buying-glp-1-medications-online/oral-semaglutide/
  - Chapter 5: Oral Tirzepatide — /guide-to-buying-glp-1-medications-online/oral-tirzepatide/
- Customer Support — /contact-us/
- Login — https://portal.directmeds.com/login
- Get Started (quiz) — /dm-q2spc-c31/questionnaire-1.php?...&affid=26
Footer: How It Works · Patient Success · Customer Support · Blog · Become An Advocate (/advocate) · FAQ's · Contact Us · Careers
```
*(Top nav + flyout from JSON-LD `SiteNavigationElement` + the `<header>` region; the six category lines come from the homepage "What do you need help with?" grid + /all-solutions, not the top nav. Validated against the homepage screenshot.)*

## Credibility & proof

- **LegitScript-certified:** footer seal linking to legitscript.com verification for directmeds.com.
- **HIPAA-compliant:** footer badge.
- **Third-party tested + Certificate of Analysis:** every Rx PDP shows a "Direct Meds Certificate of Analysis" image and claims independent testing "for purity, potency, and consistency."
- **Self-reported scale/rating (flagged, and internally inconsistent):** homepage + FAQ — *"more than 53,000 satisfied patients and an average 4.8-star rating"* and *"Trusted by over 53,000+ happy customers"* (Trustpilot micro-widget, no review URL); a **stale JSON-LD FAQ** says *"more than 25,000 satisfied patients"*; JSON-LD `AggregateRating` says **"4.3 / 2,530 reviews."** Recorded verbatim, not endorsed or reconciled.
- **Press (logos, self-presented):** The Balancing Act (Lifetime), OK Magazine ("disrupting the telemedicine world"), Woman's World, LA Weekly, Health Uncensored with Dr. Drew.
- **Named partner pharmacy:** *"CraftedRx is a licensed U.S. compounding pharmacy"* (Elastira & Ortharex PDPs); GLP-1 fulfilled by an unnamed U.S. pharmacy "where the majority of our U.S. orders are compounded" (/meet-the-pharmacy).
- **No named-clinician / `/physicians` roster page found.** Compounded-meds FDA disclaimer present site-wide ("Compounded medications are not FDA-approved").

## Visual & brand impression

Clean, light, consumer-wellness aesthetic — white backgrounds, deep-navy (#092A3B) structure and footer, a brighter cyan-blue for CTAs and the "Meds" wordmark, set in **Plus Jakarta Sans** with rounded 12px cards. The logo is a friendly **mortar-and-pestle + medical-cross** mark (apothecary cue) beside the "DirectMeds" wordmark; the hostable header logo is the white/reverse variant, and the OG cover renders the full lockup on navy. The homepage is long and conversion-dense: a rotating "Lose Weight. Gain Confidence." hero, a "What do you need help with?" category grid, a popular-meds price carousel, a press-logo wall, video + written testimonials, and an avatar-driven FAQ ("Charles from New York asks…"). Design maturity is solid mid-market DTC — polished but template-heavy and repetitive. Notable: a footer disclosure that **"Certain images and videos on this website may … be AI-generated or AI-enhanced,"** and placeholder testimonial avatars — softening the otherwise heavy social-proof.

## Strategic read

- **A GLP-1 weight-loss funnel with a broad compounded catalog bolted on.** JSON-LD, the buying guide, and the hero are all GLP-1; the other six categories share the same async quiz + all-inclusive-monthly machinery but get far less prominence.
- **Pricing is opaque-by-inconsistency, not by gating.** A price *is* shown on every listing, but the listing, the PDP, and the FAQ disagree for the same SKU, and decimal listing prices look promo-driven — the real number is settled in the /portal checkout. Worth re-capturing before any quote.
- **Multi-pharmacy, multi-country fulfillment** (CraftedRx for skin/pain, an unnamed U.S. pharmacy for GLP-1, Canadian partners) — a routing brand, not a vertically integrated one; no ownership claimed.
- **Affiliate-driven acquisition** (every "Get Started" CTA carries `affid=`/`oid=`/`uid=` params), consistent with the heavy press + testimonial surface.

## Provenance

- **Pages:** 17 captured via Firecrawl (homepage; how-it-works; all-solutions hub + 6 category pages: weight-loss, anti-aging, hair, skin, pain, muscle-energy; understanding-the-price; meet-the-pharmacy; about-us; 4 PDPs: semaglutide-10, tirzepatide, elastira, ortharex). Synthesized across all + full-page screenshots + branding/rawHtml + JSON-LD (`fc.py signals`).
- **Verify:** all 17 sourceURLs matched; all body md5s unique — no geo/cache contamination.
- **Credits:** 18 (1 map + 17 scrapes).
- **Couldn't get:** exact quiz/portal-gated dose prices; a reconciled customer-count/rating (three conflicting self-reported figures recorded); founding date / founder / legal entity (not on site).
- **Run profile:** guided — all modules (+telehealth, +offerings, +logos); no emphasis.
