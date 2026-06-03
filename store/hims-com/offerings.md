---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: hims.com            # company key; each offering's slug (its relative url) is its key *within* hims
captured_at: 2026-06-03     # own freshness; captures/2026-06-03/ holds the source pages
---

## Portfolio overview

Hims (Hims & Hers, NYSE: HIMS) is **Multi-product** — six co-equal condition lines (weight loss, sexual
health, hair loss, testosterone, mental health, labs). This doc enumerates the two with a live per-SKU
consumer — **weight loss (GLP-1)** and **testosterone** — at SKU grain; the other four are real lines but
not enumerated here (no per-SKU capture this run). Both captured lines sell the same way: a condition
*family* gates a roster of medication SKUs through an intake quiz, wrapped in a recurring membership/plan.

**The shape finding — two pricing patterns, two visibility tokens:**
- **Weight-loss SKUs are `[partial]`.** A number always shows ("From $149/mo†") but it is *medication
  only*; a separate, mandatory **Weight Loss Membership** ($39 first month → $149/mo) stacks on top
  ("Medication is not available without a membership"). The advertised price is real but never the all-in.
- **Testosterone is `[on-request]`.** No price on any card or hero; the only figure on the line — "$99/month
  for a 10-month plan paid upfront and in full" — is buried in FAQ prose, and the path is gated behind
  intake **plus** a required at-home lab. And the line is **not synthetic TRT**: it's compounded
  enclomiphene ("no synthetic testosterone needed"); real injectable TRT (cypionate) is "Coming in 2026."

**Prominence (calibrated).** Weight loss is the lead line **[HIGH]** — the category page's own hero is "The
GLP-1 pill is here," and it carries the widest lineup (two molecules, 9 SKUs across pill/pen/vial) plus the
site's GLP-1 comparison tables. Testosterone reads as a **newer, lighter line [MED]** — a single molecule
(enclomiphene), two marquee SKUs still "Coming in 2026," leaning on the same at-home-labs wedge. (Card order
within a page and rotating heroes left **[LOW]** — not used for ranking.)

## Roster

