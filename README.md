🩺 Skin Lesion Detection using Deep Learning

An AI-powered web application that classifies skin lesion images using a Convolutional Neural Network (CNN). This project aims to assist in the early detection of skin diseases by providing fast and automated image-based predictions.

⚠️ This project is for educational and research purposes only and is not a substitute for professional medical advice.

🚀 Features

📤 Upload skin lesion images

🤖 Deep Learning-based classification (CNN)

🌐 Simple and responsive web interface

⚡ Real-time prediction results

🧠 TensorFlow/Keras model integration

🛠 Tech Stack

Frontend: HTML, CSS

Backend: Flask (Python)

Deep Learning: TensorFlow, Keras

Other Tools: NumPy, OpenCV / PIL

📂 Project Structure
```Skin-Lesion-Detection/
│
├── static/               # CSS, images
├── templates/            # HTML files
│   └── index.html
├── model/                # Trained model file (.h5)
├── app.py                # Flask application
├── requirements.txt
└── README.md
```
⚙️ Installation & Setup
```1️⃣ Clone the repository
git clone https://github.com/your-username/Skin-Lesion-Detection.git
cd Skin-Lesion-Detection

2️⃣ Create a virtual environment (Recommended)
```python -m venv .venv```
```

Activate it:

Windows
```
.venv\Scripts\activate
```

Mac/Linux
```
source .venv/bin/activate
```
3️⃣ Install dependencies
```pip install -r requirements.txt```

4️⃣ Run the application
```python app.py```


Open your browser and go to:
```
http://127.0.0.1:5000/
```
🧠 Model Information

Model Type: Convolutional Neural Network (CNN)

Framework: TensorFlow / Keras

Input: Skin lesion image

Output: Predicted lesion category

You can retrain the model using your own dataset for improved accuracy.

📊 How It Works

User uploads an image.

Image is preprocessed (resizing, normalization).

The trained CNN model predicts the class.

Prediction result is displayed on the web interface.

🔮 Future Improvements

Add confidence percentage display

Improve UI/UX design

Deploy using Heroku / Render / AWS

Add more skin disease classes

Integrate Grad-CAM for model explainability

📌 Disclaimer

This application is intended for educational purposes only. It does not provide medical diagnosis. Always consult a qualified healthcare professional for medical advice.
