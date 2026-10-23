from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    nombre: str
    puesto: str
    sector_id: int