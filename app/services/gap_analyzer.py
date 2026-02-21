from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models import Skill, Proof


def compute_gaps(db: Session):
    """
    Simple rule:
    - If proof_count == 0 => NEEDS_PROOF
    - Else if last proof older than 7 days => NEEDS_REVISION
    - Else OK
    """
    results = []

    skills = db.query(Skill).all()

    for s in skills:
        proof_count = db.query(func.count(Proof.id)).filter(Proof.skill_id == s.id).scalar() or 0
        last_proof_at = db.query(func.max(Proof.created_at)).filter(Proof.skill_id == s.id).scalar()

        if proof_count == 0:
            status = "NEEDS_PROOF"
        else:
            cutoff = datetime.utcnow() - timedelta(days=7)
            status = "NEEDS_REVISION" if (last_proof_at and last_proof_at < cutoff) else "OK"

        results.append(
            {
                "skill_id": s.id,
                "skill_name": s.name,
                "category": s.category,
                "proof_count": proof_count,
                "last_proof_at": last_proof_at,
                "status": status,
            }
        )

    return results