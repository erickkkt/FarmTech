# FarmTech Backend

Django REST API backend for the FarmTech platform.

## Features

- User authentication with JWT
- Farm management
- Animal tracking
- Vaccination records
- Marketplace for agricultural products
- Notification system
- Admin panel

## Tech Stack

- Django 4.2+
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Celery for background tasks
- Redis for caching and message broker

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

4. Update the `.env` file with your configuration.

5. Create the PostgreSQL database:
```bash
createdb farmtech_db
```

6. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

9. (Optional) Run Celery worker:
```bash
celery -A farmtech_backend worker -l info
```

## API Documentation

Once the server is running, you can access:
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## API Endpoints

### Authentication
- POST `/api/users/register/` - User registration
- POST `/api/users/login/` - User login
- POST `/api/users/token/refresh/` - Refresh JWT token
- GET/PUT `/api/users/profile/` - User profile

### Farms
- GET `/api/farms/` - List farms
- POST `/api/farms/` - Create farm
- GET `/api/farms/{id}/` - Get farm details
- PUT `/api/farms/{id}/` - Update farm
- DELETE `/api/farms/{id}/` - Delete farm

### Animals
- GET `/api/animals/` - List animals
- POST `/api/animals/` - Create animal
- GET `/api/animals/{id}/` - Get animal details
- PUT `/api/animals/{id}/` - Update animal
- DELETE `/api/animals/{id}/` - Delete animal

### Vaccinations
- GET `/api/vaccinations/` - List vaccinations
- POST `/api/vaccinations/` - Create vaccination record
- GET `/api/vaccinations/{id}/` - Get vaccination details
- PUT `/api/vaccinations/{id}/` - Update vaccination
- DELETE `/api/vaccinations/{id}/` - Delete vaccination

### Marketplace
- GET `/api/marketplace/` - List products
- POST `/api/marketplace/` - Create product
- GET `/api/marketplace/{id}/` - Get product details
- PUT `/api/marketplace/{id}/` - Update product
- DELETE `/api/marketplace/{id}/` - Delete product

### Notifications
- GET `/api/notifications/` - List notifications
- POST `/api/notifications/{id}/mark_as_read/` - Mark notification as read
- POST `/api/notifications/mark_all_as_read/` - Mark all notifications as read

## Admin Panel

Access the Django admin panel at: http://localhost:8000/admin/
