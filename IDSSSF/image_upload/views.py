from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
  
# Create your views here.
def image_view(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        
  
        if form.is_valid():
            
            form.owner = current_user.first_name
            form.save()
            return redirect('display_images')
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload.html', {'form' : form,'user':current_user})
  
  
def success(request):
    return HttpResponse('successfully uploaded')

def display_images(request):
  
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        Images = ImageModel.objects.all() 
        return render(request, 'display_image.html',{'uploaded_images' : Images})
