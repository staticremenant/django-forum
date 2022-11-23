from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description', 'image']

class CommentForm(forms.ModelForm):
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={
    'class': 'md-textarea form-control',
    'placeholder': 'leave a comment...',
    'rows': '1',
    }))

    class Meta:
        model = Comment
        fields = ('content', 'image')
