from fastapi import APIRouter
from database.connection import SessionLocal
from app.models.user import User
from app.schemas.user_schema import UserCreate

router = APIRouter()


@router.get("/")
def get_users():
    db = SessionLocal()

    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "nombre": user.nombre,
            "email": user.email,
            "rol": user.rol,
            "activo": user.activo
        }
        for user in users
    ]

@router.post("/")
def create_user(user: UserCreate):
    db = SessionLocal()

    new_user = User(
        nombre=user.nombre,
        email=user.email,
        rol=user.rol
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "nombre": new_user.nombre,
        "email": new_user.email,
        "rol": new_user.rol
    }