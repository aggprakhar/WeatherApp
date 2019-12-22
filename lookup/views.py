from django.shortcuts import render
import requests
import json
from pyowm import OWM


API_key = '1b8c2e3db4fdf2f2d2655492e3f4fed7'

owm = OWM(API_key)

def weather_data(request):


    observation = owm.weather_at_place('London')
    w = observation.get_weather()
    l = observation.get_location()
    wind = w.get_wind()
    temperature = w.get_temperature()
    lon = l.get_lon()
    lat = l.get_lat()
    return render(request, 'about.html', {'wind' : wind, 'temperature' : temperature, 'lon': lon, 'lat' : lat})

def input(request):

    if request.method == "POST":
        city = request.POST['city']

    return city


# Create your views here.
def home(request):

    #url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=bbe74166a0b2e5eda72860dbfaed3227'
    #city = 'Las Vegas'
    #response = requests.get(url.format(city)).json()
    #weather = {
    #    'city' : city,
    #    'temperature' : city_weather['main']['temp'],
    #    'description' : city_weather['weather'][0]['description'],
    #    'icon' : city_weather['weather'][0]['icon']
    #}

    if request.method == "POST":
        city = request.POST['city']
        api_request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=+' + city + '&units=imperial&appid=bbe74166a0b2e5eda72860dbfaed3227')
        try:
            api = json.loads(api_request.content)

        except Exception as e:

            api = "Error..."
        return render(request, 'home.html', {'api' : api})
    else:


        api_request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Las Vegas&units=imperial&appid=bbe74166a0b2e5eda72860dbfaed3227')
        try:
            api = json.loads(api_request.content)

        except Exception as e:

            api = "Error..."
        return render(request, 'home.html', {'api' : api})

def about(request):
    return render(request, 'about.html', {})

def forecast(request):
    if request.method == "POST":
        city = request.POST['city']
        api_request = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=+' + city + '&units=imperial&appid=bbe74166a0b2e5eda72860dbfaed3227')
        try:
            api = json.loads(api_request.content)

        except Exception as e:

            api = "Error..."
        return render(request, 'forecast.html', {'api' : api})
    else:


        api_request = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Las Vegas&units=imperial&appid=bbe74166a0b2e5eda72860dbfaed3227')
        try:
            api = json.loads(api_request.content)

        except Exception as e:

            api = "Error..."
        return render(request, 'forecast.html', {'api' : api})


    #return render(request, 'forecast.html', {})
