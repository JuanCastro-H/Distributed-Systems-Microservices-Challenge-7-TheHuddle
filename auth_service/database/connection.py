# ====================================
# MODULO DE CONEXION A BASE DE DATOS
# ====================================

# ===================================
# Importaciones Y Librerias
# ===================================

import os # Permite Interaccion con OS

from sqlalchemy import create_engine    # Administrador de conexiones con PostgreSQL
from sqlalchemy.orm import sessionmaker # Plantilla de sesiones

from dotenv import load_dotenv          # Lector de archivos env

# --- Leer Variables de entorno ---
load_dotenv("auth_service/.env")

# --- Obtener URL de la BD ---
DATABASE_URL = os.getenv("DATABASE_URL") 

# --- Crear la conexion/puente con PostgreSQL ---
engine = create_engine(DATABASE_URL)

# --- Crear Plantilla de Sesiones para BD --
SessionLocal = sessionmaker(
    autocommit=False, # Nada se guarda automaticamente.
    autoflush=False,  # No enviar cambios pendientes a la BD de forma automatica.
    bind=engine       # Le pasamos nuestro engine a las sesiones que creemos.
)