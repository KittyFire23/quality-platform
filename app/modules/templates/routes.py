from fastapi import APIRouter
from database.connection import SessionLocal
from app.models.template import Template
from app.schemas.template_schema import TemplateCreate

router = APIRouter()


@router.get("/")
def get_templates():
    db = SessionLocal()

    templates = db.query(Template).all()

    return [
        {
            "id": template.id,
            "nombre": template.nombre,
            "codigo": template.codigo,
            "activo": template.activo
        }
        for template in templates
    ]


@router.post("/")
def create_template(template: TemplateCreate):
    db = SessionLocal()

    new_template = Template(
        nombre=template.nombre,
        codigo=template.codigo
    )

    db.add(new_template)
    db.commit()
    db.refresh(new_template)

    return {
        "id": new_template.id,
        "nombre": new_template.nombre,
        "codigo": new_template.codigo
    }