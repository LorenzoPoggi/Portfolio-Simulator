# stock.py

from pydantic import BaseModel 
from typing import Optional
from datetime import datetime 

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

# Esquema de request de la API externa (stock)
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

# Esquema de request de la API externa (symbol)
class External_Symbol(BaseModel):
    symbol: str
    name: str
    type: str
    price: float
    open: float
    high: float
    low: float
    volume: int
    previous_close: float
    change: float
    change_percent: float
    pre_or_post_market: float
    pre_or_post_market_change: float 
    pre_or_post_market_change_percent: float
    last_update_utc: datetime

# Esquema de compra de stock (entrada)
class Stock_Purchase_Request(BaseModel):
    quantity: int

# Esquema de compra de stock (salida)
class Stock_Purchase_Response(BaseModel):
    symbol: str
    quantity: int
    price: float
    total_spent: float
    currency: str