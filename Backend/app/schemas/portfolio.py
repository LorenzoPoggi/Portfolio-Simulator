# portfolio.py

from pydantic import BaseModel 
from typing import Optional
from datetime import datetime 
from schemas.stock import Internal_Stock

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