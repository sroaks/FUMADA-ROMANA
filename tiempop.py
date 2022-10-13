import datetime as dt
import requests


"""
READ ME:
pip install requests
la API lasque de aqui : https://home.openweathermap.org/

"""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "d1e390c59df437eb10ad140efdb81f5b"
CITY = "London"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()


temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
tiempo = response['weather'][0]['main']
v_viento = response['wind']['speed']

print(tiempo)