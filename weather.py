'''
import pyowm

weatherapi = ''
owm = pyowm.OWM('')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Hong Kong, China')
w = observation.weather

print(w.status, w.wind(), "Humidity: " ,w.humidity)
'''

from pprint import pprint
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=bbc9f3a2990cde52e2a63cfb204e5967')
pprint(r.json())