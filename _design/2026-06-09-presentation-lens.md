# Presentation lens — rendering the store for humans

*Why the engine now renders human-facing artifacts, what rules they live under, and the running idea ledger for this layer. Exemplar: the dossier brief ([experiment](../experiments/2026-06-09-dossier-render/FINDINGS.md) → `scripts/render.py`).*

## Why the boundary moved

The Frame said "not a product" when every consumer was an agent or a SQL-literate human. A third consumer type has appeared: **outside humans** (first: a brand strategist evaluating the engine through its output). For them the rendered artifact *is* the engine — they never see schemas, recipes, or a CLI. The dossier-render experiment proved the store already holds what a beautiful brief needs (identity assets, structured offer data, trust metadata), and that one script can turn it into a deliverable worth handing over.

What did **not** move: no served API, no hosting, no accounts, no multi-tenancy. The engine produces artifacts; it never serves them. Outsiders receive files; only we run the machine.

## The framing: a second kind of lens

The repo's deepest rule already covers this: **markdown is the source of truth; everything derived is a regenerable lens.** Lenses now come in two kinds:

| Kind | Exemplar | Consumer |
|---|---|---|
| **Query lens** | `scripts/build_db.py` → `store.db` | agents, Beekeeper |
| **Presentation lens** | `scripts/render.py` → `scripts/_out/briefs/<slug>.html` | humans |

Same rules for both: derived and regenerable from the markdown, output gitignored, computed at generation time, freshness clocks visible in the artifact.

Run it directly: `python scripts/render.py <company>`.

## Guardrails

1. **Static, self-contained files only.** One script in, one openable-cold file out — no server, no build step, no framework. The moment a renderer wants infrastructure, that's the Doro flag.
2. **Operator model.** Sharing a brief ≠ sharing the engine. Artifacts travel; credentials, API keys, and the repo don't.
3. **Provenance renders or it's a bug.** Capture clocks, enumeration floors, `unverified_fields` are part of the product, not fine print. An artifact that hides its limits is more dangerous than no artifact — it's the trust surface in pixels.
4. **Renderers read the contract, never patch it.** Missing data renders as "not captured" — honest absence, never invented filler or broken layout. What a renderer *wishes* the store captured goes on the ledger below; SCHEMA changes go through the normal field-earns-its-cut process, not renderer convenience.

## Idea ledger

*The backlog for this layer — append here, **not** [`BACKLOG.md`](../BACKLOG.md) (which stays engine-level). Same discipline as there: bias to remove, graduate via an `experiments/` probe on a trigger, prune stale entries at retro. Presentation ideas multiply fast; most should die here.*

- **Compare sheet** — N slugs side by side (positioning, posture, palette, type, offer breadth); reuses `extract_model()` untouched, only the render half is new. Compares price *visibility*, quotes verbatim strings, never sorts magnitudes (Recipe 4's wall). **Act when:** the Scott session generates the ask.
- **Store wants-list from the brief renderer** — 8 capture-side gaps the renderer worked around with heuristics (wordmark ink/ground, brand-color roles, founded/HQ, verbatim tagline, structured proof numbers, font roles, committed hero crop, price magnitude-by-design): see [FINDINGS §wants](../experiments/2026-06-09-dossier-render/FINDINGS.md). These are SCHEMA candidates, not renderer fixes — promote individually when a second consumer wants the same field.
- **Gallery / corpus index page** `[parked]` — logo-grid browse over the store. Wait for someone to actually ask to browse.
- **`/brief` verb** `[parked]` — a skill wrapping `render.py`. Wait until "make me a brief for X" is a recurring spoken ask; until then the one-liner is fine.
