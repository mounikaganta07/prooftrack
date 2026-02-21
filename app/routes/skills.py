from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Skill
from app.schemas import SkillCreate, SkillOut

router = APIRouter(prefix="/skills", tags=["skills"])


@router.post("", response_model=SkillOut)
def create_skill(payload: SkillCreate, db: Session = Depends(get_db)):
    existing = db.query(Skill).filter(Skill.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=409, detail="Skill already exists")

    skill = Skill(name=payload.name.strip(), category=payload.category.strip())
    db.add(skill)
    db.commit()
    db.refresh(skill)
    return skill


@router.get("", response_model=list[SkillOut])
def list_skills(db: Session = Depends(get_db)):
    return db.query(Skill).order_by(Skill.created_at.desc()).all()