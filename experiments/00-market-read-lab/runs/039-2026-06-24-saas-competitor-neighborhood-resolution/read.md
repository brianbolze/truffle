# Market Read

## Question

For the captured Technology/SaaS slice (~22 companies nearly all tagged
`offering_category: [Software / SaaS]`), can the store draw a competitor/substitute
**neighborhood** — who competes with whom — from existing State alone, given there is no
competitor relation field and the category enum collapses distinct sub-markets into one
bucket? Where does neighborhood-drawing fall to prose / LLM judgment, and what relation or
sub-category evidence is missing?

This is a **gap-probe** (with a calibration flavor): the point is to map where Truffle can
and cannot support a competitor-neighborhood read, not to certify a market map.

## Result

**Headline: the store can reconstruct the SaaS neighborhood, but not from its structured
fields — and the reconstruction is mine, not the store's.** Three layers, in descending
trust:

**(1) Structured fields cannot resolve the neighborhood — L005 failure-side confirmed.**
Of the 23 captured profiles that `grep "primary_industry: Technology"` returns, ~19 carry
`offering_category: [Software / SaaS]` — a single bucket. `target_market` is almost
uniformly `[B2B]` (a few `[B2B, B2C]`). `business_model` is mostly `Subscription`. None of
these three structured cuts separates a revenue-intelligence tool (Gong) from an
observability platform (Datadog) from a survey tool (Typeform). **The corpus does not carry
the sub-market cut in any structured field** — the inverse of every prior L005 confirmation,
where a clean enum already encoded the cut. Grouping by `offering_category` here yields one
undifferentiated pile.

**(2) `description` prose carries enough for *me* to reconstruct ~7 sub-markets — but that
is LLM judgment, not store State.** Reading the one-line `description` of each profile, the
slice resolves cleanly into:

| Sub-market | Captured members | Store-internal adjacency? |
|---|---|---|
| Revenue / sales intelligence | Gong, Clari | **Yes — prose-confirmed edge** (gong:60 "competes with Clari") |
| Observability / product-dev analytics | Datadog, PostHog (+ Cloudflare infra-adjacent) | Adjacent; named rivals are off-store |
| Research / survey / feedback / UX | Qualtrics, Typeform, Delighted, Dovetail, Usertesting, Listenlabs | **Yes — densest cluster, multiple internal adjacencies** |
| No-code workspace / docs | Notion, Airtable, Coda | Adjacent (mutually substitutable for a buyer) |
| AI productivity / notes / assistant | Granola, Superhuman, Notion (overlap), OpenAI | Loose; overlapping jobs |
| Cloud / infra / data platforms | AWS, Snowflake, Cloudflare, Twilio | Same layer, different jobs |
| Market / brand intelligence | AlphaSense, Waldo | Adjacent, different buyers |

The neighborhood is **real and legible**, but it lives in my reading of free-text
descriptions. The store did not hand me a cluster; I inferred one. That distinction is the
whole point of the gap-probe (see `loop1_failure_mode`).

**(3) The store *does* carry explicit competitor edges — in prose, unevenly, and mostly
pointing off-store.** A minority of profiles name a competitor set verbatim in their body:

- **datadoghq.com:73-74** — clean competitor *list*: "Competes with: New Relic, Dynatrace, Splunk, Grafana, Elastic."
- **gong.io:59-60** — module-line grain: "competes with Salesloft/Outreach" / "competes with Clari." (Clari is the only one captured.)
- **dovetail.com:85** — "comparison pages vs. Condens, Looppanel, and Marvin (the research-repository competitive set)."
- **listenlabs.ai:121** — "legacy panels (Qualtrics, UserTesting) and the new AI-native cohort (Outset, Remesh, Strella, Conveo)."
- **clari.com:80** — names the category fight ("vs. combining three technology solutions"), not specific rivals.

This is heterogeneous: a clean list (Datadog), per-product edges (Gong), comparison-page
sets (Dovetail), or only a category posture (Clari). And **the named competitors are mostly
NOT in the store** — New Relic, Dynatrace, Salesloft, Outreach, Condens, Looppanel, Outset,
Remesh have no captured profile. So even where the store names the neighborhood, the edges
dangle outside the captured slice.

