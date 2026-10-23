from fastapi import APIRouter
from database.connection import SessionLocal
from app.models.process import Process
from app.schemas.process_schema import ProcessCreate

router = APIRouter()


@router.get("/")
def get_processes():
    db = SessionLocal()

    processes = db.query(Process).all()

    return [
        {
            "id": process.id,
            "nombre": process.nombre,
            "descripcion": process.descripcion,
            "activo": process.activo
        }
        for process in processes
    ]


@router.post("/")
def create_process(process: ProcessCreate):
    db = SessionLocal()

    new_process = Process(
        nombre=process.nombre,
        descripcion=process.descripcion
    )

    db.add(new_process)
    db.commit()
    db.refresh(new_process)

    return {
        "id": new_process.id,
        "nombre": new_process.nombre,
        "descripcion": new_process.descripcion
    }