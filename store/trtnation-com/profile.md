---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: trtnation.com
name: TRT Nation
aliases: ["America's Clinic"]         # trademarked brand line used sitewide ("AMERICA'S CLINIC™"); not a separate legal entity
parent: []
owns: []
socials:
  x: https://x.com/trtnationclinic
  youtube: https://www.youtube.com/channel/UCCIUm-uwvYXrLWDhb1ZMb1Q
external: {}                          # no third-party records (crunchbase/wikipedia/etc.) linked from the site

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "WordPress + Elementor (rawHtml: wp-content + elementor + wp-json; branding.designSystem 'custom' is wrong as usual). Bot-defended: plain curl to the apex 403s — capture Firecrawl-only. Products are inline cards on the category pages (/testosterone-therapy/, /weight-loss-therapy/, /anti-aging/, /sexual-health/), NOT separate PDPs; 'Select' buttons route to the /trtlw/ /wllw/ /aalw/ /shlw/ funnels. Clean isolated product renders live at wp-content/uploads/.../<Name>-Product.png (one per SKU). /popular-treatments/ is a 'popular' SUBSET — the dedicated category pages are the complete roster (Tesamorelin + IGF1-LR3 appear only on /anti-aging/). Google-reviews + a large reviews widget bloat every page's markdown."
key_pages:
  testosterone: /testosterone-therapy/
  weight_loss: /weight-loss-therapy/
  anti_aging: /anti-aging/
  sexual_health: /sexual-health/
  popular: /popular-treatments/
  labs: /lab-orders/
  about: /about/
  faqs: /faqs/
unverified_fields:
  - "Founding year — 'For over a decade' (about) is the only date signal; no explicit year stated."
  - "Pharmacy partner identity/lane (503A vs 503B) — never named; only 'licensed U.S. compounding pharmacies' / 'pharmacy partner.'"
  - "Provider names/credentials — 'licensed providers/clinicians' generically; no /physicians roster page."

# Description — one sentence: what they do + how + focus/differentiator.
description: "Delivers TRT, weight-loss, sexual-health, and anti-aging therapies to men via licensed-provider telehealth and compounded medications from U.S. pharmacies, on flat per-treatment monthly pricing with bring-your-own-labs flexibility."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product        # 4 distinct enumerable therapy lines (TRT · weight loss · sexual health · anti-aging) + labs; TRT is the brand-anchor flagship
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; confirmed against screenshots.
logo_url: https://trtnation.com/wp-content/uploads/2024/12/LOGO-with-R-e1737473379227.png   # canonical wordmark
logos:
  wordmark: { src: "https://trtnation.com/wp-content/uploads/2024/12/LOGO-with-R-e1737473379227.png", w: 250, h: 83 }   # horizontal "TR" monogram + TRTNATION®
  logomark: { src: "https://trtnation.com/wp-content/uploads/2024/11/Logo-HD-blk-150x150-1.png", px: 150, transparent: true }   # stacked square mark (JSON-LD logo); transparent confirmed on a checker tile. google-s2 favicon was only 30px — recorded the real 150px brand mark instead
  # og: omitted — no og:image declared on the homepage (true absence)
brand_colors: { primary: "#10203B", accent: "#E8AA21" }   # navy structural + gold accent. NOTE: branding payload inverted these (primary gold / accent navy) — visual read makes navy the base, gold the pop
fonts: [Poppins, Norwester]           # Poppins (headings) + Norwester (condensed display, hero + logo); body falls back to Arial/Helvetica
color_scheme: light                   # white content body; navy hero/section bands
design_framework: wordpress           # WordPress + Elementor (rawHtml), not "custom"
---

## Overview

TRT Nation is a direct-to-consumer **men's-health telehealth clinic** — self-styled "America's Clinic™" — that
sells hormone, weight-loss, sexual-health, and anti-aging treatment programs 100% online. It pairs a licensed-
provider video/phone consult with compounded and generic medications shipped to the patient's door from U.S.
pharmacies. The wedge is **price and lab flexibility**: testosterone is fronted at **$99/mo**, "any dose, same
price" weight-loss at **$219/mo**, with **no membership fee** and an explicit willingness to accept a patient's
own outside bloodwork ("one of the few clinics that accepts outside lab work"). Based in Tampa, FL; operates in
every U.S. state except Alabama, Alaska, Arkansas, Missouri, and Hawaii; treats patients 24 and older.

## What they offer

Four therapy lines (all per-treatment monthly subscriptions) plus à-la-carte lab panels — per-SKU roster in
[`offerings.md`](offerings.md):

- **Testosterone therapy:** injectable Testosterone **$99.99/mo**, Enclomiphene (oral) **$99.99/mo**, TRT + HCG **$180/mo** — the flagship line `[published]`
- **Weight loss:** Tirzepatide **$219/mo** ("any dose, same price"), Phentermine **$99.99/mo** `[published]`
- **Sexual health:** Tadalafil **$99.99**, Sildenafil **$99.99**, Enclomiphene **$99.99/mo**, HCG **$80/mo** `[published]`
- **Anti-aging / peptides:** NAD+ **$120/mo**, Glutathione **$80/mo**, Sermorelin **$199.99/mo**, Tesamorelin **$233/mo**, IGF1-LR3 **$159.99/mo** `[published]`
- **Lab panels:** TRT Bloodwork **$129**, Weight Loss Bloodwork **$129**, TRT + Weight Loss Bloodwork **$179** (via LabCorp / Quest) `[published]`

Pricing is unusually transparent for the cohort — every SKU shows a number on the category page (no intake wall),
with per-product minimum-purchase commitments (2.5-month minimum on testosterone/HCG/NAD+; 3-month on
tirzepatide/tesamorelin) in the footnotes.

