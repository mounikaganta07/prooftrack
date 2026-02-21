from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import InsightsOut
from app.services.gap_analyzer import compute_gaps

router = APIRouter(prefix="/insights", tags=["insights"])


@router.get("/gaps", response_model=InsightsOut)
def gaps(db: Session = Depends(get_db)):
    gaps_list = compute_gaps(db)
    return {"gaps": gaps_list}