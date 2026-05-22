# ====================================
# MODULO DE CONEXION
# ====================================

# ===================================
# Importaciones Y Librerias
# ===================================

import os # Permite Interaccion con OS

from sqlalchemy import create_engine     # Administrador de conexiones con PostgreSQL
from sqlalchemy.orm import sessionmaker  # Plantilla de sesiones

from pathlib import Path                 # Manejar rutas
from dotenv import load_dotenv           # Lector de archivos env



# --- Obtener ruta absoluta del archivo actual ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# --- Construir ruta al .env ---
env_path = BASE_DIR / ".env"

# --- Leer Variables de entorno ---
load_dotenv(env_path)


# --- Obtener URL de la BD ---
DATABASE_URL = os.getenv("DATABASE_URL")


# --- Crear la conexion/puente con PostgreSQL ---
engine = create_engine(DATABASE_URL)



# --- Crear Plantilla de Sesiones para BD --
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)