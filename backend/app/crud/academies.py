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

def update_academy(db: Session, academy_id: int, academy):
    db_academy = db.query(Academy).filter(Academy.id == academy_id).first()

    if db_academy:
        db_academy.academy_name = academy.academy_name
        db_academy.city = academy.city
        db_academy.contact = academy.contact

        db.commit()
        db.refresh(db_academy)

        return db_academy

    return {"message": "Academy not found"}

def delete_academy(db: Session, academy_id: int):
    academy = db.query(Academy).filter(Academy.id == academy_id).first()

    if not academy:
        return {"message": "Academy not found"}

    if academy.players:
        return {
            "message": "Cannot delete academy. Players are assigned to this academy."
        }

    db.delete(academy)
    db.commit()

    return {"message": "Academy deleted successfully"}