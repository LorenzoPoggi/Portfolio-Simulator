# api_dashboard.py 

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.database import get_db
from core.exceptions import excepciones
from core.security import *
from database.models import *
from services.api_external import *

# Inicializacion del Router
router = APIRouter(tags=['Api Dashboard'], prefix='/mercado')

# ----------------------------------------------------
# Operaciones CRUD para las Cotizaciones del mercado
# ----------------------------------------------------

# Operacion para ver las acciones extraidas de la API externa