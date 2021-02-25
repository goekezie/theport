
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from mov.models import MoviePost
from tec.models import TechPost
from django.core.paginator import Paginator

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentForm

# dev.
def der(request):
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

    return render(request, "der/der.html", {"posts":posts, "movieposts":movieposts, "techposts":techposts, "eposts":eposts, "rposts":rposts})



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
    return render(request, "der/details.html", {"post":post, "comments":comments, "new_comment":new_comment, "comment_form":comment_form, "totalcomments":totalcomments})
    #details comment
    





