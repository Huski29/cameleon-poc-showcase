"""
Gemini Avatar Service - Generate personalized avatars using Nano Banana (Gemini Image Generation)
Uses the Gemini 3 Pro Image model for high-quality avatar generation
"""

from typing import Optional
import os
import base64
from io import BytesIO

try:
    from google import genai
    from google.genai import types
    from PIL import Image
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False
    print("Warning: google-genai not installed.")


class GeminiAvatarService:
    def __init__(self):
        if not HAS_GENAI:
            print("Gemini Avatar Service not available - avatar generation will not work")
            self.client = None
            return
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("Warning: GEMINI_API_KEY not set - avatar generation will not work")
            self.client = None
            return
        
        try:
            self.client = genai.Client(api_key=api_key)
            print("Gemini Avatar Service initialized successfully!")
        except Exception as e:
            print(f"Error initializing Gemini client: {e}")
            self.client = None
    
    def generate_avatar(
        self,
        user_image: str,
        gender: str,
        height: str,
        volume: str,
        body_type: str,
        style_preference: str = "Smart Casual"
    ) -> Optional[str]:
        """
        Generate a personalized fashion avatar using Gemini Image Generation.
        Creates a consistent, predictable avatar based on the user's uploaded image
        and their body characteristics.
        
        Args:
            user_image: Base64 encoded image (data URI) of user's photo
            gender: User's gender (male/female)
            height: Height range (e.g., "150-160 cm")
            volume: Body volume/build (e.g., "slim", "average", "curvy")
            body_type: Body type (e.g., "rectangle", "hourglass", "triangle")
            style_preference: Style preference (e.g., "Smart Casual", "Formal")
        
        Returns:
            Base64 encoded data URI of the generated avatar image, or None if failed
        """
        if not self.client:
            print("Gemini client not initialized")
            return None
        
        try:
            # Decode the user image from base64 data URI
            if user_image.startswith('data:image'):
                # Extract base64 data
                base64_data = user_image.split(',')[1]
                image_bytes = base64.b64decode(base64_data)
                user_pil_image = Image.open(BytesIO(image_bytes)).convert('RGB')
            else:
                print("Invalid image format")
                return None
            
            # Build a detailed prompt for avatar transformation
            prompt = self._build_avatar_transformation_prompt(
                gender, height, volume, body_type, style_preference
            )
            
            print(f"Generating avatar from user image with Gemini...")
            print(f"Prompt: {prompt[:200]}...")
            
            # Generate the avatar using Gemini 3 Pro Image Preview (Nano Banana Pro - latest/best)
            # Using image-to-image transformation for consistency
            response = self.client.models.generate_content(
                model="gemini-3-pro-image-preview",
                contents=[prompt, user_pil_image],
                config=types.GenerateContentConfig(
                    response_modalities=['IMAGE'],
                    temperature=0.3,  # Lower temperature for consistency
                )
            )
            
            # Extract the generated image
            for part in response.parts:
                if part.inline_data is not None:
                    # Get the image data directly from inline_data
                    if hasattr(part.inline_data, 'data'):
                        # Image data is already in bytes
                        img_bytes = part.inline_data.data
                    else:
                        # Fall back to as_image() if data attribute doesn't exist
                        image = part.as_image()
                        buffered = BytesIO()
                        image.save(buffered, "PNG")
                        img_bytes = buffered.getvalue()
                    
                    # Convert to base64 data URI
                    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
                    data_uri = f"data:image/png;base64,{img_base64}"
                    
                    print("✓ Avatar generated successfully!")
                    return data_uri
                elif part.text is not None:
                    print(f"Model response text: {part.text}")
            
            print("No image generated in response")
            return None
            
        except Exception as e:
            print(f"Error generating avatar: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def _build_avatar_transformation_prompt(
        self,
        gender: str,
        height: str,
        volume: str,
        body_type: str,
        style_preference: str
    ) -> str:
        """Build a detailed prompt for transforming user photo into avatar."""
        
        # Map body parameters to descriptive terms
        gender_term = "woman" if gender == "female" else "man"
        
        # Height mapping
        height_term = height  # e.g., "150-160 cm"
        height_desc, height_details = self._get_height_description(height)
        
        
        # Build mapping
        build_term, build_details = self._get_build_description(volume)
        
        # Shape mapping
        shape_term, shape_details = self._get_shape_description(body_type)
        
        # Build the exact prompt as specified
        prompt = f"""# Transform the person's face from the provided photo into a full-body hyperrealistic avatar.



## Follow the specifications below:

### Identity:

• Keep the person's facial features, age, appearance, hairstyle, and skin tone exactly consistent with the photo.

• Gender: {gender_term}



### Body:

• Generate a full-body image from head to toe. You must always show the full body in the frame, from the head all the way to the white socks.

• Use the following anthropometric descriptors for body construction:

Height: {height_term}

Height details: {height_details}

Build: {build_term}

Build details: {build_details}

Body shape: {shape_term}

Body shape details: {shape_details}



###Clothing:

• Dress the avatar in neutral fitted clothing that shows body proportions without revealing private areas:

-plain white short-sleeved tshirt, slightly fitted

-plain white trousers, straight or slightly tapered fit

-short white socks



Style:

• Hyperrealistic rendering

• Background pure white or soft white gradient



Output:

• Full body avatar, from head to toe in frame.

• Accurate representation of the selected height, build, and body shape!"""
        
        return prompt
    
    def _get_height_description(self, height: str) -> tuple[str, str]:
        """Convert height range to descriptive term and details."""
        try:
            # Extract the starting number from range like "150-160 cm"
            height_start = int(height.split('-')[0].strip())
            
            if height_start < 155:
                return ("petite", "Shorter than average, shorter leg length, lower vertical reach, compact proportions")
            elif height_start < 175:
                return ("regular", "Average height, balanced upper to lower body ratio, standard shoulder to hip vertical proportions")
            else:
                return ("tall", "Taller than average, elongated torso, extended vertical proportions")
        except:
            return ("regular", "Average height, balanced upper to lower body ratio, standard shoulder to hip vertical proportions")
    
    def _get_build_description(self, volume: str) -> tuple[str, str]:
        """Convert volume to build term and details."""
        build_map = {
            "slim": ("lean", "Low body fat, narrow waist, no pronounced roundness in torso, slim limbs"),
            "average": ("mid", "Moderate body fat, average muscle visibility, slight roundness in torso, naturally filled frame, standard limb thickness"),
            "athletic": ("mid", "Moderate body fat, average muscle visibility, slight roundness in torso, naturally filled frame, standard limb thickness"),
            "curvy": ("mid", "Moderate body fat, average muscle visibility, slight roundness in torso, naturally filled frame, standard limb thickness"),
            "plus": ("plus", "High body fat, wider torso, thicker limbs, fuller chest and midsection, soft and rounded abdomen, broad overall frame, noticeable volume in arms and legs, plus size proportions"),
        }
        return build_map.get(volume.lower(), ("mid", "Moderate body fat, average muscle visibility, slight roundness in torso, naturally filled frame, standard limb thickness"))
    
    def _get_shape_description(self, body_type: str) -> tuple[str, str]:
        """Convert body type to shape term and details."""
        shape_map = {
            "inverted triangle": ("inverted triangle", "Very broad shoulders, wide upper chest, tapering down to a narrower waist and hips, V shaped silhouette"),
            "triangle": ("triangle", "Narrow shoulders, wider hips, softer lower body volume"),
            "rectangle": ("rectangle", "Shoulders, waist, and hips aligned in similar width, straight silhouette, minimal tapering"),
            "round": ("round", "Full torso with pronounced midsection, softened shoulders, round silhouette"),
            "trapezium": ("trapezium", "Broad shoulders, moderately narrow waist, balanced hips, athletic silhouette with gentle taper"),
            "hourglass": ("trapezium", "Broad shoulders, moderately narrow waist, balanced hips, athletic silhouette with gentle taper"),  # Map hourglass to trapezium
            "oval": ("round", "Full torso with pronounced midsection, softened shoulders, round silhouette"),  # Map oval to round
        }
        return shape_map.get(body_type.lower(), ("neutral", "Balanced and neutral silhouette with no strong tapering, average proportions"))


# Singleton instance
gemini_avatar_service = GeminiAvatarService()

