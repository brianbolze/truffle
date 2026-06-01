# SCHEMA — the store contract

> **Current contract version: `2.1`.** This is what new captures stamp as `schema_version`. Bump rules + the version history are in the `schema_version` note below (under the frontmatter block).

> **What this is.** The contract between *capture* (a `/research-company` agent writes it) and *query* (any agent reads it). It's written to be read by an Opus-class agent that has the **whole capture** in context — multiple pages, screenshots, and the Firecrawl `branding` + `metadata` payloads — not a quick homepage skim.

*Companion: [`TAXONOMIES.md`](TAXONOMIES.md) holds the closed value sets; [`QUERYING.md`](QUERYING.md) is the consume-side companion (how to read profiles back). Scope: commercial companies + products.*

> **Drift guard.** Renaming a field, changing the frontmatter format, or renaming a body section breaks [`QUERYING.md`](QUERYING.md)'s recipes — update it and run `scripts/querycheck.py`. (Changing a closed-set *value* lives in TAXONOMIES and does not affect QUERYING.)

## How to write a profile (capturing agent)

- **Describe the company, not the engine.** A profile records what the company *is* — never commentary about the schema itself. Observations about the contract (missing values, taxonomy gaps, capture-tooling quirks) go to [`BACKLOG.md`](BACKLOG.md), not into prose or comments. The one exception is the inline `# STRAIN:` note on a frontmatter line, which explains *that field's* value to a grep-consumer in a few words.
- **Everything traces to the capture.** Fill only what the captured pages support; else `unverified_fields`, never a guess. Every fact — *especially* volatile ones (prices, counts, dates, "current X") — must point to a captured page: greppable in the markdown or legible in a screenshot. Can't point to where it came from? It doesn't go in. And don't invent a reason or date to reconcile two captures that disagree — report the discrepancy. The lone exception: a prior used purely to **resolve identity** (a ticker, the domain behind a named brand) may land *marked* on the `Enriched (model knowledge)` Provenance line — kept near-empty, never for what the company does, sells, or claims. *(Funding stage, headcount, revenue are rarely on a marketing site — leave them out; that's a deep-research job, not this one.)*
- **Verbatim where the exact words are the data.** Quote, don't paraphrase, wherever the wording or number is itself the signal — prices and tiers, the company's own product and category names, quantified or regulated claims, proof points, guarantees, named certifications and partners (among others). A verbatim string can't survive the grep if it was invented, and it stops a prior leaking into a paraphrase. Paraphrase only connective prose.
- **Use the screenshots.** The visual read (design maturity, imagery, tone) is yours to make and a text scraper can't. Write it in *Visual & brand impression*.
- **Reconcile across the whole site you captured.** The homepage is one input, not the answer. Apply this to every section, not just the first.
- **Prominence is an observation, not a verdict.** Record what a site foregrounds — hero, repeated CTAs — as what they make *salient*; never infer flagship status, market position, or adoption from placement. Who leads a market is a consumer-layer call, not capture.
- **Keep each body section tight** — a few sentences or bullets. Earn a section with evidence; omit it rather than pad with "N/A".
- **Write the body to be queried, not just read** — enumerable lists (offerings, plans, proof-points) **lead each line with a bold `name:`** + verbatim value (see *body*, below); interpretive prose stays prose. Don't template sections — shape the lists.

## `profile.md` — frontmatter

Stable, queryable, cheap. Closed-set fields draw from [`TAXONOMIES.md`](TAXONOMIES.md); leave any undetermined field empty.

