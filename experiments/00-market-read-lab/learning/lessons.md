# Lessons

The only reviewed decision surface for Market Read Lab. A lesson is a general, reusable pattern
a learning pass distilled from observations — never raw run narrative. Raw sightings stay in
[`observations.md`](observations.md); Brian-specific calls stay in [`brian.md`](brian.md).

## How a lesson works

**States:** `proposed → accepted → graduated`, with `parked` and `dropped` as exits. Rows are
never deleted; `parked`/`dropped` stay as the record of a call made.

**Routes** — where an accepted lesson goes if it graduates:

- `Agentic Build` — an engine change packet.
- `docs/recipe edit` — a light documentation or convention edit (e.g. a QUERYING recipe).
- `capture worklist` — proposed capture/corpus work.
- `roadmap` — a Notion/BACKLOG-sized product decision.
- `no-op` — accepted as a no-build / anti-sprawl lesson.

**Two tests before graduating:** (1) state the rule without naming a single run or company;
(2) name what it replaces — if nothing, don't add it.

**Graduation is Brian's call.** A pass proposes; only Brian moves a lesson to `graduated`. To
check whether an observation is already used, grep this file for its row — `observations.md`
carries no back-stamp in v0.

Each block carries: **state · route · source observations · rule (stated generally) · replaces · notes.**

These five are seeds from the first ~35 runs, carried over when triage was retired. They are
not the whole backlog — the old queue's narrative lives in [`../_archive/triage-legacy-2026-06-24.md`](../_archive/triage-legacy-2026-06-24.md).

---

## L001 — Bounded-live coverage radar answers "who is the store missing?"

- **state:** graduated — 2026-06-22, into [`QUERYING.md`](../../../QUERYING.md) Recipe 9 (pre-migration).
- **route:** docs/recipe edit.
- **source observations:** runs 012 / 022 / 024 (three verticals); archived triage MRL-002.
- **rule:** A best-of/listicle coverage gap is answerable at query time — SERP → ≥2 authoritative listicles → cross-source intersection → token-match store diff — with no helper, field, or stored object.
- **replaces:** the reflex to build a "missing companies" list or field; it stays a documented pattern.
- **notes:** Stayed pattern-level on purpose. Other State/Signals query-recipe work is not covered by this lesson.

## L002 — A headline Signal misleads until its confound sibling travels with it

- **state:** accepted.
- **route:** docs/recipe edit (a source-rigor reading convention).
- **source observations:** runs 005 / 006 / 007 (Trustpilot score, Wayback tenure, SEC hits), 011 (score vs body), 034 (ads count); archived triage MRL-008.
- **rule:** A captured headline metric (trust score, tenure days, total hits, creative count) reads as decision-grade only when its integrity/confound sibling is surfaced with it; verdicts like "trusted" or "established" stay labeled Judgments, not State.
- **replaces:** confident reads off a lone headline field; not a monitor, score, or new schema.
- **notes:** Flavor-aware — the confound differs by source family, so name the flavor rather than flattening them.

## L003 — Decision-grade review/forum bodies are an uncaptured source ingredient

- **state:** accepted.
- **route:** capture worklist.
- **source observations:** runs 011 (Trustpilot bodies obscured by the score), 029 (signal coverage); archived triage MRL-008 / MRL-010.
- **rule:** The store holds the headline review *score* but not the review/forum *bodies* that carry the decision-grade objection clusters; a sentiment or trust read off the score alone inverts on brands whose score reflects invitation posture, not quality.
- **replaces:** treating a captured Trustpilot/score field as if it answered "what do customers actually complain about."
- **notes:** A source-family want, not a confound convention — distinct from L002. Capture is spend/approval-gated.

## L004 — Market-read denominators are partial; their reconciliation travels with the read

- **state:** accepted.
- **route:** docs/recipe edit (a read/receipt convention).
- **source observations:** runs 000 / 016 / 022 / 024 / 029; archived triage MRL-001.
- **rule:** A market denominator is slow, partial, and method-sensitive, so a read must name the sources checked, inclusion/exclusion rules, resolver/dedupe method, known gaps, and selection bias, and say "not found," never "not there." External SERP/listicle panels are a fallback when curated lists are thin, not the default denominator.
- **replaces:** an unqualified "N companies do X" headline; not a stored entity-resolution table.
- **notes:** The recurring `parse-the-value-not-the-comment` denominator footgun (runs 016/029) is the concrete instance to guard.

## L005 — Query-time grouping is enough only when the corpus already carries the cut

