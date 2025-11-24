from app.database import SessionLocal, engine, Base
from app import models

Base.metadata.create_all(bind=engine)

def seed_database():
    db = SessionLocal()
    
    try:
        existing_user = db.query(models.User).filter(models.User.id == "user-1").first()
        if existing_user:
            print("Database already seeded.")
            return
        
        # Create default user (Sarah Johnson)
        user = models.User(
            id="user-1",
            name="Sarah Johnson",
            email="sarah.j@email.com",
            profile_picture="https://lh3.googleusercontent.com/aida-public/AB6AXuCgyx43deMJXdxwSV6CSDmpDiAqkKPoxbKEJahnnRBIcoMDjZ_DxDeUguHlJng7r2a3wGrxReHgAKaPLnUsF7Hb41DduomvjzSZf91ThUQFkoMvUPc8FBHVYYsclK3JgGsK6ded4p1ll6t5bkpNOWpqDSXNd5r5_TZKBrwIbvXIa0Nx1kq3z3GA_btD7douPDKd0k-HFTK04r-IC0R3H5ziQWXnZjutKvCRces8EaamLKXL9zeh-evPTSJXvof90f5jSmYyEeVzv0U",
            height="Regular",
            volume="Mid",
            body_type="Rectangle",
            style_preference="Smart Casual",
            color_palette="Neutral & Earth Tones",
            budget="Mid-Range"
        )
        db.add(user)
        db.flush()
        
        print("Created user: Sarah Johnson")
        
        # Create wardrobe items
        wardrobe_items = [
            # Tops
            {
                "category": "tops",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuDbri_km-ADGYg6rWqwctuYCw24n3O8E03OufwQ6sqYzkUwMydHjCiwsWEFiPmqLqWpvn0r6DiqVbd3d6IyPS67sIJMauQIVAe56LmDJTEOsVJ50sK7org0Lrs1tQF8xMt2oNVzL7XQPdW-tc2NyZnxd7pOr_eLOFT71OebCZGKabF2w_Ez-HnVfi-D7Ppdsp2Y4khQCocEtk2aZclidV0dJ1zU7SG1Ykg18I_7nXgQdqiag_pC8FObLfkCPPsqdxxWYs_AJVt3rKo",
                "alt": "Cream cashmere crewneck sweater",
                "title": "Everlane Cashmere",
                "description": "Cream sweater, size M"
            },
            {
                "category": "tops",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuC1ngT1vBIsqU2HMo910q7DdqUb2wcyyeRSLsHErVzF-szAW8ghJNoINDjkplhGeQc2v_fh9Mkz2lqUWtmZ_F0CzvaROqryJLBXi8GHSw8vn5oSTQROzS2RE3hxL9msf3LVOfhaiJ8bHbwbuwt2yBZqEAtasu7tLgWbf6rX1aZvgX9cpD-NgjgnSDvOiGHcdIgXO8YjDRbM5VYFvJ8kXB1XulYIQ1JjnuG3a0KJbD_t8gezPC4EpPnJGmBV4VBNozisCRVfqMv9B8c",
                "alt": "Blush pink silk camisole",
                "title": "Silk Camisole",
                "description": "Blush pink, size S"
            },
            {
                "category": "tops",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuA06C65_8XwfMF1HxRbk5WKB3nONXtGSkn07V_FXDJTsH6pRaUXsnqF2R_T8UqygdEYJEaweC1MW3p6kidMMSWdGPe0hEZ8gT7SI7CT6Ou1MXru6WeUVnH-HaDdnNnJhC8nm__9PIZz7S59LHeGaXrX0OiFHl8ymBx6KGR4t7pWQJs3-0QbNqexRIICDhUVrzdcTL5IbscE0TjhRRAkjxT6nvxUo4eqJ1pKQoSXMm0ZJrGpDWlBOuT2KY_N2PZUADKgrwnfrsNFnc0",
                "alt": "Classic white t-shirt",
                "title": "Classic White Tee",
                "description": "Cotton blend, size S"
            },
            {
                "category": "tops",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAmCBX0tVTlP74XG-t59FttALHCiI43nxZKYGNEvQ3M0A2NbcFiaDhkIR03l4AIIurNKUP0-ROUQqdpBDQTuCUe6X7fAj-HTxAqaZcTj3pHXQRANYWChV6xbPcZiXpvKXXs7IUoHM8SvWPEHMWuDsw5cnm8jDWjREsCPe1MhcNpistlnMDzgR6pPixLG6VcjiGsTMKGurjr7srX43zuRRTVVZLELvDPMsZI9KJkLX-ho7pXg-yk9tn4vrAvupjr9sbe_IUb4Rac7LU",
                "alt": "Beige linen button-down shirt",
                "title": "Linen Button-Down",
                "description": "Beige, size M"
            },
            # Bottoms
            {
                "category": "bottoms",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuCDBJQRrjpCChvtByKQu_VT88ooY90B8JdixF1YfNrrSvaDbTIjqd3oNLM9Mj1S5VwaVO0jEMuj80vk8xnSInQVoC70_-bH4PPKU-itM-2tCNU_9gD-tvUkjQ4pysxhgXFcZqLlKobO29gbsUB-ng4lHy2AByML4HHzmBjKDXlglka76WWsdwcLf80b_mviU4_KLPnPO9Xw8aVmAJIylmV8-505pVxd8xSo-FFEVCgtCq_mJMS349s1G9N6AmunnppyYGbbnkiEKxI",
                "alt": "High-waisted denim jeans",
                "title": "Levi's Wedgie Fit",
                "description": "Light wash denim, size 27"
            },
            {
                "category": "bottoms",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuB3fMf0d9Fgl7mgKE1ytNfFG6NaoIhHGJOBKhFViV52dDBPW6iK0VAfeMCl37p-kq4oLerQx0oLRBXVDYRYk3295Tgl2wlF_Fadg2xaS9Jj4x99M3nOkMmZcOIAJNmwdxmj9c4Ahb8GJPPxAnGNkgtZSird89dogzXqaryUOsiAgvZ9sZolnSPAwXcm6g2a4YzFDPBYu7axPcrwBu4suSqr70PshaKmYgl9zQXr2GPPpqTIQMJSp76j6lQkpK5rqPec_3Hva78Hlbs",
                "alt": "Black wide-leg trousers",
                "title": "Aritzia Effortless",
                "description": "Black trousers, size 4"
            },
            {
                "category": "bottoms",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAzT9WI6ttloO2rbFOtb25x2qyYk1KXZv0ZyJsQcuD0nV5GX7DofbE4uvIJVFGi_zVF3Q1z4vRiV9LblXDhaPC_uTAK6SV0Gkp3eLxnWlNVL4i-4hy8J6tBN9IU-jtrGNCm3fgRAro3LNn0pvlNddGOpDctLddafo9Cf6zOx2U_bxJatZrkZ3RX2ajKX5NseC17Chkwutav_43eLPIzp1DDMGDq3v1xmrFh01JSigbs2lplBMWKNcAERgfCKjYC3uRALlfItTz5nQI",
                "alt": "A-line midi skirt in a floral pattern",
                "title": "Réalisation Par Skirt",
                "description": "Floral midi skirt, size S"
            }
        ]
        
        for item_data in wardrobe_items:
            item = models.WardrobeItem(
                user_id="user-1",
                **item_data
            )
            db.add(item)
        
        print(f"Created {len(wardrobe_items)} wardrobe items")
        
        # Create notifications
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
        
    except Exception as e:
        print(f"\nError seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Seeding database with mock data...\n")
    seed_database()

