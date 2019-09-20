from django.contrib import admin
from .models import Movie, Vote, Person


admin.site.register(Movie)
admin.site.register(Vote)
admin.site.register(Person)