from django.urls import path
from control_blog.views import list_movies, add_movie, search_movies, list_genres, add_genre, search_genres

urlpatterns = [
    path('genres/', list_genres, name='genres_list'),
    path('new-genres/', add_genre, name='new_genre'),
    path('search-genres', search_genres, name='search_genres'),
    path('movies/', list_movies, name='movies_list'),
    path('new-movie/', add_movie, name='new_movie'),
    path('search-movies', search_movies, name='search_movies')
]
