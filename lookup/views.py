from django.shortcuts import render
import requests
import json
from pyowm import OWM
from pyowm.tiles.enums import MapLayerEnum
from django.http import HttpResponseRedirect
from .forms import CityForm
from .models import City



API_key = '1b8c2e3db4fdf2f2d2655492e3f4fed7'

owm = OWM(API_key)

def weather_data(request):
    if request.method == 'POST':

        #form = CityForm(request.POST)
        city_name = request.POST['city_name']
        observation = owm.weather_at_place(city_name)
        try:

            fc = owm.three_hours_forecast(city_name)
            f = fc.get_forecast()
            lst = list(f.get_weathers())
            w = observation.get_weather()
            l = observation.get_location()
            wind = w.get_wind()
            temperature = w.get_temperature()
            lon = l.get_lon()
            lat = l.get_lat()
            layer_name = MapLayerEnum.TEMPERATURE
            tm = owm.tile_manager(layer_name)
            tile = tm.get_tile(lon, lat, 6)
            #tile.persist('/User/prakharaggarwal/Desktop/Courses/weather_api/openweathermap/djangoweather/weatherapp/media/' + city_name + '.png')

        except Exception as e:
            wind = 'Error...'
        return render(request, 'about.html', {'wind' : wind})

    else:
        observation = owm.weather_at_place('Las Vegas')
        try:

            fc = owm.three_hours_forecast('Las Vegas')
            f = fc.get_forecast()
            lst = list(f.get_weathers())
            w = observation.get_weather()
            l = observation.get_location()
            wind = w.get_wind()
            temperature = w.get_temperature()
            lon = l.get_lon()
            lat = l.get_lat()

        except Exception as e:
            wind = 'Error...'
        return render(request, 'about.html', {'wind' : wind})


def input(request):

    if request.method == "POST":
        city = request.POST['city']

    return city


# Create your views here.
def home(request):


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

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=bbe74166a0b2e5eda72860dbfaed3227'
    cities = City.objects.all()

    if request.method =='POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    weather_data = []
    for city in cities:

        city_weather = requests.get(url.format(city)).json()
        weather = {
        'city' : city,
         'temperature' : city_weather['main']['temp'],
         'description' : city_weather['weather'][0]['description'],
         'icon' : city_weather['weather'][0]['icon']
         }

        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'index.html', context)


    #return render(request, 'forecast.html', {})
