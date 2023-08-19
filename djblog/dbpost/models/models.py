from django.db import models
from django.contrib.auth import get_user_model
from dbpost.models.core_models import BaseStampStampModel
from dbpost.models.categories import PostCategory
from django.utils import timezone


User = get_user_model()

class Post(BaseStampStampModel) :
    title = models.CharField(max_length=50, blank = False)
    description = models.TextField(blank = True)
    published = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(PostCategory, related_name = 'post')
    