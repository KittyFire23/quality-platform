from pydantic import BaseModel


class SectorCreate(BaseModel):
    nombre: str