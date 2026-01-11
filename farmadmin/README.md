# FarmTech Admin Web Application

React-based admin dashboard for managing the FarmTech platform.

## Features

- User authentication with JWT
- Dashboard with statistics
- Farm management (CRUD)
- Animal management (CRUD)
- Vaccination tracking
- Marketplace product management
- Notifications

## Tech Stack

- React 18
- Material-UI (MUI)
- React Router
- Axios for API calls

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

3. Update the `.env` file with your API URL:
```
REACT_APP_API_URL=http://localhost:8000/api
```

4. Start the development server:
```bash
npm start
```

The application will open at http://localhost:3000

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm test` - Launches the test runner
- `npm run build` - Builds the app for production
- `npm run eject` - Ejects from Create React App (one-way operation)

## API Integration

The app communicates with the Django backend via REST API. Make sure the backend is running at the URL specified in your `.env` file.

## Default Admin Credentials

After setting up the backend, create an admin user with:
```bash
python manage.py createsuperuser
```

## Project Structure

```
src/
├── components/      # Reusable React components
│   └── Layout.js   # Main layout with sidebar
├── context/        # React context providers
│   └── AuthContext.js
├── pages/          # Page components
│   ├── Dashboard.js
│   ├── Login.js
│   ├── Farms.js
│   └── Animals.js
├── services/       # API service layers
│   ├── api.js
│   ├── authService.js
│   └── dataService.js
└── App.js          # Main app component with routing
```
