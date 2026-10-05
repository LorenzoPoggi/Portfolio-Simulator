# 📊 Portfolio Simulator

Este proyecto se basa en un MVP de un Simulador de Portfolio, el cual tiene el objetivo de simular la mayoria de operaciones que se pueden hacer dentro de un broker digital. 

Está construido con FastAPI, SQLAlchemy, SQLite y templates HTML con Jinja2. Permite registrar usuarios, iniciar sesión, consultar activos financieros y simular compras y ventas.

## Estructura

```text
├── Backend/
│   ├── app/
│   │   ├── core/       # Configuración, seguridad y errores
│   │   ├── database/   # Conexión SQLite y modelos SQLAlchemy
│   │   ├── routers/    # Rutas de autenticación, perfil, mercado y portfolio
│   │   ├── schemas/    # Validación de datos con Pydantic
│   │   ├── services/   # Integración con la API financiera
│   │   └── main.py     # Aplicación FastAPI
│   └── .env            # Configuración local (la crea cada usuario; no subir a Git)
├── Frontend/
│   ├── styles/         # Estilos de los Templates
│   └── templates/      # Páginas Jinja2
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.10 o posterior.
- `pip` (incluido normalmente con Python).
- Una clave de Real-Time Finance Data en RapidAPI solo si quieres usar la búsqueda y consulta de cotizaciones. La portada, el registro y el inicio de sesión no necesitan esa API.

## Clonar e instalar

Clona el repositorio y entra a su raíz:

```bash
git clone https://github.com/LorenzoPoggi/Portfolio-Simulator.git
cd Portfolio-Simulator
```

Crea un entorno virtual:

```bash
python -m venv .venv
```

Actívalo usando el comando correspondiente a tu terminal:

```bash
# macOS / Linux (bash o zsh)
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows Command Prompt (CMD)
.venv\Scripts\activate.bat
```

En Windows, si `python` no está disponible, prueba `py`. Instala las dependencias:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Variables de entorno

La app necesita `SECRET_KEY` para firmar los tokens de inicio de sesión. Las tres variables `FINANCE_*` habilitan las búsquedas de acciones. Puedes crear `Backend/.env` con un editor de texto; no hace falta que el archivo esté versionado.

Contenido de ejemplo:

```dotenv
SECRET_KEY=pon_aqui_un_valor_aleatorio_largo
FINANCE_API_KEY=tu_clave_de_rapidapi
FINANCE_API_HOST=real-time-finance-data.p.rapidapi.com
FINANCE_BASE_URL=https://real-time-finance-data.p.rapidapi.com
```

Genera tu propia `SECRET_KEY`; no uses una clave publicada en ejemplos o compartida por otra persona. No subas `Backend/.env` a Git. Si no configuras la API financiera, la aplicación puede arrancar y podrás probar las páginas de bienvenida, registro e inicio de sesión; la búsqueda y las cotizaciones no estarán disponibles.

## Crear una base local vacía

El proyecto usa SQLite, así que no hace falta instalar ni ejecutar un servidor de base de datos. Desde la raíz del repositorio ejecuta:

```bash
python -c "from pathlib import Path; Path('Backend/app/database').mkdir(parents=True, exist_ok=True)"
```

Esto solo crea el directorio donde SQLite espera guardar el archivo. La app crea las tablas cuando arranca. Si ya existe `Backend/app/database/sqlalchemy.db`, la app reutiliza esa base; para una prueba completamente limpia, clona el repositorio en otra carpeta (no borres una base que quieras conservar).

## Ejecutar la aplicación

Los imports y las rutas de templates/estilos actuales esperan que el directorio de trabajo sea `Backend/app`. Desde la raíz del repositorio:

```bash
cd Backend/app
python -m fastapi dev main.py
```

También puedes usar el ejecutable `fastapi` si está disponible en tu entorno virtual:

```bash
fastapi dev main.py
```

Abre <http://127.0.0.1:8000>. La documentación interactiva de la API está en <http://127.0.0.1:8000/docs>. Para detener el servidor, vuelve a la terminal y presiona `Ctrl+C`.

## Solución de problemas

- **`ModuleNotFoundError` al iniciar:** confirma que activaste el entorno virtual, instalaste `requirements.txt` y ejecutaste el comando desde `Backend/app`.
- **No carga el CSS o una plantilla:** comprueba que sigues en `Backend/app` al iniciar; las rutas de recursos están escritas respecto a ese directorio.
- **Error al conectarse a la API financiera:** revisa `FINANCE_API_KEY`, `FINANCE_API_HOST` y `FINANCE_BASE_URL` en `Backend/.env`, además de que tu clave y plan de RapidAPI permitan llamar a Real-Time Finance Data.
- **No se crea SQLite:** crea `Backend/app/database` con el comando anterior y comprueba que tienes permiso de escritura en la carpeta del proyecto.

## Dependencias principales

`requirements.txt` declara las dependencias de la app, incluyendo FastAPI/Uvicorn, SQLAlchemy/SQLite, autenticación, templates y el cliente `httpx` con `tenacity` para llamadas y reintentos a la API financiera.