- **state:** accepted.
- **route:** no-op.
- **source observations:** runs 015 / 027 / 028 / 031 / 032 / 035; tag `query-time-grouping-enough`.
- **rule:** When a clean enum or consistent prose already encodes a cut, group at query time — don't mint a durable category, field, or stored object. The corollary is the trap: when that field is unpopulated, an empty *structured* surface is a coverage signal, not a market fact ("not captured" ≠ "not true").
- **replaces:** the reflex to promote a one-off grouping into durable ontology, and the inverse misread of structured-absence as market-absence.
- **notes:** Three consecutive trust-metadata reads (confidence, freshness, ownership) each concluded no-new-primitive (the `query-time-grouping-enough` verdict itself split TRUE/FALSE across them); the axis breaks entirely for capital allocators, which have no on-site price to gate.

## L006 — The price-visibility token reports buyer-reachability, not what an intermediary charges its own side

- **state:** proposed.
- **route:** docs/recipe edit (a reading convention for the price-visibility token on two-sided / intermediary entities).
- **source observations:** run 036 G1 (read: grain mismatch) + R1 (consumer review: readability trap); corroborated this pass across 4 fresh entity types — 037 S2 + DR3 (hardware hybrid: non-trap, scope sharpened), 044 S3 (payments intermediary: non-trap), 045 S2 (services: faithful `[on-request]`), 046 S1 (consumer goods: per-line token clean); 050 DR3 (keep distinct from the Services/Consulting two-conventions mechanism).
- **rule:** The SCHEMA price-visibility token (`[published | partial | on-request]`) certifies only whether a buyer can obtain the *consumer offering's* price; on a two-sided or intermediary entity it is silent on what the entity charges its monetized side (its take rate), which lives at a grain the token never addresses. A `[published]` token can therefore be misread as pricing transparency the entity does not actually offer.
- **replaces:** the reflex to read the price-visibility token as a completeness/transparency signal on non-DTC, two-sided, or intermediary entities. Corrects token *interpretation* — it does not add a field or change the token (the row pair explicitly declines a fix at n=5).
- **notes:** Cousin to L002 (a clean field over-claims unless its scope is read with it) but a distinct mechanism — a State token's grain, not a Signal headline's confound. **The 2nd-entity-type graduation precondition (set in pass 001) is now met 4× across runs 037/044/045/046**, and 037 DR3 sharpens the trap's scope: it fires only when an entity's *primary monetization runs through an intermediary leg that has no consumer-facing price* (a marketplace take-rate split) — Apple (037 S2/DR3) and Stripe (044 S3) are non-traps precisely because their consumer-facing prices ARE published. Ready for Brian's accept/graduate call. 050 DR3 cautions against folding the unrelated "one token carrying two conventions" mechanism into L006.

## L007 — A structured field's fill-rate and per-row correctness do not certify it as a cohort partition key

- **state:** proposed.
- **route:** docs/recipe edit (a QUERYING cohort-draw convention).
- **source observations:** runs 037 G2 / 039 S2 + DR1 / 042 G3 / 044 DR2 / 045 G1 / 054 G2 / 055 S3 (the system counted these explicitly: "3rd / 4th / 5th / 6th sighting"); origin 036 G3 (routed as an L005 sighting in pass 001).
- **rule:** Before drawing or grouping a cohort by a structured field, validate the field *as a partition key* — its fill-rate and individual-row correctness do not make it one. Producer-shaped classification fields (`primary_industry`, coarse `offering_category` leaves) don't encode entity-shape or buyer-goal cohorts, so an industry/category draw either scatters the cohort across many values or contaminates the draw with non-members; even a 100%-filled field is a weak key when one value dominates (`primary_industry` is 52% Healthcare store-wide); `business_model` keys cleanly only when the cohort *is* its primary-tag semantics (metered pure-plays) and fails when the cohort cuts across models or is tagged by primary leg only (hybrids). Name the draw method and its leakage; never trust a single-field draw to recover a cross-cutting cohort.
- **replaces:** the reflex to draw a cohort by `primary_industry`/coarse `offering_category`, and the inference that a high-fill or individually-correct field is therefore a safe grouping key. Adds a query-time guardrail; mints no field and retags nothing.
- **notes:** The missing store-internal third member of the denominator family (L004 = external market denominators; L005 = don't mint ontology when the corpus carries the cut). Recurs n≥6 across distinct entity-shape cohorts, both supply-side (036/037/039/042/045) and demand-side/buyer-goal (054), plus the whole-store concentration cut (055). 045 G1 is the severe flavor (no field even *approximates* the creative-agency cohort); 054 DR2 names the deeper mechanism (correct producer tags can make a captured player *invisible* to a buyer-goal draw).

## L008 — The store's honesty flags are content-complete but relay- and salience-dependent across delivery surfaces

- **state:** proposed.
- **route:** docs/recipe edit (a synthesis/relay + presentation-salience convention).
- **source observations:** runs 038 R1 + W1 / 042 R1 + S1 / 049 G1 + S2 + W1 / 051 S3 / 055 S4.
- **rule:** Every profile self-discloses its soft spots — `unverified_fields` is non-empty in 136/136 captures, and `site_notes` / "self-reported" labels / `STRAIN` markers carry the rest — but this protection is relay- and salience-dependent: it lives in prose or off a rendered surface's default path, so any downstream consumer (a delegated agent, the HTML brief's 5-second view, a structured-only read) that drops or buries the flag launders a self-reported / over-claim-prone / point-in-time fact into apparent verified fact. The fix is a relay-and-salience discipline on the *consuming* surface — carry the flag into delegated output; raise at least one flag to hero salience beside the field it qualifies — never an assumption that honest capture equals safe delivery, and never a new provenance field.
- **replaces:** the assumption that content-complete honest capture is automatically safe to relay, and the reflex to add a provenance/flag field (the flag already exists; the failure is at the consuming surface).
- **notes:** A live `risk-miss` against the engine's #1 "make AI safe to delegate to" value job (038 R1, 042 R1) — surfaced under the severe-risk bypass. Cousin to L002 (038 R1 calls itself "delegation-relay grain of L002") but a distinct mechanism: L002 is "a headline metric needs its confound sibling to not mislead"; L008 is "the honesty context already exists and is honest, but doesn't travel to / isn't salient on the delivery surface." Two sub-mechanisms, one rule: relay-drop (038/042) and salience-burial (049 preserve-but-bury in tab 4). 049 VR1 scopes it honestly — the default path is *not* flag-free when the captor wrote prose, so the protection is also a captor-prose-dependent unreliable second channel (run-037 DR2 shape). The machine-parse variant is a *different* hazard — see L009.

