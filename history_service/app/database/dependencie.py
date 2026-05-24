# ==============================
# MODULO DE DEPENDENCIA 
# ==============================

# --- Importaciones Y Librerias ---
from app.database.connection import SessionLocal



# --- Crear conexion temporal con la BD ---
def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()