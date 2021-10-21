from django import forms
from .models import *
  
class ImageUploadForm(forms.ModelForm):
  
    class Meta:
        model = ImageModel
        fields = ['image_url']