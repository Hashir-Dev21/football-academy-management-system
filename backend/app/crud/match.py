from sqlalchemy.orm import Session

from app.database.models import Match
from app.schemas.match import MatchCreate


def create_match(db: Session, match: MatchCreate):
    new_match = Match(**match.model_dump())

    db.add(new_match)
    db.commit()
    db.refresh(new_match)

    return new_match


def get_matches(db: Session):
    return db.query(Match).all()


def get_match(db: Session, match_id: int):
    return db.query(Match).filter(
        Match.id == match_id
    ).first()


def update_match(
    db: Session,
    match_id: int,
    match: MatchCreate
):
    existing_match = db.query(Match).filter(
        Match.id == match_id
    ).first()

    if not existing_match:
        return {"message": "Match not found"}

    existing_match.home_team_id = match.home_team_id
    existing_match.away_team_id = match.away_team_id
    existing_match.match_date = match.match_date
    existing_match.match_time = match.match_time
    existing_match.venue = match.venue
    existing_match.home_score = match.home_score
    existing_match.away_score = match.away_score
    existing_match.status = match.status

    db.commit()
    db.refresh(existing_match)

    return existing_match


def delete_match(db: Session, match_id: int):

    match = db.query(Match).filter(
        Match.id == match_id
    ).first()

    if not match:
        return {"message": "Match not found"}

    db.delete(match)
    db.commit()

    return {"message": "Match deleted successfully"}

def get_upcoming_matches(db: Session):
    return db.query(Match).filter(
        Match.status == "Scheduled"
    ).all()