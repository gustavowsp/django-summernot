from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin 
from blog import models


# Register your models here.
@admin.register(models.Post)
class PostAdmin(SummernoteModelAdmin):
    ...
    #summernote_fields = ('blog_post',)

