from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'

class WeatherData(models.Model):

    city = models.CharField(max_length=25)
    temperature = models.DecimalField(max_digits = 6, decimal_places=2)
    description = models.CharField(max_length=30)
    datetime = models.DateTimeField('weather date / time', null=True)


    def __str__(self): #show the actual city name on the dashboard
        return self.city

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
