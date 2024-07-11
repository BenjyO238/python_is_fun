import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('WEATHER_API_KEY')
city = "San Francisco"
state = "CA"
location = f"{city},{state},US" if state else city
current_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'

response = requests.get(current_url)
print(response.json())
