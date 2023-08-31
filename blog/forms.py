from django import forms
from django_summernote.widgets import SummernoteWidget
from blog import models

class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = ('titulo','descricao','blog_post')
        widgets = {
            'blog_post' : SummernoteWidget()
        }