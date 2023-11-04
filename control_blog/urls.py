from django.urls import path
from control_blog.views import list_movies

urlpatterns = [
    path('movies/', list_movies)
]
