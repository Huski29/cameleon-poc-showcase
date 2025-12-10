import os
import base64
from io import BytesIO
from PIL import Image
from typing import Dict, Optional, List
from google import genai
from google.genai import types

class GeminiTryOnService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("Warning: GEMINI_API_KEY not set. Gemini Try-On Service will not be available.")
            self.client = None
        else:
            try:
                self.client = genai.Client(api_key=api_key)
                print("Gemini Try-On Service initialized successfully!")
            except Exception as e:
                print(f"Error initializing Gemini Try-On Service: {e}")
                self.client = None

    def generate_tryon(
        self,
        avatar_image: str,  # Base64 encoded avatar
        outfit_items: List[Dict],  # List of outfit items with images
        user_body_info: Dict,  # User's body measurements
        user_uploaded_image: Optional[str] = None  # Original user photo for consistency
    ) -> Optional[str]:
        """
        Generate a realistic try-on image showing the avatar wearing the outfit items.
        
        Args:
            avatar_image: Base64 encoded user avatar
            outfit_items: List of dicts with 'type', 'name', 'image' (base64), 'brand'
            user_body_info: Dict with 'height', 'volume', 'body_type', 'gender'
            user_uploaded_image: Optional original user photo for better facial/body consistency
        
        Returns:
            Base64 encoded try-on image or None if generation fails
        """
        if not self.client:
            print("Gemini Try-On Service not available.")
            return None

        try:
            # Decode the avatar image
            if avatar_image.startswith('data:image'):
                avatar_data = avatar_image.split(',')[1]
            else:
                avatar_data = avatar_image
            
            avatar_img = Image.open(BytesIO(base64.b64decode(avatar_data))).convert('RGB')

            # Decode the user's original uploaded photo if available
            user_photo_img = None
            if user_uploaded_image:
                user_photo_data = user_uploaded_image
                if user_photo_data.startswith('data:image'):
                    user_photo_data = user_photo_data.split(',')[1]
                user_photo_img = Image.open(BytesIO(base64.b64decode(user_photo_data))).convert('RGB')
            
            # Decode outfit item images
            outfit_images = []
            outfit_descriptions = []
            
            for item in outfit_items:
                # Decode item image
                item_image_data = item['image']
                if item_image_data.startswith('data:image'):
                    item_image_data = item_image_data.split(',')[1]
                
                item_img = Image.open(BytesIO(base64.b64decode(item_image_data))).convert('RGB')
                outfit_images.append(item_img)
                
                # Create DETAILED description for this item
                desc = f"{item['type']}: {item['name']}"
                if item.get('brand'):
                    desc += f" by {item['brand']}"
                outfit_descriptions.append(desc)

            # Use the exact prompt as specified
            prompt_text = """Dress the subject in the first image, only using the following attached clothing items images.

- Make it look stylish.

- White plain background."""
            
            print("Generating virtual try-on with Gemini...")
            print(f"References: Avatar + {len(outfit_images)} outfit items" + (" + original photo" if user_photo_img else ""))
            
            # Combine all reference images: avatar, original photo (if available), and outfit items
            all_images = [avatar_img]
            if user_photo_img:
                all_images.append(user_photo_img)
            all_images.extend(outfit_images)
            
            # Use the image generation model (same as avatar generation)
            response = self.client.models.generate_content(
                model="gemini-3-pro-image-preview",
                contents=[prompt_text] + all_images,
                config=types.GenerateContentConfig(
                    temperature=0.2,  # Very low for consistency
                    max_output_tokens=4096
                )
            )

            if hasattr(response, 'parts') and response.parts:
                for part in response.parts:
                    if hasattr(part, 'inline_data') and part.inline_data:
                        # Get the raw image data directly from inline_data
                        image_data = part.inline_data.data
                        img_str = base64.b64encode(image_data).decode("utf-8")
                        
                        # Determine the mime type
                        mime_type = part.inline_data.mime_type if hasattr(part.inline_data, 'mime_type') else 'image/png'
                        print(f"✓ Virtual try-on generated successfully! (mime: {mime_type})")
                        return f"data:{mime_type};base64,{img_str}"
            
            # Also check candidates structure
            if hasattr(response, 'candidates') and response.candidates:
                print(f"DEBUG: Found {len(response.candidates)} candidates")
                for candidate in response.candidates:
                    if hasattr(candidate, 'content') and candidate.content:
                        if hasattr(candidate.content, 'parts') and candidate.content.parts:
                            for part in candidate.content.parts:
                                if hasattr(part, 'inline_data') and part.inline_data:
                                    # Get the raw image data directly from inline_data
                                    image_data = part.inline_data.data
                                    img_str = base64.b64encode(image_data).decode("utf-8")
                                    
                                    # Determine the mime type
                                    mime_type = part.inline_data.mime_type if hasattr(part.inline_data, 'mime_type') else 'image/png'
                                    print(f"✓ Virtual try-on generated successfully! (mime: {mime_type})")
                                    return f"data:{mime_type};base64,{img_str}"
            
            print("❌ No image part found in Gemini response.")
            return None

        except Exception as e:
            print(f"Error generating virtual try-on: {e}")
            import traceback
            traceback.print_exc()
            return None

gemini_tryon_service = GeminiTryOnService()

