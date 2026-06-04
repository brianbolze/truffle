# OFFERINGS.md — the `offerings.md` module contract

> **What this is.** The living contract for the opt-in **`offerings.md`** module — the per-SKU/molecule roster a project writes when `profile.md`'s family-grain *What they offer* line is too coarse. This is the spec you **obey** when authoring a `store/<domain>/offerings.md`; the *why* (intent, decisions, principles) is the design record [`_design/2026-06-03-offerings.md`](_design/2026-06-03-offerings.md).

> **CAPS vs lowercase.** `OFFERINGS.md` (this file, repo root) = the **contract**. `store/<domain>/offerings.md` = the **instances** that obey it. Same word, two roles — the case tells them apart.

*Companion to [`SCHEMA.md`](SCHEMA.md) (the always-on `profile.md` contract), [`TAXONOMIES.md`](TAXONOMIES.md), and [`QUERYING.md`](QUERYING.md). A **module** = a gathering recipe + a schema + a destination; this doc is the schema half. The other halves live where they belong: capture recipe → [`firecrawl-capture.md` §1.1](skills/research-company/firecrawl-capture.md); lint → [`scripts/offeringscheck.py`](scripts/offeringscheck.py); instances → `store/<domain>/offerings.md`.*

> **Module convention (forward-looking).** Module contracts are top-level CAPS files; this is the first. At the **second** real module schema (`brand.md` or another), `git mv` the CAPS contracts into a `modules/` directory and repoint — *two contracts earn the directory; one does not.*

## When to write it

Opt-in — **enablement = the file exists** (no config mechanism). Write `offerings.md` for a company **only** when a cohort's consumer needs the per-SKU/molecule grain a `profile.md` family line collapses ("who's cheapest for compounded semaglutide, and is the price even public?"). **First enabled set: the telehealth cohort.** Default everywhere else: **don't write the file** — `profile.md`'s *What they offer* lines + the per-line `price_visibility` token ([SCHEMA 2.3](SCHEMA.md#price-visibility)) remain the family-grain convention. When `offerings.md` is active for a company it **owns `price_visibility` per-SKU**.

**Hard floor — decline even on request.** A pure-services / bespoke company — no published price and no enumerable SKU (a consultancy whose "products" are confidential client work) — has nothing for the roster to bind, so **don't write the file even when a guided run asks for it**. `profile.md`'s *What they offer* lines + their per-line `[on-request]` tokens are the complete, correct altitude; **record the decline** in `## Provenance` → `### Run profile` (`Skipped with reason: …`). A reasoned decline is a valid, recorded outcome — not a gap. *(Seed exemplar: [`store/ideo-com/profile.md`](store/ideo-com/profile.md).)*

## Frontmatter — doc-meta only

The offerings live in the body; frontmatter is just doc-meta, with **its own `captured_at`** (pricing goes stale fast — the reason this is a separate module from `profile.md`).

```yaml
---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: hims.com            # company key; each offering's slug (its relative url) is its key *within* the company
captured_at: 2026-06-03     # own freshness; captures/<date>/ holds the source pages
site_notes: "Catalog lives in the JS bundle, not nav; prices PDP-only (budget ~1 scrape/SKU); prices A/B-flicker $64↔$65 — re-check next run."
---
```

**`site_notes` is carry-forward only** — the offerings-capture playbook the next run inherits: where the real catalog lives (CMS REST / an `app.` subdomain / a SPA bundle registry / nav+census), where prices hide, what's A/B-volatile or worth a diff. One-time run narration (credits, runtime, "no contamination this run") stays in `## Provenance`, **never here** — same discipline as `profile.md`'s `site_notes`. *(Added in `schema_version` **1.1** — MINOR/additive; absent on a `1.0` file reads as "predates the field," not "none found." No backfill, no re-stamp.)*

## Body — roster-first

Order: `## Portfolio overview` → `## Roster` → `### Verbatim anchors` → `## Deep blocks` → `## Provenance`. The **roster is the load-bearing core**; the overview is brief; deep blocks are *earned*, never a default top-N. (Seed exemplar: [`store/hims-com/offerings.md`](store/hims-com/offerings.md).)

- **`## Portfolio overview`** — brief: how the lines relate, the "shape" finding (e.g. "this brand's 'testosterone' is an OTC supplement, not TRT"), and a **calibrated prominence read**. Tag each prominence claim `[HIGH]` / `[MED]` / `[LOW]` by signal stability: **HIGH** = the company's *own* label (a "Best seller" badge) or a corroborated hero; **MED** = section order / nav depth / CTA repetition; **LOW** = a single weak cue, a rotating/A-B-tested hero, or carousel order. Honest subjectivity beats false precision. For a `Catalog`-shape company this section *is* the main content.

