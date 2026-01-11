# FarmTech - Docker Setup Guide

This guide provides instructions for running the FarmTech platform using Docker and Docker Compose.

## Prerequisites

- Docker Engine 20.10 or higher
- Docker Compose 2.0 or higher
- At least 4GB of available RAM
- At least 10GB of available disk space

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/erickkkt/FarmTech.git
cd FarmTech
```

### 2. Start All Services

```bash
docker-compose up -d
```

This command will:
- Build Docker images for all services (backend, farmadmin, webuser)
- Start PostgreSQL database
- Start Redis cache
- Start Django backend API
- Start Celery worker for background tasks
- Start web admin application
- Start web user application

### 3. Initialize the Database

After all services are up, run migrations and create a superuser:

```bash
# Run database migrations (already done automatically on startup)
docker-compose exec backend python manage.py migrate

# Create a superuser for admin access
docker-compose exec backend python manage.py createsuperuser
```

### 4. Access the Applications

- **Backend API**: http://localhost:8000
- **API Documentation (Swagger)**: http://localhost:8000/swagger/
- **API Documentation (ReDoc)**: http://localhost:8000/redoc/
- **Admin Panel**: http://localhost:8000/admin/
- **Web Admin App**: http://localhost:3000
- **Web User App**: http://localhost:3001

## Docker Compose Services

The docker-compose.yml file defines the following services:

### Core Services

1. **db** (PostgreSQL 15)
   - Database for storing all application data
   - Port: 5432
   - Default credentials: postgres/postgres
   - Data persisted in `postgres_data` volume

2. **redis** (Redis 7)
   - Cache and message broker for Celery
   - Port: 6379

3. **backend** (Django API)
   - REST API built with Django REST Framework
   - Port: 8000
   - Depends on: db, redis

4. **celery** (Celery Worker)
   - Background task worker
   - Depends on: db, redis

5. **farmadmin** (React Admin App)
   - Web admin interface
   - Port: 3000 (mapped to container port 80)
   - Served by Nginx

6. **webuser** (React User App)
   - Web user interface
   - Port: 3001 (mapped to container port 80)
   - Served by Nginx

## Common Docker Commands

### View Running Containers

```bash
docker-compose ps
```

### View Service Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f farmadmin
```

### Stop All Services

```bash
docker-compose down
```

### Stop and Remove Volumes (Clean Slate)

```bash
docker-compose down -v
```

### Rebuild Specific Service

```bash
# Rebuild backend
docker-compose build backend

# Rebuild and restart
docker-compose up -d --build backend
```

### Execute Commands in Running Containers

```bash
# Django management commands
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py shell

# Access database
docker-compose exec db psql -U postgres farmtech_db

# Access Redis CLI
docker-compose exec redis redis-cli
```

## Development Workflow

### 1. Making Backend Changes

The backend code is mounted as a volume, so changes are reflected immediately with auto-reload:

```bash
# Edit files in ./backend/
# The gunicorn server will auto-reload on changes
```

### 2. Making Frontend Changes

For development with hot-reload, you may want to run frontend apps locally:

```bash
# Stop the containerized frontend
docker-compose stop farmadmin

# Run locally
cd farmadmin
npm install
npm start
```

### 3. Running Tests

```bash
# Backend tests
docker-compose exec backend python manage.py test

# Frontend tests
docker-compose exec farmadmin npm test
```

## Environment Variables

### Backend Environment Variables

The backend service uses the following environment variables (set in docker-compose.yml):

- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (True/False)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`: Database connection
- `CORS_ALLOWED_ORIGINS`: Allowed CORS origins
- `CELERY_BROKER_URL`: Redis URL for Celery
- `CELERY_RESULT_BACKEND`: Redis URL for Celery results

### Frontend Environment Variables

Frontend apps use build-time arguments:

- `REACT_APP_API_URL`: Backend API URL (default: http://localhost:8000/api)

To customize the API URL, modify the `docker-compose.yml` file:

```yaml
farmadmin:
  build:
    args:
      REACT_APP_API_URL: http://your-api-url:8000/api
```

## Production Deployment

### Security Considerations

For production deployment, make the following changes:

1. **Change Secret Keys**
   ```yaml
   environment:
     - SECRET_KEY=your-very-long-secure-random-key
   ```

2. **Disable Debug Mode**
   ```yaml
   environment:
     - DEBUG=False
   ```

3. **Set Proper Allowed Hosts**
   ```yaml
   environment:
     - ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

4. **Use Environment Files**
   Create a `.env` file for sensitive data:
   ```bash
   # .env
   SECRET_KEY=your-secret-key
   DB_PASSWORD=secure-password
   ```

   Then reference it in docker-compose.yml:
   ```yaml
   backend:
     env_file:
       - .env
   ```

5. **Use HTTPS**
   - Configure SSL certificates
   - Use a reverse proxy (Nginx, Traefik)

6. **Database Backups**
   ```bash
   # Backup
   docker-compose exec db pg_dump -U postgres farmtech_db > backup.sql
   
   # Restore
   docker-compose exec -T db psql -U postgres farmtech_db < backup.sql
   ```

### Scaling Services

Scale specific services:

```bash
# Scale backend workers
docker-compose up -d --scale backend=3

# Scale Celery workers
docker-compose up -d --scale celery=2
```

## Troubleshooting

### Port Already in Use

If you get a "port already in use" error, change the port mapping in docker-compose.yml:

```yaml
ports:
  - "8001:8000"  # Changed from 8000:8000
```

### Database Connection Issues

Check if the database is healthy:

```bash
docker-compose ps
docker-compose logs db
```

Wait for the health check to pass:

```bash
docker-compose exec db pg_isready -U postgres
```

### Frontend Not Connecting to Backend

Ensure CORS settings in backend allow the frontend origin:

```python
# backend/farmtech_backend/settings.py
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:3001',
]
```

### Rebuilding from Scratch

```bash
# Stop everything
docker-compose down -v

# Remove images
docker-compose rm -f

# Rebuild and start
docker-compose up -d --build
```

### Viewing Container Resource Usage

```bash
docker stats
```

## File Structure

```
FarmTech/
├── docker-compose.yml          # Main orchestration file
├── Dockerfile                  # Root-level Dockerfile (optional)
├── .dockerignore              # Root-level ignore file
├── backend/
│   ├── Dockerfile             # Backend-specific Dockerfile
│   ├── .dockerignore          # Backend ignore file
│   └── ...
├── farmadmin/
│   ├── Dockerfile             # Admin app Dockerfile
│   ├── .dockerignore          # Admin app ignore file
│   ├── nginx.conf             # Nginx configuration
│   └── ...
└── webuser/
    ├── Dockerfile             # User app Dockerfile
    ├── .dockerignore          # User app ignore file
    ├── nginx.conf             # Nginx configuration
    └── ...
```

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Django Docker Deployment](https://docs.djangoproject.com/en/stable/howto/deployment/)
- [React Production Build](https://create-react-app.dev/docs/production-build/)

## Support

For issues related to Docker setup:
1. Check the logs: `docker-compose logs`
2. Verify all containers are running: `docker-compose ps`
3. Open an issue on GitHub with the error logs

## License

This project is licensed under the MIT License.
