import os
from flask import Flask,  request

from CropDiseaseClasssifier.upload_image import upload_image

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CropDiseaseClasssifier/uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 16 megabytes size limit
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/upload-image", methods=["POST"])
def upload_img():
    return upload_image(request, ALLOWED_EXTENSIONS, app.config)