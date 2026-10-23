from pydantic import BaseModel


class TemplateCreate(BaseModel):
    nombre: str
    codigo: str