---
schema_version: 1

# Identity
domain: eden.health
name: Eden
aliases: [tryeden.com, www.tryeden.com]   # rebrand/migration: tryeden.com → www.eden.health (301 chain verified 2026-05-30, the day of migration). eden.health is now canonical; tryeden.com still 301-resolves.
parent: []
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "DOMAIN MIGRATED 2026-05-30 (capture day): tryeden.com → www.tryeden.com → www.eden.health (all HTTP 301; eden.health now canonical). NB store folder is `eden-health` (canonical key), NOT the brief's `tryeden-com` — keyed on the resolved domain per AG1 precedent. Some legacy mega-nav 'Get Started' deep-links still point to www.tryeden.com/intake/* (mixed-migration remnant; old host 301-resolves so capture works either way). Webflow site (cdn.prod.website-files.com asset host; rawHtml has data-wf-* + website-files.com; branding.designSystem.framework='custom' is WRONG per §5.4 — it's Webflow). Mega-nav + footer DO render inside the markdown (Webflow hangs them in <main>) — unlike the Next.js DTC sites where nav is client-rendered/absent. firecrawl-only. Rotating top-bar promo ('Up to $80 off your first order' / '$80 off your first GLP-1 Treatment Plan' / 'Free expedited shipping'). H1 is a rotating vertical-flip carousel (Health/Weight Loss/Muscle growth/Anti-aging/Hormones/Mental health/Hair regrowth) — Firecrawl snapshot timing can catch a half-rendered chip ('Healt'), a render artifact, not signal. Per-treatment pricing IS in the markdown as 'From/Starting at $X first month' anchors; full per-tier tables render on the PDPs. /v2/map at limit:500 returns ~485–496 URLs dominated by /post/* blog; the /treatment/* catalog is best extracted from homepage links (it was, here). No §5.1 geo/cache contamination this run (all 6 bodies unique, all sourceURLs matched) with maxAge:0 + location:US + waitFor:4000 + serialized."
key_pages:
  weight_loss: /weight-loss                              # flagship vertical
  glp1_treatments: /treatment/glp-1-treatments           # flagship compounded-GLP-1 PDP + pricing
  hormone_kit_women: /treatment/hormone-kit-for-women     # women's hormone therapy (mixed-gender catalog)
  cell_theory: /treatment/cell-theory                    # Eden's own-label non-Rx supplement
  about: /about                                          # founders + 503A pharmacy network
  faq: /frequently-asked-questions
  safety_info: /safety-info
  partner: /partner-with-eden                            # B2B2C partner motion
  calculators: /calculators/bmi                          # free BMI/BMR/TDEE/calorie/protein/carb tools
  intake: https://app.eden.health/intake/weightloss/welcome   # signup funnel (subdomain)
unverified_fields:
  - "Branded GLP-1 pricing (Ozempic®/Wegovy®/Zepbound®/Mounjaro®) — listed as SKUs in nav but no price on category pages; revealed inside the /intake quiz, not submitted."
  - "Per-tier pricing for several SKUs (Methylene Blue, Glutathione, GHK-Cu, men's hair) not walked this run (key-page cap)."
  - "'127,000+ members' claim — homepage, no methodology stated. Per prior weekly snapshots this number has been flat across 7 consecutive captures (2026-05-12 → 05-30) — likely a frozen marketing figure, not a live count."
  - "Headcount / revenue / funding / ownership — not on the marketing site (deep-research job, not capture)."

# Description — one sentence
description: "A DTC telehealth brand delivering compounded and branded prescription treatments — GLP-1 weight loss, NAD+/longevity, hormone therapy, hair, sexual health, and mood — to consumers in all 50 states via licensed clinicians and a network of 503A compounding pharmacies, on flexible monthly subscriptions."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]                 # primary DTC; also runs a B2B2C "Partner with Eden" program (kept in body for cohort consistency — see FINDINGS)
offering_category: [Services / Consulting, Biotech / Pharma Products]   # telehealth = clinician service + the (compounded) Rx drugs — the SCHEMA's canonical hybrid
portfolio_shape: Multi-product       # multi-vertical Rx catalog (weight loss / longevity / hormones / hair / sexual / mood) — distinct, separately-bought lines
business_model: Subscription         # monthly autorenew treatment plans (3-mo / monthly cadences); one-time not the default
primary_industry: Healthcare & Life Sciences

# Visual identity — lifted from Firecrawl `branding` (homepage), confirmed against screenshot
logo_url: https://cdn.prod.website-files.com/676eb86a8ca7187507487da6/678a7c93763d80c5ef6ea922_edn-favicon.png   # hostable favicon proxy; the actual wordmark (branding.images.logo) is an inline data-URI SVG, a near-black (#1D1D1F) lowercase "edn" mark — too long for frontmatter
brand_colors: { primary: "#4EEAFF", accent: "#E60C00", secondary: "#B2CBD0", background: "#F9F9FA", text: "#49494B" }   # copied from branding.colors. Screenshot read: the page is overwhelmingly light/near-white with a near-black wordmark; #4EEAFF (cyan) appears as a soft accent, #E60C00 (red) is the link/CTA color. No single dominant brand hue — clean/neutral palette (see Visual & brand impression).
fonts: [Satoshi Variable, Arial]     # branding.fonts: Satoshi=brand, Arial=fallback
color_scheme: light                  # branding.colorScheme + screenshot (white canvas)
design_framework: webflow            # rawHtml data-wf-* + cdn.prod.website-files.com. branding.designSystem said "custom" — wrong (§5.4).
---

