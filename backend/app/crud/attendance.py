from sqlalchemy.orm import Session
from app.database.models import Attendance
from app.schemas.attendance import AttendanceCreate


def create_attendance(db: Session, attendance: AttendanceCreate):
    new_attendance = Attendance(**attendance.model_dump())

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return new_attendance


def get_attendance(db: Session):
    return db.query(Attendance).all()

def get_player_attendance_summary(db: Session, player_id: int):

    total_days = db.query(Attendance).filter(
        Attendance.player_id == player_id
    ).count()

    present = db.query(Attendance).filter(
        Attendance.player_id == player_id,
        Attendance.status == "Present"
    ).count()

    absent = db.query(Attendance).filter(
        Attendance.player_id == player_id,
        Attendance.status == "Absent"
    ).count()

    percentage = 0

    if total_days > 0:
        percentage = round((present / total_days) * 100, 2)

    return {
        "player_id": player_id,
        "total_days": total_days,
        "present": present,
        "absent": absent,
        "attendance_percentage": percentage
    }