from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Project, Messenger 
from django import template


class ProjectAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Messenger)

# Register your models here.

