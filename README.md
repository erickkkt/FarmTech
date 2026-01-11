# FarmTech

A comprehensive farm management platform with backend API, web applications, and mobile apps for both administrators and users.

## Project Overview

FarmTech is a full-stack agricultural technology platform that enables farmers to:
- Manage their farms and livestock
- Track animal vaccinations and health records
- Participate in an agricultural marketplace
- Receive notifications and reminders
- Access admin tools for platform management

## Architecture

The project consists of 5 main components:

### 1. Backend (Django + Django REST Framework)
Located in `/backend`
- Python/Django REST API
- PostgreSQL database
- JWT authentication
- Celery for background tasks
- Redis for caching and message broker

### 2. Web Admin Application (React)
Located in `/farmadmin`
- React 18 with Material-UI
- Admin dashboard with analytics
- CRUD operations for all entities
- User management

### 3. Web User Application (React)
Located in `/webuser`
- React 18 with Material-UI
- User-friendly interface for farmers
- Farm and animal management
- Marketplace browsing

### 4. Mobile Admin App (React Native)
Located in `/MobileAdmin`
- React Native for iOS and Android
- Admin functionality on mobile
- Push notifications

### 5. Mobile User App (React Native)
Located in `/MobileUser`
- React Native for iOS and Android
- Mobile-first user experience
- Push notifications for reminders

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- PostgreSQL 12+
- Redis (optional, for Celery)
- React Native development environment (for mobile apps)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/erickkkt/FarmTech.git
cd FarmTech
```

2. **Set up the Backend**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your database credentials
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

3. **Set up Web Admin**
```bash
cd farmadmin
npm install
cp .env.example .env
# Edit .env with backend API URL
npm start
```

4. **Set up Web User**
```bash
cd webuser
npm install
cp .env.example .env
# Edit .env with backend API URL
npm start
```

5. **Set up Mobile Apps (Optional)**
```bash
# For Admin App
cd MobileAdmin
npm install
# Configure .env file
npx react-native run-android  # or run-ios

# For User App
cd MobileUser
npm install
# Configure .env file
npx react-native run-android  # or run-ios
```

## API Documentation

Once the backend is running, access the API documentation at:
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## Key Features

### User Management
- JWT-based authentication
- Role-based access control (Admin/User)
- User profiles and settings

### Farm Management
- Create and manage multiple farms
- Track farm details (location, size, description)
- View farm statistics

### Animal Management
- Register and track animals
- Record animal details (type, breed, health status)
- Unique tag number system
- Health monitoring

### Vaccination Tracking
- Schedule vaccinations
- Record vaccination history
- Track due dates
- Veterinarian information

### Marketplace
- List products for sale
- Browse available products
- Category-based filtering
- Product images and descriptions

### Notifications
- System notifications
- Vaccination reminders
- Marketplace updates
- Custom notifications

## Technology Stack

### Backend
- **Framework**: Django 4.2+
- **API**: Django REST Framework
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Database**: PostgreSQL
- **Task Queue**: Celery
- **Message Broker**: Redis
- **Documentation**: drf-yasg (Swagger/OpenAPI)

### Frontend (Web)
- **Framework**: React 18
- **UI Library**: Material-UI (MUI)
- **Routing**: React Router v6
- **HTTP Client**: Axios
- **State Management**: React Context API

### Mobile
- **Framework**: React Native
- **Navigation**: React Navigation
- **HTTP Client**: Axios
- **Storage**: AsyncStorage

## Project Structure

```
FarmTech/
├── backend/                 # Django backend
│   ├── farmtech_backend/   # Main Django project
│   ├── users/              # User management app
│   ├── farms/              # Farm management app
│   ├── animals/            # Animal tracking app
│   ├── vaccinations/       # Vaccination records app
│   ├── marketplace/        # Marketplace app
│   ├── notifications/      # Notifications app
│   └── requirements.txt    # Python dependencies
├── farmadmin/              # React admin web app
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── context/
│   └── package.json
├── webuser/                # React user web app
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── context/
│   └── package.json
├── MobileAdmin/            # React Native admin app
│   ├── src/
│   │   ├── screens/
│   │   ├── services/
│   │   └── navigation/
│   └── package.json
└── MobileUser/             # React Native user app
    ├── src/
    │   ├── screens/
    │   ├── services/
    │   └── navigation/
    └── package.json
```

## Development

### Backend Development
```bash
cd backend
source venv/bin/activate
python manage.py runserver

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run Celery worker (optional)
celery -A farmtech_backend worker -l info
```

### Frontend Development
```bash
# Admin App
cd farmadmin && npm start

# User App
cd webuser && npm start
```

### Mobile Development
```bash
# Admin App
cd MobileAdmin && npx react-native run-android

# User App
cd MobileUser && npx react-native run-ios
```

## Testing

### Backend
```bash
cd backend
python manage.py test
```

### Frontend
```bash
cd farmadmin  # or webuser
npm test
```

## Deployment

### Backend
- Configure production settings in `.env`
- Set DEBUG=False
- Use proper SECRET_KEY
- Configure allowed hosts
- Set up PostgreSQL production database
- Configure static files serving
- Use gunicorn or uwsgi as WSGI server

### Frontend (Web)
```bash
npm run build
# Deploy the build folder to your hosting service
```

### Mobile Apps
- Build release APK/AAB for Android
- Archive and submit to App Store for iOS

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Support

For support, email support@farmtech.com or open an issue in the repository.

## Authors

- FarmTech Team

## Acknowledgments

- Django and Django REST Framework communities
- React and React Native communities
- All contributors to this project

