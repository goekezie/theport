from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class MoviePost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(blank=True, default=0)
    image = models.ImageField(upload_to="movie/images/", blank=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('mov:details', args={self.slug})

class Comment(models.Model):
    moviepost = models.ForeignKey(MoviePost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    text = models.TextField()
    email = models.EmailField()
    created_on = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="movie/images/", default="dev/images/mando.jpg")
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    class Meta:
        ordering = ['created_on']