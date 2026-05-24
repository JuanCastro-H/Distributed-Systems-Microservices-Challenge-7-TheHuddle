# ====================================
# MODULO DE RUTAS
# ====================================

# ===================================
# Importaciones Y Librerias
# ===================================

# --- Obtener Router, inyeccion de dependencias Y manejo de errores HTTP ---
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

# --- Obtener session a activa con la DB ---
from sqlalchemy.orm import Session

# --- Obtener Schemas Pydantic para validacion y respuestas ---
from app.schemas.user_schema import UserCreate   # Valida el JSON con los datos del usuario recibidos.
from app.schemas.user_schema import UserResponse # Controla JSON que Devolvemos.

# --- Dependencia para crear conexion con DB ---
from app.database.dependencies import get_db 

# --- Obtener servicio de autenticacion ---
from app.services.auth_service import AuthService

from app.schemas.user_schema import UserLogin
from app.schemas.user_schema import Token

from app.core.security import verify_token

from fastapi.security import OAuth2PasswordRequestForm
from app.models.user_model import User
from app.core.security import verify_password
from app.core.security import create_access_token

# --- Crear Router ---
router = APIRouter(prefix="/auth", tags=["Auth"])


# ============================================ 
# RUTA PARA REGISTRAR UN NUEVO USUARIO
# ============================================ 

@router.post("/register", response_model=UserResponse, status_code=201) # 201 codigo para nuevo recurso
def register(user_data: UserCreate, db: Session = Depends(get_db)):

    # --- Ejecutr logica de registro de usuario ---
    user = AuthService.register_user(
        db,
        user_data.username,
        user_data.email,
        user_data.password
    )

    # --- Validacion de datos ---
    if not user: # Si el email esta repetido el resultado devuelto sera None.

        # --- lanzar excepcion ---
        raise HTTPException(
            status_code=400,
            detail="Email Already exists"
        )
    
    # --- Retornar usuario ---
    return user


# ============================================ 
# RUTA PARA INICIAR SESION Y GENERAR JWT
# ============================================ 

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), # Obtener credenciales del formulario.
    db: Session = Depends(get_db)                                    
):
    
    # --- Buscar usuario por email ---
    user = db.query(User).filter(
        User.email == form_data.username # El email se envia dentro de la sesion username.
    ).first()
    
    # --- Si no existe ---
    if not user:
        
        # --- Devolver error 401 ---
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    # --- Verificar contrasenha hasheando y comparando ---
    if not verify_password(
        form_data.password,
        user.hashed_password
    ):

        # --- Si sale mal retornar error 401 ---
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    # -- Generar JWT con ID del usuario ---
    access_token = create_access_token(
        data={"sub": str(user.id)}
    )

    # --- Retornar JWT ---
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# ============================================ 
# RUTA PARA VALIDAR JWT
# ============================================ 

@router.get("/me")
def me(user_id: str = Depends(verify_token)):

    return {"user_id": user_id} # Te devuelve tu ID
