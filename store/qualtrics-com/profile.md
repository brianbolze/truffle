---
schema_version: 1

# Identity
domain: qualtrics.com
name: Qualtrics
aliases: []
parent: []
owns: ["Press Ganey Forsta"]   # STRAIN: homepage banner announces "Qualtrics acquires Press Ganey Forsta"; no resolvable standalone domain captured, recorded as name (un-joinable until it earns a slug)

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "qualtrics.com → www.qualtrics.com (301). Site is DRUPAL (theme 'arcadia'; assets under /sites/default/files/, /modules/custom/, favicon /themes/custom/arcadia/favicon.ico). PATH TRAPS — several obvious guesses are 404 Marketo-Forms proxy stubs (recognizable: mdlen ~5.3k, body 'This page is used by Marketo Forms 2 to proxy cross-domain Ajax requests'): the third pillar is /market-research (NOT /research → 404); AI has no standalone page (/platform/ai → 404; AI content lives inside /platform); company page is /about (NOT /about-qualtrics → 404). Real pillars: /customer-experience, /employee-experience, /market-research; platform at /platform; pricing at /pricing; company at /about. Map is useless — returns ~100–480 URLs that are ~all /articles/* blog/news + /articles/author/* (drop entirely); nav comes from homepage links. Pricing = custom-quote only ('Request Pricing' / 'Request Suite Pricing'), pricing metric is 'Interactions', no public $ figures; three suites: XM for Customer Experience / Employee Experience / Strategy & Research."
key_pages:
  homepage: /
  platform: /platform
  customer_experience: /customer-experience
  employee_experience: /employee-experience
  market_research: /market-research
  pricing: /pricing
  about: /about
unverified_fields:
  - "Pricing — no public list prices; /pricing is custom-quote ('Request Pricing') metered on 'Interactions'. Tier/seat figures not determinable from the site."
  - "Founding year/founders, HQ, headcount, revenue, ownership structure — not present on any captured page (the /about page is culture/values + careers, not company facts). Deep-research job, not capture."
  - "Press Ganey Forsta acquisition is announced as a homepage banner (state of the platform), but deal terms/close/structure are events — out of scope here."

description: "An enterprise SaaS platform for Experience Management (XM) — AI-powered listening, analytics, and automated action across customer experience, employee experience, and market research, unifying survey, digital, and conversational feedback in one system."

# Classification
entity_type: Company
target_market: [B2B, B2G]
offering_category: [Software / SaaS]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://www.qualtrics.com/modules/custom/nav_service/images/main_logo/qualtrics-logo-white.svg
brand_colors: { primary: "#0768DD", secondary: "#5F1AE5", background: "#EDF2F4", text: "#1E1E1E" }  # STRAIN: screenshot-confirmed — a blue (#0768DD) + purple (#5F1AE5/#601AE5) gradient identity on light ground; both hues are load-bearing across hero/CTAs.
fonts: [Helvetica Neue, qualtrics-text, bento-sans]
color_scheme: light
design_framework: Drupal (custom "arcadia" theme; /sites/default/files/, /modules/custom/, Marketo + Adobe Launch tags)
---

## Overview

Qualtrics is the company that created **Experience Management (XM)** — "the technology platform that organizations use to collect, manage, and act on experience data," with "20,000+ brands rely[ing] on us to close experience gaps." It sells one AI-heavy platform across three solution pillars — **Customer Experience**, **Employee Experience**, and **Market Research** — that capture feedback and signals across channels (surveys, digital, contact center, conversations), apply AI to surface meaning, and drive automated action. Its 2026 positioning leans hard on connected intelligence and "Experience Agents," and the homepage headlines its acquisition of **Press Ganey Forsta** ("World's largest Experience Management (XM), AI & data platform"). Brand line: *"We're for breakthrough experiences and those bold enough to chase them."*

## What they offer

One platform, three solution pillars (sold as "XM for…" suites), all enterprise SaaS, custom-quote, metered on **Interactions**.

