# authentication.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.database import Base, get_db, engine
from core.exceptions import excepciones
from core.security import *
from core.config import *
from database.models import *
from schemas.schemas import *
from typing import List

# Inicializacion del Router
router = APIRouter(tags=['Authentiacion'], prefix='/authentication')

# ----------------------------------------------------
# Operaciones CRUD para Register y Login
# ----------------------------------------------------

# Operacion para registrar nuevos usuarios
@router.post('/register', response_model= User_Response, status_code=status.HTTP_201_CREATED)
async def register_user(user: User_Register, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email= user.email)
    if db_user:
        raise excepciones['email_ya_registrado']
    hashed_password = hash_password(user.password)
    db_user = User(
        email = user.email,
        password = hashed_password,
        fullname = user.fullname
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Operacion para el inicio de sesión de usuarios
