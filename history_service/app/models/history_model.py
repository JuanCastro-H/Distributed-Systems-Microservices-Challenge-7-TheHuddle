# ===================================
# Importaciones Y Librerias
# ===================================

# --- Importar columnas y tipos SQL ---
from sqlalchemy import Column
from sqlalchemy import Integer

# --- Importar clase base ORM ---
from app.database.base import Base

# --- Importar librerias para manejar el tiempo ---
from datetime import datetime
from datetime import timezone
from sqlalchemy import DateTime



# ---------------------------------------------
# MODELO DE HISTORIAL
# Representa el historial de los usuarios
# ---------------------------------------------

class History(Base):

    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)

    movie_id = Column(Integer, nullable=False)

    watched_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )