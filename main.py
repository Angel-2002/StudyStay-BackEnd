from fastapi import FastAPI
from database import engine
from tables import Base
from routes.Controller_user import user
from routes.Controller_university import university
from routes.Controller_post import post
from routes.Controller_reservation import reservation
from routes.Controller_creditcard import card

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(

    title="StudiStay API",
    description="Simple API made with FastAPI and MySQL",
    version="1.0.0"
)

# Configuración para permitir todas las solicitudes CORS (debes ajustar según tus necesidades)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas al iniciar la aplicación
@app.on_event("startup")
async def on_startup():
    Base.metadata.create_all(bind=engine)

#http://127.0.0.1:8000

app.include_router(user)
app.include_router(university)
app.include_router(post)
app.include_router(reservation)
app.include_router(card)