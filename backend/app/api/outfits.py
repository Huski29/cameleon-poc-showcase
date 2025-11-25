from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from app.database import get_db
from app import models, schemas
from app.services.recommendation_service import recommendation_service
from app.services.gpt_service import gpt_service
from app.services.weather_service import weather_service
import uuid
import random

router = APIRouter()

DEFAULT_USER_ID = "user-1"

@router.post("/generate", response_model=schemas.OutfitResponse)
async def generate_outfit(
    request: schemas.OutfitGenerateRequest,
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == DEFAULT_USER_ID).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    intent = gpt_service.parse_intent(request.prompt)
    
    weather_data = weather_service.get_current_weather("New York")
    temp_category = weather_service.get_temperature_category(weather_data["temperature"])
    
    items = recommendation_service.search_similar_items(
        db=db,
        query_text=request.prompt,
        user_id=DEFAULT_USER_ID,
        gender=user.gender,
        top_k=50
    )
    
    filtered_items = recommendation_service.filter_by_context(
        items=items,
        weather_temp=weather_data["temperature"],
        occasion=intent.get("occasion"),
        season=None
    )
    
    grouped_items = recommendation_service.group_by_category(filtered_items)
    
    context = {
        "prompt": request.prompt,
        "weather_condition": weather_data.get("condition"),
        "temperature": weather_data.get("temperature"),
        "intent": intent
    }
    
    user_prefs = {
        "style_preference": user.style_preference,
        "color_palette": user.color_palette,
        "budget": user.budget
    }
    
    gpt_result = gpt_service.generate_outfit(grouped_items, context, user_prefs)
    
    selected = gpt_result.get("selected", {})
    outfit_items = []
    
    for category, item_title in selected.items():
        if category == "accessory" and not item_title:
            continue
        
        matching_items = [i for i in filtered_items if i.title == item_title]
        if matching_items:
            selected_item = matching_items[0]
            outfit_items.append({
                "type": category.capitalize(),
                "image": selected_item.image,
                "name": selected_item.title,
                "brand": selected_item.brand or "Unknown"
            })
        else:
            if category in grouped_items and grouped_items[category]:
                fallback = random.choice(grouped_items[category])
                outfit_items.append({
                    "type": category.capitalize(),
                    "image": fallback.image,
                    "name": fallback.title,
                    "brand": fallback.brand or "Unknown"
                })
    
    outfit_id = str(uuid.uuid4())
    db_outfit = models.Outfit(
        id=outfit_id,
        user_id=DEFAULT_USER_ID,
        title=intent.get("vibe", request.prompt[:30]),
        vibe=intent.get("style", "Stylish"),
        generated_at=datetime.utcnow(),
        is_saved=False
    )
    db.add(db_outfit)
    db.flush()
    
    for item_data in outfit_items:
        db_item = models.OutfitItem(
            outfit_id=outfit_id,
            type=item_data["type"],
            image=item_data["image"],
            name=item_data["name"],
            brand=item_data["brand"]
        )
        db.add(db_item)
    
    db.commit()
    db.refresh(db_outfit)
    
    response = schemas.OutfitResponse(
        id=db_outfit.id,
        title=db_outfit.title,
        vibe=db_outfit.vibe,
        generated_at=db_outfit.generated_at,
        is_saved=db_outfit.is_saved,
        items=[schemas.OutfitItemResponse(**item_data) for item_data in outfit_items],
        reasoning=gpt_result.get("reasoning"),
        style_tips=gpt_result.get("style_tips"),
        color_harmony=gpt_result.get("color_harmony")
    )
    
    return response

@router.get("", response_model=List[schemas.OutfitResponse])
async def get_saved_outfits(db: Session = Depends(get_db)):
    outfits = db.query(models.Outfit).filter(
        models.Outfit.user_id == DEFAULT_USER_ID,
        models.Outfit.is_saved == True
    ).order_by(models.Outfit.generated_at.desc()).all()
    
    return outfits

@router.get("/history", response_model=List[schemas.OutfitResponse])
async def get_outfit_history(db: Session = Depends(get_db)):
    outfits = db.query(models.Outfit).filter(
        models.Outfit.user_id == DEFAULT_USER_ID
    ).order_by(models.Outfit.generated_at.desc()).all()
    
    return outfits

@router.get("/current", response_model=schemas.OutfitResponse)
async def get_current_outfit(db: Session = Depends(get_db)):
    outfit = db.query(models.Outfit).filter(
        models.Outfit.user_id == DEFAULT_USER_ID
    ).order_by(models.Outfit.generated_at.desc()).first()
    
    if not outfit:
        raise HTTPException(status_code=404, detail="No outfits generated yet")
    
    return outfit

@router.post("/{outfit_id}/save", response_model=schemas.OutfitResponse)
async def save_outfit(
    outfit_id: str,
    db: Session = Depends(get_db)
):
    outfit = db.query(models.Outfit).filter(
        models.Outfit.id == outfit_id,
        models.Outfit.user_id == DEFAULT_USER_ID
    ).first()
    
    if not outfit:
        raise HTTPException(status_code=404, detail="Outfit not found")
    
    outfit.is_saved = True
    db.commit()
    db.refresh(outfit)
    
    return outfit

