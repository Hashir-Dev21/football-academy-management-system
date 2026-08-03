from pydantic import BaseModel


class CoachCreate(BaseModel):
    full_name: str
    age: int
    specialization: str
    experience: int
    phone: str
    academy_id: int


class CoachResponse(BaseModel):
    id: int
    full_name: str
    age: int
    specialization: str
    experience: int
    phone: str
    academy_id: int

    class Config:
        from_attributes = True