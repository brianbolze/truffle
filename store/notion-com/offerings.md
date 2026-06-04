---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: notion.com          # company key; each offering's slug (its relative url) is its key *within* Notion
captured_at: 2026-06-04      # own freshness; captures/2026-06-04/ holds the source pages
site_notes: "Not a storefront — there is no catalog backbone or per-SKU PDP. Notion sells per-seat PLANS (all four live on one page, /pricing) that bundle a set of marketed features + a few free standalone apps. So the roster's grain is plan × app × feature, not SKU; prices live almost entirely on /pricing (client-rendered, captures clean) + each feature's /product/* page. The only metered/usage prices are Notion credits (Custom Agents $10/1,000) and Workers (credits from Aug 11) — re-check the credit terms + the savings-calculator competitor prices next run (both move)."
---

## Portfolio overview

Notion is **Flagship + companions**, not a catalog: one core product — the **Notion workspace** (docs, wikis,
projects, databases) — wrapped in an **AI layer** (Notion AI, agents, meeting notes, search) and trailed by two
free **standalone apps** (Calendar, Mail). Nothing is sold à la carte; you buy a **per-seat plan** and the
features come bundled. This roster therefore enumerates at three grains Brian asked for, split by the
**`Category`** column: **`app`** = a downloadable product you install (the products), and **`AI feature` /
`workspace feature` / `developer`** = the marketed capabilities inside the workspace (the features) — plus the
**`plan`** tiers that gate them and the metered **`add-on`** layer.

**The whole portfolio rides four prices**, all per member/month, all verbatim on `/pricing`: **Free $0 · Plus
$10 · Business $20 (Recommended) · Enterprise Custom.** The only prices that aren't a seat fee are usage-metered
**Notion credits** (Custom Agents — "$10 per 1,000 monthly Notion credits," live since **May 4, 2026**) and
**Workers** (Beta, credits from **Aug 11**), plus a **custom-domain** add-on ("$8/month/domain paid annually").