```yaml
---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.0"                # contract MAJOR.MINOR this profile obeys; querycheck warns if it outruns SCHEMA's current version (see note below)

# Identity
domain: honehealth.com               # primary key
name: Hone Health
aliases: []                          # alt names/domains of the SAME entity (rebrand + M&A escape hatch)
parent: []                           # domain SLUG(s) this is a subsidiary / brand-of — from footer/©/about. Empty if top-level. (See relations note.)
owns: []                             # domain SLUG(s) of sub-brands / subsidiaries this entity owns. Empty if none. (See relations note.)
socials: {}                          # external profiles when present: linkedin/x/instagram/youtube/facebook/tiktok -> URL. Seed from rawHtml JSON-LD `sameAs`, else footer/header anchors; verify each resolves to THIS entity. (See structured-layer note.)

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
specialties: []                      # open-vocab tags of what they're known for (e.g. [Endocrinology, Menopause, Andrology]) — NOT a closed set, NOT in TAXONOMIES. The fine vertical tag the coarse closed sets can't carry. Seed from JSON-LD `medicalSpecialty`/`applicationCategory` or prose; empty if undetermined.

# Visual identity — Firecrawl `branding` is a hint to verify, never source-of-truth; confirm against the screenshot (see note).
logo_url: https://honehealth.com/...  # branding.images.logo, else favicon fallback (it's often empty / a data-URI)
brand_colors: { primary: "#0E3A2F", accent: "#C7A867" }  # retain the palette; confirm the real hue visually (see note)
fonts: [Söhne, Tiempos]              # usually branding.fonts[0] — but verify (generic "sans-serif" can rank first)
color_scheme: light                  # light | dark
design_framework: next.js            # read from rawHtml (__NEXT_DATA__, /_next/), not the branding payload
---
```

*The first frontmatter line is a fixed pointer to [`QUERYING.md`](QUERYING.md) — **identical boilerplate on every profile**, so an agent that opens a `profile.md` cold (a deep path that never passed the store README) still finds the query contract. It's a YAML comment (the parser ignores it) and is store infrastructure, not a description of the company — carry it forward verbatim; the "describe the company, not the engine" rule doesn't reach a fixed template pointer.*

*`schema_version` is the contract the profile obeys — the field / value / section set, **not** the prose docs (a docs-only edit like wording changes nothing). It's `MAJOR.MINOR`:*
- ***MAJOR*** *(`1`→`2`) — a **breaking** change: a field removed/renamed, or a closed-set value whose meaning changed. Old profiles are now non-conformant — migrate `store/`, re-capture where needed, **re-stamp every profile to the new version**, run `scripts/querycheck.py`.*
- ***MINOR*** *(`1.0`→`1.1`) — an **additive**, backward-compatible change: a new optional field, value, or section. **No backfill, no re-stamp** — grandfather the old number, so an empty new field in an older profile reads as "predates the field," not "missing data."*

*Store it as a quoted string (e.g. `"2.0"`) so a future `"1.10"` doesn't collapse to the float `1.1`. The stamp is **the version a profile was authored or last migrated under** — a MAJOR re-stamps the whole store as its closing step, so the number always answers "does this obey the current contract?" Grandfathering (leave the old number) is **MINOR-only**, where an empty new field must still read as "predates it." New captures stamp the current contract version (above), quoted.*

*<a id="schema_version-note"></a>**Version history** — the referent that makes a bump mean something: a reader compares their profile's number to this list (not a `git blame`) to read an empty field as "predates it" vs "missing." Append one line per bump.*
- ***1.0*** *— initial contract: the identity / capture-meta / classification / visual-identity frontmatter and the body sections defined in this doc.*
- ***2.0*** *— `offering_category`: renamed `Hardware / Physical Products` → `Physical Products / Hardware`, removed `Apparel & Footwear` (folded physical-goods makers — watches, apparel — into Physical Products), added per-value exemplars + a maker-vs-reseller rule. Re-mapped 9 profiles' values; re-stamped all 44 to `"2.0"`.*
- ***2.1*** *(MINOR, additive — no backfill, grandfathered) — added `socials` + `specialties` frontmatter fields and the **Structured layer** read (enrichment now mines `rawHtml`'s JSON-LD + `<header>`/`<nav>` region as a hint-to-verify source). Older profiles read empty on the new fields = "predates the field." See the [signal audit](experiments/2026-06-01-signal-audit/FINDINGS.md).*

*`favicon` and `website_url` are **derived from `domain`** at read time — never stored.*

*Relations (`parent` / `owns`) hold the related entity's canonical **dotted domain** (e.g. `kenvue.com`, or a subdomain like `gshock.casio.com`) — **not** the dashed dir-slug. A JOIN folds the value to the store-slug with the same lowercase + dots→dashes rule the dirs use (`canon()` in [`scripts/store.py`](scripts/store.py)), so the two forms can never silently miss each other. No resolvable domain (a brand folded under the parent's site; a holding co with no site)? Record the **name in quotes** and accept it's un-joinable until it earns one — never mix a bare name and a domain as if both were keys.*

