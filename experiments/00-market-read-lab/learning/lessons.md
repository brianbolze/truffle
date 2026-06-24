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
