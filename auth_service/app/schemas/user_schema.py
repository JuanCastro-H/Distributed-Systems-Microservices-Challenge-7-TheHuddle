# ==============================================
# MODULO DE VALIDACION DE DATOS Y SERIALIZACION
# Creas Esquemas de validacion de datos
# ==============================================

# ===================================
# Importaciones Y Librerias
# ===================================

# --- Importar modelo base ---
from pydantic import BaseModel # Valida los datos y devuelve codigos de errores de forma automatica si fallan


from pydantic import EmailStr # Formato para validar Emails.



# --- Schema para validacuion de datos de entrada --- 
class UserCreate(BaseModel): # En caso de error automaticamente salta: 422 Unprocessable Entity

    # --- Nombre ---
    username: str

    # --- Formato email ---
    email: EmailStr 

    # --- Contrasenha ---
    password: str


# --- Schema para controlar datos devueltos al cliente ---
class UserResponse(BaseModel):

    # --- Definir campos a devolver ---

    # ID
    id: int

    # Nombre
    username: str

    # Email
    email: EmailStr

    # Actividad de usuario ---
    is_active: bool

    # --- Configuracion especial ---
    class Config:

        # Convertir objetos ORM SQL.. a Pydantic
        from_attributes = True


# --- Schema para login de usuario ---
class UserLogin(BaseModel):

    email: EmailStr

    password: str


# --- Schema de respuesta JWT ---
class Token(BaseModel):

    # --- Token ---
    access_token: str

    # --- Tipo de autenticacion ---
    token_type: str
    