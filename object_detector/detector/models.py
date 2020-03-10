from django.db import models


class ImageModel(models.Model):
    input_name = models.CharField(max_length=50)
    input_image = models.ImageField(upload_to='uploaded_images')
    input_threshold = models.FloatField(default=0.7)
    
