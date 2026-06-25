# Receipt - C1 signals-absence

Confirms the deep-tech cohort has no `signals/` (time-axis) substrate.

```yaml
receipt_type: store-query
created: 2026-06-25
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/{electra-aero,verdegoaero-com,blueenergy-co,cfs-energy,euclidpower-com,evoloh-com,sorafuel-com,beta-team}/signals/` | 2026-06-25 (filesystem) | local-store | derived | none | no | C1 |

## Method

For each of the 8 cohort domains, counted entries under `store/<domain>/signals/`:

```bash
for d in electra-aero verdegoaero-com blueenergy-co cfs-energy \
         euclidpower-com evoloh-com sorafuel-com beta-team; do
  match=$(ls -d store/${d}* 2>/dev/null | head -1)
  sig=$(ls "$match/signals" 2>/dev/null | wc -l | tr -d ' ')
  echo "$match → signals: $sig"
done
```

## Evidence

```
store/electra-aero → signals: 0
store/verdegoaero-com → signals: 0
store/blueenergy-co → signals: 0
store/cfs-energy → signals: 0
store/euclidpower-com → signals: 0
store/evoloh-com → signals: 0
store/sorafuel-com → signals: 0
store/beta-team → signals: 0
```

All eight return `0` (no `signals/` directory or empty). The `signals/` append layer was
never run on this cohort.

## Limits

Proves only that no Signals were *captured*, not that no signal *exists* — beta-team's SEC
10-Q and several firms' dated funding announcements are publicly available; they are simply
not in the store. "Not captured" ≠ "not available" (L004/L005).

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 0/8 cohort profiles have any `signals/` capture; no time-axis substrate exists for a momentum read | S1 | Absence of capture, not absence of signal. |
