import requests
from datetime import datetime
import time

def get_weather(api_key, city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    weather = data['weather'][0]['description']
    return weather

def show_time_and_weather(api_key, city):
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    weather = get_weather(api_key, city)
    print(f'The current time is {current_time}. The weather in {city} is {weather}.')

api_key = '076d7e39d8490b66e8587a958288b3b5'
city = 'Dubai'

while True:
    show_time_and_weather(api_key, city)
    time.sleep(3600) # pause for an hour
