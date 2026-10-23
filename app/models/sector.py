from sqlalchemy import Column, Integer, String, Boolean
from app.models.user import Base


class Sector(Base):
    __tablename__ = "sectors"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)
    activo = Column(Boolean, default=True)