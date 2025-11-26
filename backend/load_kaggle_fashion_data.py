"""
Load Fashion Product Images Dataset from Kaggle into the database.
This script:
1. Reads the styles.csv metadata file
2. Maps Kaggle categories to our wardrobe categories
3. Loads a balanced selection of items into the database
4. Converts images to base64
5. Generates FashionCLIP embeddings
"""

import os
import csv
import base64
from PIL import Image
from io import BytesIO
import random
from app.database import SessionLocal
from app import models
from app.services.fashionclip_service import FashionCLIPService
from sqlalchemy import func

# Ensure DATABASE_URL is set
os.environ['DATABASE_URL'] = os.getenv('DATABASE_URL', 'postgresql://cameleon_user:cameleon_password_2024@localhost:5432/cameleon_db')

# Category mapping from Kaggle to our categories
CATEGORY_MAPPING = {
    # TOPS
    'tops': [
        'Shirts', 'Tshirts', 'Tops', 'Tunics', 'Kurtas', 'Kurtis', 
        'Sweaters', 'Sweatshirts', 'Jackets', 'Blazers', 'Waistcoat',
        'Shrug', 'Nehru Jackets', 'Camisoles', 'Tank Tops', 'Blouses'
    ],
    # BOTTOMS
    'bottoms': [
        'Jeans', 'Trousers', 'Track Pants', 'Shorts', 'Skirts', 
        'Capris', 'Leggings', 'Tights', 'Stockings', 'Churidar',
        'Salwar', 'Jeggings', 'Patiala'
    ],
    # SHOES
    'shoes': [
        'Casual Shoes', 'Sports Shoes', 'Formal Shoes', 'Sandals',
        'Flip Flops', 'Flats', 'Heels', 'Wedges', 'Shoe Accessories',
        'Boots', 'Sneakers'
    ],
    # ACCESSORIES
    'accessories': [
        'Watches', 'Bags', 'Belts', 'Sunglasses', 'Wallets', 'Ties',
        'Scarves', 'Caps', 'Hat', 'Gloves', 'Mufflers', 'Stoles',
        'Socks', 'Jewellery', 'Backpacks', 'Handbags', 'Clutches',
        'Messenger Bags', 'Laptop Bag', 'Travel Bag', 'Trolley Bag',
        'Duffel Bags', 'Rucksacks', 'Mobile Pouch'
    ]
}

def get_our_category(article_type: str) -> str:
    """Map Kaggle articleType to our category."""
    for category, article_types in CATEGORY_MAPPING.items():
        if article_type in article_types:
            return category
    return None  # Skip items that don't fit our categories

def convert_image_to_base64(image_path: str, max_size=(800, 800), quality=85) -> str:
    """Convert an image file to base64 string."""
    try:
        img = Image.open(image_path)
        
        # Convert to RGB if needed
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Resize to save space
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Convert to base64
        buffered = BytesIO()
        img.save(buffered, format="JPEG", quality=quality)
        return f"data:image/jpeg;base64,{base64.b64encode(buffered.getvalue()).decode()}"
    except Exception as e:
        print(f"  ❌ Error converting image {image_path}: {e}")
        return None

