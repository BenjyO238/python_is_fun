from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

api_key = os.getenv('WEATHER_API_KEY')
app.logger.debug(f'API Key Loaded: {api_key}')


def get_weather_data(city, state, api_key):
    location = f"{city},{state},US" if state else city
    current_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=imperial'

    app.logger.debug(f'Current Weather API URL: {current_url}')
    app.logger.debug(f'Forecast Weather API URL: {forecast_url}')

    current_response = requests.get(current_url)
    forecast_response = requests.get(forecast_url)

    app.logger.debug(
        f'Current Weather API Response: {current_response.status_code}')
    app.logger.debug(
        f'Forecast Weather API Response: {forecast_response.status_code}')

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
        for entry in forecast_data[
                'list'][:
                        3]:  # Get forecast for the next 3 intervals (3-hour intervals)
            forecast_weather.append({
                'datetime':
                entry['dt_txt'],
                'temperature':
                entry['main']['temp'],
                'description':
                entry['weather'][0]['description'],
                'icon':
                entry['weather'][0]['icon']
            })

        app.logger.debug(f'Current Weather Data: {current_weather}')
        app.logger.debug(f'Forecast Weather Data: {forecast_weather}')

        return current_weather, forecast_weather
    else:
        app.logger.error(
            f'Error fetching weather data: {current_response.status_code}, {forecast_response.status_code}'
        )
        return None, None


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = []
    if request.method == 'POST':
        app.logger.debug(
            f'Received POST request with form data: {request.form}')
        cities = [(request.form[f'city{i}'], request.form[f'state{i}'])
                  for i in range(1, 6) if request.form[f'city{i}']]
        app.logger.debug(f'Parsed cities from form data: {cities}')
        for city, state in cities:
            current_weather, forecast_weather = get_weather_data(
                city, state, api_key)
            if current_weather:
                weather_data.append({
                    'current': current_weather,
                    'forecast': forecast_weather
                })
    app.logger.debug(f'Rendering template with weather data: {weather_data}')
    return render_template('index.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
