# ====================================
# REPOSITORIO DE USUARIOS
# Encapsula y centraliza consultas SQL.
# ====================================

# ===================================
# Importaciones Y Librerias
# ===================================

# --- Importar Session ---
from sqlalchemy.orm import Session # Obtenemos la conexion activa con la BD

# --- Importar modelo de User ---
from app.models.user_model import User


# --------------------------------------------
# Centralizar consutas SQL de usuarios
# --------------------------------------------
class UserRepository:

    # --- Obtener email de la base de datos ---
    @staticmethod # Permite usar el metodo de la clase sin crear un objeto.
    def get_user_by_email(
        db: Session,
        email: str
    ):
        # --- Devolver email ---
        return db.query(User).filter(
            User.email == email
        ).first() # Devuelve el primer resultado o None
    

        # --- Crear un usuario nuevo ---
    @staticmethod
    def create_user(

        # --- Obtener datos procesados ---
        db: Session,
        username: str,
        email: str,
        hashed_password: str
    ):
        # --- Cargar datos a un objeto usurio ---
        user = User(
            username=username,
            email=email,
            hashed_password=hashed_password
        )

        # --- Prepara el objeto para insertarlo ---
        db.add(user)

        # --- Guardar en la BD ---
        db.commit()

        # --- Cargar Id al usuario ---
        db.refresh(user)
        
        # --- Retornar usuario nuevo --
        return user
