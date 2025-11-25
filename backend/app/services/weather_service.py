import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

class WeatherService:
    def __init__(self):
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.api_url = os.getenv("WEATHER_API_URL", "http://api.weatherapi.com/v1")
        
        if not self.api_key:
            print("Warning: WEATHER_API_KEY not found in environment")
    
    def get_current_weather(self, location: str = "New York") -> Dict:
        if not self.api_key:
            return self._get_mock_weather()
        
        try:
            url = f"{self.api_url}/current.json"
            params = {
                "key": self.api_key,
                "q": location,
                "aqi": "no"
            }
            
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                "temperature": data["current"]["temp_c"],
                "condition": data["current"]["condition"]["text"],
                "feels_like": data["current"]["feelslike_c"],
                "location": data["location"]["name"]
            }
        except Exception as e:
            print(f"Weather API failed: {e}")
            return self._get_mock_weather()
    
    def get_temperature_category(self, temp: float) -> str:
        if temp < 10:
            return "cold"
        elif temp < 20:
            return "mild"
        elif temp < 30:
            return "warm"
        else:
            return "hot"
    
    def _get_mock_weather(self) -> Dict:
        return {
            "temperature": 20,
            "condition": "Partly cloudy",
            "feels_like": 19,
            "location": "Unknown"
        }

weather_service = WeatherService()

