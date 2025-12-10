from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional
from datetime import datetime
from app.database import get_db
from app import models, schemas
from app.services.fashionclip_service import fashionclip_service
from app.services.cache_service import get_cached, set_cached, delete_cached_pattern, get_cache_key
import json

router = APIRouter()

DEFAULT_USER_ID = "user-1"

@router.get("", response_model=List[schemas.WardrobeItemResponse])
async def get_wardrobe_items(
    category: Optional[str] = Query(None),
    limit: Optional[int] = Query(None, ge=1, le=100),
    offset: Optional[int] = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    """
    Get wardrobe items with pagination support.
    
    Args:
        category: Filter by category (tops, bottoms, shoes, accessories)
        limit: Number of items to return (default: all, max: 100)
        offset: Number of items to skip (default: 0)
    """
    # Get user to filter by gender
    user = db.query(models.User).filter(models.User.id == DEFAULT_USER_ID).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Generate cache key based on user gender, category, limit, and offset
    cache_key = get_cache_key("wardrobe", DEFAULT_USER_ID, user.gender, category or "all", limit or "all", offset)
    
    # Try to get from cache
    cached_items = get_cached(cache_key)
    if cached_items is not None:
        # Convert cached dicts back to Pydantic models
        # Handle datetime conversion from ISO strings
        converted_items = []
        for item in cached_items:
            if item.get('created_at') and isinstance(item['created_at'], str):
                item['created_at'] = datetime.fromisoformat(item['created_at'])
            if item.get('updated_at') and isinstance(item['updated_at'], str):
                item['updated_at'] = datetime.fromisoformat(item['updated_at'])
            converted_items.append(schemas.WardrobeItemResponse(**item))
        return converted_items
    
    # Filter items by user's gender (show items matching user's gender + unisex items)
    query = db.query(models.WardrobeItem).filter(
        models.WardrobeItem.user_id == DEFAULT_USER_ID
    ).filter(
        or_(
            models.WardrobeItem.gender == user.gender,
            models.WardrobeItem.gender == 'unisex'
        )
    )
    
    if category:
        query = query.filter(models.WardrobeItem.category == category)
    
    # Apply pagination
    if limit:
        query = query.offset(offset).limit(limit)
    
    items = query.all()
    
    # Cache for 1 hour (3600 seconds)
    # Convert to dict for caching (exclude embeddings to save space)
    items_dict = [
        {
            "id": item.id,
            "user_id": item.user_id,
            "category": item.category,
            "image": item.image,
            "alt": item.alt,
            "title": item.title,
            "description": item.description,
            "brand": item.brand,
            "color": item.color,
            "style_tags": item.style_tags,
            "occasions": item.occasions,
            "season": item.season,
            "gender": item.gender,
            "created_at": item.created_at.isoformat() if item.created_at else None,
            "updated_at": item.updated_at.isoformat() if item.updated_at else None
        }
        for item in items
    ]
    set_cached(cache_key, items_dict, ttl=3600)
    
    return items

@router.get("/{item_id}", response_model=schemas.WardrobeItemResponse)
async def get_wardrobe_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = db.query(models.WardrobeItem).filter(
        models.WardrobeItem.id == item_id,
        models.WardrobeItem.user_id == DEFAULT_USER_ID
    ).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Wardrobe item not found")
    
    return item

@router.post("", response_model=schemas.WardrobeItemResponse, status_code=201)
async def add_wardrobe_item(
    item: schemas.WardrobeItemCreate,
    db: Session = Depends(get_db)
):
    db_item = models.WardrobeItem(
        user_id=DEFAULT_USER_ID,
        category=item.category,
        image=item.image,
        alt=item.alt,
        title=item.title,
        description=item.description,
        brand=item.brand,
        color=item.color,
        style_tags=item.style_tags,
        occasions=item.occasions,
        season=item.season,
        gender=item.gender
    )
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    item_data = {
        "image": item.image,
        "title": item.title,
        "description": item.description,
        "color": item.color,
        "brand": item.brand,
        "style_tags": json.loads(item.style_tags) if item.style_tags else []
    }
    
    image_emb, text_emb = fashionclip_service.generate_item_embeddings(item_data)
    
    if image_emb and text_emb:
        db_item.image_embedding = image_emb
        db_item.text_embedding = text_emb
        db.commit()
        db.refresh(db_item)
    
    # Invalidate wardrobe cache
    delete_cached_pattern("cameleon:wardrobe:*")
    
    return db_item

@router.delete("/{item_id}", status_code=204)
async def delete_wardrobe_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = db.query(models.WardrobeItem).filter(
        models.WardrobeItem.id == item_id,
        models.WardrobeItem.user_id == DEFAULT_USER_ID
    ).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Wardrobe item not found")
    
    db.delete(item)
    db.commit()
    
    # Invalidate wardrobe cache
    delete_cached_pattern("cameleon:wardrobe:*")
    
    return None

