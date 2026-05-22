import os

# --- Crear connexion ---
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# --- leer env ---
from dotenv import load_dotenv

# --- Cargar variables globales ---
load_dotenv("catalog_service/.env")

# --- Obtener URL de la base de datos ---
DATABASE_URL = os.getenv("DATABASE_URL")

# --- Crear la conexion o puente con la base de datos
engine = create_engine(DATABASE_URL)

# --- Crear plantilla para sesiones temporales con la base de datos ---
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)