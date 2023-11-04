from django.shortcuts import render
from control_blog.models import Movie
# Create your views here.
def list_movies(request):
    contexto = {'movies': Movie.objects.all()}
    http_response = render(
        request=request,
        template_name='control_blog/movies_list.html',
        context=contexto
    )
    return http_response