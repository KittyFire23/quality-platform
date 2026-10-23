from database.connection import SessionLocal
from app.models.machine import Machine

db = SessionLocal()

machines = [

    # Armado de Valvulas
    ("41", 2),
    ("139", 2),
    ("38", 2),
    ("140", 2),
    ("43", 2),

    # Prearmado
    ("51", 3),
    ("52", 3),
    ("53", 3),
    ("54", 3),

    # Cuerpos Inyectados
    ("17", 4),
    ("18", 4),
    ("11", 4),
    ("10", 4),

    # Estampado
    ("57", 6),
    ("61", 6),

    # Colocacion de Sleeve
    ("69", 7),
    ("71", 7),
    ("119", 7),

    # Colocacion de Arandelas
    ("65", 8),
    ("73", 8),

    # Armado de Pulsadores Mach
    ("66", 9),

    # Tapas Inyectadas
    ("14", 11),
    ("28", 11),
    ("30", 11),

    # Domos Inyectados
    ("84", 12),
    ("87", 12),
    ("89", 12),
    ("83", 12),

    # Extrusion
    ("31", 13),
    ("98", 13),
    ("36", 13),

    # Insertos Inyectados
    ("3", 14),
    ("13", 14),

    # Mach Inyectados
    ("30", 15),
    ("15", 15),

    # Armado de Kosmos
    ("68", 16),
    ("72", 16),

    # Armado de Pulsadores Labrador y Kosmos
    ("78", 17),

    # Vastagos Inyectados
    ("20", 18),
    ("8", 18),
    ("19", 18),
    ("16", 18),
    ("4", 18),
]

for numero, process_id in machines:

    existing = db.query(Machine).filter(
        Machine.numero == numero,
        Machine.process_id == process_id
    ).first()

    if not existing:
        db.add(
            Machine(
                numero=numero,
                process_id=process_id
            )
        )

db.commit()

print("Maquinas cargadas correctamente")