## Overview

Eden is a direct-to-consumer telehealth brand offering a broad, multi-vertical catalog of prescription (mostly **compounded**) treatments delivered 100% online. Its acquisition wedge is **GLP-1 weight loss** (compounded semaglutide/tirzepatide + branded Ozempic®/Wegovy®/Zepbound®/Mounjaro®), but the catalog spans **anti-aging/longevity** (NAD+ in three delivery forms, glutathione, methylene blue, and Eden's own non-Rx "Cell Theory" NAD+ supplement), **hormone therapy for women**, **hair growth** (men *and* women), **strength/performance** (sermorelin), **sexual function** (vardenafil + tadalafil), and **mood** (MIC+B12). Treatment plans are monthly subscriptions; the brand leans on "no surprises, upfront pricing," FSA/HSA eligibility, same-day visits, and US compounding. Migrated its primary domain from `tryeden.com` to **`eden.health`** on the capture day (2026-05-30).

## What they offer

A wide multi-vertical Rx catalog organized by goal (a future `offerings.md` would list these breadth-first):

- **Weight Loss** — `/treatment/glp-1-treatments` (flagship). Compounded **Semaglutide** "$129 first month / $209/mo after" (3-month plan, Best Value) or "$149 first / $229/mo after" (monthly); compounded **Tirzepatide** "$249 first / $329/mo after". Plus branded **Ozempic® / Wegovy® / Zepbound® / Mounjaro®** (gateway funnel, pricing in intake) and a **Custom Weight Loss Kit**. "Same Price at Every Dose" guarantee; Klarna/Afterpay.
- **Anti-Aging / Longevity** — **NAD+** Injections ("From $145 first month"), Nasal Spray, Face Cream; **Glutathione**; **Methylene Blue**; **Cell Theory™** — Eden's first own-label, **non-prescription** "Triple Action NAD+" supplement, "$25 first month / then $75/mo."
- **Hormone Therapy (women)** — `/treatment/hormone-kit-for-women` ("My Custom Hormone Kit"): **Balance** $79→$99/mo, **Ignite** $129→$149/mo, **Radiance** $179→$199/mo.
- **Hair Growth** — men *and* women: Finasteride, Minoxidil, GHK-Cu, Custom Hair Growth Kit ("As low as $83/mo").
- **Strength** — Sermorelin Injections ("From $126 first month") / Tablets; **Vardenafil + Tadalafil** (sexual function).
- **Mood** — MIC+B12 ("As low as $106/mo"), Methylene Blue.

**`portfolio_shape: Multi-product` — unambiguous.** Unlike AG1's `Flagship + companions` edge case, Eden is a genuinely multi-vertical telehealth catalog: weight loss, longevity, hormones, hair, sexual health, and mood are each distinct, separately-bought programs with their own pages and pricing. **Notable catalog asymmetry: men's hair yes, but no men's TRT** — Eden sells women's hormone therapy and men's/women's hair, but no men's testosterone vertical (a real gap vs. the men's-health-anchored cohort peers).

## How it works / model

Self-serve DTC telehealth, **subscription-first**. Journey: land (heavy paid funnel — `/mailers`, `/tv`, `/multitouch`, `/weight-loss-quiz` slugs in the map) → pick a treatment → **online intake/eligibility quiz** on `app.eden.health` → clinician review + same-day prescription → recurring monthly shipment from a partner pharmacy. Money is made on **recurring treatment-plan subscriptions** (3-month and monthly cadences, autorenew), with a first-month discount as the standard hook ("Up to $80 off your first order").

## Positioning & audience

- **Who:** broad B2C health-and-wellness consumers, weight-loss-led; women's-hormone and longevity audiences are explicit secondary targets.
- **Against:** the men's-health/longevity telehealth cohort (Hims, Hone, PeterMD, Healthspan) and GLP-1 players — competing on **catalog breadth + upfront pricing + speed** ("Same-day doctor visits & prescriptions," "No surprises, upfront pricing").
- **Claimed edge:** personalization ("tailored to you"), 50-state coverage via a multi-pharmacy network, FSA/HSA eligibility on all plans, and a "Same Price at Every Dose" GLP-1 guarantee.

## Nav structure

Webflow mega-nav (renders *inside* the markdown, unlike the Next.js peers). Five goal-based treatment categories + More + Get Started:

