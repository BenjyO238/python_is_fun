from datetime import datetime
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)


def get_weather_data(city, state, api_key):
    location = f"{city},{state},US" if state else city
    current_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=imperial'

    current_response = requests.get(current_url)
    forecast_response = requests.get(forecast_url)

    if current_response.status_code == 200 and forecast_response.status_code == 200:
        current_data = current_response.json()
        forecast_data = forecast_response.json()

        current_weather = {
            'city': current_data['name'],
            'temperature': current_data['main']['temp'],
            'description': current_data['weather'][0]['description'],
            'icon': current_data['weather'][0]['icon']
        }

        forecast_weather = []
        for entry in forecast_data['list'][:5]:  # Get forecast for the next 5 intervals (3-hour intervals)
            forecast_weather.append({
                'datetime': datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S').strftime('%d %H:%M'),
                'temperature': entry['main']['temp'],
                'description': entry['weather'][0]['description'],
                'icon': entry['weather'][0]['icon']
            })

        return current_weather, forecast_weather
    else:
        return None, None


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = []
    if request.method == 'POST':
        cities = [(request.form[f'city{i}'], request.form[f'state{i}']) for i in range(1, 6) if
                  request.form[f'city{i}']]
        api_key = os.getenv('WEATHER_API_KEY')  # Get the API key from environment variable
        for city, state in cities:
            current_weather, forecast_weather = get_weather_data(city, state, api_key)
            if current_weather:
                weather_data.append({
                    'current': current_weather,
                    'forecast': forecast_weather
                })
    return render_template('index.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
