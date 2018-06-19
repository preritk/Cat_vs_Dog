import base64
import io
import numpy as np
from PIL import Image
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import Flask,request,redirect
from flask import render_template,jsonify

app = Flask(__name__)

@app.route('/letsgo')
def letsgo():
    return render_template('predict.html')

def get_model():
    global model
    model = load_model('my_model.h5')
    print("Model loaded !")
    
def preprocess_image(image,target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image,axis = 0)
    return image

print("Loading Keras model")
get_model()


@app.route("/predict",methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        option = request.form['image']
        if(option == '1'):
            img = Image.open("cat.jpg")
            processed_image = preprocess_image(img,target_size = (32,32))
            matrix = []
            matrix.append(processed_image)
            prediction = model.predict(matrix).tolist()
            return '{}'.format(prediction)
        else:
            img = Image.open("deer.jpeg")
            processed_image = preprocess_image(img,target_size = (32,32))
            matrix = []
            matrix.append(processed_image)
            prediction = model.predict(matrix).tolist()
            return '{}'.format(prediction)
    else:
        return '0'