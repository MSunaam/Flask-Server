def allowed_file(filename,ALLOWED_EXTENSIONS,appConfig,request):
    # Check filename and file size
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS and \
              request.content_length < appConfig['MAX_CONTENT_LENGTH']