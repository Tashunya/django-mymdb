from django.contrib import admin
from .models import Movie, Vote, Person, MovieImage


admin.site.register(Movie)
admin.site.register(Vote)
admin.site.register(Person)
admin.site.register(MovieImage)