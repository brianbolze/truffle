# Design: the `offerings.md` module — the per-SKU roster

> **What this is.** The per-SKU/molecule roster a project writes when `profile.md`'s family line is too coarse —
> and the *why* behind it. The spec you *obey* is [`OFFERINGS.md`](../OFFERINGS.md); this doc is the reasoning.
> Companion to the [frame](2026-05-29-frame.md) (engine scope) and [architecture](2026-05-30-architecture.md) (lifecycle).

## Why it exists

`profile.md` already says *what a company sells* — but only at **family grain** (its level of detail): one
bullet for a brand's six GLP-1 SKUs, no room for six prices. `offerings.md` is the
per-SKU layer for the question family grain can't answer:

> **"Who's cheapest for compounded semaglutide, and is the price even public?"**

**Both modules stay — they answer different questions and don't overlap.** The `profile.md` family line wins the
fast scan across all companies ("which brands sell GLP-1s?"); the per-SKU roster wins the price read ("who's
cheapest, is it public?"). We tested "just extend `profile.md`" head-to-head in the **tournament** (three
candidate designs — roster-first, extend-`profile.md`, and a molecule-keyed pivot — cold-judged by agents over
four telehealth brands): the separate roster won **8.3 to 5.5**, and was the only design that priced *all four*
brands' GLP-1s.

It's **durable State** — what the company sells, from its own pages — keyed *within* the company by slug, opt-in
per cohort, with its own freshness TTL. And it's **near-free over the baseline capture** (same category and PDP —
product-detail — pages, no new endpoints), which is why it's a separate module, not a heavier `profile.md`.

*(Doro, referenced throughout, is the prior PE-era research tool whose heavy entity-resolution machinery the
engine deliberately refuses — see [`engine-dev.md`](../.claude/rules/engine-dev.md).)*

## The file, in order

**Roster-first:** `## Portfolio overview` → `## Roster` → `### Verbatim anchors` → `## Deep blocks` →
`## Provenance`. The roster is the load-bearing core; the overview is brief; deep blocks are earned. The full
shape and the exemplar live in [`OFFERINGS.md`](../OFFERINGS.md).

## Key decisions

The settled calls, each with its one-line *why*. (Which probe settled what is in the decision log below.)

- **The win is the roster, not the rich blocks.** Cold agents answered the price query straight from the roster;
  deep blocks earned a few correctness cells, else merely restated roster prices. So lead with the roster, demote
  blocks to earned.
- **Molecule rides `What`, page-attested — never a column, key, or frontmatter field.** The molecule-pivot design
  gained zero resolution, invented canonical names no page supported, and botched its own slugs. Cross-brand
  grouping ("semaglutide across brands") is query-time `rg`, never a stored key — the same move that lets us skip
  company entity-resolution.
- **Deep blocks come in two types, and neither is a quota.** A *per-SKU dive* is earned only on a real ambiguity a
  roster row can't carry (a gated line whose only price is an FAQ figure; a "this isn't TRT" disambiguation). A
  *PDP-template anatomy* is one opt-in block per company mapping the repeated page shell — a portfolio-level
  finding, gold to a copy/structure consumer, near-useless to a price one. A fixed 2–3-per-run quota just
  manufactures padding.
- **The visibility token is a stated judgment, not a mechanism.** Quote the *why* verbatim; cross-brand
  consistency is a query-time concern. Across the six-run pilot the same "From $X" shape got opposite tokens
  brand-to-brand — so one mechanical rule would be false precision.
- **Seven roster columns; `Form`/`Category` rejected.** They duplicate `What`, reintroduce the cross-company
  canonical key the engine refuses, and break worst on broad and platform catalogs. The Notion mapping is derived
  at promotion time, never stored in the roster.
- **Complete at the indexed level, never every leaf.** Hims's 70+ biomarker leaf-pages are one panel plus an
  add-on — two rows. The roster stops where the catalog begins.
- **Depth scales with `portfolio_shape`.** `Single`/`Flagship + companions`/`Multi-product` enumerate the set;
  `Catalog` gets shape + exemplars, never the SKUs. Directional, not strict — if a deep dive contradicts the
  field, correct `profile.md`. The dial lives with the [capture recipe](../skills/research-company/firecrawl-capture.md).
