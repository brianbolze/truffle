# V5 blind PQR-lite scoring protocol

Input:

- Worker protocol
- Cleaned tile manifest
- Capture QA
- Judge/pruned evidence YAML

Do not read profile/company dossiers, live web, prior experiment findings, Brian
ratings, reference anchors, evaluation files, or raw unpruned evidence except as
needed to understand accepted card IDs.

## Job

Produce blind site-level PQR-lite scores from cleaned screenshots and pruned visual
evidence. Every score must cite visible evidence.

## Dimensions

Use a 1-5 scale:

- `typography_hierarchy`
- `layout_components`
- `color_brand_imagery`
- `iconography_graphics`
- `overall_visual_quality`

Scale:

- 5: rare, visibly controlled, distinctive, and finished across multiple inspected
  regions.
- 4: clearly above generic competence; strong craft with limited caveats.
- 3: competent or mixed; usable, coherent, or ambitious but not fully controlled.
- 2: weak; generic, dated, inconsistent, or visibly under-finished in important
  regions.
- 1: broken or amateur at the visual-system level.

Calibration:

- Default down when evidence is thin.
- Generic competence is not a 4.
- Ambition, density, or dark/glossy styling is not a 4 unless execution supports it.
- Broken fundamentals cap top-end scores even when one family has attractive moments.
- Capture-excluded tiles cannot support a score.
- If a family has no accepted evidence for a site, score conservatively and say why.

## Output

Return YAML:

```yaml
site_scores:
  - site: example.com
    dimensions:
      typography_hierarchy:
        score: 1-5
        evidence:
          - card_id or tile_path
      layout_components:
        score: 1-5
        evidence:
          - card_id or tile_path
      color_brand_imagery:
        score: 1-5
        evidence:
          - card_id or tile_path
      iconography_graphics:
        score: 1-5
        evidence:
          - card_id or tile_path
      overall_visual_quality:
        score: 1-5
        evidence:
          - card_id or tile_path
    rationale: "Two to four calibrated sentences."
ranking:
  - site: example.com
    overall_visual_quality: 1-5
notes: |-
  Short calibration notes and uncertainty.
```
