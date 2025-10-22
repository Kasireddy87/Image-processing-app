# Image-processing-app

# Image-processing-app

**1. Project Overview****

This project is a Flask-based web application that allows users to upload an image, performs several basic computer vision operations using OpenCV, and then stores a feature vector of the image in a FAISS vector index for similarity search.
It demonstrates how to integrate a web framework, image processing, and a vector database into a simple, functional end-to-end application.

**2. Objectives**

Develop a web application using Flask that allows users to upload images and view processing results.
Perform image processing operations using OpenCV, including:
    Grayscale conversion
    Edge detection (Canny algorithm)
    Gaussian blurring
Generate a numerical feature vector from the uploaded image to represent its content.
Store image vectors in a FAISS index for efficient similarity search or retrieval.
Display all processed images and a confirmation message in the UI, ensuring a user-friendly experience.

**3.Project Structure**

image-processing-app/
│
├── app.py                   # Main Flask application
├── requirements.txt          # List of dependencies
│
├── /templates
│   ├── index.html            # Image upload form
│   └── results.html          # Result display page
│
└── /static
    └── /uploads              # Temporary storage for uploaded and processed images

**4.How It Works**
User Uploads Image via the home page (index.html).
**The backend:**

a.Saves the uploaded image.
b.Converts it to grayscale.
c.Performs edge detection using Canny algorithm.
d.Applies Gaussian Blur to the original image.
e.All processed images are saved in /static/uploads/.
f.A feature vector (flattened grayscale 64×64 image) is generated.
g.The vector is added to a FAISS index (for future similarity search).
h.The results page (results.html) displays all processed images and a success message.

**AI Usage Disclosure**

AI-assisted parts:

a.Helped design the project structure (folders, templates, static paths).

b.Assisted in writing the Flask routes (/ and /upload).

c.Helped with FAISS vector index setup and vector generation logic.

d.Suggested README.md format and documentation improvements.

e.Provided debugging help for dependency installation and import errors.
