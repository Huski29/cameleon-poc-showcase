from app.database import SessionLocal, engine, Base
from app import models
from app.data.fashion_data import FASHION_ITEMS

Base.metadata.create_all(bind=engine)

def seed_database():
    db = SessionLocal()
    
    try:
        existing_user = db.query(models.User).filter(models.User.id == "user-1").first()
        if existing_user:
            print("Database already seeded. Deleting old data...")
            db.query(models.WardrobeItem).filter(models.WardrobeItem.user_id == "user-1").delete()
            db.query(models.Outfit).filter(models.Outfit.user_id == "user-1").delete()
            db.query(models.Notification).filter(models.Notification.user_id == "user-1").delete()
            db.delete(existing_user)
            db.commit()
        
        user = models.User(
            id="user-1",
            name="Sarah Johnson",
            email="sarah.j@email.com",
            profile_picture="https://lh3.googleusercontent.com/aida-public/AB6AXuCgyx43deMJXdxwSV6CSDmpDiAqkKPoxbKEJahnnRBIcoMDjZ_DxDeUguHlJng7r2a3wGrxReHgAKaPLnUsF7Hb41DduomvjzSZf91ThUQFkoMvUPc8FBHVYYsclK3JgGsK6ded4p1ll6t5bkpNOWpqDSXNd5r5_TZKBrwIbvXIa0Nx1kq3z3GA_btD7douPDKd0k-HFTK04r-IC0R3H5ziQWXnZjutKvCRces8EaamLKXL9zeh-evPTSJXvof90f5jSmYyEeVzv0U",
            gender="female",
            height="Regular",
            volume="Mid",
            body_type="Rectangle",
            style_preference="Smart Casual",
            color_palette="Neutral & Earth Tones",
            budget="Mid-Range"
        )
        db.add(user)
        db.flush()
        
        print(f"Created user: {user.name} (gender: {user.gender})")
        
        print(f"\nInserting {len(FASHION_ITEMS)} fashion items...")
        for idx, item_data in enumerate(FASHION_ITEMS, 1):
            item = models.WardrobeItem(
                user_id="user-1",
                **item_data
            )
            db.add(item)
            
            if idx % 50 == 0:
                print(f"  Inserted {idx} items...")
        
        print(f"Created {len(FASHION_ITEMS)} wardrobe items")
        
        notifications = [
            {"text": "New outfit suggestion available", "time": "5m ago", "unread": True},
            {"text": "Your wardrobe has been updated", "time": "1h ago", "unread": True},
            {"text": "Style Guide: Summer trends are here", "time": "3h ago", "unread": False},
            {"text": "New items added to your favorites", "time": "5h ago", "unread": False},
            {"text": "Coastal Cruise outfit is ready", "time": "1d ago", "unread": False},
            {"text": "Weekly style tips are available", "time": "2d ago", "unread": False},
            {"text": "Your avatar has been generated", "time": "3d ago", "unread": False},
            {"text": "New wardrobe items suggested", "time": "4d ago", "unread": False}
        ]
        
        for notif_data in notifications:
            notif = models.Notification(
                user_id="user-1",
                **notif_data
            )
            db.add(notif)
        
        print(f"Created {len(notifications)} notifications")
        
        db.commit()
        print("\nDatabase seeded successfully!")
        print(f"Total items: {len(FASHION_ITEMS)}")
        
        female_items = len([i for i in FASHION_ITEMS if i['gender'] == 'female'])
        male_items = len([i for i in FASHION_ITEMS if i['gender'] == 'male'])
        print(f"  Female items: {female_items}")
        print(f"  Male items: {male_items}")
        
    except Exception as e:
        print(f"\nError seeding database: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Seeding database with 500 fashion items...\n")
    seed_database()


