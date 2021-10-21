from django.db import models

# Create your models here.
class ImageModel(models.Model):
    #name = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to='images/')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    owner = models.CharField(max_length=20)


    def __str__(self):
        return self.owner