from pydantic import BaseModel


class TeamCreate(BaseModel):
    team_name: str
    age_group: str
    academy_id: int


class TeamResponse(TeamCreate):
    id: int

    model_config = {
        "from_attributes": True
    }