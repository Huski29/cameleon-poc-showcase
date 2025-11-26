# Cameleon - AI Fashion Stylist

AI-powered outfit generator that helps you create stylish looks from your wardrobe using natural language.

## What It Does

- Chat with AI stylists to generate outfit combinations
- Manage your virtual wardrobe with real fashion items
- Get personalized recommendations based on your style preferences
- Choose from 6 different stylist personalities (from Minimalist to Streetwear)

## Tech Stack

**Frontend:** Next.js 15, TypeScript, Tailwind CSS  
**Backend:** FastAPI, PostgreSQL + pgvector, FashionCLIP  
**AI:** GPT-4 for outfit generation, FashionCLIP for visual similarity

## Quick Start

### 1. Setup PostgreSQL

```bash
cd backend
./setup_postgres.sh
```

### 2. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Add your OPENAI_API_KEY

# Seed initial data
python seed.py

# Start server
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Backend runs at http://localhost:8000

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at http://localhost:3000

## Adding Fashion Items

You can load a real fashion dataset from Kaggle:

1. Download [Fashion Product Images Dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset)
2. Extract to `backend/` folder
3. Run `python load_kaggle_fashion_data.py`

This loads 400 items (100 per category) with AI-generated embeddings.

## How It Works

1. You describe what you want: "casual outfit for a coffee date"
2. GPT-4 parses your intent and style preferences
3. FashionCLIP finds similar items from your wardrobe using vector search
4. AI stylist combines them based on fashion rules and color theory
5. You get a complete outfit with styling tips

## AI Stylists

Each stylist has a unique approach:

- **Alex Rivera** - Smart Casual (sophisticated comfort)
- **Victoria Sterling** - Formal (timeless elegance)
- **Jordan Kim** - Streetwear (bold & expressive)
- **Luna Flores** - Bohemian (free-spirited)
- **Emma Chen** - Minimalist (less is more)
- **Richard Hartford** - Classic (traditional refinement)

## Environment Setup

Create `backend/.env`:
```env
DATABASE_URL=postgresql://cameleon_user:cameleon_password_2024@localhost:5432/cameleon_db
OPENAI_API_KEY=your_key_here
```

## Project Structure

```
cameleon-poc-showcase/
├── frontend/          # Next.js app
│   └── app/
│       ├── generate/  # Outfit generation
│       ├── wardrobe/  # Wardrobe manager
│       └── profile/   # User settings
└── backend/           # FastAPI server
    ├── app/
    │   ├── api/       # REST endpoints
    │   └── services/  # AI & business logic
    └── load_kaggle_fashion_data.py
```

## Notes

- Currently single-user (no auth system)
- Images stored as base64 in database
- Vector embeddings enable smart fashion search
- Requires PostgreSQL 14+ with pgvector extension

## License

MIT
