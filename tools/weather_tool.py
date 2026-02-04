import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    key = os.getenv("WEATHER_API_KEY")

    if not key:
        return {
            "error": "WEATHER_API_KEY missing"
        }

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    data = requests.get(url).json()

    if "main" not in data:
        return {
            "error": "Weather API failed",
            "response": data
        }

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }
