# ==============================================
# MODULO DE VALIDACION DE DATOS Y RESPUESTA
# ==============================================


# --- Importaciones Y Librerias ---
from pydantic import BaseModel


# --- Schema de Validacion ---
class WatchlistCreate(BaseModel):

    movie_id: int


# --- Schema de Respuesta ---
class WatchlistResponse(BaseModel):

    id: int

    user_id: int

    movie_id: int

    class Config:

        from_attributes = True