from fastapi import FastAPI
from app.database.connection import engine
from app.database.models import Base
from app.routers.players import router as player_router
from app.routers.academies import router as academy_router

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