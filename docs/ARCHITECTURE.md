# Architecture Overview: Crisis Cartographer

The Crisis Cartographer is designed as a modular, data-driven intelligence platform that combines deterministic analysis with generative narrative insights.

## System Components

### 1. Backend (FastAPI)
- **API Layer**: RESTful endpoints for crisis discovery, search, and comparison.
- **Engines**:
    - **Normalization Engine**: Standardizes heterogeneous crisis data (dates, metrics).
    - **Comparison Engine**: Pairwise analysis using Jaccard similarity and metric ratios.
    - **Temporal Service**: Aligns disparate timelines to a relative "Month 0" scale.
    - **Geo Service**: Calculates Haversine distances and regional proximities.
    - **Recommendation Service**: Clustering logic to find similar historical conflicts.
- **Intelligence Layer**: OpenAI GPT-4 integration for narrative generation with a deterministic fallback.

### 2. Frontend (React + TypeScript)
- **Design System**: Built with Tailwind CSS, following a high-fidelity, data-dense aesthetic.
- **Visualizations**:
    - **ParallelTimeline**: Side-by-side event progression.
    - **CrisisMap**: Leaflet-based geospatial impact mapping.
    - **CrisisGraph**: SVG-based relational networking.
- **Analytical Views**: Split-panel comparison dashboards with predictive forecasting.

### 3. Data Layer
- **Unified Crisis Schema**: A Pydantic-based specification for crisis records.
- **Flat-File Storage**: Crisis records stored as versioned JSON files for transparency and ease of curation.

## Data Flow
1. **Request**: User selects two crisis IDs.
2. **Analysis**: Backend loads records, normalizes metrics, and calculates similarity/proximity.
3. **Intelligence**: Metrics are passed to the LLM Narrator (or Fallback Engine) to generate text.
4. **Projection**: Statistical trends are calculated for the 12-month forecast.
5. **Response**: A single `ComparisonResult` object is returned to the frontend.
