from fastapi import APIRouter
from database.connection import SessionLocal
from app.models.employee import Employee
from app.schemas.employee_schema import EmployeeCreate

router = APIRouter()


@router.get("/")
def get_employees():
    db = SessionLocal()

    employees = db.query(Employee).all()

    return [
        {
            "id": employee.id,
            "nombre": employee.nombre,
            "puesto": employee.puesto,
            "activo": employee.activo
        }
        for employee in employees
    ]


@router.post("/")
def create_employee(employee: EmployeeCreate):
    db = SessionLocal()

    new_employee = Employee(
    nombre=employee.nombre,
    puesto=employee.puesto,
    sector_id=employee.sector_id
)

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return {
    "id": new_employee.id,
    "nombre": new_employee.nombre,
    "puesto": new_employee.puesto,
    "sector_id": new_employee.sector_id
}