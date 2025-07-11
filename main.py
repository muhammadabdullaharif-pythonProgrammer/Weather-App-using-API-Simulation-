import pandas as pd
import numpy as np

class WeatherApp:
    def __init__(self):
        # Simulating a weather database
        self.weather_data = pd.DataFrame({
            "city": ["New York", "London", "Tokyo", "Sydney"],
            "temperature": [72, 60, 75, 85],
            "humidity": [65, 70, 60, 55],
            "conditions": ["Sunny", "Cloudy", "Rainy", "Sunny"]
        })
    
    def get_weather(self, city):
        city_data = self.weather_data[self.weather_data["city"].str.lower() == city.lower()]
        if not city_data.empty:
            return city_data.iloc[0].to_dict()
        return None

# Example usage
app = WeatherApp()
print(app.get_weather("London"))