**Vertical relations are the part the store handles structurally — and even those have a
consistency gap.** `parent`/`owns` is the one real relation primitive, and it is rich on
this slice (Qualtrics owns Delighted; Twilio owns SendGrid + Segment; AlphaSense owns
Tegus/Sentieo/BamSEC/Canalyst; AWS parent Amazon; Upwork owns Lifted). But the
Grammarly→Coda→Superhuman chain is recorded **inconsistently across three profiles**:
`coda.io` has `parent: [grammarly.com]`, while `superhuman.com` has `owns: [coda.io]` and is
itself "Grammarly rebranded." A reader asking "who owns Coda" gets `grammarly.com` from one
profile and `superhuman.com` from another — both STRAIN-flagged, but not reconciled.

**Verdict on the design question: no new primitive needed *yet*, but the failure mode is
now mapped.** Competitor neighborhood is a **horizontal** relation the store has no field
for; `parent`/`owns` is purely **vertical** (ownership). The horizontal neighborhood is
carried (a) implicitly by `description` prose, recoverable by LLM reading, and (b) explicitly
by competitor-naming body lines in a minority of profiles. A durable competitor/sub-category
field would be mostly **empty or dangling** today (most edges point off-store), so it fails
the "every field is a cut you can fill reliably" bar. The lightest path, *if* a cross-company
neighborhood consumer appears, is a query-time recipe — "read `description` + grep competitor
lines" — not a field.

## Gap Map

| Capability | Store result | Evidence |
|---|---|---|
| Resolve sub-markets from a **structured** field | **Fails** — `offering_category`/`target_market`/`business_model` collapse ~7 sub-markets into one `Software / SaaS` × `B2B` × `Subscription` pile | Frontmatter grep, §Result(1) |
| Reconstruct sub-markets from **description prose** | **Works, but as LLM judgment** — clean 7-cluster read, not store State | descriptions, §Result(2) |
| Surface **explicit competitor edges** | **Partial / uneven** — named verbatim in ~5/23 bodies, heterogeneous grain, mostly off-store targets | datadog:74, gong:59-60, dovetail:85, listenlabs:121 |
| Map **vertical (ownership)** relations | **Works structurally** — `parent`/`owns` rich on this slice | frontmatter |
| Keep an **M&A chain consistent** across profiles | **Gap** — Coda owned by grammarly.com (per coda) vs superhuman.com (per superhuman) | coda.io parent; superhuman.com owns |
| Treat captured slice as the **market** | **Must not** — named rivals (New Relic, Salesloft, Condens…) are uncaptured; slice is partial | §Result(3) |

For a `gap-probe`, this map *is* the main result: the store's competitor-neighborhood
support is prose-grade and inference-dependent on the horizontal axis, structured only on
the vertical axis.

## Evidence Used

All evidence is local store State (`evidence_mode: store-only`); no external or current
claims, so no dated-URL receipts are required. The one derived artifact — the sub-market
clustering and the captured-vs-named competitor set — is receipted in
`receipts/01-tech-slice-neighborhood.md` (claims C1–C5).

- **C1** — ~19/23 Technology profiles carry `offering_category: [Software / SaaS]`; structured fields do not separate sub-markets. (frontmatter grep)
- **C2** — The slice resolves into ~7 description-legible sub-markets (clustering is LLM judgment). (descriptions)
- **C3** — Explicit competitor edges appear verbatim in a minority of bodies, heterogeneous grain. (datadog:74, gong:59-60, dovetail:85, listenlabs:121)
- **C4** — Most named competitors are not captured (off-store dangling edges). (cross-check vs `ls store/`)
- **C5** — The Grammarly/Coda/Superhuman ownership chain is recorded inconsistently across coda.io and superhuman.com. (parent/owns frontmatter)

## Companies Seen

