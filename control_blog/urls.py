from django.urls import path
from control_blog.views import list_movies, add_movie, search_movies

urlpatterns = [
    path('movies/', list_movies, name='movies_list'),
    path('new-movie/', add_movie, name='new_movie'),
    path('search-movies', search_movies, name='search_movies')
]
