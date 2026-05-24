# ====================================
# MODULO DE LOGICA DEL HISTORIAL
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

# --- Importar Herramietas de acceso a la BD ---
from app.repositories.history_repository import HistoryRepository


# ----------------------------------
# SERVICIOS DE HISTORIAL
# ----------------------------------
class HistoryService:

    # --- Registrar pelicula al historial ---
    @staticmethod
    def add_history(
        db: Session,
        user_id: int,
        movie_id: int
    ):

        # --- Intentar conectar con catalog_service ---
        try:
            
            # --- Verificar si la pelicula existe ---
            response = httpx.get(
                f"http://catalog_service:8000/catalog/movies/{movie_id}"
            )

            # --- Si no existe ---
            if response.status_code != 200:
                
                # --- Devovler error 404 ---
                raise HTTPException(
                    status_code=404,
                    detail="Movie not found"
                )

        # --- Manejar errores de conexion ---
        except Exception:
            
            # --- Devolver error 500 ---
            raise HTTPException(
                status_code=500,
                detail="Catalog service unavailable"
            )

        # --- Registrar pelicula en el historial ---
        return HistoryRepository.create_history(
            db,
            user_id,
            movie_id
        )


    # --- Obtener historial del usuario ---
    @staticmethod
    def get_history(
        db: Session,
        user_id: int
    ):

        # --- Retornar historial ---
        return HistoryRepository.get_user_history(
            db,
            user_id
        )
    

    # --- Eliminar registro del historial ---
    @staticmethod
    def delete_history(
        db: Session,
        user_id: int,
        history_id: int
    ):

        # --- Buscar historial por ID en la BD---
        history = HistoryRepository.get_history_by_id(
            db,
            history_id
        )

        # --- Si no existe ---
        if not history:

            # --- Devolver error 404 ---
            raise HTTPException(
                status_code=404,
                detail="History not found"
            )

        # --- Verificar propietario por el ID ---
        if history.user_id != user_id: # Si quien quiere eliminar el historial no es el propietario.
            
            # --- Devolver error 403 de permiso ---
            raise HTTPException(
                status_code=403,
                detail="Forbidden"
            )

        # --- Eliminar historial ---
        HistoryRepository.delete_history(
            db,
            history
        )

        # --- Retornar exito de la operacion ---
        return {
            "message": "History deleted"
        }


