import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_pollution_level(data):
    if data["PM2.5"] > 120 or data["PM10"] > 200:
        return "high"
    elif data["PM2.5"] > 60 or data["PM10"] > 100:
        return "moderate"
    else:
        return "low"

def get_data():
    return {
        "PM2.5": random.randint(20, 200),
        "PM10": random.randint(30, 250),
        "NO2": random.randint(10, 150),
        "temp": random.randint(20, 40),
        "humidity": random.randint(30, 80)
    }

def get_recommendation(city, data):
    level = get_pollution_level(data)

    result = {
        "level": level,
        "plants": [],
        "foods": [],
        "actions": []
    }

    # 🔴 HIGH POLLUTION (Delhi-like)
    if level == "high":
        result["plants"] = [
            "Snake Plant", "Areca Palm", "Spider Plant", "Rubber Plant"
        ]

        result["foods"] = [
            "Apple", "Orange", "Spinach", "Turmeric", "Ginger"
        ]

        result["actions"] = [
            "Avoid outdoor activities",
            "Wear mask outside",
            "Use air-purifying plants",
            "Eat anti-inflammatory foods"
        ]

    # 🟡 MODERATE POLLUTION (Pune-like)
    elif level == "moderate":
        result["plants"] = [
            "Aloe Vera", "Peace Lily", "Anthurium"
        ]

        result["foods"] = [
            "Carrot", "Tomato", "Beetroot", "Papaya"
        ]

        result["actions"] = [
            "Limit long outdoor exposure",
            "Stay hydrated",
            "Maintain indoor plants"
        ]

    # 🟢 LOW POLLUTION
    else:
        result["plants"] = [
            "Tulsi", "Croton"
        ]

        result["foods"] = [
            "Banana", "Mango", "Coconut water"
        ]

        result["actions"] = [
            "Maintain healthy lifestyle",
            "Regular exercise outdoors"
        ]

    return result

@app.get("/air")
def get_air_data(city: str = "delhi"):
    data = get_data()
    recommendation = get_recommendation(city, data)

    return {
        "city": city,
        "data": data,
        "recommendation": recommendation
    }