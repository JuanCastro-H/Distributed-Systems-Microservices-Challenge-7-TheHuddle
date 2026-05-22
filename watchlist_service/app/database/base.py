# ============================================
# MODULO DE ESTRUCTURA BASE PARA CREAR TABLAS
# ============================================


# --- Importaciones Y Librerias ---
from sqlalchemy.orm import declarative_base
# ORM -> Object Relational Mapping 


# --- Crear La Clase Madre Para Tablas ---
Base = declarative_base()