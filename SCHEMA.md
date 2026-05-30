# SCHEMA — the store contract

> **What this is.** The contract between *capture* (a `/research-company` agent writes it) and *query* (any agent reads it). It's written to be read by an Opus-class agent that has the **whole capture** in context — multiple pages, screenshots, and the Firecrawl `branding` + `metadata` payloads — not a quick homepage skim.

*Companion: [`TAXONOMIES.md`](TAXONOMIES.md) holds the closed value sets. Scope: commercial companies + products.*

## How to write a profile (capturing agent)

- **Fill every field the captured pages support — and only those.** If a field isn't determinable from what you captured, leave it empty and add one line to `unverified_fields`. Do not infer it from prior knowledge. *(Funding stage, headcount, revenue are rarely on a marketing site — leave them out. They're a deep-research job, not this one.)*
- **Quote verbatim anything claim- or price-bearing** — taglines, pricing, regulated claims. Paraphrase only long prose.
- **Use the screenshots.** The visual read (design maturity, imagery, tone) is yours to make and a text scraper can't. Write it in *Visual & brand impression*.
- **Reconcile across the whole site you captured.** The homepage is one input, not the answer. Apply this to every section, not just the first.
- **Keep each body section tight** — a few sentences or bullets. Earn a section with evidence; omit it rather than pad with "N/A".

## `profile.md` — frontmatter

Stable, queryable, cheap. Closed-set fields draw from [`TAXONOMIES.md`](TAXONOMIES.md); leave any undetermined field empty.

```yaml
---
# Identity
domain: honehealth.com               # primary key
name: Hone Health
aliases: []                          # alt names/domains; rebrand + M&A escape hatch

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

# Description — one sentence: what they do + for whom. Prefer their words (og:description / hero), tightened.
description: "DTC men's-health telehealth brand offering TRT, weight-loss, and longevity programs via licensed clinicians."

# Classification — closed sets (see TAXONOMIES.md). Leave empty if the site doesn't determine it.
target_market: B2C
offering_category: [Services / Consulting, Biotech / Pharma Products]   # primary first; list only for genuine hybrids
is_multi_product: true
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — lift straight from Firecrawl `branding`. Copy, don't analyze.
logo_url: https://honehealth.com/...
brand_colors: { primary: "#0E3A2F", accent: "#C7A867" }
fonts: [Söhne, Tiempos]
color_scheme: light                  # light | dark
design_framework: next.js            # from branding.designSystem; free tech signal
---
```

*`favicon` and `website_url` are **derived from `domain`** at read time — never stored. `site_notes` carries forward to the next capture: it's how the next run inherits the playbook instead of re-discovering it.*

## `profile.md` — body

Prose flexes where enums can't — write each section for the company in front of you.

| Section | What goes here |
|---|---|
| **Overview** | 2–4 sentences: what they do, who for, how. Synthesized across pages, not the meta tag. |
| **What they offer** | The *shape* of their offerings (lines/categories). Point to `products.md` for per-product detail. |
| **How it works / model** | Customer journey (e.g. quiz → consult → subscription) + how they make money + delivery. |
| **Positioning & audience** | Who they target, against whom, their claimed edge. Brief — deep voice work goes to `brand.md`. |
| **Nav structure** | Their own taxonomy, as a nested list with URLs. Order matters. |
| **Credibility & proof** | Trust signals: press logos, certifications, # customers, guarantees, testimonial presence. |
| **Provenance** | Pages analyzed, capture method per page, and what you couldn't get. |

**Optional (only when there's real signal):**

| Section | What goes here |
|---|---|
| **Visual & brand impression** | The screenshot-derived read: design maturity, imagery, motifs, overall feel. |
| **Strategic read** | The "so what" — anything distinctive, surprising, or strategically relevant. |

<details>
<summary>Positive examples — the level of synthesis expected</summary>

**Overview**
> A DTC men's-health telehealth brand. It pairs at-home lab testing with licensed-clinician oversight to deliver TRT, weight-loss, and longevity programs on a monthly membership. Positions as a clinical, data-driven alternative to both in-person clinics and lighter "wellness" telehealth.

**What they offer**
> Three lines, all subscription: **Hormone therapy** (TRT, anchored on at-home bloodwork), **Weight loss** (GLP-1 + orals), **Longevity/peptides** (Sermorelin, NAD+). Labs are the wedge — most journeys start with a panel. Per-product detail in `products.md`.

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

- **`products.md`** — the product/offering index. One `### <product>` per offering: URL, one-line description, pricing (verbatim), form/delivery, notable claims. *This structure is the cross-brand query fidelity lever — keep product headings consistent.*
- **`brand.md`** — the interpretive brand layer: voice/tone, personality (seed from Firecrawl `branding.personality`), positioning narrative, typography. The richer read that doesn't belong in `profile.md`'s scalars.

*Detailed schemas for these land when the first project enables them — deferred on purpose.*
