# FarmTech User Web Application

React-based web interface for FarmTech users to manage their farms and participate in the marketplace.

## Features

- User registration and authentication
- Personal dashboard with statistics
- Farm management
- Animal tracking
- Marketplace browsing
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

The application will open at http://localhost:3001 (or another port if 3000 is taken)

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm test` - Launches the test runner
- `npm run build` - Builds the app for production

## API Integration

The app communicates with the Django backend via REST API. Make sure the backend is running at the URL specified in your `.env` file.

## User Registration

New users can register directly from the login page. After registration, they can:
- Create and manage their farms
- Add and track animals
- Browse the marketplace
- Receive notifications

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
│   ├── MyFarms.js
│   └── Marketplace.js
├── services/       # API service layers
│   ├── api.js
│   ├── authService.js
│   └── dataService.js
└── App.js          # Main app component with routing
```
