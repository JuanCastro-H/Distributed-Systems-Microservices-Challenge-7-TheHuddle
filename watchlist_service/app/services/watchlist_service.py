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

        # --- Retornar pelicula en watchlist ---
        watchlist = WatchlistRepository.create_watchlist_item(
            db,
            user_id,
            movie_id
        )

        # --- Parsear json ---
        movie_data = response.json()

        # --- Retornar pelicula enriquecida ---
        return {
            "id": watchlist.id,
            "user_id": watchlist.user_id,
            "movie_id": watchlist.movie_id,
            "movie_title": movie_data["title"],
            "movie_genre": movie_data["genre"],
            "movie_rating": movie_data["rating"]
        }


    # --- Obtener Watchlist del usuario ---
    @staticmethod
    def get_watchlist(
        db: Session,
        user_id: int
    ):

        # --- Obtener peliculas guardadas ---
        watchlist_items = WatchlistRepository.get_user_watchlist(
            db,
            user_id
        )

        # --- Lista para almacenar watchlist enriquecida ---
        enriched_watchlist = []

        # --- Recorrer cada pelicula guardada ---
        for item in watchlist_items:
            
            # intentar Obtener informacion detallada de la pelicula ---
            try:
                
                # --- Solicitar la informacion a catalogo ---
                response = httpx.get(
                    f"http://catalog_service:8000/catalog/movies/{item.movie_id}"
                )  

                # --- Parsear json ---
                movie_data = response.json()

                # --- Cargar pelicula enriquecida ---
                enriched_watchlist.append({
                    "id": item.id,
                    "user_id": item.user_id,
                    "movie_id": item.movie_id,
                    "movie_title": movie_data["title"],
                    "movie_genre": movie_data["genre"],
                    "movie_rating": movie_data["rating"]
                })

            # --- Capturar errrores de conexion ---
            except Exception:
                
                # --- Agregar datos basicos si catalogo falla ---
                enriched_watchlist.append({
                    "id": item.id,
                    "user_id": item.user_id,
                    "movie_id": item.movie_id,
                    "movie_title": "Unavailable",
                    "movie_genre": "Unavailable",
                    "movie_rating": 0
                })

        # --- Retornar watchlist ---
        return enriched_watchlist
    

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