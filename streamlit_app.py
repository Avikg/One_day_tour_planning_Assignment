import streamlit as st
import requests

st.title("One-Day Tour Planner")

BASE_URL = "http://127.0.0.1:8000"

def get_user_input():
    user_id = st.text_input("Enter User ID", value="user123")
    city = st.text_input("City", value="Berlin")
    date = st.date_input("Date").strftime("%Y-%m-%d")
    start_time = st.text_input("Start Time", value="9:00 AM")
    end_time = st.text_input("End Time", value="6:00 PM")
    interests = st.multiselect("Select Interests", ["history", "museums", "food"])
    budget = st.number_input("Budget", value=100)
    starting_point = st.text_input("Starting Point", value="Hotel Berlin Central")
    return {
        "user_id": user_id,
        "city": city,
        "date": date,
        "start_time": start_time,
        "end_time": end_time,
        "interests": interests,
        "budget": budget,
        "starting_point": starting_point
    }

user_data = get_user_input()

if st.button("Save Preferences"):
    response = requests.post(f"{BASE_URL}/collect_preferences", json=user_data)
    st.json(response.json())

if st.button("Generate Itinerary"):
    response = requests.post(f"{BASE_URL}/generate_itinerary", json=user_data)
    st.json(response.json())
    
if st.button("Optimize Itinerary"):
    response = requests.post(f"{BASE_URL}/generate_itinerary", json=user_data)
    optimized_itinerary = response.json()
    st.json(optimized_itinerary)
