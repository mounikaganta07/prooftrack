from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, List


class SkillCreate(BaseModel):
    name: str = Field(min_length=2, max_length=60)
    category: str = Field(min_length=2, max_length=40)


class SkillOut(BaseModel):
    id: int
    name: str
    category: str
    created_at: datetime

    class Config:
        from_attributes = True


class ProofCreate(BaseModel):
    skill_id: int
    kind: str = Field(min_length=2, max_length=20)  # leetcode/github/note
    link: Optional[str] = None
    score: Optional[int] = Field(default=None, ge=0, le=100)
    difficulty: Optional[str] = None
    time_taken_min: Optional[int] = Field(default=None, ge=0)


class ProofOut(BaseModel):
    id: int
    skill_id: int
    kind: str
    link: Optional[str]
    score: Optional[int]
    difficulty: Optional[str]
    time_taken_min: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True


class RevisionOut(BaseModel):
    id: int
    skill_id: int
    next_revision_date: date
    interval_days: int

    class Config:
        from_attributes = True


class GapItem(BaseModel):
    skill_id: int
    skill_name: str
    category: str
    proof_count: int
    last_proof_at: Optional[datetime]
    status: str  # OK / NEEDS_PROOF / NEEDS_REVISION


class InsightsOut(BaseModel):
    gaps: List[GapItem]