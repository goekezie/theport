from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.core.paginator import Paginator
from .forms import MessageForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 

# Create your views here.
def index(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 5)
    page = request.GET.get('page')
    projects = paginator.get_page(page)
    response = ""
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():      
            message_form.save()
            response = HttpResponse("message sent ")
            return HttpResponseRedirect('/')
    else:
        message_form = MessageForm()    
    return render(request, "theport/index.html", {"projects":projects, "message_form":message_form, 'successful_submit': True, "response":response})



    