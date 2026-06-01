---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.2"

# Identity
domain: functionhealth.com
name: Function Health
aliases: [www.functionhealth.com]
parent: []
owns: ["ezra.com"]              # acquired Ezra (medical imaging); Ezra runs as a named brand under Function — leadership + scans integrated. Domain slug unconfirmed against ezra.com — see unverified_fields.
socials: { facebook: "https://facebook.com/askfunction/", instagram: "https://instagram.com/functionhealth/", x: "https://x.com/function", youtube: "https://youtube.com/channel/UCdeq9Uha-87vDSvtCoSJLQg", linkedin: "https://linkedin.com/company/functionhealth/" }   # JSON-LD sameAs (hand-read; the block has a stray trailing brace)

# Capture meta
captured_at: 2026-06-01
capture_method: firecrawl
site_notes: "Webflow (data-wf-* ×400 + cdn.prod.website-files.com; branding.designSystem said 'custom' — wrong, per the §5.4 rule). App lives on my.functionhealth.com; marketing on www. Logo is an inline data-URI SVG wordmark → use favicon fallback. Membership price ($365/yr, '$1/day') is on homepage + /pricing; scans pricing (member vs list, via Ezra) only on /scans. Long biomarker/condition marquees repeat the same terms many times in markdown — animation noise, not data. Footnote: $365 lab membership excluded in NY & NJ. No A/B tool fingerprinted, but $365 is 'first-year' promotional framing and scan prices show strikethrough promos — treat pricing as a snapshot. 2026-06-01 re-verify: re-scraped homepage + /pricing + /scans only (3 pages, 3 credits) — ALL pricing unchanged from the 2026-05-31 full capture ($365/yr; MRI $999→$899, MRI+Spine $1699→$1,499, MRI Skeletal/Neuro $3,999, Heart CT $349, Lungs CT $399, $200 scan credit). /pricing also surfaces an FAQ link 'MRI starting at $499' and out-of-pocket comparison stats ($12,022/yr diabetes, $4,423/yr heart failure, $2,529/day hospital). Scan booking now routes to my.ezra.com 'Book directly with Ezra' alongside the Function signup. Body sections below carried forward from the 2026-05-31 capture (still accurate)."
key_pages:
  how_it_works: /how-it-works
  what_we_test: /what-we-test
  scans: /scans
  pricing: /pricing
  about: /about
  why_choose: /why-choose-function
  for_business: /for-business
  lab_locations: /lab-locations
unverified_fields:
  - "Prices/promotions are a point-in-time snapshot, not fixed — $365 is explicitly first-year membership pricing (was ~$499; site links an article 'membership is now $365/year'); scan prices show member strikethrough promos ($999→$899, etc.)."
  - "owns: ezra.com — Ezra is integrated (its CEO/CMO sit on Function's team, scans booked via my.ezra.com) but the parent/child domain relation wasn't captured from ezra.com itself; slug is inferred."
  - "Member count not stated; '75M+ results delivered to Function members' is the only public scale metric on-site."
  - "Add-on test catalog (Galleri/GRAIL multi-cancer, brain, environmental toxins, sexual health, etc.) is named but à-la-carte pricing sits behind the member app, not captured."

description: "A healthcare-technology membership that gives consumers twice-yearly access to 160+ lab biomarkers at Quest locations, with clinician-reviewed results and personalized action plans, plus member-priced full-body MRI/CT scans via its Ezra acquisition."

# Classification
entity_type: Company
target_market: [B2C, B2B]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://cdn.prod.website-files.com/68823b2fd9cc28b78fb3ee65/69710ea94b3b07ac1965f017_Favicon.png  # branding.images.logo is an inline data-URI SVG wordmark; favicon fallback per §5.4
brand_colors: { primary: "#FEF9EF", accent: "#B05A36", text: "#2A2B2F" }  # cream ground + terracotta/rust accent, near-black text — verified against homepage screenshot
fonts: [Financier Display, Inter]   # serif display (italic headlines) + sans body; branding listed Arial/Inter first, but Financier Display carries the brand
color_scheme: light
design_framework: webflow           # rawHtml: data-wf-* ×400 + website-files.com, NOT branding.designSystem ("custom")
---

## Overview

