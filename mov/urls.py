
from django.urls import path
from . import views

app_name = "movie"
urlpatterns = [
    path('', views.movie, name="movie"),
    path('<slug:slug>/', views.details, name="details"),
    
]