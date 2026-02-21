from datetime import datetime, date
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.db import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    category = Column(String, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    proofs = relationship("Proof", back_populates="skill", cascade="all, delete-orphan")
    revisions = relationship("Revision", back_populates="skill", cascade="all, delete-orphan")


class Proof(Base):
    __tablename__ = "proofs"

    id = Column(Integer, primary_key=True, index=True)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False, index=True)

    kind = Column(String, nullable=False)  # "leetcode" / "github" / "note"
    link = Column(String, nullable=True)
    score = Column(Integer, nullable=True)  # 0-100
    difficulty = Column(String, nullable=True)  # Easy/Med/Hard
    time_taken_min = Column(Integer, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    skill = relationship("Skill", back_populates="proofs")


class Revision(Base):
    __tablename__ = "revisions"

    id = Column(Integer, primary_key=True, index=True)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False, index=True)

    next_revision_date = Column(Date, nullable=False)
    interval_days = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    skill = relationship("Skill", back_populates="revisions")