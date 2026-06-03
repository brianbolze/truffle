---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.3"

# Identity
domain: gogeviti.com
name: Geviti
aliases: ["Geviti Health Inc."]      # legalName from footer © line
parent: []
owns: []
socials:
  instagram: https://instagram.com/gogeviti
  linkedin: https://linkedin.com/company/geviti
external: {}                          # no JSON-LD sameAs / third-party records found

# Capture meta
captured_at: 2026-06-02
capture_method: firecrawl
site_notes: "Next.js on Vercel; the actual product is a separate app at app.gogeviti.com — every Login / 'Start Free' / 'Get My Protocol' CTA redirects there, so marketing copy is on www and pricing/ordering depth is app-walled. Map is ~80% /blog + /es (Spanish-locale) noise; ALL signal pages surfaced from homepage links, not the map. No /about page — founder story + mission live on the homepage and /pricing (and a /blog mission post). A/B: yes — the /pricing page is served under a CRO variant (URL utm_content=pricing-cro_c) and the annual Plus price flickers ($1,524 on /pricing vs $1,529.99 on homepage); treat captured pricing/IA as point-in-time. State counts differ by scope across pages: platform 47 / clinic-page 39 'licensed' / FAQ Rx-services 29 — re-verify each on recapture. Support chat = Crisp (website_id=geviti)."
key_pages:
  pricing: /pricing
  clinic: /clinic
  testing: /testing
  bloodwork: /bloodwork
  supplements: /supplements
  faq: /faq
unverified_fields:
  - "State availability is inconsistent across pages — homepage/pricing say '47 states' (excl. AK, HI, RI), the /clinic page says '39 States Licensed', and /faq says Rx clinical services are in '29 states' (incl. CA, TX, FL, IL). Different scopes (platform vs clinician licensure vs Rx), not reconciled on-site."
  - "Prices/IA are a point-in-time snapshot, not fixed — /pricing is served under a CRO/A-B variant (utm_content=pricing-cro_c); annual Plus is '$1,524' there vs '$1,529.99' on the homepage."
  - "Free-tier pay-per-test panel is listed as both '$399 full panel' and 'full panel from $349' on the same card."
  - "/testing references an 'Infinite' / 'Premium' membership tier ('Included · Plus & Infinite', 'quarterly with Infinite', 'Premium membership'), but /pricing and /faq list only Free + Plus and give no Infinite price — stale or unreleased tier; left out."
  - "Per-Rx pricing (HRT, peptides, GLP-1s) and the full à-la-carte catalog are behind the app + intake; only 'Exclusive Member Pricing' shown. JSON-LD numberOfEmployees '50+' is self-reported structured data, not on a visible page — omitted."

description: "A telehealth longevity membership: 100+ biomarker blood panels, genetics, and gut tests, read by AI and a clinician care team into personalized protocols — HRT, peptides, GLP-1s, and custom supplements shipped monthly."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://www.gogeviti.com/images/icons/ui/geviti-logo.svg
brand_colors: { primary: "#06284B", accent: "#D5EFFF", background: "#F9F8F6" }   # deep navy + pale-blue sky accent on off-white; confirmed vs screenshot
fonts: [Aspekta, VictorSerif]        # Aspekta sans body, VictorSerif display headings
color_scheme: light
design_framework: next.js            # /_next/ in rawHtml + Vercel host (branding payload mislabels it "tailwind")
---

## Overview

Geviti is a DTC longevity / health-optimization telehealth platform sold as a membership. It unifies four data streams — blood, genetics, gut microbiome, and wearables — into one system, runs them through an AI layer it brands **Makor AI**, and pairs each member with a dedicated care team that builds and continually re-tunes a personalized protocol. The protocol spans custom-compounded supplements, prescription therapies (HRT, peptides, GLP-1s, thyroid), nutrition, and lifestyle, shipped monthly. Positioned as the antidote to fragmented "your-doctor-sees-14-markers-once-a-year" care: *"We don't treat sickness. We solve what causes it."* Founded and led by **Nathan Graville (Founder & CEO)**, whose stated origin story is losing his father to cancer at 58 despite tests that "said he was 'fine.'" Explicitly for **both men and women** (not a male-only brand). Operating entity: Geviti Health Inc.

