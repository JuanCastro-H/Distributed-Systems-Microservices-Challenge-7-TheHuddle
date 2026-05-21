# ====================================
# MODULO DE AUTENTICACION
# ====================================

# ===================================
# Importaciones Y Librerias
# ===================================

# --- Obtener session activa SQL ---
from sqlalchemy.orm import Session

# --- Importar acceso a DB ---
from auth_service.app.repositories.user_repository import UserRepository

# --- Importar funcion de Hashing ---
from auth_service.app.core.security import hash_password



# --- Servicio con logica de autenticacion y registro ---
class AuthService:
    
    # --- Registrar usuario ---
    @staticmethod # No necesita instancias.
    def register_user(
        db: Session,
        username: str,
        email: str,
        password: str
    ):
        # --- Verificar si el email ya existe ---
        existing_user = UserRepository.get_user_by_email(
            db,
            email # Obtener email.
        )

        # --- Si no existe devolver None ---
        if existing_user:

            return None 
        
        # --- Hashear password ---
        hashed_pw = hash_password(password)

        # --- Crear usuario ---
        return UserRepository.create_user(
            db,
            username,
            email,
            hashed_pw
        )