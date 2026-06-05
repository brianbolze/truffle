---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: gethealthspan.com
captured_at: 2026-06-04
site_notes: "Next.js + Strapi; catalog is clean off four index pages — /medications (Rx + all-in protocols), /supplements (OTC), /labs (one-time panels), /programs (memberships). Prices sit on the index CARDS as 'Starting at $X/mo' (no PDP scrape needed to roster), but the index floor ≠ all-in for HRT/GLP-1: those carry a separate Membership ('$129/mo or $99/mo for 3 months') + medication 'billed separately' (GLP-1 via LillyDirect), so the card '$X/mo' is the member-discounted MED price → partial. Longevity protocols (rapamycin/oxytocin/methylene blue/SGLT2/acarbose/metformin/LDN) are self-contained ('Everything included: labs, meds, dosing; cancel anytime') → published. A/B: VWO — per-SKU prices flicker run-to-run (Topical Rapamycin Hair $120 index / $140 PDP this run). Many /treatments/* slugs are A/B or legacy variants (-old, -fb, -troche-a, -hero, testosterone-replacement-therapy, trt-cream/trt-injection, brenzavvy, canagliflozin, wegovy-pen alt) NOT on the index grid — roster the index-surfaced SKUs. Product renders: '*_Gallery_Card_540x540' on strapiapp = clean isolated bottle on white."
---

## Portfolio overview

A genuinely **Multi-product** longevity clinic: ~35 buyable SKUs across **Rx medications, OTC supplements, one-time lab panels, and four membership programs**. The shape finding is the **two commercial structures**, not the molecule count:

1. **All-inclusive longevity protocols** — one self-contained `$X/mo` ("Everything included: advanced lab testing, medications, and ongoing dosing optimization. Modify or cancel anytime"). These are `published`. (Rapamycin, Topical Rapamycin, SGLT2, Acarbose, Metformin, LDN, Methylene Blue, Oxytocin.)
2. **Membership + medication-separate** — for HRT, GLP-1, and men's TRT, the card `$X/mo` is the member-discounted *medication* price; a Healthspan **Membership ($129/mo, or $99/mo on a 3-month commitment)** sits on top and the med is "billed separately" (GLP-1 fulfilled via **LillyDirect**). These are `partial`.

