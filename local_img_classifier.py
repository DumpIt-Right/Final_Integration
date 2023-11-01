import cv2
import PIL
import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers,models
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import Callback, EarlyStopping,ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import Model
from tensorflow.keras.layers.experimental import preprocessing



def captureImage():
    #code for opening camera and taking picture
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    img_counter = 0
    img_name = None
    while True:
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        if k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))

            img = PIL.Image.open(img_name)
            img = img.resize((224, 224))
            img.save(img_name)

            break
            
    
    cap.release()
    cv2.destroyAllWindows()

    return img_name

def imgAnnotation(img_name, className):
    img = cv2.imread(img_name)
    img = cv2.putText(img, className, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('image', img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

def classification(model, img_name):
    img = keras.preprocessing.image.load_img(
    img_name, target_size=(224, 224))
    
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    score = tf.nn.softmax(predictions[0])
    class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

    print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
    )

    classNum = np.argmax(score)
    className = class_names[classNum]

    classNum += 1

    imgAnnotation(img_name, className)

    return score, classNum, className

if __name__ == '__main__':
    img_name = captureImage()

    model = tf.keras.models.load_model('garbage_classifier_new.h5')

    score, classNum, className = classification(model, img_name)

    print(classNum, type(classNum), str(classNum))