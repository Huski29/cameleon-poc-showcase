import os
from openai import OpenAI
from typing import Dict, List, Optional
import json
from dotenv import load_dotenv
from app.services.stylist_profiles import get_stylist_profile

load_dotenv()

class GPTService:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("Warning: OPENAI_API_KEY not found in environment")
            self.client = None
        else:
            self.client = OpenAI(api_key=api_key)
    
    def parse_intent(self, user_prompt: str, style_preference: str = "Smart Casual") -> Dict:
        if not self.client:
            return {
                "occasion": "casual",
                "style": "comfortable",
                "formality": "casual",
                "vibe": user_prompt,
                "keywords": []
            }
        
        try:
            stylist_profile = get_stylist_profile(style_preference)
            
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You are {stylist_profile['name']}, a {stylist_profile['title']}. Parse outfit requests through the lens of your styling philosophy: {stylist_profile['philosophy']}"},
                    {"role": "user", "content": f"""Parse this outfit request and extract:
- occasion (e.g., work, casual, date, party, formal)
- style (e.g., minimalist, trendy, classic, bohemian, edgy)
- formality (formal, smart casual, casual, loungewear)
- vibe (a short descriptive phrase that captures the request)
- keywords (list of relevant fashion terms)

Request: "{user_prompt}"

Respond with JSON only."""}
                ],
                temperature=0.7,
                max_tokens=200
            )
            
            content = response.choices[0].message.content.strip()
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
                content = content.strip()
            
            parsed = json.loads(content)
            return parsed
        except Exception as e:
            print(f"GPT intent parsing failed: {e}")
            return {
                "occasion": "casual",
                "style": "comfortable",
                "formality": "casual",
                "vibe": user_prompt,
                "keywords": []
            }
    
    def generate_outfit(
        self, 
        grouped_items: Dict[str, List], 
        context: Dict,
        user_prefs: Dict
    ) -> Dict:
        if not self.client:
            return self._generate_mock_outfit(grouped_items, context)
        
        try:
            # Get stylist profile based on user's style preference
            style_preference = user_prefs.get('style_preference', 'Smart Casual')
            stylist_profile = get_stylist_profile(style_preference)
            
            # Prepare item lists for GPT
            tops = [{"title": i.title, "color": i.color, "brand": i.brand} for i in grouped_items.get("tops", [])[:10]]
            bottoms = [{"title": i.title, "color": i.color, "brand": i.brand} for i in grouped_items.get("bottoms", [])[:10]]
            shoes = [{"title": i.title, "color": i.color, "brand": i.brand} for i in grouped_items.get("shoes", [])[:10]]
            accessories = [{"title": i.title, "color": i.color, "brand": i.brand} for i in grouped_items.get("accessories", [])[:5]]
            
            # Build the prompt with stylist personality
            user_prompt = f"""
STYLING REQUEST:
User Request: "{context.get('prompt', 'Create an outfit')}"
Weather: {context.get('weather_condition', 'N/A')}, {context.get('temperature', 'N/A')}°C
User's Color Palette Preference: {user_prefs.get('color_palette', 'neutral')}
User's Budget: {user_prefs.get('budget', 'Mid-Range')}

AVAILABLE ITEMS TO CHOOSE FROM:
Tops: {json.dumps(tops, indent=2)}
Bottoms: {json.dumps(bottoms, indent=2)}
Shoes: {json.dumps(shoes, indent=2)}
Accessories: {json.dumps(accessories, indent=2)}

YOUR TASK:
Select ONE item from each category (top, bottom, shoes, and optionally accessory) to create a cohesive outfit that:
1. Aligns with YOUR styling philosophy
2. Addresses the user's request
3. Considers the weather and context
4. Respects the user's color palette preference

Return your response in this EXACT JSON format:
{{
  "selected": {{
    "top": "exact title of selected top from the list",
    "bottom": "exact title of selected bottom from the list",
    "shoes": "exact title of selected shoes from the list",
    "accessory": "exact title of selected accessory or null if not needed"
  }},
  "reasoning": "2-3 sentences explaining why you chose these items together, reflecting YOUR styling philosophy",
  "style_tips": ["tip 1 specific to this outfit", "tip 2 about styling", "tip 3 about wearing this look"],
  "color_harmony": "Brief description of how the colors work together in this outfit"
}}

Remember: Style this outfit as {stylist_profile['name']} would - staying true to the philosophy of {stylist_profile['philosophy']}"""

            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": stylist_profile['system_prompt']},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.8,
                max_tokens=600
            )
            
            content = response.choices[0].message.content.strip()
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
                content = content.strip()
            
            result = json.loads(content)
            return result
        except Exception as e:
            print(f"GPT outfit generation failed: {e}")
            return self._generate_mock_outfit(grouped_items, context)
    
    def _generate_mock_outfit(self, grouped_items: Dict[str, List], context: Dict) -> Dict:
        selected = {}
        
        if grouped_items.get("tops"):
            selected["top"] = grouped_items["tops"][0].title
        if grouped_items.get("bottoms"):
            selected["bottom"] = grouped_items["bottoms"][0].title
        if grouped_items.get("shoes"):
            selected["shoes"] = grouped_items["shoes"][0].title
        if grouped_items.get("accessories"):
            selected["accessory"] = grouped_items["accessories"][0].title if grouped_items["accessories"] else None
        
        return {
            "selected": selected,
            "reasoning": f"This outfit combines comfort and style, perfect for {context.get('prompt', 'your day')}.",
            "style_tips": [
                "Layer accessories for depth",
                "Ensure colors complement each other",
                "Consider the occasion and weather"
            ],
            "color_harmony": "The colors create a balanced, cohesive look."
        }

gpt_service = GPTService()

