---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: lsvp.com
name: Lightspeed Venture Partners
aliases: ["LSVP", "Lightspeed", "Lightspeed Ventures"]
legal_entity: "Lightspeed Management Company, L.L.C."   # © footer + global-presence page ("LSVP")
parent: []
owns: []   # Faction (faction.vc) and Lightspeed India (LSIP, lsip.com) are explicitly SEPARATE entities, not owned — see Overview / Strategic read
socials:
  facebook: https://www.facebook.com/Lightspeed/
  x: https://x.com/lightspeedvp
  instagram: https://www.instagram.com/lightspeedventurepartners/
external: {}   # no third-party records (crunchbase/wikipedia/…) in the homepage JSON-LD sameAs

# Capture meta
captured_at: 2026-06-14
capture_method: firecrawl
site_notes: "WordPress (wp-content); Cloudflare-fronted. Heavy CookieYes consent banner + repeated portfolio-logo / founder-photo carousels inflate the markdown — substantive copy starts ~line 755 on every page. Portfolio companies live at /company/<slug> (443 URLs in the map). India (LSIP) + Southeast Asia content sits on a SEPARATE site, lsip.com. Brand font GoodSans. No A/B tool detected. AUM / fund sizes / founding year are NOT stated on the marketing pages."
key_pages:
  about: /about
  founder_experience: /founder-experience
  launch: /launch
  global_presence: /global-presence
  companies: /companies
  team: /lightspeed-team
  research_hub: /research-ai
unverified_fields:
  - "AUM / total committed capital, fund sizes, and number of funds — not stated on captured marketing pages (deep-research figures)."
  - "Founding year and founding partners — not stated on captured pages; the firm says only 'over twenty years' / '20+ years'."
  - "Headcount, total number of portfolio companies, and exit/IPO counts — named but not given as totals on captured pages."
  - "Business model (fund management fees + carried interest) — standard VC economics, but not described on the captured pages; left empty."

# Description — one sentence: [what they do] + [how] + [focus/differentiator].
description: "A multi-stage venture capital firm that backs founders from Seed to Series F and beyond across enterprise, AI, consumer, fintech, health, and cybersecurity, pairing capital with a hands-on operator platform (Lighthouse) and offices across the US, Europe, and Israel."

# Classification — closed sets (see TAXONOMIES.md).
entity_type: Investor / Holding
target_market: [B2B]
offering_category: [Services / Consulting]   # investment + advisory/platform services; an Investor/Holding has no priced product
portfolio_shape:               # empty by rule — an Investor/Holding's "portfolio" is its investments, not an offering set
business_model:                # empty — VC fund economics (mgmt fees + carry) not described on captured pages
primary_industry: Finance & Fintech   # the sector the FIRM operates in (venture capital / investment management)

# Visual identity — Firecrawl `branding` is a hint to verify; confirmed against screenshot.
logo_url: https://lsvp.com/wp-content/uploads/2023/04/logo_lightspeed_venture_partners.svg
logos:
  wordmark: { src: "https://lsvp.com/wp-content/uploads/2023/04/logo_lightspeed_venture_partners.svg", w: 200, h: 33 }
  logomark: { src: "https://lsvp.com/wp-content/uploads/2023/04/mstile-310x310-1.png", px: 558, transparent: false }   # geometric "L" mark, dark on a BAKED white tile bg
  og:       { src: "https://lsvp.com/wp-content/uploads/2023/06/Lightspeed_Video_2-scaled.jpg?1779795047", w: 2560, h: 1440 }
brand_colors: { primary: "#FFF7F0", ink: "#000000", accent: "#FFD7CF" }   # STRAIN: black wordmark/headlines on warm cream (#FFF7F0); coral (#FFD7CF) + a blue (#1863DC) gradient are accent washes — confirmed vs screenshot
fonts: [GoodSans]
color_scheme: light
design_framework: wordpress   # rawHtml/JSON-LD wp-content
---

## Overview

Lightspeed Venture Partners is a global, multi-stage venture capital firm that has, in its own words, "for over twenty years been the first investor and an early backer of some of the most innovative companies in the world." It backs founders "from Seed to Series F and beyond" across enterprise/software, AI, consumer, fintech, healthcare/bio, and cybersecurity, and frames its differentiator as **depth** — "Depth is our center of gravity… possibility grows the deeper you go" — positioning itself against "speculators and opportunists" who "fund from afar."

