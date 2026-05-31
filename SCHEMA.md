# SCHEMA — the store contract

> **What this is.** The contract between *capture* (a `/research-company` agent writes it) and *query* (any agent reads it). It's written to be read by an Opus-class agent that has the **whole capture** in context — multiple pages, screenshots, and the Firecrawl `branding` + `metadata` payloads — not a quick homepage skim.

*Companion: [`TAXONOMIES.md`](TAXONOMIES.md) holds the closed value sets. Scope: commercial companies + products.*

## How to write a profile (capturing agent)

- **Describe the company, not the engine.** A profile records what the company *is* — never commentary about the schema itself. Observations about the contract (missing values, taxonomy gaps, capture-tooling quirks) go to [`BACKLOG.md`](BACKLOG.md), not into prose or comments. The one exception is the inline `# STRAIN:` note on a frontmatter line, which explains *that field's* value to a grep-consumer in a few words.
- **Fill every field the captured pages support — and only those.** If a field isn't determinable from what you captured, leave it empty and add one line to `unverified_fields`. Do not infer it from prior knowledge. *(Funding stage, headcount, revenue are rarely on a marketing site — leave them out. They're a deep-research job, not this one.)*
- **Quote verbatim anything claim- or price-bearing** — taglines, pricing, regulated claims. Paraphrase only long prose.
- **Use the screenshots.** The visual read (design maturity, imagery, tone) is yours to make and a text scraper can't. Write it in *Visual & brand impression*.
- **Reconcile across the whole site you captured.** The homepage is one input, not the answer. Apply this to every section, not just the first.
- **Keep each body section tight** — a few sentences or bullets. Earn a section with evidence; omit it rather than pad with "N/A".

## `profile.md` — frontmatter

Stable, queryable, cheap. Closed-set fields draw from [`TAXONOMIES.md`](TAXONOMIES.md); leave any undetermined field empty.

```yaml
---
schema_version: 1                    # contract version this profile targets; readers gate on it (see note below)

# Identity
domain: honehealth.com               # primary key
name: Hone Health
aliases: []                          # alt names/domains of the SAME entity (rebrand + M&A escape hatch)
parent: []                           # domain SLUG(s) this is a subsidiary / brand-of — from footer/©/about. Empty if top-level. (See relations note.)
owns: []                             # domain SLUG(s) of sub-brands / subsidiaries this entity owns. Empty if none. (See relations note.)

# Capture meta
captured_at: 2026-05-29
capture_method: firecrawl            # firecrawl | webfetch | mixed
site_notes: "Cloudflare-fronted; per-product pricing lives on product pages, not /membership."
key_pages:                           # the semantic links worth keeping; relative ok
  membership: /membership
  trt: /hormone-therapy/trt
  about: /about
unverified_fields:
  - "Per-product pricing — behind the intake quiz, did not submit."

# Description — one sentence (~160-220 chars): [what they do] + [how] + [focus/differentiator].
# Active voice, concrete, no buzzwords/superlatives. For firms/investors: "A [type] that…".
description: "Delivers TRT, weight-loss, and longevity programs to men through licensed telehealth clinicians, using at-home lab testing to personalize and monitor each protocol."

# Classification — closed sets (see TAXONOMIES.md). Leave empty if the site doesn't determine it.
entity_type: Company                 # what kind of entity; usually "Company". Gates the rest.
target_market: [B2C]                 # multi-select, best-fit first
offering_category: [Services / Consulting, Biotech / Pharma Products]   # multi-select, best-fit first
portfolio_shape: Flagship + companions   # optional; shape of what they sell (also drives offerings capture) — see TAXONOMIES.md
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — from Firecrawl `branding`, but VERIFY against the screenshot — don't copy blindly (see note).
logo_url: https://honehealth.com/...  # branding.images.logo, else favicon fallback (it's often empty / a data-URI)
brand_colors: { primary: "#0E3A2F", accent: "#C7A867" }  # retain the palette; confirm the real hue visually (see note)
fonts: [Söhne, Tiempos]              # usually branding.fonts[0] — but verify (generic "sans-serif" can rank first)
color_scheme: light                  # light | dark
design_framework: next.js            # read from rawHtml (__NEXT_DATA__, /_next/) — NOT branding.designSystem (reliably wrong)
---
```

*`schema_version` is the **contract version** this profile was written against — currently `1`. Bump it only on a **breaking** change to this schema (a removed/renamed field, or a closed-set value whose meaning changed); purely additive changes don't bump it. Old profiles keep their existing number until migrated, so a reader can tell which contract a profile obeys instead of mistaking a pre-existing gap for missing data.*

