---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: clerky.com
name: Clerky
aliases: ["Clerky, Inc."]
parent: []
owns: []
socials: { x: "https://twitter.com/clerkyinc", linkedin: "https://www.linkedin.com/company/clerky-inc-" }
external: {}

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Webflow site (website-files.com CDN, data-wf-* in rawHtml; branding.designSystem says 'custom' — ignore per §5.4). /pricing is a JS-rendered interactive comparison table — scrapes THIN (only the H1) even with --proxy enhanced; the SAME table renders statically in the homepage capture ($427 / $819 + full feature matrix), so read pricing from homepage.md, not /pricing. Per-product à-la-carte prices are NOT published — pricing rolls up into two one-time packages + 3rd-party fee pass-throughs. Products are anchor sections on /startups/products (#formation … #maintenance), not separate PDPs. Help center + handbooks are on subdomains (help.clerky.com, handbooks.clerky.com); the app is app.clerky.com. Map is clean (subdomains-off); filter /article/, /category/, /collection/, /blog/, /help/ help+content noise."
key_pages:
  products: /startups/products
  pricing: /pricing
  about: /about
  comparison: /comparison
  legal_quality: /legal-quality
  attorneys: /attorneys
unverified_fields:
  - "Per-product à-la-carte prices — not published; only the two packages ($427 / $819) and '+ 3rd party fees' pass-throughs are shown."
  - "/pricing comparison table did not render to markdown (JS wall, thin even with enhanced proxy) — pricing read from the homepage's static copy of the same table."

# Description — one sentence
description: "An online legal service that helps startup founders generate, sign, and file standard legal paperwork — incorporation, fundraising SAFEs, equity, and hiring docs — built and run by former startup attorneys."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS, Services / Consulting]   # software that generates legal docs; secondary = done-for-you filing (DE/IRS), registered agent, EIN
portfolio_shape: Flagship + companions                        # Formation/Incorporation is the hero; fundraising/hiring/commercial/maintenance "go further" after forming
business_model: Transactional / One-time                      # one-time fees ($427 pay-per-use, $819 lifetime); no subscription. Minor recurring: registered-agent renewals
primary_industry: Consulting & Professional Services           # legal services / legaltech — no "Legal" value in the set; closest fit

