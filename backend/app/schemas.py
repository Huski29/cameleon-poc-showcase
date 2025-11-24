from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# Style Avatar Schemas
class StyleAvatar(BaseModel):
    height: str
    volume: str
    body_type: str

# Style Preferences Schemas
class StylePreferences(BaseModel):
    style_preference: str
    color_palette: str
    budget: str

# User Schemas
class UserBase(BaseModel):
    name: str
    email: EmailStr
    profile_picture: Optional[str] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    profile_picture: Optional[str] = None

class AvatarUpdate(BaseModel):
    height: Optional[str] = None
    volume: Optional[str] = None
    body_type: Optional[str] = None

class PreferencesUpdate(BaseModel):
    style_preference: Optional[str] = None
    color_palette: Optional[str] = None
    budget: Optional[str] = None

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    profile_picture: Optional[str]
    height: str
    volume: str
    body_type: str
    style_preference: str
    color_palette: str
    budget: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Wardrobe Schemas
class WardrobeItemBase(BaseModel):
    category: str
    image: str
    alt: str
    title: str
    description: str

class WardrobeItemCreate(WardrobeItemBase):
    pass

class WardrobeItemResponse(WardrobeItemBase):
    id: int
    user_id: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Outfit Item Schemas
class OutfitItemBase(BaseModel):
    type: str
    image: str
    name: str
    brand: str

class OutfitItemResponse(OutfitItemBase):
    id: int
    
    class Config:
        from_attributes = True

# Outfit Schemas
class OutfitGenerateRequest(BaseModel):
    prompt: str
    category: Optional[str] = None

class OutfitResponse(BaseModel):
    id: str
    title: str
    vibe: str
    generated_at: datetime
    is_saved: bool
    items: List[OutfitItemResponse]
    
    class Config:
        from_attributes = True

# Notification Schemas
class NotificationBase(BaseModel):
    text: str
    time: str

class NotificationResponse(NotificationBase):
    id: int
    unread: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class NotificationUpdate(BaseModel):
    unread: bool