## L009 — Frontmatter inline `#` comments are a parse trap: strip them before keying on a field value

- **state:** proposed.
- **route:** docs/recipe edit (a QUERYING/parsing convention; carries an audit task).
- **source observations:** runs 050 G2 / 055 R1.
- **rule:** The store records contested classifications and subtractive emptiness as inline frontmatter comments (`business_model:    # empty — VC economics…`, `offering_category: [...] # STRAIN …`). A consumer that splits on `:` / `[` / `,` and takes the remainder ingests the **comment as the value** — yielding wrong counts and wrong values, not merely missed context. Any tool, recipe, or render surface that keys on a frontmatter value MUST strip inline `#` comments first; a "how many X" headline is meaningless without naming the counting rule and comment-stripping.
- **replaces:** the naive frontmatter splitter and the assumption that frontmatter values parse cleanly; mandates comment-stripping as a read-side contract. Mints no field and changes no convention — the human-protective fail-loud comment stays.
- **notes:** Distinct from L008 — that is a *human/agent reading* miss (flag present but un-relayed/buried); this is a *machine parse* error (the parser actively reads comment text as data). Both source runs caught it on the operator's own first pass (050: 68-vs-61 count footgun; 055: `business_model` read 100%-filled until comments stripped, exposing 6 true empties). 050 DR2 flags the open audit task: check whether an existing QUERYING recipe or `scripts/present` surface already keys on `offering_category[0]` without stripping — that audit decides urgency.

## L010 — Bounded-live spend must fail-closed on the *class* of variable-cost Firecrawl formats, and substitution must match cost-class, not just source-family

- **state:** proposed.
- **route:** docs/recipe edit (the Market Read Lab run playbook / `live_evidence_plan` `fail_closed_when`).
- **source observations:** runs 047 R1 + DR1 / 052 DR1 / 053 R2 + DR3 (origin instance run-040 R1, PDF).
- **rule:** Firecrawl formats that delegate post-fetch processing — PDF parsing (`parsers:[pdf]`), JSON/LLM extraction (`formats:["json"]`) — carry a variable, pre-call-invisible per-unit cost, so "stop before exceeding the ceiling" is fragile for the whole *class*, not just the format that last breached. A bounded-live plan must fail-closed on the class of variable-cost formats, not enumerate instances (PDF, then JSON, then the next one). Source substitution stays in-contract only when the substitute shares both the planned source's *family* and its *cost-class* — a same-family swap into a higher cost-class still breaches.
- **replaces:** per-instance ceiling hardening (the `fail_closed_when` block excluded PDF explicitly but not the class, so run-047's JSON-extraction breached at 7/6 credits); and family-only source-substitution reasoning (053 R2 → DR3). Tightens an existing plan contract; adds no machinery.
- **notes:** A proven fix, not a hypothesis — run-052 named the *class* ("variable-cost formats") in `fail_closed_when` and stayed at 3 of 8 credits (052 DR1). 047 DR1 is the row that reframed two instances (run-040 PDF, run-047 JSON) as one class. 052 DR1 also notes the residual risk: the class rule lives in one plan, so a future plan-writer who doesn't inherit it can still miss it — which is exactly why it wants a home in the playbook.
