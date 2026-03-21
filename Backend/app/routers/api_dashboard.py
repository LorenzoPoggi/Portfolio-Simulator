# api_dashboard.py 

from fastapi import APIRouter, Depends, HTTPException, status
from database.models.models import *
from core.security import *
from services.api_external import *
from services.api_external import busqueda_stock, busqueda_symbol
from schemas.stock import External_Stock, External_Symbol
import httpx 

# Inicializacion del Router
router = APIRouter(tags=['Api Dashboard'], prefix='/mercado')

# ----------------------------------------------------
# Operaciones CRUD para las Cotizaciones del mercado
# ----------------------------------------------------

# Operacion para ver las acciones extraidas de la API externa
@router.get('/search', response_model= list[External_Stock], status_code= status.HTTP_200_OK)
async def search_stock(query: str, user: User = Depends(current_user)):
    try:
        data = await busqueda_stock(query)
        return data ['data']['stock']
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code,
                            detail='Error desde Real-Time Finance')
    except httpx.RequestError:
        # Errores de conexión / timeout
        raise HTTPException(status_code=502,
                            detail='Fallo de conexión a Real-Time Finance')
    
# Operacion para obtener informacion de una accion en especifico
@router.get('/stock/{symbol}', response_model= External_Symbol, status_code= status.HTTP_200_OK)
async def get_especific_symbol(symbol: str, user: User = Depends(current_user)):
    try: 
        data = await busqueda_symbol(symbol)
        if not data or 'data' not in data:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                                detail='Accion no encontrada')
        return data ['data']
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code,
                            detail='Error desde Real-Time Finance')
    except httpx.RequestError:
        # Errores de conexión / timeout
        raise HTTPException(status_code=502,
                            detail='Fallo de conexión a Real-Time Finance')