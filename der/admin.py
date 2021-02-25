from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment 
from django import template

class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

# Register your models here.
