from fastapi import APIRouter
from database.connection import SessionLocal
from app.models.machine import Machine
from app.schemas.machine_schema import MachineCreate

router = APIRouter()


@router.get("/")
def get_machines():
    db = SessionLocal()

    machines = db.query(Machine).all()

    return [
        {
            "id": machine.id,
            "numero": machine.numero,
            "activo": machine.activo
        }
        for machine in machines
    ]


@router.post("/")
def create_machine(machine: MachineCreate):
    db = SessionLocal()

    new_machine = Machine(
    numero=machine.numero,
    process_id=machine.process_id
)

    db.add(new_machine)
    db.commit()
    db.refresh(new_machine)

    return {
    "id": new_machine.id,
    "numero": new_machine.numero,
    "process_id": new_machine.process_id
}