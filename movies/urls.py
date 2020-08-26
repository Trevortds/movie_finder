from django.urls import path

from . import views

urlpatterns = [
    path('', views.movie_list, name='index'),
    path('<slug:movie_id>', views.movie_detail, name='detail'),
]