import os

# --- jwt y manejo de erroer ---
from jose import jwt
from jose import JWTError

# --- leer env ---
from dotenv import load_dotenv

# --- manejo de excepcciones y dependencias
from fastapi import Depends
from fastapi import HTTPException

# --- Verificar bearer ---
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

# --- Cargar variables globales ---
load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = os.getenv("ALGORITHM")


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