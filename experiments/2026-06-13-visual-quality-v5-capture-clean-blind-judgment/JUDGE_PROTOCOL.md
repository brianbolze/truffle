# V5 judge/pruning protocol

Input:

- Worker protocol
- Cleaned tile manifest
- Capture QA
- Four evidence-agent YAML outputs

Do not read profile/company dossiers, live web, prior scoring/evaluation files, or
reference quality anchors.

## Job

Prune and merge evidence cards. Do not score or rank sites.

Reject a card when:

- The tile path is not in the active cleaned manifest.
- The card cites an explicitly excluded tile.
- The claim depends on a modal, cookie banner, blank media, black card, or capture
  artifact.
- The claim is vague, taste-word heavy, or lacks a visible tell.
- The claim is mainly about business quality, claims, reputation, or copy.
- The card duplicates another card without adding a new visible tell.
- The polarity is too flattering for generic competence or visual ambition without
  finish.

Keep or merge a card when:

- A reader can verify the claim in the cited tile.
- The claim has at least one concrete visual tell.
- It adds useful contrast for a family or site.
- It helps calibrate a known trap: generic polish, ambitious inconsistency,
  template gloss, broken fundamentals, or capture artifacts.

## Output

Return YAML:

```yaml
accepted_cards:
  - id: typography_hierarchy_01
    family: typography_hierarchy
    polarity: strong | mixed | poor
    site: example.com
    page_or_region: "..."
    tile_path: "experiments/..."
    claim: "..."
    visible_tells:
      - "..."
    confidence: high | medium | low
rejected_cards:
  - source_family: typography_hierarchy
    site: example.com
    tile_path: "experiments/..."
    reason: "duplicate | vague | artifact | inactive_path | polarity_too_generous | nonvisual"
notes: |-
  Short summary of pruning decisions.
```
