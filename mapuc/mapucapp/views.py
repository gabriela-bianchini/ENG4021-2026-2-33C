from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import Movie
from .forms import MovieForm

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
def criar_filme(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home2')
    return render(request, 'movie_form.html', {'form': form, 'titulo': 'Novo filme'})

def editar_filme(request, pk):
    filme = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=filme)
    if form.is_valid():
        form.save()
        return redirect('home2')
    return render(request, 'movie_form.html', {'form': form, 'titulo': 'Editar filme'})


def deletar_filme(request, pk):
    filme = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        filme.delete()
    return redirect('home2')