Beyond capital, the firm runs an operator platform branded **Lighthouse** (executive talent, business development, founder community) and an early-stage program, **Lightspeed Launch**. It operates as one global team across US, Europe, and Israel offices; the **India and Southeast Asia** offices belong to a *separate* legal entity, Lightspeed India Partners, L.L.P. ("LSIP", lsip.com).

## What they offer

The "offerings" of a VC firm are capital plus founder services — none are priced/published, so each carries `[on-request]`:

- **Investment capital — Seed to Series F and beyond:** Multi-stage backing; the firm emphasizes being the **first/lead institutional investor** and "high conviction" participation in every subsequent round `[on-request]`
- **Lighthouse — the operator platform team:** "the most senior operators, industry luminaries and prominent executives" who "roll up their sleeves." Spans Executive Talent, Business Development, and Founder Network `[on-request]`
  - **Executive Talent:** Executive (VP→C-suite) team building, organization strategy, industry-luminary access, pre-IPO board & advisory recruiting, executive compensation strategy, and a functional-expert "Operator Network"
  - **Business Development:** Design Partner Program, **CxO Innovation Network** ("2,500+ enterprise IT and innovation leaders across 1,200+ companies"), Strategic Partnerships (cloud providers, analysts), the **Velocity Program** annual conference (portfolio ↔ Fortune 1000 IT buyers), and a vendor **Marketplace**
  - **Founder Network & Global Community:** peer founder network, Technology Visionaries (advisory board), and "Industry Tastemakers" community programming
- **Lightspeed Launch — early-stage company-building program:** "A first-of-its-kind, company-building program for early-stage Lightspeed founders" with three parts — **1-on-1 Advisory Support**, the **Lighthouse Knowledge Base** (early-stage playbooks/toolkits), and **Early-Stage Founder Workshops**. Run by Launch Partner Luke Beseda; currently designed for US/EU founders `[on-request]`
- **Emergence Program:** Support for "break-out emerging managers" (VC fund managers); inaugural class drawn from "Black, Latinx, Indigenous and Pacific Islander, and Veteran communities" `[on-request]`
- **Faction:** A separate seed-stage affiliate (Faction Ventures, L.L.C.) — see Strategic read `[on-request]`

## How it works / model

Multi-stage venture investing: Lightspeed positions itself as the first/lead investor that then "participates in every equity round since the very beginning" (founder testimonials cite backing from Seed through IPO over 7–8+ years). It invests "based on the merits regardless of where the founder resides," operating as "one global team." The Launch FAQ explicitly states the program "is **not** an investment screening mechanism" — it's post-investment company-building support.

Revenue model (standard VC fund economics — management fees + carried interest) is **not described** on the captured marketing pages; left out of `business_model` rather than guessed. LP-facing operations run through a gated portal ("LP login") and the **Lighthouse** platform site (lighthouse.lsvp.com); a **Portfolio Jobs** board sits at jobs.lsvp.com.

## Positioning & audience

Targets ambitious technology founders — increasingly **AI-first** ("over a decade as AI founders' first call"), with deep concentration in enterprise software, cybersecurity, fintech, and frontier/bio. The claimed edge is *depth* over breadth: "rolling up our sleeves to earn our seat at the table," "creating together instead of funding from afar." Implicitly positions against larger, more transactional multi-stage funds by emphasizing hands-on operator support and long-duration partnership.

## Nav structure

```
- About — /about
- Team — /lightspeed-team   (India variant: /lightspeed-team/?location=india)
- Companies — /companies   (India variant: /companies-india/)
- Founder Experience — /founder-experience   (India variant: /india-founder-experience/)
- Stories — /stories   (India variant: /india-stories/)
- Launch — /launch
- Research Hub — /research-ai
- (utility)
  - Faction — /#modal-faction → faction.vc
  - Contact — /global-presence/
  - LP login — services.dataexchange.fiscloudservices.com (external)
  - Events — /events/
  - Lighthouse — lighthouse.lsvp.com (external platform portal)
  - Portfolio Jobs — jobs.lsvp.com (external)
```

