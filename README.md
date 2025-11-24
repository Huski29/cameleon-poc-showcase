# Cameleon - AI Fashion Stylist

An AI-powered outfit generator and wardrobe manager built with Next.js and FastAPI.

## Stack

**Frontend:** Next.js 15, TypeScript, Tailwind CSS, Zustand  
**Backend:** FastAPI, SQLAlchemy, SQLite

## Getting Started

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python seed.py
uvicorn app.main:app --reload --port 8000
```

API: http://localhost:8000  
Docs: http://localhost:8000/api/docs

### Frontend

```bash
cd frontend
npm install
npm run dev
```

App: http://localhost:3000

## Features

- Create personalized style avatars
- Generate outfits with natural language
- Manage virtual wardrobe
- Save favorite outfit combinations
- Customize style preferences

## API Endpoints

### Users
- `GET /api/v1/users/profile`
- `PUT /api/v1/users/profile`
- `PUT /api/v1/users/avatar`
- `PUT /api/v1/users/preferences`

### Wardrobe
- `GET /api/v1/wardrobe`
- `POST /api/v1/wardrobe`
- `DELETE /api/v1/wardrobe/{id}`

### Outfits
- `POST /api/v1/outfits/generate`
- `GET /api/v1/outfits`
- `GET /api/v1/outfits/history`
- `POST /api/v1/outfits/{id}/save`

### Notifications
- `GET /api/v1/notifications`
- `PUT /api/v1/notifications/{id}/read`

## Development

This is a POC with mock AI responses. Currently single-user (no auth).

Reset database:
```bash
rm backend/cameleon.db && python backend/seed.py
```

## License

MIT
