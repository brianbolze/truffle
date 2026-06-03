---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.3"

# Identity
domain: ro.co
name: Ro
aliases: [Roman]                     # "Roman" is Ro's heritage/men's-health brand (now a sub-brand at /roman/); rebranded to parent "Ro"
parent: []
owns: []
socials: {}                          # none in captured footer/JSON-LD (icons may be client-rendered)
external: {}                         # JSON-LD carried no sameAs

# Capture meta
captured_at: 2026-06-01
capture_method: firecrawl
site_notes: "React/Remix SPA; mega-nav is client-rendered (signals <header> collapsed) — rebuild nav from homepage markdown links, which capture the full flyout. A/B: yes (own engine, ro-experiments/roexp.min.js) — pricing/IA is point-in-time. Datadog RUM + Cloudflare + GTM. Comprehensive per-condition pricing at /pricing/ AND per-product pages; Ro Body (GLP-1) membership price lives in the /weight-loss/how-it-works/ FAQ, med cost billed separately/gated. Map (499 urls) is swamped by /health-guide, /weight-loss/*, /erectile-dysfunction/* SEO content + /network-physician/* bios — select from homepage links, not the map."
key_pages:
  pricing: /pricing/
  weight_loss: /weight-loss/
  weight_loss_how_it_works: /weight-loss/how-it-works/
  erectile_dysfunction: /erectile-dysfunction/
  ro_os: /os/
  founder_letter: /founder-letter/
  advisors: /advisors/
  faq: /faq/
unverified_fields:
  - "GLP-1 medication cash price — billed separately from the Ro Body membership; 'varies by medication and insurance', not published."
  - "Prices/IA are a point-in-time snapshot, not fixed — own A/B engine (ro-experiments) + promo-driven offers (e.g. TrumpRx pricing, $20-off ED) rotate."

description: "A DTC telehealth company connecting patients to licensed providers, a nationwide pharmacy, and at-home labs on one vertically integrated platform, delivering prescription weight-loss, sexual-health, hair, skin, and fertility treatments online."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://ro.co/rocostatic/favicon.svg   # on-domain SVG mark (branding.images.logo + JSON-LD logo both absent)
brand_colors: { primary: "#1A1A1A", accent: "#F8FFA1", secondary: "#5E6F8D" }   # black wordmark/text on white; signature acid-chartreuse accent (branding called it "primary"); muted blue-grey + pastel photo blocks
fonts: [Ro Sans]                     # proprietary typeface (branding.fonts[0], body role)
color_scheme: light
design_framework: custom (react/remix spa)   # rawHtml: react + remix markers, hashed /assets/, no __NEXT_DATA__/gatsby/wp; branding "custom" agrees
---

## Overview

Ro is a direct-to-consumer telehealth company that gets patients prescription treatment online — online visit → licensed-provider review → medication shipped or sent to a pharmacy, with ongoing messaging and support. It spans six consumer health goals: weight loss (GLP-1s), sexual health (ED, premature ejaculation), hair loss, skin/dermatology, fertility, and daily supplements. Founded by Zachariah Reitano, Saman Rahmanian, and Rob Schutz (per the founders' letter), it began as the men's-health brand **Roman** and broadened into the gender-neutral **Ro** parent; Roman survives as the men's sexual-health sub-brand (`/roman/`). The pitch is patient-as-first-call: "handle everything you need from beginning to end," with technology that empowers — not replaces — clinicians.

## What they offer

Six condition lines, mostly subscription with monthly/quarterly/annual plans (prices verbatim from `/pricing/`; med names quoted):

- **Weight loss — Ro Body membership:** GLP-1 access + insurance concierge + coaching/labs — **$39 first month, then $74/mo prepaid annually (or $149/mo monthly)**; medication cost billed separately. Meds: Wegovy pill (semaglutide), Zepbound KwikPen + pen (tirzepatide), Foundayo pill (orforglipron), Wegovy pen, Ozempic. `[partial]` (membership published, med cash price gated)
- **Sexual health — ED:** Ro Sparks (sildenafil 55mg/tadalafil 22mg, compounded) **$48–$120/mo**; Daily Rise Gummies (tadalafil 7mg, compounded) **$69–$89/mo**; generic Viagra/sildenafil **from $2–$10/dose**; branded Viagra **$90**; generic Cialis/tadalafil **$8–$44**; branded Cialis **$20–$80**. `[published]`
- **Premature ejaculation:** Roman Swipes (4% benzocaine, OTC) **$22–$27/mo**; sertraline (generic Zoloft) **$24/mo**. `[published]`
- **Hair loss (men):** finasteride **$16–$20/mo**; oral minoxidil **$24–$30/mo**; topical minoxidil **$13–$16/mo**; Ro Mane Spray (3-in-1 compounded) **$43–$50/mo**. `[published]`
- **Women's hair loss:** women's oral minoxidil **$30/mo**; Hair Solution Rx (compounded) **$40/mo**. `[published]`
- **Skin / dermatology:** Custom Rx skincare **$29/mo**; enriching cream **$8/mo**; LATISSE (bimatoprost, lashes) **$110/mo or $159/quarter**. `[published]`
- **Cold sores / genital herpes:** valacyclovir (generic Valtrex) **$42–$144 per 3 mo** by dose/use. `[published]`
- **Fertility:** Fertility Hormone Test, Ovulation Test, Pregnancy Test, Prenatal Multivitamin, Sperm Kit. `[on-request]` (priced via intake; not on `/pricing/`)
- **Daily health (OTC supplements):** Ro Daily men's multivitamin **$29–$35/mo**; Testosterone Support **$29–$35/mo**. `[published]`

## How it works / model

Customer journey (weight-loss example, but the pattern generalizes): **1)** online visit answering health/lifestyle/goals questions (no in-person visit; eligibility within ~2 days); **2)** provider reviews and prescribes if eligible — "you won't be charged the ongoing membership fee" if you don't qualify; **3)** Ro's insurance concierge navigates coverage/prior-auth, or recommends cash-pay options; **4)** medication picked up at pharmacy or delivered; **5)** ongoing support — unlimited provider messaging, dose titration, side-effect management, refills. Money: recurring **memberships** (Ro Body) + recurring medication/refill **subscriptions** with monthly/quarterly/annual tiers (quarterly/annual discounted). The Ro Body membership is **cash-pay only** (does not accept insurance for the membership fee itself), while it coordinates insurance for the medication.

