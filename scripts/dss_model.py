from keras.preprocessing import image
from tensorflow.keras import layers , models
import numpy as np


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
    model.load_weights("saved_model/dss_model_final.h5")
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


if __name__ == "__main__":
    model = load_model()
    classes = predict_img("C:\\Users\DELL\OneDrive\Desktop/brown.png" , model)
    label = get_class_label(classes)
    print(label)
