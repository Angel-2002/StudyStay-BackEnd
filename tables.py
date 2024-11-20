from database import engine
from schemas.user import Base
from schemas.university import Base
from schemas.post import Base
from schemas.reservation import Base
from schemas.creditcard import Base

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)