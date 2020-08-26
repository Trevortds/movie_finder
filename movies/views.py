import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
import requests

# Create your views here.

def movie_list(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        print(data.get("search_query"))
        query = data.get("search_query")
        response_json = {
            "results": []
        }
        if not query:
            response = requests.get("https://api.themoviedb.org/3/movie/popular",
                                    params={"api_key": settings.MOVIE_DATABASE_KEY})
            if response.status_code == 200:
                response_json["results"] = response.json()["results"]
            else:
                return HttpResponseBadRequest("Movie Database Request Didn't Work")
        else:
            response = requests.get("https://api.themoviedb.org/3/search/movie",
                                    params={"api_key": settings.MOVIE_DATABASE_KEY,
                                            "query": query})
            if response.status_code == 200:
                response_json["results"] = response.json()["results"]
            else:
                return HttpResponseBadRequest("Movie Database Request Didn't Work")
        return JsonResponse(response_json)
    context = {}
    return render(request, 'movies/index.html', context=context)

def movie_detail(request, movie_id=None):
    if movie_id:
        context = {}
        response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}",
                                    params={"api_key": settings.MOVIE_DATABASE_KEY})
        if response.status_code == 200:
            context["movie"] = response.json()
        else:
            return HttpResponseBadRequest("Error getting information on movie")
        return render(request, 'movies/detail.html', context=context)
    else:
        return HttpResponseBadRequest()