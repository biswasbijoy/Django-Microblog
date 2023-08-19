from django.contrib import admin
from django.urls import path
from dbpost.views.hello_veiw import home_page_veiw, create_post

urlpatterns = [
    path('hello', home_page_veiw, name="hello"),
    path('create', create_post, name="create"),
]