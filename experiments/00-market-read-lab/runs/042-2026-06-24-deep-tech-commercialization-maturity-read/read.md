# Market Read

## Question

Across the captured climate / energy / deep-tech slice (electra-aero, verdegoaero,
blueenergy, cfs-energy, euclidpower, evoloh, sorafuel, beta-team), can a reader — or a
delegated agent — tell a **shipping / commercial product apart from a pre-revenue pilot or
pre-product vision** from captured State alone, and where does the DTC/telehealth-shaped
schema force *commercialization maturity* to be invented?

## Result

**Lead:** A careful human reader **can** rank these eight on commercialization maturity
from captured State — the evidence is present and the store does *not* force maturity to be
invented. But it lives **entirely in prose** (a milestones/traction block + `unverified_fields`),
never in a structured field. A delegated agent doing the cheap thing — quoting `description`
+ frontmatter — would **systematically over-claim maturity**, because every headline/structured
field is present-tense and maturity-blind. So the honest answer is split by *reader type*:
safe for a careful human, a live over-claim risk for a shallow agent. This is the
"make-AI-safe-to-delegate-to" failure the run was built to probe, and it reproduces. **No
new field is needed** (n=8; prose carries it; a `stage` enum would be a rotting captor
judgment — see Gap Map).

**(1) Maturity is recoverable, but only from prose, and the ranking is clean.** Reading
each profile's milestones/traction lines + `unverified_fields` together, the eight rank on
attested commercialization maturity (most → least), with the *attested* anchor for each:

| # | Company | Attested maturity anchor (from captured State) | Maturity read |
|---|---|---|---|
| — | **euclidpower** | Commercially **operating now**: services + SaaS, "22 GW supported / 1,100+ projects / 31–37 states," acquired Thresh Power 2026-04-30 | **Operating** — but a services/SaaS firm, **not** pre-revenue deep-tech (foil; see Companies Seen) |
| 1 | **beta-team** | **Public co** (2025 IPO, NYSE:BETA, $1B+ raised, 10-Q, Q1-2026 results); 188k sq-ft mfg, "up to 300 aircraft/yr"; **UL-certified** Charge Cubes; DO-160G/ARP4754/DO-254; FAA test-pilot eval | **Early-commercial hardware** — components shipping/certified; flagship aircraft still in certification, no published price |
| 2 | **evoloh** | **Published** forward price ("below $250/kW for 2026-27 deliveries"); "500 MW binding orders to date," 16 GW signed intent; S440 pilot "operational in 2027" | **Order-book, pre-delivery** — binding orders + the slice's only `[published]` price; deliveries future |
| 3 | **electra-aero** | EL2 demonstrator first flew 2023-11-11; **FAA Part-23 type-cert application** submitted 2025-12 (not granted); 2,200 pre-orders / ~$9B pipeline (self-reported); $115M Series B 2025-04 | **Flying demonstrator, pre-cert** — strong demand signals, zero deliveries; profile itself names "stage" as the visible risk |
| 4 | **cfs-energy** | $2B+ raised; **SPARC** net-energy *demonstration* machine under construction at Devens; ARC plant "planned"; Google 200 MW + Eni >$1B offtake signed; **zero power produced** | **Proof-stage, heavily capitalized** — partners signed, no output; Q>1 still "predicted" by papers |
| 5 | **verdegoaero** | Founded 2017; powerplants "being developed with USAF/NASA support"; VH-4T "maturing… since 2024"; products route to "Inquire" | **Development / dev-contract stage** — no delivered commercial product evidenced |
| 6 | **blueenergy** | Founded 2023; first site "planned" in Texas; $380M financing 2026-04; NRC licensing topical report approved; GE Vernova turbines "reserved for site delivery in **2029**" | **Pre-construction / development** — financing + a regulatory milestone, no plant, no power sold |
| 7 | **sorafuel** | $14.6M round 2026-04; pilot facility to be **constructed**; demonstration ("gallons → barrels") in "18–24 months"; **LOI** (not signed offtake) for first 10 M gal of *future* e-SAF | **Pre-pilot, earliest** — no production; everything forward-dated |

The ranking is defensible *because* the bodies carry dated, specific maturity anchors. That
is a genuine store strength on this axis (C2).

