---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: airtable.com
captured_at: 2026-06-17
enumeration: indexed-complete
site_notes: "SaaS offerings roster is plan/add-on grain, not feature/SKU soup. /pricing is the backbone: Free/Team/Business/Enterprise Scale plans, AI-credit packs, Portals add-on, EKM/professional-services add-ons, API limits, and per-seat billing FAQ are all markdown-clean. Product modules such as Omni, Field Agents, HyperDB, App Library, automations, views, reporting, sync, templates, and Marketplace are plan-gated platform features, not separately buyable rows."
---

## Portfolio overview

Airtable sells one flagship app-building platform through four plans, with paid add-ons layered on top. This `offerings.md` is intentionally **plan/add-on grain**: it captures the buyable packages and separately priced add-ons, while platform features (Omni, Field Agents, HyperDB, App Library, automations, interfaces, views, reporting, sync, templates, Marketplace, Web API) remain in the `What` cells and in `profile.md` / `productivity_saas.md`.

**Prominence read:**
- **Core Airtable platform `[HIGH]`:** the homepage, platform page, and pricing table all lead with the app-building platform and plan ladder.
- **AI credits / AI layer `[HIGH]`:** AI is in the homepage hero and every plan includes AI credits; packs are separately priced.
- **Portals `[MED]`:** new/visible in nav and pricing grid, but add-on rather than core plan.
- **Professional services / EKM `[LOW]`:** real add-ons, but enterprise/admin line items rather than first-screen offers.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (package · billing basis · access) |
|---|---|---|---|---|---|---|
| Airtable platform | family | — | /platform | — | — | No-code app platform: shared data, interfaces, automations, views, reporting, sync, integrations, AI app building/agents · plan ladder · self-serve + sales |
| Free | buyable | Airtable platform | /pricing | **Free** | published | Individual/small-team plan · no-cost tier · self-serve; up to 5 editors, 1,000 records/base, 100 automation runs, 500 AI credits/editor/month |
| Team | buyable | Airtable platform | /pricing | **$20USD** per seat/month billed annually; **$24** billed monthly | published | Team plan · per-seat subscription · self-serve; 50,000 records/base, 25,000 automation runs, 15,000 AI credits/paid user/month |
| Business | buyable | Airtable platform | /pricing | **$45USD** per seat/month billed annually; **$54** billed monthly | published | Business/department plan · per-seat subscription · purchase now or sales; SAML SSO, App Sandbox, verified data, two-way sync, 20,000 AI credits/paid user/month |
| Enterprise Scale | buyable | Airtable platform | /pricing | **Custom pricing** / Contact Sales | on-request | Enterprise plan · custom contract · sales; 500,000 records/base, Enterprise API, App Library, HyperDB, Enterprise Hub, DLP, audit logs, EKM, HIPAA, 25,000 AI credits/paid user/month |
| AI credit packs | buyable | Airtable platform | /pricing | Starts at **$120/month for 10k credits**; Enterprise Scale Contact Sales | published | AI usage overlay for Omni / Airtable AI / Field Agents · monthly credit pack · self-serve on paid plans, sales for Enterprise Scale |
| Portals | buyable | Airtable platform | /pricing | Starts at **$120/month for 15 guests**; starts at **$150/month for 15 guests**; Enterprise Scale Contact Sales | published | Guest-user access portals · monthly guest-pack add-on · Team/Business self-serve, Enterprise sales |
| Enterprise Key Management | buyable | Enterprise Scale | /pricing | Add-on | on-request | Customer-owned encryption keys · enterprise security add-on · sales/admin-gated |
| Professional Services | buyable | Business / Enterprise Scale | /pricing | Add-on | on-request | Airtable professional service packages for qualified customers · services add-on · sales/partner-gated |
| Marketplace extensions | family | Airtable platform | /marketplace | — | — | Extensions, scripts, and open-source extension ecosystem; Marketplace page lists Airtable-built and third-party extensions, not a single Airtable-priced SKU |

### Verbatim Anchors

- **Per-seat meter:** pricing FAQ says "Airtable plans are charged per seat" and Team/Business charge users with edit permissions for at least one base in the workspace.
- **Free plan:** "Our Free plan is available at no cost for users just getting started" and is formulated for "individual users, very small teams, or those with lightweight needs."
- **Team / Business / Enterprise pricing:** pricing FAQ says Team is "$20/user/month when billed annually"; Business is "$45/user/month when billed annually"; Enterprise Scale is custom and "based on the organization's needs and scale with Airtable."
- **AI credits:** plan cards list "500 AI credits per editor each month," "15,000 AI credits per paid user each month," "20,000 AI credits per paid user each month," and "25,000 AI credits per paid user each month at list price." The feature grid lists "Starts at $120/month for 10k credits."
- **Portals:** feature grid lists "Starts at $120/month for 15 guests" and "Starts at $150/month for 15 guests"; the footnote says "Pricing for Portals starts at $127.50/month for 15 guests on our annual plan for Business."
- **Professional services:** pricing footnote says "Airtable professional service packages are available for purchase by qualified customers on Business and Enterprise Scale plans."
- **Molecule/spec audit:** N/A - software platform. `What` descriptors use package/feature/billing language from `/pricing`, `/platform`, `/platform/ai`, `/marketplace`, and `/developers/web/api/introduction`.

## Deep Blocks

**None earned - the roster carries this company.** The ambiguity is not hidden SKU detail; it is the difference between buyable packages and included platform features. The roster keeps rows to the buyable level and leaves the feature taxonomy in `profile.md` and `productivity_saas.md`.

## Provenance

- **Pages read (cited captures, 2026-06-17):** `pricing.md` (backbone: plans, add-ons, AI credits, API limits, billing FAQ), `platform.md` (platform/product taxonomy), `ai.md` (Omni / Field Agents), `marketplace.md` (extension ecosystem), `api.md` (public API), `homepage.md` (AI-front-door and nav).
- **Scope note (`enumeration: indexed-complete`):** every public plan and separately priced/gated add-on on `/pricing` is rostered at plan/add-on grain. Deliberately not row-expanded: included feature modules, plan limits, individual Marketplace extensions, templates, and integration cards.
- **Visibility:** Free/Team/Business, AI credit packs, and Portals have public prices or floors; Enterprise Scale, EKM, and professional services are sales/on-request.
- **Point-in-time caveat:** SaaS packaging, AI-credit allowances, and add-on pricing are a 2026-06-17 snapshot; recapture before comparing current prices.
- **Run profile:** express opt-in full pack — `offerings.md` requested for a productivity SaaS company; kept at the plan/add-on indexed level rather than feature SKU inflation. Flagship hero product images are N/A for a software platform.
