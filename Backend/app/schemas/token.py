# token.py

from pydantic import BaseModel, EmailStr 
from typing import Optional, List
from datetime import datetime 
from user import User_Response

# ----------------------------------------------------
# Token Schema
# ----------------------------------------------------

# Esquema del tipo de Token
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Esquema para el Tocken de Respuesta del Login
class Login_Response(BaseModel):
    access_token: str
    token_type: str
    user: User_Response