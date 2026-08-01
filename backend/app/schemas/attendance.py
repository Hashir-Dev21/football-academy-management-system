from pydantic import BaseModel


class AttendanceCreate(BaseModel):
    player_id: int
    date: str
    status: str