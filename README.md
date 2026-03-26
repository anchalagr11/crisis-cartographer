# Crisis Cartographer

A full-stack application for crisis analysis and comparison.

## Project Structure

- `backend/` - FastAPI backend
- `frontend/` - React frontend
- `data/` - Crisis data and schemas
- `docs/` - Documentation
- `scripts/` - Utility scripts
- `tests/` - Test suites
- `docker/` - Docker configurations

## Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## Development

- Backend runs on http://localhost:8000
- Frontend runs on http://localhost:3000