## How it works / model

A four-step async-to-sync journey: **(1) select treatment → (2) submit your own labs or order labs through them →
(3) meet a licensed provider via video or phone → (4) medication ships discreetly via FedEx.** Money is made on
recurring monthly medication subscriptions (per treatment, billed monthly); labs are a separate one-time charge.
Ongoing care is included in the medication price — "unlimited support," secure messaging between appointments, and
mandatory lab monitoring (after the first 10 weeks, at 6 months, then yearly). No separate membership or platform fee.

## Positioning & audience

Targets adult men (24+) seeking hormone optimization, positioned against both traditional in-person hormone
clinics ("1/3 of the cost," "without the commute, waiting rooms") and higher-friction online competitors ("no
hidden prices or membership fees," "no pushy protocols"). The claimed edge is a trifecta of **affordability,
price transparency, and provider specialization** ("our providers specialize exclusively in hormone optimization,
men's health, and anti-aging medicine"), plus the bring-your-own-labs flexibility most peers don't offer.
Men's-health-first, though weight-loss and labs are not gender-gated (the lab order form accepts Female).

## Nav structure

```
- Testosterone — /testosterone-therapy/
- Weight Loss — /weight-loss-therapy/
- Anti-Aging — /anti-aging/
- Sexual Health — /sexual-health/
- Popular — /popular-treatments/
- Labs — /lab-orders/
- Sign In (Patient Refill) — /trt-nation-refill-validation/
- About TRT Nation
  - About Us — /about/
  - Peer Reviewed — /evidence-based-excellence-how-trt-nation-is-revolutionizing-testosterone-therapy/
  - Customer Reviews — /reviews
  - Contact — /contact-testosterone-replacement/
- Resources
  - FAQs — /faqs/
  - Science Hub (blog) — /blog/
  - Become An Affiliate — /affiliate-program/
  - Patient Sign In/Refill — /trt-nation-refill-validation/
- Footer: Terms — /buy-online/terms-conditions/ · Privacy — /privacy-policy/ · Cancellation — /cancellation-policy/ · Affiliate — /affiliate-partner-program/
```

## Credibility & proof

- **Reviews:** "Excellent — TRT Nation 4.9 Based on 1943 reviews" (embedded Google-reviews widget, self-reported)
- **LegitScript-certified:** footer seal (cert #14914193), linked to LegitScript's verification page
- **Compliance/quality claims:** "USA Made" seal; "Trusted Lab Network"; "All medications prescribed through TRT Nation are sourced from licensed U.S. compounding pharmacies. You will never receive counterfeit or unregulated substances." (FAQ, self-reported)
- **Provider specialization:** "our providers specialize exclusively in hormone optimization, men's health, and anti-aging medicine" — no named clinicians or /physicians roster
- **Tenure claim:** "For over a decade, TRT Nation has been at the forefront of men's health and wellness" (about, self-reported)
- **Contact / trust footprint:** 813-413-1000; 12602 Telecom Drive, Tampa FL 33637

## Visual & brand impression

Confident, masculine, value-forward DTC design. A **dark-navy (#10203B) + gold (#E8AA21)** palette runs throughout:
navy hero/section bands with gold CTAs and a gold-labeled testosterone vial as the recurring hero object. The
"TR" monogram wordmark is sharp and angular (condensed display type, Norwester/Poppins). Product cards use clean,
color-coded isolated vial renders (gold = testosterone, teal = tirzepatide, green = sermorelin, etc.) on white —
a coherent, premium-feeling product system. Overall the site reads as a polished, conversion-optimized men's-health
storefront: price-led, badge-heavy ("#1 IN THE NATION," "MOST AFFORDABLE"), heavy on social proof.

## Strategic read

The differentiator is **radical price transparency in a cohort built on price opacity**. Where most telehealth
peers quiz-wall the price (`[on-request]`) and stack a mandatory membership, TRT Nation publishes a flat number on
every SKU, advertises "no membership fees," and undercuts on the headline ($99/mo TRT). The **bring-your-own-labs**
posture is a genuine cohort-rare wedge — it removes the lab markup most clinics rely on and lowers the switching
cost for men already on TRT elsewhere ("transferred my prescription"). Trade-offs are visible: minimum-purchase
commitments (2.5–3 months) offset the low entry price, and the pharmacy/provider layer is thin on named-entity
proof (no pharmacy partner named, no clinician roster) — credibility leans on the LegitScript seal and a large
Google-review wall rather than disclosed people.

## Provenance

- **Pages:** 9 analyzed via Firecrawl (homepage, /testosterone-therapy/, /weight-loss-therapy/, /anti-aging/, /sexual-health/, /popular-treatments/, /lab-orders/, /about/, /faqs/) + the homepage JSON-LD/branding structured layer; full-page screenshots for all.
- **Verify:** all 9 sourceURLs matched; all 9 body md5s unique — no geo/cache contamination.
- **Credits:** 10 (1 map + 1 homepage + 8 key pages). Product-render + logo asset fetches were headed downloads (no credits).
- **Couldn't get:** founding year (only "over a decade"); pharmacy partner name + 503A/503B lane; provider names. See `unverified_fields`.
- **Run profile:** guided — emphasis "full module pack"; +offerings (with flagship/product hero images), +telehealth cohort pack, +logos. All 13 SKU product renders captured to `captures/2026-06-04/images/` (not just flagships).
- **Structured layer:** homepage JSON-LD (`Organization` "TRT Nation", `logo` 150×150 → logomark; no `sameAs`) + footer/about anchors seeded `socials` (X, YouTube — both verified to this entity). No `alternateName`/`legalName`; "America's Clinic" added to `aliases` from sitewide trademark usage.
