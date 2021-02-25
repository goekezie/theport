
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from movie.models import MoviePost
from tech.models import TechPost
from django.core.paginator import Paginator
from django.db.models import Q
from itertools import chain
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentForm

# Homepage.
def index(request):
    posts = Post.objects.all()
    eposts = Post.objects.order_by('-created_on')[:1]   #First post header
    rposts = Post.objects.order_by('-created_on')[:3]  #recent posts
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    movieposts = MoviePost.objects.all()
    mpaginator = Paginator(movieposts, 3)
    page = request.GET.get('page')
    movieposts = mpaginator.get_page(page)

    techposts = TechPost.objects.all()
    tpaginator = Paginator(techposts, 3)
    page = request.GET.get('page')
    techposts = tpaginator.get_page(page)

    return render(request, "dev/index.html", {"posts":posts, "movieposts":movieposts, "techposts":techposts, "eposts":eposts, "rposts":rposts})



#details view page
def details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved_comment=True,  parent__isnull=True )
    totalcomments = post.comments.filter(approved_comment=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    reply_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    reply_comment.parent = parent_obj
               
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    return render(request, "dev/details.html", {"post":post, "comments":comments, "new_comment":new_comment, "comment_form":comment_form, "totalcomments":totalcomments})
    #details comment
    


#certifications
def certifications(request):
    return render(request, "dev/certifications.html",)



#About
def about(request):
    return render(request, "dev/about.html",)


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
            quote =  'Search result for ' + query
        else: 
            quote = 'No result found for ' + query
         

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

    return render(request, 'dev/search.html', context)

#resultdetail page
def resultdetail(request, slug):
    result = get_object_or_404(MoviePost, TechPost, Post, slug=slug)
    return render(request, "dev/resultdetail.html", {"result":result})
