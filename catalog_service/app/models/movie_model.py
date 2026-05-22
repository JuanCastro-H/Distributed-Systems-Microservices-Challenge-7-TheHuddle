# Importar plantilla de los elementos de una tabla
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

# --- Obtener el ORM ---
from app.database.base import Base

# --- Crear tabla Movie ---
class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    genre = Column(String, nullable=False)

    rating = Column(Float, nullable=False)