from django.shortcuts import render
from dbpost.models.models import Post


def post_list(request):
    posts = Post.objects.all()
    
    response = {
        'posts': posts
    }
    return render(request, 'dbpost/post_list.html', response)