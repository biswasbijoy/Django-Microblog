from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm) :
    class Meta(UserCreationForm.Meta) :
        model = User
        fields = ('email',)
        
class CustomUserChangeForm(UserChangeForm) :
    class Meta(UserChangeForm.Meta) :
        model = User
        fields = ('email',)