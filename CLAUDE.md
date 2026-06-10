# web-research — agent orientation

A project-agnostic **company-research engine**: Firecrawl captures company sites, `tools/` captures repeatable external source signals, Claude reasons, and a file-first store any project can query. This is the shared engine — not any one project's knowledge base. Status + layout: [`README.md`](README.md).

## Find your path

- **Run a capture** (profile/research a company) → use the `/research-company` skill. It's self-contained — its own capture playbook ([`firecrawl-capture.md`](skills/research-company/firecrawl-capture.md)) ships beside it, plus the store contract ([`SCHEMA.md`](SCHEMA.md)/[`TAXONOMIES.md`](TAXONOMIES.md)) — you need nothing else here. To make one company's `offerings.md` roster comprehensive (re-capture missing lines), use the sibling `/deepen-offerings` preset.
- **Consume the store** (query captured research) → use the `/query-companies` skill. It is the read-only router/guardrail; recipes stay in [`QUERYING.md`](QUERYING.md), then `store/<domain>/`. For a human-facing handoff, render `python scripts/render.py <company>`; the brief is a regenerable lens, not a new source of truth.
- **Capture repeatable external signals** (SERP visibility, Wayback tenure, Trustpilot profile state, branded Trends, Exa neighbors) → [`tools/README.md`](tools/README.md), then the specific `tools/*.md`. Tools print JSON to stdout; callers decide where to save and how to interpret.
- **Work on the engine** (design/build) → [frame](_design/2026-05-29-frame.md) (why / scope / non-goals) → [architecture](_design/2026-05-30-architecture.md) (how it works) → [`SCHEMA.md`](SCHEMA.md) + [`TAXONOMIES.md`](TAXONOMIES.md) (the contract). Working principles + prior art auto-load when you touch the build surface.
