# Portfolio-Simulator

### Introduccion 

Este proyecto se basa en un MVP de un Simulador de Portfolio, el cual tiene el objetivo de simular todas las acciones que se pueden hacer dentro de un broker digital. Las principales funciones que tiene esta aplicación son:

- Registro de Usuarios
- Compra y Ventas de Activos
- Obtención de Datos Financieros de diferentes Empresas

---
### Estructua del Repositorio

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
└── README.md
```