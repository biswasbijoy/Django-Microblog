from django.urls import path
from dbpost.views.hello_veiw import home_page_veiw, create_post
from dbpost.views.func_base_view import post_list, post_details_view, post_create_view
from dbpost.views.class_base_view import PostListView, PostCreateView, PostDetailsView

app_name = "dbpost"

urlpatterns = [
    path('post-list', post_list, name="post_list"),
    path('create', create_post, name="create"),
    path('post-details/<int:post_id>', post_details_view, name="post_details"),
    path('post-create', post_create_view, name="post_create"),
    path('post-list-class', PostListView.as_view(), name="post_list_class"),
    path('post-create-class', PostCreateView.as_view(), name="post_create_class"),
    path('post-details-class/<int:pk>', PostDetailsView.as_view(), name="post_details_class"),
]