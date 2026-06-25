# Market Read

## Question

Across the captured connected-hardware health/recovery brands (Oura, Whoop, Eight Sleep,
Peloton) plus the pure-hardware foils (Therabody, Hyperice, Nike, Apple), what core
offering and revenue model does each run, and does the universal `offering_category` /
`business_model` frame express the device-sale + recurring-subscription **hybrid**
("device-as-a-service"), or does it collapse that split into a single `business_model`
value?

Mode: **calibration / system-test, store-only.** The deliverable is what the schema can
and cannot express about hybrid hardware+subscription revenue, not a buyer's-guide
ranking.

## Result

**The single-valued `business_model` enum is structurally lossy on co-primary
hardware+subscription revenue, but the loss is invisible at this cohort because captor
judgment happened to be consistent — until Apple, where the same structure flips the
tag.**

Three findings, lead-first:

**(1) Every connected hybrid carries a two-leg revenue structure that `business_model`
can only name one half of.** All four core brands sell (or bundle) a physical device
*and* run a recurring software/membership leg, yet the schema's single-valued
`business_model` forces a primary-leg pick:

| Brand | Device leg | Recurring leg | `business_model` | `offering_category` (ranked) | Split survives in… |
|---|---|---|---|---|---|
| **Oura** | Ring sold one-time $349–$499 `[published]` | App membership $5.99/mo | `Subscription` | [Hardware, Software/SaaS] | `STRAIN:` comment + body + offering_category |
| **Whoop** | Device *included* in plan (no separate sale) | Membership $199–$359/yr `[partial]` | `Subscription` | [Hardware, Software/SaaS] | `STRAIN:` comment + body + offering_category |
| **Eight Sleep** | Pod cover sold one-time $2,749 `[published]` | Autopilot sub $199–$399/yr, **required first 12 mo** | `Subscription` | [Hardware] **only** | `STRAIN:` comment + body (offering_category drops it) |
| **Peloton** | Bike/Tread one-time $1,695–$6,695 `[partial]` | All-Access membership (required) | `Subscription` | [Hardware, Media/Content] | body ("two revenue legs") + offering_category |

The recurring leg is the recoverable half only by reading prose or the inline `STRAIN:`
comment — and the channel that carries it is **inconsistent**: Oura/Whoop carry it in
`offering_category` *and* a STRAIN tag; Eight Sleep's mandatory subscription does **not**
appear in `offering_category` at all (demoted to "companion"), surviving only in a
comment; Peloton has **no** STRAIN marker, only body prose.

**(2) The primary-leg judgment is not reproducible across structurally identical
companies.** Oura (device sold one-time + recurring app) → `Subscription`. Apple (device
sold one-time + recurring services) → `Transactional / One-time`. **Same two-leg
structure, opposite tag** — the call tracks which leg the captor judged dominant
(strategically central recurring leg for the pure-play wearable; revenue-dominant
hardware for Apple), not whether the structure is hybrid. (Oura: `profile.md:48`; Apple:
`profile.md:40,65`.)

**(3) The field answers neither "has a device" nor "has recurring revenue" for hybrids.**
A reader filtering `business_model: Subscription` to find recurring-revenue businesses
**misses Apple** (recurring services, tagged Transactional). A reader filtering
`Transactional / One-time` to find device-sellers **misses Oura/Whoop/Eight
Sleep/Peloton** (all sell or bundle a device). For a single-leg foil the field is fine;
for a two-leg hybrid it under-determines both questions.

