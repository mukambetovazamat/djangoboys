from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наз'
            }),

            'text': Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите наз'
                }),
        }

