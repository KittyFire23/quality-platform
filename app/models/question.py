from sqlalchemy import Column, Integer, String, Boolean
from app.models.user import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer, nullable=False)

    texto = Column(String(500), nullable=False)

    tipo = Column(String(50), nullable=False)

    orden = Column(Integer, nullable=False)

    activo = Column(Boolean, default=True)