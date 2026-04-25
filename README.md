# Crisis Cartographer (v1.0)

Crisis Cartographer is an intelligence platform designed to normalize and compare global crises using deterministic metrics and LLM-powered narrative insights.

## 🚀 Key Features
- **Deterministic Comparison**: Jaccard similarity and metric ratio engines.
- **Narrative Intelligence**: GPT-4 driven qualitative analysis with fail-safe fallbacks.
- **Temporal Mapping**: Synchronized "Relative Time" timelines.
- **Geospatial Context**: Interactive Leaflet maps with proximity analysis.
- **Predictive Synthesis**: 12-month probabilistic trajectory forecasting.
- **Relational Graphs**: Visualizing historical precedents and conflict networks.

## 📚 Documentation
- [Architecture Overview](docs/ARCHITECTURE.md)
- [API Reference](docs/API_REFERENCE.md)
- [Data Schema](docs/SCHEMA.md)
- [Developer/Setup Guide](docs/DEVELOPER_GUIDE.md)
- [User Guide](docs/USER_GUIDE.md)
- [Original Technical Plan](docs/plad.md)

## 🛠 Tech Stack
- **Backend**: FastAPI, Pydantic v2, pytest.
- **Frontend**: React 18, TypeScript, Tailwind CSS, Leaflet.
- **Data**: JSON-based flat-file crisis records.

## 🧪 Quick Start
```bash
# Backend
cd backend
set PYTHONPATH=.
python -m uvicorn app.main:app --reload

# Frontend
cd frontend
npm install --legacy-peer-deps
npm start
```

## 📜 License
MIT License