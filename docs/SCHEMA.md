# Unified Crisis Schema (v1.0)

The Unified Crisis Schema ensures that all conflict data is comparable across different time periods and geographies.

## Core Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `name` | String | Common name of the crisis. |
| `crisis_id` | String | Unique slug (e.g., `syria-2011`). |
| `status` | Enum | Current state: `active`, `resolved`, `frozen`, `escalating`. |
| `start_date` | ISO Date | Initial date of conflict onset. |
| `regions_affected`| List[ISO] | ISO 3166-1 alpha-2 country codes. |
| `cause_tags` | List[Str] | Standardized tags: `sectarian`, `proxy`, `resources`, etc. |

## Sub-Models

### `CasualtiesRange`
- `low`: Minimum estimate.
- `high`: Maximum estimate.
- `confidence`: Data reliability level (Low, Med, High).

### `Displacement`
- `idp`: Internally displaced persons (in millions).
- `refugees`: Cross-border refugees (in millions).

### `KeyEvent`
- `date`: ISO Date.
- `type`: `trigger`, `escalation`, `peak`, `negotiation`, `resolution`.
- `description`: Qualitative event summary.

## Validation Rules
1. `end_date` must be after `start_date` if provided.
2. `casualties_range.high` must be $\ge$ `casualties_range.low`.
3. `regions_affected` must contain valid ISO alpha-2 codes.
