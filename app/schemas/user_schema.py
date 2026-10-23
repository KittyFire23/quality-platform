from pydantic import BaseModel


class UserCreate(BaseModel):
    nombre: str
    email: str
    rol: str