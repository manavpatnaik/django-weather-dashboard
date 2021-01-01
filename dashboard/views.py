from django.shortcuts import render
from django.http import HttpResponse
from requests.api import get
from .forms import CityForm
import requests
from .models import City
from django.conf import settings

def get_weather_data(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': settings.OWM_API_KEY
    }
    response = requests.get(url, params=params)
    json_response = response.json()

    if response.status_code != 200:
        return

    weather_data = {
        'temp': round(json_response['main']['temp'] - 273, 2),
        'temp_min': round(json_response['main']['temp_min'] - 273, 2),
        'temp_max': round(json_response['main']['temp_max'] - 273, 2),
        'city_name': json_response['name'],
        'country_name': json_response['sys']['country'],
        'lat': json_response['coord']['lat'],
        'lon': json_response['coord']['lon'],
        'weather': json_response['weather'][0]['main'],
        'weather_description': json_response['weather'][0]['description'],
        'pressure': json_response['main']['pressure'],
        'humidity': json_response['main']['humidity'],
        'wind_speed': json_response['wind']['speed'],
    }
    return weather_data

def home(request):
    form = CityForm()
    weather_data = {}
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            city_name = form.cleaned_data.get('city_name')
            weather_data = get_weather_data(city_name)
    elif request.method == 'GET':
        city_name = City.objects.latest('date_searched').city_name
        weather_data = get_weather_data(city_name)

    context = {
        'form': form,
        'weather_data': weather_data,
    }
    return render(request, 'home.html', context=context)