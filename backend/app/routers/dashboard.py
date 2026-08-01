from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.crud.dashboard import (
    dashboard_stats,
    monthly_revenue,
    recent_payments,
    recent_players,
    recent_attendance
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def get_dashboard_stats(db: Session = Depends(get_db)):
    return dashboard_stats(db)


@router.get("/monthly-revenue")
def get_monthly_revenue(db: Session = Depends(get_db)):
    return monthly_revenue(db)


@router.get("/recent-payments")
def get_recent_payments(db: Session = Depends(get_db)):
    return recent_payments(db)


@router.get("/recent-players")
def get_recent_players(db: Session = Depends(get_db)):
    return recent_players(db)


@router.get("/recent-attendance")
def get_recent_attendance(db: Session = Depends(get_db)):
    return recent_attendance(db)