The structural differentiator is **ro.OS (Ro Operating System)** — a vertically integrated platform combining nationwide telehealth, pharmacy, and lab services, with four apps (Patient, Care Delivery/EMR, Pharmacy, Lab) plus capabilities (Patient Intake, Care Comms, Insurance, Quality & Safety, Health Data, Test Kits). It is **exclusively for Ro's own patients/providers — not sold to other companies** (so the model stays B2C, not a B2B platform play).

## Positioning & audience

Mass-consumer, no longer male-only: weight loss is the foregrounded hero (top promo bar, hero, ambassadors Serena Williams + Charles Barkley), with sexual health the legacy strength. Claimed edges: **lowest-cost GLP-1s with or without insurance**, real licensed providers, FDA-approved options, fully online, and an insurance concierge that "fights for coverage." Generic-vs-branded price transparency is a repeated wedge ("up to 95% cheaper than branded"). Competes with Hims & Hers, Lemonaid, and GLP-1-era entrants; the vertically integrated ro.OS (own pharmacy + labs) is the moat it markets.

## Nav structure

```
- Weight Loss — /weight-loss/
  - The Ro Body membership — /weight-loss/
  - Wegovy pill (semaglutide) — /weight-loss/wegovy-pill/
  - Wegovy pen — /weight-loss/wegovy/
  - Foundayo pill (orforglipron) — /weight-loss/foundayo/
  - Zepbound KwikPen / Zepbound — /weight-loss/zepbound/
  - Ozempic — /weight-loss/ozempic/
  - Saxenda — /weight-loss/saxenda/
  - How it works — /weight-loss/how-it-works/  · Pricing — /weight-loss/pricing/  · Insurance — /weight-loss/insurance/
  - Ambassadors: Serena Williams, Charles Barkley, Hannah, Greg, The Taylors
- Sexual Health
  - Erectile Dysfunction — /erectile-dysfunction/
  - Ro Sparks — /erectile-dysfunction/sparks/  · Daily Rise Gummies — /erectile-dysfunction/daily-rise-gummies/
  - Viagra / Sildenafil / Cialis / Tadalafil — /erectile-dysfunction/{viagra,sildenafil,cialis,tadalafil}/
  - Premature Ejaculation — /premature-ejaculation/  · Roman Swipes — /products/swipes/
  - Testosterone Support Supplement — /supplements/testosterone-support/
  - Genital Herpes — /genital-herpes/  · Cold Sores — /cold-sores/  · Valacyclovir — /medications/valacyclovir/
  - (endcap) Men's health experts → /roman/
- Fertility — /fertility/
  - Fertility Hormone Test / Ovulation Test / Pregnancy Test — /testing/...
  - Prenatal Multivitamin — /supplements/prenatal-vitamins/  · Sperm Kit — spermkit.ro.co
- Hair — /hair-loss/
  - Men: Ro Mane Spray, Oral Finasteride, Oral Minoxidil, Topical Minoxidil, Revive Shampoo, Restore Conditioner
  - Women: /womens-hair-loss/ — Oral Minoxidil, Hair Solution Rx; LATISSE (lashes)
- Skin — /dermatology/
  - LATISSE — /medications/latisse/  · Custom Rx Skincare — /dermatology/custom-rx-treatment/
  - Cold Sores / Genital Herpes
- Daily Health
  - Men's Daily Multivitamin — /supplements/mens-daily-multivitamin/
  - Prenatal Multivitamin  · Testosterone Support Supplement
- Top Products (Sexual Health / Weight Loss / Hair & Skin / Over-the-counter)
- What We Treat (A–Z): Acne, Cold Sores, ED, Genital Herpes, Hair Loss, Obesity/Overweight, Photoaging, Premature Ejaculation, Short Lashes
- Footer — About Ro: Founders letter, Ro Operating System (/os/), Advisors, Careers, Tech @ Ro, Press, Health Guide, Blog
  - Support: Contact, FAQ, Returns & Refunds, Pricing (/pricing/)
  - Free tools: GLP-1 Insurance Checker, BMI/BMR/TDEE/Calorie-Deficit/Protein calculators, GLP-1 Supply Tracker
  - Legal: Terms, Privacy, Consumer Health Data Privacy
- Log in — /my/home/
```

