from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect

from solution.models import SolutionModel
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
    return render(request, 'image_upload_v1.html', {'form' : form,'user':current_user})
  
  
def success(request):
    return HttpResponse('successfully uploaded')

def index_to_class_name(index):
    c_name = ''
    if index == 0:
        c_name = 'Bacterial Leaf Blight'
    elif index == 1:
        c_name = 'Brown Plant Hopper'
    elif index == 2:
        c_name = 'Brown Spot'
    elif index == 3:
        c_name = 'Rice False Smut'
    elif index == 4:
        c_name = 'Healthy Plant'
    elif index == 5:
        c_name = 'Hispa'
    elif index == 6:
        c_name = 'Leaf Smut'
    elif index == 7:
        c_name = 'Neck Blast'
    elif index == 8:
        c_name = 'Sheath Blight Rot'
    elif index == 9:
        c_name = 'Stem Borer'
    return c_name



def display_images(request):
    current_user = request.user
  
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        
        Images = ImageModel.objects.filter(owner=current_user.phone).latest('created_on') 
        model = load_model()
        image_url_modified = '/Users/shoebadnan/Desktop/Intelligent_Decision_Support_System_For_Smart_Farming/IDSSSF/' + Images.image_url.url
        classes = predict_img(image_url_modified , model)
        label = get_class_label(classes)
        print('Label = '+ str(label))
        class_name = index_to_class_name(label)
        print('Class Name = '+ class_name)
        solution = SolutionModel.objects.filter(disease_name = str(class_name))
        print(solution)
        print('About = '+ str(solution[0].disease_name))

        if solution[0].disease_name == "Healthy Plant":
            return render(request, 'healthy_plant.html',{'uploaded_images' : Images})
        else:
            return render(request, 'display_image_v1.html',{'uploaded_images' : Images,'solution':solution[0]})
