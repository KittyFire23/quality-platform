from fastapi import APIRouter
from database.connection import SessionLocal
from app.models.question import Question
from app.schemas.question_schema import QuestionCreate

router = APIRouter()


@router.get("/")
def get_questions():
    db = SessionLocal()

    questions = db.query(Question).all()

    return [
        {
            "id": question.id,
            "template_id": question.template_id,
            "texto": question.texto,
            "orden": question.orden,
            "activo": question.activo
        }
        for question in questions
    ]


@router.post("/")
def create_question(question: QuestionCreate):
    db = SessionLocal()

    new_question = Question(
        template_id=question.template_id,
        texto=question.texto,
        orden=question.orden
    )

    db.add(new_question)
    db.commit()
    db.refresh(new_question)

    return {
        "id": new_question.id,
        "template_id": new_question.template_id,
        "texto": new_question.texto,
        "orden": new_question.orden
    }