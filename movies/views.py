from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.http import JsonResponse

def index(request, movie_id=None):
    movies = Movie.objects.all()
    selected_movie = None

    if movie_id:
        selected_movie = get_object_or_404(Movie, id=movie_id)

    return render(request, 'index.html', {
        'movies': movies,
        'selected_movie': selected_movie
    })
    
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie_details.html', {'movie': movie})

def movie_details_ajax(request, movie_id):
    from django.forms.models import model_to_dict
    movie = get_object_or_404(Movie, id=movie_id)
    return JsonResponse(model_to_dict(movie))




