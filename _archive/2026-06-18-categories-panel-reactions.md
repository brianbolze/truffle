# Panel reactions: cohorts and categories

Date: 2026-06-18 - Status: panel synthesis, **input to a frame — not a frame**.

> **Purpose.** Pressure-test the [wallow](2026-06-18-wallow.md) from six angles to get what Brian actually needs before scoping: **clarity of use cases and their relative priorities** — what must be figured out *now* vs *later*. Sister to the wallow; feeds the frame that should come next.
>
> **How this was made.** A six-angle panel reacted *independently* to the wallow (no cross-contamination, so disagreement would surface), then an Opus synthesis pass merged them. Panelists are our [personas](../../documentation/personas.md): **Strat** (the Strategist / Scott Witt), **Pantry** (Teleprescribe downstream), **Beek** (Beekeeper-Brian), **Founder** (anti-Doro arbiter), **Steward** (corpus health), **TH** (a Telehealth market analyst — the live pain). This is a lens, not a verdict.

## The 30-second read

**Ship typed, dated, evidence-cited *relations* on company records. That's the one thing this whole space earns right now.** Everything else stays a query-time grouping or a dated source capture until a repeat consumer — and a depth audit — proves it deserves more. No category entity. No `cohorts/` folder yet, maybe ever.

The panel was **near-unanimous** (5–6 of 6) on the leans. Real friction sits in only three places, and one of them is settle-by-experiment, not argument:

1. **Is query-time grouping trustworthy over today's store, or does it confidently lie over thin data?** → *Run the probe before you write the frame.*
2. **What does membership persist as** — nothing, a dated doc, or a re-diffable object?
3. **When do SERP/listicle source captures ship** — now (the live pain says yes) or earned later?

## Use-case catalog, prioritized

The deduplicated cross-panel view. **Persists-as** uses the wallow's ladder: *query-time* (don't store) · *source-capture* · *relation* · *entity* · *project-judgment* · *contested*.

