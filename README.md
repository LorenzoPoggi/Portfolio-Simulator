# Portfolio-Simulator

### Introduccion 

Este proyecto se basa en un MVP de un Simulador de Portfolio, el cual tiene el objetivo de simular todas las acciones que se pueden hacer dentro de un broker digital. Las principales funciones que tiene esta aplicación son:

- Registro de Usuarios
- Compra y Ventas de Activos
- Obtención de Datos Financieros de diferentes Empresas

---
### Estructua del Repositorio

```
├── 📁 Backend
│   ├── 📁 app
│   │   ├── 📁 core
│   │   │   ├── config.py
│   │   │   ├── exceptions.py
│   │   │   └── security.py
│   │   ├── 📁 database
│   │   │   ├── 📁 models
│   │   │   │   └── models.py
│   │   │   ├── database.py
│   │   │   └── sqlalchemy.db
│   │   ├── 📁 routers
│   │   │   ├── api_dashboard.py
│   │   │   ├── authentication.py
│   │   │   ├── user_portfolio.py
│   │   │   └── user_profile.py
│   │   ├── 📁 schemas
│   │   │   ├── portfolio.py
│   │   │   ├── stock.py
│   │   │   ├── token.py
│   │   │   └── user.py
│   │   ├── 📁 services
│   │   │   └── api_external.py
│   │   └── main.py
│   └── ⚙️ .gitignore
├── 📁 Frontend
│   ├── 📁 static
│   │   ├── 📁 css
│   │   │   └── style.css
│   │   └── 📁 js
│   │       └── script.js
│   └── 📁 templates
│       ├── login.html
│       ├── register.html
│       └── user_profile.html
├── 📄 LICENSE
└── 📝 README.md
```

---
### Tecnologias Utilizadas

**Backend:**
- **FastAPI** - Framework web asincrónico para la construcción de APIs REST
- **SQLAlchemy** - ORM para interacción con la base de datos
- **SQLite** - Base de datos

**API Externa:**
- **Real-Time Finance API** (RapidAPI) - Obtención de datos financieros en tiempo real

**Autenticación y Seguridad:**
- **JWT (JSON Web Tokens)** - Autenticación y autorización de usuarios
- **Hash de contraseñas** - Almacenamiento seguro de credenciales

---
### Funciones Principales

1. **Autenticación de Usuarios**
   - Registro de nuevos usuarios con validación de email
   - Login seguro con generación de tokens JWT
   - Gestión de sesiones de usuario

2. **Gestión de Portfolio**
   - Visualización del portfolio personal con acciones adquiridas
   - Compra de acciones en el mercado simulado
   - Venta de acciones del portfolio
   - Historial de transacciones

3. **Dashboard de Mercado**
   - Búsqueda de acciones disponibles en tiempo real
   - Información detallada de cotizaciones (precio, cambios, etc.)
   - Filtrado y búsqueda avanzada de instrumentos financieros

4. **Perfil de Usuario**
   - Gestión de información personal
   - Visualización de estadísticas y resumen del portfolio
   - Control de balance y capital disponible