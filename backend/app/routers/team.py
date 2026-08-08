from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.team import TeamCreate
from app.crud.team import (
    create_team,
    get_teams,
    get_team,
    update_team,
    delete_team,
    assign_player_to_team,
    get_team_players
)

router = APIRouter(
    prefix="/teams",
    tags=["Teams"]
)


@router.post("/")
def add_team(
    team: TeamCreate,
    db: Session = Depends(get_db)
):
    return create_team(db, team)


@router.get("/")
def all_teams(
    db: Session = Depends(get_db)
):
    return get_teams(db)


@router.get("/{team_id}")
def single_team(
    team_id: int,
    db: Session = Depends(get_db)
):
    return get_team(db, team_id)

@router.put("/{team_id}")
def edit_team(
    team_id: int,
    team: TeamCreate,
    db: Session = Depends(get_db)
):
    return update_team(db, team_id, team)


@router.delete("/{team_id}")
def remove_team(
    team_id: int,
    db: Session = Depends(get_db)
):
    return delete_team(db, team_id)

@router.get("/{team_id}/players")
def team_players(
    team_id: int,
    db: Session = Depends(get_db)
):
    return get_team_players(db, team_id)