| Use case | Job | Pushed by | Priority | Persists as | Decide first |
|---|---|---|---|---|---|
| **Jump from a brief to named neighbors** (Hims → Ro, LifeMD, Keeps) | navigate | **all 6** | **now** | relation | Min record shape + which type ships first |
| **One-off market Q via named, cited grouping** ("who sells med weight loss now") | pattern | Strat, Pantry, Beek, Founder, Steward | **now** | query-time | Can `/query-companies` fan out + merge a field? Caveat coverage. |
| **Field-coverage audit before any synthesis** (is the cohort pack filled enough to aggregate?) | gate | Beek, Strat, Founder, TH | **now** | query-time | Run it concretely (see probe below) |
| **Category SERP / listicle capture** (defines market set, surfaces who's missing, freshness anchor) | source-panel | all (priority **contested**) | soon · *TH: now* | source-capture | **Where it lands → does `cohorts/` need to exist?** |
| **Membership audit** (in / candidate / out, dated, sourced) | membership | Steward, Strat, Pantry, Founder | soon | **contested** | Is the boundary nameable + stable enough to write down? |
| **Cross-company convergence read** (what's table-stakes vs differentiating) | pattern | Strat, TH, Beek, Founder | later¹ | query-time | Gated on the depth audit passing |
| **New-entrant / membership-drift detection** | watch-change | Pantry, Steward, Beek, TH | later | **contested** | Does signals' capture→delta extend to membership? |
| **Per-company change pulse** (price/molecule/intake move) | watch-change | Strat, TH, Pantry | later | source-capture | *Already signals/delta — scope OUT of this frame* |
| **Named non-company events** (FDA compounding rule, DEA extension) | watch-change | TH, Founder | later | **contested** | Does a clean name alone earn an entity? (No — defer) |
| **Differentiation read** (is this company actually differentiated?) | differentiate | Strat | later | project-judgment | Engine supplies receipts; brief owns the verdict |

¹ *Convergence flips to **now** the moment the depth audit passes — it's gated on data, not on design.*

## Where the panel agreed (cheap, safe locks)

- **Two jobs, not one** (L1) — watching *change* and defining *membership* have different staleness, evidence bars, even integrity models. Sharpened: *different data sources*, not just different frames (change = per-company signals + relations; membership = SERP/listicle panels).
- **Persist the smallest durable object** (L2) — the Signals precedent is the template. Steward's sharpening: *date + evidence-type are mandatory, not optional* — a source capture without a freshness handle rots exactly like a premature entity.
- **Relations are the one thing to ship now** (L4) — company-keyed (no new key), visible in the brief immediately, the Pantry's only concrete near-term need, possibly *sufficient to replace most of the category layer*. Universal rider: **do not collapse relation types**; evidence-type is mandatory so an Exa-neighbor never reads as a listicle-attested rival.
- **Judgments stay project-side** (L5) — dominant / hot / threat / worth-entering / differentiated. Engine supplies receipts; the brief makes the call. Uncontested.
- **Anti-Doro, sharpened to posture** (L6) — the trap isn't only the machinery; it's *the moment you start arguing whether "GLP-1 telehealth" and "medical weight loss" are the same category.* That argument **is** the ontology project. Use the label as a dated, sourced query term.
- **Coverage caveating** — every grouping must stamp "N of M known companies, per [source]" so false completeness can't masquerade as authority.

## Live tensions (what the frame exists to decide)

**T1 — Is query-time grouping the pressure valve, or confident-wrong over thin inputs?**
*Strat / Founder / Beek:* it's the right default, answers ~80% with no stored entity. · *TH (dissent):* over 8 GLP-1 profiles it misses the 3 not captured, has stale pricing, no consistent schema — *worse than nothing*; capture SERPs + relations + depth first. · *Pantry / Steward:* "depends" — fine for one-off human analysis, useless for write-back/re-diff, and silently omits the uncaptured.
→ **Settle empirically:** run the probe (below). If it returns 3 of 9, capture moves up and this is a Coverage bet; if coverage is solid, L3 holds and it's an Access bet. Either way, mandatory coverage-caveats are the cheap bridge.

**T2 — What does membership persist as?**
*Founder / Strat:* a *document*, not an entity — markdown with in/candidate/out + an as-of date is 80% of the value; schema+lint is premature (maybe Beek's editorial call, not the engine's). · *Steward / Pantry:* if it persists at all it must be dated + re-diffable or it silently rots; "category member" may itself be a judgment that stays project-side.
→ Apply the wallow's two gates *per cohort*: nameable-without-spiralling **and** stays-true-long-enough. Founder's cut: "medical weight loss" (~12 captured) passes; "DTC telehealth" fails. Start the one that passes as a dated doc; derive the rest from relations + query-time grouping.

**T3 — SERP/listicle capture: now or earned later?**
*TH:* **now** — a dated ranked-domain snapshot for 3–5 defining queries *is* the smallest durable membership object; everything builds on it. · *Founder / Strat / Beek:* earnable — hand-curate once first; don't build discovery infra to solve a depth problem. · *Steward:* soon, but only with date + TTL + re-diff path.
→ Decide the landing location first (it's the real fork — see below); let the audit break the tie.

**T4 — Does a named non-company event (FDA rule, DEA extension) earn a durable artifact?**
*TH:* live gap today — clean keys, affects the whole cohort, nowhere to put it. · *Founder/wallow:* a clean name alone doesn't earn an entity; capture as dated signal, graduate on repeat demand.
→ **Deliberately leave open in the frame.** This is the cleanest test of the wallow's core claim: *name-ability and staleness are two separate gates.* Capture now as a signal; define the graduation *trigger*, not the entity.

**T5 — What's the freshness contract for a relation?**
*Pantry / Steward:* unresolved and *blocking* — a relation from a listicle that later drops Ro creates silent drift in the Organizations DB; a relation without a freshness handle is worse than none. · *wallow/Founder:* "persist when useful"; signals' append→delta *probably* extends to it.
→ Lock the record shape (with mandatory `captured_at`, `evidence_url`, `evidence_type`, `confidence`) **now**; settle the re-diff contract as the *immediate next step*, before any write-back.

## Scoping cut

**Now (before writing the frame)**
- Lock the **typed relation record**: `source_domain, target_domain, relation_type, evidence_url, evidence_type, captured_at, confidence` — all mandatory, machine-readable, append-diffable, company-keyed. Ship **source-attested competitor/substitute** as the first (and, I'd argue, *only*) type.
- Run the **coverage/completeness audit** on the telehealth cohort pack — resolves T1 empirically.
- Make **query-time grouping** a first-class `/query-companies` verb with **mandatory** coverage caveats. Don't store results.
- Decide the one structural fork: **do dated SERP/listicle captures land under `store/<domain>/signals/` or `cohorts/<slug>/signals/`** — i.e., does `cohorts/` need to exist yet at all?
- Re-affirm: all judgments stay project-side; the engine emits receipts only.

**Later**
- Relation **freshness / re-diff contract** (TTL, supersede-vs-stale) — required before any Pantry write-back, immediately after the record shape.
- **SERP/listicle capture tooling** — priority floats on the audit (now if the store is provably missing real players; earned otherwise).
- **Membership as a dated doc** for the one cohort that passes both gates; derive the rest.
- **Convergence/pattern extraction** as a synthesis prompt — gated on the depth audit.
- **New-entrant/drift detection**, extending signals' delta once the write contract is stable.
- **Named non-company events** as dated source captures with a defined graduation trigger.

**Never**
- A universal category ontology / canonical hierarchy ("DTC telehealth > GLP-1 telehealth > compound GLP-1").
- A durable category **entity** with a `profile.md`-equivalent minted just because a signal exists.
- Embedding-led entity resolution / datapoint reconciliation as the default (the swamp domain-as-key deleted).
- A generic market/dominance score or blended cohort metric in shared State.
- A fully automated category-discovery / store-expansion system.
- Owning broad-topic market news.
- Resolving where "men's health" ends and "longevity" begins as a precondition to anything.

## Questions the frame must answer

1. **Relation record + freshness:** the minimal typed shape, which type ships first, and what makes evidence-type and freshness *mandatory* — so the one thing we agree to ship now can't become a silent-rot vector for write-backs.
2. **Is query-time grouping trustworthy today?** Run the audit + the "compound semaglutide" probe. 3 of 9 → Depth-on-captured or Coverage-via-capture? (Resolves T1 by evidence, not argument.)
3. **Where do source captures land** — per-company signals or `cohorts/<slug>/signals/` — and **does `cohorts/` need to exist at all yet?**
4. **What test must a cohort pass to persist as membership, and at what fidelity** (none / dated doc / re-diffable object)? Show a concrete cohort that passes both gates and one that fails.
5. **Engine-generic vs project-owned:** which parts are shared (relations, source captures, the query verb) vs project (membership judgment, differentiation/dominance, cohort relevance)?
6. **Does a named non-company event earn a durable artifact**, or stay a dated capture until a repeat consumer graduates it — and what's the trigger?

## Claude's read

Where I'd push the panel, not just relay it:

- **Run the probe before you write the frame.** The single biggest tension (T1) is answerable *today* in ~10 minutes against the live store — group it for "companies offering compound semaglutide" and count returns vs the ~9 you know are in market. It costs almost nothing and it *moves the frame's center of gravity*: a 3-of-9 result makes this a **Coverage/Depth** problem (the architecture is fine, the data is thin), while a 8-of-9 result makes it an **Access** problem (just need the query verb + relations). Don't frame around a guess you can cheaply replace with a fact. This is the "probe before you bake" principle from `engine-dev`.

- **The frame is smaller than its title.** If relations + query-time grouping + source captures genuinely cover ~80% with *zero* category entities — and the panel says they do — then the first frame shouldn't be "category/cohort intelligence." It should be **"Relations + market-question answering,"** with "cohorts/categories as a durable layer" *explicitly parked* as a non-goal. Naming the smaller frame **is** the scope discipline. The wallow's title is doing you a disservice by keeping the ontology gravity well in view.

- **Watch the *inverse* of "don't collapse types."** The panel is right that mashing Exa-similar and listicle-attested into one "competitor" field destroys provenance. But the failure mode on the other side is **relation-type sprawl** — minting competitor / substitute / partner / parent / similar / same-listicle / same-treatment-line on day one. Ship **exactly one** type (source-attested competitor/substitute), prove the record shape and the brief link, and make every additional type *earn its way in*. Same defense you apply to taxonomy values.

- **Weight the dissent.** Five angles agreed easily — partly because they share the wallow's framing, so treat the consensus as "no strong objection" rather than "independently confirmed." The one genuine dissenter, **TH**, is also the one closest to the actual data. His message is the load-bearing one: *the bottleneck is completeness, not architecture.* That's exactly what the probe tests — which is why it comes first.

- **The real fork is the folder.** Whether dated captures land in `store/<domain>/signals/` or a new `cohorts/<slug>/signals/` isn't a filing detail — it's the decision about whether this is a *new layer* or an *extension of the one you have*. Decide it consciously and early; everything downstream inherits from it. My lean: per-company `signals/` until a capture genuinely has no company to attach to — which keeps `cohorts/` empty (and unbuilt) as long as possible.

**My recommended next move:** run the probe → reframe to "Relations + market-question answering" → write *that* frame, with relations (one type, freshness-mandatory) as the only build, and the `cohorts/` folder as a deferred open question rather than a foregone conclusion.

## See also

- [Wallow: cohorts and categories](2026-06-18-wallow.md) — the source spark and problem decomposition
- [Frame: a global company-research engine](../2026-05-29-frame.md) · [Architecture](../2026-05-30-architecture.md)
- [Traction approach](../2026-06-15-traction-approach.md) — the capture→persist→diff precedent the relation freshness contract should mine
- [Personas](../../documentation/personas.md) · [Strategic pillars](../../documentation/strategic-pillars.md)
