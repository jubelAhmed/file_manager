from django import forms
from .models import FileManager


class FileManagerForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = FileManager
        fields = ('files', 'name', 'description')