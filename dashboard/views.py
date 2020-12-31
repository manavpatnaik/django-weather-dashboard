from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):
    weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=coimbatore&appid=6d37ed00a79179857e7f18eaaeef43fe')
    print(weather)
    return render(request, 'home.html')
