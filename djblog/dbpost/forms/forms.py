from django import forms

class PostCreateForm(forms.Form):
    title = forms.CharField(max_length = 50)
    user_id = forms.IntegerField()