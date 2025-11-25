import os
from openai import OpenAI
from typing import Dict, List, Optional
import json
from dotenv import load_dotenv

load_dotenv()

class GPTService:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("Warning: OPENAI_API_KEY not found in environment")
            self.client = None
        else:
            self.client = OpenAI(api_key=api_key)
    
    def parse_intent(self, user_prompt: str) -> Dict:
        if not self.client:
            return {
                "occasion": "casual",
                "style": "comfortable",
                "formality": "casual",
                "vibe": user_prompt,
                "keywords": []
            }
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a fashion stylist assistant. Parse the user's outfit request and extract key styling information. Respond ONLY with valid JSON."},
                    {"role": "user", "content": f"""Parse this outfit request and extract:
- occasion (e.g., work, casual, date, party, formal)
- style (e.g., minimalist, trendy, classic, bohemian, edgy)
- formality (formal, smart casual, casual, loungewear)
- vibe (a short descriptive phrase)
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
            tops = [{"title": i.title, "color": i.color, "brand": i.brand} for i in grouped_items.get("tops", [])[:10]]
            bottoms = [{"title": i.title, "color": i.color, "brand": i.brand} for i in grouped_items.get("bottoms", [])[:10]]
            shoes = [{"title": i.title, "color": i.color, "brand": i.brand} for i in grouped_items.get("shoes", [])[:10]]
            accessories = [{"title": i.title, "color": i.color, "brand": i.brand} for i in grouped_items.get("accessories", [])[:5]]
            
            prompt = f"""You are an expert fashion stylist. Create a complete outfit from the available items.

User Request: {context.get('prompt', 'Create an outfit')}
Weather: {context.get('weather_condition', 'N/A')}, {context.get('temperature', 'N/A')}°C
User Style: {user_prefs.get('style_preference', 'versatile')}
Color Palette: {user_prefs.get('color_palette', 'neutral')}

Available Items:
Tops: {json.dumps(tops)}
Bottoms: {json.dumps(bottoms)}
Shoes: {json.dumps(shoes)}
Accessories: {json.dumps(accessories)}

Select ONE item from each category to create a cohesive outfit. Return JSON with:
{{
  "selected": {{
    "top": "title of selected top",
    "bottom": "title of selected bottom",
    "shoes": "title of selected shoes",
    "accessory": "title of selected accessory or null"
  }},
  "reasoning": "Brief explanation of outfit choice (2-3 sentences)",
  "style_tips": ["tip 1", "tip 2", "tip 3"],
  "color_harmony": "Description of how colors work together"
}}"""

            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
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

