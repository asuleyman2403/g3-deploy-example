from django.forms import Form
from django import forms


class CreateBlogForm(Form):
    title = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}))
    description = forms.CharField(required=True,
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                                'placeholder': 'Enter blogs content'}))


class CreatePostForm(Form):
    title = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}))
    content = forms.CharField(required=True,
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                                'placeholder': 'Enter posts content'}))