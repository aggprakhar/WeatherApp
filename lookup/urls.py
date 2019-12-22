
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.weather_data, name="maps"),
    path('forecast.html', views.forecast, name="forecast")
]
