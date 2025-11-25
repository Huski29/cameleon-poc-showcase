from sqlalchemy.orm import Session
from sqlalchemy import text, func
from app import models
from app.services.fashionclip_service import fashionclip_service
from typing import List, Dict, Optional
import json

class RecommendationService:
    
    def search_similar_items(
        self, 
        db: Session, 
        query_text: str, 
        user_id: str,
        gender: str = "female",
        category: Optional[str] = None,
        top_k: int = 50
    ) -> List[models.WardrobeItem]:
        query_embedding = fashionclip_service.generate_text_embedding(query_text)
        
        if not query_embedding:
            return db.query(models.WardrobeItem).filter(
                models.WardrobeItem.user_id == user_id
            ).limit(top_k).all()
        
        try:
            query_sql = """
                SELECT *, 
                       1 - (text_embedding <=> :query_embedding::vector) as similarity
                FROM wardrobe_items
                WHERE user_id = :user_id
                      AND text_embedding IS NOT NULL
                      AND (gender = :gender OR gender = 'unisex')
            """
            
            if category:
                query_sql += " AND category = :category"
            
            query_sql += """
                ORDER BY text_embedding <=> :query_embedding::vector
                LIMIT :top_k
            """
            
            params = {
                "query_embedding": str(query_embedding),
                "user_id": user_id,
                "gender": gender,
                "top_k": top_k
            }
            
            if category:
                params["category"] = category
            
            results = db.execute(text(query_sql), params).fetchall()
            
            items = []
            for row in results:
                item = db.query(models.WardrobeItem).filter(
                    models.WardrobeItem.id == row.id
                ).first()
                if item:
                    items.append(item)
            
            return items
        except Exception as e:
            print(f"Vector search failed: {e}. Falling back to basic query.")
            query_obj = db.query(models.WardrobeItem).filter(
                models.WardrobeItem.user_id == user_id
            )
            
            if category:
                query_obj = query_obj.filter(models.WardrobeItem.category == category)
            
            query_obj = query_obj.filter(
                (models.WardrobeItem.gender == gender) | (models.WardrobeItem.gender == 'unisex')
            )
            
            return query_obj.limit(top_k).all()
    
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

