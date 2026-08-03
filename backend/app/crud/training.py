from sqlalchemy.orm import Session

from app.database.models import Training
from app.schemas.training import TrainingCreate


def create_training(db: Session, training: TrainingCreate):

    new_training = Training(**training.model_dump())

    db.add(new_training)
    db.commit()
    db.refresh(new_training)

    return new_training


def get_trainings(db: Session):

    return db.query(Training).all()


def get_training(db: Session, training_id: int):

    return db.query(Training).filter(
        Training.id == training_id
    ).first()


def update_training(
    db: Session,
    training_id: int,
    training_data: TrainingCreate
):

    training = db.query(Training).filter(
        Training.id == training_id
    ).first()

    if not training:
        return None

    for key, value in training_data.model_dump().items():
        setattr(training, key, value)

    db.commit()
    db.refresh(training)

    return training


def delete_training(db: Session, training_id: int):

    training = db.query(Training).filter(
        Training.id == training_id
    ).first()

    if not training:
        return None

    db.delete(training)
    db.commit()

    return {
        "message": "Training deleted successfully"
    }