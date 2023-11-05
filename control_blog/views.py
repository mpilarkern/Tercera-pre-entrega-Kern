from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from control_blog.models import Movie
from control_blog.forms import MovieForm
# Create your views here.
def list_movies(request):
    contexto = {'movies': Movie.objects.all()}
    http_response = render(
        request=request,
        template_name='control_blog/movies_list.html',
        context=contexto
    )
    return http_response

def add_movie(request):
    if request.method == "POST":
 
        formulario = MovieForm(request.POST) 
 
        if formulario.is_valid():
                  data = formulario.cleaned_data
                  title = data["title"]
                  length = data["length"]
                  release_year = data["release_year"]
                  plot = data['plot']
                  movie=Movie(title=title, length=length, release_year=release_year, plot=plot)
                  movie.save()
                  url_exitosa = reverse('movies_list')  
                  return redirect(url_exitosa)
    
    else:
            formulario = MovieForm()
            
    
    http_response = render(
        request=request,
        template_name='control_blog/new_movie.html',
        context={'formulario': formulario}
    )
    return http_response

def search_movies(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        
        movies = Movie.objects.filter(
            Q(title__icontains=busqueda) | Q(release_year__contains=busqueda)
        )

        contexto = {
            "movies": movies,
        }
        http_response = render(
            request=request,
            template_name='control_blog/movies_list.html',
            context=contexto,
        )
        return http_response
