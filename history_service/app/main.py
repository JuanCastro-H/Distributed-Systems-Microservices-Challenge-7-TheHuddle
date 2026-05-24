# ===================================
# Importaciones Y Librerias
# ===================================

# --- Obtener Framework ---
from fastapi import FastAPI

# --- Traer Base ORM y engine (puente) ---
from app.database.base import Base
from app.database.connection import engine

# --- Registrar modelo ORM en metadata ---
from app.models.history_model import History

# --- Importar router ---
from app.routes.history_routes import router as history_routes

# --- Crear tablas registradas en metadata ---
Base.metadata.create_all(bind=engine)

# --- Iniciar Instacia de FastAPI ---
app = FastAPI()

# --- Incluir router a app ---
app.include_router(history_routes)

# Ruta Inicial de prueba
@app.get("/")
def root():

    return {
        "message": "Watchlist Service Running"
    }