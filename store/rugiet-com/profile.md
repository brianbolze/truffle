---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: rugiet.com
name: Rugiet
aliases: [www.rugiet.com, rugiethealth.com, "Rugiet Health"]   # rugiethealth.com 301s to www.rugiet.com; "Rugiet Health" appears in funnel/medical-assessment copy
legal_entity: ""                     # no site-derived legalName / legal entity found in homepage JSON-LD or captured footer copy
parent: []                           # no parent shown; Rugiet operates independently on this site
owns: []
socials: { instagram: "https://www.instagram.com/rugiethealth/", facebook: "https://www.facebook.com/rugiethealth/", linkedin: "https://www.linkedin.com/company/rugiethealth/", x: "https://x.com/RugietHealth", tiktok: "https://www.tiktok.com/@rugiethealth" }   # footer anchors
external: { trustpilot: "https://www.trustpilot.com/review/rugiet.com?utm_medium=trustbox&utm_source=MicroStar" }   # linked Trustpilot widget/profile in captured Ready lander

# Capture meta
captured_at: 2026-06-21
capture_method: firecrawl
site_notes: "Next.js on Vercel, Sanity CMS for content/images (cdn.sanity.io). Marketing/catalog on www.rugiet.com; commerce/intake on start.rugiet.com. Current indexed catalog = Sex, Testosterone, Sleep, Longevity, Weight; Hair folds into Grower. ALL commerce still starts behind the quiz funnel. Public prices: Ready via /bm/n1/shopping ($139 one-time, $79/mo subscription) plus /trimix dose ladder ($10/dose floor; $14/$17/$20/$24 by strength), and TRT via $69 initial labs + $139/month. Go Long, Daily Boost, Grower, Recharge, Weigh In, and all Longevity SKUs show no Rugiet-specific public price. `/trimix` is a Ready SEM lander, not a Trimix product. BM/N1 paths are Ready paid/shopping landers. Page title strings can include injected zero-width unicode; body text is usable. The vertical wordmark remains store/rugiet-com/assets/wordmark.svg; logomark is a baked black square."
key_pages:
  all_treatments: /all-treatments
  sex: /sex
  testosterone: /testosterone
  longevity: /longevity
  science: /science
  reviews: /reviews
  ed_ready: /erectile-dysfunction/ready
  pe_go_long: /premature-ejaculation/go-long
  ed_daily_boost: /erectile-dysfunction/boost
  ed_grower: /erectile-dysfunction/grower
  trt_enclomiphene: /testosterone/enclomiphene
  trt_injectable: /testosterone/injectable-trt
  trt_topical: /testosterone/topical-trt
  trt_oral: /testosterone/oral-trt
  sleep_recharge: /sleep/recharge
  weight_weigh_in: /weight-loss/weigh-in
  longevity_nad: /longevity/nad
  longevity_sermorelin: /longevity/sermorelin
  longevity_l_carnitine: /longevity/l-carnitine
  longevity_lipo_c: /longevity/lipo-c
  longevity_glutathione: /longevity/glutathione
unverified_fields:
  - "Per-product all-in pricing for Go Long, Daily Boost, Grower, Recharge, Weigh In, and all Longevity SKUs — gated behind start.rugiet.com intake; public pages and captured landers do not show Rugiet-specific prices."
  - "Pharmacy partner identity + 503A/503B compounding lane — site says U.S. licensed / FDA-regulated pharmacies but names no pharmacy entity and states no lane."
  - "Legal entity, founders, founding date, headcount, funding — not on captured marketing pages."
  - "Display typeface — branding exposes only an obfuscated alias; the condensed grotesque is screenshot-read, not named."
  - "Self-reported scale is point-in-time marketing copy: 500k+ men on current homepage/reviews, 400k+ men on the /trimix SEM lander, and 10 million doses delivered on /sex."