**Foils (pure one-time hardware) confirm the field works where revenue is single-leg:**
Therabody ($84.99–$1,249.99, `Transactional`), Hyperice ($25–$1,548, "No subscription
or membership is shown," `Transactional`), Nike (recovery devices; "Membership is a FREE
loyalty layer, not a subscription," `Transactional`). No strain, no loss — the enum is
accurate when there is one leg.

## Gap Map

- **Answered cleanly (store-only):** the per-brand revenue structure, the device and
  recurring prices, and *that* each hybrid has two legs — all legible from captured
  frontmatter + body. The schema **does** flag the strain itself: three of four core
  brands carry an explicit `STRAIN:` inline marker on `business_model` or
  `offering_category`. Fail-loud worked.
- **Fell short (structural):** no structured field encodes the **composite** revenue
  shape. `business_model` is single-valued by contract ("the primary model if several
  apply" — `TAXONOMIES.md:76`), so a hybrid is forced to a single token and the split
  is recoverable only from prose/comments. `offering_category` is a partial, inconsistent
  proxy (it encodes the *type* of the second offering when the captor ranks it, but
  Eight Sleep's mandatory sub is absent from it).
- **What would have changed the answer:** if `business_model` were a ranked multi-select
  like `offering_category`, the hybrid could carry `[Subscription, Transactional]` and
  both reader filters in finding (3) would resolve. *(Observed cost of the single-valued
  design — not a proposal; see run-notes W1 and the decision boundary.)*

## Evidence Used

All store-only; no external or current-event claims. Pricing quoted is the captured
point-in-time snapshot (most under live promos per each profile's `site_notes`/
`unverified_fields`) and is illustrative of structure, not a live price assertion.

- `C1` — denominator: the connected hybrids are **exactly** the only four
  `Subscription`-tagged Hardware companies in the store. `grep` of
  `offering_category: …Physical Products / Hardware` × `business_model` over `store/*`:
  19 Hardware profiles, of which the only four `Subscription` are oura, whoop, eightsleep,
  onepeloton; all 15 others (7 watches, Apple, Ford, Nike, Therabody, Hyperice, Warby
  Parker, Electra Aero, beta-team) are `Transactional / One-time`.
- Oura: `store/ouraring-com/profile.md:41,48,71-73`.
- Whoop: `store/whoop-com/profile.md:35,40,42,59,63-67`.
- Eight Sleep: `store/eightsleep-com/profile.md:37,42,44,67-68`.
- Peloton: `store/onepeloton-com/profile.md:36,41,43,64,67-70`.
- Therabody: `store/therabody-com/profile.md:49,51,72-79`.
- Hyperice: `store/hyperice-com/profile.md:49,51,84`.
- Nike: `store/nike-com/profile.md:47,49,88-94,115`.
- Apple: `store/apple-com/profile.md:38,40,59-60,65,117`.
- Contract: `TAXONOMIES.md:74-87` (`business_model` closed set, single-valued, "primary
  model if several apply"); `TAXONOMIES.md:110` (`offering_category` is a ranked
  multi-select; position 1 is primary).

## Companies Seen

Core cohort (connected device + companion app + recurring leg): **Oura, Whoop, Eight
Sleep, Peloton.** Pure-/mixed-hardware foils: **Therabody, Hyperice, Nike, Apple.**

Cohort-draw note: no single structured field cleanly isolates "connected health/recovery
hardware." `primary_industry` scatters across three values for structurally similar
brands — Oura/Whoop/Therabody = `Healthcare & Life Sciences`, Eight Sleep/Apple =
`Technology`, Peloton/Hyperice/Nike = `Sports & Recreation`. The cleanest *available*
draw is `offering_category ⊇ Hardware` ∧ `business_model = Subscription` — which recovers
the four pure-plays precisely (`C1`) but is a **coverage artifact of captor homogeneity**,
not a robust key: it wrongly excludes Apple (same hybrid structure, hardware-dominant tag)
and would wrongly include any future device-light subscription that happens to ship a
gadget. This both echoes and inverts run-036 G3 ("`business_model` is the cohort key"):
here `business_model` *splits* a structurally coherent cohort rather than recovering it,
and only looks like a key because the four members were tagged the same way.

## Missing / Stale Coverage

- Prices are promo-period snapshots across the whole cohort (every profile flags an
  active sale in `site_notes`/`unverified_fields`). Fine for structure; do not read as
  live magnitudes.
- Whoop checkout total, Oura per-finish prices, Eight Sleep Pod 5 Ultra price, and
  Peloton refurb prices are partially uncaptured (client-rendered or behind
  join/checkout subdomains) — noted in each profile, immaterial to the structural read.

## Source Gaps

None blocking — this is a pure schema-grain calibration answerable store-only. A future
*magnitude* read of hybrid economics (device ASP vs subscription LTV, attach rate, churn)
would need filings/IR, not the marketing site — the hardware analogue of run-036 G2/G5
(marketplace take rate lives off-site). Not needed for this structural question.

## Raw Learning to Preserve

See `run-notes.md` Observations: **S1** (single-valued `business_model` lossy on hybrid;
the schema-edge mechanism), **G1** (no structured composite-revenue field; the split
lives in prose/STRAIN), **R1** (primary-leg tag not reproducible — Oura vs Apple flip;
reader-filter risk-miss), **G2** (cohort-draw inversion of run-036 G3), **S2** (L006
boundary: the price-visibility token does **not** mislead here, sharpening L006's scope
to two-sided/intermediary entities), **W1** (lightest path *if* anything graduates is a
ranked-multi-select `business_model`, not a new field — held; "no new primitive needed"
stays live).

## External Completeness Check

Completeness is load-bearing only for the denominator claim (`C1`), and that is fully
settled **inside** the store by exhaustive grep — every Hardware profile was enumerated,
not sampled. No outside denominator needed: the claim is "within the captured store,
these four are the only Subscription-tagged hardware," which is a closed local set, not a
market-universe claim. Per L004, this is "not found outside this store," not "these are
the only such companies in the market."

## Market Pattern

"Device-as-a-service" is a real and recognizable consumer-hardware structure, but it is
**not one revenue model** — it is a spectrum of two-leg blends the schema flattens:
- **Subscription-primary, device bundled:** Whoop (you join, the device comes with it).
- **Device-primary, subscription mandatory:** Eight Sleep (buy the Pod, Autopilot
  required), Peloton (buy the bike, membership required).
- **Device-primary, subscription optional-for-full-value:** Oura (ring works; membership
  unlocks the scores).
- **Device-dominant, subscription overlay:** Apple (hardware is the revenue core;
  services are the retention flywheel) — tagged `Transactional`.
- **Pure one-time, no recurring:** Therabody, Hyperice, Nike recovery devices.

The schema names the *endpoint a captor judged dominant*; the *blend* — which leg is
required, which is optional, who bundles whom — lives entirely in prose. That is the
honest result of the calibration: query-time grouping plus prose reads the blend fine for
a human; the structured field alone cannot, and should not be trusted to filter
hybrid-revenue companies in or out.

## What Would Change This Answer

- A **second homogeneous hybrid cohort** plus a **real consumer** who needs to *filter*
  by composite revenue model (not just read it per-company) would raise the question of
  whether `business_model` should become a ranked multi-select. Absent that consumer,
  this stays a documented reading caveat — **"no new primitive needed."** (W1.)
- If a future capture tags a structurally-identical hybrid *inconsistently* with these
  four (e.g. a new wearable tagged `Transactional`), that would harden R1 from a
  single Oura-vs-Apple flip into a reproducibility defect worth a reading convention.
- This run is also a **second entity-type test for L006** (after marketplaces): the
  price-visibility token here reads correctly per-offering and does **not** trap the
  reader, because these entities are not two-sided/intermediary — the buyer can obtain
  every price. That sharpens L006's scope rather than confirming its trap (S2); it does
  not graduate or alter L006 (decision boundary — observation only).
