# ===================================
# Importaciones Y Librerias
# ===================================

# --- Obtener Framework ---
from fastapi import FastAPI 

# --- Traer Base ORM y engine (puente) ---
from auth_service.app.database.connection import engine
from auth_service.app.database.base import Base

# --- Registrar modelo ORM User en metadata ---
from auth_service.app.models.user_model import User # Python ejecuta el archivo al importarlo. 

from auth_service.app.routes.auth_routes import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- Incluir router a app ---
app.include_router(auth_router)

# Ruta Inicial de prueba
@app.get("/")
def root():
    return {
        "message": "Auth Service Running"
    }