# FarmTech Architecture

This document describes the architecture and design of the FarmTech platform.

## System Overview

FarmTech is a full-stack agricultural management platform consisting of:
- 1 Backend API (Django)
- 2 Web Applications (React)
- 2 Mobile Applications (React Native)

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         FarmTech Platform                        │
└─────────────────────────────────────────────────────────────────┘

┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│   Web Admin   │    │   Web User    │    │  Mobile Apps  │
│   (React)     │    │   (React)     │    │(React Native) │
│   Port 3000   │    │   Port 3001   │    │  iOS/Android  │
└───────┬───────┘    └───────┬───────┘    └───────┬───────┘
        │                    │                    │
        │         HTTP/REST API (JWT Auth)        │
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                    ┌────────▼────────┐
                    │  Django Backend │
                    │    Port 8000    │
                    │  - REST API     │
                    │  - JWT Auth     │
                    │  - CORS Enabled │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
  ┌─────▼─────┐      ┌──────▼──────┐     ┌──────▼──────┐
  │PostgreSQL │      │   Redis     │     │   Celery    │
  │ Database  │      │   Cache     │     │   Workers   │
  │ Port 5432 │      │ Port 6379   │     │  Async Jobs │
  └───────────┘      └─────────────┘     └─────────────┘
```

## Backend Architecture

### Django Project Structure

```
backend/
├── farmtech_backend/      # Main project
│   ├── settings.py       # Configuration
│   ├── urls.py           # URL routing
│   ├── celery.py         # Celery config
│   └── wsgi.py           # WSGI entry
├── users/                # User management
│   ├── models.py         # User model
│   ├── serializers.py    # User serializers
│   ├── views.py          # User views
│   └── urls.py           # User URLs
├── farms/                # Farm management
├── animals/              # Animal tracking
├── vaccinations/         # Vaccination records
├── marketplace/          # Product marketplace
└── notifications/        # Notification system
```

### API Endpoints

#### Authentication
- POST `/api/users/register/` - User registration
- POST `/api/users/login/` - User login (JWT)
- POST `/api/users/token/refresh/` - Refresh JWT token
- GET/PUT `/api/users/profile/` - User profile

#### Farms
- GET `/api/farms/` - List farms
- POST `/api/farms/` - Create farm
- GET `/api/farms/{id}/` - Get farm
- PUT `/api/farms/{id}/` - Update farm
- DELETE `/api/farms/{id}/` - Delete farm

#### Animals
- GET `/api/animals/` - List animals
- POST `/api/animals/` - Create animal
- GET `/api/animals/{id}/` - Get animal
- PUT `/api/animals/{id}/` - Update animal
- DELETE `/api/animals/{id}/` - Delete animal

#### Vaccinations
- GET `/api/vaccinations/` - List vaccinations
- POST `/api/vaccinations/` - Create vaccination
- GET `/api/vaccinations/{id}/` - Get vaccination
- PUT `/api/vaccinations/{id}/` - Update vaccination
- DELETE `/api/vaccinations/{id}/` - Delete vaccination

#### Marketplace
- GET `/api/marketplace/` - List products
- POST `/api/marketplace/` - Create product
- GET `/api/marketplace/{id}/` - Get product
- PUT `/api/marketplace/{id}/` - Update product
- DELETE `/api/marketplace/{id}/` - Delete product

#### Notifications
- GET `/api/notifications/` - List notifications
- POST `/api/notifications/{id}/mark_as_read/` - Mark as read
- POST `/api/notifications/mark_all_as_read/` - Mark all as read

## Frontend Architecture

### Web Admin Application

```
farmadmin/
├── src/
│   ├── components/        # Reusable components
│   │   └── Layout.js     # Navigation layout
│   ├── context/          # React contexts
│   │   └── AuthContext.js
│   ├── pages/            # Page components
│   │   ├── Login.js
│   │   ├── Dashboard.js
│   │   ├── Farms.js
│   │   └── Animals.js
│   ├── services/         # API services
│   │   ├── api.js        # Axios instance
│   │   ├── authService.js
│   │   └── dataService.js
│   └── App.js            # Main component
└── package.json
```

### Web User Application

Similar structure to admin app, with user-specific pages:
- Registration support
- Personal farm management
- Marketplace browsing
- Simplified interface

## Mobile Architecture

### React Native Structure

```
MobileAdmin/ or MobileUser/
├── src/
│   ├── screens/          # Screen components
│   │   ├── LoginScreen.js
│   │   ├── DashboardScreen.js
│   │   ├── FarmsScreen.js
│   │   └── AnimalsScreen.js
│   ├── navigation/       # Navigation config
│   │   └── AppNavigator.js
│   ├── components/       # Reusable components
│   ├── services/         # API services
│   │   ├── api.js
│   │   ├── authService.js
│   │   └── dataService.js
│   └── context/          # React contexts
│       └── AuthContext.js
├── android/              # Android project
├── ios/                  # iOS project
└── App.tsx               # Main component
```

## Data Models

### User Model
- username (unique)
- email
- password (hashed)
- user_type (admin/user)
- phone_number
- address
- timestamps

### Farm Model
- owner (FK to User)
- name
- location
- size (hectares)
- description
- timestamps

### Animal Model
- farm (FK to Farm)
- owner (FK to User)
- name
- animal_type
- breed
- gender
- date_of_birth
- tag_number (unique)
- weight
- health_status
- timestamps

### Vaccination Model
- animal (FK to Animal)
- vaccine_name
- date_administered
- next_due_date
- veterinarian
- batch_number
- administered_by (FK to User)
- timestamps

### Product Model (Marketplace)
- seller (FK to User)
- title
- description
- category
- price
- quantity
- status
- image
- location
- timestamps

### Notification Model
- user (FK to User)
- notification_type
- title
- message
- is_read
- created_at

## Authentication Flow

```
1. User submits credentials
   ↓
