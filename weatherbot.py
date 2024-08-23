'''
from pprint import pprint
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=bbc9f3a2990cde52e2a63cfb204e5967')
pprint(r.json())
'''

from pprint import pprint
import tweepy 
import requests
import time 
import pyowm
from dotenv import load_dotenv
import os

load_dotenv()

weatherapi = os.getenv('weatherapi')
owm = pyowm.OWM('')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Accra, Ghana')
w = observation.weather

auth = os.getenv('auth')
consumer_key= os.getenv('consumer_key')
consumer_secret= os.getenv('consumer_secret')
access_token= os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')
client = tweepy.Client(
    consumer_key= consumer_key,
    consumer_secret= consumer_secret,
    access_token= access_token,
    access_token_secret= access_token_secret
)
api = tweepy.API(auth)

def get_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London&APPID=bbc9f3a2990cde52e2a63cfb204e5967'
    response = requests.get(url)
    data = response.json()
get_weather()