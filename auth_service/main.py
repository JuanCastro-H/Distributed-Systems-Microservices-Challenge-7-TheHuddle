# ===================================
# Importaciones Y Librerias
# ===================================

# --- Obtener Framework ---
from fastapi import FastAPI 

app = FastAPI()

# Ruta Inicial de prueba
@app.get("/")
def root():
    return {
        "message": "Auth Service Running"
    }