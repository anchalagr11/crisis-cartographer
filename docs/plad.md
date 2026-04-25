# Crisis Cartographer Sprint Plan

---

### Phase 1: Foundation (Weeks 1–6)

#### Sprint 1: Core Schema & Environment
- **Goals:** Establish the technical foundation and data structure.
- **Tasks:**
    - Finalize `Unified Crisis Schema` (Pydantic models in [backend/app/models/crisis.py](file:///c:/Users/ancha/OneDrive/Desktop/New%20folder/backend/app/models/crisis.py)).
    - Set up project linting, formatting (Black/Isort), and basic CI/CD (GitHub Actions).
    - Create a "Seed-5" dataset (first 5 crisis records in `data/crises/`).
    - Implement basic `GET /crisis/{id}` and `GET /crises` endpoints.

#### Sprint 2: Data Curation & Search
- **Goals:** Populate the database and enable discovery.
- **Tasks:**
    - Curate 10 additional crisis records (total 15).
    - Implement `GET /search` with basic full-text filtering.
    - Implement `GET /schema` to serve the standard metadata format.
    - Build unit tests for data loading and validation.

#### Sprint 3: Normalization & Basic Comparison
- **Goals:** Enable deterministic comparison logic.
- **Tasks:**
    - Implement `Normalization Engine` (date ISO-standardization, unit conversion).
    - Implement `Comparison Engine` v1: Timeline alignment and tag-based similarity (Jaccard).
    - Curate final 5 crisis records for v1 (total 20).
    - Ensure 85% test coverage on engine logic.

---

### Phase 2: Intelligence Layer (Weeks 7–10)

#### Sprint 4: Frontend MVP
- **Goals:** Provide a visual interface for comparisons.
- **Tasks:**
    - Set up React + Tailwind CSS project structure.
    - Implement "Split-Panel" comparison view.
    - Connect frontend to `/compare` and `/crisis` endpoints.
    - Basic comparative metric tables.

#### Sprint 5: LLM & Insights
- **Goals:** Add the narrative analysis layer.
- **Tasks:**
    - Integrate OpenAI/Anthropic API service.
    - Implement prompt engineering for the Insight Generator (narrative from JSON).
    - Build the template-based fallback system (for when LLM is unavailable).
    - Implement Redis caching for common comparisons.

---

### Phase 3: UX & Access (Weeks 11–14)

#### Sprint 6: Visualizations & Export
- **Goals:** Make insights digestible and portable.
- **Tasks:**
    - Implement Interactive Timeline component (Recharts/D3).
    - Implement PDF/JSON export for comparison reports.
    - Expand dataset to 50 crises with source citations.
    - Add escalation velocity and geographic proximity scoring to the engine.

#### Sprint 7: Authentication & Personalization
- **Goals:** Secure the platform and enable user history.
- **Tasks:**
    - Integrate Auth0/Clerk for user authentication.
    - Implement "Saved Comparisons" for logged-in users.
    - Add rate limiting and API key management for the public tier.
    - Mobile/Tablet responsive UI refinements.

---

### Phase 4: Advanced Features (Weeks 15–20)

#### Sprint 8: Clustering & Similarity
- **Goals:** Move beyond pairwise comparisons.
- **Tasks:**
    - Implement multi-crisis cluster view (compare 3–5 items).
    - Implement "Surge Similarity" — surfacing historical precedents for new events.
    - Build the community data submission portal (draft).

#### Sprint 9: Geographic Intelligence
- **Goals:** Map-based analysis.
- **Tasks:**
    - Implement Map Overlay view for affected regions.
    - Add geographic bounding-box overlap scoring.
    - Finalize documentation site (OpenAPI + User Guide).

#### Sprint 10: Launch & Optimization
- **Goals:** Production readiness.
- **Tasks:**
    - Final performance audit and Redis tuning.
    - Comprehensive bug bash and UX polish.
    - Production deployment and monitoring (Sentry/Uptime Kuma).
    - Launch!
