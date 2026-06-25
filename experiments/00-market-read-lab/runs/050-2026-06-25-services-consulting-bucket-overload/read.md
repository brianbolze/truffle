# Market Read

## Question

The store's largest `offering_category` bucket is `Services / Consulting`. Is it a meaningful, buyer-useful category or a residual catch-all? Read every Services/Consulting profile's `entity_type`, `offering_category` STRAIN/qualifier prose, and one-line offer shape; tally the distinct sub-shapes hiding inside the bucket; and judge whether the dominant token discriminates anything a downstream reader or cross-store cut can use at this grain — or whether `entity_type` / query-time grouping already carries the load.

## Result

**Lead (gap-probe verdict): `Services / Consulting` read as a *primary token in isolation* is a residual catch-all — it merges at least six non-comparable jobs/buyers — but the store does NOT need a new sub-category, because the discriminating cut is already carried by existing State: the `offering_category` *array pair* (primary + secondary) plus `entity_type`. The failure is a *reading* failure, not a *capture* failure.** This is an L005 vindication (query-time grouping enough) and an L006 cousin (the most-loaded token over-claims category coherence when read alone).

**The split that proves it (C1, C2).** Of the 61 profiles where `Services / Consulting` is the **primary** token:

- **52 (85%) are DTC telehealth care-wrappers** — `[Services / Consulting, Biotech / Pharma Products]`. The Services token here is a corpus convention: a clinician-service shell around an Rx/compounded product, sold to a *consumer* (henrymeds, hims, ro-co, fountaintrt, keeps, numan…).
- **9 (15%) are genuine professional / B2B services** — `Services / Consulting` with NO Biotech secondary. These are not one job; they are at least five:
  - **Creative / brand / strategy agencies (5):** bullish-co, heco-partners, ideo-com, parlance-cc, redantler-com — sell brand/design/strategy *projects* to other companies (C3).
  - **Venture capital / investor partnership (1):** lsvp-com — sells capital + hands-on partnership to founders; flagged by `entity_type: Investor / Holding` (C4).
  - **B2B telehealth infrastructure / white-label enablement (1):** openloophealth-com — sells clinician network + tech to other healthcare brands (C5).
  - **Membership primary care (1):** onemedical-com — consumer + employer primary care (now Amazon's primary-care surface) (C6).
  - **Renewable-energy project execution services (1):** euclidpower-com — full-suite project services + software to energy developers/IPPs (C7).

**The discriminating signal lives in the pair, not the primary token — but only at the first cut (C2). [Scoped per VR1.]** The presence/absence of a `Biotech / Pharma` secondary cleanly separates the 52 telehealth wrappers from the 9 professional-services firms — a 100% clean split in this sample, in both directions (all 52 carry a Biotech secondary; all 9 carry none). `entity_type: Investor / Holding` then flags the one VC (lsvp). **But the pair does NOT discriminate *within* the 9-firm residual:** 6 of the 9 collapse to the *identical* `(entity_type, offering_category)` pair `(Company, [Services / Consulting])` — bullish-co, heco-partners, ideo-com, onemedical-com, parlance-cc, redantler-com — which are a marketing/capital hybrid, a web-branding consultancy, a global design firm, a membership primary-care provider, a one-person brand studio, and a brand agency: non-comparable jobs the pair + entity_type cannot tell apart. (Two more — euclidpower, openloophealth — share `(Company, [Services / Consulting, Software / SaaS])`, also non-comparable.) So the honest scope is: **the pair cleanly peels the telehealth mass off the residual, but the residual stays a residual** — discriminating *within* it needs the Overview prose (or a vertical/cohort tag), not the offering_category array. A naïve cross-store cut keyed on the primary token alone merges IDEO + Lightspeed + henrymeds + Euclid into one "category"; even the *full pair* still merges IDEO + onemedical + Red Antler.

**Secondary-token holders widen the heterogeneity further.** Beyond the 61 primaries, ~21 profiles carry `Services / Consulting` as a *secondary* tag across yet more shapes: SaaS-led (alpha-sense, usertesting, goinfusive, mdintegrations, noom), pharma/compounding-led (anazaohealth, hallandalerx, hellopepti, niagenplus, strivepharmacy), hardware-makers with a service line (warbyparker, therabody, beta-team), legal-doc software (clerky), marketplace (sesamecare), and more VC (firstround, sequoiacap). The token appears in ~82 of 145 profiles by an "anywhere in array" grep — it is the store's single most over-loaded surface.

## Gap Map

| Sub-question | Store answer | Grade |
|---|---|---|
| Does the primary token alone discriminate buyer-useful sub-shapes? | **No** — it merges ≥6 non-comparable jobs (telehealth DTC, agency, VC, B2B health infra, membership primary care, energy project services). | Clean (gap mapped) |
| Is the discriminating cut already in existing State? | **Partly (scoped per VR1).** The array *pair* + `entity_type` cleanly peel the 52 telehealth wrappers off the 9-firm residual (Biotech secondary present = telehealth; absent = professional/B2B; Investor/Holding = VC). But *within* the 9, 6 collapse to the identical pair `(Company, [Services / Consulting])` — the pair can't separate IDEO vs onemedical vs Red Antler. Discriminating inside the residual needs Overview prose or a vertical/cohort tag, not the array. | Clean for the first cut; gap within the residual |
| Does the store need a new sub-category / field for this bucket? | **No** — for the load-bearing telehealth/non-telehealth cut, query-time grouping on the pair + entity_type is enough (L005). The within-residual ambiguity is real but tiny (9 firms) and is better served by the existing per-profile prose / cohort tags than by minting `Services::Agency` vs `Services::PrimaryCare` sub-types (would over-fit a 9-row tail; L005 trap). | Clean (no-new-primitive) |
| Can a reader trust the sub-shape tally as exhaustive? | **No** — "found, not exhaustive." STRAIN/qualifier prose is unevenly populated; only some profiles carry an inline `# STRAIN` comment. The 6-shape tally is what surfaced, not a census. | Caveated |
| Is the denominator method-robust? | **No (per VR1)** — a *naïve* first-element parse returns **68**, not 61; the correct 61 requires stripping inline `# STRAIN` comments off the frontmatter line before splitting (7 telehealth wrappers — brello, fountain, goodlife, hims, keeps, rexmd, rugiet — carry comment-laden lines). Surfaced here, not just in receipt C1. | Caveated |

**The honest fix (if anything ever graduates):** a *reading convention* — "never group or compare on the `Services / Consulting` primary token alone; read the offering_category pair + entity_type" — most likely a one-line note in QUERYING.md or TAXONOMIES.md, NOT a sub-category, field, or stored object. Load-bearing reason: the data needed to discriminate already renders; the failure is that a reader keying on the lead token over-merges.

## Evidence Used

All store-only; capture clocks are per-profile `captured_at`. No external/live evidence.

- **C1** — Denominator: 61 profiles have `Services / Consulting` as the *primary* (first-array) `offering_category` token; ~21 more carry it secondary; ~82/145 carry it anywhere. Method: frontmatter grep over `store/*/profile.md`, first-element extraction. See `receipts/C1-services-consulting-denominator.md`.
- **C2** — Split: of the 61 primaries, 52 carry a `Biotech / Pharma Products` secondary (telehealth wrapper convention) and 9 do not (professional/B2B services). 100% clean separation in-sample. Same receipt.
- **C3** — Agencies: bullish-co Overview ("marketing operating partner… capital, consulting and creation"), heco-partners ("partner-led creative consultancy… branding and web design"), ideo-com ("global design and innovation consultancy"), parlance-cc ("part brand studio, part consultancy"), redantler-com ("New York brand-building agency"). `store/<d>/profile.md` Overview, captured per profile.
- **C4** — VC: lsvp-com Overview ("global, multi-stage venture capital firm"); `entity_type: Investor / Holding`. Sister VCs firstround-com / sequoiacap-com carry Services as *secondary* with explicit `# STRAIN` comments on the Financial+Services pairing.
- **C5** — B2B health infra: openloophealth-com ("B2B white-label telehealth infrastructure provider"); mdintegrations-com (secondary-token sibling, "telehealth infrastructure company… telemedicine API").
- **C6** — Membership primary care: onemedical-com ("Fall in love with your doctor's office"… now Amazon's primary-care surface).
- **C7** — Energy services: euclidpower-com ("renewable-energy project execution company… full-suite services with a software platform").

## Companies Seen

61 primary-token profiles (52 telehealth wrappers + 9 professional/B2B services), plus ~21 secondary-token holders. The 9 discriminating non-telehealth primaries: bullish-co, euclidpower-com, heco-partners, ideo-com, lsvp-com, onemedical-com, openloophealth-com, parlance-cc, redantler-com. Full primary list in `receipts/C1`.

## Missing / Stale Coverage

- STRAIN/qualifier inline comments are unevenly present — some profiles explain *why* the token was assigned (firstround, sequoiacap, clerky, warbyparker, niagenplus), most do not. So the "why this token" reasoning is not uniformly machine-readable; it lives in prose where it exists at all.
- `Media / Content` (n=2) and CPG (n=2) buckets are too thin to read for comparison; not in scope here, logged as a coverage note (Scout C6).

## Source Gaps

None requiring external panels — this is a pure schema/grain read over already-captured State. The only "gap" is interpretive: the store has no machine-readable field that says "Services-as-telehealth-wrapper vs Services-as-professional-services," but the array pair + entity_type already proxy it, so no new source family is warranted.

## Raw Learning to Preserve

See `run-notes.md` Observations: G1 (primary-token catch-all over-merges ≥6 jobs), S1 (the Biotech-secondary presence/absence is the clean discriminator — signal in the pair, not the token), G2 (denominator depends on counting method: 61 primary / 82 anywhere / 73 by exact-token-frequency — inline comments break naïve counts), W1 (lightest fix is a reading convention, not a sub-category — anti-sprawl), S2 (STRAIN-comment coverage is uneven, so "why this token" isn't uniformly queryable).

## External Completeness Check

Not load-bearing — the question is about the store's own classification grain, not market completeness. The denominator is the store itself; no outside list applies.

## Market Pattern

The store's classification taxonomy is *vertical-shaped at the secondary token and job-shaped at the primary*: for the telehealth cohort, `Services / Consulting` primary is a deliberate convention encoding "clinician service wraps the Rx," and the Biotech secondary is what actually names the vertical. For everything else, `Services / Consulting` is a true residual that absorbs any firm whose value is delivered as expertise/labor rather than a product — and "expertise/labor" spans VC, design, B2B infra, primary care, and energy EPC, which have nothing in common as markets. The token is doing two unrelated jobs (a cohort convention *and* a residual bucket), which is exactly why reading it alone over-claims.

## What Would Change This Answer

- ~~A profile where the array pair + entity_type fail to separate two non-comparable jobs … None found in this sample.~~ **Corrected (VR1): this counterexample DOES exist** — 6 of the 9 non-telehealth primaries share the identical `(Company, [Services / Consulting])` pair (IDEO, onemedical, Red Antler, bullish, heco, parlance). So the pair fails *within* the residual. It still does not push toward a new field, because the failure is on a 9-row tail better served by prose/cohort tags than by sub-typing — but the "clean discriminator" framing was scoped down.
- A real downstream consumer who must cut the store by "professional services" and is materially burned by the over-merge — would raise the reading convention from "nice-to-note" toward a QUERYING/TAXONOMIES edit. The DR4 angle sharpens this: the urgency hinges on whether an *existing* QUERYING.md recipe or render script already keys on `offering_category[0]` and is silently over-merging today (not audited here). Until that audit and a burned consumer, "no new primitive needed" stays live.
