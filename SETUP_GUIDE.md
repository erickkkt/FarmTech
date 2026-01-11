# FarmTech - Quick Setup Guide

This guide will help you get all components of the FarmTech platform running.

## Prerequisites Checklist

- [ ] Python 3.9 or higher installed
- [ ] Node.js 18 or higher installed
- [ ] PostgreSQL 12 or higher installed
- [ ] Redis installed (optional, for background tasks)
- [ ] Git installed

For mobile development:
- [ ] React Native CLI installed
- [ ] Android Studio (for Android development)
- [ ] Xcode (for iOS development, macOS only)

## Step-by-Step Setup

### 1. Database Setup

Create a PostgreSQL database:

```bash
# Login to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE farmtech_db;

# Create user (optional)
CREATE USER farmtech_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE farmtech_db TO farmtech_user;

# Exit PostgreSQL
\q
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env file with your database credentials

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

Backend will be available at: http://localhost:8000
- API Documentation: http://localhost:8000/swagger/
- Admin Panel: http://localhost:8000/admin/

### 3. Web Admin Setup

Open a new terminal:

```bash
cd farmadmin

# Install dependencies
npm install

# Configure environment
cp .env.example .env
# Edit .env to point to backend API (default: http://localhost:8000/api)

# Start development server
npm start
```

Admin app will be available at: http://localhost:3000

### 4. Web User Setup

Open a new terminal:

```bash
cd webuser

# Install dependencies
npm install

# Configure environment
cp .env.example .env
# Edit .env to point to backend API (default: http://localhost:8000/api)

# Start development server
npm start
```

User app will be available at: http://localhost:3001 (or next available port)

### 5. Mobile Admin Setup (Optional)

```bash
cd MobileAdmin

# Install dependencies
npm install

# Install required packages from PACKAGES_TO_INSTALL.txt
npm install @react-navigation/native @react-navigation/native-stack @react-navigation/drawer react-native-screens react-native-gesture-handler axios @react-native-async-storage/async-storage react-native-dotenv react-native-vector-icons

# For iOS only
cd ios && pod install && cd ..

# Configure environment
cp .env.example .env
# Edit .env with your API URL (use 10.0.2.2 for Android emulator, localhost for iOS)

# Run on Android
npx react-native run-android

# Or run on iOS (macOS only)
npx react-native run-ios
```

### 6. Mobile User Setup (Optional)

```bash
cd MobileUser

# Install dependencies
npm install

# Install required packages from PACKAGES_TO_INSTALL.txt
npm install @react-navigation/native @react-navigation/native-stack @react-navigation/drawer react-native-screens react-native-gesture-handler axios @react-native-async-storage/async-storage react-native-dotenv react-native-vector-icons

# For iOS only
cd ios && pod install && cd ..

# Configure environment
cp .env.example .env
# Edit .env with your API URL

# Run on Android
npx react-native run-android

# Or run on iOS (macOS only)
npx react-native run-ios
```

## Testing the Setup

1. **Backend**: Visit http://localhost:8000/swagger/ to see API documentation
2. **Admin Login**: 
   - Go to http://localhost:3000/login
   - Use the superuser credentials you created
3. **User Registration**: 
   - Go to http://localhost:3001/login
   - Click "Register" tab to create a new user account
4. **Create Test Data**: Use the admin panel or API to create farms, animals, etc.

## Troubleshooting

### Backend Issues

**Database connection error:**
- Verify PostgreSQL is running
- Check database credentials in `.env`
- Ensure database exists

**Import errors:**
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

### Frontend Issues

**Module not found:**
- Delete `node_modules` and `package-lock.json`
- Run `npm install` again

**API connection error:**
- Verify backend is running on port 8000
- Check CORS settings in backend
- Verify API_URL in `.env`

### Mobile Issues

**Metro bundler error:**
- Clear cache: `npx react-native start --reset-cache`
- Clean build: `cd android && ./gradlew clean`

**Unable to connect to API:**
- Use correct IP address for your development machine
- Android emulator: `http://10.0.2.2:8000/api`
- iOS simulator: `http://localhost:8000/api`
- Physical device: `http://YOUR_IP:8000/api`

## Default Ports

- Backend: 8000
- Web Admin: 3000
- Web User: 3001
- PostgreSQL: 5432
- Redis: 6379

## Next Steps

1. Create your first farm in the admin panel
2. Add animals to the farm
3. Schedule vaccinations
4. List products in the marketplace
5. Explore the API documentation

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React Documentation](https://react.dev/)
- [React Native Documentation](https://reactnative.dev/)
- [Material-UI](https://mui.com/)

## Getting Help

- Check the README files in each component directory
- Review API documentation at /swagger/
- Open an issue on GitHub
- Contact: support@farmtech.com

## Development Tips

- Always activate the Python virtual environment when working on backend
- Use `python manage.py makemigrations` after model changes
- Run `npm start` for hot-reloading in web apps
- Use React DevTools and Redux DevTools for debugging
- Test API endpoints with Swagger UI or Postman
- Use `git branch` to work on features separately
