from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
  
# Create your views here.
def image_view(request):
  
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')

def display_images(request):
  
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        Images = ImageModel.objects.all() 
        return render(request, 'display_image.html',{'uploaded_images' : Images})
