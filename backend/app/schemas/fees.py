from pydantic import BaseModel

class FeeCreate(BaseModel):
    player_id: int
    month: str
    amount: float
    due_date: str