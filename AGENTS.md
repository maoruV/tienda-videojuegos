# AGENTS.md - Tienda de Videojuegos

## Project Type
Django 6.0.4 web application (Python)

## Entry Points
- `tienda_videojuegos/manage.py` - Django management commands
- `tienda_videojuegos/tienda_videojuegos/settings.py` - Main configuration

## Essential Commands

```bash
# Run development server
cd tienda_videojuegos && python manage.py runserver

# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

## Environment Configuration
- **Development**: Uses `.env_development` (auto-loaded)
- **Production**: Set `DJANGO_PRODUCTION=1` env var to load `.env_production`
- The settings.py automatically selects the correct .env file based on this variable

## Architecture Notes
- **Custom User Model**: Uses `usuarios.Usuario` (not Django's default User)
- **Shopping Cart**: Implemented via `carrito.context_processors.carrito_total`
- **Multi-app structure**: home, catalogo, buscador, usuarios, carrito, noticias

## Database
- Default: SQLite (`db.sqlite3` in project root)
- Production: MySQL/PostgreSQL (configure in .env)

## Static Files
- Served from `static/` directory
- Configured in settings.py via `STATICFILES_DIRS` and `STATIC_ROOT`

## Testing
- Standard Django test framework (`python manage.py test`)
- Each app has its own `tests.py`