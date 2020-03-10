from django import forms
from .models import ImageModel

class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageModel
        fields = ['input_image', 'output_name', 'input_threshold']
