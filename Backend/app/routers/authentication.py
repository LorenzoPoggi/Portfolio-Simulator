# authentication.py

from fastapi import APIRouter, Depends, status, Request, Form, Response
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
router.mount("/static", StaticFiles(directory="../../Frontend/static/css", html=True), name="static")
templates = Jinja2Templates(directory='../../Frontend/templates')

# ----------------------------------------------------
# Operaciones con la LOGICA del Register y del Login
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

# Operacion para el cierre de sesión de usuarios
@router.get("/logout")
async def logout():
    response = RedirectResponse("/authentication/login")
    response.delete_cookie("access_token")
    return response

# -----------------------------------------------------------
# Operaciones para los ADAPTADORES del Register y  del Login
# -----------------------------------------------------------

# Adaptador entre HTML y API del registro
@router.post('/register-form')
async def register_form(request: Request, email: str = Form(...), password: str = Form(...), fullname: str = Form(...), db: Session = Depends(get_db)):
    user_data = User_Register(email=email, password=password, fullname=fullname)
    await register_user(user=user_data, db=db)
    return RedirectResponse(url='/authentication/login', status_code=303)

# Adaptador entre HTML y API del login 
@router.post('/login-form')
async def login_form(response: Response, request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user_data = User_Login(email=email, password=password)
    result = await login_user(user=user_data, db=db)
    db_user = get_user_by_email(db, email=email)
    if not db_user:
        return RedirectResponse("/authentication/login?error=user_not_found", status_code=303)
    if not verify_password(password, db_user.password):
        return RedirectResponse("/authentication/login?error=wrong_password", status_code=303)
    access_token = result['access_token']
    redirect = RedirectResponse(url='/profile/me/personal-data', status_code=303)
    redirect.set_cookie(
        key= 'access_token', value= access_token, httponly= True, samesite= 'lax'
    )
    return redirect

# Adaptador entre HTML Y API del logout 
@router.post('/logout-form')
async def logout_form():
    response = RedirectResponse("/authentication/login", status_code=303)
    response.delete_cookie("access_token")
    return response

# ---------------------------------------------------------
# Operaciones para las INTERFACES del Register y  del Login
# ---------------------------------------------------------

# Operacion para renderizar el registro a una interfaz
@router.get('/register', response_class= HTMLResponse)
async def register_html(request: Request):
    return templates.TemplateResponse(
        request= request, name= 'register.html')

# Operacion para renderizar el inicio de sesion a una interfaz
@router.get('/login', response_class= HTMLResponse)
async def login_html(request: Request):
    return templates.TemplateResponse(
        request= request, name= 'login.html')