from django.shortcuts import render

# Create your views here.
def list_movies(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_blog/movies_list.html',
        context=contexto
    )
    return http_response