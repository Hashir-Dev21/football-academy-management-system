from sqlalchemy.orm import Session

from app.database.models import Team
from app.schemas.team import TeamCreate


def create_team(db: Session, team: TeamCreate):
    new_team = Team(**team.model_dump())

    db.add(new_team)
    db.commit()
    db.refresh(new_team)

    return new_team


def get_teams(db: Session):
    return db.query(Team).all()


def get_team(db: Session, team_id: int):
    return db.query(Team).filter(
        Team.id == team_id
    ).first()

def update_team(db: Session, team_id: int, team: TeamCreate):

    existing_team = db.query(Team).filter(
        Team.id == team_id
    ).first()

    if not existing_team:
        return {"message": "Team not found"}

    existing_team.team_name = team.team_name
    existing_team.age_group = team.age_group
    existing_team.academy_id = team.academy_id

    db.commit()
    db.refresh(existing_team)

    return existing_team


def delete_team(db: Session, team_id: int):

    team = db.query(Team).filter(
        Team.id == team_id
    ).first()

    if not team:
        return {"message": "Team not found"}

    db.delete(team)
    db.commit()

    return {"message": "Team deleted successfully"}