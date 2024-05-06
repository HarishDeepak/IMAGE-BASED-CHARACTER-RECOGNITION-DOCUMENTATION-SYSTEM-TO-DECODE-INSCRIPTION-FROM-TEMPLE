from flask import Flask, render_template, request
from PIL import Image
import os
import pytesseract
from werkzeug.utils import secure_filename
import postProcess
app = Flask(__name__)

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def indexPage():
    return render_template('index.html')

def AddSpaces(text):

    ans = postProcess.Driver(text)
    return ans

@app.route("/Submit", methods=['POST'])
def submiting():
    if 'image' not in request.files:
        return 'No image part', 400
    image_file = request.files.get('image')
    if image_file.filename == '':
        return 'No selected file', 400

    if image_file:
        filename = secure_filename(image_file.filename)
        pathFile = UPLOAD_FOLDER + '/' + filename
        image_file.save(pathFile)
        ext_text = AddSpaces(tesseracProc(image_file))

    else:
        ext_text = "No image uploaded"
    
    return render_template('Submit.html', translated_text=ext_text, image_filename=image_file.filename)

os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata/'

def tesseracProc(image_file):
    ext=pytesseract.image_to_string(Image.open(image_file),lang="atam",config="--psm 6")
    return ext

if __name__ == '__main__':
    app.run(debug=True)



















