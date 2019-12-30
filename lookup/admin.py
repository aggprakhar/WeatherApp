from django.contrib import admin

# Register your models here.
from .models import City, WeatherData, Post


admin.site.register(City)
admin.site.register(WeatherData)
admin.site.register(Post)