- **`## Roster`** — one row per offering, **complete at the indexed level** (the level the company indexes at, never every leaf — for a `Catalog` / marketplace that means line + tier + marked exemplars, **not** the leaf SKUs; see the **Catalog / marketplace shape** note below). Columns, exactly:

  | Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
  |---|---|---|---|---|---|---|

  - **What** — **leads with `molecule · form · access`**, then a short clause. Keep the column header literally `What (molecule · form · access)` even for **molecule-free** verticals (legal / SaaS / eyewear) — vary the *cell* (lead with the form clause, molecule omitted), never the spine label, so a header-keyed digest still matches.
  - **Kind** — `family` \| `buyable` (a roster annotation, mostly derivable from `parent` + nesting).
  - **Slug** — the offering's relative URL = its **within-company key**; never blank (a no-PDP item notes `(no PDP — …)`) and **never constructed** — an attested URL from a captured page. Never asserted equal to another brand's slug.
  - **Price (verbatim)** — quoted exactly, with its footnote markers, or `—` for family rows. Never normalized. **Bundled / included-in-parent price:** a buyable leaf whose price is *inherited from a named parent* package/plan (not a family umbrella) takes the token **`incl. (<parent> $X)`** — carry the parent's verbatim price inside (e.g. `incl. (Business $20)`) so the leaf still satisfies the grep-verifiable-price rule. Its **Visibility is `published`** when the parent's all-in is the shown, self-contained price; `partial` only if a *further* mandatory cost sits on top. Reserve `—` for true family-umbrella rows — and a parent package row *is* the price card when the verbatim anchors live there.
  - **Visibility** — `published \| partial \| on-request` per SKU (`—` for family rows). The one closed set, and a **stated judgment, not a mechanism**: quote the *why* verbatim (the membership footnote, the "From $X" dose-floor, the med-bought-elsewhere note) in the Price cell or a Verbatim anchor — cross-brand consistency is **query-time, never forced at capture**. Default tree: `partial` = the all-in isn't fully shown (a mandatory separate cost like membership, the med bought elsewhere, **or** a floor that moves materially with dose/tier); `published` = the shown number is the full, self-contained price; `on-request` = no price shown (intake / quiz / consult / lab-gated). A self-valuation ("$X if bought separately") is not a price → `on-request`. A **published maker/manufacturer floor** whose final price is set by a *third party* (dealer / marketplace markup, destination, fees) stays `published` — distinguish it from a *same-seller* hidden mandatory cost (a membership, a required add-on), which is `partial`.

