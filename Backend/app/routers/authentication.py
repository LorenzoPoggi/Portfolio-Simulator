# authentication.py

from fastapi import APIRouter, Depends, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database.database import get_db
from core.exceptions import excepciones
from core.security import *
from core.config import *
from database.models import *
from schemas.user import *
from schemas.token import Login_Response

# Inicializacion del Router y Templates
router = APIRouter(tags=['Authentication'], prefix='/authentication')
router.mount("/static", StaticFiles(directory="Frontend/static", html=True), name="static")
templates = Jinja2Templates(directory='Frontend/templates')

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
@router.post('/login', response_model= Login_Response, status_code= status.HTTP_202_ACCEPTED)
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
        'user': db_user
    }

# ----------------------------------------------------
# Operaciones INTERFAZ para Register y Login
# ----------------------------------------------------

# Operacion para renderizar el registro a una interfaz
@router.get('/register', response_class= HTMLResponse)
async def register_html(request: Request):
    return templates.TemplateResponse(
        request= request, name= 'authentication.html')

# Operacion para renderizar el inicio de sesion a una interfaz
@router.get('/login', response_class= HTMLResponse)
async def login_html(request: Request):
    return templates.TemplateResponse(
        request= request, name= 'authentication.html')