import requests
import json

API_KEY = "h682M1TtACh5yUFgarcjpY16ExxNF8wVRDj9vXVi"
WEATHER_URL = "https://api.nasa.gov/insight_weather/?api_key=" + API_KEY +"&feedtype=json&ver=1.0&sol=474"

def parse_url():
    r = requests.get(WEATHER_URL)
    weather_json = r.content
    weather = json.loads(weather_json)
    return weather

