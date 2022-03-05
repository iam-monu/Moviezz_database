from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader



import requests

# Create your views here.
def index(request):
    query = request.GET.get('q')

    if query:
        url = 'https://www.omdbapi.com/?apikey=951a2211&s=' + query
        response = requests.get(url)
        movie_data = response.json()

        context ={
            'query': query,
            'movie_data': movie_data,
            'page_number': 1,
        }
        template = loader.get_template('search_results.html')

        return HttpResponse(template.render(context, request))

    return render(request,'index.html')

def pagination(request, query, page_number):

    url = 'https://www.omdbapi.com/?apikey=951a2211&s=' + query +'&page='+ str(page_number)
    # https://www.omdbapi.com/?apikey=951a2211&s=Batman&page=2
    response = requests.get(url)
    movie_data = response.json()
    page_number = int(page_number) +1

    context ={
            'query': query,
            'movie_data': movie_data,
            'page_number' : page_number,
    }

    template = loader.get_template('search_results.html')

    return HttpResponse(template.render(context, request))




