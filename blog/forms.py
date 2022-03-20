from django.forms import ModelForm
from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['body'].widget = CKEditorWidget(attrs={'class': 'form-control'})