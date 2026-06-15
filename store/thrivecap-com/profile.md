---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: thrivecap.com
name: Thrive Capital
aliases: []
legal_entity: ""                     # site states no legal name (no JSON-LD/©/footer)
parent: []
owns: []
socials: {}                          # site links no social channels (no JSON-LD sameAs, no footer anchors)
external: {}

# Capture meta
captured_at: 2026-06-14
capture_method: firecrawl
site_notes: "Framer-built SPA; markdown is thin on every page — content renders client-side, READ FROM SCREENSHOTS. Homepage is a live date/time-clock landing with a Spline 3D logomark embed; /info is the real index. No JSON-LD, no <nav> (bare-div nav — rebuild from screenshot). Deliberately opaque: NO portfolio list, team, fund size, or AUM anywhere on site. LP/investor portal is external (thrivecapital.altareturn.com). Brand hue is RED #B21420 (the mark), not the black branding.colors reports (that's the UI text)."
key_pages:
  info: /info
  incubations: /incubations
  contact: /contact
  investors: https://thrivecapital.altareturn.com/   # external LP portal (AltaReturn)
unverified_fields:
  - "Portfolio companies, team/partners, fund sizes, AUM, founding date — none disclosed on the site (by design); a deep-research job, not capture."
  - "thrive.capital also resolves HTTP 200 — likely a vanity domain they own, but not captured/confirmed as the same entity, so left out of aliases."

# Description — one sentence: [what they do] + [how] + [focus/differentiator].
description: "A New York venture-capital firm that invests in and builds internet, software, and technology-enabled companies, partnering with founders from incubation through growth."

# Classification — closed sets (see TAXONOMIES.md). Leave empty if the site doesn't determine it.
entity_type: Investor / Holding
target_market: [B2B]                 # deals with businesses (portfolio companies) + institutional/HNW LPs
offering_category: []                # STRAIN: a capital-allocating VC firm has no sellable product/service in the taxonomy; entity_type carries it. Left empty per the Investor/Holding gating rule.
portfolio_shape:                     # empty — Investor/Holding; its "portfolio" is investments, not offerings (TAXONOMIES rule)
business_model:                      # empty — VC economics (mgmt fees + carry) aren't in the closed set and aren't stated on the site
primary_industry: Finance & Fintech

# Visual identity — Firecrawl `branding` is a hint to verify, never source-of-truth.
logo_url: "https://framerusercontent.com/images/wTRQbw1UlJLLsjPTdU2bulTkj6M.png"   # no graphical wordmark exists; the red geometric logomark is the canonical "just give me the logo" mark
logos:                               # 2.5 module — wordmark omitted on TRUE absence (brand uses no graphical lockup; name is set in plain Helvetica)
  logomark: { src: "https://framerusercontent.com/images/wTRQbw1UlJLLsjPTdU2bulTkj6M.png", px: 1200, transparent: false }   # red geometric mark on a baked WHITE square (apple-touch-icon; larger than the google-s2 256px)
  og:       { src: "https://framerusercontent.com/images/DE67fmTqkUvDss4wxk9dAkWZQ.gif", w: 1200, h: 630 }                  # declared og:image — 3D render of the red mark on black (a .gif, may animate)
brand_colors: { primary: "#B21420", accent: "#000000", background: "#F7F5F2" }   # red = the mark (true brand hue); black = text/UI; cream = page background
fonts: [Helvetica, "Helvetica Neue"]
color_scheme: light
design_framework: framer             # framerusercontent.com CDN + "framer" markers in rawHtml (branding said "custom")
---

## Overview

Thrive Capital is a New York venture-capital firm that, in its own words, "builds and invests in internet, software, and technology-enabled companies." Beyond investing in existing companies, it runs an incubation arm (Thrive Incubations) that partners with founders to start and build new ventures. The public site is radically minimal — a tagline, an incubations blurb, and a contact card — and discloses nothing about its portfolio, partners, or funds.

## What they offer

As an investment firm there are no priced, sellable offerings — two activities, both described only at the highest level:

- **Venture investment:** Backs "internet, software, and technology-enabled companies" (verbatim). No stage, check size, or terms are published.
- **Thrive Incubations:** "We partner with founders to explore new ideas, build exceptional products, and launch world-class companies" (verbatim) — an in-house company-building arm, not just passive capital.

## How it works / model

The site frames Thrive as both a builder and an investor ("builds and invests"). Capital is raised from limited partners — the **Investors** link routes to an external LP portal at `thrivecapital.altareturn.com` (AltaReturn is a fund-administration / investor-reporting platform), which is the only signal on the site that this is a managed fund with outside LPs. Fee/carry economics are not stated and aren't readable from the site.

## Positioning & audience

Two audiences, neither courted with detail: **founders** of internet/software/tech-enabled companies (the investment + incubation targets) and **limited partners** (routed to the gated portal). The whole presentation is built on withholding — no pitch, no portfolio, no team. The implicit positioning is that of an established firm that doesn't need to sell itself.

## Nav structure

```
- Home — /
- Info — /info            (the index page; links out to the three below)
  - Investors — https://thrivecapital.altareturn.com/   (external LP portal)
  - Incubations — /incubations
  - Contact — /contact
```

Each subpage is a single screen with a CLOSE/Home link back to /info — effectively a four-card site.

## Credibility & proof

None presented — and the absence is itself the signal. No client/portfolio logos, no testimonials, no AUM or fund figures, no named team, no press. The only concrete facts on the site are the headquarters (**New York, New York**) and two contact addresses (**pr@thrivecap.com**, **info@thrivecap.com**).

## Visual & brand impression

Austere, confident, anti-marketing. A near-blank cream canvas (#F7F5F2) with a live date/time clock centered at the top and tiny black Helvetica text anchored to the bottom-left corner. The single graphic is the brand's red geometric **logomark** — an abstract chevron/"T" built from three crimson (#B21420) parallelograms — rendered in 3D via a Spline embed on the homepage (which is why the static screenshot reads blank). The type is uniformly small (≈12px Helvetica), tightly tracked, lowercase-of-nothing — the design equivalent of speaking quietly because everyone already leans in. There is no graphical wordmark; the name is simply set in Helvetica.

## Strategic read

The opacity is the strategy. Where most VC sites foreground portfolio, partners, and thesis, Thrive's site is engineered to reveal almost nothing — a deliberate scarcity/exclusivity posture. Practically, this means the site is a poor primary source for anything beyond identity and positioning; portfolio, team, and fund data must come from external research. The "builds and invests" framing plus a named incubation arm is the one substantive differentiator the site does assert: Thrive presents itself as a company-builder, not only a check-writer.

## Provenance

- **Pages:** 4 analyzed via Firecrawl — homepage, /info, /incubations, /contact. All thin-markdown SPA pages; content read primarily from the full-page screenshots + metadata.
- **Verify:** All sourceURLs matched; all 4 bodies md5-unique; no junk soft-404s.
- **Credits:** 5 spent this run (1 map + 4 scrapes); logos module rode the cached homepage payload (no re-scrape; only headed icon fetches).
- **Couldn't get:** Portfolio companies, partners/team, founders, fund sizes, AUM, founding date — none on the site by design (deep-research, not capture). LP portal content is gated.
- **Run profile:** +logos (express — user requested the logos module). Wordmark omitted on true absence (no graphical lockup).
