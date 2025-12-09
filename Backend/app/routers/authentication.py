# authentication.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.database import get_db
from core.exceptions import excepciones
from core.security import *
from core.config import *
from database.models import *
from schemas.schemas import *

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
@router.post('/login', response_model= User_Response, status_code= status.HTTP_202_ACCEPTED)
async def login_user(user: User_Login, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email = user.email)
    if not db_user:
        raise excepciones['usuario_no_encontrado']
    if not verify_password(user.password, db_user.password):
        raise excepciones['contrasena_incorrecta']
    access_token = generate_access_token(str(db_user.id))
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user': User_Response.from_attributes(db_user)
    }