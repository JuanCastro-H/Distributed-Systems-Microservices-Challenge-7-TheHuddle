# ====================================
# REPOSITORIO DE HISTORIAL
# Encapsula y centraliza consultas SQL.
# ====================================

# ===================================
# Importaciones Y Librerias
# ===================================

# --- Importar Session ---
from sqlalchemy.orm import Session


# --- Importar modelo History ---
from app.models.history_model import History



# --------------------------------------------
# Centralizar consultas SQL del historial
# --------------------------------------------
class HistoryRepository:


    # --- Crear un registro en el Historial ---
    @staticmethod
    def create_history(
        db: Session,
        user_id: int,
        movie_id: int
    ):

        # --- Crear objeto a registrar ---
        history = History(
            user_id=user_id,
            movie_id=movie_id
        )

        # --- Preparar Guardado ---
        db.add(history)

        # --- Confirmar cambio --
        db.commit() 

        # --- Obtener ID ---
        db.refresh(history)

        # --- Retornar historial ---
        return history


    # --- Obtener historial del usuario ---
    @staticmethod
    def get_user_history(
        db: Session,
        user_id: int
    ):

        # --- Buscar registros relacionados al usuario ---
        return db.query(History).filter(
            History.user_id == user_id
        ).all() # Devolverlos todos.
    

    # --- Obtener historial por id ---
    @staticmethod
    def get_history_by_id(
        db: Session,
        history_id: int
    ):

        return db.query(History).filter(
            History.id == history_id
        ).first() # Devuelve el primer resultado o None.


    # --- Eliminar pelicula del historial ---
    @staticmethod
    def delete_history(
        db: Session,
        history: History
    ):

        db.delete(history)

        db.commit()

    # --- Eliminar todo el historial ---
    @staticmethod
    def delete_all_history(
        db: Session,
        user_id: int
    ):
        
        # --- Buscar y eliminar todos los registros ---
        db.query(History).filter(
            History.user_id == user_id
        ).delete()

        db.commit()


