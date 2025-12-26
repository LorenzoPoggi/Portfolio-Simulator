# main.py

from fastapi import FastAPI
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from database.database import Base, engine, get_db
from routers.authentication import router as router_authentication
from routers.user_profile import router as router_user_profile
from routers.api_dashboard import router as router_api_dashboard
from routers.user_portfolio import router as router_user_portfolio

# Inicializacion de la APP
app = FastAPI(openapi_tags=[
    {
        "name": "Proyecto",
        "description": "Portfolio-Simulator"
    }
])

# Inicializacion del variables de entorno .env
load_dotenv()

# Inicializacion de la Base de Datos
Base.metadata.create_all(bind = engine)

# Inicializacion de los Routers
app.include_router(router_authentication)
app.include_router(router_user_profile)
app.include_router(router_api_dashboard)
app.include_router(router_user_portfolio)