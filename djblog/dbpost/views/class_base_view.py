# from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from dbpost.forms.forms import PostCreateForm
from dbpost.models.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "dbpost/post_list.html"


class PostCreateView(CreateView):
    model = Post
    # fields = "__all__"
    form_class = PostCreateForm
    template_name = "dbpost/post_create.html"
    # success_url = reverse_lazy("dbpost:post_details_class", kwargs={"pk": 1})


class PostDetailsView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "dbpost/post_details.html"
