from fastapi import APIRouter, HTTPException, status
from config.db_dependency import db_dependency
import bcrypt
#importar las clase
from models.user import User
from schemas.user import UserS

user=APIRouter()

@user.post("/usuario/", status_code=status.HTTP_201_CREATED, tags=["User"])
async def crear_usuario(usuario:User, db:db_dependency):
    db_usuario = UserS(**usuario.dict())

    # Hasheo de la contraseña
    psswrd = usuario.password
    hash = psswrd.encode('utf-8')
    sal = bcrypt.gensalt()
    encript = bcrypt.hashpw(hash,sal)

    # Convertir bytes a string
    db_usuario.password = encript.decode('utf-8')

    db.add(db_usuario)
    db.commit()
    return {"message": "User creado correctamente"}


@user.get("/listarusuarios/", status_code=status.HTTP_200_OK, tags=["User"])
async def consultar_usuarios(db:db_dependency):
    usuarios = db.query(UserS).all()
    return usuarios


@user.get("/listarusuario/{id_usuario}", status_code=status.HTTP_200_OK, tags=["User"])
async def consultar_usuarioID(id_usuario:int, db:db_dependency):
    usuario = db.query(UserS).filter(UserS.id == id_usuario).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="User no encontrado")
    return usuario


@user.get("/verificarusu/{email}/{password}", status_code=status.HTTP_200_OK, tags=["User"])
async def consultar_usuarioID(email:str, password:str, db:db_dependency):
    usuario = db.query(UserS).filter(UserS.email == email).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="${password}")
    
    if not bcrypt.checkpw(password.encode('utf-8'), usuario.password.encode('utf-8')):
        raise HTTPException(status_code=404, detail="${password}")

    return usuario


@user.put("/usuario/{usuario_id}", status_code=status.HTTP_200_OK, tags=["User"])
async def actualizar_registro(usuario_id: int, nuevo: User, db:db_dependency):
    # Buscar el User por ID
    db_registro = db.query(UserS).filter(UserS.id == usuario_id).first()

    if not db_registro:
        raise HTTPException(status_code=404, detail="User no encontrado")

    # Actualizar los campos del User
    for key, value in nuevo.dict().items():
        setattr(db_registro, key, value)

    # Commit a la base de datos
    db.commit()

    return db_registro