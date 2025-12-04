# user.py

from pydantic import BaseModel, EmailStr 
from typing import Optional, List
from datetime import datetime 

# ----------------------------------------------------
# User Schemas
# ----------------------------------------------------

# Esquema para lo que se necesita para registrarse
class User_Register(BaseModel):
    fullname: str
    email: EmailStr
    password: str

# Esquema para lo que necesita para registrarse
class User_Login(BaseModel):
    email: EmailStr
    password: str

# Esquema de devolucion de datos
class User_Response(BaseModel):
    id: int
    fullname: str
    email: EmailStr
    is_active: Optional[str]
    created_at: datetime
    # Clase para convertir de objeto sqlalchemy a este modelo, FastAPI lo interpreta 
    class Config:
        from_attributes = True 

# ----------------------------------------------------
# Stock Schemas
# ----------------------------------------------------

# Esquema de devolucion del stock 
class Stock_Response(BaseModel):
    id: Optional[int]
    name: str
    symbol: str
    sector: str
    price: float
    updated_at: datetime
    currency: str 

# ----------------------------------------------------
# Portfolio Schemas
# ----------------------------------------------------