- **`site_notes` carries the capture playbook forward; a `Run profile` note flags non-vanilla runs.** Where the
  catalog actually lives, where prices hide, what's volatile — the next run inherits it. One-time narration
  (credits, what a custom prompt changed) stays in `## Provenance`. The same split `profile.md` keeps.
- **Promotion to Notion is propose-only, deferred** — a roster row maps cleanly to Products/SKUs, but that's built
  when promotion is the live task.

## Principles — why it stays light

- **Capture observations, not interpretations.** Verbatim is the anti-hallucination guard: a price that survives
  the grep against a cited capture can't be invented. Every load-bearing rule — grep-verifiable price,
  page-attested molecule, slug-from-a-real-URL — is a flavor of it.
- **There is no cross-company canonical key.** Domain keys a company; a slug keys an offering *within* one.
  Building a canonical "semaglutide" entity across brands *is* the Doro entity-resolution swamp — declined, not
  engineered. Grouping happens at query time.
- **Earn every field; derive what's free.** A field justifies itself by dividing offerings on a real question
  *and* being fillable from the page. `Form` duplicates `What`; a SKU count is `wc -l`. Neither is a field.
- **Prominence is observation, not a verdict.** Record what a site foregrounds, tagged `[HIGH]`/`[MED]`/`[LOW]` by
  signal stability; never infer market leadership — that's a consumer's call.

## What we refused, and why

<details>
<summary>The fields and structures probed, then deliberately cut</summary>

Behind the roster's seven columns sits a **nine-field design core**: six spine fields that lead every deep block,
plus three *earned* fields that live only in deep-block prose — `includes` (what's bundled), `audience`
(per-offering, ≠ the company's `target_market`), and `notes` (a verbatim catch-all).

**Cut, each after a probe:**
- **`granularity_class`** (Doro's suite/model/sku/plan enum) — it exists to resolve product *references across
  sources* ("Office" vs "Excel" in a transcript). We capture one site in one pass and never reconcile, so the
  level is a capture-time judgment (`parent` + nesting), not a stored key.
- **A `{unit, value, cadence}` price struct + a `pricing_model` field** — the price *value* never generalizes (a
  watch's MSRP, a SaaS seat, a telehealth all-in share no unit), so price stays a verbatim string; heavy
  normalization is project-side, per messy vertical.
- **`Form` / `Category` Notion columns** — duplication plus a cross-company key (above); derive at promotion.
- **Per-SKU depth for `Catalog` companies, and `competitors` / `status` / `launched_year`** — out of scope by
  design: a catalog is indexed at the category level, and the rest is Signals or Judgments, not State.

</details>

## Decision log

<details>
<summary>How the design got here — three milestones</summary>

- **2026-06-01 — the draft.** A 5-shape hand-capture probe + Doro's product schema, pruned to the engine's
  anti-heavy line → the nine-field core, identity-keyed-within-company, price-as-one-field. Body shape was
  overview → blocks → roster; activation left open.
- **2026-06-03 — tournament + activation.** Three designs × four telehealth brands, cold-judged: roster-first
  beat extend-`profile.md` decisively, the molecule-pivot backfired → build it, store-only, telehealth first.
  Inverted the body shape (roster first, blocks earned); shipped the contract, recipe, and lint.
- **2026-06-03 — the six-run pilot.** First real runs (Hone, AgelessRx, Eden, GoGeviti, Hims, MyDrHank): the
  roster and both anti-hallucination guards held; visibility blessed as a judgment; `Form`/`Category` rejected;
  `site_notes` + `Run profile` added; slug-attested + don't-assert-silence capture rules.
  *([pilot triage](retro/offerings/2026-06-03-offerings-pilot-triage.md).)*

</details>

---

<sub>Contract → [`OFFERINGS.md`](../OFFERINGS.md) · recipe → [`firecrawl-capture.md` §1.1](../skills/research-company/firecrawl-capture.md)
· lint → [`offeringscheck.py`](../scripts/offeringscheck.py) · evidence → the
[tournament](../experiments/2026-06-03-offerings-tournament/FINDINGS.md) + the six [retros](retro/offerings/).
Consolidates `2026-06-01-offerings.md` + `2026-06-03-offerings-module.md` (both in [`_archive/`](../_archive/)).
Authored 2026-06-03.</sub>
