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
from app.schemas.watchlist_schema import WatchlistCreate
from app.schemas.watchlist_schema import WatchlistResponse

# --- Obtener conexion con la BD ---
from app.database.dependencies import get_db

# --- Obtener Metodos de Watchlist ---
from app.services.watchlist_service import WatchlistService

# --- Obtener funcion para verificar JWT ---
from app.core.security import verify_token



# --- Crear Router ---
router = APIRouter(
    prefix="/watchlist",
    tags=["Watchlist"]
)

# -------------------------------------------
# RUTA PARA AGREGAR PELICULAS A WATCHLIST
# -------------------------------------------
@router.post("",response_model=WatchlistResponse)
def add_to_watchlist(
    watchlist_data: WatchlistCreate,
    user_id: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    return WatchlistService.add_movie_to_watchlist(
        db,
        int(user_id),
        watchlist_data.movie_id
    )


# -------------------------------------------
# RUTA PARA OBTENER WATCHLIST
# -------------------------------------------
@router.get("",response_model=list[WatchlistResponse])
def get_watchlist(
    user_id: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    return WatchlistService.get_watchlist(
        db,
        int(user_id)
    )

# -------------------------------------------
# RUTA PARA ELIMINAR UNA PELICULA POR SU ID
# -------------------------------------------
@router.delete("/{movie_id}")
def remove_from_watchlist(
    movie_id: int,
    user_id: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    return WatchlistService.remove_movie_from_watchlist(
        db,
        int(user_id),
        movie_id
    )

