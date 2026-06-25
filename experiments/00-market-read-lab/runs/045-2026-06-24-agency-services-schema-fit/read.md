# Market Read

## Question

For a marketing/brand/innovation leader building a shortlist of creative/strategy **agency
partners** (ideo, redantler, heco-partners, bullish, parlance), can the captured store
support a vendor comparison — what each does, who it serves, its positioning wedge,
proof/clients, and how to engage — or does Truffle's product/price-shaped universal schema
leave a **services** buyer with nothing comparable?

Gap-probe. Builder lens: schema fit for the no-catalog, no-list-price, project-based
professional-services entity type — the most product-hostile corner of the entity spectrum
the schema-edge series (036 marketplaces / 037 wearables / 042 deep-tech / 035 investors)
has not yet hit. Store-only.

## Result

**Split verdict: the buyer can build the shortlist — but only by reading prose. Every
structured field the schema offers is either degenerate across the cohort or can't even
assemble it.** The product/price spine has nothing to bind to on a pure-services firm, yet
the body sections carry the buyer's whole decision richly. "No new primitive needed" holds,
on a sharper edge than prior runs.

**(1) The cohort is not recoverable from any structured field (the schema can't even
assemble it).** A buyer who doesn't already know the five names cannot draw them from
frontmatter:
- `offering_category: [Services / Consulting]` returns **80** profiles (C1) — essentially the
  entire telehealth cohort carries it as a *secondary* value (clinical-services leg), plus VC
  firms (firstround, lsvp, sequoia), usertesting, warbyparker. Useless as an agency key.
- `business_model: Services / Project-based` returns **8** (C2): the 5 agencies **+ 3
  contaminants** — euclidpower (renewable-energy services+SaaS), verdegoaero (aerospace
  manufacturing), goinfusive (healthcare supply-chain software). The field recovers
  "firms that bill per project," not "creative agencies."
- So the entity type *creative/strategy agency* has **no isolating structured handle**. This
  is a **new, more severe flavor of `denominator-reconciliation`**: prior runs (036 G3, 037
  G2, 039 DR1, 042 G3 — the n=4 industry-draw) found a roughly-right draw *contaminated* by a
  stray member; here **no field draw even approximates the cohort**.

