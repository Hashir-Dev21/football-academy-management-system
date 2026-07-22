from sqlalchemy.orm import Session
from app.database.models import Academy
from app.schemas.academies import AcademyCreate


def create_academy(db: Session, academy: AcademyCreate):
    db_academy = Academy(
        academy_name=academy.academy_name,
        city=academy.city,
        contact=academy.contact
    )

    db.add(db_academy)
    db.commit()
    db.refresh(db_academy)

    return db_academy
def get_academies(db: Session):
    return db.query(Academy).all()