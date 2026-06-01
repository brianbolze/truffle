---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.0"

# Identity
domain: twilio.com
name: Twilio
aliases: [SendGrid, Twilio SendGrid, Segment, Twilio Segment]
parent: []
owns: ["sendgrid.com", "segment.com"]

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "AEM (Adobe Experience Manager) — rawHtml shows /etc.clientlibs/, cq:, granite, data-cmp (AEM Core Components); branding.designSystem says 'custom' (wrong, as usual). Homepage is dark-themed (near-black navy #000104). www. canonical; /en-us locale prefix on every path. Mega-nav (Products/Solutions/Why Twilio/Resources/Pricing) renders fully in markdown — best source of the offering hierarchy. Verbatim pricing lives on /en-us/pricing (all-products summary) and per-product /pricing pages. Company history + metrics on /en-us/company. Map returned 378 URLs, heavily weighted to /docs, /blog, jobs.twilio.com, investors.twilio.com — filter those for signal pages."
key_pages:
  pricing: /en-us/pricing
  sms_pricing: /en-us/sms/pricing/us
  company: /en-us/company
  platform: /en-us/customer-engagement-platform
  products: /en-us/products
  cpaas: /en-us/cpaas
  conversational_ai: /en-us/products/conversational-ai
  customer_data: /en-us/customer-data-platform
unverified_fields:
  - "Headcount, revenue, funding stage — not on the marketing site (public-company financials live on investors.twilio.com, out of Tier-0 scope)."
  - "Per-message SMS rates by carrier/destination — /en-us/sms/pricing/us captured but rates vary by route; the /en-us/pricing 'starts at' figures are the verbatim anchors used here."

# Description — one sentence
description: "A cloud communications platform (CPaaS) selling developer APIs for SMS, voice, email, and identity verification, plus a customer-data platform (Segment) and AI conversation orchestration, to power cross-channel customer engagement."

# Classification — closed sets
entity_type: Company
target_market: [B2B, B2B2C]
offering_category: [Software / SaaS]
portfolio_shape: Multi-product
business_model: Usage-based / Consumption
primary_industry: Technology

# Visual identity
logo_url: https://www.twilio.com/content/dam/twilio-com/core-assets/social/favicon-32x32.png   # STRAIN: branding.images.logo is an inline data-URI SVG; favicon fallback
brand_colors: { primary: "#B10F23", secondary: "#1866EE", background: "#000104" }   # STRAIN: red is the historic Twilio brand hue; homepage runs dark navy ground w/ red+blue accents (verified in screenshot)
fonts: [Whitney SSm]
color_scheme: dark
design_framework: Adobe Experience Manager (AEM)
---

## Overview

Twilio is a cloud communications platform — the category-defining CPaaS (Communications Platform as a Service) — that sells developers and enterprises programmable APIs to embed messaging, voice, email, video, and user authentication into their own applications. Founded in 2008 to "bring communications to the cloud," it has expanded well beyond raw channels into a unified customer-engagement platform: a customer-data platform (Twilio Segment, acquired 2020), email at scale (Twilio SendGrid, acquired 2019), a contact-center product (Flex), and — its current strategic center of gravity — a suite of AI "Conversations" products that orchestrate context-rich interactions across channels for both human and AI agents. Positions itself for "conversations in the AI era," where AI agents and humans hand off mid-conversation without losing context.

## What they offer

