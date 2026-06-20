# Market Read

## Question

Across the captured store, which brands roll up to a shared corporate parent (via
`parent`/`owns` frontmatter), how concentrated is ownership (any parent linked to
multiple captured brands), and can the store map market consolidation at query time —
or is ownership mostly undisclosed or uncaptured?

## Result

**The store can render an ownership *map*, but cannot *traverse* it — and cannot claim
consolidation as a market fact.** Three layered findings:

1. **Ownership disclosure is sparse but real.** Of 126 profiles carrying the fields,
   **13** disclose a non-empty `parent:` and **15** a non-empty `owns:` (C1). The rest
   (`parent: []` = 109) are mostly silent. So a "who owns whom" map exists — it's just a
   thin, disclosed-only slice of the corpus.

2. **The map almost never joins.** Of ~21 distinct domains referenced by `parent`/`owns`
   edges, **only 3 (lifemd.com, qualtrics.com, rexmd.com) are themselves captured** (C2). Concretely:
   - **`lifemd ↔ rexmd` is the *single* fully-captured, bidirectionally-reconciled
     ownership edge in the entire store** (rexmd `parent:[lifemd.com]` and lifemd
     `owns:[rexmd.com,…]`) (C3).
   - **`delighted → qualtrics`** has both endpoints captured but **qualtrics' `owns:` does
     not list delighted back** — a one-directional, unreciprocated edge (C4).
   - Every other edge **dangles**: the parent or sibling isn't in the store (amazon,
     thirtymadison, niagenbioscience, richemont, openaifoundation; reverb, depop, ezra,
     fordpro, sendgrid, segment, ubereats, shapiromd, navamd, converse, …).

3. **The "concentration" you can see is structurally untrustworthy.** Four parents link
   ≥2 captured children — amazon (aws, onemedical), thirtymadison (keeps, nurx),
   niagenbioscience (niagenplus, truniagen), richemont (cartier, alange-soehne) — but
   **all four parents are uncaptured**, the richemont pair is *inferred* (STRAIN), and the
   denominator is doubly bounded (disclosed-only + a selection-biased corpus) (C5). This
   is a *lead*, not a measured consolidation rate.

**Builder-lens verdict:** `parent`/`owns` is the clean joinable relation *in shape*, but
in *practice* it behaves exactly like MRL-006's backend-pharmacy finding — **the join
fails because the counterpart entity isn't captured**, now generalized from prose
partners to the corporate-ownership frontmatter axis. `query-time-grouping-enough` holds
for a *string-grouped map* (group children by their parent value); it does **not** hold
for *traversal* (click a parent, see its portfolio) and it does **not** support a
consolidation *claim*. No new primitive is needed; what's missing is **capture coverage
of the parent/sibling entities**, not a relation table.

## Gap Map

| Sub-question | Store answer | Grade |
|---|---|---|
| Which brands disclose a parent/owner? | Clean — 13 `parent` + 15 `owns`, with provenance comments | **answered** |
| Can I traverse parent → its captured portfolio? | No — only lifemd→rexmd resolves both ways; 3/21 targets captured | **gap (coverage)** |
| How concentrated is ownership in this market? | Cannot say — disclosed-only floor over a selection-biased corpus; 4 multi-child clusters are all uncaptured/inferred | **gap (denominator)** |
| Is a `parent: []` brand actually independent? | Usually unknowable — 103/109 empties are bare, no independent-vs-not-stated marker | **gap (absence discipline)** |
| Do parent and owns edges reconcile? | Rarely testable (need both captured); where testable, 1 reconciles (lifemd/rexmd), 1 does not (qualtrics/delighted) | **partial** |

**What would change the answer:** capturing the parent/sibling entities (Thirty Madison,
Niagen Bioscience, the LifeMD sibling brands, etc.) would convert dangling edges into
traversable portfolios and let a real intra-corpus consolidation rate be computed.

## Evidence Used

All claims are store-only and derived from local frontmatter; see
`receipts/ownership-edge-map-2026-06-20.md` (claims C1–C8). No external/current/pricing
claims in this read, so no URL/capture-date evidence applies.

## Companies Seen

- **Disclosed `parent`:** aws-amazon, onemedical, keeps, nurx, niagenplus, truniagen,
  cartier, alange-soehne, rexmd, delighted, hims, openai, redantler.
- **Disclosed `owns`:** alpha-sense, casio, eden-health, etsy, euclidpower, ford,
  functionhealth, lifemd, marekhealth, nike, qualtrics, tryshed, twilio, uber, upwork.
- **Both endpoints captured:** lifemd↔rexmd (reconciled); qualtrics←delighted (unreciprocated).

## Missing / Stale Coverage

The dangling edges are a concrete, propose-don't-write capture-candidate list (MRL-009
shape) — capturing any of these converts a dangling pointer into a joinable portfolio:
**Thirty Madison** (parent of keeps + nurx, plus named siblings Cove/Facet),
**Niagen Bioscience** (parent of niagenplus + truniagen), and the **LifeMD siblings**
shapiromd.com / navamd.com (named in lifemd `owns`, uncaptured). General-brand siblings
(reverb, depop, ezra, sendgrid, segment, fordpro, ubereats, converse) are lower priority —
their ownership is well-known public fact and they're outside the telehealth focus.
**Not autonomous-safe** (Firecrawl spend → human approval); surfaced as informational.

## Source Gaps

None external. The binding gap is **internal capture coverage of parent/sibling
entities**, not a missing source family — the ownership facts are already disclosed on the
captured children's own pages; their counterparties just aren't in the store. A
secondary gap: the `parent: []` convention has an *independent-vs-not-stated* distinction
(used in 6 commented empties) that is applied to <6% of empties, so absence is not
self-describing at the field level.

## Raw Learning to Preserve

See `run-notes.md` Discovery ledger IDs O1–O4, G1–G2, W1, S1, F1 for Loop 2 to append to
`discovery-ledger.md`.

## External Completeness Check

Not run (store-only by contract). Completeness is explicitly *not* claimed — the map is a
disclosed-only floor over a selection-biased corpus; an external denominator (e.g. SEC
subsidiary filings or a M&A database) would be needed to state a true consolidation rate,
which is out of scope and out of budget here.

## Market Pattern

1. **The clean-relation axis dangles for the same reason the prose axis does.** MRL-006
   found pharmacy/clinical partners dangle because targets aren't captured; ownership is
   the *cleanest* relation in the schema (structured frontmatter, often explicit
   attestation) and it **still** dangles 18-of-21 times. The bottleneck across every
   relation read is **counterpart capture coverage**, not relation representation.
2. **The richest ownership facts ride in on general public companies.** Amazon, Etsy,
   Nike, Uber, Twilio, Ford, Casio carry the most confident `owns:` edges — but they're
   ad-hoc corpus members whose siblings were never captured, so the cleanest data is also
   the most orphaned.
3. **Absence is not self-describing.** 103/109 `parent: []` are bare. A naive
   consolidation read would treat every empty as "independent" and badly overstate the
   independent share; the honest reading is "undisclosed-or-uncaptured" for ~95% of them.

## What Would Change This Answer

- Capturing Thirty Madison + Niagen Bioscience + the LifeMD siblings would create the
  first *traversable* multi-brand portfolios and let an intra-corpus consolidation rate
  be computed honestly.
- A convention that backfilled the independent-vs-not-stated comment on bare `parent: []`
  would make absence legible (turning 103 silent empties into a real signal).
- An external ownership denominator would be required before any *market* consolidation
  claim — not just an intra-store one.
