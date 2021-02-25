from django.shortcuts import render, get_object_or_404
from .models import TechPost, Comment
from dev.models import Post
from movie.models import MoviePost
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentForm



# Create your views here.
def tech(request):
    techposts = TechPost.objects.all()
    etechposts = TechPost.objects.order_by('-created_on')[:1]   #First post header
    rtechposts = TechPost.objects.order_by('-created_on')[:3]  #recent posts
    paginator = Paginator(techposts, 6)
    page = request.GET.get('page')
    techposts = paginator.get_page(page)
    
    posts = Post.objects.all()
    tpaginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = tpaginator.get_page(page)

    movieposts = MoviePost.objects.all()
    mpaginator = Paginator(movieposts, 3)
    page = request.GET.get('page')
    movieposts = mpaginator.get_page(page)
    return render(request, "tech/tech.html", {"techposts":techposts, "posts":posts, "movieposts":movieposts, "etechposts":etechposts, "rtechposts":rtechposts})



#details view page
def details(request, slug):
    techpost = get_object_or_404(TechPost, slug=slug)
    comments = techpost.comments.filter(approved_comment=True,  parent__isnull=True )
    totalcomments = techpost.comments.filter(approved_comment=True)
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
            new_comment.techpost = techpost
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(techpost.get_absolute_url())
    else:
        comment_form = CommentForm()

    return render(request, "tech/details.html", {"techpost":techpost, "comments":comments, "new_comment":new_comment, "comment_form":comment_form, "totalcomments":totalcomments})