## Credibility & proof

Trust signals are dominated by portfolio prominence (all company names verbatim, self-presented):

- **Named portfolio / exits:** Anthropic (Series F), Wiz, Cyera, Rubrik, Snap, Stripe, Affirm, Navan (IPO), Netskope (IPO), Faire, Nutanix, AppDynamics, MuleSoft, Grafana, Zscaler, Arctic Wolf, Cato Networks, Glean, Moveworks, Carta, Rippling, Epic Games, 1Password, Guardant Health, Ultima Genomics, The Honest Company, BetterUp, Mistral AI, xAI, ElevenLabs, Ramp, Suno, Snorkel AI, ThoughtSpot
- **"First institutional investor in" claim (verbatim):** "Affirm, AppDynamics, Arctic Wolf, Blend, Honest Company, MuleSoft, Mist, Oyo, Nutanix, Navan (formerly TripActions), QuantumScape, Rubrik, Snap, ThoughtSpot, Zscaler, Materialize, Yugabyte, Redpanda, Handshake and others"
- **Network scale claim (self-reported):** CxO Innovation Network of "2,500+ enterprise IT and innovation leaders across 1,200+ companies"; "generated hundreds of millions of dollars in ARR" for companies
- **Tenure:** "For over twenty years" / "20+ years As First Believers"; "over a decade as AI founders' first call"
- **Founder testimonials:** Ariel Cohen (Navan), Bipul Sinha (Rubrik), Bhavin Shah (Moveworks), Ajeet Singh (ThoughtSpot/Nutanix), and others, each citing Lightspeed as first investor across multiple rounds
- **Ecosystem partnerships:** Founding partner of AllRaise Xcelerate and the BLCK VC Scout Program (with Sequoia); Lightspeed + UC Berkeley Sky Lab

## Visual & brand impression

Premium, editorial, restraint-forward. Warm **cream/off-white (#FFF7F0)** canvas with **black** GoodSans headlines set very large ("POSSIBILITY GROWS / THE DEEPER YOU GO"), a single soft **blue gradient** wash mid-page, and warm-toned founder portraits as the human anchor. The mark is a geometric **"L"** (a folded-corner shape) plus a lowercase "lightspeed" wordmark in near-black (#303030). The coral/salmon (#FFD7CF) appears as an accent tone. Overall read: a confident, design-mature firm that signals taste and seriousness rather than flash — consistent with the "depth, not surface" thesis.

## Strategic read

- **AI concentration is the headline.** Recent activity (newsfeed, logo walls, "first call" copy) skews heavily to AI/foundational-model and AI-application companies — Anthropic, Mistral, xAI, ElevenLabs, Suno, Fireworks, Reactor — alongside the long-standing enterprise/cyber book.
- **Deliberate multi-entity structure (relevant for ownership joins).** The site repeatedly stresses that **LSVP** (US/Europe/Israel), **Lightspeed India Partners / LSIP** (India + SE Asia, lsip.com), and **Faction Ventures** (faction.vc) are "distinct," "separate businesses that operate independently." LSVP "holds certain interests in Faction" — a stake, not control. These are **affiliations, not ownership**, so `owns`/`parent` are intentionally empty; treat them as related firms, not subsidiaries.
- **Platform as moat.** The breadth of Lighthouse (talent, BD, community) + Launch is positioned as the structural differentiator versus capital-only investors — the "we go deeper" claim made operational.

## Provenance

- **Pages:** Analyzed 5 captured pages via Firecrawl (`maxAge:0`, US geo) — homepage, /about, /founder-experience, /launch, /global-presence — plus the homepage `branding` + JSON-LD/nav structured layer and full-page screenshots. Map returned 443 URLs (portfolio at /company/<slug>).
- **Verify:** All 5 sourceURLs matched; all body md5s unique; no junk soft-404s.
- **Credits:** 6 (1 map + 1 homepage + 4 key pages); logos rode the cached homepage payload (free).
- **Couldn't get:** AUM/fund sizes, founding year/partners, and exit/headcount totals — not on the marketing pages (see `unverified_fields`).
- **Run profile:** express — +logos (wordmark/logomark/og measured); no offerings module (Investor/Holding has no priced SKU roster).
