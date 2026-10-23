from pydantic import BaseModel


class MachineCreate(BaseModel):
    numero: str
    process_id: int