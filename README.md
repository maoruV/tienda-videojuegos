# Tienda de Videojuegos

Tienda en línea de videojuegos construida con Django. Proyecto completo con catálogo de juegos, carrito de compras, sistema de usuarios y noticias.

## Tecnologías

- **Framework**: Django 6.0.4
- **Lenguaje**: Python 3.x
- **Base de datos**: SQLite (desarrollo) / MySQL/PostgreSQL (producción)
- **Gestión de configuración**: python-dotenv

## Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes Python)

## Instalación

### 1. Clonar el proyecto

```bash
git clone <url-del-repositorio>
cd tienda_videojuegos
```

### 2. Crear y activar entorno virtual

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Copiar el archivo de configuración apropiado según el entorno:

**Para desarrollo:**
```bash
copy .env_development .env
```

**Para producción:**
```bash
copy .env_production .env
```

Editar `.env` con los valores correspondientes:

```
DEBUG=True                  # False en producción
SECRET_KEY=tu-clave-secreta
ALLOWED_HOSTS=localhost,127.0.0.1,tu-dominio.com

DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3

# Si usas MySQL/PostgreSQL:
# DATABASE_ENGINE=django.db.backends.mysql
# DATABASE_NAME=nombre_db
# DATABASE_USER=usuario
# DATABASE_PASSWORD=password
# DATABASE_HOST=localhost
# DATABASE_PORT=3306
```

### 5. Aplicar migraciones

```bash
cd tienda_videojuegos
python manage.py migrate
```

### 6. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 7. Recolectar archivos estáticos

```bash
python manage.py collectstatic
```

## Ejecución

### Servidor de desarrollo

```bash
cd tienda_videojuegos
python manage.py runserver
```

Acceder a: http://localhost:8000

### Panel de administración

http://localhost:8000/admin

## Estructura del proyecto

```
tienda_videojuegos/
├── manage.py                 # Punto de entrada Django
├── db.sqlite3               # Base de datos SQLite
├── requirements.txt        # Dependencias Python
├── .env_development        # Variables desarrollo
├── .env_production         # Variables producción
├── .venv/                 # Entorno virtual
├── tienda_videojuegos/      # Proyecto Django
│   ├── settings.py        # Configuración
│   ├── urls.py           # Rutas principales
│   ├── wsgi.py          # Entrada WSGI
│   └── asgi.py          # Entrada ASGI
├── templates/            # Plantillas HTML
├── static/               # Archivos estáticos (CSS, JS, imágenes)
└── home/                 # App página principal
    catalogo/             # App catálogo de juegos
    buscador/            # App búsqueda
    usuarios/            # App usuarios
    carrito/             # App carrito de compras
    noticias/            # App noticias
```

## Apps incluidas

| App | Descripción |
|-----|-------------|
| `home` | Página principal |
| `catalogo` | Catálogo de videojuegos |
| `buscador` | Sistema de búsqueda |
| `usuarios` | registro/login de usuarios |
| `carrito` | Carrito de compras |
| `noticias` | Noticias y actualizaciones |

## Variables de entorno

| Variable | Descripción | Valores |
|----------|-------------|---------|
| `DEBUG` | Modo depuración | `True` / `False` |
| `SECRET_KEY` | Clave secreta Django | Texto seguro |
| `ALLOWED_HOSTS` | Hosts permitidos | Lista separada por comas |
| `DATABASE_ENGINE` | Motor de base de datos | `sqlite3`, `mysql`, `postgresql` |
| `DATABASE_NAME` | Nombre de la base de datos | Nombre |
| `DATABASE_USER` | Usuario de base de datos | Usuario |
| `DATABASE_PASSWORD` | Contraseña de base de datos | Contraseña |
| `DATABASE_HOST` | Host de base de datos | Host |
| `DATABASE_PORT` | Puerto de base de datos | Puerto |
| `DJANGO_PRODUCTION` | Entorno de producción | `1` para producción |

## Comandos útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear app
python manage.py startapp nombre_app

# Recolectar estáticos
python manage.py collectstatic

# Verificar configuración
python manage.py check

# Shell interactiva
python manage.py shell
```

## Produccion

### Configuración para producción

1. Establecer `DEBUG=False` en `.env`
2. Configurar `ALLOWED_HOSTS` con el dominio
3. Usar base de datos MySQL o PostgreSQL
4. Configurar servidor WSGI (Gunicorn, uWSGI)
5. Configurar servidor web (Nginx, Apache)

### Ejemplo con Gunicorn

```bash
pip install gunicorn
gunicorn tienda_videojuegos.wsgi:application --bind 0.0.0.0:8000
```

## Desarrollo futuro

- Pruebas unitarias
- Sistema de pedidos
- Pasarela de pago
- Panel de administración avanzado
- API REST
- Tests de rendimiento

## Licencia

MIT