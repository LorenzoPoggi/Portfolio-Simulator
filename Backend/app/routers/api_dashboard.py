# api_dashboard.py 

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.database import get_db
from core.exceptions import excepciones
from database.models.models import *
from core.security import *
from services.api_external import *
from services.api_external import busqueda_stock
from schemas.schemas import External_Stock, Internal_Stock
from datetime import datetime
import httpx 

# Inicializacion del Router
router = APIRouter(tags=['Api Dashboard'], prefix='/mercado')

# ----------------------------------------------------
# Operaciones CRUD para las Cotizaciones del mercado
# ----------------------------------------------------

# Operacion para ver las acciones extraidas de la API externa
@router.get("/stock", response_model= list[External_Stock], status_code= status.HTTP_200_OK)
async def search_stock(query: str, user: User = Depends(current_user)):
    try:
        data = await busqueda_stock(query)
        return data ['data']['stock']
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code,
                            detail="Error desde Real-Time Finance")
    except httpx.RequestError:
        # Errores de conexión / timeout
        raise HTTPException(status_code=502,
                            detail="Fallo de conexión a Real-Time Finance")