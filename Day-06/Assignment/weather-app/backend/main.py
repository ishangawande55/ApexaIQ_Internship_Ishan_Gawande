from fastapi import FastAPI, HTTPException, Query
import os
import requests
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Weather API is running!"}

@app.get("/weather")
def get_weather(lat: float = Query(...), lon: float = Query(...)):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    # Check if API key is missing
    if not api_key:
        raise HTTPException(status_code=400, detail="Missing API Key")

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch weather data")

    data = response.json()

    # Extract relevant fields
    formatted_response = {
        "location": data.get("name", "Unknown"),
        "country": data["sys"]["country"],
        "temperature": {
            "current": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "min": data["main"]["temp_min"],
            "max": data["main"]["temp_max"]
        },
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind": {
            "speed": data["wind"]["speed"],
            "gust": data["wind"].get("gust", "N/A"),
            "direction": data["wind"]["deg"]
        },
        "cloudiness": f"{data['clouds']['all']}%",
        "visibility": f"{data['visibility'] / 1000} km",
        "weather": {
            "main": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
        }
    }

    return formatted_response