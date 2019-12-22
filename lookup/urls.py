
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="maps"),
    path('forecast.html', views.forecast, name="forecast")
]
