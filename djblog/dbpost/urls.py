from django.contrib import admin
from django.urls import path
from dbpost.views.hello_veiw import home_page_veiw, create_post
from dbpost.views.post_list_view import post_list

urlpatterns = [
    path('post-list', post_list, name="post_list"),
    path('create', create_post, name="create"),
]