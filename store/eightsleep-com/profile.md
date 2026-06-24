---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: eightsleep.com
name: Eight Sleep
aliases: []
legal_entity: ""                     # site states only "© 2026 Eight Sleep"; no registered legal name (no JSON-LD legalName)
parent: []
owns: []
socials:
  youtube: https://www.youtube.com/@eight_sleep
  instagram: https://www.instagram.com/eightsleep
  x: https://www.x.com/eightsleep
external: {}                         # no third-party records on the site (no JSON-LD sameAs)

# Capture meta
captured_at: 2026-06-24
capture_method: firecrawl
site_notes: "Next.js on Vercel. Map is ~80% /blog content + many athlete/ambassador landing pages (/andy, /astonmartin, /efprocycling…) — pick pages from homepage + footer links, NOT the map. No /about page; company story + tech live on /why-eight-sleep and /science. All product PDPs sit under /product/<slug>; the Pod configurator, ALL hardware pricing, and the 3 Autopilot tiers are on /product/pod-cover. Decagon AI chat widget + Dstillery pixel present; no A/B tool fingerprinted, but a '4th July Sale' promo was live so captured prices are a sale snapshot (struck-through regular prices also captured)."
key_pages:
  pod_pdp: /product/pod-cover
  accessories: /accessories
  autopilot: /autopilot
  the_base: /product/the-base
  why_eight_sleep: /why-eight-sleep
  science: /science
  how_the_pod_works: /pod-cover
unverified_fields:
  - "Prices/IA are a point-in-time snapshot, not fixed — a '4th July Sale' (up to $500 off) was active; both sale and struck-through regular prices were captured."
  - "Pod 5 Ultra (the higher Cover variant) price not captured — the /product/pod-cover configurator rendered only the Pod 5 Core price ($2,749, Queen)."
  - "Hardware prices shown for Queen size only; Full / King / Cali King may differ (not rendered)."
  - "Funding, headcount, revenue not on the marketing site (deep-research, not capture)."

# Description — one sentence (~160-220 chars)
description: "Makes the Pod — a smart, dual-zone mattress cover that heats, cools, and tracks sleep and biometrics without a wearable — paired with a required Autopilot software subscription whose AI adjusts temperature and elevation automatically each night."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Physical Products / Hardware]   # smart-hardware maker; the bundled Autopilot software + supplements are companion lines, not co-primary (see body)
portfolio_shape: Flagship + companions
business_model: Subscription         # hardware sold one-time, but Autopilot is a MANDATORY recurring subscription (+ full rental option) — the defining recurring structure; see How it works
primary_industry: Technology         # self-styled "sleep technology" — AI, clinical-grade sensors, app, patented tech is the whole pitch; health/wellness positioning noted in body

# Visual identity — branding is a hint to verify; confirmed against the homepage screenshot
logo_url: https://res.cloudinary.com/eightsleep/image/upload/v1761171870/Logo_White_xwtn4w.svg
logos:
  wordmark: { src: "https://res.cloudinary.com/eightsleep/image/upload/v1761171870/Logo_White_xwtn4w.svg", w: 64, h: 27 }                      # white colorway (built for dark backgrounds), SVG viewBox 64x27
  logomark: { src: "https://www.google.com/s2/favicons?domain=eightsleep.com&sz=256", px: 180, transparent: false }                            # white geometric "8" cube mark on a baked near-black square
  og:       { src: "https://res.cloudinary.com/eightsleep/image/upload/c_fill,w_1200,h_630,f_jpg,q_auto/v1747147611/Homepage_c0dril.png", w: 1200, h: 630 }
brand_colors: { primary: "#1862FF", accent: "#E8EFFF" }   # branding-reported blue + pale-blue; site reads dark-premium with cool-blue accents (see Visual)
fonts: [Neue Montreal]
color_scheme: light                  # white structural base; heavy near-black feature bands (see Visual)
design_framework: next.js            # /_next/ paths in rawHtml (Vercel-hosted)
---

## Overview

