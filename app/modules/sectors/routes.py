from fastapi import APIRouter
from database.connection import SessionLocal
from app.models.sector import Sector
from app.schemas.sector_schema import SectorCreate

router = APIRouter()


@router.get("/")
def get_sectors():
    db = SessionLocal()

    sectors = db.query(Sector).all()

    return [
        {
            "id": sector.id,
            "nombre": sector.nombre,
            "activo": sector.activo
        }
        for sector in sectors
    ]


@router.post("/")
def create_sector(sector: SectorCreate):
    db = SessionLocal()

    new_sector = Sector(
        nombre=sector.nombre
    )

    db.add(new_sector)
    db.commit()
    db.refresh(new_sector)

    return {
        "id": new_sector.id,
        "nombre": new_sector.nombre
    }