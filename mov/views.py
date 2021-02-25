from django.shortcuts import render, get_object_or_404
from .models import MoviePost, Comment
from dev.models import Post
from tech.models import TechPost
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentForm



# Create your views here.
def movie(request):
    movieposts = MoviePost.objects.all()
    emovieposts = MoviePost.objects.order_by('-created_on')[:1]   #First post header
    rmovieposts = MoviePost.objects.order_by('-created_on')[:3]  #recent posts
    paginator = Paginator(movieposts, 6)
    page = request.GET.get('page')
    movieposts = paginator.get_page(page)

    posts = Post.objects.all()
    mpaginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = mpaginator.get_page(page)
    
    techposts = TechPost.objects.all()
    tpaginator = Paginator(techposts, 3)
    page = request.GET.get('page')
    techposts = tpaginator.get_page(page)

    return render(request, "movie/movie.html", {"movieposts":movieposts, "posts":posts, "techposts":techposts, "emovieposts":emovieposts, "rmovieposts":rmovieposts})



#details view page
def details(request, slug):
    moviepost = get_object_or_404(MoviePost, slug=slug)

    comments = moviepost.comments.filter(approved_comment=True,  parent__isnull=True )
    totalcomments = moviepost.comments.filter(approved_comment=True)
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
            new_comment.moviepost = moviepost
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(moviepost.get_absolute_url())
    else:
        comment_form = CommentForm()

    return render(request, "movie/details.html", {"moviepost":moviepost, "comments":comments, "new_comment":new_comment, "comment_form":comment_form, "totalcomments":totalcomments})

