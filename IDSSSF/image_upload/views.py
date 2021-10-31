from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from keras.preprocessing import image
from keras import layers , models
import numpy as np


# =======

def create_model():
    model = models.Sequential()

    model.add(layers.Conv2D(16 , (3 , 3) , activation='relu' , input_shape=(224 , 224 , 3)))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D())

    model.add(layers.Conv2D(24 , (3 , 3) , activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D())

    model.add(layers.Conv2D(32 , (3 , 3) , activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D())

    model.add(layers.Conv2D(48 , (3 , 3) , activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D())

    model.add(layers.Conv2D(64 , (3 , 3) , activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D())

    model.add(layers.Flatten())

    model.add(layers.Dense(128 , activation='relu'))
    model.add(layers.Dropout(rate=0.3))
    model.add(layers.Dense(128 , activation='relu'))

    model.add(layers.Dense(10 , activation='softmax'))
    return model


# load_model
def load_model():
    model = create_model()
    model.load_weights("/Users/shoebadnan/Desktop/TEST/Intelligent_Decision_Support_System_For_Smart_Farming/saved_model/dss_model_final.h5")
    return model


# predicting images
def predict_img(img_path , model):
    path = img_path
    img = image.load_img(path , target_size=(224 , 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x , axis=0)

    images = np.vstack([x])
    classes = model.predict(images , batch_size=10)
    return classes


def get_class_label(classes):
    return list(classes[0]).index(max(classes[0]))

  
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
        model = load_model()
        image_url_modified = '/Users/shoebadnan/Desktop/Intelligent_Decision_Support_System_For_Smart_Farming/IDSSSF/' + Images.image_url.url
        classes = predict_img(image_url_modified , model)
        label = get_class_label(classes)
        return render(request, 'display_image.html',{'uploaded_images' : Images,'class_no':label})
