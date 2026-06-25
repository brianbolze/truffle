# Market Read

## Question

For an investor/partner sizing up the captured **pre-revenue deep-tech cohort**
(electra-aero, verdegoaero, blueenergy, cfs-energy, evoloh, sorafuel, beta-team;
euclidpower as a commercial foil), can Truffle's captured State support a "**who has
momentum / is gaining ground**" triage — capital raised, milestone cadence,
hiring/partnership motion — or is traction a Signals/time-axis, comparative fact the static
profiles structurally cannot carry?

Mode: **gap-probe**. Evidence: **store-only** (8 profiles, all captured 2026-06-14, single
capture each). Builder lens: the traction frame's deferred **cohort roll-up (#4)** and the
**State-vs-Signals** boundary.

## Result

**Lead (gap-probe):** Truffle's static State supports **level** rankings of this cohort —
a *capital-size* ordering and a *stage* ordering — but **not** a **momentum** ("who's
gaining ground") triage. Momentum is a *delta over time*; the store holds only *levels at
one capture*. Note the two level axes are only loosely correlated and partly independent:
the *stage* ordering does re-derive run-042's maturity read, but *capital size* does **not**
— **cfs-energy raised the most ($2B) while sitting near the bottom on maturity** (zero
power, pre-demonstration). So static State carries more than one level axis, yet **none**
carries a delta. The blocking gap is not capture (the levels are present and capturable) —
it is **comparability** (frame #2) and a **durable time-series home** (frame #3), neither of
which exists for this cohort. `0/8` profiles have any `signals/` capture (C1). "No new
primitive needed *now*" stays live; the run's payload is a roadmap finding.

### (1) What State CAN carry — a level snapshot per company (C2)

Each profile carries a static, self-reported **level** read on capital, orders, and
milestones. Assembled (all figures self-reported on the company's own site unless noted):

| Company | Capital (self-reported) | Most-recent dated event | Demand / order signal | Stage anchor |
|---|---|---|---|---|
| **beta-team** | **2025 IPO raised >$1B**, NYSE ticker `BETA`; Q1 2026 10-Q (auditable) | IPO 2025; 10-Q Q1 2026 | ">800 aircraft backlog"; UL-listed Charge Cubes **sold** | Early-commercial (shipping non-flagship lines) |
| **cfs-energy** | "over **$2 billion** in capital" (cumulative, **undated**) | Google/Eni offtakes (undated on captured pages) | Google 200 MW offtake; Eni >$1B offtake; Dominion lease | Pre-revenue, demonstration (SPARC→ARC) |
| **electra-aero** | **$115M Series B** (Apr 2025); USAF SFP up to $85M (Jan 2023) | Series B Apr 2025; FAA Part-23 application Dec 2025 | "2,200 pre-orders", pipeline "~$9B", ">60 operators" | Pre-revenue; EL2 first flew Nov 2023 |
| **blueenergy-co** | **$380M financing** (Apr 21 2026) | $380M Apr 2026; GE Vernova 2.5 GW May 2026 | GE Vernova 2.5 GW collaboration; NRC milestone | Pre-construction |
| **evoloh-com** | "over **$40 million**" (cited Dec 2024) | 0.5 GW supply agreement Dec 2024; brochure Sept 2025 | "500MW binding orders"; "16 GW signed intent" | Pre-revenue; 3M pilot operational 2027 |
| **sorafuel-com** | **$14.6M round** (Apr 8 2026) | Round Apr 2026 | FEG offtake LoI, "first 10M gallons" (future) | Earliest; pilot in "18–24 months" |
| **verdegoaero-com** | **No $ figure** — investor logos only (RTX Ventures, DiamondStream, Florida Opportunity Fund…) | AFWERX contracts "since 2022"; USAF work "since 2024" | "Inquire for ordering" — no order figure | Pre-revenue; founded 2017 |
| *euclidpower-com (foil)* | No $ figure — investor logos (Spero, Toba…) | Thresh Power acquisition Apr 30 2026 | 22–26 GW supported (conflicting); customer case studies | **Commercial / operating** (the foil) |

A reader can rank **capital**: beta-team ($1B+ IPO) > cfs ($2B cumulative — note this
out-ranks beta on cumulative capital) > blue ($380M) > electra ($115M) > evoloh ($40M) >
sorafuel ($14.6M); verdego cannot be placed at all (logos, no figure). And a reader can rank
**stage** (≈ run-042 maturity): beta-team (shipping non-flagship lines) > electra (first
flight, cert application) > blue (pre-construction) ≈ evoloh (pilot 2027) > cfs / sorafuel
(pre-demonstration). **The two orderings disagree** — cfs is #1–2 on capital but bottom on
stage — which is itself the tell that capital-raised is not a maturity proxy. Neither is a
*momentum* read.

### (2) What State CANNOT carry — the momentum/Signals axis (the gap)

Four distinct reasons the level table above is **not** a momentum read:

- **Level ≠ delta (the frame's #1 grain trap).** Every figure is a *cumulative or
  point-in-time level* captured **once** (all `captured_at: 2026-06-14`). "Is the pipeline
  growing? Is fundraising accelerating? Is hiring up?" is structurally unanswerable — there
  is no second capture to diff. You can rank *size*, never *velocity*.
- **No Signals substrate (C1).** `0/8` of the cohort has any `store/<domain>/signals/`
  capture. The append-only `signals/` layer + `signal_delta.py` — the engine's actual
  comparability machinery — were never run on deep-tech (telehealth-only to date). The
  time-axis home the traction frame (#3) requires does not exist here.
- **Units don't commensurate (cousin of run-023/043/044 incomparability).** Capital is
  cumulative (cfs $2B) vs single-round (sora $14.6M, blue $380M) vs absent (verdego, euclid).
  Demand is pre-orders (electra 2,200) vs backlog (beta 800) vs binding orders (evoloh
  500MW) vs signed intent (evoloh 16GW) vs offtake LoI (sora). No common momentum unit
  exists to sort on.
- **The capture clock can't date the traction event (cousin of run-047 CR2).** Recent events
  (blue $380M Apr 2026, sora $14.6M Apr 2026) and stale ones (electra Series B Apr 2025, cfs
  $2B undated) all sit under the *same* `captured_at: 2026-06-14`. Event recency lives only
  in prose milestone blocks, never a structured field — so "what moved lately" requires
  per-profile prose reading, not a query.

### (3) Positive surprise — the cheap traction floor exists but was never captured

**beta-team is the lone cohort member with a genuine, first-party, auditable traction
anchor**: an NYSE ticker (`BETA`), a 2025 IPO size (>$1B), and a Q1 2026 10-Q linked from
its investor page (C2). This is exactly the "capture easy, first-party, obvious signal"
(ticker, big round, public filing) the traction frame says to grab cheaply and refuse the
paid-data swamp for. Yet **even beta-team has no `signals/` capture**. So the gap for this
cohort is **not discoverability** — the cheapest, most reliable signal in the whole set is
sitting in plain view — it is that the cheap-capture traction floor the frame describes was
simply never run here.

## Gap Map

| Sub-question | Store result | What would change it |
|---|---|---|
| Rank cohort by **size/stage** | **Answered** from static State (C2) — but duplicates run-042's maturity ranking | — |
| Rank cohort by **momentum / who's gaining** | **Not answerable** — levels only, no deltas, `0/8` signals (C1) | A 2nd dated capture + `signal_delta.py` run per company (frame #2/#3) |
| Tell **what moved lately** per company | **Prose-only** — event dates in milestone blocks, not structured; `captured_at` is uniform | A structured event/Signal layer with its own clock |
| Compare capital **across** the cohort | **Defeated by units** — cumulative vs single-round vs absent | A normalized round-history (which would launder false precision; engine-dev "evidence not scores" cautions against it) |
| Trust the traction claims as **real** | **Self-reported, single-source** for 7/8; only beta-team is auditable (10-Q) — and that isn't captured as a Signal | Independent panel (SEC/news/IR) — off the captured marketing surface |

## Evidence Used

Store-only; all profiles `store/<domain>/profile.md`, `captured_at: 2026-06-14`. Receipts:

- **C1** — `0/8` cohort profiles have a `signals/` capture (receipt `receipts/C1-signals-absence.md`).
- **C2** — per-company capital / round / milestone level table, derived from the 8 profiles
  (receipt `receipts/C2-traction-level-table.md`).

Key prose anchors (file:line): electra Series B + USAF + pipeline `electra-aero/profile.md:97-100`;
cfs "$2B" `cfs-energy/profile.md:61,109`; blue "$380M" `blueenergy-co/profile.md:97`;
evoloh "$40M" + orders `evoloh-com/profile.md:98`; sora "$14.6M" `sorafuel-com/profile.md:96`;
verdego investor logos (no $) `verdegoaero-com/profile.md:111`; beta IPO/ticker/10-Q
`beta-team/profile.md:123`; euclid (foil) `euclidpower-com/profile.md:100-101`.

## Companies Seen

8 deep-tech profiles (run-042 cohort): electra-aero, verdegoaero-com, blueenergy-co,
cfs-energy, evoloh-com, sorafuel-com, beta-team, + euclidpower-com (commercial foil).
Membership is the **named-8**, not a `primary_industry` grep — run-042 G3 established that
an industry draw scatters this entity-shape cohort across Automotive/Manufacturing/Energy
and pulls in commercial firms (euclidpower itself). Treated as a partial, hand-built set.

## Missing / Stale Coverage

- `0/8` have `signals/` captures (C1) — no time-axis substrate.
- All single-capture, all `2026-06-14` — no diffable second point for any company.
- cfs "$2B" and several offtake/partner claims are **undated** on captured pages — even the
  level read has gaps.

## Source Gaps

- **The `signals/` append layer was never run on this cohort.** For beta-team the cheap
  first-party signal (SEC 10-Q via ticker `BETA`) is directly capturable; for the 7 private
  firms, dated funding-announcement / news capture would be the panel — both off the static
  marketing profile, spend/approval-gated. This is the same "decision-grade lives off the
  captured surface" boundary as run-036 G2 / 037 / 038 G2 / 042 G4, now on the **traction**
  axis.
- A **neutral** momentum denominator (who's actually winning deep-tech) would need news/IR +
  filings, not the companies' own self-reported milestone blocks (L004 / L002 shape).

## Raw Learning to Preserve

See `run-notes.md` Observations: **G1** (level≠delta, momentum unanswerable), **G2** (0/8
signals — comparability/durable-home is the missing piece, not capture), **S1** (beta-team
cheap auditable anchor exists yet uncaptured), **S2** (size/stage ranking duplicates
run-042 maturity — traction-from-State collapses onto maturity), **G3** (unit
incommensurability defeats cross-cohort capital compare), **S3** (capture clock can't date
the traction event; recency is prose-only), **W1** (lightest path if anything graduates).

## External Completeness Check

Not run — store-only by contract. The named-8 membership is hand-built and partial by
design (run-042 G3); no outside denominator was consulted, so no completeness claim is made
about "all pre-revenue deep-tech," only about what these 8 captured profiles can and cannot
carry.

## Market Pattern

Across this cohort, static State supports **level** orderings but no **delta**. The *stage*
ordering re-derives run-042's maturity read; the *capital* ordering is a partly independent
level axis (cfs raised the most yet ranks bottom on stage), so "traction" does not cleanly
collapse onto "maturity" — there are at least two loosely-correlated level axes, neither of
which moves. The thing that makes traction its *own* axis — movement, velocity, "gaining
ground" — is precisely the time-axis/comparative layer the engine flags first-class-future
and has not built. The cohort also splits cleanly on *signal auditability*: 1 public filer
(beta-team, auditable) vs 7 self-reported-only — and even the auditable one isn't captured
as a Signal.

## What Would Change This Answer

- A **second dated capture** + a `signal_delta.py` run for any cohort member would turn a
  level into a delta and make at least a crude per-company momentum read possible — the
  cleanest test of frame #2 (comparability). beta-team (public, SEC-anchored) is the
  natural first probe.
- A **real cohort-momentum consumer** (an investor wanting "who's hottest in deep-tech this
  quarter") plus the comparability machinery would be the pair that justifies the traction
  roll-up (#4); neither exists today, so **"no new primitive needed now" stays live**.
- If anything graduates, the lightest path is a **query-time recipe + the cheap first-party
  capture** (ticker/10-Q for public filers; dated funding-news for private), **not** a
  normalized traction-magnitude field — which unit-incommensurability would turn into
  laundered false precision (engine-dev "evidence, not scores"). Mirrors the 036–047
  anti-sprawl W1 landings.
