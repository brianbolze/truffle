---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: 1

# Identity
domain: upwork.com
name: Upwork
aliases: []
parent: []
owns: ["go-lifted.com"]              # STRAIN: Enterprise rebranded to "Lifted, an Upwork Company" (Aug 2025); own domain, nav points there

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Cloudflare-fronts the root (curl 403; Firecrawl passes clean). Marketing pages are Webflow (assets on cdn.prod.website-files.com). Every marketing page renders the FULL mega-nav — hundreds of /hire/<skill> and /freelance-jobs/<skill> category links that drown grep; strip lines matching `upwork.com/(hire|freelance-jobs)/` to reach substantive content. Client pricing is at /pricing/client (table + FAQ); freelancer-side fees not on it. Enterprise (/enterprise/) now redirects to the Lifted brand (go-lifted.com)."
key_pages:
  about: /about
  pricing_client: /pricing/client
  how_it_works: /i/how-it-works/client/
  talent_marketplace: /talent-marketplace/
  project_catalog: /services/
  business_plus: /business-plus/
  enterprise: /enterprise/
  impact: /about/our-impact
unverified_fields:
  - "Freelancer-side (supply) fees and Freelancer Plus / Connects pricing — only the client pricing page was captured."
  - "Per-skill or category-level rate variation beyond the headline service fees."
  - "Founding date / corporate history — not stated on captured pages (CEO bio gives 2011 join, not company founding)."

# Description — one sentence
description: "A two-sided online work marketplace connecting businesses with freelance and increasingly AI-augmented independent professionals across 180 countries, monetized via service fees on each contract through self-serve, Business Plus, and enterprise (Lifted) tiers."

# Classification
entity_type: Company
target_market: [B2B, B2C]
offering_category: [Marketplace / Platform]
portfolio_shape: Multi-product
business_model: Marketplace / Commission
primary_industry: Technology

# Visual identity
logo_url: https://www.upwork.com/favicon.ico   # branding.images.logo is an inline data-URI; favicon fallback
brand_colors: { primary: "#108A00", accent: "#D2FF00" }   # signature Upwork green + lime accent, confirmed against screenshot
fonts: [Neue Montreal, Helvetica Neue]
color_scheme: light
design_framework: webflow   # marketing site (cdn.prod.website-files.com); the logged-in product app is a separate stack, not captured
---

## Overview

Upwork is the self-described "world's human and AI-powered work marketplace" — a two-sided platform where businesses (Fortune 100 down to small companies) post jobs and hire independent professionals across 180 countries. It spans the full hiring journey: an open Talent Marketplace where clients post jobs and review proposals, a fixed-scope Project Catalog, on-demand expert Consultations, a premium Business Plus tier with vetted talent, and an enterprise contingent-workforce offering now branded **Lifted**. Upwork makes money by taking a service fee on the payments clients make to freelancers. It is a public company (NASDAQ: UPWK).

## What they offer

Several distinct hiring modalities and tiers, all riding one marketplace and supply pool of **18+ million freelancers** (per pricing page):

- **Talent Marketplace (Basic):** the core open marketplace — post a job free, get proposals, hire. "Free to get started—pay only when you hire." **5% service fee** (3% for eligible U.S. clients paying by checking account) + a one-time contract initiation fee of **$0.99–$14.99** per contract.
- **Business Plus:** premium plan with access to "the top 1% of Upwork talent" (Expert-Vetted), talent badges, and Talent Performance / Contract Audit reports. **10% service fee** (8% for eligible U.S. checking-account clients); free to join, runs on a 30-day membership cycle; no contract initiation fee except on fixed-price contracts ≤ $100.
- **Project Catalog:** browse and buy predefined, fixed-scope/fixed-price projects ("services") rather than posting a custom job — at /services/.
- **Consultations:** book one-off paid expert advice sessions — at /services/consultations/.
- **Enterprise → Lifted:** "one solution built for enterprises to source, contract, and pay contingent talent," combining the platform, the talent pool, and global compliance with a dedicated program team. Rebranded **"Lifted, an Upwork Company™"** (announced Aug 19, 2025; GM Ernesto Lamaina). Roadmap adds enhanced worker Classification, direct **Employer of Record (EOR)**, and full **Staff Augmentation**.
- **Direct Contracts / BYO:** bring talent sourced off-platform onto Upwork to contract and pay them in one place (subject to the marketplace fee).
- **Freelancer Plus:** paid membership on the supply side (Connects, profile perks) — referenced but not priced in this capture.

## How it works / model

Client journey: **post a job (always free)** → Upwork matches relevant freelancers from project details (skills, scope, budget, timeline) and surfaces suggested candidates → **review proposals, message, and hire** → **pay when work is done**, with escrow, payment protection, and dispute resolution. Buyers can instead buy a fixed-scope Project Catalog package or book a Consultation. Revenue is **commission-based**: Upwork charges the client a service fee on every payment to a freelancer (3–5% Basic, 8–10% Business Plus), plus per-contract initiation fees and supply-side memberships. The pitch is increasingly AI-forward — "Hire experts who use AI to amplify their talent" — and the product surfaces AI job-post generation and matching.

