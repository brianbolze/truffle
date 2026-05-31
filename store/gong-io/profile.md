---
schema_version: 1

# Identity
domain: gong.io
name: Gong
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Next.js (turbopack, served under /marketing-assets/_next/) on a Sanity CMS; logos + most imagery on cdn.sanity.io. Animated stat counters render in markdown as vertical digit columns (`- 0 1 2 … . , + % b $`) — headline metrics (customers, employees, FORTUNE-10 %, ARR, G2 score) are NOT legible from md; read them off the screenshot. A/B: yes (no tool fingerprinted) — hero headline rotates (md captured 'Close deals faster'; the shot showed 'Predict pipeline risk'). Pricing is quote-only behind a multi-step team-size form — no dollar figures published. Storylane interactive demos + Marketo forms embedded. Map returned 466 URLs but ~85% noise (/blog ×132, /docs ×86, /fr+/de locales); the real product catalog + nav came from homepage links/footer, not the map."
key_pages:
  platform: /platform
  gong_ai: /platform/revenue-ai
  ai_agents: /platform/ai-agents-for-revenue-teams
  pricing: /pricing
  solutions: /solutions
  why_gong: /why-gong
  about: /about
  customer_proof: /customer-proof
unverified_fields:
  - "Headline counters (customer count, employee count, FORTUNE-10 %, partner count, G2 star rating, Forrester 'Nx leader') render as animated digit-column noise in markdown — only the '5,000+ customers' / '6,200+ G2 reviews' / '$500M+ ARR, 55% YoY' figures were legible (from copy/press link), not the rest."
  - "Pricing — quote-only. Model is stated (per-user licenses + a user-count-based platform fee; integrations free) but no dollar amounts are published; gated behind a sales form."
  - "Captured homepage copy is a point-in-time snapshot, not fixed — a rotating hero headline + A/B-toggled modules shift it run-to-run."

# Description
description: "A revenue-intelligence SaaS platform that captures and analyzes B2B sales calls, emails, and deals, then applies purpose-built AI models and agents to coach reps, forecast pipeline, and automate revenue workflows for enterprise GTM teams."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://cdn.sanity.io/images/ww20clc6/production/0b50133901322a215dfcf2f3311fc378ffdaacd6-117x42.svg
brand_colors: { primary: "#3E0075", accent: "#FD63FE" }   # STRAIN: deep royal purple + magenta accent, both confirmed on the screenshot
fonts: [Inter, Inter Tight]
color_scheme: light
design_framework: next.js
---

# Gong

## Overview
Gong sells a "Revenue AI OS" — an enterprise platform that automatically captures every customer interaction (calls, meetings, emails) across a revenue team's stack, unifies it into a proprietary data layer, and runs AI over it to surface coaching insights, score and forecast deals, and automate seller workflows. It began as conversation/revenue intelligence (call recording + analysis) and has expanded into a multi-app, agent-driven platform spanning the full revenue lifecycle. Buyers are enterprise go-to-market organizations — sales leadership, RevOps, frontline sales, customer success, and enablement.

## What they offer
A single platform marketed as the **Gong Revenue AI OS**, composed of distinct, separately-positioned modules plus an agent layer:
- **Gong Revenue Graph:** the data foundation: auto-captures and connects every interaction across the business.
- **Gong AI / Conversation Intelligence:** analysis over "billions of buyer-seller interactions" using "40+ proprietary AI models" and "300+ signals."
- **Gong Engage:** sales engagement / prospecting (GenAI email composer, prioritized workflows) — competes with Salesloft/Outreach.
- **Gong Forecast:** pipeline & forecasting (deal likelihood scores, deal/forecast dashboards) — competes with Clari.
- **Gong Enable:** revenue enablement, coaching, and AI Trainer role-play — grounded in real customer calls.
- **Gong Agents:** ~18 named specialized agents (AI Tracker, Ask Anything, Briefer, Call Reviewer, Trainer, Composer, Deal Reviewer/Monitor/Predictor, Revenue Predictor, Activity Mapper, Transcriber, Translator, Data Extractor; AI Deep Researcher "coming soon"), built and tuned in a no-code **Agent Studio** (drag-and-drop, "no IT resources required").
- **Gong Collective:** 300+ integrations + services marketplace (Salesforce, Zoom, MS Teams, Slack, Okta, MS 365 Copilot).

## How it works / model
Capture → unify → intelligence → automate. Gong ingests interactions via integrations (Zoom, Teams, Salesforce, etc.), maps them to the Revenue Graph, then AI models + agents generate insights, forecasts, and actions that flow back into seller and manager workflows. Sold as **seat-based subscription**: "Licenses are priced per user" plus "a platform fee based on the number of users supported," with integrations free. Enterprise, sales-led motion — pricing is quote-only behind a team-size form (brackets: 1–50, 51–1,000, 1,001–9,999, 10,000+). A newer **Gong Credits** consumption model (referenced in a May 2026 blog) layers usage-based AI pricing on top of seats.

