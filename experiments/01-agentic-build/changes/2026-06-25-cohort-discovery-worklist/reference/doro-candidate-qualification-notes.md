# Doro Notes For Candidate Qualification

Date: 2026-06-26
Status: reference note only; not a governing proposal

## Short Take

Borrow Doro's shape, not Doro's heavier machinery.

For Truffle, candidate qualification should stay packet-local and agent-led: code should assemble compact evidence cards and preserve source context; agents should classify the thing and decide whether it deserves capture, boundary review, evidence preservation, or rejection.

The useful Doro idea is not "build a robust entity-resolution service." It is the small loop:

1. Try cheap exact/domain/name matching / evidence first.
2. Use fuzzy or alias matching only to surface possible equivalences.
3. Use classify-by-example or model judgment for "what kind of thing is this?"
4. Return an inspectable result with evidence, confidence, alternatives, and caveats.

## Useful Borrowed Ideas

- **Confidence cascade:** exact domain or official-page evidence can support capture; source-page-only evidence should hit a lower ceiling and usually preserve evidence instead.
- **Ambiguity gap:** when two plausible interpretations are close, route to `boundary_review` instead of pretending the winner is obvious.
- **Classify-by-example:** keep a tiny packet-local example set for kinds like `company_or_brand`, `source_or_publisher`, `parent_or_owner`, `directory_or_listicle`, `product_or_workflow`, `nav_or_artifact`, and `uncertain`.
- **Grain control:** ask "what kind of thing is this?" before "should we capture it?"
- **Result shape:** keep `kind`, `route`, `confidence_band`, `method`, `reasons`, `blockers`, `alternatives`, `caveats`, and compact evidence references together.

## Agent-Led Lean

Do not over-code the judgment.

The qualifier should not become a pile of fragile publisher/listicle/domain heuristics. A better split:

- **Code builds the card:** candidate name/domain, source rows, page title, outbound context, aliases, evidence count, exact/fuzzy matches, and compact snippets.
- **Optional matcher proposes:** likely kind, confidence band, nearest examples, and close alternatives.
- **Agent decides:** final kind and route, with cited reasons and caveats.

This keeps classification flexible across telehealth, conversation intelligence, and future cohorts without turning packet receipts into a hidden taxonomy.

## Prototype Shape

Try a Doro-style classify-by-example pass over the existing cached candidate cards:

```text
CandidateCard
  name
  domain
  source_pages
  evidence_snippets
  exact_domain_hit
  alias_hit
  nearby_matches

QualificationResult
  kind: company_or_brand | source_or_publisher | parent_or_owner | directory_or_listicle | product_or_workflow | nav_or_artifact | uncertain
  route: capture_candidate | preserve_source_evidence | boundary_review | reject_or_defer
  confidence_band: high | medium | low
  method: exact | fuzzy_alias | classify_by_example | agent_judgment
  alternatives
  reasons
  caveats
```

The example set should be small and editable in the packet. If a label does not change routing or evaluation, cut it.

## Avoid

- Durable schema or taxonomy changes.
- Temporal/Postgres/reconciliation/indexing infrastructure.
- Blended numeric scores.
- Automatic full capture.
- Qrels or Brian-reviewed labels as classifier inputs. Join them only after routing for evaluation.
- Vertical-specific negative categories unless they remain free-text caveats.

## Cheapest Test

Reuse the cached page-extraction candidates from this packet. No new source spend.

Run the qualifier over both telehealth and conversation-intelligence candidates, then evaluate after routing. The borrowed shape helps if it:

- keeps source/listicle/publisher artifacts out of `capture_candidate`;
- preserves page-extraction recall gains;
- sends domainless but plausible brands to `boundary_review`, not false reject;
- makes top capture candidates auditable from the evidence card;
- works with the same kind/route menu across both cohorts.