Complete at the indexed level for the two captured lines. Within-company key = **Slug**. Price quoted
verbatim with its on-page footnote markers; molecule/form is page-attested (never inferred from the brand —
see the molecule note under Verbatim anchors). An offering here is never asserted equal to a same-molecule
offering at another brand.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Weight Loss | family | — | `/weight-loss` | — | — | GLP-1 weight-loss line; a "holistic program" (meds + nutrition + app) gating a SKU roster behind a membership. |
| Weight Loss Membership | buyable | Weight Loss | (recurring fee — no standalone PDP captured) | `$39 for the first month, auto-renews at $149/month thereafter` | published | — · subscription · the recurring fee that gates every WL SKU; billed separately from medication. |
| Wegovy® Pill | buyable | Weight Loss | `/weight-loss/wegovy-pill` | `From $149/mo†` / `Starts at $149/mo` | partial | semaglutide · oral, once-daily · membership-gated; price is med-only + mandatory membership. |
| Wegovy® Pen | buyable | Weight Loss | `/weight-loss/wegovy-pen` | `From $199/mo†` / `Starts at $199/mo` | partial | semaglutide · injection, once-weekly (doses 0.25–7.2mg) · membership-gated; med-only price. |
| Zepbound® Vial | buyable | Weight Loss | `/weight-loss/zepbound-vial` | `From $299/mo†` / `Starts at $299/mo` | partial | tirzepatide · injection, once-weekly (vial) · membership-gated; med-only price. |
| Zepbound® KwikPen® | buyable | Weight Loss | `/weight-loss/zepbound-kwikpen` | `From $299/mo†` / `Starts at $299/mo` | partial | tirzepatide · injection, once-weekly (pre-filled pen) · membership-gated; price from category card + Vial comparison (own PDP not captured). |
| Foundayo™ Pill | buyable | Weight Loss | `/weight-loss/foundayo-pill` | `From $149/mo†` | partial | orforglipron · oral, once-daily · membership-gated; "no rules around food, water, timing." |
| Ozempic® Pill | buyable | Weight Loss | `/weight-loss/ozempic-pill` | `From $149/mo†` | partial | semaglutide · oral · membership-gated; FDA-approved for T2D, off-label for weight loss (own PDP not captured). |
| Ozempic® (injection) | buyable | Weight Loss | (no PDP — category card/modal) | `From $199/mo†` | partial | semaglutide · injection, weekly · membership-gated; off-label for weight loss. [anchor a] |
| Mounjaro® | buyable | Weight Loss | (no PDP — category modal) | `$1,899/mo†` / `$1,899/mo*` | partial | not stated · injection, weekly · membership-gated; "a weekly GLP-1 injection," FDA-approved T2D, off-label weight loss. |
| Zepbound® (brand entry) | buyable | Weight Loss | (no PDP — category card/modal) | `$1,899/mo†` / `$1,899/mo*` | partial | tirzepatide · injection, weekly · membership-gated; full-price brand card, distinct from the $299 Vial/KwikPen SKUs. [anchor b] |
| Testosterone | family | — | `/testosterone` | — | — | "Testosterone Rx / Rx+" line; enclomiphene-based, at-home-labs-gated — not synthetic TRT. |
| Testosterone Rx+ (enclomiphene + supplements) | buyable | Testosterone | `/testosterone/enclomiphene-supplements` | none on page; FAQ `starts at $99/month for a 10-month plan paid upfront and in full` | on-request | enclomiphene + supplements (L-arginine, B6, B12, zinc) · oral, daily · lab + intake gated. |
| Testosterone Rx+ (enclomiphene + tadalafil + supplements) | buyable | Testosterone | `/testosterone/enclomiphene-tadalafil-supplements` | none on page; FAQ `starts at $99/month for a 10-month plan paid upfront and in full` | on-request | enclomiphene + tadalafil + supplements · oral, daily · lab + intake gated; identical H1 "Testosterone Rx+." |
| Enclomiphene | buyable | Testosterone | `/testosterone/enclomiphene` | — (PDP not captured) | on-request | enclomiphene · oral · lab + intake gated; linked from category "Featured." |
| Enclomiphene & Tadalafil | buyable | Testosterone | `/testosterone/enclomiphene-tadalafil` | — (PDP not captured) | on-request | enclomiphene + tadalafil · oral · lab + intake gated; linked from category "Featured." |
| Testosterone cypionate (injection) | buyable (roadmap) | Testosterone | (no PDP — category card) | `Coming in 2026*` | on-request | testosterone cypionate · injection, weekly · not yet offered — "Hims does not currently offer access to TRT injections." |
| Kyzatrex® | buyable (roadmap) | Testosterone | (no PDP — category card) | `Coming in 2026*` | on-request | testosterone undecanoate · oral, twice-daily · FDA-approved; not yet offered. |

### Verbatim anchors

The footnotes the roster's Price column points at — they are what decide `[partial]` vs `[on-request]`,
and the molecule-sourcing audit trail. Quoted exactly from the captured pages.

- **† (weight-loss membership):** *"Price includes medication only, if prescribed. An active Hims Weight
  Loss Membership is required ($39 for the first month, auto-renews at $149/month thereafter). Membership is
  billed separately and does not include or guarantee a prescription. Medication is not available without a
  membership. Membership fee is not included."* (weight-loss category + every WL PDP) → the WL number is
  real but med-only; all-in = membership + medication, hence `[partial]`.
- **\* (Mounjaro / generic Zepbound, $1,899):** *"$1,899 price includes medication only, if prescribed. An
  active Hims Weight Loss Membership is required ($39 for the first month, auto-renews at $149/month
  thereafter)..."* (weight-loss category "Our brands" modals).
- **\* (testosterone "Coming in 2026"):** *"Such expected launch is subject to certain assumptions and
  factors, some of which may be outside of our control, and as such may be subject to change."*
- **Molecule sourcing (the page-attested-only rule, audited):** Zepbound forms (Vial, KwikPen, brand entry)
  → **tirzepatide**, attested on the Vial PDP: *"Zepbound® is available in a vial or pre-filled KwikPen®.
  Both contain tirzepatide."* Ozempic (pill + injection) → **semaglutide**, attested: *"Contains
  semaglutide, a clinically-proven ingredient that's also in Ozempic®."* **Mounjaro → "not stated"** — no
  captured page names its molecule (the card reads only "a weekly GLP-1 injection"); recorded "not stated"
  rather than inferred from the brand.