Function Health sells a single annual membership ($365/year, framed as "$1/day") that gives consumers comprehensive, proactive lab testing far beyond a standard physical — **160+ lab tests** drawn twice a year, scheduled at 2,000+ Quest Diagnostics locations, with every result reviewed by clinicians and turned into a personalized action plan inside the Function app. The pitch is preventive and longevity-framed ("100 Healthy Years"): catch early, silent signals of "1000+ conditions" before symptoms appear, owning your own data rather than relying on a PCP. In 2025 it acquired **Ezra** and now layers member-priced full-body **MRI and CT scans** on top of the bloodwork. It positions itself explicitly as a *healthcare technology company — not a lab or medical provider* (independent third parties run the labs and medical services).

## What they offer

One membership is the product; scans and add-on tests are companions (breadth here; per-SKU depth defers to `offerings.md`):

- **Function membership:** "$365 per year — $1 per day" (first-year pricing, HSA/FSA eligible). Includes 160+ lab tests annually, an Annual Test + a Mid-Year (3–6 mo) retest, clinician review of every result, and a personalized protocol. "There's just one Function membership" — no tiers.
- **Add-On Tests (member-only):** à-la-carte advanced tests on top of membership — **Galleri® / GRAIL multi-cancer**, brain/Alzheimer's health, environmental-toxin & mold reactivity, sexual health (chlamydia, herpes, etc.). Pricing behind the app.
- **MRI & CT scans (via Ezra):** member-priced imaging booked through Ezra. **Annual MRI:** "$999 / $899" (member); **MRI with Spine:** "$1699 / $1,499"; **MRI with Skeletal & Neurological Assessment:** "$3,999"; **Heart CT (CAC score):** "$349"; **Lungs CT:** "$399." Up to a "$200 credit off scans for Function members." 170 scan locations and growing.
- **Function for Work (B2B):** employer-sponsored program (`/for-business`) — onboarding, engagement tooling, reporting; tailored for executives, remote, and frontline teams.
- **Gifting + referral + creator/practitioner programs:** memberships are giftable; referral rewards paid via Impact.

## How it works / model

Four-step member journey: **(1) Personalize & test** — share health history, book at 2k+ Quest labs (or Getlabs mobile phlebotomy in select areas); a phlebotomist draws blood (deliberately *no* at-home kits — "they risk sample integrity"). **(2) Review results** — clinicians flag what matters and what to do next; critical results trigger a provider call. **(3) Test again** — Annual + Mid-Year retests to see change over time. **(4) Monitor for life** — track trends/red flags across years. Revenue is the recurring annual membership (subscription), with transactional add-ons (scans, advanced tests) layered on. Function facilitates access; labs/imaging/medical services are billed by and provided by third parties.

## Positioning & audience

Targets affluent, health-engaged consumers ("a new, discerning generation") who feel underserved by insurance-gated primary care — "doctors aren't ordering the right tests." The claimed edge is **depth + proactivity + ownership**: tests standard care skips (ApoB, Lp(a), fasting insulin, lipoprotein particle size, heavy metals, autoimmune panels), drawn twice yearly, at a transparent flat price ("What could cost you $15,000 is $365"), with the data in the member's hands. Competes against both traditional annual physicals and lighter wellness/at-home-test brands by claiming clinical-grade rigor (Quest labs, no at-home kits) plus a marquee medical board. Now also competes in the longevity-imaging space (Prenuvo, Ezra-standalone) via the scans line.

## Nav structure

```
Primary nav:
- How it works — /how-it-works
- What we test — /what-we-test
- About — /about
- MRI & CT scans — /scans
- FAQ — /faq
- Gift Function — /gifting
- Pricing — /pricing
- For employers — /for-business
- Contact us — /contact-us
- Log in — https://my.functionhealth.com/login
- Start testing — https://my.functionhealth.com/signup

Footer — Company:
- Join Function · Login · Newsroom — /newsroom · Security — /security · Careers — /careers · Contact us — /contact-us
Footer — Explore:
- What people say — /what-people-say · About — /about · MRI & CT scans — /scans · Pricing — /pricing · Lab locations — /lab-locations
Footer — Community:
- Gift Function — /gifting · For employers — /for-business · For practitioners — /practitioners-and-providers · For creators — /for-creators · Share your story (Typeform)
Apps: iOS (App Store) · Android (Google Play)
```

"What we test" areas (the offering taxonomy): Autoimmunity, Heart, Thyroid, Cancer Detection, Immune Regulation, Female Health, Male Health, Metabolic, Environmental Toxins, Biological Age, Nutrients, Stress & Aging, Liver, Blood, Kidneys, Pancreas, Brain Health, Electrolytes, Allergies & Sensitivities, Urine, Sexual Health, Bone Health, Infections, Gut, + MRI & CT Scans.

## Credibility & proof

