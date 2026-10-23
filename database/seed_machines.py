from database.connection import SessionLocal
from app.models.machine import Machine

db = SessionLocal()

machines = [

    # Armado de Válvulas
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
    ("57", 5),
    ("61", 5),

    # Colocación de Sleeve
    ("69", 6),
    ("71", 6),
    ("119", 6),

    # Colocación de Arandelas
    ("65", 7),
    ("73", 7),

    # Armado de Pulsadores Mach
    ("66", 8),

    # Vástagos Inyectados
    ("20", 9),
    ("8", 9),
    ("19", 9),
    ("16", 9),
    ("4", 9),

    # Tapas Inyectadas
    ("14", 10),
    ("28", 10),
    ("30", 10),

    # Domos Inyectados
    ("84", 11),
    ("87", 11),
    ("89", 11),
    ("83", 11),

    # Extrusión
    ("31", 12),
    ("98", 12),
    ("36", 12),

    # Insertos Inyectados
    ("3", 13),
    ("13", 13),

    # Mach Inyectados
    ("30", 14),
    ("15", 14),

    # Armado de Kosmos
    ("68", 15),
    ("72", 15),

    # Armado de Pulsadores Labrador y Kosmos
    ("78", 16),
]

for numero, process_id in machines:
    db.add(
        Machine(
            numero=numero,
            process_id=process_id
        )
    )

db.commit()

print("Maquinas cargadas correctamente")