- **[anchor a] Ozempic split:** the weight-loss category grid shows two Ozempic entries — an oral pill at
  "From $149/mo†" linking to `/weight-loss/ozempic-pill`, and a "Weekly injectable" at "From $199/mo†" (the
  footer "Ozempic®" modal). Read as: oral pill = $149, weekly injectable = $199. Both verbatim; not reconciled.
- **[anchor b] Zepbound naming:** the brand carries three price points on the captured pages — Vial **and**
  KwikPen at "From $299/mo†" (the buyable Hims WL SKUs, with PDPs/comparison rows), and a separate generic
  "Zepbound®" brand card/modal at "$1,899/mo†/\*" (the full-price brand entry). Kept as distinct rows; no
  claim about which dose maps to which price.

## Deep blocks

One block earns its place — the only one the roster row can't carry (the rest of the lineup answers from the
table). The two weight-loss molecules and their per-SKU prices live in the roster; reproducing them as deep
blocks would only restate roster cells.

### Testosterone Rx+ — enclomiphene, *not* synthetic TRT

- **Parent:** Testosterone · **slug:** `/testosterone/enclomiphene-supplements` · **price:** none on the
  product page; FAQ-only "$99/month for a 10-month plan paid upfront and in full" · **visibility:** `[on-request]`

> **H1:** "Testosterone Rx+"  (eyebrow: "Now with supplements")
> **Not-TRT (verbatim):** "Enclomiphene is the essential ingredient in Testosterone Rx, which works with
> your body's natural T production—**no synthetic testosterone needed**."
> **The only price on the line (FAQ, verbatim):** "Pricing for low testosterone treatment with enclomiphene
> through Hims **starts at $99/month for a 10-month plan paid upfront and in full**."
> **Gating (verbatim):** "Lab testing is required to determine eligibility. After checkout, you'll be sent
> an initial lab kit…" — every CTA is "Get started," routing to the intake.
> **Compliance (verbatim):** "Compounded drug products are not approved or evaluated for safety,
> effectiveness, or quality by the FDA. Rx required."

**Why this block earns its place** (and the others don't): (1) the $99/mo figure is the *only* price on the
entire testosterone line and it is buried in FAQ prose — a roster cell flags `[on-request]` but can't carry
where the number hides; this is the figure that flips a cheapest-enclomiphene comparison. (2) "No synthetic
testosterone" + compounded enclomiphene is the disambiguation that stops a reader mis-grouping this line as
TRT — it isn't. Hims's only real injectable TRT (testosterone cypionate) is "Coming in 2026," not buyable
today. The sibling SKU `/testosterone/enclomiphene-tadalafil-supplements` carries the **identical H1
"Testosterone Rx+"** and the same $99/mo FAQ figure; its only differentiator is added tadalafil "to boost
sexual performance" — kept as its own roster row, keyed by its own slug.

## Provenance

- **Pages read (8, all `captures/2026-06-03/`):** `weight-loss-category.md` (/weight-loss),
  `weight-loss-wegovy-pill.md`, `weight-loss-wegovy-pen.md`, `weight-loss-zepbound-vial.md`,
  `weight-loss-foundayo-pill.md`, `testosterone-category.md` (/testosterone), `testosterone-enclomiphene.md`
  (/testosterone/enclomiphene-supplements), `testosterone-enclomiphene-tadalafil.md`
  (/testosterone/enclomiphene-tadalafil-supplements). Context: `store/hims-com/profile.md`. These reuse the
  2026-06-03 offerings-tournament capture (15 credits for the 4-company cohort) — zero new Firecrawl spend.
- **Scope:** weight-loss (GLP-1) + testosterone only — the two lines with a live per-SKU consumer. Hims's
  other four lines (sexual health, hair loss, mental health, labs) are noted in the overview but **not
  enumerated** — no per-SKU capture this run.
- **Gated / unreachable:** all-in weight-loss cost (medication + membership + dose-titration variance —
  "Pricing may vary by dosage"); all testosterone pricing beyond the $99/mo FAQ teaser (intake + required
  lab); own PDPs for Zepbound KwikPen, Ozempic (pill + injection), Mounjaro, the generic Zepbound brand
  card, and both bare enclomiphene variants (priced/described only via category cards/modals).
- **Point-in-time snapshot, not fixed:** Hims runs promo + A/B pricing ("for a limited time" recurs on the
  WL heroes) — this module's own `captured_at` + a short freshness TTL are the guard; re-capture before
  trusting a price as current.
</content>
</invoke>
