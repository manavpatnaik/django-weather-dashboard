from django.shortcuts import render
from django.http import HttpResponse
from .forms import CityForm
import requests

def home(request):
    form = CityForm()
    weather_data = {}
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            city_name = form.cleaned_data.get('city_name')
            
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=6d37ed00a79179857e7f18eaaeef43fe&unit=metric'
            response = requests.get(url)
            json_response = response.json()

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

    context = {
        'form': form,
        'weather_data': weather_data,
    }
    return render(request, 'home.html', context=context)
