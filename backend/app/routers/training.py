from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.training import TrainingCreate
from app.crud.training import (
    create_training,
    get_trainings,
    get_training,
    update_training,
    delete_training
)

router = APIRouter(
    prefix="/trainings",
    tags=["Trainings"]
)


@router.post("/")
def add_training(
    training: TrainingCreate,
    db: Session = Depends(get_db)
):
    return create_training(db, training)


@router.get("/")
def all_trainings(
    db: Session = Depends(get_db)
):
    return get_trainings(db)


@router.get("/{training_id}")
def single_training(
    training_id: int,
    db: Session = Depends(get_db)
):
    return get_training(db, training_id)


@router.put("/{training_id}")
def edit_training(
    training_id: int,
    training: TrainingCreate,
    db: Session = Depends(get_db)
):
    return update_training(db, training_id, training)


@router.delete("/{training_id}")
def remove_training(
    training_id: int,
    db: Session = Depends(get_db)
):
    return delete_training(db, training_id)