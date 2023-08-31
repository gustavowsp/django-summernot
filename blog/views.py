from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from blog import forms
from blog import models


# Create your views here.
def index(request):

    return HttpResponse('Seja bem vindo a pagina inicial')

def create_artigo(request):

    if request.method == 'GET':
        form = forms.PostForm()
    else:
        form = forms.PostForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('blog:list_post')
    
    context = {
        'form' : form
    }

    return render(request,'blog/create.html', context )

def list_artigo(request):

    artigos = models.Post.objects.all()

    context = {
        'artigos' : artigos
        }
    
    return render(request,'blog/listagem.html',context)


def read_post(request, id_post):
    
    postagem = get_object_or_404(models.Post, id=id_post)

    context = {
        'artigo' : postagem
    }

    return render(request, 'blog/readpost.html', context)