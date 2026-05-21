# ========================================
# MODULO DE DEFINICION DE LA TABLA USERS
# ========================================

# ===================================
# Importaciones Y Librerias
# ===================================

# --- Obtener Moldes Para crear Tablas ---
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

# --- Obtener La Clase Madre para las tablas ---
from auth_service.app.database.base import Base



# --- Crear Clase User para la tabla Usario ---
class User(Base): # Sig: "Esta clase pertenece al sistema ORM"

    # --- Nombre de la tabla ---
    __tablename__ = "users"

    # --- COLUMNAS DE LA TABLA ---

    # -- ID-PrimaryKey --
    id = Column(Integer, primary_key=True, index=True)

    # -- Nombre --
    username = Column(String, nullable=False)

    # -- Email --
    email = Column(String, unique=True, nullable=False) # Texto, valor unico, no puede estar vacio o None

    # -- Contrasenha-has --
    hashed_password = Column(String, nullable=False)

    # -- Actividad del usuario --
    is_active = Column(Boolean, default=True) 