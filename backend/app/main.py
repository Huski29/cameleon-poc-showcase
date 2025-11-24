from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import models
from app.api import users, wardrobe, outfits, notifications

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Cameleon API",
    description="AI-powered fashion styling platform",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(wardrobe.router, prefix="/api/v1/wardrobe", tags=["wardrobe"])
app.include_router(outfits.router, prefix="/api/v1/outfits", tags=["outfits"])
app.include_router(notifications.router, prefix="/api/v1/notifications", tags=["notifications"])

@app.get("/")
async def root():
    return {"message": "Cameleon API v1.0.0", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

