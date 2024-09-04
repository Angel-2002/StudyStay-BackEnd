from database import engine
from schemas.alumno import Base
from schemas.university import Base
from schemas.post import Base

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)