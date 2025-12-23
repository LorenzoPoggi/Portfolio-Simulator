# stock.py

from pydantic import BaseModel, EmailStr 
from typing import Optional, List
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