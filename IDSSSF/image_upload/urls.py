from django.contrib import admin
from django.urls import path
from .views import *
  
urlpatterns = [
    path('', image_view, name = 'image_upload'),
    path('success', success, name = 'success'),
    path('display', display_images, name = 'display_images'),
]
  
