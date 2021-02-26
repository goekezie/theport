from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.core.paginator import Paginator
from .forms import MessageForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from itertools import chain 
from mov.models import MoviePost
from tec.models import TechPost
from der.models import Post



# Create your views here.
def index(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 5)
    page = request.GET.get('page')
    projects = paginator.get_page(page)
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():      
            message_form.save()
            return HttpResponseRedirect('/')
    else:
        message_form = MessageForm()    
    return render(request, "theport/index.html", {"projects":projects, "message_form":message_form, 'successful_submit': True})


#certifications
def certifications(request):
    return render(request, "theport/certifications.html",)
    



def search(request):
    query = request.GET.get('q')
    quote = ''
    if query:
        postresults = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
        moviepostresults = MoviePost.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
        techpostresults = TechPost.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
        result_list = list(chain(
                    postresults,
                    moviepostresults,
                    techpostresults
                     ))
        if result_list != []:
            quote =  'Search result for : ' + query
        else: 
            quote = 'No result found for : ' + query
         

    else:
        postresults = Post.objects.filter(status=0)
        moviepostresults = MoviePost.objects.filter(status=0)
        techpostresults = TechPost.objects.filter(status=0)
        result_list = list(chain(
                    postresults,
                    moviepostresults,
                    techpostresults
                     ))  
        
    paginator = Paginator(result_list, 8)
    page = request.GET.get('page')
    results = paginator.get_page(page)
    context = {'results': results, 'query':query, 'quote':quote}

    return render(request, 'theport/search.html', context)

#resultdetail page
"""def resultdetail(request, slug=slug):
    result = get_object_or_404(MoviePost, TechPost, Post, slug=slug)
    return render(request, "theport/resultdetail.html", {"result":result})"""

