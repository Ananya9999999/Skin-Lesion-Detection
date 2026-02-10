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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    image_file= request.files['image']
    image= Image.open(image_file)

    if model is None:
        return jsonify({
            "label": "Model not loaded",
            "confidence": 0
        })
    
    img= preprocess_image(image)
    prediction= model.predict(img)[0][0]

    label= "Malignant" if prediction > 0.5 else "Benign"
    confidence= round(float(prediction)*100, 2)

    return jsonify({
        "label": label,
        "confidence": confidence
    })

if __name__ == '__main__':
    app.run(debug=True)