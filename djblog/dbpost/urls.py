from django.urls import path
from dbpost.views.hello_veiw import home_page_veiw, create_post
from dbpost.views.func_base_view import post_list, post_details_view, post_create_view

app_name = "dbpost"

urlpatterns = [
    path('post-list', post_list, name="post_list"),
    path('create', create_post, name="create"),
    path('post-details/<int:post_id>', post_details_view, name="post_details"),
    path('post-create', post_create_view, name="post_create"),
]