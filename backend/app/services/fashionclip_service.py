from typing import List, Optional
import requests
from io import BytesIO
import base64
import re

try:
    from PIL import Image
    import torch
    import numpy as np
    import open_clip
    HAS_FASHION_CLIP = True
except ImportError:
    HAS_FASHION_CLIP = False
    print("Warning: fashion-clip dependencies not installed.")

class FashionCLIPService:
    def __init__(self):
        if not HAS_FASHION_CLIP:
            print("Marqo-FashionCLIP not available - embeddings will not be generated")
            self.model = None
            self.processor = None
            self.device = "cpu"
            return
            
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Initializing Marqo-FashionCLIP on {self.device}...")
        try:
            # Load using OpenCLIP's API (recommended approach for Marqo-FashionCLIP)
            self.model, self.preprocess_train, self.preprocess_val = open_clip.create_model_and_transforms(
                'hf-hub:Marqo/marqo-fashionCLIP'
            )
            self.tokenizer = open_clip.get_tokenizer('hf-hub:Marqo/marqo-fashionCLIP')
            
            # Move to device
            self.model = self.model.to(self.device)
            self.model.eval()
            print(f"Marqo-FashionCLIP loaded successfully on {self.device}!")
        except Exception as e:
            print(f"Error loading Marqo-FashionCLIP: {e}")
            self.model = None
            self.tokenizer = None
            self.preprocess_val = None
    
    def generate_image_embedding(self, image_source: str) -> Optional[List[float]]:
        """
        Generate image embedding from either a URL or base64 encoded image.
        
        Args:
            image_source: Either a URL (http://...) or base64 data URI (data:image/...)
        """
        if not self.model or not self.preprocess_val:
            return None
            
        try:
            # Check if it's a base64 data URI
            if image_source.startswith('data:image'):
                # Extract base64 data from data URI
                base64_match = re.search(r'base64,(.+)', image_source)
                if base64_match:
                    base64_data = base64_match.group(1)
                    image_bytes = base64.b64decode(base64_data)
                    image = Image.open(BytesIO(image_bytes)).convert('RGB')
                else:
                    raise ValueError("Invalid base64 data URI")
            else:
                # It's a regular URL
                response = requests.get(image_source, timeout=10)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content)).convert('RGB')
            
            # Preprocess and generate embedding using OpenCLIP API
            image_input = self.preprocess_val(image).unsqueeze(0).to(self.device)
            
            with torch.no_grad(), torch.amp.autocast(device_type=self.device, enabled=(self.device == "cuda")):
                image_features = self.model.encode_image(image_input, normalize=True)
            
            # Convert to list
            embedding_list = image_features[0].cpu().numpy().tolist()
            
            return embedding_list
        except Exception as e:
            print(f"Error generating image embedding for {image_source[:100]}...: {e}")
            return None
    
    def generate_text_embedding(self, text: str) -> Optional[List[float]]:
        if not self.model or not self.tokenizer:
            return None
            
        try:
            # Tokenize and generate embedding using OpenCLIP API
            text_input = self.tokenizer([text]).to(self.device)
            
            with torch.no_grad(), torch.amp.autocast(device_type=self.device, enabled=(self.device == "cuda")):
                text_features = self.model.encode_text(text_input, normalize=True)
            
            # Convert to list
            embedding_list = text_features[0].cpu().numpy().tolist()
            
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