**(2) Every structured / headline field is maturity-blind — and `description` actively
launders vision into shipping.** The `description` field is uniformly present-tense:
electra "**Builds** the EL9," evoloh "**Manufactures** electrolyzer stacks," sorafuel
"**Produces** sustainable aviation fuel." Read alone (the cheap delegated move), all three
imply ongoing commercial operation — yet electra has delivered zero aircraft, evoloh's
deliveries are 2026-27, and sorafuel has **no production at all** (pilot still to be built).
The single field most likely to be quoted is the one that over-claims maturity hardest (C3).

**(3) `business_model` is empty or intent-only on the pre-revenue set.** It is **blank**
for cfs-energy and sorafuel (the closed set has no value for "pre-revenue / no commercial
model yet" — an L005-style *subtractive* absence, cousin to run-035's empty-business_model-for-investors).
Where populated, it states the *planned* model (electra/evoloh `Transactional / One-time`,
blueenergy `Usage-based / Consumption`) — indistinguishable from an operating company's.
`offering_category` carries the **same hardware value** `[Physical Products / Hardware]` for
beta-team (public, shipping components — it also lists `Services / Consulting`) and electra
(zero deliveries), so the category that *does* match between them encodes nothing about
maturity. No structured field separates "selling" from "intends to sell" (C3).

**(4) `unverified_fields` is the unsung maturity-protector — at prose grain.** Across all
eight it consistently and honestly flags exactly the maturity-relevant absences:
sorafuel "current production… pages describe a planned pilot"; electra "pre-order pipeline
is site-reported, not a price card"; cfs "capital raised is self-reported"; near-universal
"revenue/headcount/cap-table not shown." This is the one near-structured surface that guards
against over-claim — but it is a free-text list whose protection depends on the downstream
reader actually carrying it (the L002/L004/038-R1 relay shape, here on the maturity axis) (C2).

## Gap Map

| Where Truffle stood | Verdict | Evidence |
|---|---|---|
| Rank 8 deep-tech cos by commercialization maturity | **Answered cleanly — from prose** | Milestones + `unverified_fields` per profile; Result (1), C2 |
| Tell shipping from vision via a *structured field* | **Could not** — no `lifecycle`/`stage`/`maturity` field exists; `business_model`/`offering_category`/`description` are present-tense or blank | Result (2)/(3); grep returned no stage field |
| Protect a delegated agent from over-claiming maturity | **Partial** — `unverified_fields` carries the guard, but at prose grain, relay-dependent | Result (4) |
| Draw the cohort itself from `primary_industry`/`offering_category` | **Could not** — scatters across Automotive/Manufacturing/Energy; pulls in euclid (operating services) as a non-pre-revenue foil | Companies Seen; denominator-reconciliation |

**What would have changed the answer:** a structured maturity/stage signal would let a
*shallow* agent rank without prose-reading — but see "What Would Change This Answer" for
why that field would rot. Outside confirmation of the self-reported milestones (trade press,
filings) would harden the *absolute* stage of each, though not the *relative* ranking.

## Evidence Used

All evidence is local store files captured 2026-06-14 (Firecrawl). No external/live sources.
Claim IDs map to receipts in `receipts/`.

- **C1** — slice denominator (which 8 are the cohort; euclid is a foil): receipt `denominator-deep-tech-slice.md`.
- **C2** — maturity ranking + the prose surfaces that carry it: receipt `maturity-classification.md`.
- **C3** — structured fields are maturity-blind / `description` over-claims: receipt `maturity-classification.md` (field-vs-prose columns).

## Companies Seen

Eight read in full: electra-aero, verdegoaero-com, blueenergy-co, cfs-energy,
euclidpower-com, evoloh-com, sorafuel-com, beta-team.

- **Pre-revenue deep-tech (the real cohort, n=7):** beta-team, evoloh, electra-aero,
  cfs-energy, verdegoaero, blueenergy, sorafuel. (beta-team is the most mature — public,
  shipping components — but its *flagship aircraft* is still pre-certification, so it sits
  at the commercial edge of the pre-revenue-flagship cohort, not outside it.)
- **Foil (operating, not pre-revenue):** euclidpower — a renewable-energy services + SaaS
  firm operating at scale today; included by the energy draw but **not** a "is it real yet"
  case. Its presence is itself the denominator finding: the slice an industry/category draw
  returns is **not** the pre-revenue cohort.
- **Excluded by design:** ford-com, uber-com (tagged Automotive/Energy-adjacent but mature
  operating companies; foils named in the Scout contract).

`primary_industry` for the eight scatters: Automotive & Mobility (electra), Manufacturing &
Industrial (verdego, beta), Energy & Utilities (the other five). **Fourth sighting** that an
industry draw is the wrong key for an entity-shape cohort (after run-036 G3, run-037 G2,
run-039 DR1) — here the entity shape is "pre-revenue deep-tech," not an industry.

## Missing / Stale Coverage

All eight captured 2026-06-14 (10 days old at read) — fresh. blueenergy and sorafuel carry
the most recent dated milestones (Apr–May 2026 funding/financing), so their captures sit
close behind fast-moving events; a real stage could advance between captures. No profile is
stale by clock, but stage is the most freshness-sensitive fact in this cohort (a "pilot in
18–24 months" claim decays fastest).

## Source Gaps

- **No structured maturity/stage signal** is the cohort's defining absence — but see the
  rotting-field argument below; the gap is real without being a build mandate.
- **Self-reported milestones, unconfirmed.** Funding rounds, order books, pipelines,
  partner/offtake deals are all self-reported on owned pages and flagged as such by the
  profiles. The **filings / IR / trade-press** source family (10-Q for beta-team; press for
  the rest) is the panel that would independently date and confirm absolute stage. This is
  the same off-surface, spend/approval-gated source family flagged by run-036 G2,
  run-037 Source Gaps, and run-038 G2 — now hit on the maturity axis. Not chased (store-only).

## Raw Learning to Preserve

See `run-notes.md` Observations: G1 (description launders vision→shipping), G2 (no
structured maturity field; business_model blank on pre-revenue), S1 (unverified_fields is
the maturity-protector, prose-grade), S2 (maturity recoverable cleanly from prose — a store
strength, not just a gap), G3 (denominator-reconciliation n=4; industry draw ≠ pre-revenue
cohort; euclid foil), R1 (delegated-agent over-claim risk on the present-tense description),
W1 (lightest path = a read/relay convention, not a stage field).

## External Completeness Check

Not run — store-only by contract. The cohort is an explicitly **known-partial,
capture-biased** slice (eight profiles that happen to be captured), not a census of
deep-tech. Say "not found in the captured slice," never "no such company." An outside
denominator (e.g. a climate-tech tracker) would be needed to claim cohort completeness; it
is not load-bearing for this read, which is about *whether captured State carries maturity*,
not *how many deep-tech cos exist*.

## Market Pattern

Across this deep-tech cohort the real-world maturity gradient is wide — from a public,
component-shipping manufacturer (beta-team) to a pre-pilot fuel startup with an LOI and a
projection (sorafuel) — yet the **structured fields compress that entire gradient to flat**:
identical `offering_category`, present-tense `description`, intent-only or blank
`business_model`. The maturity signal survives only in the milestones prose and
`unverified_fields`. For deep-tech specifically, the buyer/scout's *first* decision fact
("is this real yet?") is therefore **legible but not queryable** — the same "diagnosable,
not an ingredient" frontier run-039 CR1 hit on competitor neighborhood, here on the maturity
axis. Truffle's honest-absence discipline (`unverified_fields`, `[on-request]` price tokens,
"self-reported" labels) is what keeps the read safe; the risk is entirely at relay, when a
shallow consumer quotes the present-tense headline and drops the guard.

## What Would Change This Answer

- **A second pre-revenue-vs-operating cohort showing the same description-overclaim** (e.g.
  early-stage biotech, pre-launch consumer hardware) would move G1/R1 from a deep-tech
  singleton toward a general "present-tense `description` over-claims maturity on pre-revenue
  entities" pattern.
- **A real returning consumer who must *filter* (not just read) by maturity** — only then
  does a structured signal earn its keep.
- **Why a `stage`/`maturity` field would rot (the anti-sprawl case):** stage is a captor
  *judgment* on a continuum (is BETA "commercial" because components ship, or "pre-commercial"
  because the aircraft isn't certified?), it decays fastest of any field (sorafuel's "pilot
  in 18–24 months" is wrong in 18–24 months), and it would be **blank or stale** for most of
  the store — failing engine-dev's "a field is a cut you can fill reliably" bar. The lightest
  path *if* anything graduates is a **read/relay convention** — "for pre-revenue/deep-tech,
  rank maturity from the milestones block + `unverified_fields`; treat present-tense
  `description` as positioning, not attainment; carry the self-reported flag" — **not** a new
  field. "No new primitive needed" stays live. Mirrors run-036/037/039/040 anti-sprawl W1
  landings.
