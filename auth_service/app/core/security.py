# ====================================
# MODULO ENCARGADO DE LA SEGURIDAD 
# ====================================

# ===================================
# Importaciones Y Librerias
# ===================================

from passlib.context import CryptContext # Administrador de algoritmos de hashing

import os # Interactuar con el OS
from pathlib import Path  

# --- Manejo de fechas y expiracion de tokens JWT ---
from datetime import datetime
from datetime import timedelta
from datetime import timezone

# --- Libreria para crear y verificar JWT ---
from jose import jwt

# --- Manejo de errores JWT invalidos ---
from jose import JWTError

# --- Leer archivos env
from dotenv import load_dotenv

# --- Dependencias y Errores HTTP
from fastapi import Depends
from fastapi import HTTPException

# --- Herramienta para extraer el token del header ---
from fastapi.security import OAuth2PasswordBearer # Se queda con el codigo del JWT.



# --- Obtener ruta absoluta del archivo actual ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# --- Construir ruta al .env ---
env_path = BASE_DIR / ".env"

# --- Leer Variables de entorno ---
load_dotenv(env_path)


# --- Obtener variables de entorno ---

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


# --- Crear extractor de tokens ---
oauth2_scheme = OAuth2PasswordBearer( #Extraer JWT desde authorization Header con el Sistemaa OAuth2 
    tokenUrl="/auth/login"
)


# --- Configuracion del contenedor de Hashin ---
pwd_context = CryptContext(
    schemes=["bcrypt"], # Algoritmo de hasheo lento
    deprecated="auto"   # Actualizar contrasenhas si se usa un algoritmo mas moderno.
)

# --- Recibir y Hashear contrasenha ---
def hash_password(password: str):

    return pwd_context.hash(password)


# --- Verificar Contrasenha ---
def verify_password(
        plain_password: str,   # Obtener contrasenha
        hashed_password: str   # Obtener hash
): 
    # --- Verificar ---
    return pwd_context.verify( # Compara hashes y devuelve True o False
        plain_password,
        hashed_password
    )


# --- Crear acceso al token ---
def create_access_token(data: dict):

    # --- Copiar dtos del payload ---
    to_encode = data.copy()

    # --- Crear fecha de expircion del token ---
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # --- agregar Expiracion al JWT ---
    to_encode.update({
        "exp": expire
    })

    # --- Crear JWT ---
    encoded_jwt = jwt.encode(  # Codifica el token.
        to_encode,             # Payload / datos que iran dentro del token.
        SECRET_KEY,            # Clave secreta sirve para firmar el token y verificar autenticidad.
        algorithm=ALGORITHM 
    )

    # --- Devolver JWT ---
    return encoded_jwt


# --- Verificar token ---
def verify_token(token: str = Depends(oauth2_scheme)): # Obtener y validar token desde authorization header.

    try:

        # --- DecodificarJWT ---
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # --- Obtener ID del usuario ---
        user_id = payload.get("sub")

        # --- Si no  error 401 token invalido ---
        if not user_id:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        
        # --- Retornar ID ---
        return user_id
    
    # --- Error si es invalido o expirado ---
    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )