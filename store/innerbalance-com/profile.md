---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: innerbalance.com
name: Inner Balance
aliases: []
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/innerbalancemd/
  facebook: https://www.facebook.com/Inner-Balance-61556388119053
  youtube: https://www.youtube.com/channel/UCc-UcYfw7zzBqGrLgG8NdlA
  tiktok: https://www.tiktok.com/@sarahdaccarettmd     # founder's handle (@sarahdaccarettmd), used as the brand's TikTok in the footer
external: {}                          # no JSON-LD sameAs; no crunchbase/wikipedia surfaced on captured pages

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Next.js marketing frontend (`/_next/` ×211, no __NEXT_DATA__ but next/image proxy everywhere); the `/p/` section (blog `/p/learn`, `/p/treatment/*`, `/p/faq`, `/p/about-us`) is WordPress-backed (assets under `/p/wp-content/`). A/B: Optimizely — every scrape's TAIL carries an ad-blocked Optimizely block-page artifact (`a4692478322802688.cdn.optimizely.com is blocked … ERR_BLOCKED_BY_CLIENT`); strip it as noise. No JSON-LD on homepage. Prices live ON the product pages as published 'From $X/mo' floors (Oestra full tier on /p/treatment/hrt; skincare plan tiers on /pqp/anti-aging-face-cream); exact dose/checkout behind each per-product `/quiz/<x>` intake. Map (385 urls) is swamped by `/p/learn` SEO + dozens of `/p/learn/*-review` and `inner-balance-vs-*` competitor-comparison pages — select from homepage links/nav, not the map. Canonical host is www.innerbalance.com (apex 200s fine)."
key_pages:
  hrt: /p/treatment/hrt
  nad: /p/longevity/nad
  libida: /p/sexual-wellness/libida
  skincare: /pqp/anti-aging-face-cream
  about: /p/about-us
  science: /science
  faq: /p/faq
  reviews: /reviews
unverified_fields:
  - "Per-SKU checkout pricing + exact dose tiers — behind each /quiz/<x> intake; only published 'From $X/mo' floors captured."
  - "Pharmacy lane: pages predominantly say 503A (NABP/PCAB/LegitScript), but one Oestra FAQ says '503B FDA-regulated' — page-attested discrepancy, not resolved."
  - "Prices/promos are a point-in-time snapshot, not fixed — Optimizely A/B + rotating promo badges (20%/15% off)."
  - "Founding year — a patient testimonial cites being a customer 'since 2023'; no official founding date stated."

description: "A women's-health telehealth brand delivering prescription bioidentical-hormone, libido, longevity (NAD+), and anti-aging-skincare treatments — a licensed clinician reviews an online quiz, then a U.S. compounding pharmacy ships each compounded formula to the patient."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Flagship + companions    # Oestra is the hero ("Bestseller", brand-namesake quiz); NAD+/Libida/BodyMatched are companions
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg        # 2.5: canonicalized to the wordmark — the inline "Inner Balance" logotype SVG (branding.images.logo, decoded from its data-URI). Favicon fallback was https://www.innerbalance.com/favicon.ico
logos:                               # 2.5 module (+logos this run); each slot = what was found + ITS measurements (consumer applies the bar)
  wordmark: { src: assets/wordmark.svg, w: 183, h: 24 }                                                                # horizontal "Inner Balance" logotype, periwinkle #5472CC, committed text SVG; viewBox 0 0 183 24 (~7.6:1)
  logomark: { src: "https://www.google.com/s2/favicons?domain=innerbalance.com&sz=256", px: 256, transparent: false }  # stacked "Inner Balance" mark on a baked white square — renders as a white box on a dark slide (s2 256px; no separate symbol mark exists)
  # og slot omitted — no og:image declared on the homepage (true absence)
brand_colors: { primary: "#5472CC", text: "#09090B" }   # periwinkle-blue brand hue (logo + "Balance" highlight) on white/cream; near-black body text
fonts: [Suisse BP]                   # branding.fonts[0] = "suisseBP" (role unknown — verify; the only declared family)
color_scheme: light
design_framework: next.js            # rawHtml: next/image proxy ×211, no __NEXT_DATA__/gatsby/wp/shopify markers in the shell (the /p/ content subpath is separately WordPress)
---

## Overview

Inner Balance is a physician-founded, direct-to-consumer **women's hormonal-health telehealth brand** ("Balance, *prescribed.*"). Its model is fully **async**: a woman takes a 2-minute online quiz, a licensed clinician reviews it (no appointment, no video), and a U.S. compounding pharmacy ships a **compounded prescription** to her door with ongoing telehealth support. It sells four compounded products — a bioidentical-HRT cream (Oestra®), an on-demand libido tablet (Libida™), a sublingual longevity tablet (NAD+), and an anti-aging face cream (BodyMatched™) — spanning menopause, perimenopause, PCOS, endometriosis, postpartum, sexual wellness, longevity, and skin. It was founded by **Dr. Sarah Daccarett, MD**, and positions itself as women-first, root-cause care that simplifies "5–6 prescriptions" into one routine.

