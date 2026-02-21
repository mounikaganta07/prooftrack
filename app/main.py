from fastapi import FastAPI

from app.db import Base, engine
from app.routes.skills import router as skills_router
from app.routes.proofs import router as proofs_router
from app.routes.insights import router as insights_router

# Create tables on startup (simple MVP)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ProofTrack API", version="0.1.0")

app.include_router(skills_router)
app.include_router(proofs_router)
app.include_router(insights_router)


@app.get("/")
def root():
    return {"message": "ProofTrack running. Open /docs"}