Eight Sleep is a direct-to-consumer sleep-technology company built around **the Pod** — a smart mattress *cover* (not a mattress) that actively heats and cools each side of the bed between **55°F and 110°F**, tracks sleep and cardiovascular/respiratory biometrics with no wearable, and runs on **Autopilot**, an AI software layer that adjusts temperature and elevation through the night. The current generation is **Pod 5** (a Core and a higher **Pod 5 Ultra** variant). The Pod is the hero; everything else — a **Base**, **Blanket**, **Pillow Cover**, a **Premium Mattress**, sleep **supplements**, and bedding — extends it, and most "Require Pod." Founder Matteo Franceschetti is named on the site (a captured testimonial tweet). The brand frames itself as a "sleep fitness" movement, leaning hard on clinical validation and a sleep-science advisory board.

## What they offer

The Pod system + a required software membership; per-SKU detail (12+ companion SKUs) lives in `offerings.md`. Prices below are the **4th July Sale** snapshot, regular price struck where shown:

- **Pod 5 (the Cover):** flagship smart mattress cover — dual-zone cooling/heating 55–110°F, sleep & health tracking, tap-to-control, vibration/thermal alarms. **$2,749** (~~$2,999~~), Queen `[published]`. A higher **Pod 5 Ultra** adds automatic elevation/snore mitigation (price not captured).
- **Autopilot (membership):** the AI software that runs the Pod — **required for the first 12 months**, annual billing, covers two users per Pod. Three tiers: **Standard $199/yr** ($17/mo), **Enhanced $299/yr** ($25/mo, adds 5-yr warranty), **Elite $399/yr** ($33/mo, "New" — adds cardiovascular/respiratory Health Check). `[published]`
- **The Base:** adjustable base under the mattress — elevation, automatic snore mitigation, integrated speaker (Huberman NSDR, white noise). **$1,899** (~~$1,999~~) `[published]`
- **The Blanket:** hydro-powered duvet insert that doubles temperature coverage. **$949** (~~$999~~) `[published]`
- **Pod Pillow Cover:** cooling/heating cover for any pillow, on its own Hub. **$949** (~~$999~~) `[published]`
- **Premium Mattress:** breathable mattress to pair with the Cover. **$1,899** (~~$1,999~~) `[published]`
- **Supplements:** **Sleep Elixir** & **Sleep Elixir Plus** (daily sleep supplements; Plus adds melatonin) **$59** (subscribe; ~~$79~~) each; **Jet Lag** supplement **$99** `[published]`
- **Bedding & accessories:** Air Pillow **$199**, Pod Sheet Set **$189**, Duvet Cover **$199**, Pod Protector **$119**, Sleep Essentials Bundle **$415** (bundle saves $200) `[published]`
- **Rent the Pod:** flat monthly rental of a Pod 5 Core/Ultra + Autopilot, cancel anytime — **from $169/mo** `[published]`

## How it works / model

A **one-time hardware purchase + a mandatory recurring software subscription**, the defining commercial structure: you buy the Pod, but Autopilot is required for the first 12 months (cancel after) and is what makes the device "intelligent." A full **rental** path (from $169/mo, Pod + Autopilot, no commitment) is the pure-subscription alternative. Sold DTC from its own site; ships to the US + ~30 countries (Canada, EU, UK, UAE, Australia, etc.). Purchase support: **30-night risk-free trial**, free shipping & returns, **2-year warranty** (extended to **5 years** on Enhanced/Elite), **HSA/FSA-eligible**, and financing via **Affirm** (0% APR, up to 36 months, "as low as $77/mo") and **Klarna**.

## Positioning & audience

A **premium, performance/health-optimization** positioning — "sleep fitness," "your edge" — aimed at consumers who treat sleep as a trainable health metric: athletes, founders/executives, biohackers, couples (dual-zone), hot sleepers, and menopausal women (a dedicated "Women's Health" / hot-flash angle). It positions the Pod not against other smart mattresses but against **ordinary sleep aids** — the `/science` page runs a comparison table of *the Pod vs melatonin vs prescription sleep medicine vs wearables*. Claimed edge: clinical-grade, wearable-free tracking + AI auto-adjustment + clinical validation, trending toward a preventive-health "health tool."

## Nav structure

Slim top nav; full taxonomy is the footer:

