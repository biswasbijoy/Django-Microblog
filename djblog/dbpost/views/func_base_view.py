from django.shortcuts import render, redirect
from dbpost.models.models import Post
from dbpost.forms.forms import PostCreateForm

def post_list(request):
    posts = Post.objects.all()
    
    response = {
        'posts': posts
    }
    return render(request, 'dbpost/post_list.html', response)

def post_details_view(request, post_id, *args, **kwargs):
    post_object = Post.objects.filter(id= post_id).first()
    return render(request, 'dbpost/post_details.html', {"post": post_object})

def post_create_view(request, *args, **kwargs) :
    form = PostCreateForm()
    if request.method == "POST" :
        data = request.POST
        form = PostCreateForm(data=data)
        if form.is_valid() :
            cl_data = form.cleaned_data
            post_obj = Post.objects.create(title=cl_data["title"], user_id=cl_data["user_id"])
            return redirect("dbpost:post_details", post_obj.id)
            
    return render(request, "dbpost/post_create.html", {"form": form})