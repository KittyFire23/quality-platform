from pydantic import BaseModel


class QuestionCreate(BaseModel):
    template_id: int
    texto: str
    orden: int