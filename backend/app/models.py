from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    profile_picture = Column(String, nullable=True)
    
    # Style Avatar
    height = Column(String, nullable=False)  # Petite, Regular, Tall
    volume = Column(String, nullable=False)  # Lean, Mid, Plus
    body_type = Column(String, nullable=False)  # Triangle, Rectangle, etc.
    
    # Style Preferences
    style_preference = Column(String, nullable=False)
    color_palette = Column(String, nullable=False)
    budget = Column(String, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    wardrobe_items = relationship("WardrobeItem", back_populates="user", cascade="all, delete-orphan")
    outfits = relationship("Outfit", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")


class WardrobeItem(Base):
    __tablename__ = "wardrobe_items"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    category = Column(String, nullable=False)  # tops, bottoms, shoes, accessories
    image = Column(String, nullable=False)
    alt = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="wardrobe_items")


class Outfit(Base):
    __tablename__ = "outfits"
    
    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    vibe = Column(String, nullable=False)
    generated_at = Column(DateTime, default=datetime.utcnow)
    is_saved = Column(Boolean, default=False)
    
    # Relationships
    user = relationship("User", back_populates="outfits")
    items = relationship("OutfitItem", back_populates="outfit", cascade="all, delete-orphan")


class OutfitItem(Base):
    __tablename__ = "outfit_items"
    
    id = Column(Integer, primary_key=True, index=True)
    outfit_id = Column(String, ForeignKey("outfits.id"), nullable=False)
    type = Column(String, nullable=False)  # Top, Bottom, Shoe, etc.
    image = Column(String, nullable=False)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    
    # Relationships
    outfit = relationship("Outfit", back_populates="items")


class Notification(Base):
    __tablename__ = "notifications"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    text = Column(String, nullable=False)
    time = Column(String, nullable=False)
    unread = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="notifications")

