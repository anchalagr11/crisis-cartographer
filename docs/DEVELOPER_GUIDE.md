# Developer Guide

## Local Setup

### Backend
1. **Requirements**: Python 3.10+
2. **Install Deps**: `pip install -r requirements.txt`
3. **Environment**: Create a `.env` file based on `.env.example`.
4. **Run Server**:
   ```bash
   set PYTHONPATH=.
   python -m uvicorn backend.app.main:app --reload
   ```

### Frontend
1. **Requirements**: Node.js 18+
2. **Install Deps**: `npm install --legacy-peer-deps`
3. **Run Dev**: `npm start`

## Testing
We use `pytest` for backend testing.
```bash
set PYTHONPATH=.
pytest backend/tests/unit
```

## Adding New Crises
1. Create a new JSON file in `data/crises/`.
2. Follow the naming convention: `{primary_country}-{year}.json`.
3. Ensure all fields match the `Crisis` model in `backend/app/models/crisis.py`.
4. Run `pytest` to ensure data validation passes.

## Intelligence Layer
The system defaults to `MOCK_LLM = True` in `config.py`. To enable GPT-4 insights:
1. Set `MOCK_LLM=False` in your `.env`.
2. Provide a valid `OPENAI_API_KEY`.
