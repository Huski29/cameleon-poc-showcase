from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app import models, schemas
from app.services.fashionclip_service import fashionclip_service
import json

router = APIRouter()

DEFAULT_USER_ID = "user-1"

@router.get("", response_model=List[schemas.WardrobeItemResponse])
async def get_wardrobe_items(
    category: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.WardrobeItem).filter(models.WardrobeItem.user_id == DEFAULT_USER_ID)
    
    if category:
        query = query.filter(models.WardrobeItem.category == category)
    
    items = query.all()
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
    return None

