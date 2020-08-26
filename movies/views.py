from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.

def movie_list(request):
    return HttpResponse("List view")

def movie_detail(request, movie_id=None):
    if movie_id:
        return HttpResponse(f"Detail View for movie {movie_id}")
    else:
        return HttpResponseBadRequest()