---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: ro.co
name: Ro
legal_entity: ""                     # 2.6: not site-derivable — JSON-LD carries only name "Ro" (no legalName); captured footer shows "Ro" + LegitScript, no ©/legal-entity line. (Terms/Privacy pages not captured.)
aliases: [Roman]                     # "Roman" is Ro's heritage/men's-health brand (now a sub-brand at /roman/); rebranded to parent "Ro"
parent: []
owns: []
socials: {}                          # none in captured footer/JSON-LD (icons may be client-rendered)
external: {}                         # JSON-LD carried no sameAs

# Capture meta
captured_at: 2026-06-18
capture_method: firecrawl
site_notes: "React/Remix SPA; mega-nav is client-rendered (signals <header> collapsed) — rebuild nav from homepage markdown links, which capture the full flyout. A/B: yes (own engine, ro-experiments/roexp.min.js) — pricing/IA is point-in-time. Datadog RUM + Cloudflare + GTM. Pricing split: /pricing/ enumerates per-SKU price + molecule + 'Most popular' badge for EVERY line EXCEPT GLP-1s (whose 'Weight management' block shows only the Ro Body membership) and fertility (intake-gated, no public price); GLP-1 prices live only on /weight-loss/pricing/. Map (~500 urls) is swamped by /health-guide, /weight-loss/*, /erectile-dysfunction/* SEO content + /network-physician/* bios — select from homepage links, not the map. Per-SKU roster (all 8 lines) → offerings.md."
key_pages:
  pricing: /pricing/
  weight_loss: /weight-loss/
  weight_loss_pricing: /weight-loss/pricing/
  weight_loss_how_it_works: /weight-loss/how-it-works/
  erectile_dysfunction: /erectile-dysfunction/
  premature_ejaculation: /premature-ejaculation/
  hair_loss: /hair-loss/
  dermatology: /dermatology/
  fertility: /fertility/
  ro_os: /os/
  founder_letter: /founder-letter/
  advisors: /advisors/
  faq: /faq/
unverified_fields:
  - "GLP-1 all-in cash cost — per-SKU 'first month' + 'thereafter' ranges ARE published on /weight-loss/pricing/ (e.g. Wegovy pill $149→$199-299, Zepbound KwikPen $299→$399-449, Ozempic $900-1100), but the all-in = those + a separately-billed Ro Body membership ($74-149/mo) + a provider-titrated dose ladder; full per-dose ladders for Wegovy pill/pen + Foundayo sit behind an unrendered 'See pricing details' expander (only Zepbound KwikPen's full ladder is in the FAQ)."
  - "Fertility line (Modern Fertility kits + Sperm Kit), Upneeq, and Saxenda carry no public price — quiz/intake-gated or nav/FAQ-only; Saxenda's molecule is unnamed on captured pages."
  - "Prices/IA are a point-in-time snapshot, not fixed — own A/B engine (ro-experiments) + promo-driven offers (TrumpRx/LillyDirect/NovoCare-matched cash pricing, Prepay & Save, a now-expired '$20-off ED through 6/7') rotate. 2026-06-18 re-capture found the full roster + prices unchanged vs 2026-06-04."

description: "A DTC telehealth company connecting patients to licensed providers, a nationwide pharmacy, and at-home labs on one vertically integrated platform, delivering prescription weight-loss, sexual-health, hair, skin, and fertility treatments online."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg        # 2.5: canonicalized to the wordmark — the inline "ro" logotype SVG (branding.images.logo, decoded from its data-URI). Favicon fallback was https://ro.co/rocostatic/favicon.svg
logos:                               # 2.5 module (+logos this run); each slot = what was found + ITS measurements (consumer applies the bar)
  wordmark: { src: assets/wordmark.svg, w: 30, h: 17 }                                              # the "ro" logotype, black #1A1A1A, transparent SVG (committed text, scales infinitely); viewBox 0 0 64 36
  logomark: { src: "https://ro.co/apple-touch-icon.png", px: 144, transparent: false }              # "ro" mark on a BAKED white square — renders as a white box on a dark slide (apple-touch-icon; google s2 returned only 32px)
  og:       { src: "https://imgctf--assets.ro.co/jj2wf7627pjc/3QamN652IGIe5jHXBe73mP/4d7444afacc2a6b53bd1ba48d3f2044f/og-ro.jpg", w: 2400, h: 1260 }   # clean brand cover — "ro" wordmark + lifestyle/product photo grid