2. Backend validates credentials
   ↓
3. Backend generates JWT tokens (access + refresh)
   ↓
4. Frontend stores tokens (localStorage/AsyncStorage)
   ↓
5. Frontend includes token in Authorization header
   ↓
6. Backend validates token for each request
   ↓
7. If token expires, use refresh token to get new access token
```

## Security Features

1. **JWT Authentication**
   - Short-lived access tokens (60 min)
   - Long-lived refresh tokens (24 hours)
   - Secure token storage

2. **Password Security**
   - Passwords hashed with Django's PBKDF2
   - Password validation on registration

3. **API Security**
   - CORS configured for allowed origins
   - CSRF protection for state-changing operations
   - Rate limiting (can be added)

4. **Authorization**
   - Role-based access control (Admin/User)
   - Permission checks on API endpoints
   - Users can only access their own data

## Scalability Considerations

### Current Setup (Development)
- Single server deployment
- SQLite or PostgreSQL database
- Development server

### Production Recommendations

1. **Application Server**
   - Use Gunicorn or uWSGI
   - Deploy behind Nginx reverse proxy
   - Multiple worker processes

2. **Database**
   - PostgreSQL with connection pooling
   - Regular backups
   - Consider read replicas for scaling

3. **Caching**
   - Redis for session storage
   - Cache frequently accessed data
   - API response caching

4. **File Storage**
   - Use cloud storage (S3, GCS) for images
   - CDN for static files
   - Image optimization

5. **Background Tasks**
   - Celery workers for async tasks
   - Redis as message broker
   - Separate worker instances

6. **Monitoring**
   - Application monitoring (Sentry)
   - Performance monitoring (New Relic)
   - Log aggregation (ELK stack)

## Technology Stack Summary

### Backend
- **Framework**: Django 4.2+
- **API**: Django REST Framework 3.14+
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Task Queue**: Celery
- **Cache/Broker**: Redis
- **CORS**: django-cors-headers
- **Documentation**: drf-yasg (Swagger/OpenAPI)

### Frontend (Web)
- **Framework**: React 18
- **UI Library**: Material-UI v5
- **Routing**: React Router v6
- **HTTP Client**: Axios
- **State Management**: React Context API

### Mobile
- **Framework**: React Native 0.83+
- **Navigation**: React Navigation 6
- **HTTP Client**: Axios
- **Storage**: AsyncStorage
- **Icons**: React Native Vector Icons

### Development Tools
- **Version Control**: Git
- **Package Managers**: pip (Python), npm (JavaScript)
- **Code Quality**: ESLint, Prettier
- **API Testing**: Swagger UI, Postman

## Deployment Architecture

```
┌─────────────────────────────────────────────────┐
│                    Internet                      │
└──────────────────────┬──────────────────────────┘
                       │
              ┌────────▼────────┐
              │   Load Balancer │
              │      (Nginx)     │
              └────────┬────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
 ┌──────▼──────┐ ┌────▼─────┐ ┌──────▼──────┐
 │ Django App  │ │ Django   │ │  Django App │
 │  Server 1   │ │ Server 2 │ │  Server 3   │
 └──────┬──────┘ └────┬─────┘ └──────┬──────┘
        │              │              │
        └──────────────┼──────────────┘
                       │
        ┌──────────────┴──────────────┐
        │                             │
 ┌──────▼──────┐            ┌─────────▼────────┐
 │ PostgreSQL  │            │  Redis Cluster   │
 │   Primary   │            │  Cache/Sessions  │
 │             │            │  Message Broker  │
 │  Replicas   │            └──────────────────┘
 └─────────────┘
```

## Future Enhancements

1. **Features**
   - Real-time notifications (WebSocket)
   - Advanced analytics dashboard
   - Weather integration
   - Geolocation features
   - Photo recognition for animals

2. **Technical**
   - Microservices architecture
   - GraphQL API option
   - Progressive Web App (PWA)
   - Offline mode for mobile apps
   - Automated testing suite

3. **Scalability**
   - Kubernetes deployment
   - Database sharding
   - Elasticsearch for search
   - Message queue for events
   - API gateway
