
# One-Day Tour Planning Application

## Project Description

The **One-Day Tour Planning Application** is a full-stack application designed to help users plan personalized, optimized one-day itineraries for their travels. 
It takes user preferences such as city, interests, budget, and travel times to generate a tailored itinerary. 
The backend API is built using FastAPI, the frontend UI uses Streamlit, and optional data persistence is supported with Neo4j.

---

## Features

- **User Preferences**: Users can specify city, date, start/end times, interests, budget, and starting location.
- **Custom Itineraries**: Generates a personalized itinerary with stops, timings, activities, and estimated costs.
- **Interactive UI**: Streamlit-based frontend for easy interaction and visualization.
- **API Integration**: Swagger UI for backend API testing and interaction.
- **Optional Database Support**: Uses Neo4j for storing and retrieving user data and itineraries.

---

## How to Run

### Prerequisites
1. **Python 3.8+**: Ensure Python is installed.
2. **Virtual Environment**: Set up and activate a Python virtual environment.
3. **Dependencies**: Install required libraries using the provided `requirements.txt` file.
4. **Neo4j (Optional)**: Set up a Neo4j database for advanced functionality.

### Steps to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Avikg/One_day_tour_planning_Assignment
   cd One_day_tour_planning_Assignment
   ```

2. **Set Up the Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate    # On Windows
   source venv/bin/activate   # On macOS/Linux
   pip install -r requirements.txt
   ```

3. **Run the Backend Server (FastAPI)**:
   ```bash
   python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
   ```
   - Access Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

4. **Run the Frontend (Streamlit)**:
   ```bash
   streamlit run streamlit_app.py
   ```
   - Open the app in your browser at [http://localhost:8501](http://localhost:8501).

---

## API Endpoints

1. **POST /collect_preferences**:
   - Save user preferences.
   - Example Input:
     ```json
     {
       "user_id": "user123",
       "city": "Paris",
       "date": "2024-12-10",
       "start_time": "9:00 AM",
       "end_time": "6:00 PM",
       "interests": ["history", "food"],
       "budget": 150,
       "starting_point": "Hotel du Louvre"
     }
     ```

2. **POST /generate_itinerary**:
   - Generate a one-day itinerary based on saved preferences.
   - Example Output:
     ```json
     [
       {
         "stop_name": "Eiffel Tower",
         "activity": "Visit the Eiffel Tower",
         "cost": 25,
         "travel_time": "15 min",
         "travel_method": "walk"
       },
       {
         "stop_name": "Louvre Museum",
         "activity": "Explore the Louvre Museum",
         "cost": 17,
         "travel_time": "10 min",
         "travel_method": "taxi"
       }
     ]
     ```

---

## Future Enhancements

- **Dynamic Data Fetching**: Integrate third-party APIs for real-time activity recommendations.
- **User Accounts**: Add authentication for multiple users and itinerary history.