*`site_notes` is **carry-forward only** — durable, site-specific facts the next capture needs (JS-walled nav, geo traps, where pricing hides), so the next run inherits the playbook instead of re-discovering it. One-time run narration ("no contamination this run," credits spent) belongs in the **Provenance** body section, not here.*

*Live-variable capture — when a site **A/B-tests, rotates, or geolocates** what it serves, the captured prices / hero copy / which modules render are **real but unstable** (they differ next run). Flag it in two fixed spots, never ad hoc: (1) a stock **`A/B: <tool>`** token in `site_notes` when an experimentation tool is fingerprintable (`A/B: VWO`, `A/B: Optimizely`; `A/B: yes` if you see the behavior but can't name the tool) — the carry-forward cue that the next run hits the same flicker (and the tool's blob as markdown noise); (2) one `unverified_fields` line carrying the literal **"point-in-time snapshot, not fixed"** plus the cause: `"Prices/IA are a point-in-time snapshot, not fixed — <cause>."` Rotation, geolocation, or plan/dose variance take the snapshot line but skip the `A/B:` token (no tool to name). Keeps "is this capture volatile?" greppable without a new field.*

*Visual identity — the `branding` payload is a **hint, not a source of truth**: seed from it, but verify every field rather than copy it. `branding.colors` has no positional or presence guarantee — it can surface UI chrome, miss the true brand hue, or catch a campaign color; retain the palette but confirm the real one against the screenshot and write the read in **Visual & brand impression**. Read `design_framework` from `rawHtml`, not the `branding` payload. `logo_url` falls back to the favicon when `branding.images.logo` is empty or an inline data-URI.*

*<a id="structured-layer"></a>**Structured layer (`rawHtml` JSON-LD + nav) — same hint-to-verify discipline as `branding`.** The homepage's `<script type="application/ld+json">` block is company-authored, verbatim identity data that markdown drops; the `<header>`/`<nav>` region carries the mega-nav hierarchy markdown flattens. `scripts/fc.py signals --slug <slug>` slices both out of the persisted homepage payload (a deterministic grep + pretty-print — **not** extraction; no reducer/LLM/Pydantic, so the anti-Doro line holds), targeted so enrichment reads a few KB, never the 2 MB blob. It maps onto schema surface as:*
- *`sameAs` → **`socials`** (the standout — most profiles carry none today); also yields wikipedia/crunchbase/trustpilot URLs (identity-resolution hooks, not socials — leave for a consumer).*
- *`alternateName` + `legalName` → **`aliases`** — both are alt names of the same entity (`legalName` "Time Therapeutics, Inc." for Hone Health is an alias, **not** a new field).*
- *self-reported `AggregateRating` → **Credibility & proof**, verbatim + flagged self-reported (the section already mandates this).*
- *`medicalSpecialty` / `applicationCategory` → **`specialties`**.*
- *`logo` → the front of the `logo_url` source chain (cleaner/higher-trust than the favicon fallback).*
- *the slimmed `<header>`/`<nav>` region → **Nav structure** — recover the flyout tree, then **validate completeness against the homepage screenshot** (ground truth; a label present in the HTML ≠ hierarchy captured). No `<header>`/`<nav>` element (nav in a bare div)? Rebuild from the screenshot.*

*It's **self-authored** ⇒ confirm every value against the page/screenshot before it lands — it can be marketing-shaped (a combined brand folded into `alternateName`), stale, or absent (≈¼ of homepages ship none). **Founders / founding-date stay at the deep-research edge** — land trivially-present ones in prose (Overview) where they already go, never as a frontmatter field.*

## `profile.md` — body

Prose flexes where enums can't — write each section for the company in front of you. But the body is also an **index** other agents grep, so wherever a section lists *the same kind of thing* (offerings, plans/tiers, proof-points, the Provenance fields), **lead each line with a bold name/label, then a colon, then the content — with any price/metric quoted verbatim**:

> `- **<name or label>:** <what it is, price/metric verbatim>`

The bold lead-in is the load-bearing part — `rg '^- \*\*'` enumerates the items, and the verbatim value puts the price on the line. The separator isn't policed (an em-dash reads better than a colon for some name–detail lines; fine — the bold lead-in is what matters). Interpretive sections (Overview, Positioning, Strategic read, Visual) are exempt — don't template them.

