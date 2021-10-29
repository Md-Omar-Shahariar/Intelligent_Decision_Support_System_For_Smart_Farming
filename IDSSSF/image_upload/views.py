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
            post = form.save(commit=False)
            post.owner = current_user.phone
            post.save()
            return redirect('display_images')
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload.html', {'form' : form,'user':current_user})
  
  
def success(request):
    return HttpResponse('successfully uploaded')

def display_images(request):
    current_user = request.user
  
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        Images = ImageModel.objects.filter(owner=current_user.phone).latest('created_on') 
        return render(request, 'display_image.html',{'uploaded_images' : Images})
