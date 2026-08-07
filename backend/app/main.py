from app.routers.team import router as team_router
from app.routers.training import router as training_router
from app.routers.coach import router as coach_router
from app.routers.attendance import router as attendance_router
from app.routers.dashboard import router as dashboard_router
from app.routers.fees import router as fee_router
from fastapi import FastAPI

from app.database.connection import engine
from app.database.models import Base

from app.routers.players import router as player_router
from app.routers.academies import router as academy_router
from app.routers.users import router as user_router


app = FastAPI(
    title="Football Academy Management System API",
    description="AI Powered Football Academy Management System",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Welcome to Football Academy Management System API"
    }


app.include_router(player_router)
app.include_router(academy_router)
app.include_router(user_router)
app.include_router(fee_router)
app.include_router(dashboard_router)
app.include_router(attendance_router)
app.include_router(coach_router)
app.include_router(training_router)
app.include_router(team_router)