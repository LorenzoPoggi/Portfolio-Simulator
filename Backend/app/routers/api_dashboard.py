# api_dashboard.py 

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.database import get_db
from core.exceptions import excepciones
from database.models.models import Stock, Price
from services.api_external import busqueda_stock
from schemas.schemas import External_Stock, Internal_Stock
from datetime import datetime

# Inicializacion del Router
router = APIRouter(tags=['Api Dashboard'], prefix='/mercado')

# ----------------------------------------------------
# Operaciones CRUD para las Cotizaciones del mercado
# ----------------------------------------------------

# Operacion para ver las acciones extraidas de la API externa
