from sqlalchemy import Column, Integer, String, Boolean
from app.models.user import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    puesto = Column(String(100), nullable=False)
    sector_id = Column(Integer, nullable=True)
    activo = Column(Boolean, default=True)
