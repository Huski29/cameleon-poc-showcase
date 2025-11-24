from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import asyncio
from datetime import datetime
from app.database import get_db
from app import models, schemas
import uuid

router = APIRouter()

DEFAULT_USER_ID = "user-1"

MOCK_OUTFITS = [
    {
        "title": "Coastal Cruise",
        "vibe": "Relaxed Fit",
        "items": [
            {
                "type": "Top",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuBgU4xfgJrU2aXBE9XPeov-MAAZ3WdMRZysP_oTiRyyO42wx-WC1lBL_Mvu1O0OJAghFI3GtZLWU0wJLMhr1Z2Q8aYUB0khNjGcA-8um9w1yblwzhasvP3D3gtqR0XYpDdvMu89Oa8XAqUp8pRNNjpXFASaQJvh6qKP7Dul51eGlvmpACED95PfpVw7owhUmKMfexZp4g1UwRyBQ15b-c87Et2CePjNq28QlFJoH6fudP_BRb4bjcWuCDx2AgGnsl_dW_KzV5W6XpM",
                "name": "Cashmere Sweater",
                "brand": "Zegna"
            },
            {
                "type": "Layer",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuCXw-4MkdXXsU8vuj2jQBxArSY6fccVsqlJi3Enr7Rdc7hf_UtlOWXXEDujj8agLiBm2v-YcG2B5gJXkQP87kKpxw6sxZVW60Rw2Wb_As1uotQx4qfa_kAwQpoAgHIp961mXsSUXX2rNCDBrjiQ_Y9e27ndMZq36jU40xrvZz1SsnumcG_UGIYrMxokYJ_DQUPeUJ-t-gEjDL5RrIic4axbf07QL5JgstYsm25GnRos7IxmLp1BhHDyJMbXpuBDGXsc_mCGpnTb0es",
                "name": "Trench Coat",
                "brand": "Burberry"
            },
            {
                "type": "Bottom",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAmWyESzGnsflEfIb5Udk0zhK7zCrRoTbDBiZPofeGqcRAhzQmpjKV9puczWjuNIsMH2KYdP5P5Z_EyimtX3Z6JCKAzNFyqp5TyAwUsxLElMXJDkGYrqtTEXK7azDrCdtBCHmS4JJUN1Mf2OpFi6--e9yyTUwDwljWcTFpi10tpZ3hSj0mhurqRpcUXsSVgIwqYd64aERMRNGWaUgoASkYtwsk5LQ4h-hgKa4apqhKXnAMsbc4ADmTu4Rj5ozKCrXFg_Ge-47MmrD0",
                "name": "Linen Trousers",
                "brand": "Prada"
            },
            {
                "type": "Shoe",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuCUJy2OsFwfJEsnCaumEVKWRdt_x2fZqfVMOvCy7nfBXu-SVAR4W7aQkDRqkIDvlq7yqzrTVxPn8LByd5Osi8-5ciH7wbjfUEDU9pR7OFObZS8HKQPgIhWlavJk7TgnMQ8xgS1SIIQbfOKxycctpIkCEDv-fOHTCdANQSuE5qHxadyQUPBrvspcDY9MidM3t6qXZQiJeMjz4eKbQZgFwAeSpztSp22wT-Jgh0u_SI7f0hYETf7AZQDyMjZ1OL4v5l1QMdlQNr3ZRV4",
                "name": "Leather Loafers",
                "brand": "Gucci"
            }
        ]
    },
    {
        "title": "Smart Casual Weekend",
        "vibe": "Relaxed yet put-together",
        "items": [
            {
                "type": "Top",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuDbri_km-ADGYg6rWqwctuYCw24n3O8E03OufwQ6sqYzkUwMydHjCiwsWEFiPmqLqWpvn0r6DiqVbd3d6IyPS67sIJMauQIVAe56LmDJTEOsVJ50sK7org0Lrs1tQF8xMt2oNVzL7XQPdW-tc2NyZnxd7pOr_eLOFT71OebCZGKabF2w_Ez-HnVfi-D7Ppdsp2Y4khQCocEtk2aZclidV0dJ1zU7SG1Ykg18I_7nXgQdqiag_pC8FObLfkCPPsqdxxWYs_AJVt3rKo",
                "name": "Cashmere Sweater",
                "brand": "Everlane"
            },
            {
                "type": "Bottom",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuCDBJQRrjpCChvtByKQu_VT88ooY90B8JdixF1YfNrrSvaDbTIjqd3oNLM9Mj1S5VwaVO0jEMuj80vk8xnSInQVoC70_-bH4PPKU-itM-2tCNU_9gD-tvUkjQ4pysxhgXFcZqLlKobO29gbsUB-ng4lHy2AByML4HHzmBjKDXlglka76WWsdwcLf80b_mviU4_KLPnPO9Xw8aVmAJIylmV8-505pVxd8xSo-FFEVCgtCq_mJMS349s1G9N6AmunnppyYGbbnkiEKxI",
                "name": "High-Waisted Jeans",
                "brand": "Levi's"
            }
        ]
    }
]

@router.post("/generate", response_model=schemas.OutfitResponse)
async def generate_outfit(
    request: schemas.OutfitGenerateRequest,
    db: Session = Depends(get_db)
):
    await asyncio.sleep(1.5)
    
    outfit_count = db.query(models.Outfit).filter(models.Outfit.user_id == DEFAULT_USER_ID).count()
    mock_data = MOCK_OUTFITS[outfit_count % len(MOCK_OUTFITS)]
    outfit_id = str(uuid.uuid4())
    db_outfit = models.Outfit(
        id=outfit_id,
        user_id=DEFAULT_USER_ID,
        title=mock_data["title"],
        vibe=mock_data["vibe"],
        generated_at=datetime.utcnow(),
        is_saved=False
    )
    db.add(db_outfit)
    db.flush()
    
    for item_data in mock_data["items"]:
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
    
    return db_outfit

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

