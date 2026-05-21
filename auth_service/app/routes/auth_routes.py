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
from auth_service.app.schemas.user_schema import UserCreate   # Valida el JSON con los datos del usuario recibidos.
from auth_service.app.schemas.user_schema import UserResponse # Controla JSON que Devolvemos.

# --- Dependencia para crear conexion con DB ---
from auth_service.app.database.dependencies import get_db 

# --- Obtener servicio de autenticacion ---
from auth_service.app.services.auth_service import AuthService



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