- **Customer Experience (CX) — /customer-experience:** "Make an unbreakable connection with customers." Products include Voice of Customer, Omnichannel Experience Management, Website & Mobile App Feedback, Digital Experience Analytics, Contact Center Analytics, Quality Management & Compliance, Agent Coaching, Online Reputation Management, Location Experience Hub.
- **Employee Experience (EX) — /employee-experience:** "Close the gap between listening and leading." Products include Employee Engagement, 360 Development Feedback, Employee Lifecycle (onboarding & exit), candidate/lifecycle feedback.
- **Market Research — /market-research:** "Uncover insights at the speed of change." Market & Audience Understanding, Product & Innovation Research, User Experience Research; pitches "synthetic audiences" / research-grade LLMs for fast validation. (The pricing page labels this suite "XM for Strategy & Research.")
- **XM platform — /platform:** "Make every experience count." Cross-pillar capabilities: conversational feedback, text analytics insights & recommendations, frontline/location intelligence, dashboards, integrations — "specialized, secure and trusted."
- **Qualtrics AI:** "Powerful AI for knowing what matters, and acting when it counts" — Experience Agents (automated responses), text analytics, AI recommendations. No standalone page; woven through /platform and every pillar.
- **XM Institute — /xm-institute:** Built-in frameworks, benchmarks, and playbooks (experience-management expertise).

## How it works / model

Enterprise B2B/B2G subscription SaaS, sales-led. Buyers reach the platform via **Request Demo / Request (Suite) Pricing**; pricing is tailored per suite + product mix and metered on **Interactions** (pooled across channels, volume-discounted — "no additional contracts needed to unlock another channel"). A free survey tier is the self-serve on-ramp. The company's own loop is **Listen** (every signal across surveys, calls, digital, service) → **Understand** (automated text analytics — themes, sentiment, risk) → **Act** (Experience Agents and workflows that move insight to action "while the moment still matters"). Revenue is recurring suite subscription, expanded across CX/EX/MR product lines and AI add-ons.

## Positioning & audience

Targets large enterprises and the public sector — "Global enterprises, healthcare systems, and governments rely on Qualtrics." Industry solutions: Healthcare, Financial Services, Government, Education, Travel & Hospitality, Retail. Pitched by team (CX professionals, research teams, product, digital, HR) and use case (churn, CLV, NPS/CSAT, engagement, operational excellence, revenue growth, time-to-market). Claimed edge: it created the XM category, offers one connected platform spanning customer + employee + research that disconnected point tools can't match ("Most companies track experience with disconnected tools. The best ones compete on experience with Qualtrics."), and built-in, trustworthy AI grounded in real human behavior.

## Nav structure

```
- Products
  - Customer Experience — /customer-experience
    - Voice of Customer — /customer-experience/voice-of-customer
    - Omnichannel Experience Management — /customer-experience/omnichannel
    - Location Experience Management — /customer-experience/locations
    - See all CX products — /customer-experience/capabilities
  - Employee Experience — /employee-experience
    - 360 Development Feedback — /employee-experience/360-degree-feedback
    - Employee Engagement — /employee-experience/employee-engagement
    - Employee Onboarding & Exit — /employee-experience/employee-lifecycle
    - See all EX products — /employee-experience/capabilities
  - Market Research — /market-research
    - Market & Audience Understanding — /market-research/research
    - Product & Innovation Research — /market-research/product-research
    - User Experience Research — /market-research/ux
    - See all MR products — /market-research/capabilities
  - Platform — /platform   (Security — /platform/security)
- Solutions
  - By industry — /industries (Healthcare, Financial services, Government, Education, Travel & hospitality, Retail)
  - By team — /teams (CX professionals, Research teams, Product research, Digital, Human resources)
  - By use case — /use-cases (churn, CLV, NPS/CSAT, engagement, high-performing culture, operational excellence, revenue growth, research cost/quality, product innovation)
- Resources
  - Popular: Product demo, Webinars, Customer stories, Blog, News, Events
  - Company: About — /about, Careers, Marketplace, Integrations, Partners, Trust center
  - X4 Summit — /x4summit (X4 2026, on demand, session catalog)
- Pricing — /pricing
- Support (Experience Community, Customer success hub, Developer resources, Product docs, Training & certification, System status)
```

