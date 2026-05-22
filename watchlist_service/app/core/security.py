# ====================================
# MODULO ENCARGADO DE LA SEGURIDAD 
# ====================================

# ===================================
# Importaciones Y Librerias
# ===================================

import os  # Interactuar con el OS

# --- jwt y manejo de erroer ---
from jose import jwt
from jose import JWTError


from dotenv import load_dotenv          # Leer archivo env.
from pathlib import Path                # Manejar rutas.

# --- manejo de excepcciones y dependencias
from fastapi import Depends
from fastapi import HTTPException

# --- Verificar bearer ---
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials



# --- Obtener ruta absoluta del archivo actual ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# --- Construir ruta al .env ---
env_path = BASE_DIR / ".env"

# --- Leer Variables de entorno ---
load_dotenv(env_path)


# --- Obtener clave secretaa ---
SECRET_KEY = os.getenv("SECRET_KEY")

# --- Obtener algoritmo ---
ALGORITHM = os.getenv("ALGORITHM")

# --- Autenticacion bearer ---
security = HTTPBearer() 


# --- Verificar Token ---
def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    # --- Obtener token ---
    token = credentials.credentials


    try:
        
        # --- cargar payload ---
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # --- ID del usuario ---
        user_id = payload.get("sub")

        # --- no se pudo obtener ID ---
        if not user_id:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return user_id

    # --- Si expiro o hubo algun error ---
    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )