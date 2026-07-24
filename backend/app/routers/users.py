from app.security.jwt_handler import create_access_token
from app.schemas.auth import LoginRequest
from app.crud.users import authenticate_user
from fastapi import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.users import UserCreate
from app.crud.users import create_user, get_users

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/login")
def login(user: LoginRequest, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={"sub": db_user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }