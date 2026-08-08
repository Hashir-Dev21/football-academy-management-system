from pydantic import BaseModel


class MatchCreate(BaseModel):
    home_team_id: int
    away_team_id: int
    match_date: str
    match_time: str
    venue: str
    home_score: int = 0
    away_score: int = 0
    status: str = "Scheduled"


class MatchResponse(MatchCreate):
    id: int

    model_config = {
        "from_attributes": True
    }