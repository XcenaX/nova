from django import forms

from .models import User, Comment, Blog

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','password')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'category', 'img_url')
    

