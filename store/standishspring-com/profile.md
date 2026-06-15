---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: standishspring.com
name: Standish Spring
aliases: []
legal_entity: "Standish Spring Investments, LLC"   # © footer
parent: []
owns: []                              # portfolio companies are EQUITY INVESTMENTS, not owned subsidiaries — see Portfolio (relation-evidence: affiliation ≠ ownership)
socials: { linkedin: "https://www.linkedin.com/company/standishspring" }
external: { crunchbase: "https://www.crunchbase.com/organization/standish-spring-investments" }

# Capture meta
captured_at: 2026-06-14
capture_method: firecrawl
site_notes: "Single-page Next.js site (App Router — /_next/ present, no __NEXT_DATA__). No sitemap (map returns only the homepage); zero internal links (every anchor is external — portfolio-company sites + team profiles). No <header>/<nav> element and no JSON-LD. No graphical logo — brand is styled text only; favicon is a generic snake-plant placeholder. Accent (emerald-600 #059669, the teal on 'founders.') lives in external CSS — the branding payload missed it and caught only grays."
key_pages:
  homepage: /
unverified_fields:
  - "offering_category / business_model / portfolio_shape left empty — entity is an Investor / Holding (VC firm); the product/service taxonomy doesn't apply (a VC's 'portfolio' is investments, per TAXONOMIES)."
  - "No designed logo on the site — logomark slot records the generic placeholder favicon (snake plant, 48px); wordmark slot omitted (true absence — text only)."
  - "Team bios, fund size, vintage, AUM, LPs — not stated on the one-page site (deep-research territory, not capture)."

# Description — one sentence (~160-220 chars)
description: "An early-stage venture firm in Duxbury, MA that backs founders building hard tech across energy transition, advanced air mobility, AI infrastructure, life sciences, and enterprise software."

# Classification — closed sets (see TAXONOMIES.md). Empty where the entity type doesn't determine it.
entity_type: Investor / Holding
target_market: [B2B]
offering_category: []                  # n/a — investor has no product/service offering (see unverified_fields)
portfolio_shape:                       # empty by rule — Investor / Holding, "portfolio" = investments (TAXONOMIES)
business_model:                        # empty — VC fee/carry isn't in the closed set
primary_industry: Finance & Fintech    # the sector the FIRM operates in (venture investing); its portfolio thesis is deep-tech/climate

# Visual identity — branding payload is a hint; confirmed against the screenshot.
logo_url: "https://www.google.com/s2/favicons?domain=standishspring.com&sz=256"   # favicon fallback — no wordmark exists to canonicalize to
logos:
  logomark: { src: "https://www.google.com/s2/favicons?domain=standishspring.com&sz=256", px: 48, transparent: false }   # generic placeholder favicon (snake plant), not a designed brand mark; under the 128px deck bar
  og:       { src: "https://standishspring.com/standish-homepage.webp", w: 2000, h: 1341 }   # the historical Duxbury-hotel illustration that fills the hero — the de facto brand cover
  # wordmark: omitted — true absence; the brand renders as styled text (Lora serif), no graphic mark in rawHtml
brand_colors: { primary: "#111827", accent: "#059669" }   # near-black text on white; emerald-600 accent (verified via text-emerald-600 + screenshot). Portfolio grid sits on dark navy.
fonts: [Lora]
color_scheme: light
design_framework: next.js
---

## Overview

Standish Spring is an early-stage venture firm based in Duxbury, MA, fronted by the line **"We invest in founders."** It runs a concentrated, thesis-driven book of ~25 disclosed portfolio companies weighted toward hard tech and the energy transition. The team listed on the site is three people — **Steve Bolze**, **Brian Bolze**, and **Griffin Ready** — and the entire web presence is a single editorial one-pager: thesis, team, and a logo wall of investments. Legal entity is **Standish Spring Investments, LLC** (© 2025 footer).

## Investment focus

Five stated focus areas (verbatim from the site):

- **Energy Transition** — the dominant theme; most of the portfolio sits here (fusion, fission, hydrogen, grid, solar, storage, EV/marine electrification).
- **Advanced Air Mobility** — eVTOL and sustainable-aviation plays (Beta, Electra, Verdego, Sora).
- **AI Infrastructure**
- **Life Sciences** — diagnostics and therapeutics (Freenome, Biolinq, Valora, Lytica).
- **Enterprise Software**

## Team

Three people are listed under the site's **About Us** section:

- **Steve Bolze** — LinkedIn profile linked.
- **Brian Bolze** — personal site linked.
- **Griffin Ready** — LinkedIn profile linked.

No team bios or role titles are published on the one-page site.

## Portfolio

~25 companies named on the homepage, each with a one-line descriptor and a link to its own site (no Standish Spring deal/exit detail is published). Several are already captured in this store:

