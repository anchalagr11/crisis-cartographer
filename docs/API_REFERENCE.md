# API Reference (v1.0)

Base URL: `http://localhost:8000/api/v1`

## Endpoints

### 1. Crisis Discovery
- **`GET /crises`**: List all available crisis records.
- **`GET /crises/{id}`**: Retrieve full detail for a specific crisis, including similar conflict recommendations.
- **`POST /search`**: Filter crises by tags, status, or keyword.
    - *Body*: `{"query": "string", "tags": [], "status": "active"}`

### 2. Comparison Engine
- **`POST /compare`**: Perform a pairwise comparison between two crises.
    - *Body*: `{"crisis_ids": ["id1", "id2"]}`
    - *Returns*: `ComparisonResult` object including metrics, timeline, map data, and LLM insights.

### 3. Metadata & Schema
- **`GET /schema`**: returns the Unified Crisis Schema (OpenAPI/JSON Schema format).
- **`GET /health`**: API status check.

### 4. Export
- **`POST /export/json`**: Generates a structured JSON analytical report from a `ComparisonResult`.

## Key Models

### `Crisis`
The core data record representing a single crisis event.
- `crisis_id`: Unique identifier (slug).
- `name`: Human-readable name.
- `status`: [active, resolved, frozen, escalating].
- `cause_tags`: List of drivers (e.g., "sectarian", "resources").

### `ComparisonResult`
The output of the analytical engine.
- `metrics`: Numerical similarity and intensity scores.
- `key_similarities/differences`: Qualitative narrative points.
- `aligned_events`: Synchronized timeline data.
- `forecasts`: 12-month predictive projections.
