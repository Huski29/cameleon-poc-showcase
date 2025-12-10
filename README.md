# Cameleon - AI Fashion Stylist

An AI-powered fashion styling platform that helps you create personalized outfits from your wardrobe using natural language descriptions. Generate hyperrealistic avatars, try on virtual clothing, and get style recommendations from AI stylists with unique personalities.

## ✨ Features

- **AI Outfit Generation**: Describe your style needs in natural language and get complete outfit recommendations
- **Virtual Try-On**: See how clothing items look on your personalized avatar using Google Gemini AI
- **Hyperrealistic Avatar**: Generate a full-body avatar from your photo with customizable height, build, and body shape
- **Smart Wardrobe Management**: Organize and search your wardrobe with AI-powered visual similarity search
- **6 AI Stylists**: Choose from different stylist personalities (Smart Casual, Formal, Streetwear, Bohemian, Minimalist, Classic)
- **Vector Search**: Fast semantic search using FashionCLIP embeddings and PostgreSQL pgvector

## 🛠️ Tech Stack

**Frontend:**
- Next.js 15 (App Router)
- TypeScript
- Tailwind CSS
- Zustand (state management)

**Backend:**
- FastAPI (Python)
- PostgreSQL 14+ with pgvector extension
- Redis (caching)
- Marqo-FashionCLIP (fashion embeddings)
- Google Gemini API (avatar & try-on generation)
- OpenAI GPT-4 (outfit generation)

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL 14+ with pgvector extension
- Redis (optional, for caching)

### 1. Database Setup

```bash
cd backend
./setup_postgres.sh
```

This script will:
- Create the database and user
- Install the pgvector extension
- Set up the schema

### 2. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create `backend/.env`:
```env
DATABASE_URL=postgresql://cameleon_user:cameleon_password_2024@localhost:5432/cameleon_db
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here
REDIS_URL=redis://localhost:6379
```

**API Keys:**
- Get OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
- Get Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 3. Seed Database

```bash
python seed.py
```

This creates a default user and populates the database with initial data.

### 4. Start Backend

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Backend API runs at http://localhost:8000  
API documentation at http://localhost:8000/api/docs

### 5. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at http://localhost:3000

## 📁 Project Structure

```
cameleon-poc-showcase/
├── frontend/
│   ├── app/
│   │   ├── components/     # React components
│   │   ├── stores/          # Zustand state management
│   │   ├── generate/        # Outfit generation page
│   │   ├── wardrobe/        # Wardrobe management
│   │   ├── profile/         # User profile & avatar
│   │   └── try-on/          # Virtual try-on feature
│   └── public/              # Static assets
├── backend/
│   ├── app/
│   │   ├── api/            # FastAPI routes
│   │   ├── services/       # Business logic & AI services
│   │   ├── models.py       # SQLAlchemy models
│   │   └── schemas.py     # Pydantic schemas
│   ├── seed.py             # Database seeding script
│   └── setup_postgres.sh   # Database setup script
└── README.md
```

## 🎨 How It Works

### Outfit Generation Flow

1. **User Input**: Describe your style need (e.g., "casual outfit for a coffee date")
2. **Intent Parsing**: GPT-4 analyzes the request and extracts style preferences
3. **Vector Search**: FashionCLIP finds similar items from your wardrobe using semantic search
4. **Styling Logic**: AI stylist combines items based on fashion rules, color theory, and personal style
5. **Result**: Complete outfit with styling tips and recommendations

### Avatar Generation

1. **Photo Upload**: User uploads a photo of themselves
2. **Body Measurements**: User selects height, build, and body shape
3. **AI Generation**: Google Gemini creates a hyperrealistic full-body avatar
4. **Customization**: Avatar reflects user's facial features, age, and selected body characteristics

### Virtual Try-On

1. **Avatar Selection**: Use your generated avatar or upload a photo
2. **Clothing Selection**: Choose items from your wardrobe
3. **AI Try-On**: Gemini AI dresses the avatar in selected clothing
4. **Result**: See how the outfit looks on your avatar

## 🤖 AI Stylists

Each stylist has a unique fashion philosophy:

- **Alex Rivera** - Smart Casual (sophisticated comfort)
- **Victoria Sterling** - Formal (timeless elegance)
- **Jordan Kim** - Streetwear (bold & expressive)
- **Luna Flores** - Bohemian (free-spirited)
- **Emma Chen** - Minimalist (less is more)
- **Richard Hartford** - Classic (traditional refinement)

## 🔍 Features in Detail

### Vector Search
Uses [Marqo-FashionCLIP](https://huggingface.co/Marqo/marqo-fashionCLIP), a state-of-the-art fashion embeddings model that outperforms previous models by 45-57% on text-to-image search tasks.

### Caching
Redis caching for wardrobe endpoints to improve performance with large datasets.

### Pagination
Efficient pagination for wardrobe items to handle large collections.

## 📝 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DATABASE_URL` | PostgreSQL connection string | Yes |
| `OPENAI_API_KEY` | OpenAI API key for GPT-4 | Yes |
| `GEMINI_API_KEY` | Google Gemini API key | Yes (for avatar/try-on) |
| `REDIS_URL` | Redis connection string | No (optional) |

## 🧪 Development

### Running Tests
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

### Code Quality
```bash
# Backend linting
cd backend
flake8 app/
black app/

# Frontend linting
cd frontend
npm run lint
```

## 📦 Deployment

### Production Build

**Backend:**
```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

**Frontend:**
```bash
cd frontend
npm run build
npm start
```

### Using PM2

```bash
pm2 start ecosystem.config.js
```

## 🔒 Security Notes

- Backend binds to `127.0.0.1` by default (not exposed publicly)
- Use reverse proxy (nginx) for production
- Environment variables should never be committed
- Database credentials should be strong and unique

## 📄 License

MIT License

## 🙏 Acknowledgments

- [Marqo-FashionCLIP](https://huggingface.co/Marqo/marqo-fashionCLIP) for fashion embeddings
- [Google Gemini](https://deepmind.google/technologies/gemini/) for image generation
- [OpenAI GPT-4](https://openai.com/gpt-4) for outfit generation

## 📧 Support

For issues and questions, please open an issue on GitHub.
