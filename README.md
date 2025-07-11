🌤️ Weather App (using API Simulation)
Tech Stack: Python, Pandas, NumPy
Type: Console-based Simulation

📌 Description
This project simulates a basic Weather App using Python, mimicking an API-based data retrieval system. Instead of using real-time API calls, the application utilizes a Pandas DataFrame as a mock database to represent weather data for multiple cities. This is a lightweight and educational way to demonstrate how APIs work in weather-based applications.

🔧 Features
Simulated weather database for cities like New York, London, Tokyo, and Sydney

Fetches weather details such as:

🌡️ Temperature

💧 Humidity

☁️ Weather Conditions (e.g., Sunny, Cloudy, Rainy)

Case-insensitive city search using string matching

Returns None if the city is not found (graceful error handling)

💡 Learning Objectives
Working with Pandas DataFrames to store and query tabular data

Implementing a simulated API-like behavior in Python

Practicing object-oriented programming (OOP)

Handling string operations and conditional logic in Python

🧪 Sample Output
python
Copy
Edit
{'city': 'London', 'temperature': 60, 'humidity': 70, 'conditions': 'Cloudy'}
🔄 Future Improvements
Integrate a real-time weather API (e.g., OpenWeatherMap)

Build a GUI or web-based interface using Flask or Tkinter

Add support for temperature units (Celsius/Fahrenheit toggle)
