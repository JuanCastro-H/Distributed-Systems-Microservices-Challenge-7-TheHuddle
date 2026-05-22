# ====================================
# MODULO MODELO WATCHLIST
# ====================================

# ===================================
# Importaciones Y Librerias
# ===================================

# --- Importar columnas y tipos SQL ---
from sqlalchemy import Column
from sqlalchemy import Integer

# --- Importar clase base ORM ---
from app.database.base import Base


# ---------------------------------------------
# MODELO DE WATCHLIST
# Representa peliculas guardadas por usuarios
# ---------------------------------------------
class Watchlist(Base):

    __tablename__ = "watchlist"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)

    movie_id = Column(Integer, nullable=False)