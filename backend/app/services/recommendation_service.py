from sqlalchemy.orm import Session
from sqlalchemy import text, func
from app import models
from app.services.fashionclip_service import fashionclip_service
from typing import List, Dict, Optional
import json
import os

class RecommendationService:
    
    def _is_postgresql(self) -> bool:
        """Check if we're using PostgreSQL"""
        db_url = os.getenv("DATABASE_URL", "sqlite:///./cameleon.db")
        return db_url.startswith("postgresql")
    
    def search_similar_items(
        self, 
        db: Session, 
        query_text: str, 
        user_id: str,
        gender: str = "female",
        category: Optional[str] = None,
        top_k: int = 50
    ) -> List[models.WardrobeItem]:
        """
        Search for similar wardrobe items using text embeddings.
        Uses pgvector for PostgreSQL, falls back to basic filtering for SQLite.
        """
        # Enhance query with prompt template for better CLIP performance
        # Fashion-CLIP models work better with descriptive prompts
        enhanced_query = f"a photo of {query_text}" if not query_text.startswith("a photo of") else query_text
        query_embedding = fashionclip_service.generate_text_embedding(enhanced_query)
        
        if not query_embedding:
            return db.query(models.WardrobeItem).filter(
                models.WardrobeItem.user_id == user_id
            ).limit(top_k).all()
        
        # Use pgvector for PostgreSQL
        if self._is_postgresql():
            print(f"Searching items with pgvector cosine similarity...")
            print(f"Query embedding type: {type(query_embedding)}, length: {len(query_embedding)}")
            
            # Build the base query with vector similarity search
            # Pass the embedding list directly to cosine_distance
            query_obj = db.query(models.WardrobeItem).filter(
                models.WardrobeItem.user_id == user_id,
                models.WardrobeItem.text_embedding.isnot(None)
            )
            
            if category:
                query_obj = query_obj.filter(models.WardrobeItem.category == category)
            
            query_obj = query_obj.filter(
                (models.WardrobeItem.gender == gender) | (models.WardrobeItem.gender == 'unisex')
            )
            
            # Order by cosine similarity (lower distance = more similar)
            # pgvector's cosine_distance accepts the embedding list directly
            query_obj = query_obj.order_by(
                models.WardrobeItem.text_embedding.cosine_distance(query_embedding)
            )
            
            items = query_obj.limit(top_k).all()
            return items
        
        # Fallback for SQLite - basic filtering
        else:
            print(f"Searching items with basic query (SQLite mode)...")
            
            query_obj = db.query(models.WardrobeItem).filter(
                models.WardrobeItem.user_id == user_id,
                models.WardrobeItem.text_embedding != None
            )
            
            if category:
                query_obj = query_obj.filter(models.WardrobeItem.category == category)
            
            query_obj = query_obj.filter(
                (models.WardrobeItem.gender == gender) | (models.WardrobeItem.gender == 'unisex')
            )
            
            items = query_obj.limit(top_k).all()
            return items
    
    def filter_by_context(
        self,
        items: List[models.WardrobeItem],
        weather_temp: Optional[float] = None,
        occasion: Optional[str] = None,
        season: Optional[str] = None
    ) -> List[models.WardrobeItem]:
        filtered = items
        
        if weather_temp is not None:
            if weather_temp < 10:
                filtered = [i for i in filtered if i.season in ['winter', 'fall', 'all', None]]
            elif weather_temp > 25:
                filtered = [i for i in filtered if i.season in ['summer', 'spring', 'all', None]]
        
        if occasion and filtered:
            filtered = [
                i for i in filtered 
                if not i.occasions or occasion.lower() in (i.occasions or "").lower()
            ]
        
        if season and filtered:
            filtered = [
                i for i in filtered 
                if not i.season or i.season == season or i.season == 'all'
            ]
        
        return filtered if filtered else items
    
    def group_by_category(self, items: List[models.WardrobeItem]) -> Dict[str, List]:
        grouped = {"tops": [], "bottoms": [], "shoes": [], "accessories": []}
        
        for item in items:
            if item.category in grouped:
                grouped[item.category].append(item)
        
        return grouped

recommendation_service = RecommendationService()

