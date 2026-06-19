# Starter Scope

This is a non-authoritative starter list for Run 001. The Loop 1 agent should revise it
from the store rather than treat it as a denominator.

## Likely In-Scope Examples

- `bluechew-com` — men-only ED / sexual performance; named fulfillment and pharmacy
  claims may matter.
- `getpetermd-com` — men-first TRT / hormones / sexual wellness; broad catalog and
  generic partner-pharmacy language.
- `home-medvi-org` — multi-vertical DTC front door with named clinical and pharmacy
  partners.
- `honehealth-com` — men-first hormone / longevity; likely relevant if captured.
- `invigormedical-com` — men's / women's health clinic with named partner pharmacies.
- `maximustribe-com` — men's hormone / performance; useful comparator if captured.
- `rexmd-com` — men's-health front door owned by LifeMD; parent relation may be
  load-bearing.
- `rugiet-com` — men's performance medicine; mostly compounded formulations and
  partner-pharmacy claims.

## Edges To Look For

- Parent / owned-by / front-door relationship
- Clinical provider network or affiliated medical group
- Named pharmacy / fulfillment partner
- Generic "partner pharmacy" claim with no named entity
- Product-equivalence relation across molecule stacks or formulations, if it appears
  unavoidable while answering the main question

## Guardrails

- Treat missing partner names as "not found in captured material," not as "no partner."
- Do not turn this into a broad men's health census.
- Do not propose typed relations unless the relationship changes the market answer.
