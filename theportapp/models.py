from django.db import models
from django.urls import reverse
from django.utils import timezone
from django import forms

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    cloud_architecture = models.URLField(max_length=200, blank=True, verbose_name="Cloud Architecture")
    sre = models.URLField(max_length=200, blank=True, verbose_name="SRE")
    pipeline = models.URLField(max_length=200, blank=True, verbose_name="CI/CD Pipeline")
    cost_analysis = models.URLField(max_length=200, blank=True, verbose_name="Cost Analysis")
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="theport/images/")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    


    def get_absolute_url(self):
        return reverse('index')

class Messenger(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['created_on']    