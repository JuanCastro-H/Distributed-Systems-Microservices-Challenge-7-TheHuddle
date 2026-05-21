# ===================================
# Importaciones Y Librerias
# ===================================

# --- Obtener Framework ---
from fastapi import FastAPI

from auth_service.app.database.connection import engine
from auth_service.app.database.base import Base

from auth_service.app.models.user_model import User


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Ruta Inicial de prueba
@app.get("/")
def root():
    return {
        "message": "Auth Service Running"
    }