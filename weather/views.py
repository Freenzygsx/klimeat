from django.shortcuts import render
from django.http import HttpResponse
import requests
from decouple import config



def index(request):
    return render(request, 'index.html')

def getWeather(request, city):
    rlatlon = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={config('api_key')}")
    rlatlonjson = rlatlon.json()[0]
    lat = rlatlonjson['lat']
    lon = rlatlonjson['lon']
    rweather = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={config('api_key')}")
    rjweather = rweather.json()
    print(rjweather['list'])

    return HttpResponse(rlatlon)