## What they offer

Four compounded prescription products, all subscription, each accessed through a per-product quiz — **prices are published as floors on the product pages** (unusual for compounded telehealth):

- **Oestra® (Hormonal Imbalance / HRT):** bioidentical estradiol + micronized progesterone vaginal cream — **$199/month for the first 6 months, then $99.50/month** ongoing `[published]`
- **Libida™ (Sexual Wellness):** on-demand bremelanotide + oxytocin sublingual tablet, non-hormonal — **from $99.70/mo** (20% off) `[published]`
- **NAD+ (Longevity & Cellular Repair):** sublingual NAD+ 200mg daily tablet, needle-free — **from $183/mo** (15% off) `[published]`
- **BodyMatched™ (Anti-Aging Skin Care):** compounded estriol + tretinoin + niacinamide face cream (+ optional finasteride **+$20**) — **from $83/mo** ($249/3-mo) or **$199/mo** monthly `[published]`

Oestra® is the flagship ("Bestseller"); the conditions in the nav (menopause, perimenopause, PCOS, endometriosis, postpartum) are all Oestra applications, not separate SKUs. Per-SKU detail in `offerings.md`.

## How it works / model

Customer journey (identical shell across all four products): **1)** complete a short online quiz/assessment — "no labs or appointments required upfront"; **2)** a licensed clinician reviews the intake and prescribes if appropriate — "no visit needed"; **3)** the prescription is **compounded by a partner U.S. pharmacy and shipped** discreetly; **4)** ongoing telehealth support — unlimited secured messaging, clinician follow-up, and dose adjustments. Labs are **optional, not required** to start ("guided first and foremost by your symptoms... not just lab numbers"). Money: recurring **subscription**, billed monthly against a multi-month supply (Oestra ships a 90-day supply every 90 days, billed monthly). **Cash-pay, no insurance**, HSA/FSA accepted at checkout (+ a letter of medical necessity), free shipping, cancel anytime, 6-month money-back guarantee on Oestra.

## Positioning & audience

**Women only** — "made by women, for women," closing "the gap in women's healthcare." The pitch is root-cause vs. symptom-masking, and radical simplification: Oestra "replaces 5–6 prescriptions" with one cream; NAD+ and Libida are "needle-free" alternatives to injections/IVs. Heavy founder-credibility framing around Dr. Sarah Daccarett. The brand competes against women's-health telehealth peers and runs an aggressive SEO comparison play — 200+ `/p/learn` articles, including dozens of `*-review` and `inner-balance-vs-*` pages targeting Midi, Alloy, Evernow, Winona, Hers, Maven, Gennev, HerMD, Tia, Thrivelab, Visana, Hone, PlushCare, and others. Claimed edges: bioidentical (no synthetics), the proprietary **BodyMatched™** method, vaginal systemic delivery, and female-brain-targeted libido science.

## Nav structure

```
- Shop (mega-menu)
  - What We Treat
    - General HRT — /p/treatment/hrt
    - Endometriosis — /p/treatment/endometriosis
    - Perimenopause — /p/treatment/perimenopause
    - Menopause — /treatment/menopause
    - PCOS — /p/treatment/pcos
    - Postpartum — /p/treatment/postpartum
    - Sexual Wellness — /p/sexual-wellness/libida
    - Longevity & Cellular Repair — /p/longevity/nad
    - Anti-Aging Skin Care — /pqp/anti-aging-face-cream
  - Our Products
    - Oestra™ — bioidentical HRT — /quiz/hormone-imbalance
    - NAD+ — longevity & cellular repair — /quiz/nad
    - Libida™ — on-demand libido booster — /quiz/libida
    - BodyMatched™ Anti-Aging Skincare — /pqp/anti-aging-face-cream
- Learn (mega-menu)
  - About Us — Meet the Doctor (Dr. Sarah Daccarett) — /p/about-us
  - Our Science — Our Approach — /science
  - Clinical Journal — /p/learn (+ "Read all articles")
- Reviews — /reviews
- FAQ — /p/faq
- Log in — /sign-in  ·  Get started — /quiz/hormone-imbalance
- Footer
  - Learn: FAQs (/p/faq), About us (/p/about-us), The Science (/science), Reviews (/reviews), Journal (/p/learn), Featured In (/p/podcasts)
  - What We Treat: General HRT, Perimenopause, Menopause, Endometriosis, PCOS, Postpartum, Skin Care
  - Support: My account (/sign-in), Contact us, Money back guarantee (/p/refund-policy)
  - Getting started: health quiz (/quiz/hormone-imbalance), skin care quiz (/quiz/anti-aging-face-cream)
  - Also: HSA/FSA (/p/hsa-fsa), Fullscript (/p/fullscript)
  - Legal: Terms & Consent (/p/terms-of-use), Privacy Policy (/p/privacy-policy), HIPAA
  - LegitScript-approved seal → legitscript.com lookup
```

