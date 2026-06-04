---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: henrymeds.com
captured_at: 2026-06-04
site_notes: "Catalog = nav + map (Framer site, no CMS/bundle registry). Each treatment PDP slug under /treatments/<category>/<sku>. Prices live in a bottom-of-page FAQ ('How much does X cost'), not a pricing page; all prices are all-in (visit + meds + supplies + shipping). GLP-1 molecule SKUs all share the '$179/month' family floor — exact per-dose price is intake-gated. The /semaglutide (injectable) PDP carries NO price in markdown; floor is page-attested on the GLP-1 hub + sibling PDPs."
---

## Portfolio overview

`Multi-product` telehealth brand, four condition lines. Weight management is the anchor and the broadest line — a GLP-1 hub fanning into six molecule/form SKUs (semaglutide & tirzepatide, each injectable + oral, plus a lower-dose "microdose" pair and liraglutide) **[MED** — first nav item, first homepage hero card, title leads with "Weight Loss"]**, plus standalone phentermine. The other three lines are single-PDP: Women's HRT, TRT, and ED (oral + injectable). All SKUs are flat-monthly, cash-pay, and bundle the visit + medication + supplies + shipping into one price — there is **no separate membership fee**, so a shown floor is closer to the true all-in than at membership-stacked peers. The split that matters: **flat-priced lines** (phentermine, HRT, ED-oral) publish a self-contained number; **dose-laddered lines** (GLP-1, TRT, ED-injectable) publish a "starting at" floor that moves with dose/plan set in the gated intake → `partial`.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| GLP-1 Weight Management | family | — | /treatments/weight-management/glp-1-weight-management | — | — | compounded GLP-1 hub · injectable + oral · Rx, intake-gated |
| Semaglutide (injectable) | buyable | glp-1-weight-management | /treatments/weight-management/semaglutide | "starts at $179/month" (floor; PDP markdown carries no price — hub/sibling-attested) | partial | semaglutide · subcutaneous injection · Rx |
| Semaglutide Oral | buyable | glp-1-weight-management | /treatments/weight-management/semaglutide-oral | "starts at $179/month" | partial | semaglutide · oral (sublingual tablet) · Rx |
| Tirzepatide Tablets | buyable | glp-1-weight-management | /treatments/weight-management/tirzepatide-tablets | "starts at $179/month" | partial | tirzepatide · oral tablet · Rx |
| Microdose (injectable) | buyable | glp-1-weight-management | /treatments/weight-management/microdose | "starts at $179/month" | partial | semaglutide (microdose) · injection · Rx |
| Microdose Oral | buyable | glp-1-weight-management | /treatments/weight-management/microdose-oral | "starts at $179/month" | partial | semaglutide (microdose) · oral · Rx |
| Liraglutide | buyable | glp-1-weight-management | /treatments/weight-management/liraglutide | "starts at $179/month" | partial | liraglutide · injection · Rx |
| Phentermine | buyable | — | /treatments/weight-management/phentermine | "The total monthly price for Phentermine is $149" | published | phentermine (compounded) · oral · Rx |
| Women's HRT | buyable | — | /treatments/hrt | "$149/month" | published | estrogen · progesterone · testosterone (compounded + FDA-approved) · body cream / vaginal cream / patch / tablet · Rx |
| Testosterone Therapy (TRT) | buyable | — | /treatments/trt | "Starting at $129 per Month ($179 for KYZATREX™ oral TRT … not available in California)" | partial | testosterone (compounded) + KYZATREX™ (FDA-brand oral) · injection / oral capsule · Rx; labs + aromatase inhibitor incl. |
| ED — Oral | buyable | — | /treatments/erectile-dysfunction/ed-oral | "three month supply for $50 each month ($150 total)" | published | not stated · oral ODT (flavored) · Rx |
| ED — Injectable (ICP) | buyable | — | /treatments/erectile-dysfunction/icp | "Starting as low as $149/mo" | partial | Trimix · Bimix · alprostadil · papaverine · phentolamine (± tadalafil/sildenafil) · intracavernosal injection · Rx |

## Verbatim anchors

The footnotes that decide `partial` vs `published`, quoted exactly:

- **GLP-1 floor (all six SKUs):** "The price of GLP-1 medication varies by treatment plan and dosing, but starts at $179/month. This includes the cost of your provider visits, medication, supplies, and ongoing support." — /treatments/weight-management/glp-1-weight-management (and each sibling GLP-1 PDP). → floor moves with dose ⇒ `partial`.
- **Phentermine:** "The total monthly price for Phentermine is $149. That price includes everything—your healthcare provider visits, medication and supplies, shipping, and ongoing support." — /treatments/weight-management/phentermine. → flat ⇒ `published`.
- **HRT:** "personalized treatment for $149/month … Start HRT treatment for a flat monthly fee of $149, no insurance required." — /treatments/hrt. → flat ⇒ `published`.
- **TRT:** "Starting at $129 per Month ($179 for KYZATREX™ oral TRT oral capsule.- not available in California.) … compouded treatments start at $129 per month … Labs are included as well." — /treatments/trt. → floor + variant ⇒ `partial`.
- **ED oral:** "Oral pills start with a three month supply for $50 each month ($150 total)." — /treatments/erectile-dysfunction/ed-oral. → specific stated price ⇒ `published`.
- **ED injectable (ICP):** "Starting as low as $149/mo" (hero) / "Injections cost $149/month" — /treatments/erectile-dysfunction/icp. → "starting as low as" floor across Trimix/Bimix options ⇒ `partial`.
- **Molecule audit (`not stated`):** ED — Oral names only "oral ED medication" / "Oral pills" / ODT (flavored) in product copy; no molecule (sildenafil/tadalafil) is named on /ed-oral, so `not stated` rather than inferred. (The /icp page does name Tadalafil & Sildenafil among its injectable mixes.)

## Deep blocks

None earned — the roster carries this company. Every line resolves to a slug-keyed row with a page-attested price floor; the only ambiguity (the /semaglutide PDP's missing price) is captured inline via the family-floor attestation, and the GLP-1 SKUs are pure molecule/form variants of one priced family.

## Provenance

- **Pages read:** the 12 treatment PDPs under `captures/2026-06-04/` (GLP-1 hub, semaglutide, semaglutide-oral, tirzepatide-tablets, microdose, microdose-oral, liraglutide, phentermine, trt, hrt, ed-oral, icp) + homepage for nav/cards.
- **Scope:** all 4 condition lines and all 12 indexed treatment pages enumerated (complete at the indexed level). GLP-1 dose ladders and HRT med-by-form options are noted, not exploded into per-dose rows (intake-gated).
- **Gated/unreachable:** exact per-dose & per-plan prices set in the onboarding flow (not submitted); /semaglutide PDP price (family floor applied).
- **Point-in-time:** prices are a snapshot — site reserves the right to "update pricing, product availability, and service terms at any time"; re-check before quoting.
- **Run profile:** guided — `offerings.md` enabled alongside `profile.md` + `telehealth.md`; plain roster (no hero-image capture, no PDP-anatomy block).