- **Catalog / marketplace shape (the un-enumerable-leaf case).** For a `Catalog` or a host/seller-priced **marketplace**, *complete at the indexed level* means **line + pricing-tier + marked flagship exemplars — never the leaf SKUs** (the same rule as "shape + exemplars only" in [Capture & depth](#capture--depth) — stated once, here). Mark a representative row `*(exemplar)*`. Where a leaf has no canonical URL, its within-company key may be a **stable non-URL id**, written `(no PDP — <tag/partner-id>)` (e.g. a marketplace service-tag id). Availability ("coming soon") rides inside `What` — **not** a new column or a new visibility value.

- **`### Verbatim anchors`** — the footnotes the Price column points at (the `†`/`*` membership + dose notes that *decide* `partial` vs `published`), quoted exactly, plus a molecule-sourcing audit for any `not stated`.

- **`## Deep blocks`** — **earned, not default**. A rich block ONLY where a verbatim H1 / exact price footnote / disambiguation resolves a real ambiguity a roster row can't (a gated line whose only price is an FAQ figure; a "this isn't actually TRT" disambiguation). Spine line, then verbatim gold. If nothing earns one, say so (*"None earned — the roster carries this company"*).
  - **Two block types — don't conflate them.** A *per-SKU deep-dive* is earned **only on ambiguity** (above), **never** a per-flagship quota — the quota manufactured padding ([pilot triage §C](_design/retro/offerings/2026-06-03-offerings-pilot-triage.md)). A *PDP-template anatomy* — **one** block per company that maps the repeated PDP shell so reading one teaches the whole catalog ([Hone exemplar](store/honehealth-com/offerings.md)) — is a **portfolio-level finding**: high-signal to a copy/structure consumer (website-building), near-useless to a price consumer. So it's an **opt-in archetype, not a default** — include it only when a run asks for it, and record that in the `### Run profile` note. It earns its place by the *cross-SKU template read*, not by re-quoting one page (the raw PDP it distills already sits verbatim in `captures/`).
  - **Hero image — opt-in asset, never a column.** A flagship's deep block may reference a captured **hero product render** at `captures/<date>/images/<sku>.<ext>` — a clean isolated product shot for a design / rendering-reference consumer. Capture recipe → [`firecrawl-capture.md` §1.1](skills/research-company/firecrawl-capture.md) (`fc.py hero`); opt-in per run, noted in the `### Run profile`. Default runs skip it.

- **`## Provenance`** — pages read (the cited captures), scope (what's enumerated vs noted-but-not-enumerated), gated/unreachable, and a point-in-time-snapshot caveat (pricing runs promo/A-B). Plus a **`### Run profile`** line **when the run was non-vanilla** — what a custom prompt changed vs. a plain run (added columns, an opt-in PDP-anatomy block, a deeper cut on one line). One or two lines; **absent reads as vanilla**, not "unknown." This is one-time run narration — forward-carry capture intel still goes to `site_notes`, the same split `profile.md` keeps.

## The rules (what the lint enforces)

`python3 scripts/offeringscheck.py --slug <slug>` is the gate — it must pass. The load-bearing rules:

1. **Grep-verifiable price.** Every `$` amount in the file must be findable verbatim in a cited `store/<domain>/captures/` page. A verbatim number can't survive the grep if it was invented — this is the misattribution guard, and the exact slip the design probe caught.
2. **Molecule + form page-attested only.** Record the molecule only where a captured page states it for *that* SKU; else **`not stated`**. **Never infer a molecule from the brand name** (a brand tagged with a molecule no page names is the other slip the probe caught).
3. **Gating is a finding.** A quiz / membership / app-gated SKU still gets a row — the floor that *is* shown + the `[partial]`/`[on-request]` token.
4. **No cross-company canonical key.** Molecule rides inside `What`, page-attested; it is **not** a lead column, **not** a stored canonical entity, **not** a frontmatter key. Cross-brand grouping ("semaglutide across brands") is **query-time** `rg` ([QUERYING Recipe 4](QUERYING.md)), never reconciled into a stored key.
5. **Structural** — every row slug-keyed, the closed visibility set, the roster columns all present.

**What you can customize — and what you can't.** The five rules above + the seven-column spine are the **inviolable, universal contract**: every cross-company query (`rg` / digest) leans on them, so they hold on *every* file. **Above** that line a project may **add** — a **project-local grouping column** (e.g. Notion's `Category` = its product-vs-feature axis), deep-block types, a deeper cut on one line — to fit its vertical or consumer. The lint checks the spine is **present, not exclusive** (only a standalone `Molecule` column or a canonical-key frontmatter field trips it, rule 4), so additive columns **pass the gate cleanly** — customize without fear of `offeringscheck.py`. **The line is semantic, not lexical:** a *within-company* grouping (meaningful only inside this company) is fine; a *cross-company canonical* `Category` — one stored key meant to mean the same across brands (to group "semaglutide" / "GLP-1" across companies) — is the rule-4 key the architecture refuses, derived at **promotion time**, never stored in the roster. Two disciplines on any addition: it stays **project-local** (invisible to cross-company queries — by design, not by accident), and the deviation from a vanilla run is named in the `### Run profile` note ([Body](#body--roster-first) → `## Provenance`). *(This refines the telehealth pilot's "no Form/Category" lock — that lock targets the cross-company **canonical** key, not a project-local grouping column; see [non-Rx triage](_design/retro/offerings/2026-06-04-non-rx-triage.md).)*

## Capture & depth

The gathering recipe — the enumeration ladder, the `portfolio_shape` depth dial, and the prominence capture flags — lives with the verb: [`firecrawl-capture.md` §1.1](skills/research-company/firecrawl-capture.md). In brief: enumerate the roster off the category/index page (the cheapest authoritative backbone, which doubles as the prominence read), deepen only the flagships, and read prominence **at capture time** (full-page screenshot + `rawHtml`, before payloads prune). Depth follows `portfolio_shape`: `Single` ~4–6 SKUs · `Flagship + companions` / `Multi-product` → the whole set, top-N rich · `Catalog` → shape + exemplars only, never the SKUs (this *is* the roster's "indexed level" for a Catalog — see [`## Roster`](#body--roster-first)).
