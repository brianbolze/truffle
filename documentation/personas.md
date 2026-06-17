# User Personas

**Personas are the lenses we convene to pressure-test a call.** Put each on and ask *who does this serve, who does it ignore?* — primarily for roadmap prioritization, but also for writing docs and designing the tools. A persona earns its seat if wearing it would change a call you'd otherwise get wrong.

Pairs with [Product Pillars / Themes](./strategic-pillars.md): pillars = *what value* a bet creates; personas = *whose shoes* you stand in to feel it.


## Primary Consumers
Run every decision through these:

**The Strategist** — *anchored on Scott Witt (Parlance); ex-Apple / Peloton / Twill*

The senior creative who consumes the brief for narrative and whitespace — judges it by whether it lands with a creative director in five seconds. He's the **chef** in the **kitchen**; Truffle is the **farm** that hands him the highest-quality, freshest ingredients to work with.

- **Wants:** magic + finish, verbatim brand language, whitespace & convergence reads, pricing visible by default, plain-English everything, evocative naming when it earns it.
- **Resists:** exposed architecture, engineer-speak, engine-internals dressed as features, setup ceremony, generic AI hype.

**The Pantry** — *a downstream system built on Truffle (the archetype; the Teleprescribe "pantry" is the first real one)*

The class of consumer that reads Truffle's captured **state** and builds its *own* maintained layer on top — judgments, enrichment, monitoring, a project's working knowledge. Where Truffle is the **farm** that grows cited ingredients, the Pantry is the stocked larder downstream, keeping its own higher-order reads fresh off them — building on the farm precisely so it never re-captures. *(Pantries differ in shape and keep evolving — this is the posture, not any one build.)*

- **Wants:** a stable, queryable contract; cited, dated, machine-readable provenance; freshness it can detect cheaply (what changed since last look); Truffle to stay a clean **state / facts** layer it can build its own judgments on; frictionless programmatic access.
- **Resists:** breaking changes to the contract; capture it can't trust or re-diff; ambiguous freshness; Truffle climbing into its territory — baking in opinions or "cooking the meal" instead of growing the ingredients.

**First Contact** *(New User)* — *any human or agent at first run*

README open, nothing captured yet, no mental model — deciding in ninety seconds whether this is real.

- **Wants:** a quickstart that works first try, narration of what's happening, plain-English errors with a next step, one obvious default, an honest "what this is" before any depth.
- **Resists:** cryptic output, silent long-running captures, undocumented setup, MCP-first access before they've seen a brief, jargon that assumes the system is already in your head.

## The bench

*Convened only when a decision is in their lane.*

- **Dev Agent** *(Claude Code, in-repo)* — the build / maintain lens. **Wants** clean grep-verifiable contracts, defaults over knobs, terse output, deleting code; **resists** config sprawl, living infra, half-finished modules, bloat. → *tooling & contract calls.*
- **The Steward** *(corpus caretaker)* — keeps the store a healthy, honest asset. **Wants** coverage, freshness, provenance integrity, gaps surfaced and refreshed; **resists** rot, dangling relations, anything that looks complete but isn't. → *coverage / health calls.*
- **Beekeeper-Brian** *(you, hands-on)* — browses the store and writes ad-hoc SQL over `store.db`. **Wants** the synthesis that pays off the corpus — convergence reads, store-health, slicing cohorts; **resists** footgun aggregations and false completeness. → *synthesis calls.*
- **The Founder** *(you, arbiter)* — does this compound the warm / cited / cheap-to-reask moat **and** respect "stay light"? **Wants** bets that deepen the asset and re-pay forever; **resists** XL standing surface, productizing for an audience of one. → *the tiebreaker on every roadmap bet.*

## How to use this

- **Run a call through the three Primary Consumers first** — then pull a bench lens when its situation comes up (a roadmap bet → the Founder; an onboarding or docs call → First Contact; a corpus-health call → the Steward).
- **The friction is the point.** When two lenses disagree — the Pantry wants the raw field, the Strategist wants the rendered brief — that's the trade-off made visible, not a bug.
- **Name the hat.** Brian himself wears several — Founder, Beekeeper, even Steward or Strategist for his own projects — so say which lens you're in.


Authoritative reference for this is in Notion: [User Personas](https://app.notion.com/p/getdoro/User-Personas-38284b6d1f4980f5833cff61169a9358)