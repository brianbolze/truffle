---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: remedymeds.com       # company key; each offering's slug (its relative url) is its key *within* Remedy
captured_at: 2026-06-03      # own freshness; captures/2026-06-03/ holds the source pages
---

## Portfolio overview

Remedy Meds is **Single** — one vertical, **medical weight loss via compounded GLP-1**, sold as four plan
variants of a single month-to-month membership. No TRT/testosterone or any non-weight-loss line appears on
any captured page; every CTA on the site routes to `/quiz`. Pricing is marketed all-in (medication +
unlimited clinician care + free labs + shipping + community), and the homepage strip reads "No Memberships
or Hidden Fees" — even though the patient manual calls the recurring charge a "membership" billed
automatically every 28 days (the tension is itself a finding; see the anchors).

**The shape finding — two patterns, two visibility tokens:** the catalog the site *shows* is two-priced;
the catalog it *sells* is four, two of them price-opaque.
- **The two compounded injectables are `[published]`.** Semaglutide and Tirzepatide each get a dedicated
  `/medication/*` product page with a hero monthly price (Semaglutide **$299/month**, Tirzepatide
  **$399/month**). These are the only greppable prices on the entire site.
- **Microdose and Branded are `[on-request]`.** Both appear *only* as homepage plan-cards with **no price
  string at all**; the price is reachable only by completing the quiz. The gating is the finding — a
  number shows for two of four variants, not the line as a whole.