def load_fashion_data(items_per_category=100):
    """
    Load fashion data from Kaggle dataset.
    
    Args:
        items_per_category: Number of items to load per category (tops, bottoms, shoes, accessories)
    """
    db = SessionLocal()
    fashionclip = FashionCLIPService()
    
    try:
        # Get the default user (assuming user_id=1 exists)
        user = db.query(models.User).first()
        if not user:
            print("❌ No user found in database. Please create a user first.")
            return
        
        print("================================================================================")
        print("  LOADING KAGGLE FASHION DATASET")
        print("================================================================================")
        print(f"Target: {items_per_category} items per category")
        print(f"User ID: {user.id}")
        print("================================================================================\n")
        
        # Clear existing wardrobe items
        print("🗑️  Clearing existing wardrobe items...")
        db.query(models.OutfitItem).delete()
        db.query(models.Outfit).delete()
        db.query(models.WardrobeItem).delete()
        db.commit()
        print("✅ Cleared existing items.\n")
        
        # Read CSV and categorize items
        csv_path = '/home/xsolai/hdd/Projects/cameleon-poc-showcase/backend/styles.csv'
        images_dir = '/home/xsolai/hdd/Projects/cameleon-poc-showcase/backend/images'
        
        categorized_items = {
            'tops': [],
            'bottoms': [],
            'shoes': [],
            'accessories': []
        }
        
        print("📖 Reading CSV and categorizing items...")
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                article_type = row.get('articleType', '')
                our_category = get_our_category(article_type)
                
                if our_category:
                    # Check if image exists
                    image_path = os.path.join(images_dir, f"{row['id']}.jpg")
                    if os.path.exists(image_path):
                        categorized_items[our_category].append({
                            'id': row['id'],
                            'gender': row.get('gender', 'Unisex'),
                            'masterCategory': row.get('masterCategory', ''),
                            'subCategory': row.get('subCategory', ''),
                            'articleType': article_type,
                            'baseColour': row.get('baseColour', ''),
                            'season': row.get('season', ''),
                            'year': row.get('year', ''),
                            'usage': row.get('usage', ''),
                            'productDisplayName': row.get('productDisplayName', ''),
                            'image_path': image_path
                        })
        
        print(f"\n📊 Categorized items:")
        for cat, items in categorized_items.items():
            print(f"  {cat.capitalize()}: {len(items)} items available")
        
        # Sample items from each category
        print(f"\n🎲 Sampling {items_per_category} items from each category...")
        selected_items = {}
        for cat, items in categorized_items.items():
            if len(items) >= items_per_category:
                selected_items[cat] = random.sample(items, items_per_category)
            else:
                selected_items[cat] = items
                print(f"  ⚠️  Only {len(items)} items available for {cat}")
        
        # Load items into database
        print(f"\n💾 Loading items into database...")
        total_loaded = 0
        total_skipped = 0
        
        for category, items in selected_items.items():
            print(f"\n📁 Processing {category}...")
            loaded = 0
            skipped = 0
            
            for idx, item in enumerate(items):
                print(f"  [{idx+1}/{len(items)}] {item['productDisplayName'][:50]}...")
                
                # Convert image to base64
                base64_image = convert_image_to_base64(item['image_path'])
                if not base64_image:
                    skipped += 1
                    total_skipped += 1
                    continue
                
                # Generate text embedding
                text_for_embedding = f"{item['productDisplayName']} {item['articleType']} {item['baseColour']} {item['usage']}"
                text_embedding = fashionclip.generate_text_embedding(text_for_embedding)
                
                # Generate image embedding
                image_embedding = fashionclip.generate_image_embedding(base64_image)
                
                # Map gender
                gender_map = {
                    'Men': 'male',
                    'Women': 'female',
                    'Boys': 'male',
                    'Girls': 'female',
                    'Unisex': 'unisex'
                }
                gender = gender_map.get(item['gender'], 'unisex')
                
                # Create wardrobe item
                wardrobe_item = models.WardrobeItem(
                    user_id=user.id,
                    category=category,
                    image=base64_image,
                    alt=item['productDisplayName'],
                    title=item['articleType'],
                    description=item['productDisplayName'],
                    brand=item['masterCategory'],
                    color=item['baseColour'],
                    style_tags=f"{item['subCategory']}, {item['usage']}",
                    occasions=item['usage'],
                    season=item['season'],
                    gender=gender,
                    image_embedding=image_embedding,
                    text_embedding=text_embedding
                )
                
                db.add(wardrobe_item)
                loaded += 1
                total_loaded += 1
                
                # Commit in batches
                if (idx + 1) % 20 == 0:
                    db.commit()
                    print(f"    💾 Saved batch ({loaded} loaded, {skipped} skipped so far)")
            
            db.commit()
            print(f"  ✅ {category.capitalize()}: Loaded {loaded} items, Skipped {skipped} items")
        
        # Final verification
        final_count = db.query(func.count(models.WardrobeItem.id)).scalar()
        
        print("\n================================================================================")
        print("  LOADING COMPLETE!")
        print("================================================================================")
        print(f"Total items loaded: {total_loaded}")
        print(f"Total items skipped: {total_skipped}")
        print(f"Database verification: {final_count} items")
        print("================================================================================")
        
        # Show distribution
        print("\n📊 Final distribution:")
        for cat in ['tops', 'bottoms', 'shoes', 'accessories']:
            count = db.query(func.count(models.WardrobeItem.id)).filter(
                models.WardrobeItem.category == cat
            ).scalar()
            print(f"  {cat.capitalize()}: {count} items")
        
        print("\n✅ All items have:")
        print("  - Real images from Kaggle dataset (base64 encoded)")
        print("  - FashionCLIP image embeddings")
        print("  - FashionCLIP text embeddings")
        print("  - Complete metadata (color, season, usage, gender, etc.)")
        
    except Exception as e:
        print(f"\n❌ Error loading fashion data: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    # Load 100 items per category (400 total)
    load_fashion_data(items_per_category=100)