```
- Weight Loss
  - GLP-1 Treatments ᴿˣ — /treatment/glp-1-treatments
  - Custom Weight Loss Kit ᴿˣ — /treatment/custom-weight-loss-kits
  - Ozempic® / Zepbound® / Wegovy® / Mounjaro® ᴿˣ — /treatment/{ozempic,zepbound,wegovy,mounjaro}
- Strength
  - Sermorelin Injections ᴿˣ — /treatment/sermorelin  ·  Sermorelin Tablets — /treatment/sermorelin-odt
  - Vardenafil + Tadalafil ᴿˣ — /treatment/vardenafil-tadalafil
- Anti-Aging
  - NAD+ Injections — /treatment/nad  ·  NAD+ Nasal Spray — /treatment/nad-nasal-spray  ·  NAD+ Face Cream — /treatment/nad-facial-cream
  - Glutathione ᴿˣ — /treatment/glutathione  ·  Cell Theory™ NAD+ Supplement (non-Rx) — /treatment/cell-theory
- Hair Growth
  - Men: Finasteride / Minoxidil / GHK-Cu / Custom Hair Growth Kit — /treatment/*-for-men
  - Women: Minoxidil / GHK-Cu / Custom Hair Growth Kit — /treatment/*-for-women
- Improved Mood
  - MIC+B12 ᴿˣ — /treatment/mic-b12  ·  Methylene Blue ᴿˣ — /treatment/methylene-blue
- Hormone Therapy (women) — /treatment/hormone-kit-for-women
- Health Calculators — /calculators/{bmi,bmr,tdee,calorie,protein,carbs}
- Discover Eden: Eden Health Clubs (edenhealthclubs.com) · About · Blog · Reviews
- Get Started → app.eden.health/intake/weightloss/welcome
```

## Credibility & proof

- **Scale claim:** "127,000+ members" (homepage; flat across 7 prior weekly captures — treat as a frozen marketing figure, see `unverified_fields`).
- **Outcome claim (verbatim, footnoted):** "*Eden members reported an average weight loss of 29.3 lbs in the first six months based on self reported data from 111 members while on GLP-1 injections, combined with diet and exercise."
- **Trust strip:** "No surprises, upfront pricing," "100% entirely online," "FSA & HSA eligible," "FDA-registered labs," "24/7 provider messaging," "Same-day doctor visits & prescriptions," "Compounded in the USA."
- **Pharmacy / regulatory:** "Quality-audited & US-licensed **503A pharmacies**" — named network **GoGoMeds, Precision, Enovex, AbsolutePharmacy**, **PCAB**-accredited, serving all 50 states + DC. Washington-state **My Health My Data** privacy page (`/policies/my-health-my-data-privacy-policy`).
- **No named celebrity MD on the homepage** — "leading medical experts" framing + named cofounders/VP of Pharmacy Operations on `/about`.

## Visual & brand impression

High-maturity, clean **light-mode** DTC aesthetic on a near-white canvas (#F9F9FA) with a near-black lowercase "edn" wordmark, soft rounded product cards, and warm lifestyle photography (multi-ethnic models, product-in-hand shots). The palette is deliberately **neutral** — there's no single dominant brand hue; `branding.colors` reports a cyan `#4EEAFF` accent and a red `#E60C00` link/CTA color, with green/peach/cream product-tile imagery providing most of the on-page color. Reads as approachable-clinical and product-forward (a "harmony of science and nature" section motif), not sterile. Satoshi (a modern geometric grotesk) is the brand type.

## Strategic read

Eden is the **breadth play** in the telehealth cohort — the widest Rx catalog of the six, spanning weight loss, longevity, hormones, hair, sexual health, and mood, anchored on compounded GLP-1s as the acquisition wedge and cross-selling into longevity/hormones. The durable state worth recording: a 50-state, subscription-first, **multi-pharmacy-network** compounder competing on catalog breadth + upfront pricing + speed, with a heavy paid/affiliate acquisition machine and an emerging own-label supplement line (Cell Theory) that mirrors AG1's move from service into branded product. Two things to watch: the **domain migration to eden.health** (capture-day, still settling — mixed-migration intake links remain), and the **men's-TRT gap** (conspicuous in a cohort where TRT is table stakes for Hone/PeterMD). The plural-pharmacy-network framing (vs. first-party ownership) persists despite a reported 2025 Contigo Compounding acquisition — a positioning choice, not surfaced on-site.

## Provenance

- **Pages analyzed (all Firecrawl `/v2/scrape`, 2026-05-30, via canonical eden.health):** homepage (`/`, rich pass: markdown + html + rawHtml + links + branding + images + full-page screenshot), `/weight-loss`, `/treatment/glp-1-treatments`, `/treatment/hormone-kit-for-women`, `/treatment/cell-theory`, `/about` — each markdown + links + full-page screenshot. Site inventory via `/v2/map` (limit 500).
- **Capture mechanics:** `maxAge:0` + `location:{country:US}` + `waitFor:4000` + serialized; all 6 bodies unique + all sourceURLs matched (no §5.1 contamination). **7 credits** (1 map + 6 scrapes), clean run.
- **Raw payloads + screenshots:** `captures/2026-05-30/.payloads/`; cleaned page markdown: `captures/2026-05-30/*.md`.
- **Couldn't get:** branded-GLP-1 and several per-tier prices (behind the intake quiz); membership-count methodology. See `unverified_fields`.