| Section | What goes here |
|---|---|
| **Overview** | 2–4 sentences: what they do, who for, how. Synthesized across pages, not the meta tag. |
| **What they offer** | Enumerate the offering lines/families as **bold-led** lines (`- **Name:** …`), pricing verbatim where shown — breadth + shape here, per-SKU depth defers to `offerings.md`. |
| **How it works / model** | Customer journey (e.g. quiz → consult → subscription) + how they make money + delivery. |
| **Positioning & audience** | Who they target, against whom, their claimed edge. Brief — deep voice work goes to `brand.md`. |
| **Nav structure** | Their own taxonomy, as a nested list with URLs. Capture the **complete** nav — mega-menu flyouts and dropdowns included; it's the best signal of their offering hierarchy. |
| **Credibility & proof** | Trust signals: press logos, certifications, # customers, guarantees, testimonial presence. Capture self-reported proof ("trusted by 10M") **verbatim and flagged self-reported** — record the claim, never endorse it as fact. |
| **Provenance** | A fixed, greppable set — one line each: **Pages** (analyzed + method) · **Verify** (sourceURL + md5 result) · **Credits** spent · **Couldn't get** (what + why). Optionally **Enriched** (model knowledge) — *only* the rare identity prior taken from the model, not the page (e.g. `Enriched (model knowledge): ETSY ticker; Reverb→reverb.com`); distinct from `unverified_fields` ("couldn't get it"), this is "got it — from the model, not the site." Optionally **Migrations** — added only to a profile a later migration *rule-rewrote* (not re-captured), one line per migration: date, version delta, value before→after (see [Migrations](#migrations)). |

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
  > Three lines, all subscription (bold lead-in; no public price on these):
  >
  > - **Hormone therapy:** TRT, anchored on at-home bloodwork
  > - **Weight loss:** GLP-1 injections + orals
  > - **Longevity / peptides:** Sermorelin, NAD+
  >
  > Labs are the wedge — most journeys start with a panel. Per-offering detail in `offerings.md`.

  **Nav structure**
  > ```
  > - Treatments
  >   - TRT — /hormone-therapy/trt
  >   - Weight loss — /weight-loss
  > - How it works — /how-it-works
  > - Membership — /membership
  > ```

</details>

## Migrations

When a **MAJOR** bump (see `schema_version`) makes existing profiles non-conformant, migrate the store in one pass. Steps:

1. **Edit the contract** — update [`SCHEMA.md`](SCHEMA.md) / [`TAXONOMIES.md`](TAXONOMIES.md), bump the *Current contract version* at the top, add a Version-history line.
2. **Re-map values** in `store/` — change only the affected fields; never re-write prose a migration can't justify.
3. **Mark what you rewrote** — append a **Migrations** line to the Provenance section of *every profile whose values changed* (date, version delta, before→after). This preserves the trust chain: a migrated value traces to a *rule*, not to that capture.
4. **Re-stamp all profiles** to the new version (the migration's closing step) — a uniform stamp is the signal that the whole store obeys the current contract.
5. **`python3 scripts/querycheck.py --strict`** — proves every value conforms; this is what makes the re-stamp honest.
6. **Commit** as one logical change; the diff is the record (no separate migration script kept unless it's genuinely non-trivial).

*MINOR/additive bumps skip all of this — no re-map, no re-stamp (grandfather the old number).*

## Tier-1 modules (opt-in, separate docs)

Only written when a project enables them. Same frontmatter discipline; own `captured_at`.

- **`offerings.md`** — the product / service index. One `### <offering>` per item: URL, one-line description, pricing (verbatim), form/delivery, notable claims. Discover **breadth-first** (one per line/family before variants); the primary offering often shares the company name — list it first. *This structure is the cross-brand query fidelity lever — keep headings consistent.*
- **`brand.md`** — the interpretive brand layer: voice/tone, personality (seed from Firecrawl `branding.personality`), positioning narrative, typography. The richer read that doesn't belong in `profile.md`'s scalars.

*Detailed schemas land when the first project enables them — deferred on purpose. (The seed for `offerings.md` is [`_design/references/doro-product-analysis-prompt.md`](_design/references/doro-product-analysis-prompt.md).)*