## Credibility & proof

- **Scale (self-reported):** "Trusted by **60,000+ women**"; **4.9/5**, **5,695 reviews** (homepage + /p/treatment/hrt).
- **Founder credentials:** **Dr. Sarah Daccarett, MD** — board-certified physician and specialist in women's hormonal health and longevity medicine; "**licensed in 50 states**"; "holds **multiple healthcare patents**"; research "published in the **International Journal of Cardiology**, the **American Journal of Clinical Pathology**, and other leading medical journals"; A4M + Longevity Docs board-certified (/science).
- **Pharmacy / quality:** "compounded in partnership with a U.S.-licensed pharmacy"; partner pharmacy is "**NABP-certified, LegitScript-certified, and PCAB-accredited**"; third-party potency/purity tested; APIs "sourced from FDA-inspected U.S. manufacturers." Predominantly described as **503A**; one Oestra FAQ instead says "**503B FDA-regulated compounding pharmacy** … inspected by the FDA, DEA, and state licensing boards" (verbatim discrepancy — recorded, not adjudicated).
- **Press (self-reported "featured in"):** USA Today, LA Weekly, Muscle & Fitness, Womanly, iHeart, In Touch, Galore, Grit Daily, Mom Magazine, Gladden.
- **Outcome claims (self-reported, internal data — flagged):** Oestra 8-week review — "98% improved vaginal dryness," 81% sleep, 80% mood; "90% of our patients saw an improvement in sleep, mood, anxiety and depression within 10–14 days." BodyMatched — "wrinkle depth … decreasing by 61–100%," "+80% collagen."
- **Cited authority (verbatim, flagged):** "Estrogen is one of the most effective longevity interventions for women. — FDA announcement, November 2025" (the brand's characterization of an FDA decision).
- **Guarantees:** 6-month money-back (Oestra); 30-day money-back (skincare 3-month plan). HIPAA-compliant & secure.

## Visual & brand impression

Clean, modern, feminine-clinical. The mark is a lightweight **periwinkle-blue (#5472CC)** "Inner Balance" logotype on a white/cream canvas, segmented into soft pastel photo blocks. Heavy use of warm, real-women lifestyle photography plus tidy isolated product renders — pastel tins (teal NAD+, purple Libida) and white/blue jars/bottles (Oestra, BodyMatched). Typography is a clean grotesque (branding reports "Suisse BP"). Overall it reads as a trustworthy, premium, science-forward women's-wellness brand — warmer and softer than the bro-coded men's-health DTC aesthetic, leaning on the founder-physician as the credibility anchor.

## Strategic read

The differentiators worth flagging: **(1) published price floors** — Inner Balance shows "From $X/mo" on every product page, where most compounded-telehealth peers gate all pricing behind intake. **(2) An aggressive comparison-SEO engine** — hundreds of `/p/learn` articles, including a large library of `*-review` and `inner-balance-vs-<competitor>` pages farming branded-competitor search. **(3) Asset-light fulfillment** — entirely **compounded** (no FDA-brand drugs) through a **partner** 503A pharmacy it does *not* claim to own, lighter than Ro/Hims-style owned-pharmacy stacks. **(4) A "needle-free" wedge** for NAD+ and Libida against injectable/IV incumbents, and Oestra's "replaces 5–6 prescriptions" simplification wedge. The site is **A/B-tested via Optimizely**, so prices, promos (20%/15% off), and modules are point-in-time. Note the 503A/503B inconsistency across pages as a quality-of-claims signal.

## Provenance

- **Pages:** homepage, /p/treatment/hrt, /p/longevity/nad, /p/sexual-wellness/libida, /pqp/anti-aging-face-cream, /p/about-us, /science, /p/faq, /reviews (9 pages); Firecrawl, all formats on homepage; map (385 urls) for inventory.
- **Verify:** all 9 sourceURLs matched requested; all body md5s unique (no geo/cache contamination).
- **Credits:** 10 (1 map + 9 scrapes), all basic proxy.
- **Couldn't get:** per-SKU checkout pricing + exact dose tiers (behind each /quiz intake); the compounding pharmacy's name/entity (described only as a "partner" pharmacy, unnamed, no owned facility); official founding year (a patient cites "since 2023").
- **Run profile:** guided — full-pack request: +offerings.md (flagship + companions roster), +telehealth.md cohort pack, +logos (2.5: wordmark/logomark), +PDP hero product renders (4 clean isolated images at captures/2026-06-04/images/).
