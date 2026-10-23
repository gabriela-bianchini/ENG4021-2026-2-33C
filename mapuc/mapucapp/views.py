from django.shortcuts import render
import requests
from.models import Movie

def home(request):
    response = requests.get("https://omdbapi.com/?apikey=38b4b85b&s=Batman&type=movie")
    results_json = response.json()
    movies = results_json['Search']
    context = {
        'movies' : movies
    }
    return render(request, 'index.html', context)

def home2(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {"movies": movies})
