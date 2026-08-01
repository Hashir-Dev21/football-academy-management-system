from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.attendance import AttendanceCreate
from app.crud.attendance import (
    create_attendance,
    get_attendance,
    get_player_attendance_summary
)

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

@router.post("/")
def add_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):
    return create_attendance(db, attendance)


@router.get("/")
def all_attendance(
    db: Session = Depends(get_db)
):
    return get_attendance(db)


@router.get("/player/{player_id}")
def attendance_summary(
    player_id: int,
    db: Session = Depends(get_db)
):
    return get_player_attendance_summary(db, player_id)