**Visibility rule (stated once, applied to every row).**
- **`published`** — the displayed seat price is the complete, self-contained cost to use the thing (a bundled
  feature inherits its plan's published price; a free app is `published` at $0).
- **`partial`** — a mandatory *separate* cost sits on top of the seat price: the two **metered** lines (Custom
  Agents, Workers) bill Notion credits *in addition to* the Business/Enterprise seat, so the shown seat number
  isn't the all-in.
- **`on-request`** — no price shown: **Enterprise** ("Custom pricing," Contact Sales) and **Consultants**
  (engagement-priced).

**Prominence (calibrated).**
- **Agents / AI are the lead [HIGH]** — the homepage hero is "Meet the night shift," agents are the first
  scroll, and AI is in the page title and every paid tier.
- **Business is the pushed plan [HIGH]** — Notion's own **"Recommended"** badge on `/pricing`; it's the first
  tier to unlock Notion Agent, AI Meeting Notes, and Enterprise Search.
- **The core workspace (Docs · Wikis · Projects · Databases) is the foundation [HIGH]** — the product spine
  every plan includes and the AI features act on.
- **Calendar + Mail are companion apps [MED]** — own nav entries and download CTAs, but free adjuncts to the
  workspace, not the headline.

## Roster

Complete at the level Notion indexes (its `/product/*` feature pages, its footer apps, and the four plan tiers
on `/pricing`); core surfaces with no standalone marketing page are rostered with a `(no PDP — …)` slug. Prices
quoted verbatim from `/pricing`; bundled features show `incl.` (their cost is the plan's). A `—` price marks a
family umbrella. Added column: **`Category`** (project-local — the product-vs-feature axis Brian asked for; see Run profile).

| Offering | Kind | Category | Parent | Slug | Price (verbatim) | Visibility | What |
|---|---|---|---|---|---|---|---|
| **Plans** | family | plan | — | `/pricing` | — | — | Per-seat tiers; all four live on one page and gate every feature below. |
| **Free** | buyable | plan | `/pricing` | `/pricing` | **$0** per member / month | published | "For individuals to organize personal projects and life." Trial of Notion AI, basic forms/sites, Calendar + Mail, databases. |
| **Plus** | buyable | plan | `/pricing` | `/pricing` | **$10** per member / month | published | "For small teams." Everything in Free + custom forms/sites, unlimited charts/blocks/uploads, basic connections. Free for students/educators (1-member). |
| **Business** | buyable | plan | `/pricing` | `/pricing` | **$20** per member / month | published | "Recommended." Everything in Plus + Notion Agent, AI Meeting Notes, Enterprise Search (Beta), SAML SSO, private teamspaces, premium connections. |
| **Enterprise** | buyable | plan | `/pricing` | `/pricing` | Custom pricing | on-request | Everything in Business + zero data retention, SCIM, audit log, advanced security/DLP/SIEM, domain mgmt, CSM. Contact Sales. |
| **Notion workspace** | buyable | app | — | `/product` | incl. (seat) | published | The flagship app — "Your AI workspace": docs, wikis, projects, databases from composable blocks. Web + desktop (Mac/Windows) + mobile. |
| **Notion Calendar** | buyable | app | `/product` | `/product/calendar` | **$0** (free) | published | Standalone calendar app; syncs Google Calendar + Apple iCloud (Outlook on roadmap). macOS/Windows/iOS/Android. |
| **Notion Mail** | buyable | app | `/product` | `/product/mail` | **$0** (free) | published | Standalone AI inbox that syncs with Gmail; auto-labels, drafts, schedules. iOS live, Android "coming soon." SOC2 + HIPAA. |
| **Notion Web Clipper** | buyable | app | `/product` | `/web-clipper` | incl. (free) | published | Browser extension to save web pages into Notion. (Footer download; no marketing page captured.) |
| **Mobile app (iOS & Android)** | buyable | app | `/product` | `/mobile` | incl. (free) | published | The workspace on iPhone/Android. |
| **Desktop app (Mac & Windows)** | buyable | app | `/product` | `/desktop` | incl. (free) | published | The workspace as a native desktop app. |
| **Notion AI** | family | AI feature | — | `/product/ai` | incl. (Business **$20**) | published | The AI layer — chat, generate/edit docs, autofill, translate, AI blocks; included on Business/Enterprise, trial on lower tiers. |
| **Notion Agent** | buyable | AI feature | `/product/ai` | `/product/agents` | incl. (Business **$20**) | published | Personal, on-demand AI assistant; inherits your permissions; "anything you can do in Notion." All users get it; full on Business+. |
| **Custom Agents** | buyable | AI feature | `/product/agents` | `/product/agents` | "Free to try, then **$10** per 1,000 monthly Notion credits" | partial | Team-wide agents that run on schedules/triggers (Q&A, task-routing, status); metered on Notion credits (live May 4, 2026) on top of the Business/Enterprise seat. |
| **AI Meeting Notes** | buyable | AI feature | `/product/ai` | `/product/ai-meeting-notes` | incl. (Business **$20**) | published | Auto-transcribes meetings (records system audio, no bots) + summaries + action items; 19 languages; Business+ (Beta). |
| **Enterprise Search** | buyable | AI feature | `/product/ai` | `/product/enterprise-search` | incl. (Business **$20**) | published | Answers across connected apps (Slack, Drive, GitHub, Jira…); "#1 by G2"; Business+ (Beta). |
| **Research Mode** | buyable | AI feature | `/product/enterprise-search` | `/product/enterprise-search` | incl. (Business **$20**) | published | Deep-reasoning multi-step reports pulling from workspace, apps, and the web. (Sub-feature of the AI/search layer.) |
| **Docs** | buyable | workspace feature | `/product` | `/product/docs` | incl. (seat) | published | "Simple and powerful" documents — the writing surface. |
| **Knowledge Base / Wikis** | buyable | workspace feature | `/product` | `/product/wikis` | incl. (seat) | published | "Centralize your knowledge" — one source of truth for teams and agents. |
| **Projects** | buyable | workspace feature | `/product` | `/product/projects` | incl. (seat) | published | "Manage any project" — tasks, dependencies, timelines. |
| **Databases** | buyable | workspace feature | `/product` | `(no PDP — core surface, in /pricing)` | incl. (seat) | published | Flexible databases (subtasks, dependencies, custom properties, charts); the data spine under everything. |
| **Forms & Sites** | buyable | workspace feature | `/product` | `(no PDP — in /pricing)` | incl. (Basic free; Custom on Plus **$10**) | published | Capture responses (Forms) and publish pages to the web (Sites); Basic on Free, Custom on Plus+. |
| **Connections / Integrations** | buyable | workspace feature | `/product` | `/connections` | incl. (Basic free; Premium on Business **$20**) | published | Connect Slack, Drive, GitHub, Asana & more; Basic/Premium/Advanced by tier. |
| **Public API & Webhooks** | buyable | developer | — | `(no PDP — developers.notion.com)` | incl. (seat) | published | Build integrations; real-time webhooks. Surfaced at developers.notion.com / notion.dev. |
| **Workers** | buyable | developer | — | `(no PDP — in /pricing)` | "Free to try now. Starts using credits on **August 11**" | partial | Beta — run custom code to extend agents, sync data, trigger workflows; moves onto Notion credits Aug 11. |
| **CLI** | buyable | developer | — | `(no PDP — in /pricing)` | incl. (seat) | published | "Build on Notion and deploy Workers with code or coding agents." |
| **Custom domain & branding** | buyable | add-on | — | `(no PDP — in /pricing)` | "**$8**/month/domain paid annually, or **$10**/month per domain paid monthly" | published | Connect a custom domain to a published Site and remove Notion branding; per-domain add-on. |
| **Templates** | buyable | ecosystem | — | `/templates` | incl. (free) | published | Large free gallery of pre-built workspace templates. |
| **Consultants** | buyable | ecosystem | — | `/explore-consultants` | engagement-priced | on-request | Marketplace of certified Notion consultants for setup/services; no list price. |

### Verbatim anchors

The footnotes the Price column points at, quoted exactly from the captures:

- **Custom Agents (metered):** "AI agents handle repetitive tasks autonomously, so your team doesn't have to. Free to try, then **$10 per 1,000 monthly Notion credits**." Agents page: "Starting May 4, 2026, Custom Agents will run on Notion credits, available as an add-on to Business and Enterprise plans… Monthly Notion credits are $10 per 1,000 credits." (`/pricing`, `/product/agents`, `/product/ai`)
- **Workers (metered):** "Extend Notion with custom code… **Free to try now. Starts using credits on August 11.**" (`/pricing`)
- **Custom domains:** "Connect a custom domain to your Site and remove Notion branding for **$8/month/domain paid annually, or $10/month per domain paid monthly**." (`/pricing`)
- **Business badge:** "**Recommended**" (`/pricing`).
- **Student/educator:** "The Plus Plan (with a 1-member limit) is free for students and educators." (`/pricing`)
- **AI bundling:** "All other AI features—Notion Agent, AI Meeting Notes, Enterprise Search—are included in Business and Enterprise plans at no additional cost." (`/product/agents`)
- **Yearly:** "Save up to 20% with yearly." Refunds: "full amount… within three days of signing up for monthly billing, or within 30 days… for annual." (`/pricing`)

No molecule audit applies — Notion is software, so the telehealth `molecule · form · access` lead is dropped from `What`; capability descriptors are page-attested instead (the spine columns are unchanged, so the lint holds).

## Deep blocks

One earned — the **AI credit model**, because the roster's `partial` tokens can't carry why two AI lines price
differently from the rest, and the cutover date is a real ambiguity:

**Notion Agent vs Custom Agents — the credit split.** Verbatim (`/product/agents`): *"Custom Agents are
team-wide AI teammates that run automatically on schedules or triggers. Notion Agent is a personal AI assistant
that works on-demand when you ask. All Notion users get Notion Agent. Business and Enterprise customers get
Custom Agents, priced under the Notion credit system."* The cutover (`/product/ai`): *"Now through May 3, 2026:
Custom Agents are free to use on Business and Enterprise plans… Starting May 4, 2026: Custom Agents will start
using Notion credits when they run."* — so as of this capture (2026-06-04) metering is **live**. Credits are
*"$10 per 1,000 credits… shared across the workspace and reset monthly. Unused credits don't roll over."* Every
other AI feature (Notion Agent, AI Meeting Notes, Enterprise Search, Research Mode) is **bundled at no extra
cost** in Business/Enterprise — only Custom Agents and Workers meter. That's the whole reason those two rows are
`partial` and the rest are `published`.

No per-app deep block earned — the roster rows carry Calendar, Mail, and the workspace surfaces; their
`/product/*` captures sit verbatim in `captures/2026-06-04/`.

## Provenance

- **Pages read:** `/pricing` (the plan + feature matrix backbone), `/product`, `/product/ai`, `/product/agents`,
  `/product/ai-meeting-notes`, `/product/enterprise-search`, `/product/calendar`, `/product/mail`, `/enterprise`,
  homepage — all in `store/notion-com/captures/2026-06-04/`. Every `$` in this file greps to one of them.
- **Scope:** enumerated — the 4 plans, the standalone apps, the AI features, the core workspace surfaces, the
  developer platform, and the metered add-ons. **Noted but not enumerated:** the Templates gallery (hundreds of
  individual templates) and the Consultants marketplace (rostered as single ecosystem lines, not per-item);
  per-team/solution landing pages (Eng & Product, Design, etc.) are positioning, not offerings.
- **Gated/unreachable:** Enterprise pricing (Contact Sales only); exact Notion-credit consumption per task
  ("depends on the task," not published); Web Clipper / mobile / desktop have no marketing page (rostered from
  footer download links).
- **Snapshot caveat:** pricing/IA is point-in-time — Custom Agents metering began May 4 2026, Workers credits
  start Aug 11, and the homepage savings-calculator competitor prices flex with a team-size slider.
- **Run profile:** non-vanilla — added a project-local **`Category`** column (the downloadable-product vs
  marketed-feature axis Brian requested) and adapted `What` for software (dropped the telehealth
  `molecule · form · access` lead); the seven spine columns + closed visibility set are unchanged, so
  `offeringscheck.py` holds. First non-telehealth `offerings.md` in the store.
