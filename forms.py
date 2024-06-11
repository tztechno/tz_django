
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}), label='Content')

    class Meta:
        model = Post
        fields = ['title', 'content']

