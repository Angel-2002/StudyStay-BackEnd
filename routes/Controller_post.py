from fastapi import APIRouter, HTTPException, status
from config.db_dependency import db_dependency
#importar las clase
from models.post import Post
from schemas.post import PostS

post=APIRouter()

@post.post("/post/", status_code=status.HTTP_201_CREATED, tags=["Post"])
async def crear_post(post:Post, db:db_dependency):
    db_post = PostS(**post.dict())
    db.add(db_post)
    db.commit()
    return {"message": "Post creado correctamente"}


@post.get("/listarposts/", status_code=status.HTTP_200_OK, tags=["Post"])
async def consultar_posts(db:db_dependency):
    posts = db.query(PostS).all()
    return posts


@post.get("/listarpost/{id_post}", status_code=status.HTTP_200_OK, tags=["Post"])
async def consultar_postID(id_post:int, db:db_dependency):
    post = db.query(PostS).filter(PostS.id == id_post).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return post


@post.put("/post/{post_id}", status_code=status.HTTP_200_OK, tags=["Post"])
async def actualizar_post(post_id: int, nuevo: Post, db:db_dependency):
    # Buscar el post por ID
    db_post = db.query(PostS).filter(PostS.id == post_id).first()

    if not db_post:
        raise HTTPException(status_code=404, detail="Post no encontrado")

    # Actualizar los campos del post
    for key, value in nuevo.dict().items():
        setattr(db_post, key, value)

    # Commit a la base de datos
    db.commit()

    return {"message": "Post actualizado correctamente"}