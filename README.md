# Cameleon - AI Fashion Stylist POC

A production-ready, modern Next.js application for AI-powered outfit generation and wardrobe management. Built with best practices, clean architecture, and optimized for performance.

## Overview

Cameleon is a proof-of-concept application that demonstrates a complete frontend implementation for an AI-powered fashion styling platform. The application allows users to create personalized style avatars, manage their virtual wardrobe, and receive AI-generated outfit recommendations.

## Key Features

### Core Functionality
- AI Avatar Generation - Create personalized style avatars based on body measurements
- Smart Outfit Generator - Natural language outfit requests with AI suggestions
- Virtual Wardrobe - Organize and manage clothing items by category
- Virtual Try-On - Preview outfits on AI-generated models
- Profile Management - Comprehensive style preferences and settings

### Technical Implementation
- Production-Ready Architecture - Clean code structure with separation of concerns
- State Management - Zustand with persistence for global state
- Fully Responsive - Optimized for mobile, tablet, and desktop (90% scale)
- Dark Mode Support - Seamless theme switching
- Accessibility - ARIA labels, keyboard navigation, screen reader support
- Glassmorphic UI - Modern frosted glass effects with backdrop blur
- Performance Optimized - React.memo, useCallback, code splitting ready
- Type-Safe - Full TypeScript coverage with strict mode
- Component Library - Reusable, modular UI components
- Mock Data Layer - Frontend-ready for backend integration

## Technology Stack

**Framework:** Next.js 15 (App Router)  
**Language:** TypeScript 5  
**Styling:** Tailwind CSS 3.4  
**State Management:** Zustand (with persist middleware)  
**Icons:** Material Symbols Outlined  
**Fonts:** Manrope (400, 500, 700, 800)  
**Optimization:** React.memo, useCallback, useMemo  

## Project Architecture

```
cameleon-poc-showcase/
├── app/
│   ├── components/           # Reusable UI components
│   │   ├── common/          # Generic components (Button, Input, Card, etc.)
│   │   ├── forms/           # Form-specific components (RangeSlider, BodyTypeSelector)
│   │   ├── layout/          # Layout components (AppHeader, Logo)
│   │   └── wardrobe/        # Wardrobe-specific components
│   ├── constants/           # Application constants
│   │   └── index.ts         # Body types, style preferences, etc.
│   ├── hooks/               # Custom React hooks
│   │   ├── useClickOutside.ts
│   │   ├── useDebounce.ts
│   │   └── useMediaQuery.ts
│   ├── lib/                 # Utility functions
│   │   ├── utils.ts         # Helper functions (cn, formatDate, etc.)
│   │   └── mock-data.ts     # Mock data for development
│   ├── stores/              # Zustand state stores
│   │   ├── useUserStore.ts       # User profile & avatar
│   │   ├── useWardrobeStore.ts   # Wardrobe items
│   │   ├── useOutfitStore.ts     # Outfit generation
│   │   └── useUIStore.ts         # UI state (notifications)
│   ├── types/               # TypeScript type definitions
│   │   ├── user.ts
│   │   ├── wardrobe.ts
│   │   ├── outfit.ts
│   │   └── notification.ts
│   ├── (pages)/             # Application pages
│   │   ├── page.tsx              # Home - Avatar creation
│   │   ├── avatar-confirmation/  # Avatar review
│   │   ├── generate/             # Outfit generation
│   │   ├── wardrobe/             # Wardrobe view
│   │   ├── outfit-result/        # Outfit display (80% scale)
│   │   ├── try-on/              # Virtual try-on (80% scale)
│   │   └── profile/             # User settings (scrollable)
│   ├── layout.tsx           # Root layout with ErrorBoundary
│   └── globals.css          # Global styles & utilities
├── public/                  # Static assets
├── tailwind.config.ts       # Tailwind configuration
├── tsconfig.json           # TypeScript configuration
└── package.json            # Dependencies
```

## Getting Started

### Prerequisites

Node.js 18.0 or higher is required, along with npm or yarn package manager.

### Installation

