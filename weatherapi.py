# This program uses api key of openweathermap.org so you need to get a key before using this program.
import requests

# import api key from another file
def get_api_key():
    try:
        with open('OpenWeatherApiKey.txt', 'r') as file:
            api_key = file.read().strip()
            return api_key
    except FileNotFoundError:
        print("API key file not found.")
        return None

API_KEY = get_api_key()

def get_weather(city):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        return f"Weather in {city}: {weather_description}, Temperature: {temperature_celsius:.2f}°C"
    else:
        return "Error fetching weather data."

while True:
        # Use q to exit the loop whenever you want
        city_name = input("Enter a city name: ")
        if city_name == "q":
            break
        weather_info = get_weather(city_name)
        print(weather_info)
