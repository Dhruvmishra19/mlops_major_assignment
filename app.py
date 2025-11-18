from flask import Flask, render_template, request
import joblib
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Load the trained model + test data
data = joblib.load("models/savedmodel.pth")
model = data["model"]

# Olivetti dataset expects 64x64 grayscale images
def preprocess_image(image_path):
    img = Image.open(image_path).convert("L")  
    img = img.resize((64, 64))
    img_array = np.array(img).reshape(1, -1)
    return img_array

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']
    file_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(file_path)

    img_array = preprocess_image(file_path)
    pred = model.predict(img_array)[0]

    return f"Predicted Class: {pred}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