Navigate to the project directory and install dependencies:

```bash
cd cameleon-poc-showcase
npm install
```

### Development

Start the development server:

```bash
npm run dev
```

The application will be available at http://localhost:3000

### Production Build

To create an optimized production build:

```bash
npm run build
npm start
```

### Code Quality

Run the linter to check for code issues:

```bash
npm run lint
```

## Application Flow

### Page 1: Home (/)
Users begin by creating their style avatar. They can upload a selfie, define their proportions using custom sliders (height: petite/regular/tall, volume: lean/mid/plus), and select their body type from six options: triangle, inverted triangle, round, rectangle, trapezium, or not sure. The generate avatar button remains disabled until a body type is selected.

### Page 2: Avatar Confirmation (/avatar-confirmation)
After generating an avatar, users review the AI-generated result in a glassmorphic modal overlay. They can either confirm the avatar to proceed or regenerate it if adjustments are needed.

### Page 3: Generate Outfit (/generate)
The main outfit generation interface allows users to describe their outfit needs using natural language. Quick category pills provide shortcuts for common occasions like smart casual, summer date, dinner out, or office look. A preview of the user's wardrobe displays the first six items for context.

### Page 4: Your Wardrobe (/wardrobe)
A comprehensive view of all wardrobe items, organized by category (tops, bottoms, shoes, accessories). Each item displays with high-quality images and detailed information including brand, color, and size. The interface uses a scrollable modal design with smooth hover effects.

### Page 5: Outfit Result (/outfit-result)
Generated outfits appear in a 2x2 grid layout on the left, with detailed outfit information on the right including a title, vibe description, and item breakdown with thumbnails. Users can try on the outfit, request a new suggestion, or add it to favorites. This page uses 80% scaling for optimal viewing.

### Page 6: Try On (/try-on)
The virtual try-on page displays a full-body model preview wearing the complete outfit, accompanied by a detailed breakdown of each item. Action buttons match those on the outfit result page. This page also uses 80% scaling.

### Page 7: Profile (/profile)
A comprehensive settings page with scrollable content allows users to manage their profile picture, personal information (name, email), style avatar settings (height, volume, body type), and style preferences (preferred style, color palette, budget range). Changes can be saved or cancelled.

## Design System

### Color Palette

The application uses a carefully selected color palette optimized for both light and dark modes:

- Primary: #e8ba30 (Golden yellow for buttons and highlights)
- Background Light: #f8f7f6
- Background Dark: #211d11
- Text Light: #1b180e
- Text Dark: #f3f0e7
- Card Light: #fcfbf8
- Card Dark: #2a261a
- Border Light: #f3f0e7
- Border Dark: #3b3421

### Typography

The entire application uses the Manrope sans-serif typeface in four weights: 400 (regular), 500 (medium), 700 (bold), and 800 (extra bold). A global 90% font-size scaling ensures comfortable readability across all viewport sizes.

### Visual Effects

Glassmorphic effects create a modern frosted glass appearance using backdrop-blur(10px). Radial gradients provide smooth background transitions. Custom range sliders feature 16px golden thumbs on 4px tracks. Layered shadow effects add subtle depth throughout the interface.

### Responsive Design

The application adapts to four main breakpoint categories:
- Small (640px): Optimized for tablets
- Medium (768px): Standard desktop
- Large (1024px): Large desktop displays
- Extra Large (1280px): Wide screens

Default pages display at 90% scale via a global font-size adjustment. The try-on and outfit-result pages use an additional 80% transform scale for optimal content presentation.

## State Management

The application uses Zustand for predictable state management with four main stores:

**useUserStore** manages user profile data, avatar settings, and style preferences. It provides methods to set the complete profile, update avatar properties, update preferences, and modify user information.

**useWardrobeStore** handles all wardrobe-related operations including the collection of items, methods to add and remove items, and category-based filtering functionality.

**useOutfitStore** controls outfit generation and management. It maintains the current outfit, saved outfits collection, outfit history, and provides an asynchronous generateOutfit function that simulates API calls with mock data.

