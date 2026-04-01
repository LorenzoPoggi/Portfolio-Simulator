# main.py

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
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

# Inicializacion de Estilos 
app.mount("/static", StaticFiles(directory='../../Frontend/styles', html=True), name="static")

# Inicializacion del Template Principal
principal_template = Jinja2Templates(directory='../../Frontend/templates')
 
@app.get('/', response_class= HTMLResponse)
async def index_html(request: Request):
    return principal_template.TemplateResponse(
        request= request, name= 'index.html'
    )

# Inicializacion de los Routers
app.include_router(router_authentication)
app.include_router(router_user_profile)
app.include_router(router_api_dashboard)
app.include_router(router_user_portfolio)