from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.coach import CoachCreate
from app.crud.coach import (
    create_coach,
    get_coaches,
    get_coach,
    update_coach,
    delete_coach
)

router = APIRouter(
    prefix="/coaches",
    tags=["Coaches"]
)


@router.post("/")
def add_coach(
    coach: CoachCreate,
    db: Session = Depends(get_db)
):
    return create_coach(db, coach)


@router.get("/")
def all_coaches(
    db: Session = Depends(get_db)
):
    return get_coaches(db)


@router.get("/{coach_id}")
def single_coach(
    coach_id: int,
    db: Session = Depends(get_db)
):
    return get_coach(db, coach_id)

@router.put("/{coach_id}")
def edit_coach(
    coach_id: int,
    coach: CoachCreate,
    db: Session = Depends(get_db)
):
    return update_coach(db, coach_id, coach)

@router.delete("/{coach_id}")
def remove_coach(
    coach_id: int,
    db: Session = Depends(get_db)
):
    return delete_coach(db, coach_id)