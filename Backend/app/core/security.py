# security.py

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_DURATION, crypt
from database.database import get_db
from database.models.models import User
from exceptions import excepciones

# ------------------------------------------------------------
# Sistema de Seguridad del Proyecto
# ------------------------------------------------------------

# Encriptacion de las contraseñas
def hash_pasword(password: str) -> str:
    return crypt.hash(password)

# Verificacion de las contraseñas
def verify_password(password: str, hashed_password: str)-> bool:
    return crypt.verify(password, hashed_password)

# 