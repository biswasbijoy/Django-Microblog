from django import forms
from dbpost.models.models import Post


# class PostCreateForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     user_id = forms.IntegerField()

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