**Prominence (calibrated).** Semaglutide is framed as the entry/lead variant **[MED]** — its own card label
is "Best First Step" / "New to GLP-1s? → Start here," and it is the first plan-card in homepage order.
Tirzepatide carries the only self-reported share claim, "**64% of members use this**" **[MED]** (the
company's own card text, single signal — emphasis, not a corroborated hero). Microdose is labelled
"Easiest Entry" and badged "New!", Branded "Retail Pricing" — both read as lighter, edge variants **[LOW]**
(homepage-card-only, no page, no price). Card order within the plan carousel left **[LOW]** — not used for
ranking beyond the "Start here" label.

## Roster

Complete at the indexed level — every GLP-1 offering surfaced on the captured pages. Within-company key =
**Slug**; only the two injectables have real `/medication/*` slugs in the capture. Price quoted verbatim
with its on-page strings; molecule/form is page-attested (never inferred from the brand — see the molecule
note under Verbatim anchors). No cross-brand equivalence is asserted as stored fact.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Medical weight loss (GLP-1) | family | — | `/` | — | — | The single vertical: a compounded-GLP-1 weight-loss membership, all-in (med + unlimited care + free labs + shipping); "charged automatically every 28 days," marketed "No Memberships or Hidden Fees." |
| Semaglutide | buyable | Medical weight loss (GLP-1) | `/medication/comp-sema-inj` | `$299/month` (own-page hero); `Starting at$299/mo.` / `Less than $9/day.` (comparison card) | published | semaglutide · injection, once-weekly · quiz-gated intake; "Compounded GLP-1," "Best First Step" for GLP-1-naïve members. |
| Tirzepatide | buyable | Medical weight loss (GLP-1) | `/medication/comp-tirz-inj` | `$399/month` (own-page hero); `Starting at$399/mo.` / `Less than $13/day.` (comparison card) | published | tirzepatide · injection · quiz-gated intake; "Compounded GLP-1," "Dual GIP + GLP-1 agonist," "strongest compounded option," "64% of members use this." |
| Microdose Plan | buyable | Medical weight loss (GLP-1) | (no PDP — homepage card → `/quiz`) | — (no price shown; quiz-gated) | on-request | not stated (labelled "GLP-1 receptor agonist · micro-titration") · injectable, "half the dose, twice a week" · quiz-gated; "Easiest Entry," badged "New!" — specific molecule not named on any captured page. |
| Branded (Ozempic® / Zepbound®) | buyable | Medical weight loss (GLP-1) | (no PDP — homepage card → `/quiz`) | — (no price shown; labelled "Retail Pricing") | on-request | not stated · name-brand form · quiz-gated; one "name brand" card lists Ozempic® and Zepbound® under one "Start name brand" CTA — neither molecule is stated on any captured Remedy page. |

### Verbatim anchors

The price strings + the gating language the roster points at — what decides `[published]` vs `[on-request]`,
plus the molecule-sourcing audit. Quoted exactly from the captured pages.

- **Semaglutide price (own page, `med-semaglutide_comp-sema-inj.md`):** the hero block reads
  *"Monthly1 Month"* → *"$299/month"* (lines 19–21). The *"Starting at$299/mo."* / *"Less than $9/day."*
  comparison-card strings for Semaglutide sit on the **Tirzepatide** page (`med-tirzepatide_comp-tirz-inj.md`
  lines 244–246), in its "explore additional GLP-1s" cross-sell — not on the sema page's own hero.
- **Tirzepatide price (own page, `med-tirzepatide_comp-tirz-inj.md`):** the hero block reads
  *"Monthly1 Month"* → *"$399/month"* (lines 19–21). The *"Starting at$399/mo."* / *"Less than $13/day."*
  comparison-card strings for Tirzepatide sit on the **Semaglutide** page
  (`med-semaglutide_comp-sema-inj.md` lines 246–248). (Seed correction: these card strings do **not** appear
  on the homepage — the homepage carries no `$` amount at all — and each appears on the *sibling's* page,
  not its own.)
- **Microdose / Branded — no price anywhere:** a full grep of `captures/2026-06-03/` returns only
  `$299`, `$399`, `$9/day`, `$13/day` — all tied to the two injectables. The Microdose card
  (`homepage.md` lines 164–199) and the Branded card (lines 200–208 / 326–334) carry **no `$` string**;
  both route to `/quiz`. Hence `[on-request]`.
- **Membership / "No Memberships" tension:** homepage marquee says *"No Memberships or Hidden Fees"*
  (`homepage.md` lines 463, 479); the patient manual says *"Your membership is charged automatically every
  28 days"* and *"once a prescription has been written, we are unable to issue a refund"*
  (`patient-manual_getting-started.md` lines 100, 104). The recurring charge is the all-in unit; "no hidden
  fees" means it bundles med + care + labs + shipping, not that there is no recurring membership.
- **Molecule sourcing (the page-attested-only rule, audited):**
  - **Semaglutide → semaglutide** and **Tirzepatide → tirzepatide** are attested directly, not inferred
    from a brand: each is the product H1 itself (*"# Semaglutide"* / *"# Tirzepatide"*, subhead
    *"Compounded GLP-1"*), reinforced by *"Compounded Semaglutide & Tirzepatide"* (`homepage.md` line 13)
    and *"for both compounded Semaglutide and compounded Tirzepatide"* (`patient-manual_getting-started.md`
    line 280). These are sold by molecule name, so the name *is* the page attestation.
  - **Semaglutide form = once-weekly injection** — attested: *"A once-weekly injection that quiets food
    noise…"* (`homepage.md` line 113). Tirzepatide's own page does not state "once-weekly" for tirz (its
    "once-weekly" line is the sema cross-sell card), so the Tirzepatide row records form as **injection**
    without a cadence — not inferred.
  - **Microdose → "not stated."** The card labels it *"GLP-1 receptor agonist · micro-titration"* and
    *"Same medication — half the dose, twice a week"* (`homepage.md` lines 172, 176) — but "same
    medication" never names *which* (sema, tirz, or either), so the specific molecule is recorded
    "not stated," not back-filled from the two injectables.
  - **Branded → "not stated."** The card shows only *"Ozempic®"* and *"Zepbound®"* (`homepage.md` lines
    204–206); no captured Remedy page states Ozempic's or Zepbound's molecule. Recorded "not stated" rather
    than inferred from the brand (the Mounjaro-trap the module exists to prevent — Ozempic is semaglutide
    and Zepbound is tirzepatide in the world, but **Remedy's pages don't say so**, so the file doesn't).

## Deep blocks

None earned — the roster carries this company. The two `[published]` SKUs put their full price in the
roster (hero + comparison-card strings, with the cross-page provenance pinned in the anchors); the two
`[on-request]` SKUs have no price to surface and no H1/footnote that disambiguates anything a roster row
plus the molecule note can't already carry. There is no gated-FAQ price figure and no "this isn't actually
TRT"–style disambiguation to resolve here.

## Provenance

- **Pages read (5, all `captures/2026-06-03/`):** `homepage.md` (`/` — the plan-card roster + the four
  variants + the all-in/membership language), `med-semaglutide_comp-sema-inj.md`
  (`/medication/comp-sema-inj` — Semaglutide hero $299 + the Tirzepatide cross-sell card),
  `med-tirzepatide_comp-tirz-inj.md` (`/medication/comp-tirz-inj` — Tirzepatide hero $399 + the Semaglutide
  cross-sell card), `patient-manual_getting-started.md` (`/getting-started` PDF — billing/labs/refund),
  `quiz-shell.md` (`/quiz` — app shell, no static pricing). Context: `store/remedymeds-com/profile.md`.
  These reuse the 2026-06-03 capture — zero new Firecrawl spend.
- **Scope:** the full enumerable catalog — one vertical, four plan variants. There is no second line to
  omit; the roster is complete at the indexed level for everything the captured pages surface.
- **Gated / unreachable:** Microdose and Branded (Ozempic®/Zepbound®) pricing — quiz-gated, no published
  price; their specific molecules — not stated on any captured page; the all-in cost beyond the two hero
  monthlies (dose-titration variance, the membership's bundled vs. à-la-carte breakdown — the manual states
  the bundle but no line-item prices). No dedicated PDP exists for Microdose or Branded (homepage cards →
  `/quiz` only).
- **Point-in-time snapshot, not fixed:** Remedy runs a single A/B-tested funnel (the homepage is a
  `lander/variant_3` build; "New!" / "64% of members" are live marketing claims, point-in-time). This
  module's own `captured_at` + a short freshness TTL are the guard; re-capture before trusting a price as
  current.
