from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from app.database import get_db
from app import models, schemas
from app.services.recommendation_service import recommendation_service
from app.services.gpt_service import gpt_service
from app.services.weather_service import weather_service
from app.services.gemini_tryon_service import gemini_tryon_service
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
    
    # Pass user's style preference to intent parser for personalized interpretation
    intent = gpt_service.parse_intent(request.prompt, style_preference=user.style_preference)
    
    weather_data = weather_service.get_current_weather("New York")
    temp_category = weather_service.get_temperature_category(weather_data["temperature"])
    
    # Search for items in each category separately to ensure we get items from all categories
    all_items = []
    for category in ["tops", "bottoms", "shoes", "accessories"]:
        category_items = recommendation_service.search_similar_items(
            db=db,
            query_text=request.prompt,
            user_id=DEFAULT_USER_ID,
            gender=user.gender,
            category=category,
            top_k=15  # Get 15 items per category
        )
        all_items.extend(category_items)
    
    filtered_items = recommendation_service.filter_by_context(
        items=all_items,
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
            # Fallback: if GPT's selection doesn't match exactly, pick a random item from that category
            if category in grouped_items and grouped_items[category]:
                fallback = random.choice(grouped_items[category])
                outfit_items.append({
                    "type": category.capitalize(),
                    "image": fallback.image,
                    "name": fallback.title,
                    "brand": fallback.brand or "Unknown"
                })
    
    outfit_id = str(uuid.uuid4())
    
    # Ensure title is never None - use a fallback
    outfit_title = intent.get("vibe") or intent.get("style") or request.prompt[:50] or "My Outfit"
    outfit_vibe = intent.get("style") or intent.get("vibe") or "Stylish"
    
    db_outfit = models.Outfit(
        id=outfit_id,
        user_id=DEFAULT_USER_ID,
        title=outfit_title,
        vibe=outfit_vibe,
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
    
    # Refresh outfit to get items with their IDs
    outfit_with_items = db.query(models.Outfit).filter(
        models.Outfit.id == outfit_id
    ).first()
    
    response = schemas.OutfitResponse(
        id=outfit_with_items.id,
        title=outfit_with_items.title,
        vibe=outfit_with_items.vibe,
        generated_at=outfit_with_items.generated_at,
        is_saved=outfit_with_items.is_saved,
        items=[schemas.OutfitItemResponse(
            id=item.id,
            type=item.type,
            image=item.image,
            name=item.name,
            brand=item.brand
        ) for item in outfit_with_items.items],
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

@router.post("/{outfit_id}/tryon", response_model=schemas.TryOnResponse)
async def generate_tryon(
    outfit_id: str,
    db: Session = Depends(get_db)
):
    """
    Generate a virtual try-on image showing the user's avatar wearing the outfit.
    """
    # Get the outfit with all items
    outfit = db.query(models.Outfit).filter(
        models.Outfit.id == outfit_id,
        models.Outfit.user_id == DEFAULT_USER_ID
    ).first()
    
    if not outfit:
        raise HTTPException(status_code=404, detail="Outfit not found")
    
    # Get user profile with avatar
    user = db.query(models.User).filter(models.User.id == DEFAULT_USER_ID).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not user.profile_picture:
        raise HTTPException(status_code=400, detail="User avatar not found. Please create your avatar first.")
    
    # Prepare outfit items for try-on
    outfit_items = []
    for item in outfit.items:
        # Get the full wardrobe item to access the image
        wardrobe_item = db.query(models.WardrobeItem).filter(
            models.WardrobeItem.title == item.name
        ).first()
        
        outfit_items.append({
            "type": item.type,
            "name": item.name,
            "brand": item.brand,
            "image": item.image if item.image else (wardrobe_item.image if wardrobe_item else "")
        })
    
    # Prepare user body info
    user_body_info = {
        "gender": user.gender,
        "height": user.height,
        "volume": user.volume,
        "body_type": user.body_type
    }
    
    # Get user's original uploaded image if available (stored when creating avatar)
    # Check if user has an uploaded_image attribute, otherwise use None
    user_uploaded_image = getattr(user, 'uploaded_image', None)
    
    # Generate try-on image with both avatar and original photo for better consistency
    tryon_image = gemini_tryon_service.generate_tryon(
        avatar_image=user.profile_picture,
        outfit_items=outfit_items,
        user_body_info=user_body_info,
        user_uploaded_image=user_uploaded_image
    )
    
    if not tryon_image:
        raise HTTPException(status_code=500, detail="Failed to generate try-on image. Please try again.")
    
    return schemas.TryOnResponse(
        outfit_id=outfit_id,
        tryon_image=tryon_image,
        message="Virtual try-on generated successfully!"
    )

