# ====================================
# MODULO DE AUTENTICACION
# ====================================

# ===================================
# Importaciones Y Librerias
# ===================================

# --- Obtener session activa SQL ---
from sqlalchemy.orm import Session

# --- Importar acceso a DB ---
from app.repositories.user_repository import UserRepository

# --- Importar funcion de Hashing ---
from app.core.security import hash_password

# --- Funcion para comparar y verificar contrasenha ---
from app.core.security import verify_password

# --- Generador de tokens ---
from app.core.security import create_access_token



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
    
        # --- Login De Usuarios ---
    @staticmethod
    def login_user(
        db: Session,
        email: str,
        password: str
    ):
        # --- Buscar usuario por Email ---
        user = UserRepository.get_user_by_email(
            db,
            email
        )

        # --- Si no lo encontramos devolver None ---
        if not user:

            return None

        # --- Verificar contrasenha ---
        valid_password = verify_password(
            password,             # Hashea Contrasnha Para compararla con el hash de la contrasenha real.
            user.hashed_password  # Hash de la Contrasenha real.
        )

        # --- Si no es valida devolver None ---
        if not valid_password:

            return None
        
        # --- Al logearse correctamente creamos un JWT ---
        access_token = create_access_token({
            "sub": str(user.id)
        })

        # --- Retornar el token ---
        return access_token
    