```
- How the Pod works — /pod-cover
- Accessories — /accessories
- Reviews — /wall-of-love
- Shop the Pod — /product/pod-cover
- Blog
  - Sleep — /blog/sleep   · Fitness — /blog/fitness   · Wellness — /blog/wellness   · Science — /blog/science
- Company
  - Careers — /careers   · Press — /press   · Athletes — /athletes
  - Women's Health — /hot-flash   · Our Research — /science   · Sleep Accessories — /accessories
- Support
  - Member Login   · Sleep Elixir Login — /sleep-elixir-management   · FAQ — help.eightsleep.com
  - Speak with a specialist — /speak-with-a-specialist   · Autopilot — /autopilot
  - Warranty — /warranty   · Return Policy — /return-policy   · Accessibility — /accessibility
- Legal
  - Financing Policy — /financing   · Privacy — /legal/privacy   · Sale Terms — /terms-and-conditions
  - Consumer Health Data Privacy — /legal/consumer-health-data-privacy-policy   · IP — /intellectual-property   · Trade-In — /tradein-terms
```

## Credibility & proof

Heavy clinical/scientific framing; all self-reported unless noted:
- **Ratings:** "(4.5 stars) • 30,215 reviews" on the Pod PDP; a "Loved by millions" review wall (self-reported).
- **Clinical-outcome claims (verbatim, self-reported):** "Up to 44% less time to fall asleep," "Up to 34% more deep sleep," "Up to 45% reduction in snoring," "Up to 23% fewer night wake ups."
- **Tracking accuracy:** "HR is 99% accurate compared to the gold standard (ECG)"; "RR is 98% accurate compared to gold standard (respiratory inductance plethysmography)."
- **Scale claims:** "supported by over 50 clinical studies"; "600M+ hours of sleep analyzed"; "14 patented technologies"; "1 billion hours of sleep data" (Autopilot); "over 5,000 nights of data" (algorithm testing).
- **Scientific Advisory Board:** Andrew Huberman, Ph.D. (Stanford; Huberman Lab podcast) and Matthew Walker, Ph.D. (UC Berkeley; *Why We Sleep*).
- **Named endorsers (testimonial wall):** Elon Musk, Mark Zuckerberg, Paul Graham, Bryan Johnson, Joe Rogan, Charles Leclerc, Peyton Stearns.
- **Disclaimer (verbatim):** Health Check "is not intended to diagnose, treat, cure, or prevent any disease. This is not a medical device" — they explicitly disclaim medical-device status.

## Visual & brand impression

A polished, premium, photography-led aesthetic. The structural base is **light** (white background, light-gray product/review cards, generous whitespace), but the brand's emotional register is **dark and cinematic** — large near-black feature bands with moody bedroom photography, a cool-blue accent (#1862FF), and a clean geometric sans (**Neue Montreal**). The logomark is a confident geometric "8" cube; the wordmark ships in a white colorway for the dark sections. Design maturity is high — it reads like a well-funded consumer-tech flagship (Apple/Whoop adjacent), not a bedding brand. Motifs: dual-zone red/blue temperature dots, app/data screenshots, clinical-grade framing.

## Strategic read

The interesting move is the **deliberate march from hardware to recurring health platform**. Autopilot is mandatory (no Pod without a subscription), and the new **Elite** tier reframes the bed as a *preventive-health device* — "your bed becomes a health tool… they want it to help them live longer" — with cardiovascular/respiratory monitoring and a "Health Check" early-warning feature, all while disclaiming medical-device status. Rental (from $169/mo) lowers the entry barrier and further subscription-izes a big-ticket device. The social-proof strategy is unusually founder/celebrity-led (Musk, Zuckerberg, Graham, Rogan) layered over genuine sleep-science credentials (Huberman, Walker).

## Provenance

- **Pages** (8 analyzed, Firecrawl, 2026-06-24): homepage, `/product/pod-cover` (rich), `/accessories` (rich), `/autopilot`, `/product/the-base`, `/why-eight-sleep`, `/science`, `/pod-cover`. Map + footer links drove selection.
- **Verify:** all 8 sourceURLs matched, all bodies md5-unique, no junk soft-404s.
- **Credits:** 9 (1 map + 8 scrapes).
- **Couldn't get:** Pod 5 Ultra price (configurator showed only Core/Queen); non-Queen sizes; funding/headcount/revenue (not on a marketing site).
- **Run profile:** guided — +offerings.md (per-SKU roster). No emphasis; no hero images.
