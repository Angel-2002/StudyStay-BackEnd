from fastapi import FastAPI
from database import engine
from tables import Base
from routes.Controller_alumno import user

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(

    title="StudiStay API",
    description="Simple API made with FastAPI and MySQL",
    version="0.0.1"
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