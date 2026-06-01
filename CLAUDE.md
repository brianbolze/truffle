# web-research — agent orientation

A project-agnostic **company-research engine**: Firecrawl captures, Claude reasons, a file-first store any project can query. This is the shared engine — not any one project's knowledge base. Status + layout: [`README.md`](README.md).

## Find your path

- **Run a capture** (profile/research a company) → use the `/research-company` skill. It's self-contained and points to its own contract ([`firecrawl-capture.md`](_design/references/firecrawl-capture.md) + [`SCHEMA.md`](SCHEMA.md)/[`TAXONOMIES.md`](TAXONOMIES.md)) — you need nothing else here.
- **Consume the store** (query captured research) → [`QUERYING.md`](QUERYING.md), then `store/<domain>/`. The dossier *is* the product.
- **Work on the engine** (design/build) → [frame](_design/2026-05-29-frame.md) (why / scope / non-goals) → [architecture](_design/2026-05-30-architecture.md) (how it works) → [`SCHEMA.md`](SCHEMA.md) + [`TAXONOMIES.md`](TAXONOMIES.md) (the contract). Working principles + prior art auto-load when you touch the build surface.
