# token.py

from pydantic import BaseModel
from schemas.user import User_Response

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