from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.academies import AcademyCreate
from app.crud.academies import create_academy, get_academies

router = APIRouter(
    prefix="/academies",
    tags=["Academies"]
)


@router.post("/")
def add_academy(academy: AcademyCreate, db: Session = Depends(get_db)):
    return create_academy(db, academy)
@router.get("/")
def all_academies(db: Session = Depends(get_db)):
    return get_academies(db)