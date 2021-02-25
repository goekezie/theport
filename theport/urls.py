"""theport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from theportapp import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "index"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),

    path('certifications/', views.certifications, name="certifications"),
    path('about/', views.about, name="about"),
    path('search/', views.search, name="search"),
    
    
    
    #path('', include(('post.urls', 'post'), namespace='post')),



    #movies
    path('movie/', include('movie.urls')),

    #techhardware
    path('tech/', include('tech.urls')),

    #django-summernote
    path('summernote/', include('django_summernote.urls')),

    path('<slug:slug>/', views.details, name="details"),

    path('<slug:slug>/', views.resultdetail, name="resultdetail"),

    #django-summernote
    path('summernote/', include('django_summernote.urls')),
]

#Further edit of debug feature for dev and hosting
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
