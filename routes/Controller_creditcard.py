from fastapi import APIRouter, HTTPException, status
from config.db_dependency import db_dependency
#importar las clase
from models.creditcard import Card
from schemas.creditcard import CardS

card=APIRouter()

@card.post("/creditcard/", status_code=status.HTTP_201_CREATED, tags=["CreditCard"])
async def crear_creditcard(card:Card, db:db_dependency):
    db_card = CardS(**card.dict())

    db.add(db_card)
    db.commit()
    return {"message": "Credit card creado correctamente"}

@card.delete("/creditcard/{card_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["CreditCard"])
async def delete_creditcard(card_id: int, db: db_dependency):
    # Buscar el Credit card en la base de datos
    db_card = db.query(CardS).filter(CardS.id == card_id).first()
    
    # Si no se encuentra el Credit card, lanzar un error 404
    if not db_card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Credit card no encontrado")
    
    # Eliminar el Credit card de la base de datos
    db.delete(db_card)
    db.commit()
    
    # No se necesita devolver nada en una respuesta DELETE exitosa
    return {"message": "Post eliminado correctamente"}

@card.get("/listarcreditcards/", status_code=status.HTTP_200_OK, tags=["CreditCard"])
async def consultar_creditcards(db:db_dependency):
    Lcreditcard = db.query(CardS).all()
    return Lcreditcard


@card.get("/listarcreditcards/{id_user}", status_code=status.HTTP_200_OK, tags=["CreditCard"])
async def consultar_postID(id_user:int, db:db_dependency):
    Lcreditcards = db.query(CardS).filter(CardS.userid == id_user).all()
    if Lcreditcards is None:
        raise HTTPException(status_code=404, detail="Credit Card no encontrado")
    return Lcreditcards


@card.put("/creditcard/{card_id}", status_code=status.HTTP_200_OK, tags=["CreditCard"])
async def actualizar_post(card_id: int, nuevo: Card, db:db_dependency):
    # Buscar el Credit card por ID
    db_card = db.query(CardS).filter(CardS.id == card_id).first()

    if not db_card:
        raise HTTPException(status_code=404, detail="Credit Card no encontrado")

    # Actualizar los campos del post
    for key, value in nuevo.dict().items():
        setattr(db_card, key, value)

    # Commit a la base de datos
    db.commit()

    return {"message": "Credit Card actualizado correctamente"}