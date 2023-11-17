import pysrial_connectivity as pc
import local_img_classifier as lic
import tensorflow as tf

from pyfiglet import Figlet

def main():
    imgName = lic.captureImage()
    model = tf.keras.models.load_model('garbage_classifier_new.h5')
    
    score, classNum, className = lic.classification(model, imgName)

    # print(classNum, className)
    pc.inputSerial('COM4', 115200, input())

if __name__ == '__main__':
    f = Figlet()
    print(f.renderText('Dump-It'))
    main()