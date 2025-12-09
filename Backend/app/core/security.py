# security.py

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_DURATION, crypt
from database.database import get_db
from database.models.models import User
from core.exceptions import excepciones

# Sistema de Autenticacion
oauth2 = OAuth2PasswordBearer(tokenUrl='login')

# ------------------------------------------------------------
# Sistema de Hashing de Contraseñas
# ------------------------------------------------------------

# Encriptacion de las contraseñas
def hash_password(password: str) -> str:
    return crypt.hash(password)

# Verificacion de las contraseñas
def verify_password(password: str, hashed_password: str)-> bool:
    return crypt.verify(password, hashed_password)

# ------------------------------------------------------------
# Sistema de Generacion de Tokens
# ------------------------------------------------------------

# Creacion de Tokens codificados para usuarios
def generate_access_token(subject: str) -> str:
    to_encode = {'sub': subject}
    to_encode['iat'] = datetime.utcnow()
    access_token_expire = timedelta(minutes=ACCESS_TOKEN_DURATION)
    expiration = datetime.utcnow() + access_token_expire
    to_encode['exp'] = expiration
    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return access_token

# Decodificacion de Tokens con devolucion del usuario
def decode_access_token(access_token: str) -> str:
    try:
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        subject = payload.get('sub')
        if subject is None:
            raise excepciones['no_autorizado']
    except JWTError: 
        raise excepciones['no_autorizado']
    return subject 

# ------------------------------------------------------------
# Sistema de Validacion de Tokens y obtención de Usuarios
# ------------------------------------------------------------

# Dependencia que busca el usuario en la base de datos
async def auth_user(access_token: str = Depends(oauth2), db: Session = Depends(get_db)) -> User:
    subject = decode_access_token(access_token)
    user = db.query(User).filter(User.email == subject).first()
    if not user:
        raise excepciones['usuario_no_encontrado']
    return user 

# Criterio de Dependencia de actividad del usuario
async def current_user(user: User = Depends(auth_user)) -> User:
    if not user.is_active:
        raise excepciones['usuario_inactivo']
    return user 

# Funcion para la busqueda de usuarios por email
def get_user_by_email(db: Session, email: str) -> User | None:
    # Usamos User que es el nombre de la clase del modelo
    return db.query(User).filter(User.email == email).first()

# Funcion para la busqueda de usuarios por id
def get_user_by_id(db: Session, id: int) -> User | None:
    return db.query(User).filter(User.id == id).first()