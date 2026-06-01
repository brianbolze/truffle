---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: 1

# Identity
domain: granola.ai
name: Granola
aliases: [granola.so, meetgranola, "Granola, Inc."]   # granola.so = earlier domain (still cited in on-site testimonials); meetgranola = social handle
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Next.js (/_next/ present; __NEXT_DATA__ absent — app-router). Map is rich (323 URLs, real sitemap) but ~70% is /blog/* SEO content + /jobs/* + docs.granola.ai help-center — the product surface (/pricing, /enterprise, /chat, /ai-note-taker, /integrations, /security, /use-cases/*) is small and also fully linked from the homepage footer. Homepage is heavy with duplicated module copy + an embedded X/Twitter testimonial wall (so branding.colors.primary #536471 is Twitter-chrome slate, NOT the brand hue). Real brand color = olive/lime green #5B6F00 (primary CTA) on near-white. Custom fonts are Quadrant (headings) + Melange (body); branding.fonts lists Roboto/Segoe/Helvetica/Arial as generic fallbacks only. Logo as hostable SVG: /logos/rebrand/marque.svg (branding.images.logo is an inline data-URI). Pricing/help live partly off-domain: notes.granola.ai (app/download), docs.granola.ai (help center), go.granola.so (privacy). CAPTURE HAZARD (this machine): fc.py scrape inside a bash `for`-loop fails — first `python3: command not found` (pyenv shim not on the subshell PATH), then even `env: bash: No such file or directory`; run each scrape as an individual, non-loop command. Tool-output delivery was also heavily batched/delayed this session (files persist fine; reads just lag)."
key_pages:
  pricing: /pricing
  enterprise: /enterprise
  notepad_vs_notetaker: /ai-note-taker
  chat: /chat
  integrations: /integrations
  security: /security
  for_sales: /use-cases/sales
  for_product: /use-cases/product
  download: https://notes.granola.ai/download
  help_center: https://docs.granola.ai/help-center
unverified_fields:
  - "/integrations returned a thin soft-404 (26-char body) — the integration list below is taken verbatim from /pricing instead (Attio, Notion, Slack, HubSpot, Affinity, Zapier, MCP, API)."
  - "SOC 2 Type 2 / HIPAA posture is referenced across /pricing, /enterprise, and /security FAQs, but specific certificate scope/audit dates were not extracted."
  - "Founding date and formal HQ — not stated on captured pages; footer reads 'Made with ♥ in Shoreditch' (London) + '© Granola, Inc. 2026'. The '$125M' homepage banner is an on-site funding claim (event signal), left to deep research."

# Description
description: "A Mac/iPhone (and Windows) AI notepad that transcribes your computer's audio directly — no meeting bots — and merges it with the notes you type, then uses AI to enhance, template, search, and chat across your meetings."

# Classification
entity_type: Company
target_market: [B2C, B2B]
offering_category: [Software / SaaS]
portfolio_shape: Single
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://www.granola.ai/logos/rebrand/marque.svg
brand_colors: { primary: "#5B6F00", secondary: "#E5EACD" }   # olive/lime CTA green + pale-green secondary; slate #536471 in branding payload is embedded-tweet chrome, ignored
fonts: [Quadrant, Melange]            # custom heading/body families (branding.fonts' Roboto/Segoe/Helvetica/Arial are generic fallbacks)
color_scheme: light
design_framework: next.js             # rawHtml: /_next/ present (app-router; no __NEXT_DATA__)
---

## Overview

Granola is an **AI notepad** for people who live in back-to-back meetings. The desktop app (Mac-first, with iPhone and a Windows build per open roles) records your computer's audio **directly — with no meeting bot joining the call** — transcribes it, and merges that transcript with the sparse notes you type yourself; when the meeting ends it AI-enhances those raw notes into a clean, structured writeup. Around that core it adds **Granola Chat** (ask questions across your meetings/transcripts), customizable per-meeting-type templates, post-meeting actions (draft the follow-up email, pull action items), and one-click sharing into the tools you already use. Positioned as "like Apple Notes, but it also transcribes your meeting" and explicitly as an *AI notepad* rather than an *AI note-taker*.

## What they offer

One product (Mac/iPhone/Windows app), expressed as a few surfaces of the same tool — `portfolio_shape: Single`:

- **Notepad:** the core app — "Granola takes your raw meeting notes and makes them awesome." Records computer audio with **no meeting bots**, works across Zoom, Google Meet, Microsoft Teams, Webex, and Slack huddles.
- **Granola Chat:** "AI chat that already knows what you're working on" — query and analyze across your meetings/transcripts (`/chat`).
- **Granola for iPhone:** "Meeting notes on the go and for your phone calls" — mobile capture incl. phone calls.
- **Templates:** "Get notes in the format your team needs" — customizable templates for common meeting types (customer discovery, user interviews, 1-on-1s, pitches, standups).
- **Post-meeting actions:** "the latest AI models built in" to write follow-up emails, list action items, summarize, surface objections/budget.
- **Sharing:** one-click out to Slack, Notion, CRM/Affinity, email, public link, ATS/candidate notes.
- **Briefs** (recently launched): pre-meeting prep "as you join" (`/blog/briefs-...`).

Plans (per user / month, verbatim from `/pricing`):

- **Basic — $0:** AI meeting notes, limited meeting history, AI chat within & across meetings, shared folders, custom templates, multi-language, opt out of model training any time
- **Business — $14:** everything in Basic + unlimited notes/history, "advanced AI thinking models," advanced integrations, centralized billing & user management, MCP integration, API access
- **Enterprise — $35:** everything in Business + enterprise-grade security & admin controls, SSO, priority support + usage analytics, org-wide auto-deletion periods, org-wide model-training opt-out, org-wide "Granola is being used" notification

Dedicated **startup** and **student** programs widen the funnel; Granola donates "1.5% of your subscription" to Stripe Climate.

## How it works / model

Customer journey: **download the Mac app (free to start) → it captures your computer's audio + your typed notes in any meeting → AI enhances the notes when the meeting ends → chat/template/share/act on them.** Product-led, individual-download motion (the homepage CTA is "Download for Mac," not "Book a demo"), expanding into teams (team folders, shared notes) and **Enterprise**. Monetization is recurring **subscription**, per-seat, with a free tier funneling to paid (the in-app "AllFound" mock even role-plays a per-employee-per-year comparison). Distribution/app + help live off the marketing domain: `notes.granola.ai` (app/download), `docs.granola.ai` (help center), plus a public **API**, **MCP** integration, and CRM/workflow connectors — **Attio, Notion, Slack, HubSpot, Affinity, Zapier** (Business tier and up; per `/pricing`, since `/integrations` itself soft-404s).

## Positioning & audience

- **Core claim:** an *AI notepad*, not an *AI note-taker* — they own a dedicated `/ai-note-taker` ("AI-notepad vs note-taker") page to draw the line.
- **Headline differentiator:** **no meeting bots** — "Granola transcribes your computer's audio directly, with no meeting bots joining your call." Privacy/presence framing ("You stay present"; "Ready for calmer, more productive meetings?").
- **Audience:** product teams, founders, VCs, sales, customer success, consultants, and recruiters (the blog and `/use-cases/sales`, `/use-cases/product` segment heavily; startup + student programs widen the funnel).
- **Named competitors on their own site:** Fireflies, Fathom, Otter (`/blog/meeting-note-tool-pricing-granola-vs-fireflies-fathom-otter`) and Dovetail (`/blog/enterprise-ai-notetaker-vs-dovetail`).

## Nav structure

```
Top bar
- Features
  - Notepad — /
  - Chat — /chat
  - Granola for iPhone — (notes.granola.ai / onelink mobile)
- Pricing — /pricing
- Blog — /blog
- Careers — /jobs
- Download — https://notes.granola.ai/download

Footer
- Features: Notepad (/), Chat (/chat), Mobile (onelink)
- Product: Pricing (/pricing), Enterprise (/enterprise), AI-notepad vs note-taker (/ai-note-taker),
           For sales (/use-cases/sales), For product management (/use-cases/product), Explore more… (/explore)
- Company: Careers (/jobs), Press (Notion press kit), Events (/events),
           Startup program (/startups), Student program (/students)
- Resources: Blog (/blog), Security (/security), Help Center (docs.granola.ai/help-center),
             Status (status.granola.ai), Affiliates, Contact (/contact),
             Terms (/policies), Privacy (go.granola.so/privacy), License (/third-party-licenses)
- Social: LinkedIn (/company/meetgranola), X (@meetgranola), YouTube (@meetgranola)
```

## Credibility & proof

- **Customer logos (homepage):** PostHog, Intercom, Linear, Index, Brex, Replit, Vercel — framed "Helping the world's best product teams." Dedicated customer pages exist for Vercel, Zapier, Vanta, Brex.
- **Named testimonials (embedded X wall):** Nat Friedman; Guillermo Rauch ("It's actually unbelievable how good granola.ai is… the killer user research tool"); Ryan Hoover; Des Traynor; Dan Shipper; Soleio; Alex Cohen; Deedy; Nichole Wischoff; plus John Borthwick (Betaworks) and Adriana Vitagliano (Firstminute) pull-quotes.
- **Funding (on-site banner, verbatim):** "Granola raises $125M to put your company's context to work" (`/blog/series-c`; `/blog/series-a` also present). On-site claim / event signal — noted, not treated as durable state.
- **Customer case studies (named, with exec quotes):** Brex — Pedro Franceschi, Founder & CEO ("Granola earned our trust by delivering precise, reliable summaries"); Vercel — Guillermo Rauch, Founder & CEO ("the killer user research tool… no going back to pre-Granola days"); Vanta — Kelly Bray, VP Customer Success ("without budging on our compliance commitments"). Each links a `/customers/<co>` page.
- **Press:** "Time magazine selected Granola as one of the best AI tools for note-taking" (cited on `/pricing`).
- **Security & compliance:** a dedicated `/security` page plus pricing/enterprise FAQs referencing **SOC 2 Type 2**, **HIPAA**, **SSO**, org-wide auto-deletion, and model-training opt-out (cert scope/dates not extracted — see `unverified_fields`).
- **Trust/positioning extras:** "Granola contributes 1.5% of your subscription to remove CO₂… through Stripe Climate."

## Visual & brand impression

Clean, calm, light-mode consumer-software aesthetic on near-white. The single brand accent is an **olive/lime green (#5B6F00)** carried on fully-rounded (pill) primary buttons, with a pale-green (#E5EACD) secondary; custom **Quadrant** display headings over **Melange** body type give it a crafted, slightly editorial feel rather than generic-SaaS. The page leans on realistic product mockups (a live notepad splitting "your notes + transcript," a "Casey ⟷ Rahul 1-on-1," chat suggestion chips) and a dense wall of founder/investor tweets as social proof. Footer signature "Made with ♥ in Shoreditch" reinforces a small, design-led London studio identity. Overall: mature, confident, prosumer — closer to a beloved indie Mac app than enterprise software, even as Enterprise is now a top-line motion.

## Strategic read

Granola is riding a sharp wedge — **bot-free, local-audio capture** — that doubles as a privacy/etiquette differentiator against the Otter/Fireflies/Fathom "a bot joined your call" category, and an *AI-notepad-not-notetaker* narrative that reframes the whole space. The product is deliberately **Single** (one app), but the strategy is clearly expanding up-market (Enterprise, team folders, SOC 2/HIPAA posture, API + MCP) and outward via heavy programmatic SEO (the bulk of 323 mapped URLs are use-case/comparison/ROI blog posts) plus startup/student/affiliate funnels. The prominent $125M raise and a logo wall of developer-darling companies (Vercel, Linear, Replit, PostHog) signal it's converting prosumer love into a team/enterprise land-and-expand play.

## Provenance

- **Pages (8 · Firecrawl · `maxAge:0` · `location:US`):** homepage (`/` — markdown + screenshot + branding/rawHtml/links), the 323-URL site map, and key pages `/pricing`, `/enterprise`, `/ai-note-taker`, `/chat`, `/security` (all full), plus `/integrations` (soft-404, thin — its list recovered from `/pricing`).
- **Verify:** `fc.py verify` (8 pages) — all sourceURLs match, all bodies md5-unique, no §5.1 contamination; `profile.md` lint clean (no leaked tags, Provenance + required keys present).
- **Credits:** 11 this run (a clean run is ~9) — inflated by duplicate map/homepage captures (map ×3, homepage ×2) while recovering from the for-loop PATH hazard; the first two key-page batches died `python3: command not found` / `env: bash: No such file or directory` and billed nothing, then each scrape was re-run as an individual non-loop command.
- **Couldn't get:** `/integrations` body (soft-404); SOC 2 / HIPAA cert scope + audit dates; founding date and formal HQ (not on captured pages).
