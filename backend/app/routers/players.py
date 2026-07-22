from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.players import PlayerCreate, PlayerUpdate
from app.crud.players import (
    create_player,
    get_players,
    get_player_by_id,
    delete_player,
    update_player
)

router = APIRouter(
    prefix="/players",
    tags=["Players"]
)


@router.post("/")
def add_player(player: PlayerCreate, db: Session = Depends(get_db)):
    return create_player(db, player)
@router.get("/")
def all_players(db: Session = Depends(get_db)):
    return get_players(db)
@router.get("/{player_id}")
def one_player(player_id: int, db: Session = Depends(get_db)):
    return get_player_by_id(db, player_id)
@router.delete("/{player_id}")
def remove_player(player_id: int, db: Session = Depends(get_db)):
    return delete_player(db, player_id)

@router.put("/{player_id}")
def edit_player(
    player_id: int,
    player: PlayerUpdate,
    db: Session = Depends(get_db)
):
    return update_player(db, player_id, player)