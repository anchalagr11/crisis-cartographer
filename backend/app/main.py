from fastapi import FastAPI
from .api.routes import compare, crisis, search, schema, export

app = FastAPI(title="Crisis Cartographer API", version="1.0.0")

app.include_router(compare.router, prefix="/api/v1")
app.include_router(crisis.router, prefix="/api/v1")
app.include_router(search.router, prefix="/api/v1")
app.include_router(schema.router, prefix="/api/v1")
app.include_router(export.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Crisis Cartographer API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