- **Scale claim:** "Over 75+ million results delivered to Function members"; "2,000+ lab test locations across the US."
- **Medical & Scientific Advisory Board:** JoAnn E. Manson (Harvard/Brigham), Andrew Huberman (Stanford), Toby Cosgrove (ex-CEO Cleveland Clinic), Daniel Sodickson (NYU, parallel-MRI pioneer; also Chief Medical Scientist), Azra Raza (Columbia oncology), Eddie Chang (UCSF), Luis A. Diaz (Memorial Sloan Kettering).
- **Founders/leadership:** Jonathan Swerdlin (Co-Founder, CEO), Pranitha Patil (Co-Founder, CBO), **Mark Hyman, M.D.** (Co-Founder, CMO; 15× NYT bestseller), Seth Weisfeld (Co-Founder, CDO), Dan Swerdlin (Co-Founder, GC); Ziad Sultan (CPTO, ex-Spotify SVP Personalization), Neil Shah (COO, ex-Slack COO), **Emi Gal (CEO, Ezra)**, Danna Chung MD (CMO, Ezra), Tiffany Lester MD (Women's Health Med Dir, ex-Parsley Health).
- **Security:** SOC 2 Type II + HIPAA-aligned; encrypted data.
- **Awards/press:** TIME100, Fast Company (Most Innovative / World Changing Ideas), Oprah, LinkedIn, Merit Awards, Inc Best Of.
- **Partnerships:** NBPA, Erewhon, Sweetgreen, Thrive Global, OneMind.
- **Endorsers/voices:** Andrew Huberman, Jay Shetty, Mari Llewellyn, Baya Voce; heavy member-testimonial and "real people, real results" story library.

## Visual & brand impression

High design maturity — an editorial, premium-wellness aesthetic that reads clinical-but-warm. Cream/off-white ground (`#FEF9EF`) with a single terracotta/rust accent (`#B05A36`) and near-black text; large italic serif display headlines (Financier Display) over a clean sans body (Inter), generous whitespace, restrained motion. Imagery leans on credentialed-physician portraits, member story photography, and a quantified results UI. The overall feel signals trust, science, and aspiration rather than DTC-funnel urgency — closer to a luxury health brand than a discount lab service.

## Strategic read

The **Ezra acquisition** is the headline move: Function is bolting structural imaging (MRI/CT) onto its bloodwork membership to become a one-stop proactive-screening platform, and pulling Ezra's leadership/cancer-detection mission inside. The "$499 → $365/year" price cut signals an aggressive land-grab for membership scale (the 75M-results figure implies large volume), with margin shifting toward the higher-ticket scans and add-on tests. The deliberate **no-at-home-kits** stance (Quest-only draws) is a credibility wedge against at-home testing rivals. Watch: the recurring-membership ↔ transactional-scan mix, and how the "healthcare technology company, not a provider" framing holds as the clinical surface (clinician review, scans) deepens.

## Provenance

- **2026-06-01 re-verify (this run):** re-scraped the 3 pricing-bearing pages — homepage, /pricing, /scans (3 credits) — at the user's request to confirm pricing isn't stale. All sourceURLs matched, all bodies unique (verify clean). **Every price is unchanged** from the 2026-05-31 capture; prior full capture moved to `captures/_archive/2026-05-31`. Body sections below are carried forward (still accurate).
- **2026-05-31 full capture:** homepage, /how-it-works, /what-we-test, /scans, /pricing, /about, /why-choose-function (7 captures) — Firecrawl scrape, all-formats homepage + markdown/links/screenshot on key pages, `maxAge:0` + `location:US`.
- **Verify:** all 7 sourceURLs matched; all body md5s unique (no §5.1 contamination).
- **Credits:** 8 (1 map + 1 homepage + 6 key pages) on the original capture, + 3 on the 2026-06-01 re-verify; no enhanced-proxy or PDF add-ons.
- **Couldn't get:** member-app-gated add-on/scan à-la-carte pricing; member count; the parent↔Ezra domain relation from ezra.com itself (inferred). Long biomarker/condition marquees are animated repeats — treated as noise.
- **Structured layer (schema 2.2):** read this capture's homepage JSON-LD via `fc.py signals` ($0 re-enrichment from the persisted 2026-06-01 rawHtml, hint-to-verify) — filled `socials` (fb/ig/x/youtube/linkedin) — hand-read from the homepage JSON-LD (a stray trailing brace fails strict parse, but the `sameAs` is intact and handle-matched); no usable `logo`/`external`. Re-stamped 2.0→2.2.