description: "A DTC men's performance-medicine telehealth brand that connects men to licensed clinicians for mostly compounded prescription treatments across sex, testosterone, sleep, longevity, weight, and hair."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # clinician telehealth + prescription/compounded pharma
portfolio_shape: Multi-product       # 15 buyable SKUs across five current lines, ED-flagship-led
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 98, h: 416 }                                                            # vertical RUGIET lockup extracted in the prior run; remeasured this run
  logomark: { src: "https://www.rugiet.com/IMGS/favicons/R.png", px: 1080, transparent: false }                   # white R/up-arrow on baked black square
  og:       { src: "https://cdn.sanity.io/images/hgt43vn7/production/466d4e394a6f1c586f6b1cab5dd081c6857b3c7d-1333x951.png?rect=0,126,1333,700&w=1200&h=630&fm=jpg&q=75&fit=max&auto=format", w: 1200, h: 630 }
brand_colors: { primary: "#FFA200", accent: "#32C9B7", text: "#292524" }  # amber-orange is the signature hue; teal is secondary/link accent; CTAs are black
fonts: []                            # no site-stated typeface name; leave empty over guessing
color_scheme: light
design_framework: next.js            # rawHtml: Next/Vercel assets; Sanity CMS image/content backend
---

## Overview

Rugiet is a DTC men's **"performance medicine"** telehealth brand. It connects men to licensed clinicians for prescription treatments across sexual performance, testosterone, sleep, longevity, weight, and hair, with most catalog items fulfilled as compounded formulations through U.S. pharmacies after an online intake. The wedge remains **Ready**, a 3-in-1 sublingual ED troche combining sildenafil, tadalafil, and apomorphine; the major current delta is a new **Longevity** line with NAD+, Sermorelin, L-Carnitine, Lipo-C, and Glutathione.

## What they offer

Five current lines, all routed through the intake funnel. Per-SKU detail lives in `offerings.md`.

- **Sexual Performance:** Ready, Go Long, Daily Boost, and Grower. Ready has public prices (`$139` one-time / `$79/mo` subscription on `/bm/n1/shopping`, plus a `$10/dose` floor and `$14/$17/$20/$24` dose ladder on `/trimix`); the other sexual-performance SKUs are intake-gated `[partial]`.
- **Testosterone:** Enclomiphene, Injectable TRT, Topical TRT, and Oral TRT, sold behind a `$69` initial lab/evaluation and plans starting at `$139/month`; pages describe flat/all-inclusive pricing and ongoing lab monitoring `[published]`.
- **Sleep:** Recharge, a 3-in-1 sleep Rx combining ramelteon, doxylamine, and valerian root; no public Rugiet-specific price found `[on-request]`.
- **Longevity:** NAD+, Sermorelin, L-Carnitine, Lipo-C, and Glutathione; the hub/product pages show forms and access, while the cost article stays comparative/general rather than publishing Rugiet prices `[on-request]`.
- **Weight / Hair:** Weigh In is a non-GLP-1 oral metabolic stack; Hair is not a standalone line, it routes to Grower (ED + hair). Both are intake-gated `[on-request]`.

## How it works / model

Customer path: choose a treatment, complete the online questionnaire on `start.rugiet.com`, get clinician review, then receive medication by mail if prescribed. TRT starts with a **$69** lab/evaluation and video call; current TRT pages state monitoring, medication, and labs are included once treatment starts. Controlled-substance pages state a live audio-video consultation requirement; non-controlled pages still require an online provider consultation. Revenue is subscription/refill medication plus bundled clinical oversight.

## Positioning & audience

Targets men only: "Performance Medicine For Men." The brand frames itself as a premium alternative to generic, single-ingredient pills and clinic visits: faster onset, multi-drug formulations, online access, and discreet delivery. ED/Ready is still the front door, but the catalog now stretches into a broader men's optimization stack: TRT, sleep, metabolic health, and longevity injectables/sprays.

## Nav structure

Top nav now exposes Longevity; the footer still omits it and keeps Hair as a link to Grower.

