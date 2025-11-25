from app.database import SessionLocal, engine, Base
from app import models
from app.services.fashionclip_service import fashionclip_service
import json

def batch_generate_embeddings():
    db = SessionLocal()
    
    try:
        items = db.query(models.WardrobeItem).filter(
            models.WardrobeItem.image_embedding == None
        ).all()
        
        print(f"Processing {len(items)} items...\n")
        
        successful = 0
        failed = 0
        
        for idx, item in enumerate(items, 1):
            print(f"[{idx}/{len(items)}] Processing: {item.title}")
            
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
                item.image_embedding = image_emb
                item.text_embedding = text_emb
                db.commit()
                successful += 1
                print(f"  ✓ Embeddings generated")
            else:
                failed += 1
                print(f"  ✗ Failed to generate embeddings")
        
        print(f"\nBatch embedding complete!")
        print(f"  Successful: {successful}")
        print(f"  Failed: {failed}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Batch generating FashionCLIP embeddings...\n")
    batch_generate_embeddings()

