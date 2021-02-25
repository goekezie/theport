
from django.urls import path
from . import views

app_name = "mov"
urlpatterns = [
    path('', views.mov, name="mov"),
    path('<slug:slug>/', views.details, name="details"),
    
]