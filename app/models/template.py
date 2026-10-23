from sqlalchemy import Column, Integer, String, Boolean
from app.models.user import Base


class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(50), nullable=False)
    activo = Column(Boolean, default=True)