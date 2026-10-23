from sqlalchemy import Column, Integer, String, Boolean
from app.models.user import Base


class Process(Base):
    __tablename__ = "processes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(String(255))
    activo = Column(Boolean, default=True)