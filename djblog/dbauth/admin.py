from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth import get_user_model
from dbauth.forms.forms import CustomUserCreationForm, CustomUserChangeForm
from dbauth.models.models import UserProfile

User = get_user_model()
admin.site.register(UserProfile)

@admin.register(User)
class CustomUserAdmin(UserAdmin) :
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    search_fields = ('email',)
    ordering = ('-id',)
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        ("basic Info", {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
    )