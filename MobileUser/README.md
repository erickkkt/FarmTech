# FarmTech Mobile User App

React Native mobile application for FarmTech users to manage their farms and participate in the marketplace.

## Features

- User registration and authentication
- Personal dashboard with statistics
- Farm management
- Animal tracking
- Marketplace browsing and selling
- Push notifications
- Vaccination reminders

## Tech Stack

- React Native
- React Navigation
- Axios for API calls
- AsyncStorage for local data

## Prerequisites

- Node.js >= 18
- React Native development environment set up
- For iOS: Xcode and CocoaPods
- For Android: Android Studio and SDK

## Setup

1. Install dependencies:
```bash
npm install
# For iOS only
cd ios && pod install && cd ..
```

2. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

3. Update the `.env` file with your API URL:
```
API_URL=http://your-api-url:8000/api
```

## Running the App

### Android
```bash
npx react-native run-android
```

### iOS
```bash
npx react-native run-ios
```

## Build for Production

### Android
```bash
cd android
./gradlew assembleRelease
```

### iOS
Open `ios/MobileUser.xcworkspace` in Xcode and archive the app.

## API Integration

The app communicates with the Django backend via REST API. Make sure the backend is accessible from your mobile device/emulator.

For local development:
- Android emulator: Use `http://10.0.2.2:8000/api`
- iOS simulator: Use `http://localhost:8000/api`
- Physical device: Use your computer's IP address

## User Registration

New users can register directly from the app. After registration, they can:
- Create and manage their farms
- Add and track animals
- Browse and list products in the marketplace
- Receive push notifications for important events

## Project Structure

```
src/
├── components/     # Reusable React Native components
├── context/       # React context providers
│   └── AuthContext.js
├── navigation/    # Navigation configuration
│   └── AppNavigator.js
├── screens/       # Screen components
│   ├── LoginScreen.js
│   ├── RegisterScreen.js
│   ├── DashboardScreen.js
│   ├── FarmsScreen.js
│   ├── AnimalsScreen.js
│   └── MarketplaceScreen.js
├── services/      # API service layers
│   ├── api.js
│   ├── authService.js
│   └── dataService.js
└── App.js         # Main app component
```

## Troubleshooting

If you encounter issues:
1. Clear the cache: `npx react-native start --reset-cache`
2. Clean build folders: `cd android && ./gradlew clean`
3. Reinstall dependencies: `rm -rf node_modules && npm install`
