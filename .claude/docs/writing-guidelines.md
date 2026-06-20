# Writing Guidelines

Every page works at two zoom levels — a **30-second skim** and a **drill**. The skim must stand on its own.

## Patterns

- **Open with the frame.** Goal or locating sentence as the first block. No *"this doc covers…"* preamble.
- **Use progressive disclosure.** Key point at the top; detail hidden or below. Mix freely with plain bullets — use a plain bullet when nothing's worth hiding. `<detail>` blocks, or child / sub-pages that you link out to can be helpful for this.
- **Bold sparingly — it's the skim layer.** Lead clause of weighted bullets, the one phrase that matters. If everything's bold, nothing is.
- **Vary length. Blank lines are fine.** Uniform bullets get skipped wholesale. A one-liner next to a paragraph is a *feature*.
- **Keep tables narrow.** General rule of thumb — 3–5 columns. Wider → split, or convert to a list.
- **Callouts are load-bearing.** Callouts for goals, warnings, *Read Next* — not decoration. If you need section sub-headlines / descriptions, often good to *italicize*.
- **Voice: direct and opinionated.** *"Mix 6 passes, tightly."* Not hedged slide-deck prose.
- **YAML Frontmatter**: Often helpful to have a few structured fields at the very top of the file, like created & last_updated (as YYYY-MM-DD HH:MM), authors (agent, brian, both), etc.

## Prefer vs. Avoid

| **PREFER**                      | **AVOID**               |
|---------------------------------|-------------------------|
| Collapsible sections for depth  | Everything at top level |
| Bolded lead + short prose       | Wall of paragraphs      |
| Varied bullet length            | Uniform bullets         |
| Narrow tables                   | 7+ column tables        |
| Color that encodes an axis      | Decorative color        |
| Direct voice                    | Hedged, anodyne prose   |

## Anti-patterns

- **Same density everywhere.** Eye has nowhere to land.
- **No hierarchy on a long page.** Almost certainly wrong — depth should be navigable.
- **Sources at full weight.** Move to smaller links, footnotes, or the bottom of the page.