from RootUtils.allowed_file import allowed_file

from werkzeug.utils import secure_filename
import os


def upload_image(request, ALLOWED_EXTENSIONS, appConfig)->str:
    if request.method != 'POST':
        return "Method not allowed. Please send a POST request."
    
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']

    if file and allowed_file(file.filename, ALLOWED_EXTENSIONS, appConfig, request):
        filename = secure_filename(file.filename)
        file.save(os.path.join(appConfig['UPLOAD_FOLDER'], filename))
        return f"File uploaded successfully {filename}"