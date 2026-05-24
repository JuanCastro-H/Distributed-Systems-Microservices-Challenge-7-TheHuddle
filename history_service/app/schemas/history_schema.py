# ==============================================
# MODULO DE VALIDACION DE DATOS Y RESPUESTA
# ==============================================

# --- Importaciones Y Librerias ---
from pydantic import BaseModel

from datetime import datetime


# --- Modelo de Validacion ---
class HistoryCreate(BaseModel):

    movie_id: int


# --- Modelo de respuesta ---
class HistoryResponse(BaseModel):

    id: int

    user_id: int

    movie_id: int

    movie_title: str

    movie_genre: str

    movie_rating: float

    watched_at: datetime

    class Config:

        from_attributes = True