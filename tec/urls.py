
from django.urls import path
from . import views

app_name = "tech"
urlpatterns = [
    path('', views.tech, name="tech"),
    path('<slug:slug>/', views.details, name="details"),
   
]