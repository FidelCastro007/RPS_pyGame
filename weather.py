import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print('\n**** get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name:\n")

    request_Url =f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'

    print(request_Url)
    weather_data = requests.get(request_Url).json()

    #pprint(weather_data) // It prints align vals for end user  

    print(f"\nCurrent weather for {weather_data["name"]}:")
    print(f"\nThe temp is {weather_data["main"]["temp"]:.1f}°")

get_current_weather()
