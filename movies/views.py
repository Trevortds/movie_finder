from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render

# Create your views here.

def movie_list(request):
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get("test"))
        return JsonResponse({"result": "Success"})
    context = {}
    return render(request, 'movies/index.html', context=context)

def movie_detail(request, movie_id=None):
    if movie_id:
        return HttpResponse(f"Detail View for movie {movie_id}")
    else:
        return HttpResponseBadRequest()