# Doro — Prior Art Map

Truffle's frozen, heavier predecessor. This map points into it so you can mine the thinking fast. Describes-and-points; whether to borrow is your call. Builder's notes = Brian's hindsight.

**Base path** (local dev only): `/Users/brianbolze/Development/software/doro/doro/` — pointers are relative to it, and stable (Doro is frozen). System overview: `docs/tech-blog-post.md`.

| Area | What they were solving | Status |
|---|---|---|
| [Classification & matching](#classification--matching) | tag into a taxonomy; score string similarity | mapped |
| [Entity resolution](#entity-resolution) | resolve a name/domain to a known company | mapped |
| [Search](#search) | look up known entities by query | mapped |
| [Candidate → verified](#candidate--verified) | turn a discovered candidate into a trusted record | mapped |
| [Finding companies](#finding-companies) | enumerate candidate companies from the web | pointers |
| [Page → structured data](#page--structured-data) | turn a web page into structured fields | pointers |
| [Data model](#data-model) | provenance / taxonomy schemas (datapoints out of scope) | pointers |

## Classification & matching
- `services/algos/.../services/matching.py` — `TextMatchingEngine`: exact → fuzzy → semantic cascade. `find_matches()` `:403`, `cluster_values()` (name dedupe) `:526`.
- `services/algos/.../services/classification.py` — classify-by-example: categories carry weighted example snippets `:41`, best match wins. No training, no per-query LLM.
- `core/.../schemas/categorical_fields/` — the taxonomies it rides on.

> **Builder's note:** Worked well in prod. Embeddings only on the semantic tier — exact+fuzzy run first — so it's "embeddings opt-in, not default." The `data-science/` mappers are a stale older try; ignore.

## Entity resolution
Resolve a reference (`"Google"` / `"google.com"` / UUID / `CompanyReference`) to a canonical company.
- `services/app/.../companies/entity_resolution/service.py` — `CompanyEntityResolver.resolve()` `:107`: ordered strategy cascade uuid → exact_domain → exact_name → `inames` (search over name/legal/alt), each with a confidence range; early-exit at `return_threshold` (0.95); `min_confidence_score` skips strategies that can't clear the bar; candidates grouped by domain. `resolve_many()` parallelizes + dedupes.
- `services/app/.../companies/entity_resolution/schemas.py` — clean result types: `CompanyResolutionResult` with computed `is_resolved` / `is_ambiguous` (gap < 0.2, `:107`) / `is_exact_match`; `StrategyExecutionResult` (uniform per-strategy return); `ResolutionMethod` literal.
- Context-aware: resolve `"Amazon"` as *competitor-of-Shopify* via `ResolutionContext`.
- Also at product / feature grain: `products/entity_resolution/`, `product_features/entity_resolution/`.

> **Builder's note:** Brian rates these abstractions as worth borrowing — the cascade + confidence-range + ambiguity-gap + uniform-result shape — as long as the Temporal (`@activity.defn`) and Postgres/search wiring is left behind. The cascade logic itself is plain Python.

## Search
- `services/app/.../services/search/search_service.py` — `EntitySearchService`: a registry/dispatcher routing a `SearchRequest` to a per-entity search service.
- `core/.../schemas/search.py` — `SearchRequest` (query, entity, query_fields, limit, cursor), `SearchStrategy` ABC, search types keyword / neural / auto, reusable `SearchFields`.
- Per-entity implementations: `companies/search/` (also `products/search/`, `product_features/search/`). Search relevance scores feed entity-resolution confidence.

## Candidate → verified
*Design thinking:* Notion — "Entity Verification & Granularity Control Problem."
*What shipped* (under `services/app/.../services/products/`):
- **Dedupe:** via the resolver cascade — see [Entity resolution](#entity-resolution); match at ≥0.95.
- **What-kind / grain:** LLM-assigned `archetype` + `granularity_class`; grain rules live only in the prompt (`discovery/llm.py:340`), no code gate.
- **Promotion gate:** `schemas/products.py:102` `ready_to_index`; its validation is a stub (name+domain → 75).

> **Builder's note:** Leaner than the design doc — a domain key + a well-prompted LLM did most of it. Open: did prompt-only grain control hold up? was the stub gate deliberate or unfinished?

## Finding companies
- `services/app/.../services/companies/discovery_strategies/` — Google/Serper (`google_strategy.py`), Exa search + `find_similar` (`exa_strategy.py`, `exa_similar_companies.py`), LLM+search (`rapid_llm.py`).
- `_is_likely_company_website()` + `skip_domains` blocklist, in `google_strategy.py`.

## Page → structured data
- `services/app/.../web_search/nav_extraction/` — pipeline: `html_reduction/.../reducer_v4.py` (12-step HTML shrink, keeps nav) → `llm_extraction/.../extractor_v1.py` (Haiku `NavDoc` prompt `:63`) → `nav_formatter.py` (markdown round-trip). Output shape: `schemas.py` (`NavDoc`).
- `services/app/.../services/documents/` — PDF/document parser dispatcher.
- *Bake-offs / evals:* `playground/notebooks/nav_extraction.ipynb`, `playground/src/analysis/` (strategy + reduction comparison), `output/nav_extraction/evaluation/`.

## Data model
*Datapoint/provenance modeling intentionally out of scope.*
- `core/.../schemas/companies.py` — company identity; domain-as-key, `alt_names`/`alt_domains`, `parent_company`.
- `core/.../schemas/products.py` — product/offering; `archetype`, `granularity_class`, `parent_product_id` (self-referential hierarchy).
- `core/.../schemas/databases/` — Notion-like flexible DB (`database`/`properties`/`values`/`view`).
- `core/.../schemas/research/research_artifacts.py` — source artifact → extracted fields.

---
*FYI, not mapped — **Reconciliation**: multi-source, time-weighted value arbitration (`services/algos/.../reconciliation/`, `RECONCILIATION_EXAMPLE.py`). The machinery domain-as-key avoids; needs Temporal alive.*
