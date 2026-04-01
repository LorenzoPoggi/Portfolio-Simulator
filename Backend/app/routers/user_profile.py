# user_profile.py 

from fastapi import APIRouter, Depends, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database.database import get_db
from core.exceptions import excepciones
from core.security import *
from core.config import *
from database.models import *
from schemas.user import *

# Inicializacion del Router
router = APIRouter(tags=['User Profile'], prefix='/profile')
templates = Jinja2Templates(directory='../../Frontend/templates/profiles')

# ---------------------------------------------------------
# Operaciones con la LOGICA para el Perfil de cada Usuario
# ---------------------------------------------------------

# Operacion para la visualizacion de todos los usuarios 
@router.get('/users', response_model=list[User_Response], status_code= status.HTTP_200_OK)
async def view_users(db: Session = Depends(get_db)):
    db_users = db.query(User).all()
    return db_users

# Operacion para la visualizacion de datos personales de un usuario
@router.get('/me', response_model= User_Response, status_code= status.HTTP_200_OK)
async def view_my_user(user: User = Depends(current_user)):
    return user

# Operacion para actualizar los datos personales de un usuario
@router.put('/me', response_model= User_Update, status_code= status.HTTP_202_ACCEPTED)
async def update_my_user(update_data: User_Update, user: User = Depends(current_user), db: Session = Depends(get_db)):
    if update_data.email != user.email and get_user_by_email(db, update_data.email):
        raise excepciones['email_ya_registrado']
    user.fullname = update_data.fullname
    user.email = update_data.email
    if update_data.password:
        user.password = hash_password(update_data.password)
    db.commit()
    db.refresh(user)
    return user

# Operacion para eliminar un usuario
@router.delete('/me', status_code= status.HTTP_204_NO_CONTENT)
async def delete_my_account(user: User = Depends(current_user), db: Session = Depends(get_db)):
    if user is None:
        raise excepciones['usuario_no_encontrado']
    db.delete(user)
    db.commit()
    return {}

# ------------------------------------------------------------
# Operaciones para los ADAPTADORES del Perfil de cada Usuario
# ------------------------------------------------------------

# Adaptador entre HTML y API de la actualizacion de datos
@router.post('/update-me-form')
async def update_my_user_form(request: Request, 
                              email: str = Form(...), password: str = Form(None), fullname: str = Form(...), 
                              user: User = Depends(current_user),db: Session = Depends(get_db)):
    update_data = User_Update(email=email, password=password, fullname=fullname)
    await update_my_user(user=user, update_data=update_data, db=db)
    return RedirectResponse('/profile/me/personal-data?success=updated', status_code=303)

# Adaptador entre HTML y API de la eliminacion de usuario
@router.post('/delete-me-form')
async def delete_my_user_form(reques: Request, 
                              user: User = Depends(current_user), db: Session = Depends(get_db)):
    await delete_my_account(user=user, db=db)
    return RedirectResponse('/authentication/login?success=deleted', status_code=303)

# -----------------------------------------------------------
# Operaciones para las INTERFACES del Perfil de cada Usuario
# -----------------------------------------------------------

# Operacion para renderizar al perfil del usuario
@router.get('/me/personal-data', response_class= HTMLResponse)
async def view_my_user_html(request: Request, user: User = Depends(current_user)):
    return templates.TemplateResponse(
    'user_profile.html',
    {
        'request': request,
        'user': user
    }
)