- **Commonwealth Fusion Systems** — "the world's first commercial nuclear fusion power plant." — cfs.energy
- **Blue Energy** — advanced modular nuclear reactor technology — blueenergy.co
- **Evoloh** — large-scale clean hydrogen production — evoloh.com
- **Beta Technologies** — electric vertical takeoff and landing aircraft — beta.team
- **Electra.aero** — air travel without airports, emissions, or noise — electra.aero
- **Verdego Aero** — hybrid-electric powertrains for sustainable aviation — verdegoaero.com
- **Phoenix Tailings** — sustainable rare-metal mining technologies — phoenixtailings.com
- **Sora Fuel** — sustainable aviation fuel — sorafuel.com
- **Ocean Aero** — autonomous underwater vehicle — oceanaero.com
- **Euclid** — rapid deployment of solar and energy storage — euclidpower.com
- **Wattch** — critical APIs for the distributed power grid — wattch.io
- **Acelerex** — SaaS for planning and operating distributed energy assets — acelerex.com
- **Cala** — intelligent, connected heat-pump water heater — calasystems.com
- **Pellucere** — advanced optical coatings for energy and industry — pellucere.com
- **Verde Technologies** — next-gen solar panels using perovskites — verde-technologies.com
- **Ingu** — sensors and software for pipeline inspection — ingu.com
- **Odyssey Energy Solutions** — distributed renewable-energy platform — odysseyenergysolutions.com
- **Jolt Energy** — ultra-fast EV charging stations — jolt.energy
- **Flux Marine** — fully electric outboard engines for boats — fluxmarine.com
- **Puloli** — SaaS for methane monitoring — puloli.com
- **Freenome** — early cancer detection — freenome.com
- **Valora Therapeutics** — a new approach to immunotherapy — valoratherapeutics.com
- **Lytica Therapeutics** — novel peptide therapeutics — lyticatherapeutics.com
- **Biolinq** — wearable for blood information — biolinq.com
- **Core by Hyperice** — handheld device + content app for meditation — hyperice.com/core-by-hyperice

## Positioning & audience

Audience is **founders** building capital-intensive, frontier-tech companies — the one headline is the whole pitch. The portfolio reads as a climate/deep-tech thesis fund: heavy on energy generation, grid, and electrified mobility, with a life-sciences sleeve. No fund-size, stage-cap, or check-size detail is published; positioning is conveyed entirely through the thesis line and the company logo wall.

## Nav structure

Single-page site, no navigation chrome. In-page sections only:

```
- We invest in founders.  (hero)
- Focus Areas
- About Us  (team: Steve Bolze, Brian Bolze, Griffin Ready)
- Portfolio Companies  (logo grid → external company sites)
```

## Credibility & proof

- **Track record by association:** the portfolio itself is the proof — it includes high-profile deep-tech names (Commonwealth Fusion Systems, Beta Technologies, Freenome).
- **Third-party record:** a Crunchbase organization profile (linked in footer).
- **Channel:** a LinkedIn company page (linked in footer).
- No testimonials, press logos, certifications, or self-reported metrics — consistent with the minimal one-pager.

## Visual & brand impression

Restrained and editorial. The hero splits the screen: a faded sepia historical illustration of the Standish Spring hotel in Duxbury on the left, "We invest in founders." set in a **Lora** serif on the right, with "founders." picked out in **emerald**. Below, the portfolio renders as a uniform grid of dark-navy cards with full-bleed company imagery and small white labels — a clean, gallery-like logo wall. The result feels considered and understated, more boutique-firm letterhead than startup landing page. The only weak spot is the favicon: a generic snake-plant stock image, clearly a leftover default rather than a designed mark.

## Strategic read

A tightly-themed, founder-first early-stage book concentrated in energy transition and frontier hard tech — the kind of portfolio that signals a hands-on, conviction-led posture rather than spray-and-pray. Worth noting two principals share the Bolze surname (Steve and Brian), suggesting a family-anchored firm. Eight of the named portfolio companies already have dossiers in this store, so a downstream consumer can JOIN the portfolio list against captured State.

## Provenance

- **Pages:** 1 — homepage (`/`), firecrawl. Map returned only the homepage; zero internal links and no sitemap confirm a true single-page site, so no further key pages exist to capture.
- **Verify:** sourceURL matched (`https://www.standishspring.com`); single page, md5 `3cf732bb` (no cross-page dup risk). No geo/cache contamination, no soft-404.
- **Credits:** 2 (1 map + 1 homepage). Logos module free (headed fetches, no scrape).
- **Couldn't get:** fund size / vintage / AUM / LP / check-size — not published on the one-page site. Team bios beyond names + profile links — not on site.
- **Run profile:** express — +logos. No wordmark graphic exists (text-only brand); logomark slot records the placeholder favicon, og records the hero illustration.
