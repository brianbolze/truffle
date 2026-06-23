---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: coda.io
captured_at: 2026-06-23
primary_job: multi/suite       # hero "Your all-in-one collaborative workspace" + the page enumerates "Replaces [X/Y/Z]" for Writeups/Hubs/Trackers/Applications — earned plurality, not brand-metaphor. Center-of-gravity job = docs/notes/wiki (see Jobs).
primary_user: team/org         # hero leads with "collaborative workspace" / "brings teams and tools together" / "50,000+ teams"
ai_front_door: feature         # AI is NOT in the H1; it's a below-the-fold section ("Take the busywork out of your work with Coda AI") + a dedicated /product/ai page
pricing_model: per-seat        # per "Doc Maker" / month (a per-user meter scoped to creators); AI metered in pooled credits is a usage overlay, noted in body
free_entry: free-tier          # perpetual Free plan, "Free for you and your team"
platform_posture: app-platform # own nav (Product menu, footer, Extend) links to the Packs gallery/marketplace of third-party-built apps + Pack Studio + public API
---

## Platform & integrations
- **Platform:** public REST API (/developers, /developers/apis/v1) + **Packs** — a marketplace/gallery of third-party-built integrations & extensions (own nav links to it: Product → Packs, footer → Packs, Gallery `?filter=packs`) + **Pack Studio** ("Build your own") ⇒ `app-platform`. Integration count claimed verbatim: **"600+ integrations"** (homepage, /product/ai) — a marketing claim, not verified. Per-tier Pack counts shown on /pricing (Free 42 → Pro 52 → Team 78 → Enterprise 92).

## Surfaces
- **Surfaces:** web · iOS · Android · API  *(macOS/Windows desktop not confirmed on captured pages — only the iOS App Store + Google Play apps are linked in the footer.)*

## Jobs
- **Jobs:** docs/notes + spreadsheet-style tables/databases + no-code apps/automations + AI — "an all-in-one platform that blends the flexibility of docs, structure of spreadsheets, power of applications, and intelligence of AI" (meta/about). Homepage frames four uses (Writeups, Hubs, Trackers, Applications), each "Replaces" a named tool category. Hero names no single job, so center-of-gravity from nav/product = **docs/notes/wiki** (nav leads with "Docs & team hubs"; "a new kind of doc").

## AI
- **AI:** "Coda AI" — "the connected work assistant that knows your team—and can take action for you." Three named surfaces: **AI chat** (brainstorm/ask), **AI assistant** (generate content/tables), **AI column** (AI at scale over data). Included for Doc Makers ("Not a separate add-on. Not a separate license."), Editors get a free trial; metered in a pooled monthly credit allotment. Model provenance: page does not state the vendor (FAQ "What models does Coda AI leverage?" is a collapsed accordion).

## Pricing & packaging
- **Pricing:** Free · Pro **$10/month per Doc Maker** · Team **$30/month per Doc Maker** · Enterprise **Custom** — `[published]` for Free/Pro/Team, `[on-request]` for Enterprise. **Maker Billing:** only Doc Makers (creators) are paid; **Editors and Viewers are always free** ("we don't charge per seat"). AI: included for Doc Makers + paid credit add-ons **$2 / $6 / $12 per Doc Maker/month** (2,000 / 6,000 / unlimited credits) — a usage overlay on the per-seat lead meter. **15% off annual.** Discounts: non-profits 50%, eligible startups Team free for 6 months, student/educator plans. No open-source / self-host.

## Trust & compliance
- **Trust:** **SOC 2 Type II report** + **HIPAA compliance** ("New!") on Enterprise (/pricing compare table); SAML SSO, SCIM provisioning, advanced access controls, audit events, legal hold + eDiscovery (Enterprise). **99.9% uptime commitment** to Enterprise; public status page (status.coda.io); daily + cross-regional backups (/trust). Named enterprise logos: Figma, The New York Times, Square, Robinhood, BuzzFeed, TED, Uber. Self-reported reach: "80% of the Fortune 100 use Coda." (ISO 27001 / GDPR not enumerated on captured pages.)
