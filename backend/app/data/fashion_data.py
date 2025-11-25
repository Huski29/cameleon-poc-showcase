import random

def generate_fashion_dataset():
    """Generate 500 fashion items (250 female + 250 male) with real image URLs"""
    
    items = []
    
    # Image base URLs from Unsplash fashion collections
    female_top_images = [
        f"https://images.unsplash.com/photo-{img_id}?w=500&h=600&fit=crop" 
        for img_id in ["1618932260643-eee4a2f652a6", "1594633312681-425c7b97ccd1", "1589992602410-5f8b9c4f9e4e",
                      "1564257577154-8e9e1c2c388b", "1594633313593-bab3825d0caf", "1551028719-00167b16eac5",
                      "1562572159-4efc207f5aff", "1603252109360-909baaf261c7", "1591369822096-ffd140ec948f"]
    ]
    
    female_bottom_images = [
        f"https://images.unsplash.com/photo-{img_id}?w=500&h=600&fit=crop"
        for img_id in ["1541099649105-f69ad21f3246", "1582418702059-97ebafb35d09", "1624378515758-87ce4e2e3a1a",
                      "1560243563-062960ca8838", "1594633312713-5b1f2d08bc2c", "1551488831-00d07cb1f08a"]
    ]
    
    female_shoes_images = [
        f"https://images.unsplash.com/photo-{img_id}?w=500&h=600&fit=crop"
        for img_id in ["1543163521-1bf539c55dd2", "1535043934128-cf0b28d52f95", "1560769629-975ec94e6a86",
                      "1533867349308-68082fc30533", "1494955464529-790512c65305", "1518049362265-d5b2a6467637"]
    ]
    
    female_accessory_images = [
        f"https://images.unsplash.com/photo-{img_id}?w=500&h=600&fit=crop"
        for img_id in ["1590874103328-eac38a683ce7", "1611652022419-a9419f74343f", "1524805444532-a3a4fa2ca0c3",
                      "1509631179647-0177331693ae", "1508685096489-7aacd43bd3b1", "1487222477894-8943e31ef7b2"]
    ]
    
    male_top_images = [
        f"https://images.unsplash.com/photo-{img_id}?w=500&h=600&fit=crop"
        for img_id in ["1620799140188-3b2a02fd9a77", "1489987707025-afc232f7ea0f", "1620799140408-eec2d0a32048",
                      "1602810316693-3667c854239e", "1591047643389-d9ce59fecb72", "1594938390533-28c62695c6dd"]
    ]
    
    male_bottom_images = [
        f"https://images.unsplash.com/photo-{img_id}?w=500&h=600&fit=crop"
        for img_id in ["1624378441941-64db8fb47d12", "1602810316498-ab67cf68c8e1", "1542272604-787c3835535d",
                      "1549490349-8643362247b5", "1565084888279-aca607ecce0f", "1517438476312-10d79c077509"]
    ]
    
    male_shoes_images = [
        f"https://images.unsplash.com/photo-{img_id}?w=500&h=600&fit=crop"
        for img_id in ["1549298916-b41d501d3772", "1606890737304-57a1ca8a5b62", "1582897111598-57e29b8c6d7f",
                      "1603808033192-082d6919d3e1", "1608256246200-53e635b5b65f", "1512374382149-233c42b6a83b"]
    ]
    
    male_accessory_images = [
        f"https://images.unsplash.com/photo-{img_id}?w=500&h=600&fit=crop"
        for img_id in ["1524592094714-97e2562983c3", "1509048191080-d2984bad6ae5", "1585076800246-99f7e7b3f75a",
                      "1591047643389-d9ce59fecb72", "1614164185128-c20b9a5e84f6", "1611312449948-f5b58c1c03c9"]
    ]
    
    # Female Items (250 total: 80 tops, 70 bottoms, 60 shoes, 40 accessories)
    
    # Female Tops (80)
    female_tops_data = [
        # Formal Blouses (20)
        ("Classic Silk Blouse", "Equipment", "White", ["elegant", "formal", "classic"], ["work", "business"], "all"),
        ("Navy Silk Blouse", "Ann Taylor", "Navy", ["sophisticated", "elegant"], ["work", "business"], "all"),
        ("Cream Satin Blouse", "Vince", "Cream", ["luxurious", "elegant"], ["work", "dinner"], "all"),
        ("Blush Pink Blouse", "Kate Spade", "Blush", ["feminine", "elegant"], ["work", "dinner"], "spring"),
        ("Burgundy Silk Blouse", "Reiss", "Burgundy", ["elegant", "rich"], ["work", "dinner"], "fall"),
        ("Ivory Satin Blouse", "Massimo Dutti", "Ivory", ["timeless", "elegant"], ["work", "business"], "all"),
        ("Forest Green Blouse", "& Other Stories", "Forest Green", ["rich", "elegant"], ["work", "dinner"], "fall"),
        ("Lavender Silk Blouse", "COS", "Lavender", ["soft", "feminine"], ["work", "dinner"], "spring"),
        ("Champagne Satin Blouse", "Reiss", "Champagne", ["elegant", "luxurious"], ["work", "formal"], "all"),
        ("Black Silk Shirt", "The Row", "Black", ["sophisticated", "minimalist"], ["work", "formal"], "all"),
        ("White Silk Shirt", "Equipment", "White", ["classic", "elegant"], ["work", "business"], "all"),
        ("Gray Silk Blouse", "Eileen Fisher", "Gray", ["modern", "elegant"], ["work", "dinner"], "all"),
        ("Powder Blue Blouse", "J.Crew", "Powder Blue", ["fresh", "elegant"], ["work", "brunch"], "spring"),
        ("Emerald Green Blouse", "Banana Republic", "Emerald", ["bold", "elegant"], ["work", "dinner"], "fall"),
        ("Coral Silk Blouse", "Ann Taylor", "Coral", ["vibrant", "feminine"], ["work", "brunch"], "summer"),
        ("Charcoal Blouse", "Theory", "Charcoal", ["sophisticated", "modern"], ["work", "business"], "all"),
        ("Dusty Rose Blouse", "Club Monaco", "Dusty Rose", ["romantic", "elegant"], ["work", "dinner"], "all"),
        ("Teal Silk Blouse", "& Other Stories", "Teal", ["rich", "elegant"], ["work", "dinner"], "all"),
        ("Camel Silk Shirt", "Massimo Dutti", "Camel", ["warm", "elegant"], ["work", "brunch"], "fall"),
        ("Slate Blue Blouse", "COS", "Slate Blue", ["modern", "elegant"], ["work", "dinner"], "all"),
        
        # Blazers (20)
        ("Tailored Black Blazer", "Theory", "Black", ["professional", "formal"], ["work", "business"], "all"),
        ("Gray Wool Blazer", "Banana Republic", "Gray", ["classic", "professional"], ["work", "business"], "fall"),
        ("Charcoal Blazer", "Hugo Boss", "Charcoal", ["modern", "professional"], ["work", "business"], "all"),
        ("Camel Wool Blazer", "Max Mara", "Camel", ["timeless", "sophisticated"], ["work", "business"], "fall"),
        ("Navy Wool Blazer", "Theory", "Navy", ["classic", "professional"], ["work", "business"], "all"),
        ("Beige Linen Blazer", "Zara", "Beige", ["lightweight", "sophisticated"], ["work", "brunch"], "summer"),
        ("Burgundy Blazer", "J.Crew", "Burgundy", ["rich", "sophisticated"], ["work", "dinner"], "fall"),
        ("Cream Blazer", "Mango", "Cream", ["soft", "elegant"], ["work", "brunch"], "spring"),
        ("Forest Green Blazer", "& Other Stories", "Forest Green", ["rich", "bold"], ["work", "dinner"], "fall"),
        ("White Linen Blazer", "Theory", "White", ["fresh", "sophisticated"], ["work", "brunch"], "summer"),
        ("Olive Green Blazer", "Banana Republic", "Olive", ["earthy", "sophisticated"], ["work", "casual"], "fall"),
        ("Dusty Pink Blazer", "Mango", "Dusty Pink", ["soft", "feminine"], ["work", "brunch"], "spring"),
        ("Navy Pinstripe Blazer", "Brooks Brothers", "Navy", ["classic", "professional"], ["work", "business"], "all"),
        ("Light Gray Blazer", "COS", "Light Gray", ["modern", "minimalist"], ["work", "business"], "all"),
        ("Tan Blazer", "Massimo Dutti", "Tan", ["warm", "sophisticated"], ["work", "casual"], "fall"),
        ("Deep Purple Blazer", "Ted Baker", "Purple", ["bold", "sophisticated"], ["work", "dinner"], "all"),
        ("Double-Breasted Navy Blazer", "Theory", "Navy", ["classic", "formal"], ["work", "business"], "all"),
        ("Tweed Blazer", "J.Crew", "Brown/Beige", ["textured", "classic"], ["work", "casual"], "fall"),
        ("Black Velvet Blazer", "Karen Millen", "Black", ["luxurious", "formal"], ["dinner", "formal"], "winter"),
        ("Check Pattern Blazer", "Zara", "Gray/White", ["modern", "bold"], ["work", "casual"], "fall"),
        
        # Casual Tops (20)
        ("Classic White Tee", "Everlane", "White", ["essential", "minimalist"], ["casual", "weekend"], "all"),
        ("Black V-Neck Tee", "Everlane", "Black", ["essential", "minimalist"], ["casual", "weekend"], "all"),
        ("Gray T-Shirt", "Uniqlo", "Gray", ["basic", "comfortable"], ["casual", "weekend"], "all"),
        ("Breton Striped Tee", "J.Crew", "Navy/White", ["classic", "nautical"], ["casual", "weekend"], "all"),
        ("Chambray Shirt", "Madewell", "Light Blue", ["casual", "versatile"], ["casual", "weekend"], "all"),
        ("Olive Tee", "Gap", "Olive", ["earthy", "casual"], ["casual", "weekend"], "all"),
        ("Navy Henley", "J.Crew", "Navy", ["casual", "classic"], ["casual", "weekend"], "all"),
        ("Pink T-Shirt", "COS", "Pink", ["soft", "feminine"], ["casual", "weekend"], "spring"),
        ("Rust Tank Top", "Madewell", "Rust", ["warm", "casual"], ["casual", "weekend"], "summer"),
        ("White Tank Top", "Everlane", "White", ["essential", "minimalist"], ["casual", "gym"], "summer"),
        ("Charcoal Tee", "Uniqlo", "Charcoal", ["basic", "versatile"], ["casual", "weekend"], "all"),
        ("Mustard Tee", "& Other Stories", "Mustard", ["bold", "casual"], ["casual", "weekend"], "fall"),
        ("Graphic Tee", "Zara", "White/Black", ["trendy", "casual"], ["casual", "weekend"], "all"),
        ("Long Sleeve Tee", "Gap", "Navy", ["basic", "comfortable"], ["casual", "weekend"], "fall"),
        ("Plaid Shirt", "Madewell", "Red/Black", ["casual", "cozy"], ["casual", "weekend"], "fall"),
        ("Denim Shirt", "Levi's", "Light Blue", ["classic", "casual"], ["casual", "weekend"], "all"),
        ("Tie-Dye Tee", "Urban Outfitters", "Multi", ["fun", "casual"], ["casual", "weekend"], "summer"),
        ("Crop Top", "Zara", "Black", ["trendy", "casual"], ["casual", "party"], "summer"),
        ("Off-Shoulder Top", "H&M", "White", ["feminine", "casual"], ["casual", "brunch"], "summer"),
        ("Peplum Top", "Banana Republic", "Navy", ["feminine", "casual"], ["casual", "brunch"], "all"),
        
        # Sweaters & Knitwear (20)
        ("Gray Cashmere Sweater", "Vince", "Gray", ["cozy", "soft"], ["casual", "weekend"], "fall"),
        ("Blush Pink Sweater", "& Other Stories", "Blush", ["soft", "feminine"], ["casual", "weekend"], "fall"),
        ("Black Cashmere Turtleneck", "Everlane", "Black", ["luxurious", "minimalist"], ["work", "dinner"], "winter"),
        ("Cream Cable Knit", "J.Crew", "Cream", ["cozy", "classic"], ["casual", "weekend"], "winter"),
        ("Navy Turtleneck", "COS", "Navy", ["classic", "warm"], ["work", "casual"], "winter"),
        ("Camel Turtleneck", "Massimo Dutti", "Camel", ["warm", "sophisticated"], ["work", "casual"], "fall"),
        ("Burgundy Sweater", "Mango", "Burgundy", ["rich", "cozy"], ["casual", "weekend"], "fall"),
        ("Forest Green Sweater", "& Other Stories", "Forest Green", ["earthy", "cozy"], ["casual", "weekend"], "fall"),
        ("Oatmeal Cardigan", "Everlane", "Oatmeal", ["soft", "cozy"], ["casual", "weekend"], "fall"),
        ("Charcoal Sweater", "Uniqlo", "Charcoal", ["basic", "warm"], ["casual", "work"], "winter"),
        ("Rust Sweater", "Madewell", "Rust", ["warm", "cozy"], ["casual", "weekend"], "fall"),
        ("Ivory Sweater", "COS", "Ivory", ["soft", "minimalist"], ["casual", "weekend"], "winter"),
        ("Striped Sweater", "J.Crew", "Navy/White", ["nautical", "classic"], ["casual", "weekend"], "all"),
        ("Chunky Knit Sweater", "Free People", "Brown", ["cozy", "bohemian"], ["casual", "weekend"], "winter"),
        ("V-Neck Sweater", "Gap", "Navy", ["classic", "versatile"], ["work", "casual"], "fall"),
        ("Teal Sweater", "& Other Stories", "Teal", ["rich", "cozy"], ["casual", "weekend"], "fall"),
        ("Pink Cardigan", "J.Crew", "Pink", ["feminine", "soft"], ["casual", "weekend"], "spring"),
        ("Oversized Sweater", "Free People", "Gray", ["cozy", "relaxed"], ["casual", "weekend"], "winter"),
        ("Cashmere Hoodie", "Vince", "Charcoal", ["luxurious", "comfortable"], ["casual", "travel"], "all"),
        ("Turtleneck Sweater Dress", "COS", "Black", ["sophisticated", "cozy"], ["work", "dinner"], "winter"),
    ]
    
    for idx, (title, brand, color, style_tags, occasions, season) in enumerate(female_tops_data):
        items.append({
            "category": "tops",
            "gender": "female",
            "image": female_top_images[idx % len(female_top_images)],
            "alt": title.lower(),
            "title": title,
            "description": f"{color} {title.lower()} perfect for {occasions[0]}",
            "brand": brand,
            "color": color,
            "style_tags": str(style_tags).replace("'", '"'),
            "occasions": str(occasions).replace("'", '"'),
            "season": season
        })
    
    # Female Bottoms (70)
    female_bottoms_data = [
        # Formal Pants & Skirts (20)
        ("Black Dress Pants", "Theory", "Black", ["professional", "formal"], ["work", "business"], "all"),
        ("Navy Dress Pants", "Banana Republic", "Navy", ["professional", "formal"], ["work", "business"], "all"),
        ("Gray Trousers", "J.Crew", "Gray", ["classic", "professional"], ["work", "business"], "all"),
        ("Charcoal Trousers", "Hugo Boss", "Charcoal", ["modern", "professional"], ["work", "business"], "all"),
        ("Camel Trousers", "Massimo Dutti", "Camel", ["sophisticated", "warm"], ["work", "brunch"], "fall"),
        ("Black Pencil Skirt", "Theory", "Black", ["professional", "sleek"], ["work", "business"], "all"),
        ("Navy Pencil Skirt", "Banana Republic", "Navy", ["professional", "classic"], ["work", "business"], "all"),
        ("Gray Pencil Skirt", "J.Crew", "Gray", ["professional", "versatile"], ["work", "business"], "all"),
        ("Burgundy Pencil Skirt", "Ann Taylor", "Burgundy", ["rich", "professional"], ["work", "dinner"], "fall"),
        ("Cream A-Line Skirt", "COS", "Cream", ["elegant", "feminine"], ["work", "brunch"], "spring"),
        ("Black Midi Skirt", "& Other Stories", "Black", ["sophisticated", "modern"], ["work", "dinner"], "all"),
        ("Navy Midi Skirt", "COS", "Navy", ["classic", "elegant"], ["work", "dinner"], "all"),
        ("Plaid Pencil Skirt", "J.Crew", "Gray/Black", ["classic", "professional"], ["work", "business"], "fall"),
        ("White Wide-Leg Pants", "Theory", "White", ["fresh", "sophisticated"], ["work", "brunch"], "summer"),
        ("Navy Wide-Leg Pants", "Mango", "Navy", ["elegant", "comfortable"], ["work", "casual"], "all"),
        ("Beige Trousers", "Massimo Dutti", "Beige", ["soft", "professional"], ["work", "casual"], "all"),
        ("Black Culottes", "COS", "Black", ["modern", "sophisticated"], ["work", "casual"], "all"),
        ("Gray Culottes", "& Other Stories", "Gray", ["modern", "comfortable"], ["work", "casual"], "all"),
        ("Leather Pencil Skirt", "Reiss", "Black", ["edgy", "sophisticated"], ["work", "dinner"], "all"),
        ("Tweed Skirt", "J.Crew", "Brown/Beige", ["classic", "textured"], ["work", "brunch"], "fall"),
        
        # Jeans (20)
        ("Dark Wash Skinny Jeans", "Levi's", "Dark Blue", ["classic", "versatile"], ["casual", "weekend"], "all"),
        ("Black Skinny Jeans", "Madewell", "Black", ["sleek", "versatile"], ["casual", "weekend"], "all"),
        ("Light Wash Jeans", "Levi's", "Light Blue", ["casual", "relaxed"], ["casual", "weekend"], "all"),
        ("High-Waisted Black Jeans", "Everlane", "Black", ["modern", "flattering"], ["casual", "weekend"], "all"),
        ("Blue Straight-Leg Jeans", "Levi's", "Medium Blue", ["classic", "comfortable"], ["casual", "weekend"], "all"),
        ("White Jeans", "J.Crew", "White", ["fresh", "summery"], ["casual", "brunch"], "summer"),
        ("Distressed Jeans", "Madewell", "Light Blue", ["casual", "edgy"], ["casual", "weekend"], "all"),
        ("Black Ripped Jeans", "Zara", "Black", ["edgy", "trendy"], ["casual", "party"], "all"),
        ("Cropped Jeans", "Everlane", "Dark Blue", ["modern", "versatile"], ["casual", "weekend"], "spring"),
        ("Mom Jeans", "Levi's", "Medium Blue", ["vintage", "relaxed"], ["casual", "weekend"], "all"),
        ("Bootcut Jeans", "J.Crew", "Dark Blue", ["classic", "flattering"], ["casual", "weekend"], "all"),
        ("Flare Jeans", "Madewell", "Dark Blue", ["retro", "flattering"], ["casual", "weekend"], "all"),
        ("Gray Jeans", "Everlane", "Gray", ["modern", "versatile"], ["casual", "weekend"], "all"),
        ("Olive Jeans", "Madewell", "Olive", ["earthy", "casual"], ["casual", "weekend"], "all"),
        ("Black Coated Jeans", "J Brand", "Black", ["sleek", "edgy"], ["casual", "party"], "all"),
        ("Blue Boyfriend Jeans", "Gap", "Light Blue", ["relaxed", "comfortable"], ["casual", "weekend"], "all"),
        ("High-Waisted White Jeans", "Madewell", "White", ["fresh", "modern"], ["casual", "brunch"], "summer"),
        ("Cuffed Jeans", "Levi's", "Dark Blue", ["casual", "versatile"], ["casual", "weekend"], "all"),
        ("Jeggings", "Uniqlo", "Black", ["comfortable", "sleek"], ["casual", "travel"], "all"),
        ("Embroidered Jeans", "Madewell", "Light Blue", ["feminine", "trendy"], ["casual", "brunch"], "spring"),
        
        # Casual Skirts & Shorts (20)
        ("Denim Mini Skirt", "Levi's", "Light Blue", ["casual", "youthful"], ["casual", "weekend"], "summer"),
        ("Black Mini Skirt", "Zara", "Black", ["edgy", "versatile"], ["casual", "party"], "all"),
        ("Floral Midi Skirt", "& Other Stories", "Multi", ["feminine", "romantic"], ["casual", "brunch"], "spring"),
        ("Plaid Mini Skirt", "Urban Outfitters", "Red/Black", ["preppy", "casual"], ["casual", "weekend"], "fall"),
        ("White Tennis Skirt", "Lululemon", "White", ["sporty", "fresh"], ["casual", "gym"], "summer"),
        ("Leather Mini Skirt", "Zara", "Black", ["edgy", "bold"], ["casual", "party"], "all"),
        ("Denim Shorts", "Levi's", "Light Blue", ["casual", "comfortable"], ["casual", "weekend"], "summer"),
        ("Black Shorts", "Gap", "Black", ["versatile", "casual"], ["casual", "weekend"], "summer"),
        ("White Shorts", "J.Crew", "White", ["fresh", "summery"], ["casual", "beach"], "summer"),
        ("Khaki Shorts", "Gap", "Khaki", ["classic", "casual"], ["casual", "weekend"], "summer"),
        ("Flowy Midi Skirt", "Free People", "Rust", ["bohemian", "feminine"], ["casual", "brunch"], "fall"),
        ("Wrap Skirt", "& Other Stories", "Navy", ["feminine", "versatile"], ["casual", "brunch"], "all"),
        ("Pleated Midi Skirt", "COS", "Gray", ["elegant", "modern"], ["casual", "brunch"], "all"),
        ("Maxi Skirt", "Free People", "Black", ["bohemian", "flowy"], ["casual", "weekend"], "summer"),
        ("Silk Slip Skirt", "& Other Stories", "Burgundy", ["luxurious", "feminine"], ["casual", "dinner"], "fall"),
        ("Athletic Shorts", "Nike", "Black", ["sporty", "comfortable"], ["gym", "casual"], "summer"),
        ("Bike Shorts", "Lululemon", "Black", ["sporty", "trendy"], ["gym", "casual"], "summer"),
        ("Linen Shorts", "Everlane", "Beige", ["breathable", "casual"], ["casual", "beach"], "summer"),
        ("Paperbag Shorts", "Mango", "Tan", ["trendy", "feminine"], ["casual", "brunch"], "summer"),
        ("Striped Shorts", "J.Crew", "Navy/White", ["nautical", "casual"], ["casual", "beach"], "summer"),
        
        # Leggings & Active (10)
        ("Black Leggings", "Lululemon", "Black", ["comfortable", "athletic"], ["gym", "casual"], "all"),
        ("Navy Leggings", "Nike", "Navy", ["sporty", "versatile"], ["gym", "casual"], "all"),
        ("Gray Leggings", "Athleta", "Gray", ["comfortable", "athletic"], ["gym", "casual"], "all"),
        ("High-Waisted Leggings", "Lululemon", "Black", ["supportive", "flattering"], ["gym", "casual"], "all"),
        ("Yoga Pants", "Lululemon", "Black", ["comfortable", "flexible"], ["gym", "yoga"], "all"),
        ("Joggers", "Nike", "Gray", ["comfortable", "casual"], ["casual", "travel"], "all"),
        ("Track Pants", "Adidas", "Black", ["sporty", "comfortable"], ["gym", "casual"], "all"),
        ("Capri Leggings", "Nike", "Black", ["sporty", "versatile"], ["gym", "casual"], "summer"),
        ("Printed Leggings", "Lululemon", "Multi", ["fun", "athletic"], ["gym", "casual"], "all"),
        ("Fleece Lined Leggings", "Uniqlo", "Black", ["warm", "comfortable"], ["casual", "winter"], "winter"),
    ]
    
    for idx, (title, brand, color, style_tags, occasions, season) in enumerate(female_bottoms_data):
        items.append({
            "category": "bottoms",
            "gender": "female",
            "image": female_bottom_images[idx % len(female_bottom_images)],
            "alt": title.lower(),
            "title": title,
            "description": f"{color} {title.lower()} for {occasions[0]}",
            "brand": brand,
            "color": color,
            "style_tags": str(style_tags).replace("'", '"'),
            "occasions": str(occasions).replace("'", '"'),
            "season": season
        })
    
    # Female Shoes (60)
    female_shoes_data = [
        # Formal Shoes (15)
        ("Black Pumps", "Jimmy Choo", "Black", ["elegant", "formal"], ["work", "formal"], "all"),
        ("Navy Heels", "Stuart Weitzman", "Navy", ["sophisticated", "formal"], ["work", "formal"], "all"),
        ("Nude Pumps", "Christian Louboutin", "Nude", ["classic", "elegant"], ["work", "formal"], "all"),
        ("Black Pointed Flats", "Sam Edelman", "Black", ["sleek", "comfortable"], ["work", "travel"], "all"),
        ("Navy Flats", "Tory Burch", "Navy", ["classic", "comfortable"], ["work", "casual"], "all"),
        ("Patent Leather Pumps", "Stuart Weitzman", "Black", ["glossy", "formal"], ["work", "formal"], "all"),
        ("Burgundy Heels", "Nine West", "Burgundy", ["rich", "elegant"], ["work", "dinner"], "fall"),
        ("Gray Pumps", "Vince", "Gray", ["modern", "elegant"], ["work", "formal"], "all"),
        ("Black Ankle Boots", "Stuart Weitzman", "Black", ["sophisticated", "versatile"], ["work", "casual"], "fall"),
        ("Brown Ankle Boots", "Sam Edelman", "Brown", ["classic", "warm"], ["work", "casual"], "fall"),
        ("Black Loafers", "Gucci", "Black", ["polished", "comfortable"], ["work", "casual"], "all"),
        ("Tan Loafers", "Tod's", "Tan", ["classic", "sophisticated"], ["work", "casual"], "all"),
        ("Black Mary Janes", "Repetto", "Black", ["classic", "feminine"], ["work", "casual"], "all"),
        ("Black Kitten Heels", "Sarah Flint", "Black", ["elegant", "comfortable"], ["work", "dinner"], "all"),
        ("Nude Heels", "Sam Edelman", "Nude", ["versatile", "elegant"], ["work", "formal"], "all"),
        
        # Boots (15)
        ("Black Leather Boots", "Stuart Weitzman", "Black", ["classic", "versatile"], ["casual", "winter"], "winter"),
        ("Brown Leather Boots", "Frye", "Brown", ["rustic", "warm"], ["casual", "winter"], "fall"),
        ("Chelsea Boots", "Acne Studios", "Black", ["modern", "sleek"], ["casual", "work"], "fall"),
        ("Combat Boots", "Dr. Martens", "Black", ["edgy", "durable"], ["casual", "winter"], "fall"),
        ("Over-The-Knee Boots", "Stuart Weitzman", "Black", ["bold", "sleek"], ["party", "dinner"], "winter"),
        ("Suede Ankle Boots", "Sam Edelman", "Tan", ["soft", "versatile"], ["casual", "work"], "fall"),
        ("Rain Boots", "Hunter", "Black", ["practical", "waterproof"], ["casual", "rainy"], "all"),
        ("Snow Boots", "Sorel", "Brown", ["warm", "practical"], ["casual", "winter"], "winter"),
        ("Western Boots", "Frye", "Brown", ["bohemian", "rustic"], ["casual", "weekend"], "fall"),
        ("Riding Boots", "Tory Burch", "Brown", ["classic", "sophisticated"], ["casual", "work"], "fall"),
        ("Lace-Up Boots", "Timberland", "Tan", ["rugged", "casual"], ["casual", "hiking"], "fall"),
        ("Heeled Boots", "Stuart Weitzman", "Black", ["elegant", "sleek"], ["work", "dinner"], "winter"),
        ("Sock Boots", "Balenciaga", "Black", ["modern", "sleek"], ["casual", "party"], "fall"),
        ("Wedge Boots", "UGG", "Brown", ["comfortable", "casual"], ["casual", "winter"], "winter"),
        ("Platform Boots", "Jeffrey Campbell", "Black", ["bold", "edgy"], ["party", "casual"], "fall"),
        
        # Sneakers (15)
        ("White Leather Sneakers", "Common Projects", "White", ["minimalist", "clean"], ["casual", "travel"], "all"),
        ("Black Sneakers", "Adidas", "Black", ["classic", "versatile"], ["casual", "gym"], "all"),
        ("White Canvas Sneakers", "Converse", "White", ["casual", "classic"], ["casual", "weekend"], "all"),
        ("Black Canvas Sneakers", "Vans", "Black", ["edgy", "casual"], ["casual", "weekend"], "all"),
        ("Gray Athletic Shoes", "Nike", "Gray", ["sporty", "comfortable"], ["gym", "casual"], "all"),
        ("Pink Sneakers", "Nike", "Pink", ["feminine", "sporty"], ["gym", "casual"], "all"),
        ("Beige Sneakers", "Veja", "Beige", ["sustainable", "casual"], ["casual", "travel"], "all"),
        ("Navy Sneakers", "New Balance", "Navy", ["classic", "comfortable"], ["casual", "gym"], "all"),
        ("Platform Sneakers", "Superga", "White", ["trendy", "comfortable"], ["casual", "weekend"], "all"),
        ("Slip-On Sneakers", "Vans", "Black", ["convenient", "casual"], ["casual", "travel"], "all"),
        ("High-Top Sneakers", "Converse", "White", ["classic", "casual"], ["casual", "weekend"], "all"),
        ("Running Shoes", "Nike", "Multi", ["athletic", "supportive"], ["gym", "running"], "all"),
        ("Metallic Sneakers", "Golden Goose", "Silver", ["trendy", "eye-catching"], ["casual", "party"], "all"),
        ("Chunky Sneakers", "Balenciaga", "White", ["bold", "trendy"], ["casual", "party"], "all"),
        ("Velcro Sneakers", "Veja", "White", ["convenient", "casual"], ["casual", "travel"], "all"),
        
        # Sandals & Summer (15)
        ("Black Sandals", "Birkenstock", "Black", ["comfortable", "casual"], ["casual", "summer"], "summer"),
        ("Brown Leather Sandals", "Tory Burch", "Brown", ["classic", "elegant"], ["casual", "beach"], "summer"),
        ("White Sandals", "Ancient Greek Sandals", "White", ["minimalist", "summery"], ["casual", "beach"], "summer"),
        ("Slide Sandals", "Gucci", "Black", ["luxurious", "comfortable"], ["casual", "pool"], "summer"),
        ("Gladiator Sandals", "Sam Edelman", "Tan", ["bohemian", "edgy"], ["casual", "summer"], "summer"),
        ("Wedge Sandals", "Stuart Weitzman", "Beige", ["elegant", "comfortable"], ["casual", "brunch"], "summer"),
        ("Espadrilles", "Castañer", "Beige", ["summery", "comfortable"], ["casual", "beach"], "summer"),
        ("Platform Sandals", "Steve Madden", "Black", ["bold", "trendy"], ["party", "casual"], "summer"),
        ("Strappy Heels", "Stuart Weitzman", "Black", ["elegant", "formal"], ["formal", "party"], "summer"),
        ("Metallic Sandals", "Sam Edelman", "Gold", ["glamorous", "summery"], ["party", "beach"], "summer"),
        ("Flat Sandals", "Tory Burch", "Tan", ["classic", "comfortable"], ["casual", "travel"], "summer"),
        ("Cork Sandals", "Birkenstock", "Brown", ["natural", "comfortable"], ["casual", "beach"], "summer"),
        ("Jelly Sandals", "Melissa", "Clear", ["fun", "waterproof"], ["casual", "beach"], "summer"),
        ("Flip Flops", "Havaianas", "Black", ["casual", "beach"], ["beach", "pool"], "summer"),
        ("Sport Sandals", "Teva", "Black", ["practical", "comfortable"], ["hiking", "casual"], "summer"),
    ]
    
    for idx, (title, brand, color, style_tags, occasions, season) in enumerate(female_shoes_data):
        items.append({
            "category": "shoes",
            "gender": "female",
            "image": female_shoes_images[idx % len(female_shoes_images)],
            "alt": title.lower(),
            "title": title,
            "description": f"{color} {title.lower()} for {occasions[0]}",
            "brand": brand,
            "color": color,
            "style_tags": str(style_tags).replace("'", '"'),
            "occasions": str(occasions).replace("'", '"'),
            "season": season
        })
    
    # Female Accessories (40)
    female_accessories_data = [
        # Bags (20)
        ("Black Leather Tote", "Cuyana", "Black", ["professional", "spacious"], ["work", "travel"], "all"),
        ("Tan Leather Tote", "Madewell", "Tan", ["classic", "versatile"], ["work", "casual"], "all"),
        ("Crossbody Bag", "Kate Spade", "Black", ["convenient", "chic"], ["casual", "travel"], "all"),
        ("Beige Crossbody", "Celine", "Beige", ["minimalist", "elegant"], ["casual", "dinner"], "all"),
        ("Black Backpack", "Matt & Nat", "Black", ["practical", "modern"], ["casual", "work"], "all"),
        ("Leather Backpack", "Everlane", "Brown", ["professional", "comfortable"], ["work", "travel"], "all"),
        ("Evening Clutch", "Judith Leiber", "Gold", ["glamorous", "elegant"], ["formal", "party"], "all"),
        ("Black Clutch", "Saint Laurent", "Black", ["sleek", "elegant"], ["dinner", "formal"], "all"),
        ("Straw Tote", "Mar Y Sol", "Natural", ["summery", "casual"], ["beach", "casual"], "summer"),
        ("Canvas Tote", "Baggu", "Beige", ["casual", "eco-friendly"], ["casual", "shopping"], "all"),
        ("Bucket Bag", "Mansur Gavriel", "Tan", ["trendy", "spacious"], ["casual", "work"], "all"),
        ("Mini Bag", "Jacquemus", "Beige", ["trendy", "compact"], ["casual", "party"], "all"),
        ("Saddle Bag", "Dior", "Black", ["classic", "elegant"], ["casual", "dinner"], "all"),
        ("Shoulder Bag", "Coach", "Brown", ["classic", "versatile"], ["casual", "work"], "all"),
        ("Hobo Bag", "Rebecca Minkoff", "Black", ["relaxed", "spacious"], ["casual", "weekend"], "all"),
        ("Belt Bag", "Lululemon", "Black", ["practical", "sporty"], ["casual", "travel"], "all"),
        ("Weekender Bag", "Lo & Sons", "Navy", ["spacious", "travel"], ["travel", "weekend"], "all"),
        ("Laptop Bag", "Away", "Black", ["professional", "protective"], ["work", "travel"], "all"),
        ("Beach Bag", "Baggu", "Striped", ["summery", "spacious"], ["beach", "vacation"], "summer"),
        ("Gym Bag", "Lululemon", "Black", ["sporty", "practical"], ["gym", "casual"], "all"),
        
        # Jewelry & Other Accessories (20)
        ("Gold Hoop Earrings", "Mejuri", "Gold", ["classic", "elegant"], ["casual", "work"], "all"),
        ("Silver Hoop Earrings", "Mejuri", "Silver", ["minimalist", "versatile"], ["casual", "work"], "all"),
        ("Pearl Earrings", "Mikimoto", "White", ["classic", "elegant"], ["work", "formal"], "all"),
        ("Statement Necklace", "BaubleBar", "Gold", ["bold", "glamorous"], ["party", "dinner"], "all"),
        ("Delicate Necklace", "Mejuri", "Gold", ["minimalist", "delicate"], ["casual", "work"], "all"),
        ("Layered Necklaces", "Gorjana", "Gold", ["trendy", "feminine"], ["casual", "party"], "all"),
        ("Gold Watch", "Daniel Wellington", "Gold", ["classic", "elegant"], ["work", "formal"], "all"),
        ("Leather Watch", "Timex", "Brown/Gold", ["classic", "versatile"], ["casual", "work"], "all"),
        ("Silk Scarf", "Hermès", "Multi", ["luxurious", "elegant"], ["work", "travel"], "all"),
        ("Wool Scarf", "Acne Studios", "Gray", ["cozy", "minimalist"], ["casual", "winter"], "winter"),
        ("Cashmere Scarf", "Everlane", "Camel", ["soft", "warm"], ["casual", "winter"], "winter"),
        ("Black Belt", "Gucci", "Black", ["classic", "polished"], ["work", "casual"], "all"),
        ("Brown Leather Belt", "Madewell", "Brown", ["classic", "versatile"], ["casual", "work"], "all"),
        ("Aviator Sunglasses", "Ray-Ban", "Gold/Brown", ["classic", "cool"], ["casual", "travel"], "summer"),
        ("Cat-Eye Sunglasses", "Celine", "Black", ["retro", "chic"], ["casual", "travel"], "summer"),
        ("Wayfarer Sunglasses", "Ray-Ban", "Black", ["classic", "versatile"], ["casual", "beach"], "summer"),
        ("Beanie Hat", "Acne Studios", "Black", ["cozy", "minimalist"], ["casual", "winter"], "winter"),
        ("Fedora Hat", "Janessa Leone", "Beige", ["bohemian", "stylish"], ["casual", "beach"], "summer"),
        ("Baseball Cap", "Nike", "Black", ["sporty", "casual"], ["casual", "gym"], "all"),
        ("Wide-Brim Hat", "Janessa Leone", "Tan", ["summery", "elegant"], ["beach", "vacation"], "summer"),
    ]
    
    for idx, (title, brand, color, style_tags, occasions, season) in enumerate(female_accessories_data):
        items.append({
            "category": "accessories",
            "gender": "female",
            "image": female_accessory_images[idx % len(female_accessory_images)],
            "alt": title.lower(),
            "title": title,
            "description": f"{color} {title.lower()} to complete your look",
            "brand": brand,
            "color": color,
            "style_tags": str(style_tags).replace("'", '"'),
            "occasions": str(occasions).replace("'", '"'),
            "season": season
        })
    
    # MALE ITEMS (250 total: 80 tops, 70 bottoms, 60 shoes, 40 accessories)
    
    # Male Tops (80)
    male_tops_data = [
        # Formal Shirts & Suits (25)
        ("White Dress Shirt", "Brooks Brothers", "White", ["classic", "formal"], ["work", "formal"], "all"),
        ("Light Blue Dress Shirt", "Charles Tyrwhitt", "Light Blue", ["classic", "professional"], ["work", "formal"], "all"),
        ("Black Dress Shirt", "Hugo Boss", "Black", ["sophisticated", "formal"], ["formal", "dinner"], "all"),
        ("Navy Dress Shirt", "Brooks Brothers", "Navy", ["classic", "professional"], ["work", "formal"], "all"),
        ("Pink Dress Shirt", "Thomas Pink", "Pink", ["refined", "professional"], ["work", "formal"], "all"),
        ("Gray Dress Shirt", "Calvin Klein", "Gray", ["modern", "professional"], ["work", "formal"], "all"),
        ("Striped Dress Shirt", "Ralph Lauren", "Blue/White", ["classic", "professional"], ["work", "formal"], "all"),
        ("Black Suit Jacket", "Hugo Boss", "Black", ["formal", "sophisticated"], ["formal", "business"], "all"),
        ("Navy Suit Jacket", "J.Crew", "Navy", ["classic", "versatile"], ["work", "formal"], "all"),
        ("Charcoal Suit Jacket", "Bonobos", "Charcoal", ["professional", "modern"], ["work", "formal"], "all"),
        ("Tuxedo Jacket", "Tom Ford", "Black", ["luxurious", "formal"], ["formal", "black tie"], "all"),
        ("Gray Blazer", "Banana Republic", "Gray", ["versatile", "professional"], ["work", "business"], "all"),
        ("Navy Blazer", "J.Crew", "Navy", ["classic", "versatile"], ["work", "casual"], "all"),
        ("Tan Blazer", "Bonobos", "Tan", ["warm", "sophisticated"], ["work", "casual"], "fall"),
        ("Black Blazer", "Calvin Klein", "Black", ["sleek", "formal"], ["work", "formal"], "all"),
        ("Chambray Dress Shirt", "J.Crew", "Light Blue", ["casual", "versatile"], ["casual", "work"], "all"),
        ("Oxford Shirt", "Brooks Brothers", "White", ["classic", "crisp"], ["work", "casual"], "all"),
        ("Blue Oxford Shirt", "Ralph Lauren", "Blue", ["preppy", "classic"], ["work", "casual"], "all"),
        ("Flannel Shirt", "Pendleton", "Red/Black", ["rugged", "warm"], ["casual", "weekend"], "fall"),
        ("Linen Shirt", "Bonobos", "White", ["breathable", "casual"], ["casual", "beach"], "summer"),
        ("Cuban Collar Shirt", "Reiss", "Navy", ["retro", "casual"], ["casual", "party"], "summer"),
        ("Band Collar Shirt", "COS", "White", ["modern", "minimalist"], ["casual", "work"], "all"),
        ("Henley Shirt", "J.Crew", "Navy", ["casual", "classic"], ["casual", "weekend"], "all"),
        ("Polo Shirt", "Ralph Lauren", "Navy", ["preppy", "casual"], ["casual", "golf"], "summer"),
        ("Black Polo", "Lacoste", "Black", ["classic", "sporty"], ["casual", "golf"], "all"),
        
        # Casual Shirts & Tees (25)
        ("White T-Shirt", "Everlane", "White", ["essential", "minimalist"], ["casual", "weekend"], "all"),
        ("Black T-Shirt", "Uniqlo", "Black", ["essential", "versatile"], ["casual", "weekend"], "all"),
        ("Gray T-Shirt", "Everlane", "Gray", ["basic", "comfortable"], ["casual", "gym"], "all"),
        ("Navy T-Shirt", "J.Crew", "Navy", ["classic", "versatile"], ["casual", "weekend"], "all"),
        ("White V-Neck", "Calvin Klein", "White", ["clean", "minimalist"], ["casual", "weekend"], "all"),
        ("Black V-Neck", "Uniqlo", "Black", ["sleek", "versatile"], ["casual", "weekend"], "all"),
        ("Striped T-Shirt", "J.Crew", "Navy/White", ["nautical", "classic"], ["casual", "weekend"], "all"),
        ("Graphic Tee", "Urban Outfitters", "Black", ["trendy", "casual"], ["casual", "weekend"], "all"),
        ("Long Sleeve Tee", "Everlane", "Charcoal", ["comfortable", "versatile"], ["casual", "weekend"], "fall"),
        ("Henley", "J.Crew", "Oatmeal", ["casual", "classic"], ["casual", "weekend"], "all"),
        ("Flannel Shirt", "Patagonia", "Green/Blue", ["rugged", "outdoor"], ["casual", "hiking"], "fall"),
        ("Plaid Shirt", "Gap", "Red/Black", ["casual", "cozy"], ["casual", "weekend"], "fall"),
        ("Denim Shirt", "Levi's", "Light Blue", ["classic", "casual"], ["casual", "weekend"], "all"),
        ("Chambray Shirt", "Bonobos", "Blue", ["casual", "versatile"], ["casual", "work"], "all"),
        ("Work Shirt", "Carhartt", "Brown", ["durable", "rugged"], ["casual", "work"], "all"),
        ("Hawaiian Shirt", "Tommy Bahama", "Multi", ["fun", "vacation"], ["casual", "beach"], "summer"),
        ("Linen Tee", "Everlane", "White", ["breathable", "summery"], ["casual", "beach"], "summer"),
        ("Pocket Tee", "J.Crew", "Navy", ["casual", "classic"], ["casual", "weekend"], "all"),
        ("Baseball Tee", "Alternative", "White/Navy", ["sporty", "casual"], ["casual", "weekend"], "all"),
        ("Tank Top", "Everlane", "White", ["minimal", "summery"], ["casual", "gym"], "summer"),
        ("Muscle Tee", "Nike", "Gray", ["athletic", "casual"], ["gym", "casual"], "summer"),
        ("Ringer Tee", "Champion", "White/Navy", ["retro", "casual"], ["casual", "weekend"], "all"),
        ("Raglan Tee", "Alternative", "Gray/Black", ["sporty", "casual"], ["casual", "weekend"], "all"),
        ("Thermal Shirt", "Hanes", "Charcoal", ["warm", "layering"], ["casual", "winter"], "winter"),
        ("Waffle Knit Tee", "Bonobos", "Navy", ["textured", "casual"], ["casual", "weekend"], "fall"),
        
        # Sweaters & Knitwear (30)
        ("Navy Crewneck Sweater", "J.Crew", "Navy", ["classic", "versatile"], ["casual", "work"], "fall"),
        ("Gray Cashmere Sweater", "Everlane", "Gray", ["luxurious", "soft"], ["work", "casual"], "fall"),
        ("Black Turtleneck", "COS", "Black", ["sleek", "minimalist"], ["work", "dinner"], "winter"),
        ("Charcoal Sweater", "Uniqlo", "Charcoal", ["basic", "warm"], ["casual", "work"], "winter"),
        ("Oatmeal Sweater", "Bonobos", "Oatmeal", ["soft", "neutral"], ["casual", "weekend"], "fall"),
        ("Burgundy Sweater", "J.Crew", "Burgundy", ["rich", "warm"], ["casual", "work"], "fall"),
        ("Forest Green Sweater", "Bonobos", "Forest Green", ["earthy", "cozy"], ["casual", "weekend"], "fall"),
        ("Camel Sweater", "Massimo Dutti", "Camel", ["warm", "sophisticated"], ["work", "casual"], "fall"),
        ("Cable Knit Sweater", "J.Crew", "Cream", ["classic", "textured"], ["casual", "weekend"], "winter"),
        ("V-Neck Sweater", "Banana Republic", "Navy", ["classic", "layering"], ["work", "casual"], "fall"),
        ("Quarter-Zip Sweater", "Bonobos", "Gray", ["athletic", "casual"], ["casual", "golf"], "fall"),
        ("Shawl Collar Cardigan", "J.Crew", "Charcoal", ["cozy", "refined"], ["casual", "weekend"], "fall"),
        ("Zip Cardigan", "Uniqlo", "Navy", ["comfortable", "casual"], ["casual", "travel"], "fall"),
        ("Fisherman Sweater", "Aran Crafts", "Cream", ["chunky", "traditional"], ["casual", "weekend"], "winter"),
        ("Fair Isle Sweater", "Ralph Lauren", "Multi", ["festive", "classic"], ["casual", "weekend"], "winter"),
        ("Merino Wool Sweater", "Bonobos", "Gray", ["soft", "versatile"], ["work", "casual"], "fall"),
        ("Cashmere Turtleneck", "Everlane", "Black", ["luxurious", "warm"], ["work", "dinner"], "winter"),
        ("Mock Neck Sweater", "COS", "Charcoal", ["modern", "sleek"], ["work", "casual"], "fall"),
        ("Striped Sweater", "J.Crew", "Navy/White", ["nautical", "classic"], ["casual", "weekend"], "all"),
        ("Colorblock Sweater", "Bonobos", "Multi", ["bold", "trendy"], ["casual", "weekend"], "fall"),
        ("Hoodie", "Champion", "Gray", ["comfortable", "casual"], ["casual", "gym"], "all"),
        ("Zip Hoodie", "Nike", "Black", ["sporty", "casual"], ["gym", "casual"], "all"),
        ("Pullover Hoodie", "Patagonia", "Navy", ["outdoor", "casual"], ["casual", "hiking"], "all"),
        ("Fleece Pullover", "Patagonia", "Gray", ["warm", "outdoor"], ["casual", "hiking"], "fall"),
        ("Henley Sweater", "J.Crew", "Oatmeal", ["casual", "textured"], ["casual", "weekend"], "fall"),
        ("Bomber Sweater", "Bonobos", "Navy", ["modern", "casual"], ["casual", "weekend"], "fall"),
        ("Varsity Cardigan", "J.Crew", "Gray/Navy", ["preppy", "casual"], ["casual", "weekend"], "fall"),
        ("Cashmere Hoodie", "Vince", "Charcoal", ["luxurious", "comfortable"], ["casual", "travel"], "all"),
        ("Rollneck Sweater", "COS", "Black", ["minimalist", "modern"], ["work", "dinner"], "fall"),
        ("Chunky Knit Sweater", "Bonobos", "Oatmeal", ["cozy", "textured"], ["casual", "weekend"], "winter"),
    ]
    
    for idx, (title, brand, color, style_tags, occasions, season) in enumerate(male_tops_data):
        items.append({
            "category": "tops",
            "gender": "male",
            "image": male_top_images[idx % len(male_top_images)],
            "alt": title.lower(),
            "title": title,
            "description": f"{color} {title.lower()} perfect for {occasions[0]}",
            "brand": brand,
            "color": color,
            "style_tags": str(style_tags).replace("'", '"'),
            "occasions": str(occasions).replace("'", '"'),
            "season": season
        })
    
    # Male Bottoms (70)
    male_bottoms_data = [
        # Dress Pants (20)
        ("Black Dress Pants", "Hugo Boss", "Black", ["formal", "professional"], ["work", "formal"], "all"),
        ("Navy Dress Pants", "J.Crew", "Navy", ["classic", "versatile"], ["work", "formal"], "all"),
        ("Charcoal Dress Pants", "Bonobos", "Charcoal", ["professional", "modern"], ["work", "formal"], "all"),
        ("Gray Dress Pants", "Banana Republic", "Gray", ["versatile", "professional"], ["work", "formal"], "all"),
        ("Khaki Dress Pants", "Bonobos", "Khaki", ["classic", "versatile"], ["work", "casual"], "all"),
        ("Navy Suit Pants", "J.Crew", "Navy", ["formal", "tailored"], ["work", "formal"], "all"),
        ("Black Suit Pants", "Calvin Klein", "Black", ["formal", "sleek"], ["work", "formal"], "all"),
        ("Tan Chinos", "Bonobos", "Tan", ["casual", "versatile"], ["casual", "work"], "all"),
        ("Navy Chinos", "J.Crew", "Navy", ["classic", "versatile"], ["casual", "work"], "all"),
        ("Olive Chinos", "Bonobos", "Olive", ["earthy", "casual"], ["casual", "weekend"], "all"),
        ("Gray Chinos", "Gap", "Gray", ["modern", "versatile"], ["casual", "work"], "all"),
        ("Beige Chinos", "Banana Republic", "Beige", ["neutral", "classic"], ["casual", "work"], "all"),
        ("Burgundy Chinos", "J.Crew", "Burgundy", ["rich", "bold"], ["casual", "work"], "fall"),
        ("White Chinos", "Bonobos", "White", ["fresh", "summery"], ["casual", "beach"], "summer"),
        ("Black Chinos", "Levi's", "Black", ["sleek", "versatile"], ["casual", "work"], "all"),
        ("Corduroy Pants", "J.Crew", "Brown", ["textured", "vintage"], ["casual", "weekend"], "fall"),
        ("Wool Trousers", "Brooks Brothers", "Charcoal", ["warm", "professional"], ["work", "formal"], "winter"),
        ("Pleated Pants", "Ralph Lauren", "Navy", ["classic", "formal"], ["work", "formal"], "all"),
        ("Flat Front Pants", "Bonobos", "Gray", ["modern", "professional"], ["work", "casual"], "all"),
        ("Dress Chinos", "Bonobos", "Khaki", ["polished", "versatile"], ["work", "casual"], "all"),
        
        # Jeans (25)
        ("Dark Wash Jeans", "Levi's 511", "Dark Blue", ["classic", "slim"], ["casual", "weekend"], "all"),
        ("Black Jeans", "Levi's 511", "Black", ["versatile", "sleek"], ["casual", "weekend"], "all"),
        ("Light Wash Jeans", "Levi's 501", "Light Blue", ["casual", "relaxed"], ["casual", "weekend"], "all"),
        ("Indigo Jeans", "Levi's 513", "Indigo", ["classic", "comfortable"], ["casual", "weekend"], "all"),
        ("Gray Jeans", "Bonobos", "Gray", ["modern", "versatile"], ["casual", "weekend"], "all"),
        ("Selvedge Jeans", "A.P.C.", "Dark Blue", ["premium", "durable"], ["casual", "weekend"], "all"),
        ("Raw Denim", "Naked & Famous", "Dark Blue", ["authentic", "rugged"], ["casual", "weekend"], "all"),
        ("Distressed Jeans", "Levi's", "Light Blue", ["edgy", "casual"], ["casual", "weekend"], "all"),
        ("Ripped Jeans", "Zara", "Black", ["edgy", "trendy"], ["casual", "party"], "all"),
        ("Skinny Jeans", "Levi's 510", "Dark Blue", ["modern", "fitted"], ["casual", "party"], "all"),
        ("Slim Jeans", "Levi's 511", "Medium Blue", ["versatile", "modern"], ["casual", "weekend"], "all"),
        ("Straight Jeans", "Levi's 501", "Dark Blue", ["classic", "timeless"], ["casual", "weekend"], "all"),
        ("Bootcut Jeans", "Wrangler", "Medium Blue", ["western", "comfortable"], ["casual", "weekend"], "all"),
        ("Relaxed Fit Jeans", "Levi's 550", "Dark Blue", ["comfortable", "loose"], ["casual", "weekend"], "all"),
        ("Tapered Jeans", "Levi's 512", "Black", ["modern", "fitted"], ["casual", "weekend"], "all"),
        ("Acid Wash Jeans", "Levi's", "Light Blue", ["vintage", "retro"], ["casual", "party"], "all"),
        ("Coated Jeans", "J Brand", "Black", ["sleek", "edgy"], ["casual", "party"], "all"),
        ("White Jeans", "Levi's", "White", ["fresh", "summery"], ["casual", "beach"], "summer"),
        ("Carpenter Jeans", "Carhartt", "Blue", ["utilitarian", "durable"], ["work", "casual"], "all"),
        ("Black Distressed Jeans", "AllSaints", "Black", ["edgy", "modern"], ["casual", "party"], "all"),
        ("Japanese Denim", "Uniqlo", "Dark Blue", ["quality", "authentic"], ["casual", "weekend"], "all"),
        ("Stretch Jeans", "Bonobos", "Dark Blue", ["comfortable", "flexible"], ["casual", "travel"], "all"),
        ("Vintage Jeans", "Levi's Vintage", "Medium Blue", ["authentic", "classic"], ["casual", "weekend"], "all"),
        ("Jogger Jeans", "Levi's", "Black", ["comfortable", "modern"], ["casual", "travel"], "all"),
        ("Cropped Jeans", "Zara", "Light Blue", ["modern", "summery"], ["casual", "beach"], "summer"),
        
        # Shorts (15)
        ("Navy Chino Shorts", "Bonobos", "Navy", ["classic", "casual"], ["casual", "beach"], "summer"),
        ("Khaki Shorts", "J.Crew", "Khaki", ["versatile", "casual"], ["casual", "beach"], "summer"),
        ("Gray Shorts", "Bonobos", "Gray", ["modern", "casual"], ["casual", "beach"], "summer"),
        ("Olive Shorts", "Gap", "Olive", ["earthy", "casual"], ["casual", "hiking"], "summer"),
        ("White Shorts", "Bonobos", "White", ["fresh", "summery"], ["casual", "beach"], "summer"),
        ("Black Shorts", "Nike", "Black", ["versatile", "athletic"], ["gym", "casual"], "summer"),
        ("Denim Shorts", "Levi's", "Blue", ["casual", "classic"], ["casual", "beach"], "summer"),
        ("Athletic Shorts", "Nike", "Gray", ["sporty", "comfortable"], ["gym", "running"], "summer"),
        ("Basketball Shorts", "Nike", "Black", ["athletic", "loose"], ["gym", "basketball"], "summer"),
        ("Board Shorts", "Patagonia", "Navy", ["water-resistant", "casual"], ["beach", "surf"], "summer"),
        ("Cargo Shorts", "Carhartt", "Khaki", ["utilitarian", "casual"], ["casual", "hiking"], "summer"),
        ("Linen Shorts", "Bonobos", "Beige", ["breathable", "summery"], ["casual", "beach"], "summer"),
        ("Running Shorts", "Nike", "Black", ["athletic", "lightweight"], ["running", "gym"], "summer"),
        ("Swim Shorts", "J.Crew", "Navy", ["water-ready", "classic"], ["beach", "pool"], "summer"),
        ("Lounge Shorts", "Uniqlo", "Gray", ["comfortable", "casual"], ["casual", "lounging"], "summer"),
        
        # Active/Lounge (10)
        ("Black Joggers", "Nike", "Black", ["comfortable", "sporty"], ["casual", "gym"], "all"),
        ("Gray Joggers", "Adidas", "Gray", ["athletic", "casual"], ["gym", "casual"], "all"),
        ("Navy Sweatpants", "Champion", "Navy", ["comfortable", "casual"], ["casual", "lounging"], "all"),
        ("Black Sweatpants", "Nike", "Black", ["athletic", "casual"], ["gym", "casual"], "all"),
        ("Track Pants", "Adidas", "Black", ["sporty", "retro"], ["gym", "casual"], "all"),
        ("Fleece Pants", "Patagonia", "Gray", ["warm", "comfortable"], ["casual", "outdoor"], "winter"),
        ("Athletic Tights", "Nike", "Black", ["supportive", "athletic"], ["gym", "running"], "all"),
        ("Lounge Pants", "Uniqlo", "Charcoal", ["comfortable", "relaxed"], ["casual", "lounging"], "all"),
        ("Tech Pants", "Lululemon", "Black", ["modern", "comfortable"], ["casual", "travel"], "all"),
        ("Yoga Pants", "Lululemon", "Navy", ["flexible", "comfortable"], ["yoga", "gym"], "all"),
    ]
    
    for idx, (title, brand, color, style_tags, occasions, season) in enumerate(male_bottoms_data):
        items.append({
            "category": "bottoms",
            "gender": "male",
            "image": male_bottom_images[idx % len(male_bottom_images)],
            "alt": title.lower(),
            "title": title,
            "description": f"{color} {title.lower()} for {occasions[0]}",
            "brand": brand,
            "color": color,
            "style_tags": str(style_tags).replace("'", '"'),
            "occasions": str(occasions).replace("'", '"'),
            "season": season
        })
    
    # Male Shoes (60)
    male_shoes_data = [
        # Dress Shoes (20)
        ("Black Oxford Shoes", "Allen Edmonds", "Black", ["formal", "classic"], ["work", "formal"], "all"),
        ("Brown Oxford Shoes", "Allen Edmonds", "Brown", ["professional", "classic"], ["work", "formal"], "all"),
        ("Black Derby Shoes", "Cole Haan", "Black", ["formal", "versatile"], ["work", "formal"], "all"),
        ("Brown Derby Shoes", "Clarks", "Brown", ["classic", "comfortable"], ["work", "casual"], "all"),
        ("Black Loafers", "Gucci", "Black", ["sophisticated", "versatile"], ["work", "casual"], "all"),
        ("Brown Loafers", "Tod's", "Brown", ["classic", "elegant"], ["work", "casual"], "all"),
        ("Penny Loafers", "G.H.Bass", "Burgundy", ["preppy", "classic"], ["casual", "work"], "all"),
        ("Tassel Loafers", "Cole Haan", "Brown", ["sophisticated", "formal"], ["work", "dinner"], "all"),
        ("Black Monk Straps", "Allen Edmonds", "Black", ["formal", "distinctive"], ["work", "formal"], "all"),
        ("Brown Brogues", "Allen Edmonds", "Brown", ["detailed", "classic"], ["work", "casual"], "all"),
        ("Suede Loafers", "Tod's", "Tan", ["casual", "elegant"], ["casual", "work"], "all"),
        ("Patent Leather Shoes", "Hugo Boss", "Black", ["formal", "glossy"], ["formal", "black tie"], "all"),
        ("Wingtip Shoes", "Allen Edmonds", "Brown", ["classic", "detailed"], ["work", "formal"], "all"),
        ("Cap-Toe Oxfords", "Johnston & Murphy", "Black", ["formal", "elegant"], ["work", "formal"], "all"),
        ("Burgundy Oxfords", "Allen Edmonds", "Burgundy", ["rich", "sophisticated"], ["work", "formal"], "all"),
        ("Tan Brogues", "Clarks", "Tan", ["casual", "detailed"], ["casual", "work"], "all"),
        ("Black Slip-Ons", "Cole Haan", "Black", ["convenient", "formal"], ["work", "travel"], "all"),
        ("Brown Slip-Ons", "Clarks", "Brown", ["comfortable", "casual"], ["casual", "travel"], "all"),
        ("Velvet Loafers", "Gucci", "Black", ["luxurious", "formal"], ["formal", "party"], "all"),
        ("Suede Oxfords", "Cole Haan", "Navy", ["sophisticated", "textured"], ["work", "casual"], "all"),
        
        # Boots (20)
        ("Chelsea Boots", "Blundstone", "Brown", ["versatile", "classic"], ["casual", "work"], "all"),
        ("Black Chelsea Boots", "Dr. Martens", "Black", ["edgy", "durable"], ["casual", "work"], "all"),
        ("Chukka Boots", "Clarks Desert Boot", "Tan", ["casual", "classic"], ["casual", "weekend"], "all"),
        ("Work Boots", "Timberland", "Tan", ["rugged", "durable"], ["work", "outdoor"], "all"),
        ("Combat Boots", "Dr. Martens", "Black", ["edgy", "durable"], ["casual", "winter"], "fall"),
        ("Brown Leather Boots", "Frye", "Brown", ["classic", "rugged"], ["casual", "work"], "all"),
        ("Black Leather Boots", "Red Wing", "Black", ["durable", "classic"], ["work", "casual"], "all"),
        ("Hiking Boots", "Merrell", "Brown", ["outdoor", "supportive"], ["hiking", "outdoor"], "all"),
        ("Snow Boots", "Sorel", "Black", ["warm", "waterproof"], ["casual", "winter"], "winter"),
        ("Western Boots", "Ariat", "Brown", ["cowboy", "distinctive"], ["casual", "country"], "all"),
        ("Moc Toe Boots", "Red Wing", "Brown", ["rugged", "classic"], ["casual", "work"], "all"),
        ("Dress Boots", "Allen Edmonds", "Black", ["formal", "polished"], ["work", "formal"], "all"),
        ("Suede Chelsea Boots", "Common Projects", "Tan", ["elegant", "modern"], ["casual", "dinner"], "fall"),
        ("Desert Boots", "Clarks", "Sand", ["casual", "classic"], ["casual", "weekend"], "all"),
        ("Engineer Boots", "Frye", "Black", ["rugged", "motorcycle"], ["casual", "edgy"], "all"),
        ("Brogue Boots", "Allen Edmonds", "Brown", ["detailed", "sophisticated"], ["work", "casual"], "fall"),
        ("Cap-Toe Boots", "Thursday Boot Company", "Brown", ["classic", "versatile"], ["casual", "work"], "all"),
        ("Zip Boots", "John Varvatos", "Black", ["convenient", "modern"], ["casual", "work"], "all"),
        ("Duck Boots", "L.L.Bean", "Brown/Tan", ["weather-resistant", "casual"], ["outdoor", "winter"], "winter"),
        ("Lace-Up Boots", "Timberland", "Brown", ["durable", "classic"], ["casual", "outdoor"], "all"),
        
        # Sneakers (15)
        ("White Leather Sneakers", "Common Projects", "White", ["minimalist", "clean"], ["casual", "travel"], "all"),
        ("Black Sneakers", "Nike Air Force 1", "Black", ["classic", "versatile"], ["casual", "gym"], "all"),
        ("White Canvas Sneakers", "Converse Chuck Taylor", "White", ["classic", "casual"], ["casual", "weekend"], "all"),
        ("Black Canvas Sneakers", "Vans Old Skool", "Black", ["skate", "casual"], ["casual", "weekend"], "all"),
        ("Gray Running Shoes", "Nike", "Gray", ["athletic", "comfortable"], ["gym", "running"], "all"),
        ("Navy Sneakers", "New Balance 574", "Navy", ["retro", "comfortable"], ["casual", "gym"], "all"),
        ("Beige Sneakers", "Veja", "Beige", ["sustainable", "casual"], ["casual", "travel"], "all"),
        ("High-Top Sneakers", "Converse", "Black", ["classic", "casual"], ["casual", "weekend"], "all"),
        ("Slip-On Sneakers", "Vans", "Black", ["convenient", "casual"], ["casual", "travel"], "all"),
        ("Retro Sneakers", "Adidas Superstar", "White", ["classic", "iconic"], ["casual", "weekend"], "all"),
        ("Running Shoes", "Nike", "Multi", ["athletic", "supportive"], ["running", "gym"], "all"),
        ("Basketball Shoes", "Nike", "Black", ["athletic", "supportive"], ["basketball", "gym"], "all"),
        ("Skateboard Shoes", "Vans", "Gray", ["durable", "casual"], ["casual", "skating"], "all"),
        ("Minimalist Sneakers", "Allbirds", "Gray", ["comfortable", "eco-friendly"], ["casual", "travel"], "all"),
        ("Chunky Sneakers", "Balenciaga", "White", ["bold", "trendy"], ["casual", "party"], "all"),
        
        # Sandals & Casual (5)
        ("Leather Sandals", "Birkenstock", "Brown", ["comfortable", "casual"], ["casual", "beach"], "summer"),
        ("Slide Sandals", "Adidas", "Black", ["convenient", "casual"], ["casual", "pool"], "summer"),
        ("Flip Flops", "Havaianas", "Black", ["casual", "beach"], ["beach", "pool"], "summer"),
        ("Sport Sandals", "Teva", "Black", ["outdoor", "comfortable"], ["hiking", "beach"], "summer"),
        ("Boat Shoes", "Sperry", "Brown", ["nautical", "casual"], ["casual", "beach"], "summer"),
    ]
    
    for idx, (title, brand, color, style_tags, occasions, season) in enumerate(male_shoes_data):
        items.append({
            "category": "shoes",
            "gender": "male",
            "image": male_shoes_images[idx % len(male_shoes_images)],
            "alt": title.lower(),
            "title": title,
            "description": f"{color} {title.lower()} for {occasions[0]}",
            "brand": brand,
            "color": color,
            "style_tags": str(style_tags).replace("'", '"'),
            "occasions": str(occasions).replace("'", '"'),
            "season": season
        })
    
    # Male Accessories (40)
    male_accessories_data = [
        # Bags (15)
        ("Black Leather Briefcase", "Tumi", "Black", ["professional", "spacious"], ["work", "business"], "all"),
        ("Brown Leather Briefcase", "Fossil", "Brown", ["classic", "professional"], ["work", "business"], "all"),
        ("Black Backpack", "Tumi", "Black", ["professional", "versatile"], ["work", "travel"], "all"),
        ("Gray Backpack", "Herschel", "Gray", ["casual", "spacious"], ["casual", "travel"], "all"),
        ("Messenger Bag", "Fossil", "Brown", ["casual", "convenient"], ["work", "casual"], "all"),
        ("Canvas Messenger Bag", "Filson", "Tan", ["rugged", "casual"], ["casual", "work"], "all"),
        ("Laptop Bag", "Incase", "Black", ["protective", "professional"], ["work", "travel"], "all"),
        ("Duffle Bag", "Herschel", "Navy", ["spacious", "travel"], ["travel", "gym"], "all"),
        ("Gym Bag", "Nike", "Black", ["sporty", "practical"], ["gym", "sports"], "all"),
        ("Weekender Bag", "Everlane", "Black", ["spacious", "travel"], ["travel", "weekend"], "all"),
        ("Crossbody Bag", "Coach", "Black", ["convenient", "casual"], ["casual", "travel"], "all"),
        ("Belt Bag", "Herschel", "Black", ["convenient", "hands-free"], ["casual", "travel"], "all"),
        ("Tote Bag", "Baggu", "Canvas", ["casual", "eco-friendly"], ["casual", "shopping"], "all"),
        ("Camera Bag", "Peak Design", "Black", ["protective", "organized"], ["photography", "travel"], "all"),
        ("Tech Organizer", "Bellroy", "Black", ["organized", "compact"], ["travel", "work"], "all"),
        
        # Watches & Jewelry (10)
        ("Stainless Steel Watch", "Seiko", "Silver", ["classic", "elegant"], ["work", "formal"], "all"),
        ("Leather Watch", "Timex", "Brown/Gold", ["classic", "casual"], ["casual", "work"], "all"),
        ("Dive Watch", "Seiko", "Black", ["sporty", "durable"], ["casual", "diving"], "all"),
        ("Chronograph Watch", "Tissot", "Silver", ["sophisticated", "functional"], ["work", "formal"], "all"),
        ("Smart Watch", "Apple Watch", "Black", ["tech", "versatile"], ["casual", "gym"], "all"),
        ("Minimalist Watch", "Daniel Wellington", "Silver", ["sleek", "modern"], ["casual", "work"], "all"),
        ("Gold Watch", "Citizen", "Gold", ["luxurious", "formal"], ["formal", "work"], "all"),
        ("Leather Bracelet", "Fossil", "Brown", ["casual", "rugged"], ["casual", "weekend"], "all"),
        ("Beaded Bracelet", "Miansai", "Multi", ["casual", "bohemian"], ["casual", "weekend"], "all"),
        ("Cufflinks", "Tateossian", "Silver", ["formal", "elegant"], ["formal", "business"], "all"),
        
        # Belts & Other (15)
        ("Black Leather Belt", "Cole Haan", "Black", ["classic", "formal"], ["work", "formal"], "all"),
        ("Brown Leather Belt", "Allen Edmonds", "Brown", ["classic", "versatile"], ["casual", "work"], "all"),
        ("Reversible Belt", "Coach", "Black/Brown", ["versatile", "convenient"], ["work", "casual"], "all"),
        ("Woven Belt", "J.Crew", "Tan", ["casual", "textured"], ["casual", "weekend"], "summer"),
        ("Canvas Belt", "Gap", "Khaki", ["casual", "durable"], ["casual", "outdoor"], "all"),
        ("Designer Belt", "Gucci", "Black", ["luxurious", "statement"], ["casual", "party"], "all"),
        ("Aviator Sunglasses", "Ray-Ban", "Gold/Brown", ["classic", "cool"], ["casual", "driving"], "summer"),
        ("Wayfarer Sunglasses", "Ray-Ban", "Black", ["iconic", "versatile"], ["casual", "beach"], "summer"),
        ("Sport Sunglasses", "Oakley", "Black", ["athletic", "protective"], ["sports", "outdoor"], "summer"),
        ("Polarized Sunglasses", "Maui Jim", "Tortoise", ["premium", "protective"], ["casual", "beach"], "summer"),
        ("Wool Scarf", "J.Crew", "Gray", ["warm", "classic"], ["casual", "winter"], "winter"),
        ("Cashmere Scarf", "Burberry", "Camel", ["luxurious", "warm"], ["work", "winter"], "winter"),
        ("Beanie", "Carhartt", "Black", ["warm", "casual"], ["casual", "winter"], "winter"),
        ("Baseball Cap", "Nike", "Black", ["sporty", "casual"], ["casual", "sports"], "all"),
        ("Leather Gloves", "Hestra", "Black", ["warm", "elegant"], ["formal", "winter"], "winter"),
    ]
    
    for idx, (title, brand, color, style_tags, occasions, season) in enumerate(male_accessories_data):
        items.append({
            "category": "accessories",
            "gender": "male",
            "image": male_accessory_images[idx % len(male_accessory_images)],
            "alt": title.lower(),
            "title": title,
            "description": f"{color} {title.lower()} to complete your outfit",
            "brand": brand,
            "color": color,
            "style_tags": str(style_tags).replace("'", '"'),
            "occasions": str(occasions).replace("'", '"'),
            "season": season
        })
    
    return items

FASHION_ITEMS = generate_fashion_dataset()

