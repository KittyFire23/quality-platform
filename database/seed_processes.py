from database.connection import SessionLocal
from app.models.process import Process

db = SessionLocal()

processes = [

    # Armado
    ("Armado de Valvulas", "Proceso de armado"),
    ("Prearmado", "Proceso de armado"),
    ("Estampado", "Proceso de armado"),
    ("Colocacion de Sleeve", "Proceso de armado"),
    ("Colocacion de Arandelas", "Proceso de armado"),
    ("Armado de Pulsadores Mach", "Proceso de armado"),

    # Inyeccion
    ("Vastagos Inyectados", "Proceso de inyeccion"),
    ("Cuerpos Inyectados", "Proceso de inyeccion"),
    ("Tapas Inyectadas", "Proceso de inyeccion"),
    ("Domos Inyectados", "Proceso de inyeccion"),
    ("Extrusion", "Proceso de inyeccion"),
    ("Insertos Inyectados", "Proceso de inyeccion"),
    ("Mach Inyectados", "Proceso de inyeccion"),
    ("Armado de Kosmos", "Proceso de inyeccion"),
    ("Armado de Pulsadores Labrador y Kosmos", "Proceso de inyeccion"),
]

for nombre, descripcion in processes:

    existing = db.query(Process).filter(
        Process.nombre == nombre
    ).first()

    if not existing:
        db.add(
            Process(
                nombre=nombre,
                descripcion=descripcion
            )
        )

db.commit()

print("Procesos cargados correctamente")