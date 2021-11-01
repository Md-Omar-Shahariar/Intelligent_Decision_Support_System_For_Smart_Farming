from django.db import models

from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField, widgets
from django import forms
# Create your models here.


class ImageModel(models.Model):
    #name = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to='images/')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    owner = models.CharField(max_length=20)

    def __str__(self):
        return self.owner

    