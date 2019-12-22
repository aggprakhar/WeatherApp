from pyowm import OWM
from . import views
from django.shortcuts import render


API_key = '1b8c2e3db4fdf2f2d2655492e3f4fed7'

own = OWM(API_key)

def weather_data(request):


    observation = owm.weather_at_place('London')
    w = observation.get_weather()
    return render(request, 'home.html', {'w' : w})
