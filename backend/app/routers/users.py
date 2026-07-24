from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.users import UserCreate
from app.crud.users import create_user, get_users

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/")
def all_users(db: Session = Depends(get_db)):
    return get_users(db)