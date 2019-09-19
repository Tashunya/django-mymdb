from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie


class MovieList(ListView):
    """
    creates view for all the movies
    """
    model = Movie
    paginate_by = 10


class MovieDetail(DetailView):
    """
    creates view for one movie
    """
    model = Movie
