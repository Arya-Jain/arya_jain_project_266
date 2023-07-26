import os
import cv2
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_image():
    # Get the selected image file
    image_file = request.files['file']
    # Get the degree of rotation from the user input
    degree = int(request.form['text'])
    # Secure the filename
    filename = secure_filename(image_file.filename)
    # Save the uploaded image file
    image_file.save(os.path.join('static/', filename))
    # Open the image using PIL
    image = Image.open(image_file)
    # Rotate the image by the specified degree
    image_rotation_degree = image.rotate(degree)
    # Save the rotated image
    image_rotation_degree.save(os.path.join('static/', 'rotated_image.jpg'))
    # Set the rotated image filename
    img_rotate = 'rotated_image.jpg'
    # Return the upload form with the rotated image displayed
    return render_template('upload.html', filename=img_rotate)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run()
