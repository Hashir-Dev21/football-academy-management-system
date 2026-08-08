from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.match import MatchCreate
from app.crud.match import (
    create_match,
    get_matches,
    get_match,
    update_match,
    delete_match,
    get_upcoming_matches
)
router = APIRouter(
    prefix="/matches",
    tags=["Matches"]
)


@router.post("/")
def add_match(
    match: MatchCreate,
    db: Session = Depends(get_db)
):
    return create_match(db, match)


@router.get("/")
def all_matches(
    db: Session = Depends(get_db)
):
    return get_matches(db)

@router.get("/upcoming")
def upcoming_matches(
    db: Session = Depends(get_db)
):
    return get_upcoming_matches(db)


@router.get("/{match_id}")
def single_match(
    match_id: int,
    db: Session = Depends(get_db)
):
    return get_match(db, match_id)


@router.put("/{match_id}")
def edit_match(
    match_id: int,
    match: MatchCreate,
    db: Session = Depends(get_db)
):
    return update_match(db, match_id, match)


@router.delete("/{match_id}")
def remove_match(
    match_id: int,
    db: Session = Depends(get_db)
):
    return delete_match(db, match_id)

