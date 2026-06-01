---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.0"

# Identity
domain: typeform.com
name: Typeform
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Marketing site on Webflow (cdn.prod.website-files.com; wf-/data-wf- in rawHTML) — app lives at admin.typeform.com. Map returns ~480 URLs dominated by /blog/*, /es + /fr locale dupes, and per-form respondent subdomains (*.typeform.com/to/…) — filter hard. Logo is an inline SVG data-URI → favicon fallback. Pricing page is ~2,500 lines (full feature matrix); plan cards sit near the top. Sitemap exposes pricing test pages (/pricing-script-test, /pricing-copy-3) — list prices are A/B'd; treat as point-in-time."
key_pages:
  platform_overview: /platform-overview
  pricing: /pricing
  ai: /ai
  growth_flow: /growth
  research_flow: /research-flow
  about: /about-us
unverified_fields:
  - "Prices/plan lineup are a point-in-time snapshot, not fixed — SaaS list prices revised periodically and the sitemap shows live pricing test pages (/pricing-script-test, /pricing-copy-3)."
  - "'Founded 2012' and '250+ employees' are /about-us self-reports; not independently verified."

description: "A SaaS form and survey platform that builds conversational, on-brand forms, quizzes, and surveys with AI, then layers lead-capture automation and AI-moderated research on top of the responses it collects."

# Classification
entity_type: Company
target_market: [B2B, B2C]
offering_category: [Software / SaaS]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://cdn.prod.website-files.com/66ffe2174aa8e8d5661c2708/68b6f02860110a77834d228b_favicon.ico  # STRAIN: site logo is an inline SVG data-URI; favicon fallback
brand_colors: { primary: "#3E3040", accent: "#D258FE", secondary: "#DDB7F0" }  # STRAIN: aubergine canvas + vivid purple accent; bright lime CTA seen in screenshot but not in payload palette
fonts: [TWK Lausanne]
color_scheme: dark  # STRAIN: homepage + footer are dark aubergine; inner pages (pricing, platform-overview) run light
design_framework: webflow
---

## Overview

Typeform builds "people-friendly" online forms — one question at a time, conversational, heavily designed — and positions them as a way to collect **up to 3.5x more data** than traditional forms. The 2026 site reframes the product around AI and automation: the tagline is *"Your favorite forms. Now with AI automation."* Three pillars structure the offering — **ASK** (AI-built Intelligent Forms), **ACT** (Growth Flow, lifecycle automation), and **LEARN** (Research Flow, AI-moderated research). It serves 150,000+ businesses and claims 48M+ responses collected monthly. Same no-code builder underneath forms, surveys, quizzes, polls, tests, NPS, landing pages, and application forms.

## What they offer

One flagship builder, two newer "Flow" companion products, plus an AI layer that spans all three:

- **Intelligent Forms (flagship):** the conversational AI form/survey/quiz builder — 3,000+ templates, branching logic, custom branding, video questions & answers, 300+ integrations. Surfaces as Form builder, Survey maker, Quiz maker, Test maker, Poll builder, NPS/Registration/Application/Landing-page builders.
- **Typeform AI:** cross-cutting AI layer in three families — **Creator AI** (AI Form Builder, Form Import, Brand Kit, Translation in 25+ languages, Content Optimizer), **Interaction AI** (Clarify with AI — adaptive interview-style follow-ups), **Insights AI** (Ask AI, qualitative + quantitative analysis). Powered by Anthropic, OpenAI, and AWS models; "none of your data is used to train these models."
- **Growth Flow (companion, "New"):** AI customer-lifecycle automation — instant lead capture (e-signature, Calendly/Google Calendar scheduling, Stripe/PayPal payments in-form), AI data enrichment (~80% of leads; match rates "up to 92% for B2B, 71% for B2C"), and SMS/email follow-up automations. Bundles the former *Contacts & Automations* add-on.
- **Research Flow (companion, "New"):** combined qual + quant research platform — AI designs the study, recruits/screens verified panel participants (400+ targeting criteria), runs AI-moderated text/audio/video interviews at scale, and auto-synthesizes themes, sentiment, and highlight reels. Claims "4.5x more feedback per question, 3x more emotional/contextual insights, 2x participant engagement time."
- **Add-on — Contacts & Automations:** **+$29/mo** (2,400 actions/mo) or **+$89/mo** (12,000 actions/mo); custom on Enterprise/Growth Custom. 25,000 total contacts, segmentation, scheduled/triggered actions.

## How it works / model

Self-serve SaaS subscription (with a free funnel tier). Journey: sign up free → build a form via template/AI prompt → publish via link/embed/QR → collect responses → analyze with Insights AI → (paid) automate follow-up via Growth Flow or run studies via Research Flow. Monetizes by recurring per-seat/per-response-tier plans, gated features (branding removal, analytics, integrations, security), and usage add-ons (actions, enrichment, response overages). Free plan funnels to paid (Freemium funnel into a subscription model).

**Core plans** (monthly list / effective monthly when billed yearly, "Save 30%"):
- **Free:** **$0** — unlimited forms, 3,000+ templates, 10 responses/mo
- **Basic:** **$39/mo** ($28/mo yearly) — 100 responses/mo, 1 user
- **Plus:** **$79/mo** ($56/mo yearly) — 1,000 responses/mo, 3 users, remove Typeform branding, custom subdomain
- **Business:** **$129/mo** ($91/mo yearly) — 10,000 responses/mo, 5 users, drop-off rates, conversion tracking, priority support
- **Talent:** **$169/mo** ($119/mo yearly) — 3,000 responses/mo, 3 users; HR/people teams (video Q&A, Clarify with AI)
- **Enterprise:** **Custom** — tailored limits, SSO, HIPAA/GDPR, data-center choice, dedicated outcomes manager

**Growth plans:**
- **Growth Flow:** **$379/mo** ($266/mo yearly) — 5 seats, 10k+ responses/mo, 1,500 enrichments/mo
- **Growth Custom:** **Custom** (annual) — bespoke seats, 20k+ responses, 3,000 enrichments, custom domain, SSO, HIPAA

## Positioning & audience

Primary audience is **B2B teams** — Marketing (B2B/B2C), Product/UX/research, HR/Talent, Customer Success, and growth/GTM teams — explicitly reaching enterprise ("trusted by 95% of the Fortune 500"). Also lands with individual creators and small businesses via the free/Basic tiers (B2C-ish self-serve). Claimed edge is **design + conversational UX driving higher completion and richer data** ("double the completion rate vs. traditional forms"), now extended into an AI moat: build-by-prompt, adaptive follow-ups, and end-to-end automation/research so teams "go from question to decision in hours, not weeks." Competitive framing on-site is against Jotform and Formstack (footer "Why Typeform?"); Research Flow implicitly targets research-platform incumbents.

## Nav structure

```
- Platform
  - Platform overview — /platform-overview
  - Typeform AI — /ai
  - Growth Flow (New) — /growth
  - Research Flow (New) — /research-flow
  - Contacts & Automations — /contacts-and-automations
  - Video engagement — /video
  - Analytics and reporting — /reporting
  - Integrations — /connect
  - Tools: Form builder /forms · Survey maker /surveys · Quiz maker /quizzes · Test maker /test-maker · Poll builder /poll-builder · Application form /application-form-builder · Landing page /landing-page-builder · NPS /nps-form-builder · Registration /registration-form-builder · Short form /short-form-builder
  - Templates — /templates
- Solutions
  - Teams: Marketing /roles/b2b-marketing · Product /templates-category/product · HR /roles/hr · Customer success /templates-category/customer-success
  - Use cases: Lead generation /use-case/lead-generation · Employee onboarding · Employee satisfaction · Employee engagement · Customer feedback (all-use-cases /use-case-gallery)
  - Plans: Core /pricing · Growth (New) /growth · Research Flow (New) /research-flow · Talent /pricing/talent · Enterprise /enterprise
- Resources
  - Support: Help center · Community · Contact us
  - Company: Partners /partners · Careers /careers · Webinars /webinars
  - Blog — /blog
- Enterprise — /enterprise
- Pricing — /pricing
- (footer) About us /about-us · Brand /brand · Developers/API /developers · Status · Referral program · Partners (Agency/Technology/Startups)
```

## Credibility & proof

- **Scale claims:** 150,000+ businesses; 48M+ responses collected monthly; "trusted by 95% of the Fortune 500."
- **Customer logos:** Calendly, CitizenM, L'Occitane, WeTransfer, Slack, Webflow, Zapier, Barry's, HubSpot, Hermès.
- **Named case studies:** SmartBug Media (+40% sales leads), Double Denim Marketing ($3.67M in sales), WWF Cities (feedback at scale), Viva (75% faster time-to-hire), Talento (40x enrollments).
- **Compliance:** HIPAA + GDPR available (Enterprise/Growth Custom), SSO, BAA on request; published transparency report, NFIR, and modern-slavery statement.
- **AI trust posture:** explicit "no customer data trains models"; qualitative analysis runs on a private Anthropic instance; AI features disable-able in admin.

## Visual & brand impression

Confident, design-forward, distinctly "Typeform." The current homepage is a **dark aubergine/near-black canvas** with vivid purple-magenta (#D258FE) gradients and glossy 3D product renders, scrolling into lighter (lavender/white) testimonial and integration bands before a dark footer — so the brand reads dark up top, light in the middle. Primary CTAs pop in a bright lime/chartreuse against the dark ground. Type is TWK Lausanne (clean geometric grotesque). Tone is modern, polished, and slightly playful (the recurring "Click for sound" autoplay video cards, the "Telethon" banner) — premium SaaS that still signals approachability. Inner product pages (platform-overview, pricing) drop the dark hero for light, lavender-accented layouts.

## Strategic read

Typeform is mid-pivot from "the pretty form builder" to an **AI-native data-collection-and-action platform**. The structural tell is the two "Flow" products: Growth Flow pushes downstream into lead enrichment + lifecycle automation (territory of CRM/marketing-automation tools), and Research Flow pushes into AI-moderated research (territory of dedicated research/UX-testing platforms like UserTesting/Dovetail in this store's cohort). Both are bets that the form is just the entry point and the value is what happens to the response. Pricing reflects the move upmarket — Growth Flow at $379/mo is ~3x the top self-serve Business tier, and Contacts & Automations was folded in as core rather than an add-on. Heavy on-site experimentation (pricing test pages, A/B'd plans) signals an aggressive growth/monetization motion.

## Provenance

- **Pages:** 7 captured via Firecrawl (maxAge:0, US, all-formats) — homepage, /pricing, /platform-overview, /ai, /research-flow, /growth, /about-us. Plus a 480-URL map (sample, blog/locale-heavy).
- **Verify:** all sourceURLs matched; all 7 bodies md5-unique (no §5.1 contamination).
- **Credits:** 8 (1 map + 7 scrapes), all single-credit basic scrapes; no enhanced-proxy or PDF overages.
- **Couldn't get:** funding/revenue/exact headcount (not on a marketing site — deep-research job); per-template and full integration catalog (out of Tier-0 scope); live pricing is A/B'd so the captured numbers are a point-in-time snapshot.