**Prominence** (the company's own labels + hero, not a market read):
- **Rapamycin — `[HIGH]`.** The flagship and credibility anchor: the hero molecule across the site, the only drug the "Featured In" press quotes name ("the current best-in-class for a longevity drug"), carousel lead, and a footer "Top Treatments" pick. Healthspan claims it "pioneered the rapamycin dosing protocol for longevity."
- **Methylene Blue, Oxytocin — `[HIGH]`.** The other two of the three footer-labeled **"Top Treatments"** (a company-own label).
- **GLP-1 (Zepbound) — `[MED]`.** Prominent in the metabolic line + a dedicated program, but priced highest and membership-gated; not foregrounded like rapamycin.
- **The four Programs — `[MED]`.** Co-equal ("Starting at $99/mo" each), nav-level, but presented as the wrapper around the protocols rather than the hero.

## Roster

Complete at the indexed level (the SKUs surfaced on `/medications`, `/supplements`, `/labs`, `/programs`). A/B / legacy `/treatments/*` variants not on the index grids are noted, not rostered.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Longevity protocols** (all-inclusive Rx) | family | — | /medications | — | — | self-contained $X/mo: labs + med + dosing, cancel anytime |
| The Rapamycin Protocol | buyable | Longevity protocols | /treatments/rapamycin | Starting at $64/mo | published | rapamycin (sirolimus) · oral enteric-coated tablet (compounded option) · all-in protocol |
| Topical Rapamycin for Skin | buyable | Longevity protocols | /treatments/topical-rapamycin | Starting at $115/mo | published | rapamycin · topical · all-in |
| Topical Rapamycin+ for Hair | buyable | Longevity protocols | /treatments/topical-rapamycin-for-hair | Starting at $120/mo † | published | rapamycin + finasteride + minoxidil · topical · all-in |
| SGLT2 Protocol | buyable | Longevity protocols | /treatments/sglt2-metabolic-protocol | Starting at $99/mo | published | SGLT2 inhibitor (specific drug not stated on card) · oral · all-in |
| Acarbose | buyable | Longevity protocols | /treatments/acarbose | Starting at $25/mo | published | acarbose · oral · all-in |
| Metformin | buyable | Longevity protocols | /treatments/metformin | Starting at $27/mo | published | metformin · oral · all-in |
| Methylene Blue | buyable | Longevity protocols | /treatments/methylene-blue-prescription | Starting at $99/mo | published | methylene blue · compounded 5–25 mg capsules · all-in |
| Oxytocin Nasal Spray | buyable | Longevity protocols | /treatments/oxytocin | Starting at $135/mo | published | oxytocin · compounded nasal spray (~99.5% purity) · all-in |
| Oxytocin Troche | buyable | Longevity protocols | /treatments/oxytocin-troche | Starting at $135/mo | published | oxytocin · compounded troche · all-in |
| Low Dose Naltrexone (LDN) | buyable | Longevity protocols | /treatments/ldn | Starting at $40/mo | published | naltrexone (low-dose) · oral · all-in |
| LDN Troche | buyable | Longevity protocols | /treatments/ldn-troche | Starting at $99/mo | published | naltrexone (low-dose) · troche · all-in |
| **GLP-1 / weight** (Membership + med-separate) | family | — | /medications | — | — | Membership + medication billed separately (via LillyDirect) |
| Zepbound® with Ongoing Care | buyable | GLP-1 / weight | /treatments/zepbound | "Starting at $299/mo + membership" | partial | tirzepatide (GLP-1/GIP) · injectable · FDA-brand via LillyDirect ‡ |
| Zepbound® KwikPen® with Ongoing Care | buyable | GLP-1 / weight | /treatments/zepbound-pen | Starting at $299/mo | partial | tirzepatide · injectable pen · FDA-brand via LillyDirect ‡ |
| Wegovy® Pen with Ongoing Care | buyable | GLP-1 / weight | /treatments/wegovy-pen | Starting at $199/mo | partial | semaglutide · once-weekly injectable · FDA-brand; membership + med separate |
| Wegovy® Pill with Ongoing Care | buyable | GLP-1 / weight | /treatments/wegovy-pills | Starting at $149/mo | partial | oral GLP-1 (Wegovy brand; "semaglutide" named for the Pen, not the Pill) · oral tablet · membership + med separate |
| Foundayo™ Pill with Ongoing Care | buyable | GLP-1 / weight | /treatments/foundayo-pills | Starting at $149/mo | partial | oral GLP-1 (specific molecule not stated on card; "~11% at 72 wks") · oral · membership + med separate |
| **Hormone — men (TRT)** (Membership + med) | family | — | /programs/mens-hormone-health | — | — | "Care is delivered through Membership" |
| Testosterone Cypionate | buyable | Hormone — men | /treatments/testosterone-injections | Starting at $85/mo | partial | testosterone cypionate · long-acting injectable · men · membership + med separate · Schedule III |
| Testosterone Gel | buyable | Hormone — men | /treatments/testosterone-gel | Starting at $85/mo | partial | testosterone · topical gel · men · membership + med separate · Schedule III |
| Enclomiphene | buyable | Hormone — men | /treatments/enclomiphene | Starting at $60/mo | partial | enclomiphene · oral (restores endogenous testosterone) · men · membership |
| **Hormone — women (HRT)** (Membership + med) | family | — | /programs/womens-health | — | — | "HRT medications are accessed through Membership" |
| Testosterone Topical Cream | buyable | Hormone — women | /treatments/testosterone-topical-cream | Starting at $64/mo | partial | testosterone (bioidentical, low-dose for women) · topical cream · membership + med separate |
| Bi-Est 50/50 Cream | buyable | Hormone — women | /treatments/bi-est-cream | Starting at $64/mo | partial | estradiol + estriol (bioidentical) · compounded topical cream · membership |
| Estradiol Patch | buyable | Hormone — women | /treatments/estradiol-patch | Starting at $112/mo | partial | estradiol (bioidentical) · transdermal patch · membership |
| Micronized Progesterone | buyable | Hormone — women | /treatments/micronized-progesterone | Starting at $32/mo | partial | progesterone (bioidentical, micronized) · oral · membership |
| **Supplements** (OTC) | family | — | /supplements | — | — | OTC subscription, no Rx / no membership |
| Cellular Renewal Stack | buyable | Supplements | /treatments/cellular-renewal-stack | Starting at $105/mo | published | supplement stack (constituents not stated on card) · oral · OTC |
| Mitophagy | buyable | Supplements | /treatments/mitophagy | Starting at $60/mo | published | supplement blend (not stated) · oral · OTC |
| Autophagy Blend | buyable | Supplements | /treatments/autophagy-blend | Starting at $56/mo | published | supplement blend (not stated) · oral · OTC |
| AMPK Blend | buyable | Supplements | /treatments/ampk-blend | Starting at $56/mo | published | supplement blend (not stated) · oral · OTC |
| Protein Powder | buyable | Supplements | /treatments/protein-powder | Starting at $55/mo | published | protein · powder · OTC |
| Creatine + Electrolytes | buyable | Supplements | /treatments/creatine-electrolytes | Starting at $48/mo | published | creatine + electrolytes · powder · OTC |
| **Labs** (one-time panels) | family | — | /labs | — | — | one-time purchase; at-home requisition, draw at Quest |
| Longevity Pro | buyable | Labs | /labs/longevity-pro | $349 ("One-time purchase $349.00") | published | 100+ biomarker panel · Quest draw, CLIA-certified · one-time |
| Longevity Starter | buyable | Labs | /labs/prime-longevity | $40 | published | starter biomarker panel · Quest · one-time |
| Heart Vitality Panel | buyable | Labs | /labs/advanced-lipid-panel | $120 | published | advanced lipid panel · Quest · one-time |
| Female Hormone | buyable | Labs | /labs/complete-female-hormone-panel | $120 | published | female hormone panel · Quest · one-time |
| Male Hormone | buyable | Labs | /labs/complete-male-hormone-panel | $120 | published | male hormone panel · Quest · one-time |
| Rapamycin Bioavailability Panel | buyable | Labs | /labs/rapamycin-bioavailability-panel | $25 | published | sirolimus blood-level test · Quest · one-time |
| Metabolic Pro Panel | buyable | Labs | /labs/metabolic-pro-panel | — (no price on /labs index) | on-request | metabolic panel · appears as a protocol component (how-it-works), not priced on the index |
| **Programs** (memberships) | family | — | /programs | — | — | the membership wrapper; "Starting at $99/mo", exact tier behind app signup |
| Longevity Optimization | buyable | Programs | /programs/longevity-optimization-core | Starting at $99/mo | partial | membership · labs + personalized protocol + coaching + BioAge+ · async |
| GLP-1 Longevity Care | buyable | Programs | /programs/glp1-care | Starting at $99/mo | partial | membership · GLP-1 prescribing + 70+ biomarkers + coaching · async |
| Men's Hormone Health | buyable | Programs | /programs/mens-hormone-health | Starting at $99/mo | partial | membership · TRT + labs + hormone coaching · async |
| Women's Hormone Health | buyable | Programs | /programs/womens-health | Starting at $99/mo | partial | membership · peri/menopause HRT + labs + coaching · async |

### Verbatim anchors

The footnotes the Price/Visibility columns point at (quoted exactly from captures):

- **† Topical Rapamycin for Hair — price flicker.** `/medications` index card: *"Starting at $120/mo"*; the `/treatments/rapamycin` PDP cross-sell tile: *"Topical Rapamycin Hair $140/mo"* (same run, 2026-06-04). VWO A/B — recorded as a snapshot; index value rostered.
- **‡ Zepbound — the `partial` evidence.** `/treatments/zepbound`: hero price *"$299/mo + membership"*; *"If prescribed, medication is billed separately and fulfilled through LillyDirect."* FAQ: *"Membership starts at $99 per month. GLP-1 medications are billed separately based on the prescription and pharmacy used."* / *"Do I need a membership to access Zepbound? Yes."*
- **HRT membership floor (testosterone cream PDP, representative of the HRT/TRT lane):** *"Testosterone cream costs $80/month, or $64/month with your 20% member discount. Membership ($129/month or $99/month for 3 months) includes clinician oversight and visits, regular lab testing… Medication is billed separately when prescribed."* → the index `$64/mo` is the member-discounted med price; the published all-in is med + membership.
- **Longevity protocol `published` evidence (rapamycin PDP):** *"Everything included: advanced lab testing, medications, and ongoing dosing optimization"* · *"Modify or cancel anytime"* · *"Your labs are included at no additional cost."*
- **Molecule sourcing — `not stated` audit:** SGLT2 Protocol (card: "a well-researched… SGLT2 inhibitor protocol" — class only; map carries `/treatments/canagliflozin` + `/treatments/brenzavvy` slugs but neither is named on the SGLT2 card, so **not stated**); Foundayo™ Pill ("Once-daily oral GLP-1" — brand named, molecule not); Wegovy Pill ("once-daily oral GLP-1 tablet" — brand Wegovy, "semaglutide" attested only on the *Pen* card); all six supplements (no constituents listed on cards).

## Deep blocks

Two earned — they resolve the pricing dichotomy that defines the whole catalog (per OFFERINGS "earned, not default"). Hero product renders (opt-in this run) live at `captures/2026-06-04/images/<sku>.png`.

### The Rapamycin Protocol — the all-inclusive `published` archetype
Spine: the flagship, and the template for every "longevity protocol" SKU. Verbatim gold (`/treatments/rapamycin`): *"A clinically guided approach to rapamycin, with personalized dosing, lab monitoring, and ongoing physician oversight."* The price card carries *"Everything included: advanced lab testing, medications, and ongoing dosing optimization"* + *"Modify or cancel anytime"* — i.e. the `$64/mo` **is** the all-in, no separate membership. Molecule is page-attested both ways: *"FDA-approved, enteric-coated rapamycin"* (with a *"Sirolimus blood panel"* option) **and** an explicit compounded alternative (*"some patients may prefer compounded rapamycin… we provide access to trusted compounding pharmacies with complimentary bioavailability testing"*) — so a single SKU spans `compounded-or-FDA`. Render: `images/rapamycin.png` (amber pharmacy bottle, "SENESCENCE / Rapamycin", on white).

### Zepbound® with Ongoing Care — the `partial` Membership archetype
Spine: the template for the GLP-1 + HRT lanes, where the card price is **not** the all-in. Verbatim gold (`/treatments/zepbound`): hero *"$299/mo + membership"*; *"medication is billed separately and fulfilled through LillyDirect"*; FAQ *"Membership starts at $99 per month. GLP-1 medications are billed separately based on the prescription and pharmacy used."* Molecule attested as **tirzepatide** ("dual-pathway GLP-1/GIP injectable"; the PDP body names *"Tirzepatide has been studied for…"*) and **FDA-brand** (Eli Lilly via LillyDirect) — not compounded. No clean isolated Healthspan render exists for Zepbound (it's an FDA-brand drug; the PDP shows stat graphics + lifestyle, not a bottle) — hero capture intentionally skipped for this SKU.

### Product renders (opt-in asset, this run)
Six clean isolated flagship renders captured to `captures/2026-06-04/images/` — one per major line, each a Healthspan-labelled bottle on white with a category chip: `rapamycin.png` (Senescence) · `methylene-blue-prescription.png` (Energy) · `oxytocin.png` (Energy, nasal spray) · `sglt2-metabolic-protocol.png` (Metabolic) · `testosterone-topical-cream.png` (Hormones, men/women) · `bi-est-cream.png` (Hormones, women). Source: `*_Gallery_Card_540x540` / `*_Hero` assets on `methodical-vitality-*.media.strapiapp.com`.

## Provenance

- **Pages read (cited captures, 2026-06-04):** `/medications`, `/supplements`, `/labs`, `/programs` (index backbones, rich `--homepage` pass — card grid + prices + prominence), homepage carousel, and 5 flagship PDPs (`/treatments/rapamycin`, `/zepbound`, `/testosterone-topical-cream`, `/oxytocin`, `/methylene-blue-prescription`, `--images`). All in `store/gethealthspan-com/captures/2026-06-04/`.
- **Scope:** all SKUs surfaced on the four index grids are rostered (complete at the indexed level). Not enumerated: ~15 A/B/legacy `/treatments/*` variants not on the grids (`-old`, `-fb`, `-troche-a`, `-hero`, `testosterone-replacement-therapy`, `trt-cream`, `trt-injection`, `brenzavvy`, `canagliflozin`, `high-absorption-rapamycin`, `non-branded-semaglutide`, `mitophagy`-dupe slugs); and `/labs/metabolic-pro-panel` (no index price).
- **Gated / unreachable:** exact program/membership tier price and GLP-1 medication cost (behind app.gethealthspan.com signup / LillyDirect) — rostered as the shown floor + `partial`.
- **Point-in-time caveat:** VWO A/B — prices are a snapshot (e.g. Topical Rapamycin Hair $120 index vs $140 PDP this run). Re-check next run.
- **Run profile:** non-vanilla — opt-in **hero product images** captured (6 flagship renders, noted in the Deep blocks); roster authored alongside the `telehealth.md` cohort pack and the `profile.md` refresh.
