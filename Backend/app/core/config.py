# config.py

from passlib.context import CryptContext
import os

# ----------------------------------------------------
# Algoritmo de Encriptación y Tocken de Acceso
# ----------------------------------------------------

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 30
SECRET_KEY = os.getenv("SECRET_KEY")
crypt = CryptContext(schemes="bcrypt")