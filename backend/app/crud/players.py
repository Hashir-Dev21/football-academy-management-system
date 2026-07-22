from sqlalchemy.orm import Session
from app.database.models import Player
from app.schemas.players import PlayerCreate


def create_player(db: Session, player: PlayerCreate):
    db_player = Player(
        full_name=player.full_name,
        age=player.age,
        position=player.position,
        academy_id=player.academy_id
    )

    db.add(db_player)
    db.commit()
    db.refresh(db_player)

    return db_player
def get_players(db: Session):
    return db.query(Player).all()
def get_player_by_id(db: Session, player_id: int):
    return db.query(Player).filter(Player.id == player_id).first()
def delete_player(db: Session, player_id: int):
    player = db.query(Player).filter(Player.id == player_id).first()

    if player:
        db.delete(player)
        db.commit()
        return {"message": "Player deleted successfully"}

    return {"message": "Player not found"}

def update_player(db: Session, player_id: int, player):
    db_player = db.query(Player).filter(Player.id == player_id).first()

    if db_player:
        db_player.full_name = player.full_name
        db_player.age = player.age
        db_player.position = player.position
        db_player.academy_id = player.academy_id

        db.commit()
        db.refresh(db_player)

        return db_player

    return {"message": "Player not found"}