## Credibility & proof

- **Analyst recognition (verbatim):** "Leader in the Gartner® Magic Quadrant™ for Voice of the Customer report for the fifth consecutive year" (2026); "Leader in The Forrester Wave™: Employee Experience Management Platforms report for 2025"; "Strong Performer in The Forrester Wave™: Experience Research Platforms, Q1 2026" (debut).
- **Customer outcomes (homepage cards):** Shake Shack — "30% increase in likelihood to recommend, 17% increase in Shack locations"; Samsara — "2X ARR growth, 30% fewer support tickets"; Gabb — "50% lower costs vs traditional research, 98% faster time to insights"; ServiceNow — "17 connected programs, 10K+ automatic follow-up actions"; Indiana University Online — "17.3% YOY enrollment increase, 95% satisfaction increase."
- **Scale / category claim:** "20,000+ brands rely on us to close experience gaps" (/about); "World's largest Experience Management (XM), AI & data platform" (Press Ganey Forsta banner).
- **Trust:** "Trust is not a feature. It's our track record." — security/compliance badges (ISO etc.); "Global enterprises, healthcare systems, and governments rely on Qualtrics."

## Visual & brand impression

Bold, high-saturation enterprise-SaaS design — a blue (`#0768DD`) and purple (`#5F1AE5`/`#601AE5`) gradient system on a light ground (`#EDF2F4`), dark near-black ink (`#1E1E1E`), set in Helvetica Neue plus custom "qualtrics-text"/"bento-sans" display faces. The long homepage scroll alternates saturated full-bleed gradient bands with crisp product-UI mockups (AI agents drafting replies, signal dashboards tagging Friction / Loyalty risk / Billing), a customer-logo + metric wall, and an industry tab carousel. It reads as a confident, well-funded category leader — heavy on AI proof and product screenshots, light on whitespace minimalism; energetic rather than austere.

## Strategic read

- **Culture as recruiting surface:** /about is values + careers, not corporate facts — five stated values (Transparent, All-in, Customer Obsessed, One Team, Scrappy) and "Just because we're a global enterprise doesn't mean we have to always act like one." Signals a still-founder-flavored, high-ownership culture at enterprise scale.
- **5 For The Fight:** Company-sponsored movement asking everyone to give $5 to the fight against cancer; Qualtrics donates its NBA Utah Jazz jersey patch to the cause rather than running its own logo — an unusually concrete brand/CSR signature.
- **AI is the whole 2026 story:** "Experience Agents," synthetic-audience research, and AI recommendations are foregrounded on every pillar — the company is repositioning XM around agentic AI and a proprietary human-sentiment data moat, now compounded by the Press Ganey Forsta acquisition (healthcare experience data).

## Provenance

- **Pages:** Analyzed 7 content pages (firecrawl, maxAge:0 + location:US): homepage, /platform, /customer-experience, /employee-experience, /market-research, /pricing, /about.
- **Verify:** All content pages src✓ and md5-unique. (One benign DUP-BODY flag = /customer-experience scraped twice — same URL, identical body, not cross-URL contamination.)
- **Credits:** 13 total — 1 map + 12 scrapes; of the scrapes, 7 yielded content (homepage, /platform, /customer-experience, /employee-experience, /market-research, /pricing, /about), 4 were Marketo-proxy 404s from path guesses now corrected (/research, /platform/ai, /about-qualtrics, /why-qualtrics), and 1 was a duplicate /customer-experience. All basic proxy, 1/call.
- **Couldn't get:** Public pricing (custom-quote, metered on Interactions); HQ/headcount/revenue/ownership (founding year + founders captured from /about; rest not on site); Press Ganey Forsta deal specifics (event, out of scope).
