from fastapi import APIRouter, HTTPException, status
from config.db_dependency import db_dependency
#importar las clase
from models.reservation import Reservation
from schemas.reservation import ReservationS

reservation=APIRouter()

@reservation.post("/reservation/", status_code=status.HTTP_201_CREATED, tags=["Reservation"])
async def crear_reservation(reservation:Reservation, db:db_dependency):
    db_reservation = ReservationS(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    return {"message": "Reservacion creada correctamente"}


@reservation.get("/listarreservation/", status_code=status.HTTP_200_OK, tags=["Reservation"])
async def consultar_reservations(db:db_dependency):
    reservations = db.query(ReservationS).all()
    return reservations


@reservation.get("/listarreservation/{id_reservation}", status_code=status.HTTP_200_OK, tags=["Reservation"])
async def consultar_reservationID(id_reservation:int, db:db_dependency):
    reservation = db.query(ReservationS).filter(ReservationS.id == id_reservation).first()
    if reservation is None:
        raise HTTPException(status_code=404, detail="Reservacion no encontrada")
    return reservation


@reservation.put("/reservation/{reservation_id}", status_code=status.HTTP_200_OK, tags=["Reservation"])
async def actualizar_reservation(reservation_id: int, nuevo: Reservation, db:db_dependency):
    # Buscar la reservation por ID
    db_reservation = db.query(ReservationS).filter(ReservationS.id == reservation_id).first()

    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservacion no encontrada")

    # Actualizar los campos de la reservation
    for key, value in nuevo.dict().items():
        setattr(db_reservation, key, value)

    # Commit a la base de datos
    db.commit()

    return {"message": "Reservacion actualizada correctamente"}