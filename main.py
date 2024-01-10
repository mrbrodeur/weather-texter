import datetime as dt
from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env file
load_dotenv()
weather_app_id = os.environ.get("weather_app_id")

params = {
    'lat': 40.744308,
    'lon': -73.941856,
    'appid': weather_app_id,
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast',
                        params=params
                        )

data = response.json()['list'][:4]

will_rain = False
for hour_data in data:

    if hour_data['weather'][0]['main'] in ['Rain', 'Snow']:
        will_rain = True

if will_rain:
    msg = "Wear shoes with no holes today."
    print(msg)
else:
    msg = "No rain in the forecast."


