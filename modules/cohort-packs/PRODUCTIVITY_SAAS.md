# PRODUCTIVITY_SAAS.md — the `productivity_saas` cohort-pack contract

> **What this is.** The contract for the engine's **second cohort pack** — the opt-in `store/<domain>/productivity_saas.md` that carries the productivity-software classification cuts the universal `profile.md` can't tell apart. Same machinery as [`TELEHEALTH.md`](TELEHEALTH.md), a different vertical. This is the spec you **obey** when authoring a `store/<domain>/productivity_saas.md`.

> **Scope — horizontal productivity / work software.** End-user collaboration & knowledge-work apps: docs, databases, project tools, meeting notes, chat, design, CRM-for-teams. **Not** infra/devtools (Datadog, Snowflake), payments (Stripe), or vertical SaaS (Toast, Veeva) — those read differently and would flatten these cuts, the way `owns-pharmacy?` is meaningless for a watchmaker. A tool outside this scope is a *different cohort*, not a sparse `productivity_saas.md`. The name says it: **productivity** (the vertical) + **saas** (cloud-subscription, multi-tenant — excludes boxed/one-time desktop software). **Out-of-cohort examples** (stress-test false positives — gate them at corpus selection, don't force-write a distorted pack): 1Password (security/identity), DocuSign (e-signature/agreement-execution), Intercom (helpdesk/CX) — adjacent verticals, not horizontal productivity.

> **CAPS vs lowercase.** `PRODUCTIVITY_SAAS.md` (this file, in `modules/`) = the **contract**. `store/<domain>/productivity_saas.md` = the **instances** that obey it. Same name, two roles — the case tells them apart.

*Companion to [`SCHEMA.md`](../../SCHEMA.md) (the always-on `profile.md` contract), [`TAXONOMIES.md`](../../TAXONOMIES.md), and [`QUERYING.md`](../../QUERYING.md). Lint: [`scripts/cohortcheck.py`](../../scripts/cohortcheck.py) — generic, no new script. Module registration + the species distinction: [`SCHEMA.md` → Tier-1 modules](../../SCHEMA.md#tier-1-modules-opt-in-separate-docs).*

## What a cohort pack is (and isn't)

A **cohort pack** shares `offerings.md`'s machinery — a separate file, its own contract, enablement-by-existence, own `captured_at` — but it's a **different species** from a depth module:

| | **Depth module** (`offerings.md`) | **Cohort pack** (`productivity_saas.md`) |
|---|---|---|
| Extends | a *universal* dimension at finer grain (what they sell) | *vertical-specific* cuts that don't exist elsewhere (where AI sits on the page? point-tool-or-platform?) |
| Schema | cohort-agnostic — any company could have one | defined by the cohort — meaningless for a telehealth brand |
| The test | does a consumer need this grain? | does it split companies **within the cohort** on a question we'd act on? |

The pack exists because **the universal profile reads near-identical for every productivity SaaS** (all `B2B · Software / SaaS · Subscription`) — so the cuts that actually separate players are invisible to it. Every field below earns its place on **both** halves: it splits the cohort *and* fills from the company's own site. A cut that goes near-uniform *inside* the cohort is decoration even if it would split the broader corpus — that bar is why this pack is 6 fields, not more (see the design note at the bottom).

**State-only, page-attested, never adjudicated** — the same trust line as `profile.md`. Record what the site *says*; don't verify it, don't rank it, don't compare it to peers. Three things stay out, by design:

- **Judgments** (threat / fit / "real competitor?") — relative to *one* asker; a pack is shared across every project that reads the cohort, so an asker-relative verdict poisons it for the next reader. Consumer-side.
- **Cross-company comparison** ("one of only two with a public API") — rots the moment the cohort grows; it's a **query-time** read (`rg` across the cohort frontmatter), never baked per-file.
- **Deep-research provenance** (founders, funding, ARR, headcount) and **Signals** (a launch, a pricing change, an acquisition) — store the page-attested *posture*; let the consumer infer.

## When to write it

Opt-in — **enablement = the file exists** (no config mechanism). Written **alongside `profile.md`** on a productivity-SaaS capture, enabled in the `/research-company` step-2.5 pre-flight. Default everywhere else: **don't write the file** — an absent `productivity_saas.md` reads "not in this cohort."

## `productivity_saas.md` — frontmatter (the 6 cuts)

Six **single-select** closed-set fields, plus doc-meta (`schema_version`, `domain`, `captured_at`). Leave a field **empty** when the captured site doesn't determine it — *empty over guessed* — or use the explicit `unclear` value when you looked and the site is genuinely silent. Read each off the company's own pages; **never infer from the brand name, and never from off-site knowledge of the company** (the cut must survive a capturer who only sees the live page).

| Field | Closed set (single-select) | The cut it makes | Reads off |
|---|---|---|---|
| `primary_job` | `docs/notes/wiki` · `database/spreadsheet/no-code` · `project/task-mgmt` · `meeting-notes/recording` · `messaging/chat` · `video/meetings` · `whiteboard/diagramming` · `design/creative` · `email/calendar` · `scheduling/booking` · `crm/sales-workflow` · `automation/workflow` · `forms/surveys` · `search/knowledge-discovery` · `multi/suite` · `unclear` | the single job the tool **leads with** (front door), distinct from full surface area (body `Jobs:` line). **`multi/suite` is the harder call, never the default:** earned only when the hero names *enumerated* plurality/replacement ("one app for everything", "all-in-one", "replaces X/Y/Z") — brand-metaphor terms alone ("Work OS", "workspace", "the AI workspace") do **not** clear it; if any single job leads, tag *that* job; if the hero leads with an **AI-agent / automation value prop** naming no in-set job and no plurality (the 2026 pattern, e.g. "where teams and agents create together"), read the **center-of-gravity job from nav/pricing** (else `unclear`) — **never** reach for `multi/suite` to fill that void. **`scheduling/booking`** (lead = book-a-meeting / share availability) is distinct from **`email/calendar`** (lead = inbox/compose). **A/B-volatile** + suite-creep — flag rotation. | hero/H1, first nav item, `<title>`/OG |
| `primary_user` | `individual/prosumer` · `team/org` · `developer` · `unclear` | who the site **leads with** — the atomic adopter. **Tie-breakers, in order:** (1) the persona named in the hero H1/subhead; (2) if two are named ("for you *and* your team"), the addressee of the **lowest / free entry tier** — *but if that tier is uncapped / addressed to both, or there's no free tier, (2) doesn't fire → fall to (1), else `unclear`*; (3) `developer` only if the hero names a technical adopter or leads with API/self-host/code — *and (3) outranks (2) when the hero names both an individual and a developer*; (4) genuinely co-equal with no signal ⇒ `unclear` + body note. **Never the brand name.** *(`enterprise` was merged out — not page-attestable without brand/tier knowledge; that signal lives in the Trust body line as named logos.)* | hero H1/subhead, /pricing entry tier |
| `ai_front_door` | `hero` · `feature` · `absent` · `unclear` | **where AI sits on the captured page** — `hero` (AI in the **H1, hero subhead, or primary CTA block**: "The AI workspace") · `feature` (a named AI line/section *below the fold* or an add-on, not the hero) · `absent` (no AI on the front door). **Placement, not a "would it survive without AI" counterfactual** (off-site, unattestable). AI named only as the **object** the product acts on ("…for every human *and AI agent*"), not a capability it provides, is **not** a signal. The cut the universal profile can't see. **Highly A/B-volatile** — flag rotation. | hero/H1, /ai, /product |
| `pricing_model` | `per-seat` · `usage/credit-based` · `unclear` | how they **meter the charge** — a pure metering axis. `per-seat` = per-user/mo; `usage/credit-based` = metered by usage / AI credits / runs (the AI-billing wave the universal profile can't see). A flat per-account price with **no** per-seat/usage meter records the price in the **body** Pricing line, not here. "Can you start at $0" is `free_entry`'s job; open-source / self-host is a **Surfaces** `self-hosted` token, *not* a pricing value. For OSS-with-paid-cloud, record the **paid cloud** meter. | /pricing |
| `free_entry` | `free-tier` · `free-trial-only` · `no-free` · `unclear` | can you start at **$0** — the PLG fuel. **Asymmetric fill — capture the positive signal:** `free-tier`/`free-trial-only` when page-stated; `no-free` only when the site shows paid-from-day-one; **silent ⇒ `unclear`, never an assumed "no."** A heavily seat-capped free plan (e.g. ≤2 seats) is still `free-tier` — the cap goes in the body Pricing line. A perpetual plan usable past any time limit is `free-tier` even if capped; a plan that **expires** is `free-trial-only`. A money-back guarantee is **not** free entry (classify the underlying `no-free`). | /pricing |
| `platform_posture` | `point-tool` · `has-API/integrations` · `app-platform` · `unclear` | does one job closed, or is it a **platform others build on** — `point-tool` (no public dev surface) · `has-API/integrations` (public API and/or integration catalog, but **no** third-party app directory in its own nav) · `app-platform` (the product's **own site navigation, including the footer**, links to a named marketplace / gallery / directory of third-party-built apps, plugins, *or* templates — commerce optional). **Classify the product, not its parent vendor:** for a product inside a parent shell (Google Docs/Meet in Workspace), a marketplace in the *shell* nav is the parent's ⇒ `has-API/integrations`. | own nav (incl. footer) → /developers, /api, /marketplace |

### Machine-readable contract (the lint reads this)

`scripts/cohortcheck.py --cohort productivity_saas` parses the block below (the first fenced `yaml` block carrying `cohort` + `fields`) and validates every instance's frontmatter against it. Keep it in sync with the table above — this block is the source of truth the lint enforces.

```yaml
cohort: productivity_saas
doc_meta: [schema_version, domain, captured_at]
fields:
  primary_job:      [docs/notes/wiki, database/spreadsheet/no-code, project/task-mgmt, meeting-notes/recording, messaging/chat, video/meetings, whiteboard/diagramming, design/creative, email/calendar, scheduling/booking, crm/sales-workflow, automation/workflow, forms/surveys, search/knowledge-discovery, multi/suite, unclear]
  primary_user:     [individual/prosumer, team/org, developer, unclear]
  ai_front_door:    [hero, feature, absent, unclear]
  pricing_model:    [per-seat, usage/credit-based, unclear]
  free_entry:       [free-tier, free-trial-only, no-free, unclear]
  platform_posture: [point-tool, has-API/integrations, app-platform, unclear]
```

## `productivity_saas.md` — body

A light **bold-led** body (lead each line with a bold label + colon, per SCHEMA's body discipline) for what needs verbatim or fills only as prose. Governing rule for all of it: **page-attested, never adjudicated** — record what the site says, don't verify it.

- **Platform & integrations** — the platform/API **claim quoted verbatim** (e.g. *"'Connect to 7,000+ apps' — /integrations"*), API availability (`public API | private/partner | none`, /developers), and a marketplace/gallery when present (the **own-nav-link test** for `app-platform`). The **count is a claim, never verified** (a "7,000+ integrations" number is marketing). Allow an earned prose paragraph when the picture is multi-clause (*public REST API + webhooks + a partner marketplace + a separate template gallery*).
- **Surfaces** — where it runs, as one greppable token line (`web · macOS · Windows · iOS · Android · browser-extension · CLI · API · self-hosted`), a **token set, never a stored taxonomy** (cross-tool grouping is a query-time grep). `self-hosted` carries the open-source / self-host fact that `pricing_model` no longer holds.
- **Jobs** *(required when `primary_job` is `multi/suite`, and useful whenever one tool genuinely spans several)* — the **full job set + the center-of-gravity job**, verbatim from the page. This is the home for the surface area `primary_job` deliberately collapses — e.g. *"docs + databases + projects + wikis — 'one workspace for everything' (gravity: docs/notes/wiki)."*
- **Scope** *(when one URL serves both a free-consumer tier and a paid B2B tier)* — which product / SKU / URL this capture classified, and the split — e.g. *"classified the Workspace (paid B2B) path; a free consumer tier exists at docs.google.com."* Keeps a dual-funnel brand from being silently half-captured.
- **AI** — what the AI **does**, backed by the page-attested **product** (a named "AI" line, an agent, "ask AI"), quoted — not an asserted capability. Model provenance **only when the page states it** (*"built on GPT-4o" / "bring-your-own-key" / "your data is never used to train models"*). When `primary_job` is `unclear` or `multi/suite`, **name the tool's actual job in prose here**. The home for `ai_front_door` detail.
- **Pricing & packaging** — the tier names + entry price **verbatim** with the universal price-visibility token (`` `[published | partial | on-request]` ``), seat-vs-usage detail, free-tier limits + any **seat cap / minimum seats**, monthly/annual + annual lock, and a **license note** (open-source / source-available) when a license or GitHub link is in nav/footer. **Page-stated terms only** — never the real post-trial billing reality (that's a Signal).
- **Trust & compliance** — the SaaS trust signals that don't generalize to the universal profile: **certifications** (SOC 2 / ISO 27001 / GDPR / HIPAA — security/trust page or footer, y/n), **named enterprise customers/logos** (now the page-attested home for the "enterprise" signal merged out of `primary_user`), an uptime/status or SLA page. The vertical's own trust seals — the productivity analog of telehealth's LegitScript.

### File shape (drop-in template)

```yaml
---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"          # the productivity_saas-pack version (independent of profile.md's)
domain: notion.com             # company key (same as profile.md)
captured_at: 2026-06-16        # own freshness — posture shifts (moves AI to the hero, opens an API, changes pricing)
primary_job: docs/notes/wiki   # live H1 "Where teams and agents Create together" names no job → center-of-gravity (nav/pricing) = docs, NOT multi/suite
primary_user: team/org
ai_front_door: hero            # H1 + subhead name agents/AI; "AI workspace" is the title/nav tagline (placement, not a native-vs-augmented call)
pricing_model: per-seat
free_entry: free-tier          # perpetual Free plan for individuals
platform_posture: app-platform # own nav links to a template marketplace + integration gallery (+ public API)
---

## Platform & integrations
- **Platform:** public REST API (/developers) + an integration gallery + a public template marketplace (own nav links to it ⇒ `app-platform`); positions as "the connected workspace." Integration count: [verbatim claim — illustrative; confirm on capture].

## Surfaces
- **Surfaces:** web · macOS · Windows · iOS · Android · browser-extension

## Jobs
- **Jobs:** docs/notes + wikis + databases + projects + AI agents/search — the hero names no single job ("teams and agents create together"), so center-of-gravity from nav ⇒ `primary_job: docs/notes/wiki` (gravity: docs/wiki).

## AI
- **AI:** "Notion AI" + **Agents** (multi-step tasks), AI Meeting Notes, Enterprise Search — AI is the hero story. Model provenance: page names no vendor (states zero-data-retention, "not used to train models").

## Pricing & packaging
- **Pricing:** Free · Plus · Business · Enterprise; per-seat /month `[published]`, Enterprise `[on-request]`; Free tier (individual use); annual discount. AI agents metered in "Notion credits" *on top of* seats — usage overlay body-noted, per-seat stays the lead meter.

## Trust & compliance
- **Trust:** SOC 2 Type 2, ISO 27001, GDPR; HIPAA on Enterprise — /security; named enterprise logos on homepage; public status page.
```

*The Notion example is an **illustrative sketch**, not a full captured instance (telehealth's template rode a real Hone/Maximus capture). The `ai_front_door: hero` value *is* grounded — a live fetch during the stress-test confirmed Notion now leads its hero with AI — but the pricing tiers and integration count still need a real capture to quote verbatim.*

*A sparse capture is honest: a closed point tool (e.g. an AI notetaker) where the platform fields don't apply leaves them tight — `platform_posture: point-tool · pricing_model: per-seat · ai_front_door: hero`, a short **AI** line, no marketplace — rather than guessing.*

## Capture

**Near-free — it rides the `profile.md` pages, no new endpoints.** Every cut fills from pages the standard recipe already pulls (homepage, /product, /pricing, nav, JSON-LD). Enable the pack in the step-2.5 pre-flight, like `offerings.md`. The behaviors that matter:

1. **Read the hero/H1 for `ai_front_door` *and* `primary_user`** while you're on the homepage (AI placement; the persona the headline addresses), and **pull `/pricing` *and* `/security`|`/trust`** — the trust-seal page is often separate from the marketing nav and the base capture may skip it; it's the only page that determines the **Trust & compliance** line.
2. **Quote any claim verbatim; adjudicate nothing** — an integration count, an "AI" hero tagline, a SOC-2 badge are marketing until verified. The engine records the page-attested claim; checking it is a deep-research job.
3. **Dual-funnel rule (free consumer vs paid B2B at one URL).** When a brand serves a perpetual-free consumer tier *and* a paid B2B tier (e.g. a consumer doc app vs its Workspace plan), classify the **B2B / paid** reality — the cohort is productivity *SaaS* — and record the split on the **Scope** body line.
4. **Scope gate before you write the file.** A tool must itself *do* a cohort job on a live productivity-SaaS page. If the captured page is parked/placeholder/niche and **every cut comes back `unclear`**, that's a wrong-target / corpus-selection miss — fix the domain, don't force-write an all-`unclear` pack.
5. **Flag `primary_job` + `ai_front_door` rotation** with the stock `unverified_fields` "point-in-time snapshot, not fixed" line (per SCHEMA's live-variable rule) — these two are the most rotation-prone (homepage A/B + the constant 2026 AI-rebrand churn).

## The rules (what the lint enforces)

`python3 scripts/cohortcheck.py --cohort productivity_saas` is the gate — it must pass. **No new script** — `cohortcheck.py` is one generic linter that reads the machine-readable block above; the next cohort ships a contract, not code. The load-bearing rules:

1. **Closed-set conformance.** Every non-empty cut value is one of the field's declared values. A value off the list fails — exact strings only, so the cohort stays queryable.
2. **Single-select.** Each cut is one value, never a list — `ai_front_door: hero`, not `[hero, feature]` (a nuance goes in a body note).
3. **Doc-meta present.** `schema_version`, `domain`, `captured_at` — the frontmatter fence and the three keys.
4. **Empty over guessed.** A field the site doesn't determine is left empty or `unclear`; the lint never demands a value, but it rejects one outside the set.
5. **No stray keys.** A frontmatter key that's neither doc-meta nor a declared cut trips the lint — it catches a typo'd field or a universal `profile.md` field leaking in.
