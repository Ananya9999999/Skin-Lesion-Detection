from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

app = Flask(__name__)

model = load_model("model/skin_model.h5")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return {"error": "No image uploaded"}

    file = request.files["image"]

    if file.filename == "":
        return {"error": "Empty filename"}

    filepath = os.path.join("static", file.filename)
    file.save(filepath)

    img = image.load_img(filepath, target_size=(224, 224))
    img = image.img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]

    label = "Malignant" if prediction > 0.5 else "Benign"
    confidence = prediction * 100 if label == "Malignant" else (1 - prediction) * 100

    return render_template(
        "index.html",
        result=label,
        confidence=round(confidence, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
