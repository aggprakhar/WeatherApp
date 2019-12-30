from django.shortcuts import render
import requests
import json
from pyowm import OWM
from pyowm.tiles.enums import MapLayerEnum
from django.http import HttpResponseRedirect
from .forms import CityForm
from .models import City, WeatherData, Post
import datetime




API_key = '1b8c2e3db4fdf2f2d2655492e3f4fed7'

owm = OWM(API_key)

def weather_data(request):
    if request.method == 'POST':

        #form = CityForm(request.POST)
        city_name = request.POST['city_name']
        observation = owm.weather_at_place(city_name)
        #Post.objects.all()
        mapbox_access_token = 'pk.eyJ1IjoicHJha2hhcjEzIiwiYSI6ImNrNHJ3ODdxZjEzaHkzbWwxM3h2MGozcnIifQ.3ByFVejM5A80LHcUFZwliA'
        try:

            from pyowm.utils.geo import Point
            from pyowm.commons.tile import Tile
            #city_name = 'London'
            observation = owm.weather_at_place(city_name)
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
            geopoint = Point(lon, lat)
            x_tile, y_tile = Tile.tile_coords_for_point(geopoint, 0)
            tile = tm.get_tile(x_tile, y_tile, 2)
            tile.persist('/Users/prakharaggarwal/Desktop/Courses/weather_api/openweathermap/djangoweather/weatherapp/media/' + city_name + '.png')
            #p = Post(title = city_name, cover=tile)
            #p.save()

        except Exception as e:
            wind = 'Error...'
        return render(request, 'about.html', {'wind' : wind, 'mapbox_access_token' : mapbox_access_token, 'lon' : lon, 'lat' : lat})

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
        WeatherData.objects.all()
        try:
            api = json.loads(api_request.content)
            q = WeatherData(city = request.POST['city'])
            q.save()

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
    from pyowm.utils.geo import Point
    from pyowm.commons.tile import Tile


    city_name = 'London'
    observation = owm.weather_at_place(city_name)
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
    geopoint = Point(lon, lat)
    x_tile, y_tile = Tile.tile_coords_for_point(geopoint, 7)
    tile = tm.get_tile(x_tile, y_tile, 6)
    tile.persist('/Users/prakharaggarwal/Desktop/Courses/weather_api/openweathermap/djangoweather/weatherapp/media/' + city_name + '.png')
    #Post.objects.all()
    #m = Post(title = 'city_name', cover = 'tile')
    #m.save()

    return render('about.html', {'wind' : wind})

def forecast(request):
    if request.method == "POST":
        city = request.POST['city']
        api_request = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=+' + city + '&units=imperial&appid=bbe74166a0b2e5eda72860dbfaed3227')
        #WeatherData.objects.all()
        try:
            api = json.loads(api_request.content)
            #data = api.json()
            fc = owm.three_hours_forecast(city)
            #city_name = api.get(['city']['name'])
            #temperature = api.get(['list'][0]['main']['temp'])
            #description = api.get(['list'][0]['weather'][0]['main'])
            #datetime = api.get(datetime(['list'][0]['dt']))
            rain = str(fc.will_have_rain())
            snow = str(fc.will_have_snow())

            #q = WeatherData(city = city_name,  temperature = temperature,
            #description = description, datetime = datetime)
            #q = WeatherData(city = data['city']['name'],  temperature = data['list'][0]['main']['temp'],
            #description = data['list'][0]['weather'][0]['main'], datetime = api['list'][0]['dt_txt'])
            #q.save()




        except Exception as e:

            api = "Error..."
        return render(request, 'forecast.html', {'api' : api, 'rain' : rain, 'snow' : snow})
    else:


        api_request = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Las Vegas&units=imperial&appid=bbe74166a0b2e5eda72860dbfaed3227')
        try:
            api = json.loads(api_request.content)
            fc = owm.three_hours_forecast('Las Vegas')
            rain = str(fc.will_have_rain())
            snow = str(fc.will_have_snow())

        except Exception as e:

            api = "Error..."
        return render(request, 'forecast.html', {'api' : api, 'rain' : rain, 'snow' : snow})

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
