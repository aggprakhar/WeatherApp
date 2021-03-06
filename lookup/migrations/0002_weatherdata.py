# Generated by Django 3.0.1 on 2019-12-27 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=25)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
    ]
