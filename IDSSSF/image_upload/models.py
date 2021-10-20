from django.db import models

# Create your models here.
class ImageModel(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to='images/')