## Positioning & audience
Positions as the "**#1 AI OS for Revenue Teams**" and an "undisputed leader in revenue AI" — reframing the older "revenue intelligence" category it helped create into an agentic operating system. Targets enterprise GTM teams by **role** (CRO/revenue leadership, RevOps, Sales, Customer Success, Enablement) and by **industry** (Technology, Financial Services, Healthcare, Manufacturing). Claimed edge: the largest dataset of buyer-seller interactions, proprietary models tuned for revenue, enterprise-grade security/compliance, and platform **consolidation** (one system replacing point tools for CI, forecasting, and engagement).

## Nav structure
```
- Product
  - Product Overview — /platform
  - Gong AI — /platform/revenue-ai
  - Gong Agents — /platform/ai-agents-for-revenue-teams
  - Gong Engage — /platform/sales-engagement-software
  - Gong Forecast — /platform/revenue-forecasting-software
  - Gong Enable — /platform/sales-enablement-software
  - Gong Revenue Graph — /platform/revenue-graph
  - Partners & Integrations (Gong Collective) — https://collective.gong.io/
  - Trust — /platform/trust
  - Pricing — /pricing
- Solutions
  - By role: Leadership — /solutions/revenue-leadership · RevOps — /solutions/revenue-operations ·
    Sales — /solutions/sales · Customer Success — /solutions/customer-success · Enablement — /solutions/revenue-enablement
  - By industry: Technology — /solutions/tech · Financial Services — /solutions/financial-services ·
    Healthcare — /solutions/healthcare · Manufacturing — /solutions/manufacturing
  - Solutions hub — /solutions
- Innovation — /innovation
- Raving fans (proof) — Customer stories — /case-studies · Customer proof — /customer-proof
- Resources — Product tour — /platform-tour · Resource library — /resources · Blog — /blog ·
  Gong Labs — /blog?blogType=Gong+Labs · Events — /events · FAQs — /faqs · Revenue AI glossary — /revenue-intelligence-sales-glossary
- Company — About — /about · Newsroom — /press · Careers — /careers · Media kit — /media-kit · Contact — /contact-us
- Sign in — https://app.gong.io/ · Book a demo — /demo
```

## Credibility & proof
- **Scale:** "Trusted by 5,000+ customers"; homepage claims a share of "the FORTUNE 10 run on Gong." Press banner: "Gong growth accelerates past 55% YoY, ARR tops $500M."
- **Named logos:** LinkedIn, Google, Dropbox, ADP, Nasdaq, Upwork, Canva, Crayon, HubSpot, Uber for Business, Sprout Social, SurveyMonkey, Kelly, PitchBook.
- **Analyst/review badges:** "3x Leader" (Forrester Wave™), Gartner 4.8, **G2 4.8 across 6,278 reviews**, TrustRadius 9.2; "Great Place to Work" winner.
- **Customer-evidence library** (UserEvidence-sourced, on /customer-proof): 4,436 testimonials, 6 survey stats, 11 chart-backed findings, most recent verified May 29, 2026. Representative stat: "50% of Gong users decreased average time to ramp by greater than 10%." Customer-cited outcomes include Uber for Business saving "6,700 hours" and a "32%" lift in buyer response rates via the AI Tracker agent.

## Provenance

- **Pages:** homepage, /platform, /platform/revenue-ai, /platform/ai-agents-for-revenue-teams, /pricing, /solutions, /why-gong, /about, /customer-proof (9) — all Firecrawl, `maxAge:0`, `location:US`; `design_framework` from `rawHtml` (`_next/static` + turbopack → Next.js), not `branding.designSystem` (which said "tailwind").
- **Verify:** all sourceURL-matched and md5-unique (clean).
- **Credits:** not recorded this run.
- **Couldn't get:** legible values for animated stat counters (rendered as digit-column artifacts — see `unverified_fields`); any actual price (quote-only); per-module deep detail beyond what the platform/agents pages list.

## Visual & brand impression
Polished, high-budget enterprise-SaaS aesthetic. A predominantly light canvas (white → soft lavender feature cards) anchored by a deep royal-purple (#3E0075) and bright magenta (#FD63FE) brand palette, with deep-purple full-bleed sections and a near-black purple footer. Recurring motifs: a purple "star/sparkle" badge (the AI mark) and the literal gong/"ring the gong" metaphor. Clean Inter / Inter Tight type, generous whitespace, modular card grids, and animated counters and squiggle accents that read as confident and modern rather than playful. Overall: a category-leader presentation built to sell to enterprise revenue executives.

## Strategic read
The site documents an active repositioning: from **conversation intelligence** (call recording + analysis, Gong's origin) to an **agentic "Revenue AI OS."** The tells are everywhere — the "AI OS for Revenue Teams" headline, a roster of ~18 named agents with a no-code **Agent Studio**, the Revenue Graph framed as a data moat ("world's richest revenue graph"), and a nascent **Gong Credits** consumption-pricing layer alongside seats. This is a land-and-expand platform play: lead with CI, consolidate forecasting (vs. Clari) and engagement (vs. Salesloft/Outreach), then monetize AI usage on top of seat licenses. Founder origin story (CEO Amit Bendov + CPO Eilon Reshef, "worst quarter ever → use AI to hear customers") and a US-HQ'd (San Francisco) / Tel-Aviv-R&D footprint round out a late-stage, pre-IPO-profile enterprise vendor.
