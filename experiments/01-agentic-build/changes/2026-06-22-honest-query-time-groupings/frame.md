# Frame: Honest Query-Time Company Groupings

**Date**: 2026-06-22
**Status**: frame only. No proposal or implementation scope accepted.

## 30-second skim

**Truffle users often ask questions over temporary groupings of companies.** Examples: GLP-1 brands, women's health companies, finance companies, brands in an external list, companies with visible pricing.

Those groupings are useful, and they should stay lightweight. We do not need to define "market" or create a durable grouping object just because a user asks a cross-company question.

**The problem is honesty at query time:** when Truffle answers over a grouping, the reader needs to know what kind of set was used and what the answer can safely claim.

## Context

Truffle started as a company research store. A user could ask about one company and get back captured facts, evidence, and caveats.

Now users are asking comparative questions:

- "Which captured GLP-1 companies publish pricing?"
- "How complete is our women's health coverage?"
- "Which finance companies are software sellers versus investors?"
- "Which names from this source list are missing from the store?"

To answer those, the user or agent creates an on-the-fly grouping. That is normal. The risk is that the temporary grouping gets treated as more authoritative than it is.

## The Core Problem

A grouping has two failure modes.

**Mechanical errors.** The set is assembled incorrectly: raw folders counted as researched companies, comments matched as field values, overlapping groups double-counted, aliases missed, or edge-case companies left out.

**Interpretive errors.** The set is technically correct, but the answer implies too much. "Captured GLP-1-tagged companies" quietly becomes "the GLP-1 market." "Names from two listicles" quietly becomes "the market denominator."

Both produce the same bad outcome: a clean-looking answer with a hidden scope problem.

## Why This Matters

Truffle is increasingly used to generate market reads. If the grouping behind a claim is fuzzy, downstream judgements can easily go wrong, and users start to lose trust in Truffle.

The goal is not perfect coverage. The goal is that a reader can tell:

- what set was used,
- why that set was used,
- what the set leaves out,
- and what kind of claim the answer is allowed to make.

## Non-Goals

- Do not define what a "market" is for all Truffle uses.
- Do not create stored market / cohort / grouping entities by default.
- Do not force fuzzy user questions into rigid schema.
- Do not make Truffle decide whether a comparison matters strategically.

## Success Condition

A Truffle answer over a company grouping should make the grouping legible enough that the reader does not confuse:

- store coverage with market coverage,
- a structured category with a buyer-defined market,
- a source list with a census,
- or a temporary analysis set with a durable fact.

If the grouping cannot support the claim, the answer should say so instead of hiding uncertainty behind a clean number.

## Evidence Base

This frame comes from repeated internal trial reads in Market Read Lab. The detailed evidence lives in:

- `experiments/00-market-read-lab/discovery-ledger.md`
- `experiments/00-market-read-lab/triage.md` MRL-001 and MRL-002
- `QUERYING.md` Recipe 8