## What they offer

Flagship is the **Plus membership**; everything else is a companion line bought through it (à-la-carte testing, supplements, Rx) or a free on-ramp. Membership is required to access any service.

- **Plus membership:** the full stack — 100+ biomarker panel 2×/yr, at-home draws, quarterly coaching + provider visits, full Rx catalog access, AI + Specialist protocol, custom supplement packs at member pricing, same-day care-team response — **$127/mo, billed annually at $1,524** (homepage: $1,529.99); semi-annual option also offered `[published]`
- **Free plan:** app access + Personalized Health Blueprint + custom-supplement-blend access + specialty-testing marketplace, **$0/mo**, with **pay-per-test labs ("$399 full panel" / "from $349")** and at-home phlebotomist as a **$79 add-on** `[published]`
- **Longeviti Panel (bloodwork):** 100+ biomarkers across metabolic, kidney/liver, cardiovascular, hormones (incl. total/free/bioavailable testosterone, estradiol, thyroid), nutrients, inflammation; includes PhenoAge biological-age scoring. Included with Plus; **self-valued at "over $2,200" if bought independently** `[published]`
- **Longevity Clinic (Rx):** clinician-prescribed **HRT (testosterone, estrogen, progesterone), peptides (BPC-157, TB-500, sermorelin, GHK-Cu), GLP-1s (semaglutide, tirzepatide), thyroid** — compounded and shipped; member pricing only, no list price `[on-request]`
- **Custom supplements (Longeviti Blend):** blood-based AM/PM packs, Xymogen pharmaceutical-grade, re-optimized every 6 months; "member pricing," no published unit price `[on-request]`
- **Longeviti Genomics (genetics):** one-time DNA test (APOE, MTHFR, drug metabolism) — **add-on $300 member / $500 free** `[published]`
- **Longeviti Microbiome (gut):** Mosaic GI360 test — **add-on $500 member / $600 free** `[published]`
- **Longevity Blueprint:** the personalized optimization plan that ties the data together (also available on Free)

Self-reported value framing (verbatim, theirs): Plus bundles **"$10,000+ in testing & care"**; their comparison table pegs Plus at **$1,524/yr** vs labs-only **$499/yr**, PCP+concierge **$2,000+/yr**, DIY stack **$3,800+/yr**.

## How it works / model

1. **Intake** (~6–15 min) → 2. **At-home blood draw** by a licensed phlebotomist (or walk into any **Quest Diagnostics** location with a requisition) → 3. **Results in 5–7 days** from CLIA-certified labs → 4. **Makor AI** surfaces patterns; a **Longevity Specialist** + clinician build the protocol (clinician review within 72 hrs) → 5. **Monthly shipment** of supplements/Rx → 6. **Retest** (6-month for Plus, quarterly higher tiers) and re-tune.

- **Care team is 3 roles:** Medical Director (oversees protocols + Rx), Longevity Specialist (monthly check-ins), Member Support (day-to-day).
- **Money:** subscription membership (semi-annual or annual) is the core; supplements, peptide/Rx meds, and specialty diagnostics are **purchased separately at member-discounted pricing**. **Cash-pay only — no insurance, Medicare, or Medicaid.** HSA/FSA accepted (supplements need a Letter of Medical Necessity via **Truemed** partnership).
- **Rx supply chain:** prescriptions written by board-certified US physicians / NPs licensed in the member's state, dispensed from **US-licensed 503A and 503B compounding pharmacies**. Geviti's own footer disclaims it "IS A HEALTHCARE TECHNOLOGY COMPANY AND NOT A LABORATORY OR MEDICAL PROVIDER" — labs and medical services are provided by independent third parties.
- **Delivery:** native iOS + Android apps (ordering, tracking, Daily Tracker, Makor AI, Blueprint all live in-app) + web dashboard.

## Positioning & audience

