from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from typing import List

router = APIRouter()

DEFAULT_USER_ID = "user-1"

@router.get("/", response_model=List[schemas.NotificationResponse])
async def get_notifications(db: Session = Depends(get_db)):
    notifications = db.query(models.Notification).filter(
        models.Notification.user_id == DEFAULT_USER_ID
    ).order_by(models.Notification.created_at.desc()).all()
    return notifications

@router.put("/{notification_id}/read", response_model=schemas.NotificationResponse)
async def mark_notification_read(
    notification_id: str,
    db: Session = Depends(get_db)
):
    notification = db.query(models.Notification).filter(
        models.Notification.id == notification_id,
        models.Notification.user_id == DEFAULT_USER_ID
    ).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    notification.is_read = True
    db.commit()
    db.refresh(notification)
    return notification
