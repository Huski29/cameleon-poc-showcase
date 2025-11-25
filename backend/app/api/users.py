from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter()

DEFAULT_USER_ID = "user-1"

@router.get("/profile", response_model=schemas.UserResponse)
async def get_user_profile(db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == DEFAULT_USER_ID).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/profile", response_model=schemas.UserResponse)
async def update_user_profile(
    user_update: schemas.UserUpdate,
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == DEFAULT_USER_ID).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user_update.name is not None:
        user.name = user_update.name
    if user_update.email is not None:
        user.email = user_update.email
    if user_update.profile_picture is not None:
        user.profile_picture = user_update.profile_picture
    if user_update.gender is not None:
        user.gender = user_update.gender
    
    db.commit()
    db.refresh(user)
    return user

@router.put("/avatar", response_model=schemas.UserResponse)
async def update_user_avatar(
    avatar_update: schemas.AvatarUpdate,
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == DEFAULT_USER_ID).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if avatar_update.height is not None:
        user.height = avatar_update.height
    if avatar_update.volume is not None:
        user.volume = avatar_update.volume
    if avatar_update.body_type is not None:
        user.body_type = avatar_update.body_type
    
    db.commit()
    db.refresh(user)
    return user

@router.put("/preferences", response_model=schemas.UserResponse)
async def update_user_preferences(
    prefs_update: schemas.PreferencesUpdate,
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == DEFAULT_USER_ID).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if prefs_update.style_preference is not None:
        user.style_preference = prefs_update.style_preference
    if prefs_update.color_palette is not None:
        user.color_palette = prefs_update.color_palette
    if prefs_update.budget is not None:
        user.budget = prefs_update.budget
    
    db.commit()
    db.refresh(user)
    return user

