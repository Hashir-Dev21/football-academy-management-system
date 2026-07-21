from pydantic import BaseModel

class PlayerCreate(BaseModel):
    full_name: str
    age: int
    position: str
    academy_id: int