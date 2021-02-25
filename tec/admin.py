from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TechPost, Comment



class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}

    

admin.site.register(TechPost, PostAdmin)
admin.site.register(Comment)


# Register your models here.