```
- All Treatments — /all-treatments
- Sex — /sex
  - Ready — /erectile-dysfunction/ready
  - Go Long — /premature-ejaculation/go-long
  - Daily Boost — /erectile-dysfunction/boost
  - Grower — /erectile-dysfunction/grower
- Testosterone — /testosterone
  - Enclomiphene — /testosterone/enclomiphene
  - Injectable TRT — /testosterone/injectable-trt
  - Topical TRT — /testosterone/topical-trt
  - Oral TRT — /testosterone/oral-trt  (attested from current PDP recommendation links)
- Sleep — /sleep/recharge
- Longevity — /longevity
  - NAD+ — /longevity/nad
  - Sermorelin — /longevity/sermorelin
  - L-Carnitine — /longevity/l-carnitine
  - Lipo-C — /longevity/lipo-c
  - Glutathione — /longevity/glutathione
- Weight — /weight-loss/weigh-in
- Hair — /erectile-dysfunction/grower
- Science — /science · Reviews — /reviews · Sex Score — /sex-score · Log in — start.rugiet.com
```

## Credibility & proof

- **LegitScript Certified** and **HIPAA Compliant** badges appear in the footer across captured pages.
- **Trustpilot:** captured widget copy says **"Rated Excellent. 4.3 out of 5 on Trustpilot"** and links to Rugiet's Trustpilot profile.
- **Self-reported scale:** current homepage/reviews say **"500k+ men choose Rugiet"**; /sex says **"Over 10 million doses delivered"**; /trimix still says **"Over 400k men choose Rugiet"**, so treat these as marketing claims with capture-date drift.
- **Medical advisory board:** homepage names board-certified physicians Justin Houman, MD; Nicholas Farber, MD; Vipul Khanpara, MD; Asim Roy, MD; and Andrew Y. Sun, MD.
- **Clinical/compliance caveat:** compounded SKUs carry a "compounded drugs are not approved by FDA" disclaimer; controlled-substance pages carry live audio-video consultation disclaimers.

## Visual & brand impression

Rugiet still reads like a men's-lifestyle magazine rather than a clinic: high-contrast editorial photography, boxing/couple/body imagery, dense black sections, amber-orange brand fields, and hard-edged black CTAs. The wordmark is unusually vertical, while the square mark is a stark white R/up-arrow on black. The new Longevity pages keep the same visual system but lean into product-vial renders and athletic recovery imagery.

## Strategic read

The catalog has broadened from men's sexual performance plus TRT into a full optimization stack. Ready remains the commercial spearhead and the only non-TRT SKU with public pricing; the new Longevity line is a second compounding-heavy expansion surface, with five injectable/spray therapies but no public Rugiet-specific prices. The two pricing exceptions are instructive: Ready uses SEM/shopping landers to expose an entry price, while TRT uses flat all-inclusive pricing as the trust hook. Everything else is still a quiz-gated conversion funnel.

## Provenance

- **Pages:** homepage (+ rawHtml/branding/screenshot), /all-treatments (--homepage), /sex (--homepage), /testosterone (--homepage), /longevity (--homepage), /science, /reviews, 15 buyable PDPs (Ready, Go Long, Daily Boost, Grower, Enclomiphene, Injectable TRT, Topical TRT, Oral TRT, Recharge, Weigh In, NAD+, Sermorelin, L-Carnitine, Lipo-C, Glutathione), Ready price/SEM paths (/trimix, /bm/n1, /bm/n1/shopping), Go Long / Daily Boost / Recharge landers, and two cost articles (/blog/longevity-therapy-cost, /blog/how-much-does-trt-cost-online) — **31 scrapes + map** via Firecrawl (`fc.py`, `maxAge:0`, `location:US`).
- **Verify:** all 31 sourceURLs matched, all bodies md5-unique, no junk soft-404s.
- **Credits:** 32 (1 map + 31 scrapes), manifest-attributed.
- **Couldn't get:** quiz-gated all-in pricing for non-Ready/non-TRT SKUs; pharmacy partner identity / 503A-503B lane; legal entity / founders / funding.
- **Structured layer (schema 2.6):** homepage JSON-LD is an `OnlineStore` block with name/url/description/logo/image, but no legalName or sameAs. `legal_entity` left empty; socials filled from footer anchors; Trustpilot external profile filled from captured widget link. `logos` remeasured this run: wordmark 98x416, logomark 1080px baked black square, og 1200x630.
- **Run profile:** Express recapture — refreshed `profile.md` + `offerings.md`; added Longevity to the catalog; retained logos module because it already existed and the new homepage exposes a qualifying og image.
