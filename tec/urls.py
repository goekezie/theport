
from django.urls import path
from . import views

app_name = "tec"
urlpatterns = [
    path('', views.tec, name="tec"),
    path('<slug:slug>/', views.details, name="details"),
   
]