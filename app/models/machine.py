from sqlalchemy import Column, Integer, String, Boolean
from app.models.user import Base


class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String(20), nullable=False)
    process_id = Column(Integer, nullable=True)
    activo = Column(Boolean, default=True)