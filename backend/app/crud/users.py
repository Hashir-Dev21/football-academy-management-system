from app.security.password import verify_password
from app.security.password import hash_password
from sqlalchemy.orm import Session
from app.database.models import User
from app.schemas.users import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        academy_id=user.academy_id
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_users(db: Session):
    return db.query(User).all()

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user