## Positioning & audience

- **Audience:** dual — businesses needing flexible/contingent talent (the paying clients, from solo founders to enterprises) and the independent professionals who supply the work. Enterprise (Lifted) explicitly targets large contingent-workforce programs.
- **Claimed edge:** scale and trust — 18M+ vetted freelancers across 180 countries, verified identity/location, transparent track records and reviews, escrow + payment protection, and an Expert-Vetted top-1% tier for higher-stakes work.
- **Tagline:** "Work at the speed of your ambition" (homepage hero); mission: "We create opportunity in every era of work."
- **Competes against** other talent marketplaces/staffing (e.g. Fiverr, Toptal, traditional staffing agencies and MSPs); Lifted pushes upmarket into EOR/staff-aug territory.

## Nav structure

```
- Hire talent (mega-menu by category)
  - AI & Automation, Development & IT, Design & Creative, Marketing,
    Data & Analytics, Admin & Customer Support, Finance & Accounting,
    Legal, HR & Training, Engineering & Architecture, Writing & Translation
    (each → dozens of /hire/<skill> and /freelance-jobs/<skill> pages)
- Find work — /i/how-it-works/freelancer/  (freelancer side: Direct Contracts, Freelancer Plus)
- Why Upwork
  - Success stories — /success-stories
  - Reviews — /reviews
  - How to hire — /i/how-it-works/client/
  - How to find work — /i/how-it-works/freelancer/
- Pricing — /pricing/client
- Enterprise — go-lifted.com  (Lifted)
- Ways to hire: Talent Marketplace — /talent-marketplace/ · Project Catalog — /services/ ·
  Consultations — /services/consultations/ · Business Plus — /business-plus/ ·
  Direct Contracts — /direct-contracts · Enterprise — /enterprise/
- Resources — /resources · Blog — /blog · Release notes — /product-release-notes
- About — /about (Team /about/team, Our impact /about/our-impact, Contact /about/contact)
```

## Credibility & proof

- **Scale (from CEO bio on /about):** Upwork grew from $10M to **>$750M annual revenue** and from $100M to **>$4 billion in annual client spend**; ~**2,000 team members** (~75% freelancers working remotely). 18M+ freelancers, 180 countries.
- **Public company:** trades as NASDAQ: **UPWK**; CEO **Hayden Brown** (CEO since Jan 2020, joined 2011); board includes Benchmark's Kevin Harvey and Redfin CEO Glenn Kelman.
- **Client logos (homepage "Trusted by"):** Microsoft, Airbnb, Cloudflare, Databricks, Scale AI, Grammarly, Glassdoor, Bissell, BambooHR, Shutterstock.
- **Trust mechanics:** verified freelancer identity/location, public reviews and track records, talent badges, escrow + payment protection + dispute resolution, Expert-Vetted top-1% screening.
- **Promo:** "$500 in credit when you spend $1,000" (Business Plus).
- **The Upwork Foundation:** funds initiatives connecting marginalized communities with knowledge work ("close the global opportunity gap").

## Visual & brand impression

Polished, confident, modern-tech aesthetic. Light theme on white with the signature **Upwork green (#108A00)** for icons/CTAs and a punchy **lime (#D2FF00)** accent, set against a dark near-black hero and footer. Clean sans-serif type (Neue Montreal / Helvetica Neue), generous whitespace, flat line-icon category grid, and soft green gradient flourishes. The design reads as an established public-company marketplace — trustworthy and scaled rather than scrappy — with an AI-amplification narrative threaded through recent copy ("Work at the speed of your ambition").

## Strategic read

The most notable shift in this capture is the **enterprise pivot to "Lifted"** — rebranding the enterprise arm as a standalone-feeling company (own domain go-lifted.com) and explicitly building **EOR, classification, and staff-augmentation** capability. That moves Upwork from a self-serve freelance marketplace toward the regulated, higher-ACV contingent-workforce / MSP space, competing with staffing platforms and EOR providers, not just Fiverr-style marketplaces. Simultaneously the consumer-facing copy leans hard into **AI-augmented talent** as the differentiator. The two-tier fee structure (3–5% vs 8–10%) is the clearest monetization lever, with the U.S.-checking-account discount nudging payment-method choice.

## Provenance

- **Pages:** 7 analyzed via Firecrawl (maxAge:0, location:US, all-formats) — homepage, /about, /pricing/client, /enterprise/, /i/how-it-works/client/, /talent-marketplace/, /about/our-impact; plus map. Screenshots reviewed for the visual read.
- **Verify:** `fc.py verify` — all 7 sourceURLs matched, all bodies md5-unique (no contamination).
- **Credits:** 8 (1 map + 7 scrapes); no enhanced-proxy retries needed.
- **Couldn't get:** freelancer-side pricing (Connects/Freelancer Plus) and per-category rates — not on the client pricing page; founding date/history — not stated on captured pages.
