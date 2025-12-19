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
    is_active: bool
    created_at: datetime
    # Clase para convertir de objeto sqlalchemy a este modelo, FastAPI lo interpreta 
    class Config:
        from_attributes = True 

class User_Update(BaseModel):
    fullname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

# ----------------------------------------------------
# Stock Schemas
# ----------------------------------------------------

# Esquema de devolucion del stock 
class Internal_Stock(BaseModel):
    id: Optional[int]
    symbol: str
    name: str
    exchange: str 
    currency: str
    sector: str
    # Clase para convertir de objeto sqlalchemy a este modelo, FastAPI lo interpreta 
    class Config: 
        from_attributes = True 

# Esquema de request de la API externa
class External_Stock(BaseModel):
    symbol: str
    name: str
    type: str
    price: float
    change: float
    change_percent: float
    previous_close: float
    last_update_utc: datetime
    country_code: str
    exchange: str
    exchange_open: datetime
    exchange_close: datetime
    timezone: str
    currency: str
    
# ----------------------------------------------------
# Portfolio Schemas
# ----------------------------------------------------

# Esquema de creacion de inversiones en el portfolio
class Portfolio_Create(BaseModel):
    stock_id: int
    quantity: int

# Esquema para devolucion del portfolio
class Portfolio_View(BaseModel):
    id: int 
    user_id: int
    stock_id: int
    quantity: int
    buy_price: float
    total_invested: float
    buy_date: datetime
    average_price: float
    stock: Optional[Internal_Stock]
    # Clase para convertir de objeto sqlalchemy a este modelo, FastAPI lo interpreta 
    class Config:
        from_attributes = True 

# Esquema para actualizar el portfolio
class Portfolio_Update(BaseModel):
    quantity: Optional[int]
    buy_price: Optional[float]
    average_price: Optional[float]

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