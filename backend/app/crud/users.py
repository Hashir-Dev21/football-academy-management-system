from sqlalchemy.orm import Session
from app.database.models import User
from app.schemas.users import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        academy_id=user.academy_id
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_users(db: Session):
    return db.query(User).all()