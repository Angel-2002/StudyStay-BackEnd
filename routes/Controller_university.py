from fastapi import APIRouter, HTTPException, status
from config.db_dependency import db_dependency
#importar las clase
from models.university import University
from schemas.university import UniversityS

university=APIRouter()

@university.post("/university/", status_code=status.HTTP_201_CREATED, tags=["University"])
async def crear_university(university:University, db:db_dependency):
    db_university = UniversityS(**university.dict())
    db.add(db_university)
    db.commit()
    return {"message": "Universidad creada correctamente"}


@university.get("/listaruniversities/", status_code=status.HTTP_200_OK, tags=["University"])
async def consultar_universities(db:db_dependency):
    universities = db.query(UniversityS).all()
    return universities


@university.get("/listaruniversity/{id_university}", status_code=status.HTTP_200_OK, tags=["University"])
async def consultar_universityID(id_university:int, db:db_dependency):
    university = db.query(UniversityS).filter(UniversityS.id == id_university).first()
    if university is None:
        raise HTTPException(status_code=404, detail="Universidad no encontrada")
    return university


@university.put("/university/{university_id}", status_code=status.HTTP_200_OK, tags=["University"])
async def actualizar_registro(university_id: int, nuevo: University, db:db_dependency):
    # Buscar el university por ID
    db_university = db.query(UniversityS).filter(UniversityS.id == university_id).first()

    if not db_university:
        raise HTTPException(status_code=404, detail="Universidad no encontrada")

    # Actualizar los campos de la university
    for key, value in nuevo.dict().items():
        setattr(db_university, key, value)

    # Commit a la base de datos
    db.commit()

    return {"message": "Universidad actualizada correctamente"}