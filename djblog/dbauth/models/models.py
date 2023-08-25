from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from dbpost.models.core_models import *



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email :
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user
    


class User(AbstractUser, PermissionsMixin) :
    username = models.CharField(max_length = 144, unique=False)
    email = models.EmailField(max_length = 144,unique=True)
    mobile = models.CharField(max_length = 14, blank=True)
    is_active = models.BooleanField(default=True)
    object = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email


class UserProfile(BaseStampStampModel):
    phone = models.CharField(max_length = 14, blank=True)
    address = models.CharField(max_length = 144, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email
