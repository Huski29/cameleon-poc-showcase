from typing import List, Optional
import requests
from io import BytesIO

try:
    from PIL import Image
    import torch
    import numpy as np
    from fashion_clip.fashion_clip import FashionCLIP
    HAS_FASHION_CLIP = True
except ImportError:
    HAS_FASHION_CLIP = False
    print("Warning: fashion-clip dependencies not installed.")

class FashionCLIPService:
    def __init__(self):
        if not HAS_FASHION_CLIP:
            print("FashionCLIP not available - embeddings will not be generated")
            self.fclip = None
            self.device = "cpu"
            return
            
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Initializing FashionCLIP on {self.device}...")
        try:
            self.fclip = FashionCLIP('fashion-clip')
            print("FashionCLIP loaded successfully!")
        except Exception as e:
            print(f"Error loading FashionCLIP: {e}")
            self.fclip = None
    
    def generate_image_embedding(self, image_url: str) -> Optional[List[float]]:
        if not self.fclip:
            return None
            
        try:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content)).convert('RGB')
            
            embedding = self.fclip.encode_images([image], batch_size=1)
            embedding_list = embedding[0].cpu().numpy().tolist()
            
            return embedding_list
        except Exception as e:
            print(f"Error generating image embedding for {image_url}: {e}")
            return None
    
    def generate_text_embedding(self, text: str) -> Optional[List[float]]:
        if not self.fclip:
            return None
            
        try:
            embedding = self.fclip.encode_text([text], batch_size=1)
            embedding_list = embedding[0].cpu().numpy().tolist()
            
            return embedding_list
        except Exception as e:
            print(f"Error generating text embedding: {e}")
            return None
    
    def generate_item_embeddings(self, item_data: dict) -> tuple:
        image_emb = self.generate_image_embedding(item_data["image"])
        
        text_parts = [
            item_data.get('title', ''),
            item_data.get('description', ''),
            item_data.get('color', ''),
            item_data.get('brand', ''),
        ]
        
        if item_data.get('style_tags'):
            if isinstance(item_data['style_tags'], list):
                text_parts.extend(item_data['style_tags'])
            else:
                text_parts.append(str(item_data['style_tags']))
        
        text_desc = ' '.join(filter(None, text_parts))
        text_emb = self.generate_text_embedding(text_desc)
        
        return image_emb, text_emb

fashionclip_service = FashionCLIPService()

