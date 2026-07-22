from pydantic import BaseModel


class AcademyCreate(BaseModel):
    academy_name: str
    city: str
    contact: str