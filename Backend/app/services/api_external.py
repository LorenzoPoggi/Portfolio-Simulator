# api_external.py

import requests
import os
import httpx 
from tenacity import retry, stop_after_attempt, wait_exponential

# ----------------------------
# Conexión con la API externa
# ----------------------------

# Direccion de la API externa de finanzas
url = "https://real-time-finance-data.p.rapidapi.com/search"

# Lista de peticion de stock por una query 
querystring = {"query":"Apple","language":"en"}

# Metadatos para una peticion HTTP
headers = {
	"x-rapidapi-key": "191be09c6emsh2e5d3a9a042c4b6p1b9706jsn7d36f3435aef",
	"x-rapidapi-host": "real-time-finance-data.p.rapidapi.com"
}

# --------------------------
# Cliente HTTP asincrónico
# --------------------------

# Creamos una única instancia de AsyncClient que reutilizaremos
http_client = httpx.AsyncClient(timeout=10.0)

# Endpoint de reintentos: intenta hasta 3 veces con backoff exponencial
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1))
async def fetch_json(url: str) -> dict:
    # Peticion HTTP GET a la URl con parametros dados
    response = await http_client.get(url, headers=headers, params=querystring)
    response.raise_for_status()  
    # Devuelve el contenido JSON de la respuesta
    return response.json()