**(2) Within the cohort, the structured fields are degenerate *for buyer differentiation*
(the schema can't tell the members apart in a way a buyer can use).** The four **typing**
fields are identical across all five: `entity_type: Company` · `offering_category: [Services
/ Consulting]` · `business_model: Services / Project-based` · `primary_industry: Consulting &
Professional Services` (C3). The two fields that *do* vary — `target_market` (IDEO is
`[B2B, B2G]`; the other four `[B2B]`) and `portfolio_shape` (`Flagship + companions` for
ideo/heco/parlance, `Single` for redantler, `Multi-product` for bullish) — vary in
**buyer-irrelevant ways**: neither separates a global firm from a solo operator (see (3)).
The closed `offering_category` set **bottoms out** at `[Services / Consulting]` — there is no
finer leaf in TAXONOMIES.md (no `Services / Creative Agency`) to distinguish a global
innovation consultancy from a one-person brand studio. This is the **taxonomy-bottomed-out**
condition, sharper than run-039's SaaS flattening: there `[Software / SaaS]` at least sat
above ~19 real sub-markets in the corpus *and* finer leaves were conceivable; here the single
value *is* the entity type, with nothing finer available in the closed set in principle.

**(3) The buyer's #1 differentiator — firm scale/shape — has no structured field at all.**
The first question an agency buyer asks is "solo operator, boutique, or global firm?" The
cohort spans that entire range:
- **IDEO** — global, five studios (Cambridge/Chicago/London/SF/Shanghai), next-gen C-suite,
  a 266-leader research survey (the IDEO IQ study, run by NewtonX) (ideo profile:62, :136, :127).
- **Red Antler** — mid-size NY agency heading a 3-studio group (Red Antler / Fat Earth / Wild
  Fruit), ~80+ case studies (redantler profile:55, :111).
- **Bullish** — hybrid VC-fund + consultancy + creative studio, ~60 engagements (bullish
  profile:59, :113).
- **Heco** — two-partner boutique, "no B-team," 12–16-week engagements (heco profile:111, :119).
- **Parlance** — one person + an EA, capped at ~3 concurrent engagements (parlance profile:73).

`portfolio_shape` is the nearest structured field and it is **degenerate for this question**:
**three** firms across the whole size spectrum — IDEO (global), Heco (2-partner boutique),
and Parlance (solo operator) — all carry `Flagship + companions` (C3); it encodes
service-line structure, not firm size. Scale lives only in prose.

**(4) Prose carries the entire buyer decision — richly — for all five.** Every shortlist
input a services buyer needs is present and well-organized in the body:
- *what each does / capability set* → `What they offer` (IDEO's 3 design-service lines + 3
  Labs; Red Antler's 4 practice areas; Heco's 8 capabilities; Bullish's Capital/Consulting/
  Creative; Parlance's FTE/Advisory/Sprints).
- *who it serves / specialization* → `Positioning & audience` (Heco = "complex/technical
  products"; Red Antler = startups + AI-company pivot; Bullish = US consumer/B2C only;
  Parlance = early-stage founders/investors in regulated categories).
- *proof / named clients / outcomes* → `Credibility & proof` (IDEO: Ford/Moderna/PillPack;
  Red Antler: Casper/Allbirds/Ramp; Bullish: Nike/Pepsi + portfolio; Heco: Google/Motorola +
  Awwwards; Parlance: Apple-CD pedigree, Aescape/TIME).
- *engagement model / how to engage / rough price* → `How it works / model` (IDEO three
  contact funnels; Heco enterprise@ vs earlystage@; Bullish fund economics + project fees;
  Parlance Calendly + FAST equity protocol, equity up to 50% of fee).

A human reading the five profiles **can** build and differentiate the shortlist cleanly.
This is the **buyer-value inverse** of the schema-fit failure and continues the run-042
S2 / run-043 S1 "store is a genuine strength for the reader" thread: the decision is legible
from State, just not queryable.

**(5) The price-visibility token is faithful on services — and `[on-request]` here is honest
market structure, not a capture gap.** Four of five are uniformly `[on-request]`; **Parlance
is the lone partial-transparent member** and the token captures it correctly at offering-line
grain: **Sprints "Starting at $15k" `[published]`**, **Office Hours "$225 / 30 mins"
`[published]`**, Mentorship "First Session Free" `[published]`, while its bespoke fractional/
advisory lines stay `[on-request]`/equity (parlance profile:62–66). Crucial nuance: for
project-based services, `[on-request]` reflects that **no list price exists** (custom-scoped),
unlike a DTC brand gating a price that does exist — so the schema's pricing silence here is
**faithful, not lossy**. The token's "can I even get a price?" axis (SCHEMA 2.3) generalizes
correctly onto the entity type with the least price surface.

## Gap Map

| Buyer need | Structured field? | Verdict |
|---|---|---|
| Assemble the agency cohort | `offering_category` / `business_model` | **Fails** — no isolating key (80 vs 8-with-3-contaminants). C1/C2. |
| Distinguish members | 4 typing fields identical; 2 (target_market, portfolio_shape) vary buyer-irrelevantly | **Fails** — taxonomy-bottomed-out; no finer value. C3. |
| Firm scale/shape (solo→global) | `portfolio_shape` | **Fails** — degenerate (ideo=heco=parlance value, 3/5). Prose only. C3. |
| Capability / specialization / proof / engagement | body sections | **Carried in prose** — rich, well-organized, sufficient for a human shortlist. |
| "Can I get a price?" | price-visibility token | **Works + faithful** — `[on-request]` = no list price exists; Parlance's `[published]` split captured. C5. |
| Visual/brand quality (design-agency-specific) | profile `Visual & brand impression` (all 5); `visual.md` (2/5: bullish, parlance) | **Carried in profile.md** for all 5; standalone `visual.md` adds depth, not required to shortlist. |

The clean gap map *is* the gap-probe result: the schema **fails by having nothing to grab**
(degenerate + non-isolating), not by holding the wrong-grain thing — distinct from the
marketplace take-rate (036) and wearable-TCO (043) "wrong grain" failures.

## Evidence Used

All local store State (captured 2026-06-04 → 2026-06-18); no external sources, no spend.

- **C1** — `offering_category: [Services / Consulting]` matches 80 profiles: `grep -l
  'offering_category:.*Services / Consulting' store/*/profile.md | wc -l` → 80; includes
  telehealth (secondary value), VC firms, usertesting, warbyparker.
- **C2** — `business_model: Services / Project-based` matches 8: the 5 agencies + euclidpower,
  verdegoaero, goinfusive (the 3 non-agency contaminants).
- **C3** — identical classification tuple across the 5; `portfolio_shape`: ideo/heco/parlance
  `Flagship + companions`, redantler `Single`, bullish `Multi-product` (varied, but not by
  firm scale).
- **C5** — parlance profile:62–66 (`[published]` $15k / $225 / free vs `[on-request]` bespoke);
  other 4 uniformly `[on-request]` (ideo:66–74, redantler:61–64, heco:62–69, bullish:67–69).
- Firm-scale anchors: ideo:62/127/136, redantler:55/111, bullish:59/113, heco:111/119,
  parlance:73.

## Companies Seen

Core set (5): ideo.com, redantler.com, heco.partners, bullish.co, parlance.cc — all
`offering_category [Services / Consulting]` + `business_model Services / Project-based` +
`primary_industry Consulting & Professional Services`, all B2B, none with `offerings.md`
(no SKU grain). Foil: clerky.com (legaltech hybrid; `business_model Transactional / One-time`,
priced packages $427/$819, **has** `offerings.md`) — confirms the contrast: clerky productizes
into priced SKUs, the 5 agencies do not. Contaminants surfaced by the cohort-key test:
euclidpower, verdegoaero, goinfusive (non-agency project-billed firms).

## Missing / Stale Coverage

- The cohort is **partial by construction** — these 5 are the captured agencies; the real
  creative-agency market is vast (Pentagram, Wolff Olins, Collins, Instrument, R/GA…), none
  captured. "Not found in store," not "not there." No completeness claim is made.
- Captures are 2026-06-04 → 2026-06-18 (≤3 weeks old); fresh enough. Agency rosters/pricing
  drift slowly; no staleness flag.
- `visual.md` exists for only 2/5 (bullish, parlance) — uneven module coverage, noted not chased.

## Source Gaps

None requiring an external panel for *this* question — it asks what the existing capture
expresses, and store-only answers it. The one off-surface fact a buyer might still want
(headcount/revenue/funding — firm scale in numbers) is flagged `unverified_fields` on every
profile as "deep-research, not a marketing-site fact" (ideo:32, redantler:27, bullish:30) —
honest absence, not a capture failure.

## Raw Learning to Preserve

See `run-notes.md` Observations: G1 (no isolating cohort key — severe denominator-
reconciliation flavor), G2 (within-cohort degeneracy, worse than 039), G3 (firm-scale axis
unstructured; portfolio_shape degenerate), S1 (prose carries the full buyer decision —
buyer-positive), S2 (price-visibility token faithful on services; `[on-request]` = no price
exists, not gated), S3 (parlance transparency split captured at line grain but invisible to a
frontmatter filter — run-044 G1 echo), W1 (anti-sprawl: no field; the closed offering_category
set lacks an agency/specialization value but a scale field would rot), S4 (visual.md 2/5; the
`Visual & brand impression` section in profile.md already serves the design-agency buyer).

## External Completeness Check

Not run (store-only; bounded-live declined this cycle after run-040's spend block). The cohort
is explicitly partial; no "N agencies do X" headline is made, so no external denominator is
load-bearing. A real shortlist would need a SERP/listicle panel to find the uncaptured majors —
flagged, not chased.

## Market Pattern

Pure project-based professional-services firms are the **structural antithesis of the schema's
product/price spine**. The universal classification was built for sellers with a catalog and a
price surface; an agency has neither — its "product" is confidential client work and its price
is a custom scope. The result is a schema that is simultaneously **non-isolating** (can't
assemble the cohort) and **degenerate** (can't differentiate within it), while the **prose
layer carries the buyer's entire decision** — capability, specialization, proof, scale, and
engagement model — better than any field could. The one structured pricing convention that
*does* generalize (the price-visibility token) works *because* its question — "can I even get a
price?" — is exactly the axis that survives when there is no list price: `[on-request]` is the
honest answer, and Parlance's published `$15k`/`$225` anchors are correctly surfaced as the
exception. This is the cleanest case yet for the engine's "evidence (prose), not a
score/field" principle: the entity type that most defeats structure is also the one the prose
serves best.

## What Would Change This Answer

- A **filtering/programmatic** consumer (not a human reader) who needs to *select* agencies by
  scale, specialization, or price-transparency from frontmatter — then the degeneracy (2/3)
  becomes a real wall and the lightest fix would be an offering_category specialization value
  or a multi-select, **never** a firm-scale field (a rotting captor judgment, mostly-blank
  store-wide — fails engine-dev's fillable-cut bar). Even then, prose carries it for a human.
- A **second pure-services cohort** (e.g. management/strategy consultancies, law firms, dev
  shops) showing the same non-isolating + degenerate pattern would move this from a single-
  cohort sighting toward a general "services entity type defeats the product spine" lesson.
- An agency buyer who weights **visual/brand craft** heavily and finds the profile `Visual &
  brand impression` section insufficient — would raise `visual.md` from "adds depth" to
  "required," and the 2/5 coverage gap would bite.
