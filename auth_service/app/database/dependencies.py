# =================================================================
# MODULO DE DEPENDENCIA 
# Crea una conexion temporal con la BD mientras dure una request.
# =================================================================

# ===================================
# Importaciones Y Librerias
# ===================================

from app.database.connection import SessionLocal # Plantilla de Sesiones para la base de datos.

# --- Crear Session De BD Inyectable ---
def get_db():

    # --- Crear una nueva sesion SQLAlchemy ---
    db = SessionLocal()

    try:     # Intenta.    

        yield db # Pausa la funcion, y entrega elementos a demanda.
    
    finally: # Bloque de limpieza.

        # --- Cerrar conexion con la BD ---
        db.close()