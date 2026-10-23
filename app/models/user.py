from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Boolean


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    rol = Column(String(50), nullable=False)
    activo = Column(Boolean, default=True)