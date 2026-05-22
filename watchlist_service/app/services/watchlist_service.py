# ====================================
# MODULO DE LOGICA DE WAATCHLIST
# ====================================

# ===================================
# Importaciones Y Librerias
# ===================================

# --- Realizar peticiones HTTP entre microservicios ---
import httpx

# --- Obtener herramientas para manejar excepciones ---
from fastapi import HTTPException

# --- Obtener Session activa SQL ---
from sqlalchemy.orm import Session

#  --- Importar Herramientas de acceso a BD ---
from app.repositories.watchlist_repository import WatchlistRepository



# ----------------------------------
# SERVICIOS DE WATCHLIST
# ----------------------------------
class WatchlistService:

    # --- Agregar pelicula al Watchlist ---
    @staticmethod # Permite usar el metodo sin crear un objeto.
    def add_movie_to_watchlist(
        db: Session,                # Conexion con la BD.
        user_id: int,               # ID usuario autenticado.
        movie_id: int               # ID pelicula a agregar.
    ):

        # --- Buscar pelicula por ID ---
        try:

            # --- Buscar pelicula ---
            response = httpx.get(
                f"http://catalog_service:8000/catalog/movies/{movie_id}"
            )
            
            # --- Si no Existe Devolver error ---
            if response.status_code != 200:

                raise HTTPException(
                    status_code=404,
                    detail="Movie not found"
                )

        # --- Manejar errores ---
        except Exception: 

            raise HTTPException(
                status_code=500,
                detail="Catalog service unavailable"
            )

        # --- Retornar 
        return WatchlistRepository.create_watchlist_item(
            db,
            user_id,
            movie_id
        )


    # --- Obtener Watchlist del usuario ---
    @staticmethod
    def get_watchlist(
        db: Session,
        user_id: int
    ):

        # --- Retornar Watchlist de Usuario ---
        return WatchlistRepository.get_user_watchlist(
            db,
            user_id
        )
    

    # --- Eliminar pelicula ---
    @staticmethod
    def remove_movie_from_watchlist(
        db: Session,
        user_id: int,
        movie_id: int
    ):

        # --- Obtener item ---
        watchlist_item = WatchlistRepository.get_watchlist_item(
            db,
            user_id,
            movie_id
        )

        # --- Si no se obtiene ---
        if not watchlist_item:

            raise HTTPException(
                status_code=404,
                detail="Movie not found in watchlist"
            )

        # --- Borrarlo ---
        WatchlistRepository.delete_watchlist_item(
            db,
            watchlist_item
        )

        # --- Retornar mensaje de remov ---
        return {
            "message": "Movie removed from watchlist"
        }