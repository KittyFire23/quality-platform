from pydantic import BaseModel


class ProcessCreate(BaseModel):
    nombre: str
    descripcion: str