# Visual identity — branding payload is a hint; confirmed against screenshots
logo_url: https://cdn.prod.website-files.com/64bfd4a79278e7a8fe5b8d39/64bfd4a79278e7a8fe5b8d6b_logo_clerky.svg
logos:
  wordmark: { src: "https://cdn.prod.website-files.com/64bfd4a79278e7a8fe5b8d39/64bfd4a79278e7a8fe5b8d6b_logo_clerky.svg", w: 110, h: 20 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=clerky.com&sz=256", px: 256, transparent: true }   # black "C" roundel; PNG corners genuinely transparent (white disc is the logo's own fill, not a baked box)
  og:       { src: "https://cdn.prod.website-files.com/64bfd4a79278e7a8fe5b8d39/64ea1885862892bff8a0e420_twitter-card-summary-large-6d0d37a3.png", w: 1024, h: 512 }
brand_colors: { primary: "#008FD5", accent: "#006EA3" }        # Clerky blue (CTAs/checkmarks); wordmark itself is near-black charcoal — see Visual
fonts: [Graphik Clerky, Arial]
color_scheme: light
design_framework: webflow
---

## Overview

Clerky is an online legal service that builds software to help startup founders get standard legal paperwork done correctly — Delaware incorporation, fundraising, hiring, and corporate-maintenance documents. It's **self-help software, explicitly not a law firm** ("we're not your attorney"), used by founders on their own or in collaboration with their attorneys. Founded and run by two former Orrick startup attorneys, it positions on a single axis — **legal quality** — arguing it does paperwork the way top Silicon Valley law firms do, so founders avoid expensive problems later. It is deeply embedded in the YC / startup-attorney ecosystem (YC sends unincorporated founders to Clerky).

## What they offer

Pricing is **two one-time packages**, not a subscription (homepage pricing table): **Pay Per Use $427** `[published]` and **Company Lifetime Package $819** `[published]` (both "One-Time Fee"). Product lines below; per-SKU detail in [`offerings.md`](offerings.md).

- **Formation** *(flagship)* — Delaware C-corp incorporation + post-incorporation setup (stock issuance with vesting, bylaws, board/officer election, **83(b)** support, CIIAA), foreign qualification (CA/NY direct, others via partners), stock-plan adoption, EIN application for non-US founders, and corporate bank-account application. Entry price **$427** pay-per-use, incl. **$203** Delaware expedited filing fees + **$125** first-year registered-agent fee `[published]`. Self-reported: **"20,000+ Startups Incorporated."**
- **Fundraising:** SAFEs and convertible notes (valuation cap / discount / both), with a financing checklist + signature escrow ("just like how a law firm would do it"). Unlimited in the $819 package, pay-per-use otherwise — per-instrument price not shown `[partial]`. Self-reported: **"Over $5 billion raised from over 1,000 top seed investors."**
- **Hiring:** New-hire paperwork (offer letters, consulting & advisor agreements, CIIAA) + equity compensation (restricted stock; regular and early-exercisable stock options). Unlimited in lifetime package, else pay-per-use `[partial]`.
- **Commercial:** One-way and mutual NDAs. Unlimited in lifetime package, else pay-per-use `[partial]`.
- **Maintenance:** Charter amendments (company-name change, increase authorized shares) and board consents (change directors/officers, add co-founders) — **"+ 3rd party fees"** / "Pay only 3rd party fees" `[partial]`.
- **Attorney accounts** *(free, B2B channel):* a private workspace for startup attorneys to review/observe client paperwork, plus **"over 40 advanced products that are not publicly available"** (e.g. fixing formations done elsewhere) `[published]` (free).

## How it works / model

Founders fill in customizable forms; Clerky's software generates standard legal documents, collects e-signatures, and — for incorporation, EIN, and foreign qualification — **files with the state / IRS in-house** (EIN faxed to the IRS, "100% in-house, not outsourced"; Clerky also acts as registered agent). Collaboration is a core feature: loop in co-founders and attorneys as **reviewers** (sign-off) or **observers** (kept in the loop), with a full audit trail. **Monetization is one-time fees** — a **$427** Pay-Per-Use entry (incorporation + post-incorporation setup; pay per use for everything after) or an **$819** Company Lifetime Package (unlimited fundraising/hiring/NDAs/maintenance). Third-party fees (Delaware, registered agent) are bundled into formation or passed through on maintenance. Forming on Clerky unlocks a lifetime "legal dashboard" for the companion lines — the lock-in.

## Positioning & audience

Targets **high-growth startup founders on the Delaware C-corp / venture track**, and the **startup attorneys** who serve them (a second, free product surface). Competes against other online legal/incorporation services and DIY / low-quality lawyers (no competitor named on-site). Claimed edge: an **"obsession with legal quality"** — run by ex-Orrick attorneys, using forms "considered extremely standard in Silicon Valley," with a thesis that the online-legal market is **"broken"** because a founder structurally *cannot* verify legal quality (no market feedback loop on defects), so they should trust expertise + endorsements over marketing. Endorsements lean heavily on YC and elite startup law firms.

## Nav structure

```
- Products — /startups/products
  - Formation — /startups/products#formation
  - Fundraising — /startups/products#fundraising
  - Hiring — /startups/products#hiring
  - Commercial — /startups/products#commercial
  - Maintenance — /startups/products#maintenance
- Pricing — /pricing
- We're Different — /comparison
- On Legal Quality — /legal-quality
- Delaware PBCs — /public-benefit-corporations
- Help Center — https://help.clerky.com/
- [audience toggle] Startups — / · Attorneys — /attorneys
- Sign In — https://app.clerky.com/ · Get Started — https://app.clerky.com/signup
- Footer →
  - Products: Formation, Fundraising, Hiring, Commercial, Maintenance, Pricing, For Attorneys, Delaware PBCs
  - Resources: Help Center (help.clerky.com), Handbooks (handbooks.clerky.com), On Legal Quality, We're Different, Contact (support@clerky.com)
  - Company: About Us — /about, Careers — /careers, Blog — /blog, Cookie Settings
  - Legal: Terms — /terms, Privacy — /privacy
```

## Credibility & proof

*All figures are the company's own claims (self-reported), recorded verbatim:*

- **Scale:** "20,000+ Startups Incorporated" (homepage); "Over $5 billion raised from over 1,000 top seed investors" (products page); attorney accounts offer "over 40 advanced products."
- **Customer logo wall** (self-reported, with metrics): Coinbase "$86B IPO," Gusto "$140M Series C," Zapier "$140M+ ARR," Segment "Acquired for $3.2B," Clever "Acquired for $500M," Codecademy "Acquired for $525M," EasyPost "$88M raised," 15Five "$52M Series C," and others (Meteor, Parse "Acquired for $85M," LearnSprout "Acquired by Apple," iCracked "Acquired by Allstate").
- **Attorney/firm testimonials** (named): Kirsty Nathoo (Partner, Y Combinator) — "I send the founders to Clerky and know everything will be done correctly"; Lou Soto (Gunderson Dettmer); David Goldenberg (VLP Law Group); José Ancer (Optimal Counsel); John Bautista (Orrick — also a Clerky advisor); Andre Gharakhanian (Silicon Legal Strategy).
- **Advisors:** John V. Bautista (Partner, Orrick; co-founded Venture Law Group); Carolynn Levy (Partner & General Counsel, Y Combinator).
- **Press:** Forbes (2025), Fast Company, TechCrunch (2013 "YC-backed Clerky…", 2017).
- **Compliance/legal:** "Clerky, Inc. is a bonded legal document assistant registered in Santa Clara County, California (#LDA258, expiring February 27, 2028)." Address 440 N. Barranca Ave. #1881, Covina, CA 91723; phone 650-440-5449.

## Visual & brand impression

Clean, restrained, high-trust SaaS. White background, generous whitespace, a single **Clerky-blue (#008FD5)** accent on CTAs and feature checkmarks; the wordmark itself — a filled **"C" roundel + "CLERKY"** — renders in near-black charcoal, not the blue. Custom **"Graphik Clerky"** type (Graphik variant → Arial fallback). The page is deliberately sober: no flashy motion, conservative layout, a law-firm logo wall, a founders' photo, a customer-logo grid, and a detailed pricing-comparison table — every element pushing *trustworthy and transparent* over *exciting*. Lawyer-credible but founder-approachable. High design maturity.

## Strategic read

Clerky's entire moat is a property the buyer **structurally cannot verify** — legal quality — and its strategy is to make that the whole story. The `/legal-quality` manifesto reframes un-verifiability as positioning: the market is "broken" (most startups fail, so defects are never surfaced; survivors and their lawyers keep them confidential), therefore trust the ex-Orrick founders + YC/law-firm endorsements rather than marketing or popularity. The ICP is **narrow by design** (Delaware C-corp, venture-track only), and pricing is **one-time, not subscription** — which caps LTV but is congruent with the "do it once, correctly" promise. The companion lines (fundraising/hiring/maintenance) are the retention mechanism — *form here, then "go further" with lifetime access* — and the **free attorney-accounts** surface (40+ private advanced products) is a B2B2C distribution lever that also fixes rivals' formations. Risk: with one-time pricing and a deliberately narrow funnel, top-line growth is roughly **incorporation-volume-bound**.

## Provenance

- **Pages:** homepage, /startups/products, /about, /comparison, /legal-quality, /attorneys analyzed (Firecrawl markdown + full-page screenshots; homepage also rawHtml + branding + structured-layer nav). /pricing scraped but JS-walled (thin); /map gave a 74-URL inventory.
- **Verify:** 7 pages — all `sourceURL`s matched the requested URLs, all body md5s unique (no §5.1 geo/cache contamination).
- **Credits:** 9 spent — 1 map + 7 scrapes + 1 wasted /pricing enhanced-proxy retry (billed 1, not 5 — proxy didn't escalate; returned the identical JS-walled stub, so not retained as a second capture). Logos asset-fetch pass was free (headed icon/cover downloads, no credits).
- **Couldn't get:** per-product à-la-carte prices (not published — only the two packages + "3rd party fees" pass-throughs); the /pricing comparison table as text (JS-rendered, didn't extract — the homepage carries the same table statically, which is where pricing was read).
- **Run profile:** guided — +logos, +offerings (no emphasis).
- **Structured layer:** homepage carried no JSON-LD (`application/ld+json` absent); `socials` (x, linkedin) recovered from footer anchors; `aliases` ("Clerky, Inc.") from the footer legal entity; no `external` records found.
