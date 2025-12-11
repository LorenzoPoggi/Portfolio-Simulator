# config.py

from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional

# ----------------------------------------------------
# Algoritmo de Encriptación y Tocken de Acceso
# ----------------------------------------------------

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 30
SECRET_KEY = 'e2cadd35402cb270f7c256664f62b610dd9199c964a9fb616aef05f9a8ac5494'
crypt = CryptContext(schemes="bcrypt")

# ---------------------------------------------------------
# Configuracion que lee variables de entorno (API externa)
# ---------------------------------------------------------

# Gestion de configuraciones
class Settings(BaseModel):
    FINANCE_API_KEY: Optional[str] = None
    class Config:
        env_file = ".env"  

settings = Settings()