## Credibility & proof

- **Scale (self-reported):** "**3,000,000+** members and counting"; "**95%** love their experience"; ro.OS page claims "Millions of patients helped," "Tens of millions of treatments delivered," "Hundreds of millions of care interactions."
- **Outcome claims (self-reported, weight loss):** "Drop 20% of your weight," "Average weight loss in 1 year is 11–20% (vs ~2–3% with diet and exercise alone)"; member survey (n=1,243, ≥7 weeks): **87%** life-changing results, **93%** easier to incorporate, **97%** quieter food noise.
- **Clinical leadership:** CMO Dr. Melynda Barnes (triple board-certified); advisors page; "Former Surgeon General and Head of the DEA" cited among advisors; "100s of published studies." Provider/credential network surfaced via `/network-physician/*` and `/advisors/`.
- **Certification:** LegitScript-certified seal in footer.
- **Safety posture:** prominent GLP-1 boxed-warning language (thyroid tumors / MTC / MEN 2); explicit "compounded… not FDA-approved" disclaimers on Ro Sparks, Daily Rise Gummies, Ro Mane Spray; off-label disclosures (Ozempic, oral minoxidil, valacyclovir).

## Visual & brand impression

Clean, confident, mainstream-premium — not the edgy-bro aesthetic of early men's-health DTC. White canvas segmented into soft pastel photo blocks (peach/coral, lilac, cream, muted blue-grey), large lifestyle photography of real, diverse people, and uniform product tiles. Signature acid-chartreuse (#F8FFA1) accent bar up top; deep near-black footer. Proprietary "Ro Sans" typeface, generous spacing, minimal ornament. Reads as a trusted, broad-market consumer-health brand that has deliberately outgrown its niche origins.

## Strategic read

Most relevant comp signal for a men's-health-adjacent venture: Ro's durable advantage is **owning the stack** — its own pharmacy and at-home labs under ro.OS — which lets it market "lowest-cost GLP-1s" and absorb insurance friction (the concierge) as a feature, not a cost center. It runs its **own A/B experimentation engine** (`ro-experiments`), so its pricing, hero offers, and IA shift continuously (TrumpRx pricing, $20-off ED, promo bars) — any single capture is a snapshot. Pricing transparency (a public `/pricing/` page enumerating generics by dose) is itself a positioning weapon worth noting; many competitors gate everything behind intake.

## Provenance

- **Pages:** homepage, /pricing/, /weight-loss/, /weight-loss/how-it-works/, /erectile-dysfunction/, /os/, /founder-letter/ (7 pages); Firecrawl scrape, all formats on homepage; map (499 urls) for inventory.
- **Verify:** all 7 sourceURLs matched requested; all body md5s unique (no geo/cache contamination).
- **Credits:** 8 (1 map + 7 scrapes), all basic proxy; ~1347 remaining.
- **Couldn't get:** GLP-1 medication cash price (gated, varies by med/insurance); social handles (none in footer markdown / JSON-LD); per-SKU fertility pricing (intake-walled).
- **Enriched (model knowledge):** "Roman" ↔ "Ro" rebrand/heritage relationship used for identity resolution only — Roman path (`/roman/`) is on-site; founders are named on the captured `/founder-letter/` page (not enriched).
