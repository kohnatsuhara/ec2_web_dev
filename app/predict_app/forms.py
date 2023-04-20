from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    file = forms.FileField()

    class Meta:
        model = Post
        fields = ("title", "text")
        
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    
    file = forms.FileField()