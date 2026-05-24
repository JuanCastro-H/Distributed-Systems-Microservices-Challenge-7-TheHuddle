# ====================================
# MODULO DE RUTAS
# ====================================

# ============================
# Importaciones Y Librerias
# ============================

# --- Importar Rauter y obtener dependencias ---
from fastapi import APIRouter
from fastapi import Depends

# --- Obtener Session activa con la BD ---
from sqlalchemy.orm import Session

# --- Obtener Schemas de validacion y respuesta ---
from app.schemas.history_schema import HistoryCreate
from app.schemas.history_schema import HistoryResponse

# --- Obtener conexion con la BD ---
from app.database.dependencie import get_db

# --- Obtener Metodos de Watchlist ---
from app.services.history_service import HistoryService

# --- Obtener funcion para verificar JWT ---
from app.core.security import verify_token



# --- Crear Router ---
router = APIRouter(
    prefix="/history",
    tags=["History"]
)


# -------------------------------------------
# RUTA PARA AGREGAR UNA PELICULA AL HISTORIAL
# -------------------------------------------
@router.post("",response_model=HistoryResponse)
def add_history(
    history_data: HistoryCreate,
    user_id: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    # --- Registrar pelicula en historial ---
    return HistoryService.add_history(
        db,
        int(user_id),
        history_data.movie_id
    )


