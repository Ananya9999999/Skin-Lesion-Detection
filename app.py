from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app= Flask(__name__)

MODEL_PATH= "model/skin_model.h5"

model= None
if os.path.exists(MODEL_PATH):
    model= tf.keras.models.load_model(MODEL_PATH)

def preprocess_image(image):
    image=image.resize((224, 224))
    image= np.array(image)/255.0
    image= np.expand_dims(image, axis=0)
    return image

