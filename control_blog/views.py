from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from control_blog.models import Genre, Movie, Serie
from control_blog.forms import MovieForm, GenreForm, SerieForm
# Create your views here.
def list_genres(request):
    contexto = {'genres': Genre.objects.all()}
    http_response = render(
        request=request,
        template_name='control_blog/genres_list.html',
        context=contexto
    )
    return http_response

def add_genre(request):
    if request.method == "POST":
 
        formulario = GenreForm(request.POST) 
 
        if formulario.is_valid():
                  data = formulario.cleaned_data
                  name = data["name"]
                  genre = Genre(name=name)
                  genre.save()
                  url_exitosa = reverse('genres_list')  
                  return redirect(url_exitosa)
    
    else:
            formulario = GenreForm()
            
    
    http_response = render(
        request=request,
        template_name='control_blog/new_genre.html',
        context={'formulario': formulario}
    )
    return http_response

def search_genres(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        
        genres = Genre.objects.filter(
            Q(name__icontains=busqueda)
        )

        contexto = {
            "genres": genres,
        }
        http_response = render(
            request=request,
            template_name='control_blog/genres_list.html',
            context=contexto,
        )
        return http_response

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
    
def list_series(request):
    contexto = {'series': Serie.objects.all()}
    http_response = render(
        request=request,
        template_name='control_blog/series_list.html',
        context=contexto
    )
    return http_response

def add_serie(request):
    if request.method == "POST":
 
        formulario = SerieForm(request.POST) 
 
        if formulario.is_valid():
                  data = formulario.cleaned_data
                  title = data["title"]
                  seasons = data["seasons"]
                  release_year = data["release_year"]
                  plot = data['plot']
                  serie = Serie(title=title, seasons=seasons, release_year=release_year, plot=plot)
                  serie.save()
                  url_exitosa = reverse('series_list')  
                  return redirect(url_exitosa)
    
    else:
            formulario = SerieForm()
            
    
    http_response = render(
        request=request,
        template_name='control_blog/new_serie.html',
        context={'formulario': formulario}
    )
    return http_response

def search_series(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        
        series = Serie.objects.filter(
            Q(title__icontains=busqueda) | Q(release_year__contains=busqueda)
        )

        contexto = {
            "series": series,
        }
        http_response = render(
            request=request,
            template_name='control_blog/series_list.html',
            context=contexto,
        )
        return http_response
