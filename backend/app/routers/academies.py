from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.academies import AcademyCreate, AcademyUpdate
from app.crud.academies import (
    create_academy,
    get_academies,
    update_academy,
    delete_academy
)

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

@router.put("/{academy_id}")
def edit_academy(
    academy_id: int,
    academy: AcademyUpdate,
    db: Session = Depends(get_db)
):
    return update_academy(db, academy_id, academy)

@router.delete("/{academy_id}")
def remove_academy(
    academy_id: int,
    db: Session = Depends(get_db)
):
    return delete_academy(db, academy_id)