from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Optional
from fastapi.responses import FileResponse

app = FastAPI()

# In-memory storage for simplicity (extendable to Neo4j)
user_memory = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to the One-Day Tour Planning Application!"}

@app.get("/favicon.ico")
def favicon():
    return FileResponse("static/favicon.ico")  # Ensure favicon.ico is in the "static" folder

# Data Models
class UserInput(BaseModel):
    user_id: str
    city: Optional[str] = None
    date: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    interests: Optional[List[str]] = None
    budget: Optional[float] = None
    starting_point: Optional[str] = None

class ItineraryItem(BaseModel):
    stop_name: str
    start_time: str
    end_time: str
    activity: str
    cost: Optional[float] = 0.0
    travel_method: Optional[str] = "walk"
    travel_time: Optional[str] = None

class Itinerary(BaseModel):
    user_id: str
    items: List[ItineraryItem]

# Agents
class MemoryAgent:
    @staticmethod
    def save_preferences(user_id, preferences):
        if user_id not in user_memory:
            user_memory[user_id] = {}
        user_memory[user_id].update(preferences)

    @staticmethod
    def get_preferences(user_id):
        return user_memory.get(user_id, {})

class ItineraryAgent:
    @staticmethod
    def generate(user_input: UserInput):
        city_data = {
            "Berlin": [
                {"stop_name": "Brandenburg Gate", "activity": "Visit iconic landmark", "cost": 0, "travel_time": "15 min", "travel_method": "walk", "interests": ["history", "landmarks"]},
                {"stop_name": "Museum Island", "activity": "Explore museums", "cost": 12, "travel_time": "15 min", "travel_method": "taxi", "interests": ["history", "museums"]}
            ],
            "New York": [
                {"stop_name": "Battery Park", "activity": "View Statue of Liberty", "cost": 0, "travel_time": "20 min", "travel_method": "subway", "interests": ["history", "nature"]},
                {"stop_name": "Central Park", "activity": "Relax and explore nature", "cost": 0, "travel_time": "15 min", "travel_method": "walk", "interests": ["nature", "relaxation"]}
            ]
        }

        # Check if city is supported
        if user_input.city not in city_data:
            return {"error": f"City '{user_input.city}' is not supported yet. Please try another city."}

        # Get stops for the city
        stops = city_data[user_input.city]

        # Filter stops based on user interests
        filtered_stops = [
            stop for stop in stops if any(interest in stop["interests"] for interest in user_input.interests)
        ]

        # Filter stops based on user budget
        budget_remaining = user_input.budget
        final_itinerary = []
        for stop in filtered_stops:
            if stop["cost"] <= budget_remaining:
                final_itinerary.append(stop)
                budget_remaining -= stop["cost"]

        # Return itinerary or an error if no stops match
        if not final_itinerary:
            return {"error": "No stops match your interests or budget. Please adjust your preferences."}

        return final_itinerary

@app.post("/collect_preferences")
def collect_preferences(user_input: UserInput):
    preferences = user_input.dict(exclude_none=True)
    MemoryAgent.save_preferences(user_input.user_id, preferences)
    return {"message": "Preferences saved", "preferences": preferences}

@app.post("/generate_itinerary")
def generate_itinerary(user_input: UserInput):
    preferences = MemoryAgent.get_preferences(user_input.user_id)
    if not preferences:
        return {"error": "No preferences found. Collect preferences first."}
    itinerary = ItineraryAgent.generate(user_input)
    return {"itinerary": itinerary}