Organized into five families (the site's own nav taxonomy); usage-based pricing, "starts at" rates verbatim from `/en-us/pricing`:

- **Conversations (AI):** the flagship push — **Conversation Orchestrator** (cross-channel threading, $0.0002/1k chars), **Conversation Intelligence** ($0.005/1k chars, Twilio operators), **Conversation Memory** ($0.0028/1k chars + $0.007/recall), **Conversation Relay** (voice AI, $0.07/min), **Enterprise Knowledge** ($0.018/GB-hour)
- **Communications (the core CPaaS):** **SMS/RCS** ($0.0083 to send or receive), **WhatsApp Business API** ($0.005+), **Conversations API** ($0.05/active user/mo), **Voice** ($0.0085/min inbound, $0.014/min outbound), **Elastic SIP Trunking**, **Twilio Video** ($1/active user-hour), **Twilio Flex** contact center ($1/active user-hour or $150/named user/mo), **Phone Numbers** (toll-free, 10DLC, short codes)
- **Email (SendGrid):** **SendGrid Email API** (free 100 emails/day; paid from $19.95/mo), **Twilio Email** ($0.0013/email), **SendGrid Marketing Campaigns** (from $15/mo)
- **Authentication / identity:** **Verify** ($0.05/verification), **Lookup** ($0.01+ per request)
- **Customer Data (Segment CDP):** **Connections** (from $120/mo, 10k visitors), **Unify**, **Engage**, **Protocols**, **Segment CDP** (custom-priced)
- **Builder tools:** **Studio** (drag-drop flow builder, $0.0025/execution), **Functions** (serverless, $0.0001/invocation), **Assets**, **TaskRouter** ($0.06/task after first 100)

## How it works / model

Self-serve, developer-first, pay-as-you-go: sign up for a free trial (no credit card), grab a server-side SDK (Python, C#, PHP, Ruby, Java, JS, curl), and send the first message/call/email "in minutes." The dominant monetization is **usage-based/consumption** — metered per message, minute, verification, email, or API call — with volume discounts at scale and a "no contracts, scale up or down" pitch. Higher tiers (CDP, enterprise, support plans) move to subscription/custom pricing. Free trial → self-serve PAYG → enterprise contract + professional services is the expansion path. Claims a 99.95% uptime SLA with automated failover.

## Positioning & audience

Targets developers and technical teams first ("Built for builders"), then the wider enterprise buyer (data engineering, marketing, product, CX leaders) and verticals (financial services, healthcare, retail, ecommerce, public sector). Competes against CPaaS rivals (Vonage, Sinch, MessageBird/Bird, Bandwidth), CDPs, and increasingly the AI-agent/contact-center stack. Claimed edge: one extensible platform that unifies channels + first-party customer data + AI orchestration, versus stitching point tools together — "the infrastructure behind every magical customer moment." Leans heavily on analyst leadership (Gartner, Omdia, IDC) and developer trust.

## Nav structure

```
- Products — /en-us/products
  - Twilio Platform — /en-us/customer-engagement-platform
  - Conversations — /en-us/products/conversational-ai
    - Conversation Memory — /products/conversational-ai/conversation-memory
    - Conversation Orchestrator — /products/conversational-ai/conversation-orchestrator
    - Conversation Intelligence — /products/conversational-ai/conversational-intelligence
    - Conversation Relay — /products/conversational-ai/conversationrelay
  - Communications — /en-us/cpaas
    - Messaging — /en-us/messaging (SMS, WhatsApp, RCS)
    - Voice — /en-us/voice; SIP Trunking — /en-us/sip-trunking
    - Email — /en-us/products/email-api (SMTP Service)
    - Phone Numbers — /en-us/phone-numbers (Toll-free, 10DLC, Short Codes)
    - Video API — /en-us/video
    - Flex — /en-us/flex
  - Authentication — /en-us/user-authentication-identity
    - Verify — /user-authentication-identity/verify
    - Lookup — /user-authentication-identity/lookup
  - Customer Data — /en-us/customer-data-platform
    - Connections — /products/connections (Warehouses); Protocols — /products/protocols
    - Unify — /products/unify; Engage — /products/engage (Audiences, Journeys)
- Solutions — /en-us/solutions
  - Use Cases: verification & identity, fraud prevention, alerts & notifications, appointment reminders, mass texting, marketing & promotions, SMS marketing, support & sales, IVR, contact center, customer data management
  - Teams: Developers, Data Engineering, Marketing, Product, Customer Experience
  - Industry: Financial services, Healthcare, Retail, Nonprofit, Hospitality, Ecommerce, Public sector, Education
  - Company Size: Enterprise, Startup
- Why Twilio — /en-us/why-twilio
  - One platform, Privacy & security (Trust Center), Built for builders, Enterprise scale, Extensible by design, Real-time customer data, AI — /en-us/ai, Infrastructure — /en-us/global-infrastructure
  - Company: About us — /en-us/company, Values, Diversity, Careers, Twilio.org, Investor relations, Press, Events
- Resources — Documentation — /docs, Code samples — /code-exchange, Developer Hub, Changelog, Blog, Resource Center, Customer stories, State of Customer Engagement
- Pricing — /en-us/pricing (per-product pricing pages for every line above)
```

## Credibility & proof

- **Analyst leadership:** Named a Leader in the 2026 Gartner® Magic Quadrant™ for CPaaS (positioned highest for Ability to Execute); Leader in Omdia Universe: CEP; Leader in IDC MarketScape: Worldwide CPaaS
- **Scale metrics (from /company, "as of September 30, 2025"):** "180+ countries and territories," "400 patents filed," "392K+ customers" (active accounts)
- **Customer logos + outcomes:** IBM ("30% increased product adoption"), Toyota ("13% after call work reduction"), Lyft ("30M interactions weekly"), Resy ("21M+ messages sent monthly"), Delivery Hero ("60% fewer escalations"), SMAVA, OhMD, Posh
- **Reliability:** "99.95% uptime SLA … automated failover and zero maintenance windows"
- **Public company:** dedicated investors.twilio.com (SEC filings, 10-K/10-Q), CEO Khozema Shipchandler; ISO 27001 certified
- **Social impact:** Twilio.org — "$4.8M awarded … in 2024," "25,000+ social impact organizations," "716M+ people reached"

## Visual & brand impression

A confident, enterprise-grade dark theme: near-black navy ground (#000104) with Twilio's signature red (#B10F23) and electric blue (#1866EE) accents, set in the Whitney typeface. The homepage is a long, cinematic scroll — product-mockup imagery of AI-mediated customer conversations (car dealerships, hotel booking, support flows), an interactive product grid with hover states, a scrolling customer-logo wall with stat call-outs, and analyst-badge proof blocks. Polished, dense, and clearly resourced — the design of a mature public company repositioning around AI ("the platform for conversations in the AI era") rather than a scrappy developer tool, though the "Build. Without limits." SDK code-snippet section keeps the developer-first DNA visible.

## Strategic read

The capture catches Twilio mid-pivot. The historic identity — programmable SMS/voice APIs, the developer's communications toolbox — is now framed as the substrate beneath a higher-margin AI orchestration layer ("Conversations") that is given top billing in nav, homepage hero, and pricing. The two big acquisitions (SendGrid, Segment) are folded in as first-class families rather than separate brands, and the whole platform is narrated as one continuous, context-preserving conversation across channels and across the human↔AI-agent boundary — a direct bid to own the emerging "agentic" customer-engagement stack and to defend commoditizing messaging margins with stickier AI + data products.

## Provenance

- **Pages:** 6 captured via Firecrawl (`fc.py`, all-formats homepage + 5 key pages) — homepage, /en-us/pricing, /en-us/sms/pricing/us, /en-us/company, /en-us/customer-engagement-platform, /en-us/products. Plus a 378-URL map. Nav + product breadth synthesized from homepage mega-nav; pricing verbatim from /pricing; history/metrics/leadership from /company.
- **Verify:** All 6 sourceURLs matched; all body md5s unique (no geo/cache contamination). All HTTP 200.
- **Credits:** 7 (1 map + 6 scrapes, all base 1cr, basic proxy).
- **Couldn't get:** Financials/headcount (public-company data, out of Tier-0 scope → investors.twilio.com). Per-route SMS rate tables (vary by carrier/destination; "starts at" anchors used instead).
