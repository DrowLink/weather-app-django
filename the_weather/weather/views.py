import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# setting deserve


# Create your views here.
def index(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4a2fc37637d2bcd9f85f9b02c66ee6bd"
    city = 'Caracas'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city,
            'temperature': r['main']['temp'], 
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)
    
    print(weather_data)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather.html', context)
