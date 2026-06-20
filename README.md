# pyfarm-crops

Crop and cultivar registry with real growing data.

## Purpose

Centralized database of crop cultivars with optimal growing conditions per stage.

## Phase 1 Scope

- **Mushroom species**: Oyster, shiitake, lion's mane (3+ varieties each)
- **Microgreens**: Radish, broccoli, sunflower, pea shoots, alfalfa (5+ varieties)
- **Data per cultivar**:
  - Optimal temperature ranges (day/night)
  - Humidity setpoints
  - EC/pH ranges (for hydro)
  - Photoperiod requirements
  - DLI (daily light integral)
  - Expected cycle time
  - Yield expectations

## Integration

- Referenced by pyfarm-lighting for DLI/photoperiod defaults
- Referenced by pyfarm-nutrients for EC/pH defaults
- Queried by pyfarm-cli for cultivar suggestions

## Development

```bash
pip install -e ".[dev]"
pytest tests/
```
