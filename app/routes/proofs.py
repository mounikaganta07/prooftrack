from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Proof, Skill
from app.schemas import ProofCreate, ProofOut

router = APIRouter(prefix="/proofs", tags=["proofs"])


@router.post("", response_model=ProofOut)
def create_proof(payload: ProofCreate, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == payload.skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    proof = Proof(**payload.model_dump())
    db.add(proof)
    db.commit()
    db.refresh(proof)
    return proof


@router.get("", response_model=list[ProofOut])
def list_proofs(db: Session = Depends(get_db)):
    return db.query(Proof).order_by(Proof.created_at.desc()).all()