import os
from flask import Flask,  request

from CropDiseaseClasssifier import upload_image, webhook

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CropDiseaseClasssifier/uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
REPO_PATH = "/home/sunaam/mysite"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 16 megabytes size limit
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.config['REPO_PATH'] = REPO_PATH

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/upload-image", methods=["POST"])
def upload_img():
    return upload_image.upload_image(request, ALLOWED_EXTENSIONS, app.config)

@app.route('/update_server', methods=['POST'])
def update_server():
    return webhook.webhook(request,app.config)