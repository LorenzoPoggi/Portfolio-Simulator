# main.py

from fastapi import FastAPI
from sqlalchemy.orm import Session
from database.database import Base, engine, get_db
from routers.authentication import router as router_authentication

# Inicializacion de la APP
app = FastAPI(openapi_tags=[{'Proyecto': 'Portfolio-Simulator'}])

# Inicializacion de la Base de Datos
Base.metadata.create_all(bind = engine)

# Inicializacion de los Routers
app.include_router(router_authentication)