# Portfolio-Simulator

### 📖 Introduccion 

Este proyecto se basa en un MVP de un Simulador de Portfolio, el cual tiene el objetivo de simular la mayoria de operaciones que se pueden hacer dentro de un broker digital. Las principales funciones que tiene esta aplicación son:

- Registro de Usuarios 
- Configuracion de Datos Personales de cada Usuario
- Busqueda de Activos y Obtencion de sus Datos Financieros
- Compra y Ventas de Activos
- Simulacion de un Portafolio de Inversiones

---
### 🌳 Estructua del Repositorio

```
├── Backend
│   │
│   ├── app
│   │   │
│   │   ├── core
│   │   │   ├── config.py
│   │   │   ├── exceptions.py
│   │   │   └── security.py
│   │   │   
│   │   ├── database
│   │   │   ├── models
│   │   │   │   └── models.py
│   │   │   ├── database.py
│   │   │   └── sqlalchemy.db
│   │   │
│   │   ├── routers
│   │   │   ├── api_dashboard.py
│   │   │   ├── authentication.py
│   │   │   ├── user_portfolio.py
│   │   │   └── user_profile.py
│   │   │
│   │   ├── schemas
│   │   │   ├── portfolio.py
│   │   │   ├── stock.py
│   │   │   ├── token.py
│   │   │   └── user.py
│   │   │
│   │   ├── services
│   │   │   └── api_external.py
│   │   │
│   │   └── main.py
│   │   
│   └── .gitignore
│   
├── Frontend
│   │
│   ├── styles
│   │   │
│   │   └── style.css
│   │   
│   └── templates
│       │
│       ├── authentications
│       │   ├── login.html
│       │   └── register.html
│       ├── dashboards
│       │   ├── stocks.html
│       │   └── symbol.html
│       ├── portfolios
│       │   └── user_portfolio.html
│       ├── profiles
│       │   └── user_profile.html
│       └── index.html
│   
├── LICENSE
├── README.md
└── requirements.txt
```

---
### 📚 Funcionalidades 

#### Backend
- API REST completa construida con FastAPI
- ORM con SQLAlchemy para la creacion de Base de Datos 
- Arquitectura Organizada (Core, Database, Routers, Schemas, Services)

#### Frontend
- Templates basicos construidos con HTML 
- Estilos basicos hechos con CSS
- Renderizacion de Templates con Jinja2 que muestras datos recibidos del Back

#### Base de Datos
- Modelos de entidades con SQLAlchemy
- Validación de Datos con Pydantic

#### Autenticaión y Seguridad
- Registro y Login de Usuarios
- Generación de Tokens JWT
- Proteccion de Rutas Privadas
- Hashing de Contraseñas con Passlib (CryptContext)

#### Conexión con una API Externa 
- Conexion y Acceso a Datos Financieros de la API "Real-Time Finance Data" 
- Visualizacion de Informacion Detallada por Activo

#### Operaciones de un Broker Digital
- Simulacion de Compra y Venta de Activos 
- Conexion de cada Portafolio por Usuario en la Base de Datos 
- Visualizacion de Portafolio

---

### 🚀 Guia de Uso

#### Clonar el repositorio

```
git clone https://github.com/LorenzoPoggi/Portfolio-Simulator.git
cd Portfolio-Simulator
```

#### Crear un Entortno Virtual 

```
python -m venv venv
# Windows
venv\Scripts\activate
# Lix/Mac
source venv/bin/activate
```

#### Instalar Independencias

```
pip install -r requirements.txt
```

#### Agregar Variables de Entorno

```
cd Backend
touch .env 
# Agregar SECRET_KEY y FINANCE_API_KEY
```

#### Ejecutar la Aplicación

```
cd app
fastapi dev main.py
```

#### Ingresar a la Web

```
http://127.0.0.1:8000
```