**useUIStore** manages UI state including notifications with unread counts and methods to mark individual notifications or all notifications as read.

All stores use Zustand's persist middleware to maintain state across page refreshes using local storage.

## Component Architecture

### Common Components
The common component library includes standardized Button components, form Input elements, Card containers, loading Spinner indicators, and an ErrorBoundary component for graceful error handling.

### Form Components
Specialized form components include RangeSlider for custom range inputs with labels, BodyTypeSelector for the body type grid selection interface, and CustomSelect for styled dropdown menus.

### Layout Components
Layout components consist of AppHeader, which provides navigation with notifications and profile dropdowns, and Logo, which renders the brand SVG.

### Wardrobe Components
Wardrobe-specific components include WardrobeItem for individual item cards, WardrobeGrid for grid layouts, and WardrobeCategory for organizing category sections.

## Performance Optimization

The application implements several performance optimization techniques. React.memo wraps expensive components to prevent unnecessary re-renders. Event handlers use useCallback to maintain referential equality across renders. Computed values utilize useMemo to cache expensive calculations. The component structure is optimized to minimize re-renders and is prepared for code splitting when needed.

## Accessibility Features

Accessibility is built into every interactive element. All buttons, inputs, and interactive components include proper ARIA labels. Full keyboard navigation support enables users to navigate with Tab, Enter, and Space keys. Dropdowns implement focus management to trap focus appropriately. The markup uses semantic HTML elements, and all content remains screen reader friendly.

## User Interface Details

### AppHeader Component
The header adapts responsively between mobile and desktop layouts. The notifications system displays an unread count badge and allows users to mark items as read. The profile menu provides quick navigation with user information display. Navigation links include Wardrobe, Style Guide, and Inspiration sections. Touch optimization ensures dropdowns close when clicking or tapping outside, or when scrolling.

### Scrollbar Behavior
The application implements a no-scrollbar design philosophy. Global overflow hidden styling on html and body elements prevents default scrolling. Custom scrollbars appear only where explicitly needed using the scrollbar-custom class. All content remains contained within the viewport for a clean, modern appearance. The profile page is an exception, implementing vertical scrolling with custom styled scrollbars to accommodate its longer content.

## Mock Data Implementation

All mock data centralizes in app/lib/mock-data.ts for easy management and future API integration. This includes mockUserProfile with sample user data, avatar settings, and preferences; mockWardrobeItems containing sample clothing entries; mockNotifications with example notification data; and mockOutfits featuring sample generated outfit combinations.

The mock data structure exactly matches the TypeScript interfaces defined in the types directory, making the transition to real API calls straightforward. Simply replace the mock data imports with API fetch calls to connect to a backend service.

## Future Development

This proof of concept provides a solid foundation for further development. The next phases would include:

Backend API integration with RESTful or GraphQL endpoints  
Database implementation using Prisma with PostgreSQL  
Authentication system using NextAuth.js  
Real AI image generation integration  
Payment processing for premium features  
Social sharing capabilities  
Outfit favorites and browsing history  
Advanced filtering and search functionality  
Comprehensive unit and end-to-end testing  

## Development Notes

This is a frontend-only POC currently using mock data. No backend, database, or authentication is implemented. There are no login/signup screens or protected routes. The application demonstrates the complete user interface and interaction patterns without requiring server-side infrastructure.

For production deployment, you would need to add environment variables for API keys, implement backend services, set up authentication flows, configure a database, and add comprehensive testing coverage.

## Contributing

This project demonstrates modern React and Next.js development patterns. The codebase follows industry best practices including:

- Clean code architecture with clear separation of concerns
- Comprehensive TypeScript typing throughout
- Reusable component patterns
- Efficient state management
- Accessibility-first approach
- Performance optimization techniques

## License

MIT License - See LICENSE file for details

## Project Status

Status: POC Complete - Ready for Frontend Demo  
Version: 1.0.0  
Last Updated: November 2025  

This proof of concept successfully demonstrates all planned frontend functionality. The application is ready for stakeholder review and can serve as a foundation for full-stack development when backend services are implemented.
