---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: malemd.com
captured_at: 2026-06-04
enumeration: indexed-complete
site_notes: "Catalog = the 10 lines in /site-map + the homepage 'Explore' nav (BPC-157 at /repair is a homepage link, not in either). Each line is a single buyable on a campaign-coded funnel path (/sermorelin/v2/hc, /nad/v3, /25again/ckh, /hairsy/v2n/cj/h); the path codes (v2/v3/ckh/promo7g) are A/B variants. Per-line FLOOR price is on the landing page; full dose/quantity + multi-month plan tiers sit behind the questionnaire at /<product>/medication. A/B: Convert + Google Optimize — promo prices flicker (e.g. NAD+ '$299 $199'); re-check next run. Molecules are stated in product copy; forms often are not (write 'not stated')."
---

## Portfolio overview

MaleMD sells **11 prescription lines across 5 categories**, each a single buyable (no umbrella/bundle SKUs) on a cash-pay subscription. The shape: **sexual health is the widest line** (4 distinct ED/PE SKUs), **longevity/peptides is the promoted line** (Sermorelin is the site's "Hot New Product"; NAD+, Metformin, BPC-157 round it out), and **sleep / hair / pain** are single-SKU adjacencies.

Two structural findings:
- **Compounded vs. generic split.** Generic ED, hair (finasteride/minoxidil), metformin, sertraline, and the sleep generics are FDA-approved molecules; **KnockoutRx, HammerRx, and the peptides (sermorelin/NAD+/BPC-157) are compounded** — "the featured products include compounded products which have not been approved by the FDA" (/knockout). No TRT/testosterone and no GLP-1 anywhere.
- **Floor-price pattern.** Landing pages publish a teaser unit/monthly floor; the **real monthly all-in is set in the quiz** (dose/quantity/plan). Lines that show a self-contained monthly price are `published`; lines showing only a per-unit floor are `partial`; the one line with no price (BPC-157) is `on-request`.

**Prominence read:** Sermorelin is foregrounded `[MED]` — the sticky "Hot New Product Alert" bar + first slot in the "Top Treatments" carousel; KnockoutRx leads the homepage product grid `[MED]`. The hero headline A/B-rotates between "Better Sex" and "Better Energy" `[LOW]` — so category emphasis is unstable run-to-run.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| KnockoutRx | buyable | — | /knockout | "Start Today for $1.64/pill" | partial | tadalafil · vardenafil ("3-in-1"; 3rd ingredient not named) · daily tablet/troche, compounded · Rx subscription — "Not all ingredients in KnockoutRx are FDA-approved" |
| HammerRx 2-in-1 Mint | buyable | — | /HammerRx | "Sildenafil & Tadalafil Dissolving Mint $6/dose" | partial | sildenafil · tadalafil · dissolving mint, compounded · Rx subscription, as-needed |
| Generic ED | buyable | — | /25again/ckh | "As Low as $1.65/pill" | partial | sildenafil · tadalafil (generic, FDA-approved) · pill · Rx subscription |
| PE Treatment | buyable | — | /pe | "$0.87/ dose if prescribed" | partial | sertraline · oral · Rx subscription (off-label for premature ejaculation) |
| Sermorelin | buyable | — | /sermorelin/v2/hc | "Sermorelin Growth Hormone Peptide $149/mo" | published | sermorelin · GH peptide, form not stated (compounded) · monthly Rx subscription |
| NAD+ | buyable | — | /nad/v3 | "Starting at $199" (shown "$299 $199"; "$100 Off Treatment Plans") | published | NAD+ · form not stated (compounded) · monthly Rx subscription |
| Metformin | buyable | — | /metformin | "$5 for First Month … $25 per Month After" (billed $55 first shipment, shipped quarterly) | published | metformin · oral · Rx subscription (longevity/metabolic) |
| Sleep Treatments | buyable | — | /slp/lp | "Treatment starting at $1.50 per day"; tiers "As Low as $47.20" / "$66.75" | published | hydroxyzine / ramelteon / trazodone / melatonin · oral · nightly Rx subscription |
| Hair Regrowth | buyable | — | /hairsy/v2n/cj/h | "Start for $1.56 / Day" / "Starting at $47/ Month" | published | finasteride + minoxidil · form not specified · daily Rx subscription |
| Pain Management | buyable | — | /pain | "$89/ month" (tiers "$149/ month", "$199/ month") | published | diclofenac · fast-absorbing topical gel · Rx subscription, as-needed |
| BPC-157 | buyable | — | /repair | — (no price shown) | on-request | BPC-157 · peptide, form not stated (compounded) · quiz-gated Rx subscription (healing / gut health) |

## Verbatim anchors

- **KnockoutRx (compounded, partial):** "Tadalafil (Prescription ED Medication)" + "Vardenafil (Prescription ED Medication)"; "I love that taking the 3-in-1 medication daily"; disclaimer: "The featured products include compounded products which have not been approved by the FDA… Not all ingredients in KnockoutRx are FDA-approved for treatment of erectile dysfunction (ED) or low libido in men." (/knockout). The named molecules are tadalafil + vardenafil; the "3-in-1" implies a third ingredient the captured page does not name → recorded as not named, not inferred.
- **HammerRx:** "Sildenafil & Tadalafil Dissolving Mint $6/dose"; "As low as $6 per dose"; "Start for $6/dose". (/HammerRx)
- **Generic ED:** "As Low as $1.65/pill"; molecules "Sildenafil"/"Tadalafil"; ISI confirms "Sildenafil (sildenafil citrate) and Tadalafil are prescription medications used to treat erectile dysfunction." (/25again/ckh, /safety-profile)
- **PE Treatment:** "$0.87/ dose if prescribed"; active molecule "Sertraline" throughout. (/pe)
- **Sermorelin:** "Sermorelin Growth Hormone Peptide $149/mo"; "$149/ Month". (/sermorelin/v2/hc)
- **NAD+:** "$100 Off Treatment Plans"; "Starting at $199"; "$299 $199". (/nad/v3) — promo, A/B-volatile.
- **Metformin:** "$5 for First Month"; "billed $55 first shipment | shipped quarterly"; "$25 per Month After". (/metformin)
- **Sleep:** "Treatment starting at $1.50 per day"; "As Low as $47.20"; "$66.75"; molecules Hydroxyzine / Ramelteon / Trazodone / melatonin. (/slp/lp)
- **Hair:** "Start for $1.56 / Day"; "Prescription Hair Regrowth Starting at $47/ Month"; molecules Finasteride + Minoxidil. (/hairsy/v2n/cj/h)
- **Pain:** "$89/ month", "$149/ month", "$199/ month"; molecule diclofenac. (/pain)
- **Molecule sourcing audit (`not stated` forms):** sermorelin, NAD+, and BPC-157 landing pages name the molecule but do **not** state dosage form (injection vs. oral) in product copy — recorded "form not stated." (Customer reviews mention "sermorelin orals" / "BPC-157 orals," but reviews are not product copy, so not attributed.)

## Deep blocks

- **KnockoutRx — what "3-in-1" actually is.** Earned: the roster row can't carry the FDA-status nuance. KnockoutRx is a **compounded daily ED troche** built on PDE5 inhibitors **tadalafil + vardenafil** (the page names two of the advertised "3-in-1"; the third is unnamed). The page leans on tadalafil's daily-dosing evidence base (4 cited PubMed studies) but discloses "Not all ingredients in KnockoutRx are FDA-approved" — i.e., the *combination/compound* is not an FDA product even though tadalafil individually is. This is the line where MaleMD's compounding posture is most explicit. (/knockout)
- **PDP-template anatomy:** none — not requested this run.
- **Hero product images:** none — not requested this run (`+offerings` was the roster preset, not the flagship-images variant).

## Provenance

- **Pages read:** 11 product landers (knockout, HammerRx, 25again/ckh, pe, sermorelin/v2/hc, nad/v3, metformin, slp/lp, hairsy, pain, repair) + homepage + /site-map + /safety-profile (molecule/ISI corroboration), all under `captures/2026-06-04/`.
- **Scope note:** **indexed-complete** — all 11 lines rostered at SKU grain (10 from /site-map + nav, plus BPC-157 from the homepage grid). Sub-indexed leaf detail deliberately not enumerated: per-line dose/quantity options and multi-month plan tiers, which live behind the questionnaire at `/<product>/medication`. No whole line omitted.
- **Gated/unreachable:** BPC-157 price (quiz-gated, `on-request`); full plan/dose tiers for every line (intake-gated).
- **Point-in-time caveat:** pricing runs promos and the site A/B-tests (Convert + Google Optimize) — NAD+ "$299 $199" and the per-line floors are a snapshot, not fixed.
- **Run profile:** Express `+offerings` roster preset — no PDP-anatomy block, no hero images, no added columns. Vanilla roster otherwise.
