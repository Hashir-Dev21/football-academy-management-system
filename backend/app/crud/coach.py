from sqlalchemy.orm import Session

from app.database.models import Coach
from app.schemas.coach import CoachCreate


def create_coach(db: Session, coach: CoachCreate):
    new_coach = Coach(**coach.model_dump())

    db.add(new_coach)
    db.commit()
    db.refresh(new_coach)

    return new_coach


def get_coaches(db: Session):
    return db.query(Coach).all()


def get_coach(db: Session, coach_id: int):
    return db.query(Coach).filter(
        Coach.id == coach_id
    ).first()

def update_coach(db: Session, coach_id: int, coach_data: CoachCreate):

    coach = db.query(Coach).filter(
        Coach.id == coach_id
    ).first()

    if not coach:
        return None

    for key, value in coach_data.model_dump().items():
        setattr(coach, key, value)

    db.commit()
    db.refresh(coach)

    return coach

def delete_coach(db: Session, coach_id: int):

    coach = db.query(Coach).filter(
        Coach.id == coach_id
    ).first()

    if not coach:
        return None

    db.delete(coach)
    db.commit()

    return {"message": "Coach deleted successfully"}