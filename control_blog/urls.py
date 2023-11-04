from django.urls import path
from control_blog.views import list_movies, add_movie

urlpatterns = [
    path('movies/', list_movies, name='movies_list'),
    path('new-movie/', add_movie, name='new_movie'),
]
