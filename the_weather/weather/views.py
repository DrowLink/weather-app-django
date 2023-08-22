from django.shortcuts import render

# setting deserve


# Create your views here.
def index(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=4a2fc37637d2bcd9f85f9b02c66ee6bd"
    return render(request, 'weather/weather.html')
