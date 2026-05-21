# ====================================
# MODULO ENCARGADO DE LA SEGURIDAD 
# ====================================

# ===================================
# Importaciones Y Librerias
# ===================================

from passlib.context import CryptContext # Administrador de algoritmos de hashing



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