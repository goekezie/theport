
from django.urls import path
from . import views

app_name = "der"
urlpatterns = [
    path('', views.der, name="der"),
    path('<slug:slug>/', views.details, name="details"),


    path('certifications/', views.certifications, name="certifications"),
    path('search/', views.search, name="search"),

    path('<slug:slug>/', views.resultdetail, name="resultdetail"),    
]