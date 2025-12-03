# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator

# ----------------------------------------------------------------
# Configuracion de la base de datos SQLAlchemy
# ----------------------------------------------------------------

# URL de la base de datos (SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./app/database/sqlalchemy.db"
 
# Creo el motor (el puente entre Python y la Base de Datos) 
engine = create_engine(
    # El argumento connect_args es necesario solo para SQLite
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} 
)

# Creo la fábrica de sesiones (SessionLocal)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creo el nombre de la Tabla que sera la base para nuestros modelos
Base = declarative_base()

# ----------------------------------------------------------------
# Dependencia para FastAPI
# ----------------------------------------------------------------

# Funcion para obtener el estado de la sesion de la base de datos
def get_db() -> Generator[sessionmaker, None, None]:
    db = SessionLocal()
    try:
        # Retorna la sesión al endpoint que la solicitó
        yield db
    finally:
        # Cierra la sesión al finalizar la petición
        db.close()