*`favicon` and `website_url` are **derived from `domain`** at read time — never stored.*

*Relations (`parent` / `owns`) hold the canonical **domain slug** of the related entity (the store-key form, e.g. `kenvue.com`) so the rung-3 index can JOIN on it. If the related entity has no resolvable domain of its own (a brand folded under the parent's site; a holding co with no site), record its **name in quotes** and accept it's un-joinable until it earns a domain — never mix a bare name and a domain as if both were keys.*

*`site_notes` is **carry-forward only**: durable, site-specific facts the next capture needs (JS-walled nav, geo traps, where pricing hides). One-time run narration ("no contamination this run," credits spent) belongs in the **Provenance** body section, not here. It's how the next run inherits the playbook instead of re-discovering it.*

*Visual identity is **evidence to verify, not gospel.** `branding.colors` has no positional *or* presence guarantee — it can surface UI chrome, miss the true brand hue entirely, or capture an ephemeral campaign color; retain the palette but confirm the real brand color against the screenshot and write the read in **Visual & brand impression**. Read `design_framework` from `rawHtml`, not `branding.designSystem` (reliably wrong across the corpus). `logo_url` falls back to the favicon when `branding.images.logo` is empty or an inline data-URI.*

## `profile.md` — body

Prose flexes where enums can't — write each section for the company in front of you.

| Section | What goes here |
|---|---|
| **Overview** | 2–4 sentences: what they do, who for, how. Synthesized across pages, not the meta tag. |
| **What they offer** | The *shape* of their offerings (lines/categories). Point to `offerings.md` for per-offering detail. |
| **How it works / model** | Customer journey (e.g. quiz → consult → subscription) + how they make money + delivery. |
| **Positioning & audience** | Who they target, against whom, their claimed edge. Brief — deep voice work goes to `brand.md`. |
| **Nav structure** | Their own taxonomy, as a nested list with URLs. Capture the **complete** nav — mega-menu flyouts and dropdowns included; it's the best signal of their offering hierarchy. |
| **Credibility & proof** | Trust signals: press logos, certifications, # customers, guarantees, testimonial presence. |
| **Provenance** | Pages analyzed, capture method per page, and what you couldn't get. |

**Optional (only when there's real signal):**

| Section | What goes here |
|---|---|
| **Visual & brand impression** | The screenshot-derived read: design maturity, imagery, motifs, overall feel. |
| **Strategic read** | The "so what" — anything distinctive, surprising, or strategically relevant. |

<details>
  <summary>Positive examples — the level of synthesis expected</summary>

  > Examples are **shortened for brevity**. Real captures should be complete — especially **Nav structure**, which should include the full mega-nav (every flyout/dropdown), not a trimmed sample.

  **Overview**
  > A DTC men's-health telehealth brand. It pairs at-home lab testing with licensed-clinician oversight to deliver TRT, weight-loss, and longevity programs on a monthly membership. Positions as a clinical, data-driven alternative to both in-person clinics and lighter "wellness" telehealth.

  **What they offer**
  > Three lines, all subscription: **Hormone therapy** (TRT, anchored on at-home bloodwork), **Weight loss** (GLP-1 + orals), **Longevity/peptides** (Sermorelin, NAD+). Labs are the wedge — most journeys start with a panel. Per-offering detail in `offerings.md`.

  **Nav structure**
  > ```
  > - Treatments
  >   - TRT — /hormone-therapy/trt
  >   - Weight loss — /weight-loss
  > - How it works — /how-it-works
  > - Membership — /membership
  > ```

</details>

## Tier-1 modules (opt-in, separate docs)

Only written when a project enables them. Same frontmatter discipline; own `captured_at`.

- **`offerings.md`** — the product / service index. One `### <offering>` per item: URL, one-line description, pricing (verbatim), form/delivery, notable claims. Discover **breadth-first** (one per line/family before variants); the primary offering often shares the company name — list it first. *This structure is the cross-brand query fidelity lever — keep headings consistent.*
- **`brand.md`** — the interpretive brand layer: voice/tone, personality (seed from Firecrawl `branding.personality`), positioning narrative, typography. The richer read that doesn't belong in `profile.md`'s scalars.

*Detailed schemas land when the first project enables them — deferred on purpose. (The seed for `offerings.md` is [`_design/references/doro-product-analysis-prompt.md`](_design/references/doro-product-analysis-prompt.md).)*
