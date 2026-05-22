# ===================================
# Importaciones Y Librerias
# ===================================

# --- Obtener Framework ---
from fastapi import FastAPI

# --- Traer Base ORM y engine (puente) ---
from app.database.base import Base
from app.database.connection import engine

# --- Registrar modelo ORM en metadata ---
from app.models.watchlist_model import Watchlist

# --- Importar router ---
from app.routes.watchlist_routes import router as watchlist_router

# --- Crear tablas registradas en metadata ---
Base.metadata.create_all(bind=engine)

# --- Iniciar Instacia de FastAPI ---
app = FastAPI()

# --- Incluir router a app ---
app.include_router(watchlist_router)

# Ruta Inicial de prueba
@app.get("/")
def root():

    return {
        "message": "Watchlist Service Running"
    }