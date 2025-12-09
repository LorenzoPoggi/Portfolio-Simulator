# user_profile.py 

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.database import get_db
from core.exceptions import excepciones
from core.security import *
from core.config import *
from database.models import *
from schemas.schemas import *

# Inicializacion del Router
router = APIRouter(tags=['User-Profile'], prefix='/profile')

# ----------------------------------------------------
# Operaciones CRUD para el Perfil de cada Usuario
# ----------------------------------------------------

# Operacion para la visualizacion de todos los usuarios 
@router.get('/users', response_model=list[User_Response], status_code= status.HTTP_202_ACCEPTED)
async def view_users(db: Session = Depends(get_db)):
    db_users = db.query(User).all()
    return db_users

# Operacion para la visualizacion de datos personales de un usuario
@router.get('/users/{user_id}', response_model= User_Response, status_code= status.HTTP_202_ACCEPTED)
async def view_my_user(user_id: int, db: Session=Depends(get_db)):
    db_user = get_user_by_id(db, user_id)
    if db_user is None:
        raise excepciones['usuario_no_encontrado']
    return db_user