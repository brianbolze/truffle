---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.0"

# Identity
domain: listenlabs.ai
name: Listen Labs
aliases: [Listen]
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Framer site (framerusercontent images, data-framer); framework reads 'framer' from rawHtml. Logo is an inline data-URI SVG in branding.images.logo — use the favicon fallback. No public pricing page (demo-led enterprise + 'Try for Free' PLG entry). Marketing copy concentrates on the homepage (~125KB md); /compare is a 'Listen vs everyone' positioning hub with 20+ /compare/listen-vs-* subpages; deep product docs live on docs.listenlabs.ai (separate subdomain, not captured). Map is heavy with SEO /articles/* and /blog/* noise — the real IA (features, use-cases, roles, industries) comes from homepage + footer links."
key_pages:
  founders_letter: /founders-letter
  ai_moderator: /features/ai-moderator
  research_agent: /features/research-agent
  quality_guard: /features/quality-guard
  emotional_intelligence: /features/emotional-intelligence
  compare: /compare
  case_studies: /case-studies
  docs: https://docs.listenlabs.ai/get-started
unverified_fields:
  - "Pricing — no public pricing page; motion is 'Book a Demo' (enterprise) plus a 'Try for Free' self-serve sign-up. business_model inferred as Subscription from the SaaS/workspace/enterprise model, not a stated price."
  - "Headcount, exact founding date, founders' names — not on the captured marketing pages."

description: "An AI-moderated research platform that recruits participants and runs adaptive voice, video, and text interviews at scale, then auto-generates segmented insights, themes, and reports — delivering qualitative depth in hours instead of weeks."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Single
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://framerusercontent.com/images/MsbZQm1PVsbD2Dgze1v2P83xHas.png  # branding.images.logo is an inline data-URI SVG; this is the favicon fallback
brand_colors: { primary: "#0000EE", accent: "#0021CC" }  # STRAIN: pure-blue hyperlink #0000EE is the signature hue, confirmed blue on CTAs in the screenshot
fonts: [Plain]
color_scheme: light
design_framework: framer
---

## Overview

Listen Labs (the product is "Listen") is an AI-first customer-research platform. It replaces traditional surveys, focus groups, and human-moderated interviews with an AI researcher that recruits the right participants, conducts in-depth adaptive interviews (text, voice, or video) at scale, and turns the results into personas, themes, and shareable reports — the pitch is "actionable insights in hours, not weeks." It targets enterprise insights, UX, brand, and product teams who need qualitative depth at quantitative scale.

## What they offer

One platform, sold as a whole; the named features are surfaces of that single product (hence `Single` shape):

- **AI Moderator:** AI interviewer that runs in-depth interviews with "smart, adaptive probes" — asks the why, double-clicks on interesting answers, follows conditional logic ("if they mention a competitor, ask which one and why"). Researcher-designed, neutral tone, 100+ languages, fully traceable to the transcript.
- **Research Agent:** ("New Feature") collaborative analysis assistant — segment comparisons with built-in significance testing, fully traceable charts, web search for outside context, and output generation (slides on your template, downloadable memo, theme-coded CSV).
- **Quality Guard:** ("New Feature") fraud-detection + quality-scoring system on every interview by default — analyzes voice/video/behavioral signals (tab-switching, copy-paste, repeat respondents), scores each response, removes-and-replaces ones below bar, backed by a human review team.
- **Emotional Intelligence:** feature page listed in nav (/features/emotional-intelligence) — captured in nav only, not deep-scraped this run.
- **Participant recruiting:** "pool of millions" (homepage "+15M"; /compare claims "30M+ global, verified participants") — or integrate your own provider / recruit your own.
- **Cross-cutting capabilities:** 100+ language auto translate/transcribe; test any stimuli (video, images, Figma prototypes); video/audio/text modes; Research Library as a compounding archive of past interviews; MCP integration (per docs/blog).

No public per-seat or per-study pricing is shown.

## How it works / model

Self-serve or sales-led entry ("Try for Free" sign-up vs. "Book a Demo"). Workflow: design a study / upload your idea → Listen recruits or you bring participants → the AI Moderator runs interviews in parallel → Quality Guard screens and scores responses in real time → Research Agent analyzes, quantifies, and formats deliverables → results (executive summary, personas, themes, clips) in <24 hours. Always-on programs keep a living research archive fresh. Revenue model is enterprise SaaS (workspaces, org-level guardrails, enterprise security) — classified Subscription, though no price is published.

## Positioning & audience

Positions as a **hybrid qual + quant** platform that beats both "Other AI Tools" and "Traditional Methods" — the /compare hub frames Listen as superior across hybrid insights, AI-moderated multi-modal interviews, 3x-longer responses via intelligent probing, parallel scale, 24-hour reports, 30M+ verified participants, fraud detection, 100+ languages, and enterprise compliance. It maintains 20+ head-to-head /compare/listen-vs-* pages (Qualtrics, UserTesting, Maze, Outset, Remesh, Suzy, Voxpopme, dscout/Marvin, Appinio, Quantilope, etc.). Audience is segmented by **role** (consumer insights, UX researchers, brand marketers, product managers, agencies, investors) and **industry** (CPG, technology, e-commerce, healthcare, financial services, hospitality & travel). Differentiators emphasized: depth-via-probing, full traceability (every number links to source), researcher-grade rigor, and trust/quality controls.

## Nav structure

```
- Solutions (use cases) — /use-case/*
  - Brand Tracker / Brand Perception — /use-case/brand-perception
  - Usability Testing — /use-case/usability-testing
  - Multi-Market Segmentation — /use-case/multi-market
  - Concept Testing — /use-case/concept-testing
  - Consumer Journey Map — /use-case/consumer-journey
  - Creative Testing — /use-case/creative-testing
- Features — /features/*
  - AI Moderator — /features/ai-moderator
  - Research Agent — /features/research-agent
  - Quality Guard — /features/quality-guard
  - Emotional Intelligence — /features/emotional-intelligence
- Customers (case studies) — /case-studies
- Resources
  - Personality Test — /personality
  - Compare — /compare
  - Blog — /blog
  - Docs & Guides — https://docs.listenlabs.ai/get-started
  - Media Requests — press@listenlabs.ai
- Careers — /careers
- Sign in — /auth
- Demo — /book-my-demo
Footer adds:
- Role — /role/{consumer-insights, brand-marketers, product-managers, ux-researchers, agencies, investors}
- Industry — /industry/{cpg, technology, e-commerce, healthcare, financial-services, hospitality-and-travel}
- Company — Careers, What's New (/whatsnew)
- Legal — Privacy (/privacy), Terms (/terms), Cookie Policy, Security (trust.listenlabs.ai)
- Customers — KJT Group, Sweetgreen, McKinney, Monitas, Simple Modern, Sling Money, Microsoft, Emeritus, Emerald Research Group, Chubbies (/case-studies/*)
```

## Credibility & proof

- **Funding:** Series B; "$100M raised to date" (homepage banner + founder's letter). Latest round led by Ribbit Capital, with Evantic, Sequoia Capital, Conviction, and Pear VC.
- **Traction (founder's letter):** "Since launching nine months ago, Listen has grown its annualized revenue by 15x and interviewed more than one million people"; "helped hundreds of companies."
- **Named customers / case studies:** Microsoft, Sweetgreen, Perplexity (named in letter); case studies for Chubbies, Microsoft, Sweetgreen, KJT Group, McKinney, Monitas, Simple Modern, Sling Money, Emeritus, Emerald Research Group.
- **Testimonials (verbatim):** Romani Patel, Senior Research Manager, Microsoft — "What once took six to eight weeks now happens in days… It's become a true force multiplier." Jonathan Neman, CEO, Sweetgreen — "Listen has transformed how we approach customer research." Lauren Haugh Neville, Director of Product Insights, Chubbies — "It compresses hours of work into minutes."
- **Stat claims:** "2x" longer responses (homepage) / "3x longer responses" (/compare); "<19h"/"<24h" to results; "+15M" participants (homepage) vs "30M+" (/compare); "50+"/"100+" languages.
- **Security/compliance:** SOC 2 Type II, GDPR, CCPA, HIPAA; Triple ISO — AI Management (42001), Security (27001), Privacy (27701); 256-bit encryption; "data never used to train AI models." Trust center at trust.listenlabs.ai.

## Visual & brand impression

Clean, premium, light-mode SaaS aesthetic built in Framer. Signature color is a pure, almost defiantly "raw-web" hyperlink blue (#0000EE) used on CTAs against generous white space. The hero pairs a tight value prop ("Understand what people want, and why. Fast.") with a product-UI mock of a live interview. Heavy use of warm, diverse human photography (people being interviewed, candid faces) — a deliberate counterweight to the "AI" story, reinforcing the "human stories at scale" pitch. Embedded YouTube product films, customer-logo and testimonial bands, a stat band, and a recurring "Don't guess, just listen." closer. Reads as a well-funded, design-mature category leader, not an early MVP.

## Strategic read

Listen is racing to define the "AI-moderated research" category and using a comparison-SEO land grab (20+ vs-competitor pages + an /articles/* content farm) to own the consideration set against both legacy panels (Qualtrics, UserTesting) and the new AI-native cohort (Outset, Remesh, Strella, Conveo). The strategic wedge is **trust at scale**: Quality Guard (fraud detection + human review) and end-to-end traceability directly attack the biggest objection to AI-run research — "can I believe these responses?" — which is also what unlocks regulated buyers (pharma/finance/healthcare). The "living archive / Research Library" framing is a retention play, turning one-off studies into an always-on knowledge moat. Fast metrics (15x ARR in 9 months, 1M+ interviews, $100M Series B with Sequoia/Ribbit) signal a top-tier-backed company moving aggressively.

## Provenance

- **Pages:** 6 scraped via Firecrawl (`fc.py`, maxAge:0, location:US, waitFor) on 2026-05-31 — homepage, /founders-letter, /features/ai-moderator, /features/research-agent, /features/quality-guard, /compare — plus 1 map call. Nav reconstructed from homepage + footer links; /features/emotional-intelligence and case-study/docs subpages noted but not deep-scraped.
- **Verify:** All 6 sourceURLs matched; all body md5s unique — no geo/cache contamination.
- **Credits:** 7 (1 map + 6 scrapes; no enhanced-proxy or PDF overages).
- **Couldn't get:** Public pricing (none published — demo-led); headcount / founding date / founder names (not on marketing pages); deep docs (docs.listenlabs.ai, separate subdomain, out of scope this run).