Targets health-proactive adults (testimonials skew 30s–50s, both sexes) who want optimization, not sick-care. The recurring foil is the fragmented status quo — "blood panel here, genetics there, supplements from a blog post, doctor sees 14 markers once a year, none of it talks to each other." Claimed edge: a single AI-unified data system + a dedicated human care team + bundled membership economics that "pays for itself by month two." Names competitors directly — a /pricing FAQ answers **"How does Geviti compare to Function Health?"** (positioning Function as bloodwork-and-reporting only, Geviti as data→protocol→shipped), and blog content benchmarks against **Lifeforce, Function Health, and Mito Health**.

## Nav structure

```
- Features
  - Custom Supplements — /supplements        (personalized blends from bloodwork)
  - Routine Bloodwork — /bloodwork           (100+ biomarkers, at-home collection)
  - Longevity Clinic — /clinic               (provider visits, Rx, care plans)
  - Testing Shop — /testing                  (at-home panels: blood, gut, genetics)
  - Longevity Blueprint — /blueprint         (personalized optimization plan)
- Resources
  - Blog — /blog
  - FAQ — /faq
  - Security & Trust — /security
- Pricing — /pricing
- Login / Start Free → app.gogeviti.com
```

## Credibility & proof

- **Press ("As Seen In"):** Fox Business, Newsweek, Yahoo (logos only).
- **Self-reported metrics (verbatim, unverified):** "450,000+ lab tests ran"; "78% clinically meaningful improvement within 6 months"; "93% measurable improvement in at least one health category"; "4.9 average member satisfaction"; "6,000+ custom blends formulated"; "94% member retention rate"; clinic stats "12+ avg years clinical experience" and "2hr avg response time."
- **Compliance posture (self-reported):** HIPAA-compliant infrastructure, **SOC 2 Type II certified**, end-to-end encryption, data never sold; HSA/FSA eligible.
- **Named partners / vendors (real signal):** Quest Diagnostics (walk-in draws), **Mosaic Diagnostics GI360** (microbiome), **Xymogen** (supplement ingredients), **Truemed** (HSA/FSA LMN), CLIA-certified partner labs, 503A/503B compounding pharmacies, Crisp (support chat).
- **Testimonials:** heavy — named members with "Verified" badges, video/social cards, and before→after biomarker receipts (hsCRP 15.06→0.8, A1C 10.5→6.5, etc.). Treat as marketing, not evidence.

## Visual & brand impression

Premium, calm, aspirational — reads well-funded. A pale-blue sky/cloud photographic hero sits on an off-white/cream canvas (#F9F8F6) that deepens to a navy (#06284B) footer; serif display type (VictorSerif) over a clean sans body (Aspekta) gives a "modern apothecary / longevity-luxury" tone. Stat-forward (big 78% / 93% / 4.9 numbers), testimonial-dense, with an "invest in your future" emotional frame anchored by the founder's father-loss story. High design maturity and visual consistency across pages.

## Strategic read

The model's distinctive move is **absorbing four normally-separate spend categories — diagnostics, telehealth Rx, a compounding pharmacy, and supplements — into one $127/mo membership SKU**, with "Makor AI" as the connective-tissue narrative and a 3-person care team as the human moat. Structurally it's a longevity-framed, gender-neutral, premium telehealth-to-compounding-pharmacy stack: clinician-prescribed HRT / peptides / GLP-1s fulfilled through 503A/503B compounders, monitored by recurring bloodwork. The pricing page leans hard on a cost-stacking comparison (membership "pays for itself by month two") and on direct comparison to data-only players like Function Health.

## Provenance

- **Pages:** homepage + /pricing, /clinic, /testing, /bloodwork, /supplements, /faq (7 total) — Firecrawl scrape (markdown + screenshots), plus a /v2/map inventory and homepage rawHtml/branding/JSON-LD signals. All CTAs route to the app.gogeviti.com product, which was not entered.
- **Verify:** all 7 sourceURLs matched requests; all 7 body md5s unique (no geo/cache contamination). Post-write lint re-run.
- **Credits:** 8 (1 map + 1 homepage + 6 key pages, 1 credit each; no enhanced-proxy/PDF add-ons).
- **Couldn't get:** per-Rx and per-supplement unit pricing (app + intake walled); the named "Infinite"/"Premium" tier's price; any third-party reputation record (no JSON-LD sameAs).
