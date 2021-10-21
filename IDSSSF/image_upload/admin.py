from django.contrib import admin

from .models import ImageModel

# Register your models here.

class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('owner', 'created_on', 'image_url')




admin.site.register(ImageModel, ImageModelAdmin)
