from pydantic import BaseModel


class AcademyCreate(BaseModel):
    academy_name: str
    city: str
    contact: str

class PlayerUpdate(BaseModel):
    full_name: str
    age: int
    position: str
    academy_id: int
