from django import forms
from django.forms import fields, widgets
from .models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('city_name',)
        widgets = {
            'city_name': forms.TextInput(attrs={'class': 'form-control my-3 w-75 m-auto', 'placeholder': 'City Name...'})
        }