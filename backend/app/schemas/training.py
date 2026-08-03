from datetime import date
from pydantic import BaseModel


class TrainingCreate(BaseModel):
    title: str
    training_date: date
    training_time: str
    location: str
    coach_id: int


class TrainingResponse(BaseModel):
    id: int
    title: str
    training_date: date
    training_time: str
    location: str
    coach_id: int

    class Config:
        from_attributes = True