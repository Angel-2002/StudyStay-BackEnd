from fastapi import APIRouter, HTTPException, status
from config.db_dependency import db_dependency
#importar las clase
from models.alumno import Alumno
from schemas.alumno import AlumnoS

user=APIRouter()

@user.post("/usuario/", status_code=status.HTTP_201_CREATED)
async def crear_usuario(usuario:Alumno, db:db_dependency):
    db_usuario = AlumnoS(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    return {"message": "Registro creado correctamente"}


@user.get("/listarusuarios/", status_code=status.HTTP_200_OK)
async def consultar_usuarios(db:db_dependency):
    usuarios = db.query(AlumnoS).all()
    return usuarios


@user.get("/listarusuario/{id_usuario}", status_code=status.HTTP_200_OK)
async def consultar_usuarioID(id_usuario:int, db:db_dependency):
    usuario = db.query(AlumnoS).filter(AlumnoS.id == id_usuario).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return usuario


@user.put("/usuario/{usuario_id}", status_code=status.HTTP_200_OK)
async def actualizar_registro(usuario_id: int, nuevo: Alumno, db:db_dependency):
    # Buscar el registro por ID
    db_registro = db.query(AlumnoS).filter(AlumnoS.id == usuario_id).first()

    if not db_registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    # Actualizar los campos del registro
    for key, value in nuevo.dict().items():
        setattr(db_registro, key, value)

    # Commit a la base de datos
    db.commit()

    return {"message": "Registro actualizado correctamente"}