23 profiles returned by `grep "primary_industry: Technology"`. **Denominator hygiene note:**
four are not SaaS — `apple.com` and `casio.com` (hardware), `eightsleep.com` (smart
hardware), `upwork.com` (marketplace, `offering_category: [Marketplace / Platform]`). They
surface in the industry grep but are not part of the SaaS neighborhood; a naive
industry-draw silently pulls them in. The ~19 genuine SaaS profiles are the working set.
This captured set is a **partial, capture-biased** slice of the SaaS market, not the
universe — say "not found in the captured slice," never "no such competitor."

## Missing / Stale Coverage

- The **named-but-uncaptured competitors** (New Relic, Dynatrace, Splunk, Grafana, Elastic,
  Salesloft, Outreach, Condens, Looppanel, Marvin, Outset, Remesh, Strella, Conveo) are the
  concrete coverage gaps a real neighborhood read would need filled.
- Capture clocks on this slice are mostly 2026-06-17; not stale for a structural read, but a
  competitor-positioning read is freshness-sensitive (the AI repositioning Gong/Notion/Linear
  describe is live and rotating).

## Source Gaps

- **No horizontal relation field.** The store has `parent`/`owns` (vertical) but nothing for
  competes-with / substitute-for / same-sub-market. This is the structural absence the probe
  set out to test.
- **No sub-category under `offering_category`.** `[Software / SaaS]` is a leaf for ~19
  companies; there is no second-level cut (sales-intel / observability / survey / no-code)
  that would let a query separate sub-markets without prose reading.
- **Competitor prose is an inconsistent second channel.** Where it exists it is decision-grade
  and verbatim; but it is present in only ~5/23 bodies and at three different grains (list /
  per-product / comparison-page set), so a reader cannot rely on it to find every edge —
  analogous to run-037 DR2 (STRAIN as an unreliable second channel).

## Raw Learning to Preserve

See `run-notes.md` Observations: **S1** (vertical relation rich, horizontal absent —
the axis split), **G1** (structured fields cannot resolve sub-markets; L005 failure-side),
**G2** (competitor neighborhood lives in prose, uneven grain, mostly off-store),
**G3** (M&A-chain consistency gap across profiles), **S2** (industry-draw denominator
pulls in 4 non-SaaS entities), **W1** (lightest path is a query-recipe, not a field).

## External Completeness Check

Not run — `store-only`, and an external denominator would breach the contract. The read
explicitly flags the captured slice as partial rather than reconciling it against an outside
SaaS list. Per L004, the reconciliation that is *not* available travels with the read: the
named-but-uncaptured competitor list above is the honest statement of what an external check
would add.

## Market Pattern

Within the captured slice, the clearest **store-internal** competitive edges are:
**Gong ↔ Clari** (revenue intelligence — prose-confirmed) and the **research/survey
cluster** (Qualtrics / Typeform / Delighted / Dovetail / Usertesting / Listenlabs — six
captured tools in one consideration set, with Listenlabs' own page naming Qualtrics +
UserTesting as the incumbents it attacks). The no-code-workspace trio (Notion / Airtable /
Coda) is a buyer-substitutable set, complicated by Coda now sitting inside Grammarly/
Superhuman. Everything else (AWS, Snowflake, Cloudflare, Twilio, OpenAI, AlphaSense, Waldo)
is same-layer-different-job: adjacent infrastructure or intelligence, not head-to-head.

## What Would Change This Answer

- A **second slice** showing the same axis split (structured vertical relations rich,
  horizontal neighborhood prose-only) would move S1/G2 from singleton toward pattern.
- A **real cross-company neighborhood consumer** (a downstream system or strategist who
  needs to *filter* by sub-market, not just read one) would change the W1 calculus toward a
  sub-category cut or a query recipe — but only if the named edges were mostly in-store, which
  they are not today.
- **Capturing even 3-4 of the named rivals** (e.g. New Relic, Salesloft, Condens) would turn
  several dangling prose edges into in-store edges and make a competitor field fillable —
  the condition under which "no new primitive needed" would stop being the honest answer.
