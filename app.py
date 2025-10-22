import os
import uuid
import numpy as np
import cv2
import faiss
from flask import Flask, render_template, request, redirect, url_for

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize global FAISS index
VECTOR_DIM = 64 * 64  # flattened grayscale image size (64x64)
faiss_index = faiss.IndexFlatL2(VECTOR_DIM)

# ----------------  Functions ---------------- #

# Save an image and return its path
def save_image(image, prefix):
    filename = f"{prefix}_{uuid.uuid4().hex}.png"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    cv2.imwrite(filepath, image)
    return filepath

# Generate a 1D feature vector from image
def generate_vector(image_path):
    img = cv2.imread(image_path)
    img_resized = cv2.resize(img, (64, 64))
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    vector = gray.flatten().astype(np.float32)
    return vector

# ---------------- Flask Routes ---------------- #

@app.route('/', methods=['GET'])
def home():
    """Render main upload page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    """Handle image upload and processing."""
    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    # Save uploaded file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Read image using OpenCV
    img = cv2.imread(filepath)

    # Processing: grayscale, edges, blur
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    blur = cv2.GaussianBlur(img, (7, 7), 0)

    # Save processed versions
    gray_path = save_image(gray, "gray")
    edges_path = save_image(edges, "edges")
    blur_path = save_image(blur, "blur")

    # Generate vector and store in FAISS
    vector = generate_vector(filepath)
    faiss_index.add(np.expand_dims(vector, axis=0))

    # Render results page
    return render_template(
        'results.html',
        original=url_for('static', filename=f'uploads/{os.path.basename(filepath)}'),
        gray=url_for('static', filename=f'uploads/{os.path.basename(gray_path)}'),
        edges=url_for('static', filename=f'uploads/{os.path.basename(edges_path)}'),
        blur=url_for('static', filename=f'uploads/{os.path.basename(blur_path)}'),
        message="✅ Image processed and vector stored successfully."
    )

# ---------------- Main Entry ---------------- #

if __name__ == '__main__':
    app.run(debug=True)
