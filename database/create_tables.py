from database.connection import engine
from database.base import Base

Base.metadata.create_all(bind=engine)

print("Tablas creadas correctamente")