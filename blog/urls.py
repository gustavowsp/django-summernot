from django.urls import path 
from blog import views


app_name = 'blog'

urlpatterns = [

    path('',views.index, name='home'),
    
    # Post
    path('post/create',views.create_artigo, name='create_post'),
    path('post/list',views.list_artigo, name='list_post'),
    path('post/<int:id_post>/read',views.read_post, name='read_post'),

]