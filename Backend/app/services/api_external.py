# api_external.py

import os
import httpx 
from tenacity import retry, stop_after_attempt, wait_exponential

# ----------------------------
# Variables de Entonro (.env)
# ----------------------------

# Varaibles extraidas del .env 
API_KEY = os.getenv('FINANCE_API_KEY')
API_HOST = os.getenv('FINANCE_API_HOST')
FINANCE_BASE_URL = os.getenv('FINANCE_BASE_URL')
SEARCH_URL = f'{FINANCE_BASE_URL}/search'

# Headers
headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": API_HOST
}

# ----------------------------
# Conexión con la API externa
# ----------------------------

# Creamos una única instancia de AsyncClient que reutilizaremos
http_client = httpx.AsyncClient(timeout=10.0)

# Endpoint de reintentos: intenta hasta 3 veces con backoff exponencial
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1))
async def fetch_json(url: str, params: dict):
    response = await http_client.get(url, params=params, headers=headers)
    response.raise_for_status()  
    return response.json()

# Endpoint para la busqueda de stock
async def busqueda_stock(query: str):
    params = {
        "query": query,
        "language": "en"
    }
    response = await fetch_json(SEARCH_URL, params)
    return response