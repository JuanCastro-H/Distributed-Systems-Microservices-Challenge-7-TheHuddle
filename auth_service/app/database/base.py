# ============================================
# Clase base para todos los modelos ORM
# ============================================

# ===================================
# Importaciones Y Librerias
# ===================================

from sqlalchemy.orm import declarative_base 
# ORM -> Object Relational Mapping 

# --- Crear La Clase Madre Para Tablas ---
Base = declarative_base() 