brand_colors: { primary: "#1A1A1A", accent: "#F8FFA1", secondary: "#5E6F8D" }   # black wordmark/text on white; signature acid-chartreuse accent (branding called it "primary"); muted blue-grey + pastel photo blocks
fonts: [Ro Sans]                     # proprietary typeface (branding.fonts[0], body role)
color_scheme: light
design_framework: custom (react/remix spa)   # rawHtml: react + remix markers, hashed /assets/, no __NEXT_DATA__/gatsby/wp; branding "custom" agrees
---

## Overview

Ro is a direct-to-consumer telehealth company that gets patients prescription treatment online — online visit → licensed-provider review → medication shipped or sent to a pharmacy, with ongoing messaging and support. It spans six consumer health goals: weight loss (GLP-1s), sexual health (ED, premature ejaculation), hair loss, skin/dermatology, fertility, and daily supplements. Founded by Zachariah Reitano, Saman Rahmanian, and Rob Schutz (per the founders' letter), it began as the men's-health brand **Roman** and broadened into the gender-neutral **Ro** parent; Roman survives as the men's sexual-health sub-brand (`/roman/`). The pitch is patient-as-first-call: "handle everything you need from beginning to end," with technology that empowers — not replaces — clinicians.

## What they offer

Six condition lines, mostly subscription with monthly/quarterly/annual plans (prices verbatim from `/pricing/`; med names quoted):

- **Weight loss — Ro Body membership:** GLP-1 access + insurance concierge + coaching/labs — **$39 first month, then $74/mo prepaid annually (or $149/mo monthly)**; medication billed separately, with published cash starting prices: Wegovy pill (semaglutide) **$149→$199-299**, Foundayo pill (orforglipron) **$149→$199-299**, Zepbound KwikPen (tirzepatide) **$299→$399-449**, Wegovy pen **$199→$199-399**, Ozempic **$900-1100 cash**; "Prepay & Save" cuts up to $150/mo. `[partial]` (membership + starting med price published; per-dose ladder + all-in still gated)
- **Sexual health — ED:** Ro Sparks (sildenafil 55mg/tadalafil 22mg, compounded) **$48–$120/mo**; Daily Rise Gummies (tadalafil 7mg, compounded) **$69–$89/mo**; generic Viagra/sildenafil **from $2–$10/dose**; branded Viagra **$90**; generic Cialis/tadalafil **$8–$44**; branded Cialis **$20–$80**. `[published]`
- **Premature ejaculation:** Roman Swipes (4% benzocaine, OTC) **$22–$27/mo**; sertraline (generic Zoloft) **$24/mo**. `[published]`
- **Hair loss (men):** finasteride **$16–$20/mo**; oral minoxidil **$24–$30/mo**; topical minoxidil **$13–$16/mo**; Ro Mane Spray (3-in-1 compounded) **$43–$50/mo**. `[published]`
- **Women's hair loss:** women's oral minoxidil **$30/mo**; Hair Solution Rx (compounded) **$40/mo**. `[published]`
- **Skin / dermatology:** Custom Rx skincare (compounded blend) **$29/mo**; enriching cream **$8/mo**; LATISSE (bimatoprost, lashes) **$110/mo or $159/quarter**. `[published]` — plus Upneeq (oxymetazoline, ptosis eye drop), FAQ-only, no price `[on-request]`
- **Cold sores / genital herpes:** valacyclovir (generic Valtrex) **$42–$144 per 3 mo** by dose/use. `[published]`
- **Fertility — Modern Fertility (acquired by Ro):** Fertility Hormone Test (best seller), Ovulation Test, Pregnancy Test, Prenatal Multivitamin, Sperm Kit (`spermkit.ro.co`). `[on-request]` (quiz/intake-gated; not on `/pricing/`)
- **Daily health (OTC supplements):** Ro Daily men's multivitamin (23 nutrients) **$29–$35/mo**; Testosterone Support **$29–$35/mo**. `[published]`

Full per-SKU roster across all eight lines (~30 SKUs, molecules + dose ladders + visibility) → [`offerings.md`](offerings.md).

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

- **Scale (self-reported):** "**3,000,000+** members and counting"; "**95%** love their experience"; "**3,000,000+** members treated" (ED page); "Join **250,000+** Ro patients" (derm page); ro.OS page claims "Millions of patients helped," "Tens of millions of treatments delivered," "Hundreds of millions of care interactions."
- **Outcome claims (self-reported, weight loss):** "Drop 20% of your weight," "Average weight loss in 1 year is 11–20% (vs ~2–3% with diet and exercise alone)"; member survey (n=1,243, ≥7 weeks): **87%** life-changing results, **93%** easier to incorporate, **97%** quieter food noise.
- **Clinical leadership:** CMO Dr. Melynda Barnes (triple board-certified); advisors page; "Former Surgeon General and Head of the DEA" cited among advisors; "100s of published studies." Provider/credential network surfaced via `/network-physician/*` and `/advisors/`.
- **Certification:** LegitScript-certified seal in footer.
- **Safety posture:** prominent GLP-1 boxed-warning language (thyroid tumors / MTC / MEN 2); explicit "compounded… not FDA-approved" disclaimers on Ro Sparks, Daily Rise Gummies, Ro Mane Spray; off-label disclosures (Ozempic, oral minoxidil, valacyclovir).

## Visual & brand impression

Clean, confident, mainstream-premium — not the edgy-bro aesthetic of early men's-health DTC. White canvas segmented into soft pastel photo blocks (peach/coral, lilac, cream, muted blue-grey), large lifestyle photography of real, diverse people, and uniform product tiles. Signature acid-chartreuse (#F8FFA1) accent bar up top; deep near-black footer. Proprietary "Ro Sans" typeface, generous spacing, minimal ornament. Reads as a trusted, broad-market consumer-health brand that has deliberately outgrown its niche origins.

## Strategic read

Most relevant comp signal for a men's-health-adjacent venture: Ro's durable advantage is **owning the stack** — its own pharmacy and at-home labs under ro.OS — which lets it market "lowest-cost GLP-1s" and absorb insurance friction (the concierge) as a feature, not a cost center. It runs its **own A/B experimentation engine** (`ro-experiments`), so its pricing, hero offers, and IA shift continuously (TrumpRx pricing, $20-off ED, promo bars) — any single capture is a snapshot. Pricing transparency (a public `/pricing/` page enumerating generics by dose) is itself a positioning weapon worth noting; many competitors gate everything behind intake.

## Provenance

- **Pages (fresh, `captures/2026-06-18/`):** homepage, /pricing/, /weight-loss/pricing/, /weight-loss/, /weight-loss/how-it-works/, /erectile-dysfunction/, /premature-ejaculation/, /hair-loss/, /dermatology/, /fertility/, /os/, /founder-letter/, /faq/ (13 pages); Firecrawl scrape, all formats on homepage; map (499 urls) for inventory. Prior captures (2026-06-01 base, 2026-06-03 weight-loss offerings, 2026-06-04 full set) archived under `captures/_archive/`.
- **Verify:** all 13 sourceURLs matched requested; all body md5s unique (no geo/cache contamination); no junk soft-404s.
- **Credits:** 14 (1 map + 13 scrapes), all basic proxy.
- **Couldn't get:** GLP-1 all-in cash cost (per-SKU starting prices ARE published now, but the all-in = membership + provider-titrated dose ladder; Wegovy pill/pen + Foundayo full ladders behind an unrendered expander); social handles (JSON-LD carries only a minimal Organization block — name/url/contactPoint, no `sameAs`); legal entity (no ©/legalName on captured pages); fertility / Upneeq / Saxenda pricing (intake-walled / FAQ-only / nav-only); Testosterone Support + enriching cream molecules (unnamed blends).
- **Run profile:** fresh re-capture (2026-06-18, Express via `/research-telehealth-brand ro.co`) — re-scraped the full profile page set + /premature-ejaculation/ + /faq/; refreshed `offerings.md` (all 8 lines) + `telehealth.md` in place. **The full roster + every captured price is unchanged vs the 2026-06-04 capture** — a stability-confirming re-capture, not a change event. Re-stamped profile 2.5→**2.6** (added `legal_entity`, empty — not site-derivable). Logos (wordmark/logomark/og) re-measured off the fresh homepage payload, all three slots unchanged (0 credits). +telehealth +logos +offerings modules.
- **Enriched (model knowledge):** "Roman" ↔ "Ro" rebrand/heritage relationship used for identity resolution only — Roman path (`/roman/`) is on-site. Founders (Reitano, Rahmanian, Schutz) are named on the captured `/founder-letter/` page; Modern Fertility / Rory→Custom Rx renames are on captured pages (`/fertility/`, `/dermatology/`) — not enriched.
