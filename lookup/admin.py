from django.contrib import admin

# Register your models here.
from .models import City, WeatherData


admin.site.register(City)
admin.site.register(WeatherData)
